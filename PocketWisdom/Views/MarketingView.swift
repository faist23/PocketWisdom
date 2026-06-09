import SwiftUI

enum MarketingDevice: String, CaseIterable, Identifiable {
    case phone = "iPhone"
    case pad = "iPad"
    
    var id: String { self.rawValue }
}

struct MarketingView: View {
    var body: some View {
        let isPad = UIDevice.current.userInterfaceIdiom == .pad
        let currentDevice: MarketingDevice = isPad ? .pad : .phone

        TabView {
            // Slide 1: Welcome / Main Deck
            MarketingSlide(
                headline: "Wisdom for your day.",
                subheadline: "A curated collection of timeless insight and modern reflection.",
                backgroundColor: Color(hex: "0F172A"), // Deep Slate
                device: currentDevice
            ) {
                Group {
                    if currentDevice == .phone {
                        MockupPhone {
                            MockHomeView(device: .phone)
                        }
                        .padding(.bottom, -100) // Bleed off the bottom
                    } else {
                        MockupPad {
                            MockHomeView(device: .pad)
                        }
                        .padding(.bottom, -80) // Bleed off the bottom
                    }
                }
            }

            // Slide 2: Library
            MarketingSlide(
                headline: "Build your library.",
                subheadline: "Save the quotes that resonate most with your journey.",
                backgroundColor: Color(hex: "1E1B4B"), // Deep Indigo
                device: currentDevice
            ) {
                Group {
                    if currentDevice == .phone {
                        MockupPhone {
                            MockLibraryView()
                        }
                        .padding(.bottom, -100) // Bleed off the bottom
                    } else {
                        MockupPad {
                            MockiPadLibraryView()
                        }
                        .padding(.bottom, -80) // Bleed off the bottom
                    }
                }
            }

            // Slide 3: Widgets
            MarketingSlide(
                headline: "Wisdom on your home screen.",
                subheadline: "Inspiration at a glance, delivered throughout your day.",
                backgroundColor: Color(hex: "431407"), // Deep Rust
                device: currentDevice
            ) {
                Group {
                    if currentDevice == .phone {
                        VStack(spacing: 40) {
                            MockWidget(size: .small)
                            MockWidget(size: .medium)
                        }
                        .padding(.bottom, 60) // Keep widgets safely above the bottom edge
                    } else {
                        VStack(spacing: 32) {
                            HStack(spacing: 32) {
                                MockWidget(size: .small)
                                MockWidget(size: .medium)
                            }
                            HStack(spacing: 32) {
                                MockWidget(size: .medium)
                                MockWidget(size: .small)
                            }
                        }
                        .padding(.bottom, 80) // Keep widgets safely above the bottom edge
                    }
                }
            }
        }
        .tabViewStyle(.page)
        .ignoresSafeArea()
    }
}

// MARK: - Components

struct MarketingSlide<Content: View>: View {
    let headline: String
    let subheadline: String
    let backgroundColor: Color
    let device: MarketingDevice
    let content: Content

    init(
        headline: String,
        subheadline: String,
        backgroundColor: Color,
        device: MarketingDevice,
        @ViewBuilder content: () -> Content
    ) {
        self.headline = headline
        self.subheadline = subheadline
        self.backgroundColor = backgroundColor
        self.device = device
        self.content = content()
    }

    var body: some View {
        ZStack {
            backgroundColor.ignoresSafeArea()
            
            // Subtle background decoration
            Circle()
                .fill(Color.white.opacity(0.04))
                .frame(width: device == .pad ? 900 : 600, height: device == .pad ? 900 : 600)
                .offset(x: device == .pad ? -300 : -200, y: device == .pad ? -400 : -300)
            
            VStack(spacing: device == .pad ? 40 : 30) {
                VStack(spacing: device == .pad ? 16 : 12) {
                    Text(headline)
                        .font(.system(size: device == .pad ? 48 : 32, weight: .bold, design: .serif))
                        .multilineTextAlignment(.center)
                        .foregroundColor(.white)
                        .fixedSize(horizontal: false, vertical: true)
                    
                    Text(subheadline)
                        .font(.system(size: device == .pad ? 22 : 17, weight: .medium, design: .default))
                        .multilineTextAlignment(.center)
                        .foregroundColor(.white.opacity(0.85))
                        .fixedSize(horizontal: false, vertical: true)
                }
                .frame(width: device == .pad ? 680 : UIScreen.main.bounds.width - 80) // Adjust wrapping width
                .padding(.top, device == .pad ? 110 : 70)
                
                Spacer()
                
                content
            }
        }
    }
}

