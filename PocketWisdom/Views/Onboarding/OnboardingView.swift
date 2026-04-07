//
//  OnboardingView.swift
//  PocketWisdom
//

import SwiftUI

struct OnboardingView: View {
    @AppStorage("hasSeenOnboarding") private var hasSeenOnboarding = false
    @State private var currentStep = 0
    
    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()
            
            TabView(selection: $currentStep) {
                // Screen 1
                VStack(spacing: 32) {
                    Text("This is not a social app.")
                        .font(.system(.title, design: .serif))
                        .multilineTextAlignment(.center)
                        .foregroundColor(.primary)
                }
                .padding(40)
                .tag(0)
                
                // Screen 2
                VStack(spacing: 32) {
                    Text("No accounts.\nNo tracking.")
                        .font(.system(.title, design: .serif))
                        .multilineTextAlignment(.center)
                        .foregroundColor(.primary)
                }
                .padding(40)
                .tag(1)
                
                // Screen 3
                VStack(spacing: 64) {
                    Text("Just a quiet moment,\nwhen you need one.")
                        .font(.system(.title, design: .serif))
                        .multilineTextAlignment(.center)
                        .foregroundColor(.primary)
                    
                    VStack(spacing: 16) {
                        HStack(spacing: 16) {
                            Image(systemName: "arrow.left.and.right")
                                .foregroundColor(.secondary)
                            Text("Swipe for next card")
                                .font(.system(.body, design: .serif))
                                .foregroundColor(.secondary)
                        }
                        
                        HStack(spacing: 16) {
                            Image(systemName: "hand.tap")
                                .foregroundColor(.secondary)
                            Text("Tap to reflect")
                                .font(.system(.body, design: .serif))
                                .foregroundColor(.secondary)
                        }
                        
                        HStack(spacing: 16) {
                            Image(systemName: "bookmark")
                                .foregroundColor(.secondary)
                            Text("Long press to save")
                                .font(.system(.body, design: .serif))
                                .foregroundColor(.secondary)
                        }
                    }
                    
                    Button(action: {
                        withAnimation {
                            hasSeenOnboarding = true
                        }
                    }) {
                        Text("Begin")
                            .font(.system(.headline, design: .serif))
                            .foregroundColor(Color(.systemGroupedBackground))
                            .padding(.horizontal, 48)
                            .padding(.vertical, 16)
                            .background(Color.primary)
                            .clipShape(Capsule())
                    }
                }
                .padding(40)
                .tag(2)
            }
            .tabViewStyle(.page(indexDisplayMode: .always))
            .indexViewStyle(.page(backgroundDisplayMode: .always))
        }
    }
}
