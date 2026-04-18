//
//  PocketWisdomWidget.swift
//  PocketWisdomWidget
//
//  Timeline provider + view for .systemSmall, .systemMedium, .accessoryRectangular.
//
//  Two-pointer deck system:
//
//  deck (shuffled, N cards):
//  [0 .... appCurrentIndex | unseen pool | widgetIndex .... N-1]
//   (app, →)                              (widget, ←)
//
//  widgetIndex starts at deck.count-1 and decrements by 2 per timeline generation.
//  lastKnownDeckCount sentinel: if deck grows (new cards added), reset widgetIndex = deckCount-1.
//

import WidgetKit
import SwiftUI
import AppIntents

// MARK: - Timeline Entry

struct WisdomEntry: TimelineEntry {
    let date: Date
    let card: WisdomCard?
    let isSaved: Bool

    // Empty / placeholder
    static var placeholder: WisdomEntry {
        WisdomEntry(date: .now, card: nil, isSaved: false)
    }
}

// MARK: - Timeline Provider

struct WisdomTimelineProvider: TimelineProvider {

    func placeholder(in context: Context) -> WisdomEntry {
        .placeholder
    }

    func getSnapshot(in context: Context, completion: @escaping (WisdomEntry) -> Void) {
        completion(makeEntry(for: .now))
    }

    func getTimeline(in context: Context, completion: @escaping (Timeline<WisdomEntry>) -> Void) {
        let defaults = UserDefaults(suiteName: AppGroupKeys.suiteName)

        // Resolve shuffled deck IDs
        guard let deckIDs = defaults?.stringArray(forKey: AppGroupKeys.shuffledDeckIDs),
              !deckIDs.isEmpty else {
            // App hasn't launched yet — show placeholder, try again in 1 hour
            let entry = WisdomEntry.placeholder
            let next = Calendar.current.date(byAdding: .hour, value: 1, to: .now) ?? .now
            completion(Timeline(entries: [entry], policy: .after(next)))
            return
        }

        let deckCount = deckIDs.count

        // Deck growth sentinel: reset widgetIndex if deck has grown
        var widgetIndex = defaults?.integer(forKey: AppGroupKeys.widgetIndex) ?? 0
        let lastKnownCount = defaults?.integer(forKey: AppGroupKeys.lastKnownDeckCount) ?? 0

        if widgetIndex == 0 || deckCount != lastKnownCount {
            widgetIndex = deckCount - 1
            defaults?.set(deckCount, forKey: AppGroupKeys.lastKnownDeckCount)
        }

        // Collision guard: keep widgetIndex at least 20 cards ahead of appCurrentIndex
        let appCurrentIndex = defaults?.integer(forKey: AppGroupKeys.appCurrentIndex) ?? 0
        if widgetIndex <= appCurrentIndex + 20 {
            // Fallback: pick randomly from unseen pool
            let unseenRange = (appCurrentIndex + 1)..<deckCount
            if !unseenRange.isEmpty {
                widgetIndex = unseenRange.randomElement() ?? deckCount - 1
            }
        }

        // Load the full card library for lookup
        let allCards = loadAllCards()
        let cardDict = Dictionary(uniqueKeysWithValues: allCards.map { ($0.id.uuidString, $0) })
        let savedIDs = Set(defaults?.stringArray(forKey: AppGroupKeys.savedCardIDs) ?? [])

        // Morning entry: deck[widgetIndex], Evening entry: deck[widgetIndex - 1]
        let morningCardID = deckIDs[safe: widgetIndex]
        let eveningCardID = deckIDs[safe: widgetIndex - 1]

        let morningCard = morningCardID.flatMap { cardDict[$0] }
        let eveningCard = eveningCardID.flatMap { cardDict[$0] }

        // Write current widget card ID for deep-link use
        if let id = morningCardID {
            defaults?.set(id, forKey: AppGroupKeys.currentWidgetCardID)
        }

        // Decrement widget pointer by 2
        let newWidgetIndex = max(0, widgetIndex - 2)
        defaults?.set(newWidgetIndex, forKey: AppGroupKeys.widgetIndex)

        // Build timeline: morning 8am, evening 8pm, using Calendar for DST safety
        let calendar = Calendar.current
        let now = Date()

        func nextOccurrence(hour: Int) -> Date {
            var components = calendar.dateComponents([.year, .month, .day], from: now)
            components.hour = hour
            components.minute = 0
            components.second = 0
            let candidate = calendar.date(from: components) ?? now
            return candidate > now ? candidate : calendar.date(byAdding: .day, value: 1, to: candidate) ?? candidate
        }

        let morningDate = nextOccurrence(hour: 8)
        let eveningDate = nextOccurrence(hour: 20)

        var entries: [WisdomEntry] = []

        if morningDate < eveningDate {
            entries.append(WisdomEntry(
                date: morningDate,
                card: morningCard,
                isSaved: morningCardID.map { savedIDs.contains($0) } ?? false
            ))
            entries.append(WisdomEntry(
                date: eveningDate,
                card: eveningCard,
                isSaved: eveningCardID.map { savedIDs.contains($0) } ?? false
            ))
        } else {
            entries.append(WisdomEntry(
                date: eveningDate,
                card: eveningCard,
                isSaved: eveningCardID.map { savedIDs.contains($0) } ?? false
            ))
            entries.append(WisdomEntry(
                date: morningDate,
                card: morningCard,
                isSaved: morningCardID.map { savedIDs.contains($0) } ?? false
            ))
        }

        // .atEnd: iOS schedules the next timeline after the last entry
        completion(Timeline(entries: entries, policy: .atEnd))
    }

