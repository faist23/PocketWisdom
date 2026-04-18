//
//  WisdomCard.swift
//  PocketWisdomWidget
//
//  Copy of the main app's WisdomCard model.
//  Keep in sync with PocketWisdom/Models/WisdomCard.swift.
//  TODO (TODOS.md): refactor into SharedModels package when Watch complication is added.
//

import Foundation

struct WisdomCard: Identifiable, Codable {
    let id: UUID
    let category: String
    let title: String
    let body: String
    let reflection: String?
    let author: String?
}
