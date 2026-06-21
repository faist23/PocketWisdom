//
//  PocketWisdomApp.swift
//  PocketWisdom
//

import SwiftUI
import WidgetKit
import UserNotifications
import Combine

@main
struct PocketWisdomApp: App {

    @AppStorage("hasSeenOnboarding") private var hasSeenOnboarding = false
    @StateObject private var vm = WisdomViewModel()
    @Environment(\.scenePhase) private var scenePhase
    @State private var didSaveViaDeepLink = false
    @StateObject private var notificationDelegate = NotificationDelegate.shared

    init() {
        UNUserNotificationCenter.current().delegate = NotificationDelegate.shared
    }

    var body: some Scene {
        WindowGroup {
            Group {
                if hasSeenOnboarding {
                    WisdomDeckView(vm: vm)
                    // Temporarily replace the default navigation structure with the marketing generator
//                    MarketingView()
                } else {
                    OnboardingView()
                }
            }
            .onOpenURL { url in
                handleDeepLink(url)
            }
            .onChange(of: notificationDelegate.pendingCardID, initial: true) { _, cardID in
                guard let cardID = cardID else { return }
                vm.jumpToCard(cardID: cardID)
                notificationDelegate.pendingCardID = nil
            }
        }
        .onChange(of: scenePhase) { _, newPhase in
            if newPhase == .active {
                vm.mergeWidgetSaves()
                if hasSeenOnboarding {
                    NotificationScheduler.shared.promptExistingUserIfNeeded()
                }
                Task {
                    await NotificationScheduler.shared.migrateScheduleIfNeeded()
                    await NotificationScheduler.shared.rescheduleIfNeeded()
                }
            } else if newPhase == .background {
                // Reload widget on background for normal use (swipe through cards, etc).
                // Skip if saveCard() already fired a reload via deep link — that reload
                // is the authoritative one (written + synchronized before firing).
                // A second reload here would be coalesced by WidgetKit on iOS 26 and
                // could race with the saveCard() reload's getTimeline execution.
                if !didSaveViaDeepLink {
                    WidgetCenter.shared.reloadAllTimelines()
                }
                didSaveViaDeepLink = false
            }
        }
    }

    // MARK: - Deep links

    private func handleDeepLink(_ url: URL) {
        guard url.scheme == "pocketwisdom",
              let host = url.host,
              let cardID = url.pathComponents.last,
              !cardID.isEmpty else { return }

        let normalizedCardID = cardID.uppercased()

        switch host {
        case "card":
            vm.jumpToCard(cardID: normalizedCardID)
        case "save":
            didSaveViaDeepLink = true
            vm.saveCard(cardID: normalizedCardID)
        default:
            break
        }
    }
}

// MARK: - Notification Delegate

final class NotificationDelegate: NSObject, UNUserNotificationCenterDelegate, ObservableObject {
    static let shared = NotificationDelegate()

    @Published var pendingCardID: String?

    private override init() {
        super.init()
    }

    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                didReceive response: UNNotificationResponse,
                                withCompletionHandler completionHandler: @escaping () -> Void) {
        if let cardID = response.notification.request.content.userInfo["cardID"] as? String {
            DispatchQueue.main.async {
                self.pendingCardID = cardID
            }
        }
        completionHandler()
    }

    // Show the banner when the app is foregrounded so the user can still
    // tap the notification to jump to the card.
    func userNotificationCenter(_ center: UNUserNotificationCenter,
                                willPresent notification: UNNotification,
                                withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {
        completionHandler([.banner, .sound, .list])
    }
}
