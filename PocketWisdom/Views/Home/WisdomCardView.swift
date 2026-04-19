import SwiftUI
import UIKit

// UIFont matching .system(.title3, design: .serif) — used by BalancedText for measurement.
private let bodyUIFont: UIFont = {
    let base = UIFontDescriptor.preferredFontDescriptor(withTextStyle: .title3)
    let descriptor = base.withDesign(.serif) ?? base
    return UIFont(descriptor: descriptor, size: 0)
}()

struct WisdomCardView: View {

    let card: WisdomCard
    let isSaved: Bool
    let onSaveToggled: () -> Void

    @Binding var showReflection: Bool

    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()

            VStack(spacing: 24) {
                Text(card.title)
                    .font(.system(.title2, design: .serif))
                    .foregroundColor(.secondary)

                BalancedText(text: card.body, uiFont: bodyUIFont)
                    .foregroundColor(.primary)
                
                if let author = card.author {
                    Text("— \(author)")
                        .font(.system(.body, design: .serif))
                        .italic()
                        .foregroundColor(.secondary)
                }
                
                if showReflection, let reflection = card.reflection {
                    Text(reflection)
                        .font(.body)
                        .foregroundColor(.secondary)
                        .multilineTextAlignment(.center)
                        .transition(.opacity.animation(.easeInOut(duration: 0.5)))
                }
            }
            .padding(32)
            
            // Subtle "Saved" indicator
            if isSaved {
                VStack {
                    HStack {
                        Spacer()
                        Image(systemName: "bookmark.fill")
                            .font(.caption)
                            .foregroundColor(.secondary)
                            .padding(24)
                    }
                    Spacer()
                }
            }
        }
        .contentShape(Rectangle()) // Makes entire background tappable
        .onTapGesture {
            withAnimation {
                showReflection.toggle()
            }
        }
        .onLongPressGesture(minimumDuration: 0.5) {
            let generator = UINotificationFeedbackGenerator()
            generator.notificationOccurred(.success)
            onSaveToggled()
        }
        .accessibilityElement(children: .combine)
        .accessibilityAddTraits(.isButton)
        .accessibilityHint(isSaved ? "Saved. Double tap to toggle reflection. Swipe up or down to select the Unsave action, then double tap to activate." : "Double tap to toggle reflection. Swipe up or down to select the Save action, then double tap to activate.")
        .accessibilityAction(named: isSaved ? "Unsave" : "Save") {
            let generator = UINotificationFeedbackGenerator()
            generator.notificationOccurred(.success)
            onSaveToggled()
        }
    }
}