    // MARK: - Helpers

    private func makeEntry(for date: Date) -> WisdomEntry {
        let defaults = UserDefaults(suiteName: AppGroupKeys.suiteName)
        guard let deckIDs = defaults?.stringArray(forKey: AppGroupKeys.shuffledDeckIDs),
              !deckIDs.isEmpty else {
            return .placeholder
        }
        let widgetIndex = defaults?.integer(forKey: AppGroupKeys.widgetIndex) ?? 0
        let allCards = loadAllCards()
        let cardDict = Dictionary(uniqueKeysWithValues: allCards.map { ($0.id.uuidString, $0) })
        let savedIDs = Set(defaults?.stringArray(forKey: AppGroupKeys.savedCardIDs) ?? [])
        let cardID = deckIDs[safe: widgetIndex]
        let card = cardID.flatMap { cardDict[$0] }
        return WisdomEntry(date: date, card: card, isSaved: cardID.map { savedIDs.contains($0) } ?? false)
    }

    private func loadAllCards() -> [WisdomCard] {
        guard let url = Bundle.main.url(forResource: "wisdom", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let cards = try? JSONDecoder().decode([WisdomCard].self, from: data) else {
            return []
        }
        return cards
    }
}

// MARK: - Root Widget View (family branch)

struct PocketWisdomWidgetView: View {
    @Environment(\.widgetFamily) var family
    var entry: WisdomEntry

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

// MARK: - .systemSmall

struct SmallWidgetView: View {
    var entry: WisdomEntry

    var body: some View {
        if let card = entry.card {
            ZStack(alignment: .bottomTrailing) {
                VStack(spacing: 6) {
                    Spacer(minLength: 0)

                    Text(card.body)
                        .font(.system(.caption, design: .serif))
                        .multilineTextAlignment(.center)
                        .lineLimit(3)
                        .foregroundStyle(.primary)

                    if let author = card.author {
                        Text(author)
                            .font(.system(.caption2, design: .serif))
                            .italic()
                            .multilineTextAlignment(.center)
                            .foregroundStyle(.secondary)
                    }

                    Spacer(minLength: 0)
                }
                .padding(12)

                // Bookmark button — bottom-trailing
                Button(intent: SaveWisdomCardIntent(cardID: card.id.uuidString)) {
                    Image(systemName: entry.isSaved ? "bookmark.fill" : "bookmark")
                        .font(.system(size: 10))
                        .foregroundStyle(.secondary.opacity(entry.isSaved ? 1 : 0.4))
                }
                .buttonStyle(.plain)
                .padding(10)
                .accessibilityLabel(entry.isSaved ? "Saved" : "Save")
            }
            .containerBackground(.fill, for: .widget)
            .widgetURL(URL(string: "pocketwisdom://card/\(card.id.uuidString)"))
            .accessibilityElement(children: .contain)
            .accessibilityLabel("\(card.body)\(card.author.map { ", \($0)" } ?? "")")
            .accessibilityHint("Opens PocketWisdom to this card")
        } else {
            // Empty state (App Groups not yet populated)
            Text("Open PocketWisdom to begin")
                .font(.system(.caption, design: .serif))
                .multilineTextAlignment(.center)
                .foregroundStyle(.secondary)
                .padding(12)
                .containerBackground(.fill, for: .widget)
        }
    }
}

// MARK: - .systemMedium

struct MediumWidgetView: View {
    var entry: WisdomEntry

