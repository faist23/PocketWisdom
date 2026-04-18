//
//  AppGroupKeys.swift
//  PocketWisdom
//
//  Shared constants for App Groups UserDefaults.
//  This file is compiled into both the main app and the widget extension.
//  Add it to BOTH targets' Compile Sources in Xcode.
//

import Foundation

enum AppGroupKeys {
    static let suiteName           = "group.com.faist23.PocketWisdom"
    static let appCurrentIndex     = "appCurrentIndex"
    static let widgetIndex         = "widgetIndex"
    static let shuffledDeckIDs     = "shuffledDeckIDs"
    static let savedCardIDs        = "savedCardIDs"
    static let currentWidgetCardID = "currentWidgetCardID"
    static let lastKnownDeckCount  = "lastKnownDeckCount"
}
