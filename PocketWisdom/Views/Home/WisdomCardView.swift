//
//  WisdomCardView.swift
//  PocketWisdom
//
//  Created by Craig Faist on 4/6/26.
//


import SwiftUI

struct WisdomCardView: View {
    
    let card: WisdomCard
    @State private var showReflection = false
    
    var body: some View {
        VStack(spacing: 24) {
            
            Text(card.title)
                .font(.system(.title2, design: .serif))
                .foregroundColor(.secondary)
            
            Text(card.body)
                .font(.system(.title3, design: .serif))
                .multilineTextAlignment(.center)
            
            if showReflection, let reflection = card.reflection {
                Text(reflection)
                    .font(.body)
                    .foregroundColor(.gray)
                    .transition(.opacity)
            }
        }
        .padding(32)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color(.systemGroupedBackground))
        .onTapGesture {
            withAnimation {
                showReflection.toggle()
            }
        }
    }
}