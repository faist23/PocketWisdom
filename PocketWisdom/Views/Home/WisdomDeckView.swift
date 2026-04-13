import SwiftUI

struct WisdomDeckView: View {

    @StateObject private var vm = WisdomViewModel()
    @State private var showLibrary = false
    @State private var showHelp = false
    @State private var helpTask: Task<Void, Never>? = nil
    @State private var reflectionStates: [Int: Bool] = [:]
    @Environment(\.colorScheme) private var colorScheme
    
    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()
            
            TabView(selection: $vm.currentIndex) {
                ForEach(vm.deck.indices, id: \.self) { index in
                    WisdomCardView(
                        card: vm.deck[index],
                        isSaved: vm.isSaved(vm.deck[index]),
                        onSaveToggled: {
                            vm.toggleSave(for: vm.deck[index])
                        },
                        showReflection: Binding(
                            get: { reflectionStates[index, default: false] },
                            set: { reflectionStates[index] = $0 }
                        )
                    )
                    .tag(index)
                }
            }
            .tabViewStyle(.page(indexDisplayMode: .never))
            .ignoresSafeArea()
            .simultaneousGesture(
                DragGesture().onChanged { _ in
                    if showHelp {
                        hideHelp()
                    }
                }
            )
            .onChange(of: vm.currentIndex) {
                if showHelp {
                    hideHelp()
                }
            }
            
            // Corner Overlays
            VStack {
                HStack {
                    // Library Button
                    VStack(spacing: 4) {
                        Image(systemName: "building.columns")
                            .font(.system(size: 18, weight: .light))
                            .foregroundColor(.secondary.opacity(0.5))
                        
                        Text("Library")
                            .font(.caption2)
                            .foregroundColor(.secondary)
                            .opacity(showHelp ? 1 : 0)
                    }
                    .frame(width: 60, height: 60)
                    .contentShape(Rectangle())
                    .onTapGesture {
                        showLibrary = true
                    }
                    .accessibilityElement(children: .ignore)
                    .accessibilityLabel("Library")
                    .accessibilityAddTraits(.isButton)
                    .padding(.top, 16)
                    .padding(.leading, 16)
                    
                    Spacer()
                }
                
                Spacer()
                
                HStack {
                    // Help Button
                    Image(systemName: "questionmark")
                        .font(.system(size: 18, weight: .light))
                        .foregroundColor(.secondary.opacity(0.5))
                        .frame(width: 60, height: 60)
                        .contentShape(Rectangle())
                        .onTapGesture {
                            toggleHelp()
                        }
                        .accessibilityElement(children: .ignore)
                        .accessibilityLabel("Help")
                        .accessibilityAddTraits(.isButton)
                        .padding(.bottom, 16)
                        .padding(.leading, 16)

                    Spacer()

                    // Share Button
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
            
            // Lower Third Help Text Overlay
            if showHelp {
                VStack {
                    Spacer()
                    
                    VStack(spacing: 16) {
                        Text("Swipe for more wisdom")
                        Text("Tap to reveal reflection")
                        Text("Press & hold to save")
                    }
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .padding()
                    .transition(.opacity.animation(.easeInOut))
                    .allowsHitTesting(false)
                    .accessibilityHidden(true)
                }
                .padding(.bottom, 100)
            }
        }
        .animation(.easeInOut, value: showHelp)
        .fullScreenCover(isPresented: $showLibrary) {
            LibraryView(vm: vm)
        }
    }

    @MainActor
    private func renderShareImage() -> UIImage? {
        guard let card = vm.currentCard else { return nil }
        let showing = reflectionStates[vm.currentIndex, default: false]

        let shareView = ShareCardView(card: card, showReflection: showing)
            .environment(\.colorScheme, colorScheme)
        let hostingVC = UIHostingController(rootView: shareView)
        let size = CGSize(width: 360, height: 360)

        // Position off-screen so it doesn't flash visibly
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
    
    private func toggleHelp() {
        if showHelp {
            hideHelp()
        } else {
            showHelp = true
            helpTask?.cancel()
            helpTask = Task {
                try? await Task.sleep(nanoseconds: 10_000_000_000)
                if !Task.isCancelled {
                    await MainActor.run {
                        hideHelp()
                    }
                }
            }
        }
    }
    
    private func hideHelp() {
        showHelp = false
        helpTask?.cancel()
        helpTask = nil
    }
}

