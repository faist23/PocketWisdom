//
//  PocketWisdomWidgetBundle.swift
//  PocketWisdomWidget
//
//  Widget extension entry point.
//  Supports three widget families:
//    - .systemSmall    (home screen, small)
//    - .systemMedium   (home screen, medium)
//    - .accessoryRectangular (lock screen)
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

// MARK: - Home Screen Widget (.systemSmall + .systemMedium)

struct PocketWisdomHomeWidget: Widget {
    let kind = "PocketWisdomHomeWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: WisdomTimelineProvider()) { entry in
            PocketWisdomWidgetView(entry: entry)
        }
        .configurationDisplayName("Pocket Wisdom")
        .description("A wisdom card from your deck, refreshed morning and evening.")
        .supportedFamilies([.systemSmall, .systemMedium])
    }
}

// MARK: - Lock Screen Widget (.accessoryRectangular)

struct PocketWisdomLockScreenWidget: Widget {
    let kind = "PocketWisdomLockScreenWidget"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: WisdomTimelineProvider()) { entry in
            PocketWisdomWidgetView(entry: entry)
        }
        .configurationDisplayName("Pocket Wisdom")
        .description("A wisdom card from your deck.")
        .supportedFamilies([.accessoryRectangular])
    }
}
