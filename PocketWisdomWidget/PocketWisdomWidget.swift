//
//  PocketWisdomWidget.swift
//  PocketWisdomWidget
//

import WidgetKit
import SwiftUI
import AppIntents

// MARK: - Safe subscript

private extension Array {
    subscript(safe index: Int) -> Element? {
        indices.contains(index) ? self[index] : nil
    }
}

// MARK: - Card loading

private func loadAllCards() -> [WisdomCard] {
    guard let url = Bundle.main.url(forResource: "wisdom", withExtension: "json"),
          let data = try? Data(contentsOf: url) else { return [] }
    return (try? JSONDecoder().decode([WisdomCard].self, from: data)) ?? []
}

// MARK: - Timeline entry

struct WisdomEntry: TimelineEntry {
    let date: Date
    let card: WisdomCard?
    let isSaved: Bool
}

// MARK: - Timeline provider

struct WisdomTimelineProvider: TimelineProvider {

    func placeholder(in context: Context) -> WisdomEntry {
        WisdomEntry(date: .now, card: nil, isSaved: false)
    }

    func getSnapshot(in context: Context, completion: @escaping (WisdomEntry) -> Void) {
        let defaults = UserDefaults(suiteName: AppGroupKeys.suiteName)
        let savedIDs = Set(defaults?.stringArray(forKey: AppGroupKeys.savedCardIDs) ?? [])
        let card = loadAllCards().first
        let isSaved = card.map { savedIDs.contains($0.id.uuidString) } ?? false
        completion(WisdomEntry(date: .now, card: card, isSaved: isSaved))
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<WisdomEntry>) -> Void) {
        let defaults = UserDefaults(suiteName: AppGroupKeys.suiteName)
        let deckIDs = defaults?.stringArray(forKey: AppGroupKeys.shuffledDeckIDs) ?? []
        let savedIDs = Set(defaults?.stringArray(forKey: AppGroupKeys.savedCardIDs) ?? [])

        let allCards = loadAllCards()
        let cardsByID = Dictionary(uniqueKeysWithValues: allCards.map { ($0.id.uuidString, $0) })

        let deckCount = deckIDs.count

        // Reset index when deck size changes (new cards added via app update)
        let lastKnown = defaults?.integer(forKey: AppGroupKeys.lastKnownDeckCount) ?? 0
        var widgetIndex: Int
        if deckCount == 0 {
            widgetIndex = 0
        } else if deckCount != lastKnown {
            widgetIndex = deckCount - 1
            defaults?.set(deckCount, forKey: AppGroupKeys.lastKnownDeckCount)
        } else {
            // Stay on the current card if we're still within the 12-hour window.
            // If nextScheduledDate is nil (first run with this code), treat as "within
            // window" so a save-triggered reload still shows the same card filled.
            let nextScheduled = defaults?.object(forKey: WidgetKeys.nextScheduledDate) as? Date
            let withinWindow = nextScheduled.map { Date() < $0 } ?? true

            if withinWindow,
               let currentCardID = defaults?.string(forKey: AppGroupKeys.currentWidgetCardID),
               let cardPosition = deckIDs.firstIndex(of: currentCardID) {
                widgetIndex = cardPosition
            } else {
                widgetIndex = defaults?.integer(forKey: AppGroupKeys.widgetIndex) ?? (deckCount - 1)
            }
            // Clamp in case deck shrank
            widgetIndex = min(widgetIndex, max(0, deckCount - 1))
        }

        // Always include a Date() entry first so the widget shows a card immediately
        // when the timeline is refreshed — without it, WidgetKit keeps the previous
        // entry until the first future scheduled date arrives.
        let now = Date()
        let scheduledDates = nextScheduledDates(count: 3, from: now)
        let allDates = [now] + scheduledDates
        var entries: [WisdomEntry] = []

        if deckCount == 0 {
            // App Groups not yet populated — fall back to time-based bundle selection.
            let dayOrdinal = Calendar.current.ordinality(of: .day, in: .era, for: now) ?? 0
            for (i, date) in allDates.enumerated() {
                let card = allCards.isEmpty ? nil : allCards[(dayOrdinal * 2 + i) % allCards.count]
                entries.append(WisdomEntry(date: date, card: card, isSaved: false))
            }
        } else {
            // Store the next scheduled date before the loop so intent-triggered reloads
            // can detect they are within the same 12-hour window.
            if let nextDate = scheduledDates.first {
                defaults?.set(nextDate, forKey: WidgetKeys.nextScheduledDate)
            }

            var idx = widgetIndex

            for (i, date) in allDates.enumerated() {
                let cardID = deckIDs[safe: idx]
                let card = cardID.flatMap { cardsByID[$0] }
                let isSaved = cardID.map { savedIDs.contains($0) } ?? false
                entries.append(WisdomEntry(date: date, card: card, isSaved: isSaved))

                if i == 0 {
                    defaults?.set(cardID, forKey: AppGroupKeys.currentWidgetCardID)
                }

                idx = ((idx - 2) + deckCount) % deckCount
            }

            // Store post-loop idx for natural .atEnd advancement.
            defaults?.set(idx, forKey: AppGroupKeys.widgetIndex)
        }

        completion(Timeline(entries: entries, policy: .atEnd))
    }

    // Returns the next `count` scheduled refresh times (8 am and 8 pm, DST-safe).
    private func nextScheduledDates(count: Int, from now: Date) -> [Date] {
        let cal = Calendar.current
        var dates: [Date] = []
        var pivot = now

        while dates.count < count {
            var earliest: Date?
            for hour in [8, 20] {
                if let d = cal.nextDate(
                    after: pivot,
                    matching: DateComponents(hour: hour, minute: 0, second: 0),
                    matchingPolicy: .nextTime
                ) {
                    if earliest == nil || d < earliest! { earliest = d }
                }
            }
            let next = earliest ?? pivot.addingTimeInterval(43200)
            dates.append(next)
            pivot = next
        }
        return dates
    }
}

