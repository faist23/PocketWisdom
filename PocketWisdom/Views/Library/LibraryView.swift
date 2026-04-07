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
