//
//  WisdomDeckView.swift
//  PocketWisdom
//
//  Created by Craig Faist on 4/6/26.
//


import SwiftUI

struct WisdomDeckView: View {
    
    @StateObject private var vm = WisdomViewModel()
    
    var body: some View {
        TabView(selection: $vm.currentIndex) {
            ForEach(vm.cards.indices, id: \.self) { index in
                WisdomCardView(card: vm.cards[index])
                    .tag(index)
                    .padding()
            }
        }
        .tabViewStyle(.page(indexDisplayMode: .never))
    }
}