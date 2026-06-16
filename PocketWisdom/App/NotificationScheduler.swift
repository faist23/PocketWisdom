import Foundation
import UserNotifications

final class NotificationScheduler {
    static let shared = NotificationScheduler()
    private init() {}

    private let center = UNUserNotificationCenter.current()
    private let notificationHour = 9
    private let batchSize = 60
    private let refillThreshold = 7

    // Bump this whenever the notification payload format changes so existing
    // installs flush their pre-scheduled queue and re-schedule with the new
    // format. Version 1 retires the legacy batch (shipped 2026-05-13) whose
    // notifications carry no "cardID" in userInfo and therefore can't deep-link
    // to the quoted card when tapped.
    private let currentScheduleVersion = 1
    private let scheduleVersionKey = "notificationScheduleVersion"

    func requestAndSchedule() async {
        guard let granted = try? await center.requestAuthorization(options: [.alert, .sound]),
              granted else { return }
        scheduleFromAppGroups()
        UserDefaults.standard.set(currentScheduleVersion, forKey: scheduleVersionKey)
    }

    // One-time forced reschedule when the payload format version advances.
    // Unlike rescheduleIfNeeded(), this ignores the pending-count threshold:
    // legacy queues stay well above refillThreshold for weeks as they drain one
    // per day, so the normal refill path would never replace them in time.
    // Only runs (and only bumps the version) when notifications are authorized,
    // since an unauthorized install has nothing queued to migrate.
    func migrateScheduleIfNeeded() async {
        guard UserDefaults.standard.integer(forKey: scheduleVersionKey) < currentScheduleVersion else { return }
        let settings = await center.notificationSettings()
        guard settings.authorizationStatus == .authorized else { return }
        scheduleFromAppGroups()
        UserDefaults.standard.set(currentScheduleVersion, forKey: scheduleVersionKey)
    }

    // One-time prompt for users who completed onboarding before this feature shipped.
    // Fires on first app-active after the update; never prompts again regardless of outcome.
    func promptExistingUserIfNeeded() {
        let key = "hasPromptedForNotifications"
        guard !UserDefaults.standard.bool(forKey: key) else { return }
        UserDefaults.standard.set(true, forKey: key)
        Task { await requestAndSchedule() }
    }

    // Debug: fire a notification in `delay` seconds for the card immediately
    // after `appCurrentIndex` (matches what a real 9am notification would carry).
    // Long-press the "?" button in WisdomDeckView to trigger.
    func scheduleTestNotification(after delay: TimeInterval = 5) {
        Task {
            let settings = await center.notificationSettings()
            if settings.authorizationStatus != .authorized {
                guard let granted = try? await center.requestAuthorization(options: [.alert, .sound]),
                      granted else {
                    print("[PW] test notification: authorization denied")
                    return
                }
            }

            let defaults = UserDefaults(suiteName: AppGroupKeys.suiteName)
            let deckIDs = defaults?.stringArray(forKey: AppGroupKeys.shuffledDeckIDs) ?? []
            let currentIndex = defaults?.integer(forKey: AppGroupKeys.appCurrentIndex) ?? 0
            guard !deckIDs.isEmpty,
                  let url = Bundle.main.url(forResource: "wisdom", withExtension: "json"),
                  let data = try? Data(contentsOf: url),
                  let cards = try? JSONDecoder().decode([WisdomCard].self, from: data) else {
                print("[PW] test notification: could not load deck/cards")
                return
            }
            let cardsDict = Dictionary(uniqueKeysWithValues: cards.map { ($0.id.uuidString, $0) })
            let nextID = deckIDs[(currentIndex + 1) % deckIDs.count]
            guard let card = cardsDict[nextID] else {
                print("[PW] test notification: nextID \(nextID) not in cardsDict")
                return
            }

            let content = UNMutableNotificationContent()
            content.body = card.body
            if let author = card.author { content.subtitle = "— \(author)" }
            content.sound = .default
            content.userInfo = ["cardID": card.id.uuidString]

            let trigger = UNTimeIntervalNotificationTrigger(timeInterval: delay, repeats: false)
            let req = UNNotificationRequest(identifier: "pw-test-\(UUID().uuidString)", content: content, trigger: trigger)
            try? await center.add(req)
            print("[PW] test notification scheduled for cardID=\(card.id.uuidString) in \(delay)s")
        }
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