struct MockupPhone<Content: View>: View {
    let content: Content
    
    init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }
    
    var body: some View {
        ZStack {
            // Device Frame
            RoundedRectangle(cornerRadius: 44)
                .stroke(Color.white.opacity(0.2), lineWidth: 8)
                .background(Color.black)
                .cornerRadius(44)
                .shadow(color: .black.opacity(0.5), radius: 30, x: 0, y: 20)
            
            // Screen Content
            content
                .clipShape(RoundedRectangle(cornerRadius: 38))
                .padding(8)
            
            // Notch
            Capsule()
                .fill(Color.black)
                .frame(width: 120, height: 30)
                .padding(.top, 12)
                .frame(maxHeight: .infinity, alignment: .top)
        }
        .frame(width: 320, height: 680)
    }
}

struct MockupPad<Content: View>: View {
    let content: Content
    
    init(@ViewBuilder content: () -> Content) {
        self.content = content()
    }
    
    var body: some View {
        ZStack {
            // Device Frame (Modern iPad Pro design with thin bezels)
            RoundedRectangle(cornerRadius: 36)
                .stroke(Color.white.opacity(0.25), lineWidth: 10)
                .background(Color.black)
                .cornerRadius(36)
                .shadow(color: .black.opacity(0.6), radius: 45, x: 0, y: 25)
            
            // Screen Content
            content
                .clipShape(RoundedRectangle(cornerRadius: 28))
                .padding(10)
            
            // Hidden subtle camera dot in bezel
            Circle()
                .fill(Color(white: 0.15))
                .frame(width: 8, height: 8)
                .padding(.top, 14)
                .frame(maxHeight: .infinity, alignment: .top)
        }
        .frame(width: 480, height: 640) // Portrait 3:4 aspect ratio
    }
}

struct MockWidget: View {
    let size: WidgetSize
    enum WidgetSize { case small, medium }
    
    var body: some View {
        ZStack {
            // Widget container background
            RoundedRectangle(cornerRadius: 24)
                .fill(Color(hex: "1F2937"))
                .shadow(color: .black.opacity(0.3), radius: 10, x: 0, y: 5)
            
            if size == .small {
                // High-fidelity Small Widget (from PocketWisdomWidget.swift)
                ZStack(alignment: .bottomTrailing) {
                    VStack {
                        Spacer()
                        Text("Nature does not hurry, yet everything is accomplished.")
                            .font(.system(.footnote, design: .serif))
                            .multilineTextAlignment(.center)
                            .foregroundColor(.white)
                            .lineLimit(5)
                            .padding(.horizontal, 10)
                        Spacer()
                    }
                    .frame(maxWidth: .infinity)
                    
                    Image(systemName: "bookmark.fill")
                        .font(.system(size: 11))
                        .foregroundColor(.accentColor)
                        .padding(12)
                }
            } else {
                // High-fidelity Medium Widget (from PocketWisdomWidget.swift)
                ZStack(alignment: .topTrailing) {
                    VStack(spacing: 6) {
                        Spacer()
                        Text("Nature does not hurry, yet everything is accomplished.")
                            .font(.system(.subheadline, design: .serif))
                            .multilineTextAlignment(.center)
                            .foregroundColor(.white)
                            .fixedSize(horizontal: false, vertical: true)
                        
                        Text("— Lao Tzu")
                            .font(.system(size: 10))
                            .foregroundColor(.white.opacity(0.5))
                            .multilineTextAlignment(.center)
                            .padding(.top, 2)
                        
                        Text("True power comes from alignment with the flow of the universe.")
                            .font(.system(size: 11))
                            .foregroundColor(.white.opacity(0.7))
                            .multilineTextAlignment(.center)
                            .padding(.top, 4)
                            .fixedSize(horizontal: false, vertical: true)
                        Spacer()
                    }
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                    .padding(.horizontal, 24)
                    .padding(.vertical, 12)
                    
                    Image(systemName: "bookmark.fill")
                        .font(.system(size: 12))
                        .foregroundColor(.accentColor)
                        .padding(12)
                }
            }
        }
        .frame(width: size == .small ? 158 : 338, height: 158)
    }
}

