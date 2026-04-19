//
//  BalancedText.swift
//  PocketWisdom
//
//  A centered Text view that balances line lengths (similar to CSS text-wrap: balance).
//  Finds the minimum column width that still wraps the text to the same number of lines
//  as full-width, then centers that narrower column — so lines end up roughly equal.
//

import SwiftUI
import UIKit

struct BalancedText: View {
    let text: String
    let uiFont: UIFont

    @State private var balancedWidth: CGFloat? = nil

    var body: some View {
        Text(text)
            .font(Font(uiFont as CTFont))
            .multilineTextAlignment(.center)
            .frame(width: balancedWidth)
            // Outer frame fills available width so GeometryReader sees the right maxWidth
            // and so the inner (narrower) frame is centered within the available space.
            .frame(maxWidth: .infinity)
            .background(
                GeometryReader { geo in
                    Color.clear
                        .onAppear { balance(in: geo.size.width) }
                        .onChange(of: geo.size.width) { _, w in balance(in: w) }
                }
            )
    }

    private func balance(in maxWidth: CGFloat) {
        guard maxWidth > 0 else { return }

        let attrs: [NSAttributedString.Key: Any] = [.font: uiFont]
        let attrStr = NSAttributedString(string: text, attributes: attrs)
        let options: NSStringDrawingOptions = [.usesLineFragmentOrigin, .usesFontLeading]

        func lineCount(for width: CGFloat) -> Int {
            let rect = attrStr.boundingRect(
                with: CGSize(width: width, height: .infinity),
                options: options,
                context: nil
            )
            return Int(ceil(rect.height / uiFont.lineHeight))
        }

        let targetLines = lineCount(for: maxWidth)

        // Single-line text needs no balancing.
        guard targetLines > 1 else {
            balancedWidth = nil
            return
        }

        // Binary search: minimum width that still fits in targetLines.
        // Lower bound: evenly distributed would need at least maxWidth / targetLines.
        var lo = maxWidth / CGFloat(targetLines)
        var hi = maxWidth

        for _ in 0 ..< 14 {
            let mid = (lo + hi) / 2
            if lineCount(for: mid) <= targetLines {
                hi = mid
            } else {
                lo = mid
            }
        }

        balancedWidth = hi
    }
}
