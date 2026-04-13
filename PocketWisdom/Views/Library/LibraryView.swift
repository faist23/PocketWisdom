import SwiftUI

struct LibraryView: View {
    
    @ObservedObject var vm: WisdomViewModel
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        NavigationStack {
            ZStack {
                Color(.systemGroupedBackground).ignoresSafeArea()
                
                if vm.savedCards.isEmpty {
                    Text("No cards saved yet.")
                        .font(.system(.body, design: .serif))
                        .foregroundColor(.secondary)
                        .italic()
                } else {
                    List {
                        ForEach(vm.savedCards) { card in
                            NavigationLink {
                                SavedCardDetailView(
                                    card: card,
                                    isSaved: vm.isSaved(card),
                                    onSaveToggled: { vm.toggleSave(for: card) }
                                )
                                .navigationBarTitleDisplayMode(.inline)
                            } label: {
                                VStack(alignment: .leading, spacing: 8) {
                                    Text(card.title)
                                        .font(.system(.headline, design: .serif))
                                        .foregroundColor(.primary)
                                    
                                    Text(card.body)
                                        .font(.system(.subheadline, design: .default))
                                        .foregroundColor(.secondary)
                                        .lineLimit(2)
                                }
                                .padding(.vertical, 4)
                            }
                            .swipeActions {
                                Button(role: .destructive) {
                                    withAnimation {
                                        vm.toggleSave(for: card)
                                    }
                                } label: {
                                    Label("Remove", systemImage: "trash")
                                }
                            }
                            .contextMenu {
                                Button(role: .destructive) {
                                    withAnimation {
                                        vm.toggleSave(for: card)
                                    }
                                } label: {
                                    Label("Remove from Saved", systemImage: "trash")
                                }
                            }
                        }
                        .onDelete { indexSet in
                            for index in indexSet {
                                let card = vm.savedCards[index]
                                vm.toggleSave(for: card)
                            }
                        }
                    }
                    .scrollContentBackground(.hidden)
                }
            }
            .navigationTitle("Saved")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(action: { dismiss() }) {
                        Image(systemName: "xmark")
                            .foregroundColor(.primary)
                    }
                }
            }
        }
    }
}

private struct SavedCardDetailView: View {
    let card: WisdomCard
    let isSaved: Bool
    let onSaveToggled: () -> Void
    @State private var showReflection = false
    @Environment(\.colorScheme) private var colorScheme

    var body: some View {
        ZStack {
            WisdomCardView(
                card: card,
                isSaved: isSaved,
                onSaveToggled: onSaveToggled,
                showReflection: $showReflection
            )

            VStack {
                Spacer()
                HStack {
                    Spacer()
                    Image(systemName: "square.and.arrow.up")
                        .font(.system(size: 18, weight: .light))
                        .foregroundColor(.secondary.opacity(0.5))
                        .frame(width: 60, height: 60)
                        .contentShape(Rectangle())
                        .onTapGesture {
                            if let image = renderShareImage() {
                                presentShareSheet(image: image)
                            }
                        }
                        .accessibilityElement(children: .ignore)
                        .accessibilityLabel("Share")
                        .accessibilityAddTraits(.isButton)
                        .padding(.bottom, 16)
                        .padding(.trailing, 16)
                }
            }
        }
    }

    @MainActor
    private func renderShareImage() -> UIImage? {
        let shareView = ShareCardView(card: card, showReflection: showReflection)
            .environment(\.colorScheme, colorScheme)
        let hostingVC = UIHostingController(rootView: shareView)
        let size = CGSize(width: 360, height: 360)
        hostingVC.view.frame = CGRect(x: -2000, y: -2000, width: size.width, height: size.height)
        hostingVC.view.backgroundColor = UIColor.systemGroupedBackground
        guard let window = UIApplication.shared.connectedScenes
            .compactMap({ $0 as? UIWindowScene })
            .first?.windows.first else { return nil }
        window.addSubview(hostingVC.view)
        hostingVC.view.layoutIfNeeded()
        let format = UIGraphicsImageRendererFormat()
        format.scale = 3.0
        format.opaque = true
        let image = UIGraphicsImageRenderer(size: size, format: format).image { _ in
            hostingVC.view.drawHierarchy(in: hostingVC.view.bounds, afterScreenUpdates: true)
        }
        hostingVC.view.removeFromSuperview()
        return image
    }

    private func presentShareSheet(image: UIImage) {
        guard let data = image.pngData() else { return }
        let timestamp = Int(Date().timeIntervalSince1970)
        let url = FileManager.default.temporaryDirectory.appendingPathComponent("PocketWisdom-\(timestamp).png")
        guard (try? data.write(to: url)) != nil else { return }
        let vc = UIActivityViewController(activityItems: [url], applicationActivities: nil)
        guard let scene = UIApplication.shared.connectedScenes.first as? UIWindowScene,
              let rootVC = scene.windows.first?.rootViewController else { return }
        var topVC = rootVC
        while let presented = topVC.presentedViewController {
            topVC = presented
        }
        topVC.present(vc, animated: true)
    }
}
