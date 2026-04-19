//
//  WisdomViewModel.swift
//  PocketWisdom
//

import Foundation
import Combine
import SwiftUI
import WidgetKit

final class WisdomViewModel: ObservableObject {

    @Published var deck: [WisdomCard] = []
    @Published var savedCards: [WisdomCard] = []

    @Published var currentIndex: Int {
        didSet {
            appGroupDefaults?.set(currentIndex, forKey: AppGroupKeys.appCurrentIndex)
            notifyWidgetIfNeeded()
        }
    }

    private let repository = WisdomRepository.shared

    // MARK: - Persistence

    private let appGroupDefaults: UserDefaults? = UserDefaults(suiteName: AppGroupKeys.suiteName)

    private let savedCardsFileURL: URL = {
        let docs = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
        return docs.appendingPathComponent("saved_cards.json")
    }()

    // MARK: - Widget reload throttle (leading, max once per 5 seconds)

    private var lastWidgetReload: Date = .distantPast

    private func notifyWidgetIfNeeded() {
        let now = Date()
        guard now.timeIntervalSince(lastWidgetReload) >= 5 else { return }
        lastWidgetReload = now
        WidgetCenter.shared.reloadAllTimelines()
    }

    // MARK: - Init

    init() {
        // Read currentIndex from App Groups if migration has already run;
        // fall back to standard UserDefaults for the pre-migration value.
        let hasMigrated = UserDefaults.standard.bool(forKey: "hasMigratedToAppGroups")
        if hasMigrated {
            self.currentIndex = appGroupDefaults?.integer(forKey: AppGroupKeys.appCurrentIndex) ?? 0
        } else {
            self.currentIndex = UserDefaults.standard.integer(forKey: "currentIndex")
        }
        setupDeck()
        if !hasMigrated {
            migrateToAppGroups()
        }
        loadSavedCards()
    }

    // MARK: - One-time migration from standard UserDefaults → App Groups

    private func migrateToAppGroups() {
        let standard = UserDefaults.standard
        guard let appGroupDefaults else { return }

        // Copy shuffledDeckIDs
        if let ids = standard.stringArray(forKey: "shuffledDeckIDs") {
            appGroupDefaults.set(ids, forKey: AppGroupKeys.shuffledDeckIDs)
        }

        // Copy savedCardIDs from Documents JSON
        let savedIDs = savedCards.map { $0.id.uuidString }
        appGroupDefaults.set(savedIDs, forKey: AppGroupKeys.savedCardIDs)

        // Copy currentIndex
        appGroupDefaults.set(currentIndex, forKey: AppGroupKeys.appCurrentIndex)

        // Mark migration complete
        standard.set(true, forKey: "hasMigratedToAppGroups")

        // Remove legacy standard keys
        standard.removeObject(forKey: "currentIndex")
        standard.removeObject(forKey: "shuffledDeckIDs")
    }

    // MARK: - Deck setup

    var currentCard: WisdomCard? {
        guard !deck.isEmpty, currentIndex >= 0, currentIndex < deck.count else { return nil }
        return deck[currentIndex]
    }

    private func setupDeck() {
        let allCards = repository.cards
        let defaults = appGroupDefaults ?? UserDefaults.standard

        let savedDeckIDs = defaults.stringArray(forKey: AppGroupKeys.shuffledDeckIDs)
            ?? UserDefaults.standard.stringArray(forKey: "shuffledDeckIDs")

        if let savedIDs = savedDeckIDs, !savedIDs.isEmpty {
            let cardsDict = Dictionary(uniqueKeysWithValues: allCards.map { ($0.id.uuidString, $0) })
            let restoredDeck = savedIDs.compactMap { cardsDict[$0] }

            let newCards = allCards.filter { !savedIDs.contains($0.id.uuidString) }

            if !newCards.isEmpty {
                let splitIndex = min(max(self.currentIndex + 1, 0), restoredDeck.count)
                let viewedCards = Array(restoredDeck.prefix(upTo: splitIndex))
                var unviewedCards = Array(restoredDeck.suffix(from: splitIndex))
                unviewedCards.append(contentsOf: newCards)
                unviewedCards.shuffle()
                self.deck = viewedCards + unviewedCards
            } else {
                self.deck = restoredDeck
            }
        } else {
            self.deck = allCards.shuffled()
            self.currentIndex = 0
        }

        // Always write the current deck order to App Groups
        let deckIDs = self.deck.map { $0.id.uuidString }
        appGroupDefaults?.set(deckIDs, forKey: AppGroupKeys.shuffledDeckIDs)

        // Reload widget timeline now that App Groups has fresh deck data.
        // Done unconditionally (no throttle) because this only runs during init.
        WidgetCenter.shared.reloadAllTimelines()
    }

