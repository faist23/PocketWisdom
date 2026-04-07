//
//  WisdomRepository.swift
//  PocketWisdom
//
//  Created by Craig Faist on 4/6/26.
//


import Foundation

final class WisdomRepository {
    
    static let shared = WisdomRepository()
    
    private(set) var cards: [WisdomCard] = []
    
    private init() {
        loadLocalData()
    }
    
    private func loadLocalData() {
        guard let url = Bundle.main.url(forResource: "wisdom", withExtension: "json"),
              let data = try? Data(contentsOf: url),
              let decoded = try? JSONDecoder().decode([WisdomCard].self, from: data) else {
            print("Failed to load wisdom.json")
            return
        }
        
        self.cards = decoded.shuffled()
    }
}