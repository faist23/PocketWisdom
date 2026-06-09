import SwiftUI

struct LibraryView: View {
    
    @ObservedObject var vm: WisdomViewModel
    @Environment(\.dismiss) var dismiss
    @Environment(\.horizontalSizeClass) var sizeClass
    
    // Track active sidebar selection on iPad
    @State private var selectedTab: LibraryTab? = .saved

    enum LibraryTab: Hashable, Identifiable {
        case saved
        case history
        case categories
        case category(String)
        
        var id: String {
            switch self {
            case .saved: return "saved"
            case .history: return "history"
            case .categories: return "categories"
            case .category(let name): return "category-\(name)"
            }
        }
    }

    var body: some View {
        if sizeClass == .regular {
            // iPad Split View Layout
            NavigationSplitView {
                List(selection: $selectedTab) {
                    Section("Library") {
                        NavigationLink(value: LibraryTab.saved) {
                            Label("Saved Quotes", systemImage: "bookmark.fill")
                        }
                        NavigationLink(value: LibraryTab.history) {
                            Label("Recently Viewed", systemImage: "clock.fill")
                        }
                        NavigationLink(value: LibraryTab.categories) {
                            Label("Categories", systemImage: "folder.fill")
                        }
                    }
                }
                .navigationTitle("Library")
                .listStyle(.sidebar)
                .toolbar {
                    ToolbarItem(placement: .navigationBarTrailing) {
                        Button(action: { dismiss() }) {
                            Image(systemName: "xmark")
                                .foregroundColor(.primary)
                        }
                    }
                }
            } detail: {
                if let selectedTab = selectedTab {
                    switch selectedTab {
                    case .saved:
                        SavedQuotesGridView(vm: vm)
                    case .history:
                        RecentlyViewedGridView(vm: vm)
                    case .categories:
                        CategoriesGridView(vm: vm, onSelectCategory: { cat in
                            self.selectedTab = .category(cat)
                        })
                    case .category(let catName):
                        CategoryDetailGridView(category: catName, vm: vm)
                    }
                } else {
                    Text("Select a section from the sidebar.")
                        .font(.system(.body, design: .serif))
                        .foregroundColor(.secondary)
                        .italic()
                }
            }
        } else {
            // iPhone / Compact Hierarchical Layout (Option B)
            NavigationStack {
                ZStack {
                    Color(.systemGroupedBackground).ignoresSafeArea()
                    
                    List {
                        Section {
                            NavigationLink {
                                SavedQuotesListView(vm: vm)
                            } label: {
                                HStack {
                                    Label("Saved Quotes", systemImage: "bookmark.fill")
                                    Spacer()
                                    if !vm.savedCards.isEmpty {
                                        Text("\(vm.savedCards.count)")
                                            .font(.subheadline)
                                            .foregroundColor(.secondary)
                                            .padding(.horizontal, 8)
                                            .padding(.vertical, 2)
                                            .background(Color(.systemGray5))
                                            .clipShape(Capsule())
                                    }
                                }
                            }
                            
                            NavigationLink {
                                RecentlyViewedListView(vm: vm)
                            } label: {
                                HStack {
                                    Label("Recently Viewed", systemImage: "clock.fill")
                                    Spacer()
                                    if !vm.historyCards.isEmpty {
                                        Text("\(vm.historyCards.count)")
                                            .font(.subheadline)
                                            .foregroundColor(.secondary)
                                            .padding(.horizontal, 8)
                                            .padding(.vertical, 2)
                                            .background(Color(.systemGray5))
                                            .clipShape(Capsule())
                                    }
                                }
                            }
                            
                            NavigationLink {
                                CategoriesListView(vm: vm)
                            } label: {
                                Label("Categories", systemImage: "folder.fill")
                            }
                        }
                    }
                }
                .navigationTitle("Library")
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
}

// MARK: - iPhone Sub-Views

struct SavedQuotesListView: View {
    @ObservedObject var vm: WisdomViewModel
    
    var body: some View {
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
                                vm: vm,
                                onSaveToggled: { vm.toggleSave(for: card) }
                            )
                            .navigationBarTitleDisplayMode(.inline)
                        } label: {
                            LibraryRowView(card: card)
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
    }
}

struct RecentlyViewedListView: View {
    @ObservedObject var vm: WisdomViewModel
    
    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()
            
            if vm.historyCards.isEmpty {
                Text("No history yet.")
                    .font(.system(.body, design: .serif))
                    .foregroundColor(.secondary)
                    .italic()
            } else {
                List {
                    ForEach(vm.historyCards) { card in
                        NavigationLink {
                            SavedCardDetailView(
                                card: card,
                                vm: vm,
                                onSaveToggled: { vm.toggleSave(for: card) }
                            )
                            .navigationBarTitleDisplayMode(.inline)
                        } label: {
                            LibraryRowView(card: card)
                        }
                    }
                }
                .scrollContentBackground(.hidden)
            }
        }
        .navigationTitle("History")
        .toolbar {
            if !vm.historyCards.isEmpty {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(role: .destructive) {
                        vm.clearHistory()
                    } label: {
                        Text("Clear")
                            .foregroundColor(.red)
                    }
                }
            }
        }
    }
}

