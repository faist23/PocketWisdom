//
//  WisdomViewModel.swift
//  PocketWisdom
//
//  Created by Craig Faist on 4/6/26.
//


import Foundation
internal import Combine

final class WisdomViewModel: ObservableObject {
    
    @Published var cards: [WisdomCard] = []
    @Published var currentIndex: Int = 0
    
    init() {
        cards = WisdomRepository.shared.cards
    }
    
    var currentCard: WisdomCard {
        cards[currentIndex]
    }
}
