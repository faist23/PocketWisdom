//
//  PocketWisdomWidgetBundle.swift
//  PocketWisdomWidget
//

import WidgetKit
import SwiftUI

@main
struct PocketWisdomWidgetBundle: WidgetBundle {
    var body: some Widget {
        PocketWisdomHomeWidget()
        PocketWisdomLockScreenWidget()
    }
}
