//
//  PocketWisdomApp.swift
//  PocketWisdom
//

import SwiftUI

@main
struct PocketWisdomApp: App {

    @AppStorage("hasSeenOnboarding") private var hasSeenOnboarding = false
    @StateObject private var vm = WisdomViewModel()
    @Environment(\.scenePhase) private var scenePhase

    var body: some Scene {
        WindowGroup {
            Group {
                if hasSeenOnboarding {
                    WisdomDeckView(vm: vm)
                } else {
                    OnboardingView()
                }
            }
            .onOpenURL { url in
                handleDeepLink(url)
            }
        }
        .onChange(of: scenePhase) { _, newPhase in
            if newPhase == .active {
                vm.mergeWidgetSaves()
            }
        }
    }

    // MARK: - Deep link: pocketwisdom://card/{UUID}

    private func handleDeepLink(_ url: URL) {
        guard url.scheme == "pocketwisdom",
              url.host == "card",
              let cardID = url.pathComponents.last,
              !cardID.isEmpty else { return }
        vm.moveCardToNext(cardID: cardID)
    }
}