struct CategoriesListView: View {
    @ObservedObject var vm: WisdomViewModel
    
    private var categories: [String] {
        let allCategories = WisdomRepository.shared.cards.map { $0.category }
        return Array(Set(allCategories)).sorted()
    }
    
    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()
            
            List {
                ForEach(categories, id: \.self) { category in
                    NavigationLink {
                        CategoryDetailListView(category: category, vm: vm)
                    } label: {
                        HStack {
                            Text(category)
                                .font(.system(.headline, design: .serif))
                            Spacer()
                            let count = WisdomRepository.shared.cards.filter { $0.category == category }.count
                            Text("\(count)")
                                .font(.subheadline)
                                .foregroundColor(.secondary)
                                .padding(.horizontal, 8)
                                .padding(.vertical, 2)
                                .background(Color(.systemGray5))
                                .clipShape(Capsule())
                        }
                        .padding(.vertical, 4)
                    }
                }
            }
            .scrollContentBackground(.hidden)
        }
        .navigationTitle("Categories")
    }
}

struct CategoryDetailListView: View {
    let category: String
    @ObservedObject var vm: WisdomViewModel
    
    private var categoryCards: [WisdomCard] {
        WisdomRepository.shared.cards.filter { $0.category == category }
    }
    
    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()
            
            List {
                ForEach(categoryCards) { card in
                    NavigationLink {
                        SavedCardDetailView(
                            card: card,
                            vm: vm,
                            onSaveToggled: { vm.toggleSave(for: card) }
                        )
                        .navigationBarTitleDisplayMode(.inline)
                    } label: {
                        LibraryRowView(card: card)
                    }
                }
            }
            .scrollContentBackground(.hidden)
        }
        .navigationTitle(category)
    }
}

struct LibraryRowView: View {
    let card: WisdomCard
    
    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text(card.title)
                .font(.system(.headline, design: .serif))
                .foregroundColor(.primary)
            
            Text(card.body)
                .font(.system(.subheadline, design: .default))
                .foregroundColor(.secondary)
                .lineLimit(2)
            
            if let author = card.author, !author.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty {
                Text("— \(author)")
                    .font(.system(.caption, design: .serif))
                    .italic()
                    .foregroundColor(.secondary.opacity(0.8))
                    .padding(.top, 2)
            }
        }
        .padding(.vertical, 4)
    }
}

// MARK: - iPad Grid Views

struct SavedQuotesGridView: View {
    @ObservedObject var vm: WisdomViewModel
    
    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()
            
            if vm.savedCards.isEmpty {
                Text("No cards saved yet.")
                    .font(.system(.body, design: .serif))
                    .foregroundColor(.secondary)
                    .italic()
            } else {
                ScrollView {
                    LazyVGrid(columns: [GridItem(.flexible(), spacing: 20), GridItem(.flexible(), spacing: 20)], spacing: 20) {
                        ForEach(vm.savedCards) { card in
                            NavigationLink {
                                SavedCardDetailView(
                                    card: card,
                                    vm: vm,
                                    onSaveToggled: { vm.toggleSave(for: card) }
                                )
                            } label: {
                                GridCardCell(card: card, isSaved: true, onSaveToggled: {
                                    vm.toggleSave(for: card)
                                })
                            }
                            .buttonStyle(PlainButtonStyle())
                        }
                    }
                    .padding(24)
                }
            }
        }
        .navigationTitle("Saved Quotes")
    }
}

struct RecentlyViewedGridView: View {
    @ObservedObject var vm: WisdomViewModel
    
    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()
            
            if vm.historyCards.isEmpty {
                Text("No history yet.")
                    .font(.system(.body, design: .serif))
                    .foregroundColor(.secondary)
                    .italic()
            } else {
                ScrollView {
                    LazyVGrid(columns: [GridItem(.flexible(), spacing: 20), GridItem(.flexible(), spacing: 20)], spacing: 20) {
                        ForEach(vm.historyCards) { card in
                            NavigationLink {
                                SavedCardDetailView(
                                    card: card,
                                    vm: vm,
                                    onSaveToggled: { vm.toggleSave(for: card) }
                                )
                            } label: {
                                GridCardCell(card: card, isSaved: vm.isSaved(card), onSaveToggled: {
                                    vm.toggleSave(for: card)
                                })
                            }
                            .buttonStyle(PlainButtonStyle())
                        }
                    }
                    .padding(24)
                }
            }
        }
        .navigationTitle("History")
        .toolbar {
            if !vm.historyCards.isEmpty {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(role: .destructive) {
                        vm.clearHistory()
                    } label: {
                        Text("Clear History")
                            .foregroundColor(.red)
                    }
                }
            }
        }
    }
}

