import SwiftUI

struct ShareCardView: View {

    let card: WisdomCard
    let showReflection: Bool

    var body: some View {
        ZStack {
            Color(.systemGroupedBackground)

            VStack(spacing: 20) {
                Spacer()

                Text(card.title)
                    .font(.system(.title2, design: .serif))
                    .foregroundColor(.secondary)
                    .multilineTextAlignment(.center)

                Text(card.body)
                    .font(.system(.title3, design: .serif))
                    .foregroundColor(.primary)
                    .multilineTextAlignment(.center)
                    .minimumScaleFactor(0.65)

                if let author = card.author {
                    Text("— \(author)")
                        .font(.system(.body, design: .serif))
                        .italic()
                        .foregroundColor(.secondary)
                        .multilineTextAlignment(.center)
                }

                if showReflection, let reflection = card.reflection {
                    Text(reflection)
                        .font(.body)
                        .foregroundColor(.secondary)
                        .multilineTextAlignment(.center)
                }

                Spacer()

                Text("The Pocket Wisdom App")
                    .font(.caption2)
                    .foregroundColor(.secondary)
                    .opacity(0.35)
            }
            .padding(32)
        }
        .frame(width: 360, height: 360)
        .clipShape(RoundedRectangle(cornerRadius: 24))
    }
}