// MARK: - Mock Views (Simplified versions of app UI)

struct MockHomeView: View {
    let device: MarketingDevice

    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()

            // Quote content matching WisdomCardView layout
            VStack(spacing: 24) {
                Text("The Unexamined Life")
                    .font(.system(.title2, design: .serif))
                    .foregroundColor(.secondary)

                Text("The unexamined life\nis not worth living.")
                    .font(.system(.title3, design: .serif))
                    .multilineTextAlignment(.center)
                    .foregroundColor(.primary)
                    .padding(.horizontal, device == .pad ? 48 : 32)

                Text("— Socrates")
                    .font(.system(.body, design: .serif))
                    .italic()
                    .foregroundColor(.secondary)
            }
            .padding(32)

            // Saved bookmark indicator (top-right) — matches WisdomCardView
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

            // Corner overlays matching WisdomDeckView
            VStack {
                HStack {
                    Image(systemName: "building.columns")
                        .font(.system(size: 18, weight: .light))
                        .foregroundColor(.secondary.opacity(0.5))
                        .frame(width: 60, height: 60)
                        .padding(.top, 16)
                        .padding(.leading, 16)
                    Spacer()
                }
                Spacer()
                HStack {
                    Image(systemName: "questionmark")
                        .font(.system(size: 18, weight: .light))
                        .foregroundColor(.secondary.opacity(0.5))
                        .frame(width: 60, height: 60)
                        .padding(.bottom, 16)
                        .padding(.leading, 16)
                    Spacer()
                    Image(systemName: "square.and.arrow.up")
                        .font(.system(size: 18, weight: .light))
                        .foregroundColor(.secondary.opacity(0.5))
                        .frame(width: 60, height: 60)
                        .padding(.bottom, 16)
                        .padding(.trailing, 16)
                }
            }
        }
        .environment(\.colorScheme, .dark)
    }
}

struct MockLibraryView: View {
    var body: some View {
        ZStack {
            Color(.systemGroupedBackground).ignoresSafeArea()

            VStack(alignment: .leading, spacing: 0) {
                // Simulated inline nav bar matching real LibraryView
                HStack {
                    Text("Library")
                        .font(.headline)
                        .foregroundColor(.primary)
                    Spacer()
                    Image(systemName: "xmark")
                        .font(.system(size: 15, weight: .medium))
                        .foregroundColor(.secondary)
                }
                .padding(.horizontal, 16)
                .padding(.vertical, 14)

                Divider()

                List {
                    Section {
                        HStack {
                            Label("Saved Quotes", systemImage: "bookmark.fill")
                            Spacer()
                            Text("12")
                                .font(.subheadline)
                                .foregroundColor(.secondary)
                                .padding(.horizontal, 8)
                                .padding(.vertical, 2)
                                .background(Color(.systemGray5))
                                .clipShape(Capsule())
                        }
                        HStack {
                            Label("Recently Viewed", systemImage: "clock.fill")
                            Spacer()
                            Text("4")
                                .font(.subheadline)
                                .foregroundColor(.secondary)
                                .padding(.horizontal, 8)
                                .padding(.vertical, 2)
                                .background(Color(.systemGray5))
                                .clipShape(Capsule())
                        }
                        Label("Categories", systemImage: "folder.fill")
                    }
                }
                .scrollContentBackground(.hidden)
            }
        }
        .environment(\.colorScheme, .dark)
    }
}

struct MockiPadLibraryView: View {
    private let gridQuotes: [(title: String, body: String, author: String)] = [
        (title: "Nature's Pace",        body: "Nature does not hurry, yet everything is accomplished.",          author: "Laozi"),
        (title: "Action Over Argument", body: "Waste no more time arguing what a good man should be. Be one.",  author: "Marcus Aurelius"),
        (title: "Imagined Suffering",   body: "We suffer more often in imagination than in reality.",           author: "Epictetus"),
        (title: "Inner Power",          body: "You have power over your mind, not outside events.",             author: "Marcus Aurelius")
    ]

