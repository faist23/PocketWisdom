//
//  PocketWisdomApp.swift
//  PocketWisdom
//
//  Created by Craig Faist on 4/6/26.
//

import SwiftUI

@main
struct PocketWisdomApp: App {
    
    @AppStorage("hasSeenOnboarding") private var hasSeenOnboarding = false
    
    var body: some Scene {
        WindowGroup {
            if hasSeenOnboarding {
                WisdomDeckView()
            } else {
                OnboardingView()
            }
        }
    }
}