    var body: some View {
        if let card = entry.card {
            ZStack(alignment: .bottomTrailing) {
                VStack(alignment: .leading, spacing: 8) {
                    Text(card.body)
                        .font(.system(.subheadline, design: .serif))
                        .multilineTextAlignment(.leading)
                        .foregroundStyle(.primary)

                    if let reflection = card.reflection {
                        Divider()
                        Text(reflection)
                            .font(.system(.caption, design: .serif))
                            .italic()
                            .lineLimit(2)
                            .foregroundStyle(.secondary)
                    }

                    Spacer(minLength: 0)

                    if let author = card.author {
                        Text(author)
                            .font(.system(.caption, design: .serif))
                            .italic()
                            .foregroundStyle(.secondary)
                    }
                }
                .padding(16)

                // Bookmark button — bottom-trailing
                Button(intent: SaveWisdomCardIntent(cardID: card.id.uuidString)) {
                    Image(systemName: entry.isSaved ? "bookmark.fill" : "bookmark")
                        .font(.system(size: 12))
                        .foregroundStyle(.secondary.opacity(entry.isSaved ? 1 : 0.4))
                }
                .buttonStyle(.plain)
                .padding(12)
                .accessibilityLabel(entry.isSaved ? "Saved" : "Save")
            }
            .containerBackground(.fill, for: .widget)
            .widgetURL(URL(string: "pocketwisdom://card/\(card.id.uuidString)"))
            .accessibilityElement(children: .contain)
            .accessibilityLabel("\(card.body)\(card.author.map { ", \($0)" } ?? "")")
            .accessibilityHint("Opens PocketWisdom to this card")
        } else {
            Text("Open PocketWisdom to begin")
                .font(.system(.caption, design: .serif))
                .multilineTextAlignment(.center)
                .foregroundStyle(.secondary)
                .padding(16)
                .containerBackground(.fill, for: .widget)
        }
    }
}

// MARK: - .accessoryRectangular (Lock Screen)

struct LockScreenWidgetView: View {
    var entry: WisdomEntry

    var body: some View {
        if let card = entry.card {
            VStack(alignment: .leading, spacing: 2) {
                Text(card.body)
                    .font(.system(.caption, weight: .medium))
                    .lineLimit(2)
                    .foregroundStyle(.primary)

                HStack {
                    if let author = card.author {
                        Text(author)
                            .font(.caption2)
                            .foregroundStyle(.secondary)
                    }
                    Spacer()
                    // Bookmark button — lock screen (test on device: fires after unlock)
                    Button(intent: SaveWisdomCardIntent(cardID: card.id.uuidString)) {
                        Image(systemName: entry.isSaved ? "bookmark.fill" : "bookmark")
                            .font(.system(size: 10))
                    }
                    .buttonStyle(.plain)
                    .accessibilityLabel(entry.isSaved ? "Saved" : "Save")
                }
            }
            .containerBackground(.fill, for: .widget)
            .widgetURL(URL(string: "pocketwisdom://card/\(card.id.uuidString)"))
            .accessibilityElement(children: .contain)
            .accessibilityLabel("\(card.body)\(card.author.map { ", \($0)" } ?? "")")
            .accessibilityHint("Opens PocketWisdom to this card")
        } else {
            Text("Open PocketWisdom to begin")
                .font(.caption2)
                .foregroundStyle(.secondary)
                .containerBackground(.fill, for: .widget)
        }
    }
}

// MARK: - Safe array subscript

private extension Array {
    subscript(safe index: Int) -> Element? {
        indices.contains(index) ? self[index] : nil
    }
}