    var body: some View {
        HStack(spacing: 0) {
            // Sidebar — mimicking NavigationSplitView .sidebar style
            VStack(alignment: .leading, spacing: 0) {
                Text("Library")
                    .font(.title2.bold())
                    .foregroundColor(.primary)
                    .padding(.horizontal, 20)
                    .padding(.top, 20)
                    .padding(.bottom, 8)

                // Selected row
                Label("Saved Quotes", systemImage: "bookmark.fill")
                    .font(.system(size: 15, weight: .medium))
                    .foregroundColor(.white)
                    .padding(.vertical, 9)
                    .padding(.horizontal, 14)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(Color.accentColor.opacity(0.9))
                    .cornerRadius(8)
                    .padding(.horizontal, 10)
                    .padding(.bottom, 2)

                // Unselected rows
                Label("Recently Viewed", systemImage: "clock.fill")
                    .font(.system(size: 15))
                    .foregroundColor(.primary)
                    .padding(.vertical, 9)
                    .padding(.horizontal, 14)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .padding(.horizontal, 10)

                Label("Categories", systemImage: "folder.fill")
                    .font(.system(size: 15))
                    .foregroundColor(.primary)
                    .padding(.vertical, 9)
                    .padding(.horizontal, 14)
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .padding(.horizontal, 10)

                Spacer()
            }
            .frame(width: 200)
            .background(Color(.secondarySystemGroupedBackground))

            Rectangle()
                .fill(Color.primary.opacity(0.1))
                .frame(width: 0.5)

            // Detail panel — 2-column grid matching real SavedQuotesGridView
            ZStack {
                Color(.systemGroupedBackground).ignoresSafeArea()

                VStack(alignment: .leading, spacing: 0) {
                    Text("Saved Quotes")
                        .font(.title2.bold())
                        .foregroundColor(.primary)
                        .padding(.horizontal, 20)
                        .padding(.top, 20)
                        .padding(.bottom, 16)

                    LazyVGrid(
                        columns: [GridItem(.flexible(), spacing: 16), GridItem(.flexible(), spacing: 16)],
                        spacing: 16
                    ) {
                        ForEach(gridQuotes.indices, id: \.self) { i in
                            let q = gridQuotes[i]
                            VStack(alignment: .leading, spacing: 10) {
                                HStack {
                                    Text(q.title)
                                        .font(.system(.headline, design: .serif))
                                        .foregroundColor(.primary)
                                    Spacer()
                                    Image(systemName: "bookmark.fill")
                                        .font(.caption)
                                        .foregroundColor(.accentColor)
                                }
                                Text(q.body)
                                    .font(.system(.subheadline, design: .default))
                                    .foregroundColor(.secondary)
                                    .lineLimit(3)
                                    .multilineTextAlignment(.leading)
                                Spacer(minLength: 0)
                                Text("— \(q.author)")
                                    .font(.system(.caption, design: .serif))
                                    .italic()
                                    .foregroundColor(.secondary.opacity(0.8))
                            }
                            .padding(16)
                            .frame(height: 150, alignment: .topLeading)
                            .background(Color(.secondarySystemGroupedBackground))
                            .cornerRadius(14)
                        }
                    }
                    .padding(.horizontal, 20)

                    Spacer()
                }
            }
        }
        .environment(\.colorScheme, .dark)
    }
}

// MARK: - Helpers

extension Color {
    init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch hex.count {
        case 3: // RGB (12-bit)
            (a, r, g, b) = (255, (int >> 8) * 17, (int >> 4 & 0xF) * 17, (int & 0xF) * 17)
        case 6: // RGB (24-bit)
            (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        case 8: // ARGB (32-bit)
            (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
        default:
            (a, r, g, b) = (1, 1, 1, 0)
        }
        self.init(.sRGB, red: Double(r) / 255, green: Double(g) / 255, blue: Double(b) / 255, opacity: Double(a) / 255)
    }
}

#Preview {
    MarketingView()
}
