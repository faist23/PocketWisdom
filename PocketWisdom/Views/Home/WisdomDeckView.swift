import SwiftUI

struct WisdomDeckView: View {
    
    @StateObject private var vm = WisdomViewModel()
    @State private var showLibrary = false
    @State private var showHelp = false
    @State private var helpTask: Task<Void, Never>? = nil
    
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
                        }
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
            .onChange(of: vm.currentIndex) { _ in
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
                        .padding(.bottom, 16)
                        .padding(.leading, 16)
                    
                    Spacer()
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
                }
                .padding(.bottom, 100)
            }
        }
        .animation(.easeInOut, value: showHelp)
        .fullScreenCover(isPresented: $showLibrary) {
            LibraryView(vm: vm)
        }
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
