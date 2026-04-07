import SwiftUI

struct WisdomDeckView: View {
    
    @StateObject private var vm = WisdomViewModel()
    @State private var showLibrary = false
    
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
            
            // Invisible Corner Tap
            VStack {
                HStack {
                    Rectangle()
                        .fill(Color.black.opacity(0.001))
                        .frame(width: 60, height: 60)
                        .overlay(
                            Circle()
                                .fill(Color.secondary.opacity(0.3))
                                .frame(width: 6, height: 6)
                        )
                        .onTapGesture {
                            showLibrary = true
                        }
                    Spacer()
                }
                Spacer()
            }
        }
        .fullScreenCover(isPresented: $showLibrary) {
            LibraryView(vm: vm)
        }
    }
}