    // MARK: - Deep link: move a card to currentIndex + 1

    /// Moves the card with the given UUID to position currentIndex + 1 in the deck,
    /// so the user's next swipe reveals the tapped widget card.
    ///
    /// Off-by-one note: after removing fromIndex, if fromIndex < targetIndex,
    /// the target position shifts left by 1.
    func moveCardToNext(cardID: String) {
        guard var deckIDs = appGroupDefaults?.stringArray(forKey: AppGroupKeys.shuffledDeckIDs),
              let fromIndex = deckIDs.firstIndex(of: cardID) else { return }

        let targetIndex = min(currentIndex + 1, deckIDs.count - 1)
        guard fromIndex != targetIndex else { return }

        deckIDs.remove(at: fromIndex)
        let adjustedTarget = fromIndex < targetIndex ? targetIndex - 1 : targetIndex
        deckIDs.insert(cardID, at: adjustedTarget)

        appGroupDefaults?.set(deckIDs, forKey: AppGroupKeys.shuffledDeckIDs)

        // Rebuild deck array from updated order
        let cardsDict = Dictionary(uniqueKeysWithValues: repository.cards.map { ($0.id.uuidString, $0) })
        self.deck = deckIDs.compactMap { cardsDict[$0] }
    }

    // MARK: - Scene foreground: merge widget-saved cards

    /// Call this on scenePhase == .active.
    /// Re-reads App Groups savedCardIDs fresh (not cached) and Set-unions with local saved list.
    func mergeWidgetSaves() {
        guard let appGroupDefaults else { return }
        let widgetSavedIDs = Set(appGroupDefaults.stringArray(forKey: AppGroupKeys.savedCardIDs) ?? [])
        let localSavedIDs = Set(savedCards.map { $0.id.uuidString })
        let merged = widgetSavedIDs.union(localSavedIDs)

        let cardsDict = Dictionary(uniqueKeysWithValues: repository.cards.map { ($0.id.uuidString, $0) })

        // Preserve insertion order: local cards first (prepend), then new widget-saved cards appended
        var mergedCards = savedCards
        for id in merged.subtracting(localSavedIDs) {
            if let card = cardsDict[id] {
                mergedCards.append(card)
            }
        }

        self.savedCards = mergedCards

        // Write merged result back to both App Groups and Documents
        let mergedIDs = mergedCards.map { $0.id.uuidString }
        appGroupDefaults.set(mergedIDs, forKey: AppGroupKeys.savedCardIDs)
        persistSavedCards()
    }

    // MARK: - Saved cards

    func isSaved(_ card: WisdomCard) -> Bool {
        savedCards.contains { $0.id == card.id }
    }

    func toggleSave(for card: WisdomCard) {
        if isSaved(card) {
            savedCards.removeAll { $0.id == card.id }
        } else {
            savedCards.insert(card, at: 0)
        }
        persistSavedCards()
        syncSavedCardsToAppGroups()
    }

    private func syncSavedCardsToAppGroups() {
        let ids = savedCards.map { $0.id.uuidString }
        appGroupDefaults?.set(ids, forKey: AppGroupKeys.savedCardIDs)
    }

    private func loadSavedCards() {
        guard let data = try? Data(contentsOf: savedCardsFileURL),
              let savedIDs = try? JSONDecoder().decode([String].self, from: data) else {
            return
        }
        let cardsDict = Dictionary(uniqueKeysWithValues: repository.cards.map { ($0.id.uuidString, $0) })
        self.savedCards = savedIDs.compactMap { cardsDict[$0] }
    }

    private func persistSavedCards() {
        let savedIDs = savedCards.map { $0.id.uuidString }
        if let data = try? JSONEncoder().encode(savedIDs) {
            try? data.write(to: savedCardsFileURL, options: .atomic)
        }
    }
}
