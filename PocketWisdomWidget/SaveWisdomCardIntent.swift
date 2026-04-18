//
//  SaveWisdomCardIntent.swift
//  PocketWisdomWidget
//
//  AppIntent for the in-widget save button (bookmark icon).
//  Runs in the widget extension process.
//  Requires iOS 17+ (AppIntent interactive widget support).
//

import AppIntents
import WidgetKit

struct SaveWisdomCardIntent: AppIntent {
    static var title: LocalizedStringResource = "Save Wisdom Card"

    @Parameter(title: "Card ID")
    var cardID: String

    func perform() async throws -> some IntentResult {
        guard let defaults = UserDefaults(suiteName: AppGroupKeys.suiteName) else {
            return .result()
        }
        var saved = Set(defaults.stringArray(forKey: AppGroupKeys.savedCardIDs) ?? [])
        saved.insert(cardID)
        defaults.set(Array(saved), forKey: AppGroupKeys.savedCardIDs)
        WidgetCenter.shared.reloadAllTimelines()
        return .result()
    }
}