// MARK: - Widget internal keys (widget-only, not shared with main app)

private enum WidgetKeys {
    static let nextScheduledDate = "widgetNextScheduledDate"
}

// MARK: - URL helpers

private func deepLinkURL(for card: WisdomCard?) -> URL? {
    guard let card else { return nil }
    return URL(string: "pocketwisdom://card/\(card.id.uuidString)")
}

private func saveURL(for card: WisdomCard?) -> URL? {
    guard let card else { return nil }
    return URL(string: "pocketwisdom://save/\(card.id.uuidString)")
}

// MARK: - Widget view router

struct PocketWisdomWidgetView: View {
    var entry: WisdomEntry
    @Environment(\.widgetFamily) private var family

    var body: some View {
        switch family {
        case .systemSmall:
            SmallWidgetView(entry: entry)
        case .systemMedium:
            MediumWidgetView(entry: entry)
        case .accessoryRectangular:
            LockScreenWidgetView(entry: entry)
        default:
            SmallWidgetView(entry: entry)
        }
    }
}

// MARK: - Small widget

struct SmallWidgetView: View {
    let entry: WisdomEntry

    var body: some View {
        ZStack(alignment: .bottomTrailing) {
            VStack {
                Spacer()
                Text(entry.card?.body ?? "Open PocketWisdom for your daily card.")
                    .font(.caption)
                    .fontDesign(.serif)
                    .multilineTextAlignment(.center)
                    .lineLimit(5)
                    .padding(.horizontal, 4)
                Spacer()
            }
            .frame(maxWidth: .infinity)

            if let card = entry.card, !entry.isSaved, let url = saveURL(for: card) {
                Link(destination: url) {
                    Image(systemName: "bookmark")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }
                .padding(8)
                .accessibilityLabel("Save wisdom")
            } else if entry.isSaved {
                Image(systemName: "bookmark.fill")
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .padding(8)
            }
        }
        .containerBackground(.fill.tertiary, for: .widget)
        .widgetURL(deepLinkURL(for: entry.card))
    }
}

// MARK: - Medium widget

struct MediumWidgetView: View {
    let entry: WisdomEntry

    var body: some View {
        ZStack(alignment: .topTrailing) {
            ViewThatFits(in: .vertical) {
                mediumContent(showReflection: true)
                mediumContent(showReflection: false)
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .padding(.horizontal, 20)
            .padding(.vertical, 12)

            if let card = entry.card, !entry.isSaved, let url = saveURL(for: card) {
                Link(destination: url) {
                    Image(systemName: "bookmark")
                        .font(.footnote)
                        .foregroundStyle(.secondary)
                }
                .padding(8)
                .accessibilityLabel("Save wisdom")
            } else if entry.isSaved {
                Image(systemName: "bookmark.fill")
                    .font(.footnote)
                    .foregroundStyle(.secondary)
                    .padding(8)
            }
        }
        .containerBackground(.fill.tertiary, for: .widget)
        .widgetURL(deepLinkURL(for: entry.card))
    }

    @ViewBuilder
    private func mediumContent(showReflection: Bool) -> some View {
        VStack(spacing: 4) {
            Text(entry.card?.body ?? "Open PocketWisdom for your daily card.")
                .font(.subheadline)
                .fontDesign(.serif)
                .multilineTextAlignment(.center)
                .fixedSize(horizontal: false, vertical: true)

            if let author = entry.card?.author {
                Text("— \(author)")
                    .font(.caption2)
                    .foregroundStyle(.tertiary)
                    .multilineTextAlignment(.center)
                    .padding(.top, 2)
            }

            if showReflection, let reflection = entry.card?.reflection {
                Text(reflection)
                    .font(.caption)
                    .foregroundStyle(.secondary)
                    .multilineTextAlignment(.center)
                    .padding(.top, 4)
                    .fixedSize(horizontal: false, vertical: true)
            }
        }
    }
}

// MARK: - Lock screen widget

struct LockScreenWidgetView: View {
    let entry: WisdomEntry

    var body: some View {
        HStack(alignment: .center, spacing: 6) {
            Text(entry.card?.body ?? "Open PocketWisdom")
                .font(.caption)
                .fontWeight(.medium)
                .lineLimit(2)

            Spacer(minLength: 0)

            if let card = entry.card, !entry.isSaved, let url = saveURL(for: card) {
                Link(destination: url) {
                    Image(systemName: "bookmark")
                        .font(.caption2)
                }
                .accessibilityLabel("Save wisdom")
            } else if entry.isSaved {
                Image(systemName: "bookmark.fill")
                    .font(.caption2)
            }
        }
        .containerBackground(.fill.tertiary, for: .widget)
        .widgetURL(deepLinkURL(for: entry.card))
    }
}

// MARK: - Widget declarations

struct PocketWisdomHomeWidget: Widget {
    let kind = "PocketWisdomHomeWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: WisdomTimelineProvider()) { entry in
            PocketWisdomWidgetView(entry: entry)
        }
        .configurationDisplayName("PocketWisdom")
        .description("A new card of wisdom, twice a day.")
        .supportedFamilies([.systemSmall, .systemMedium])
    }
}

struct PocketWisdomLockScreenWidget: Widget {
    let kind = "PocketWisdomLockScreenWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: WisdomTimelineProvider()) { entry in
            PocketWisdomWidgetView(entry: entry)
        }
        .configurationDisplayName("PocketWisdom")
        .description("Wisdom on your lock screen.")
        .supportedFamilies([.accessoryRectangular])
    }
}
