import Foundation
import UserNotifications

final class NotificationScheduler {
    static let shared = NotificationScheduler()
    private init() {}

    private let center = UNUserNotificationCenter.current()
    private let notificationHour = 9
    private let batchSize = 60
    private let refillThreshold = 7

    func requestAndSchedule() async {
        guard let granted = try? await center.requestAuthorization(options: [.alert, .sound]),
              granted else { return }
        scheduleFromAppGroups()
    }

    // One-time prompt for users who completed onboarding before this feature shipped.
    // Fires on first app-active after the update; never prompts again regardless of outcome.
    func promptExistingUserIfNeeded() {
        let key = "hasPromptedForNotifications"
        guard !UserDefaults.standard.bool(forKey: key) else { return }
        UserDefaults.standard.set(true, forKey: key)
        Task { await requestAndSchedule() }
    }

    func rescheduleIfNeeded() async {
        let settings = await center.notificationSettings()
        guard settings.authorizationStatus == .authorized else { return }
        let pending = await center.pendingNotificationRequests()
        guard pending.count < refillThreshold else { return }
        scheduleFromAppGroups()
    }

    private func scheduleFromAppGroups() {
        let defaults = UserDefaults(suiteName: AppGroupKeys.suiteName)
        let deckIDs = defaults?.stringArray(forKey: AppGroupKeys.shuffledDeckIDs) ?? []
        let currentIndex = defaults?.integer(forKey: AppGroupKeys.appCurrentIndex) ?? 0

        guard !deckIDs.isEmpty,
              let url = Bundle.main.url(forResource: "wisdom", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let cards = try? JSONDecoder().decode([WisdomCard].self, from: data) else { return }

        let cardsDict = Dictionary(uniqueKeysWithValues: cards.map { ($0.id.uuidString, $0) })
        let deckCount = deckIDs.count
        let today = Calendar.current.startOfDay(for: Date())

        center.removeAllPendingNotificationRequests()

        for i in 0..<batchSize {
            let deckIdx = (currentIndex + 1 + i) % deckCount
            let cardID = deckIDs[deckIdx]
            guard let card = cardsDict[cardID] else { continue }

            guard let fireDate = Calendar.current.date(byAdding: .day, value: i + 1, to: today) else { continue }

            var components = Calendar.current.dateComponents([.year, .month, .day], from: fireDate)
            components.hour = notificationHour
            components.minute = 0
            components.second = 0

            let content = UNMutableNotificationContent()
            content.body = card.body
            if let author = card.author {
                content.subtitle = "— \(author)"
            }
            content.sound = .default
            content.userInfo = ["cardID": card.id.uuidString]

            let trigger = UNCalendarNotificationTrigger(dateMatching: components, repeats: false)
            let request = UNNotificationRequest(
                identifier: "pw-wisdom-\(i)",
                content: content,
                trigger: trigger
            )
            center.add(request)
        }
    }
}