struct CategoriesGridView: View {
    @ObservedObject var vm: WisdomViewModel
    let onSelectCategory: (String) -> Void
    
    private var categories: [String] {
        let allCategories = WisdomRepository.shared.cards.map { $0.category }
        return Array(Set(allCategories)).sorted()
    }
    
    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()
            
            ScrollView {
                LazyVGrid(columns: [GridItem(.flexible(), spacing: 20), GridItem(.flexible(), spacing: 20)], spacing: 20) {
                    ForEach(categories, id: \.self) { category in
                        Button(action: { onSelectCategory(category) }) {
                            VStack(alignment: .leading, spacing: 12) {
                                HStack {
                                    Image(systemName: "folder.fill")
                                        .font(.title2)
                                        .foregroundColor(.accentColor)
                                    Spacer()
                                    let count = WisdomRepository.shared.cards.filter { $0.category == category }.count
                                    Text("\(count) quotes")
                                        .font(.caption)
                                        .foregroundColor(.secondary)
                                        .padding(.horizontal, 8)
                                        .padding(.vertical, 4)
                                        .background(Color(.systemGray5))
                                        .clipShape(Capsule())
                                }
                                
                                Text(category)
                                    .font(.system(.title2, design: .serif))
                                    .fontWeight(.bold)
                                    .foregroundColor(.primary)
                            }
                            .padding(20)
                            .frame(maxWidth: .infinity, alignment: .leading)
                            .background(Color(.secondarySystemGroupedBackground))
                            .cornerRadius(16)
                            .shadow(color: Color.black.opacity(0.04), radius: 6, x: 0, y: 3)
                        }
                        .buttonStyle(PlainButtonStyle())
                    }
                }
                .padding(24)
            }
        }
        .navigationTitle("Categories")
    }
}

struct CategoryDetailGridView: View {
    let category: String
    @ObservedObject var vm: WisdomViewModel
    
    private var categoryCards: [WisdomCard] {
        WisdomRepository.shared.cards.filter { $0.category == category }
    }
    
    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()
            
            ScrollView {
                LazyVGrid(columns: [GridItem(.flexible(), spacing: 20), GridItem(.flexible(), spacing: 20)], spacing: 20) {
                    ForEach(categoryCards) { card in
                        NavigationLink {
                            SavedCardDetailView(
                                card: card,
                                vm: vm,
                                onSaveToggled: { vm.toggleSave(for: card) }
                            )
                        } label: {
                            GridCardCell(card: card, isSaved: vm.isSaved(card), onSaveToggled: {
                                vm.toggleSave(for: card)
                            })
                        }
                        .buttonStyle(PlainButtonStyle())
                    }
                }
                .padding(24)
            }
        }
        .navigationTitle(category)
    }
}

struct GridCardCell: View {
    let card: WisdomCard
    let isSaved: Bool
    let onSaveToggled: () -> Void
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                Text(card.title)
                    .font(.system(.headline, design: .serif))
                    .foregroundColor(.primary)
                Spacer()
                Button(action: onSaveToggled) {
                    Image(systemName: isSaved ? "bookmark.fill" : "bookmark")
                        .foregroundColor(isSaved ? .accentColor : .secondary)
                }
            }
            
            Text(card.body)
                .font(.system(.body, design: .default))
                .foregroundColor(.secondary)
                .lineLimit(4)
                .multilineTextAlignment(.leading)
            
            if let author = card.author, !author.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty {
                Spacer(minLength: 0)
                Text("— \(author)")
                    .font(.system(.caption, design: .serif))
                    .italic()
                    .foregroundColor(.secondary.opacity(0.8))
                    .padding(.top, 4)
            }
        }
        .padding(20)
        .frame(height: 180, alignment: .topLeading)
        .background(Color(.secondarySystemGroupedBackground))
        .cornerRadius(16)
        .shadow(color: Color.black.opacity(0.04), radius: 6, x: 0, y: 3)
    }
}

private struct SavedCardDetailView: View {
    let card: WisdomCard
    @ObservedObject var vm: WisdomViewModel
    let onSaveToggled: () -> Void
    @State private var showReflection = false
    @Environment(\.colorScheme) private var colorScheme

    var body: some View {
        ZStack {
            WisdomCardView(
                card: card,
                isSaved: vm.isSaved(card),
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
              let window = scene.windows.first,
              let rootVC = window.rootViewController else { return }
        var topVC = rootVC
        while let presented = topVC.presentedViewController {
            topVC = presented
        }
        if let pop = vc.popoverPresentationController {
            pop.sourceView = window
            pop.sourceRect = CGRect(x: window.bounds.midX, y: window.bounds.midY, width: 0, height: 0)
            pop.permittedArrowDirections = []
        }
        topVC.present(vc, animated: true)
    }
}
