//
//  WisdomViewModel.swift
//  PocketWisdom
//
//  Created by Craig Faist on 4/6/26.
//

import Foundation
import Combine
import SwiftUI

final class WisdomViewModel: ObservableObject {
    
    @Published var deck: [WisdomCard] = []
    @Published var savedCards: [WisdomCard] = []
    
    @Published var currentIndex: Int {
        didSet {
            UserDefaults.standard.set(currentIndex, forKey: "currentIndex")
        }
    }
    
    private let repository = WisdomRepository.shared
    
    private let savedCardsFileURL: URL = {
        let docs = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
        return docs.appendingPathComponent("saved_cards.json")
    }()
    
    init() {
        self.currentIndex = UserDefaults.standard.integer(forKey: "currentIndex")
        setupDeck()
        loadSavedCards()
    }
    
    var currentCard: WisdomCard? {
        guard !deck.isEmpty, currentIndex >= 0, currentIndex < deck.count else { return nil }
        return deck[currentIndex]
    }
    
    private func setupDeck() {
        let allCards = repository.cards
        let defaults = UserDefaults.standard
        
        let savedDeckIDs = defaults.stringArray(forKey: "shuffledDeckIDs")
        
        if let savedIDs = savedDeckIDs, !savedIDs.isEmpty {
            // Restore deck from saved IDs, filtering out any that no longer exist
            let cardsDict = Dictionary(uniqueKeysWithValues: allCards.map { ($0.id.uuidString, $0) })
            let restoredDeck = savedIDs.compactMap { cardsDict[$0] }
            
            // If the restored deck is missing some new cards, we should append them
            let newCards = allCards.filter { !savedIDs.contains($0.id.uuidString) }
            self.deck = restoredDeck + newCards.shuffled()
            
            // Save back if we added new cards
            if !newCards.isEmpty {
                let updatedIDs = self.deck.map { $0.id.uuidString }
                defaults.set(updatedIDs, forKey: "shuffledDeckIDs")
            }
        } else {
            // First launch or missing data: shuffle all cards and save
            self.deck = allCards.shuffled()
            let newIDs = self.deck.map { $0.id.uuidString }
            defaults.set(newIDs, forKey: "shuffledDeckIDs")
            self.currentIndex = 0
        }
    }
    
    // MARK: - Saved Cards Logic
    
    func isSaved(_ card: WisdomCard) -> Bool {
        savedCards.contains { $0.id == card.id }
    }
    
    func toggleSave(for card: WisdomCard) {
        if isSaved(card) {
            savedCards.removeAll { $0.id == card.id }
        } else {
            savedCards.insert(card, at: 0) // Prepend newest
        }
        persistSavedCards()
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
