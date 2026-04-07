//
//  WisdomCard.swift
//  PocketWisdom
//
//  Created by Craig Faist on 4/6/26.
//


import Foundation

struct WisdomCard: Identifiable, Codable {
    let id: UUID
    let category: String
    let title: String
    let body: String
    let reflection: String?
}
