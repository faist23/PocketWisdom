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
            Color.black.ignoresSafeArea()
            VStack {
                Spacer()
                ZStack {
                    RoundedRectangle(cornerRadius: device == .pad ? 32 : 24)
                        .fill(Color(hex: "262626"))
                        .padding(device == .pad ? 30 : 20)
                    
                    VStack(spacing: device == .pad ? 30 : 20) {
                        Text("“")
                            .font(.system(size: device == .pad ? 80 : 60, design: .serif))
                            .foregroundColor(.accentColor)
                        
                        Text("The unexamined life is not worth living.")
                            .font(.system(size: device == .pad ? 36 : 28, weight: .bold, design: .serif))
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, device == .pad ? 50 : 40)
                        
                        Text("— Socrates")
                            .font(device == .pad ? .title2 : .headline)
                            .foregroundColor(.gray)
                    }
                    .padding(device == .pad ? 24 : 0)
                }
                Spacer()
            }
        }
    }
}

struct MockLibraryView: View {
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            VStack(alignment: .leading) {
                Text("Library")
                    .font(.largeTitle.bold())
                    .padding()
                    .foregroundColor(.white)
                
                ForEach(0..<4) { i in
                    HStack {
                        VStack(alignment: .leading) {
                            Text(["Marcus Aurelius", "Seneca", "Rumi", "Epictetus"][i])
                                .font(.caption.bold())
                                .foregroundColor(.accentColor)
                            Text(["Be one.", "Suffer in imagination.", "The moon and stars.", "The beginning of wisdom."][i])
                                .font(.body)
                                .foregroundColor(.white)
                                .lineLimit(1)
                        }
                        Spacer()
                        Image(systemName: "chevron.right")
                            .foregroundColor(.gray)
                    }
                    .padding()
                    .background(Color.white.opacity(0.05))
                    .cornerRadius(12)
                    .padding(.horizontal)
                }
                Spacer()
            }
        }
    }
}

struct MockiPadLibraryView: View {
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            
            HStack(spacing: 0) {
                // Sidebar / Master Panel
                VStack(alignment: .leading, spacing: 20) {
                    Text("Library")
                        .font(.title2.bold())
                        .foregroundColor(.white)
                        .padding(.top, 24)
                    
                    VStack(alignment: .leading, spacing: 14) {
                        HStack(spacing: 12) {
                            Image(systemName: "bookmark.fill")
                                .foregroundColor(.accentColor)
                                .font(.system(size: 16))
                            Text("Saved Quotes")
                                .foregroundColor(.white)
                                .font(.system(size: 15, weight: .medium))
                        }
                        .padding(.vertical, 10)
                        .padding(.horizontal, 12)
                        .frame(maxWidth: .infinity, alignment: .leading)
                        .background(Color.white.opacity(0.1))
                        .cornerRadius(10)
                        
                        HStack(spacing: 12) {
                            Image(systemName: "folder")
                                .foregroundColor(.gray)
                                .font(.system(size: 16))
                            Text("Categories")
                                .foregroundColor(.gray)
                                .font(.system(size: 15))
                        }
                        .padding(.vertical, 10)
                        .padding(.horizontal, 12)
                        
                        HStack(spacing: 12) {
                            Image(systemName: "clock")
                                .foregroundColor(.gray)
                                .font(.system(size: 16))
                            Text("History")
                                .foregroundColor(.gray)
                                .font(.system(size: 15))
                        }
                        .padding(.vertical, 10)
                        .padding(.horizontal, 12)
                    }
                    Spacer()
                }
                .frame(width: 170)
                .padding(.horizontal, 12)
                .background(Color(hex: "111827"))
                
                // Divider
                Rectangle()
                    .fill(Color.white.opacity(0.08))
                    .frame(width: 1)
                
                // Details Grid
                ScrollView {
                    VStack(alignment: .leading, spacing: 20) {
                        Text("Saved")
                            .font(.largeTitle.bold())
                            .foregroundColor(.white)
                            .padding(.horizontal)
                            .padding(.top, 24)
                        
                        LazyVGrid(columns: [GridItem(.flexible()), GridItem(.flexible())], spacing: 16) {
                            ForEach(0..<4) { i in
                                VStack(alignment: .leading, spacing: 10) {
                                    HStack {
                                        Text(["Marcus Aurelius", "Seneca", "Rumi", "Epictetus"][i])
                                            .font(.caption.bold())
                                            .foregroundColor(.accentColor)
                                        Spacer()
                                        Image(systemName: "bookmark.fill")
                                            .font(.caption)
                                            .foregroundColor(.secondary)
                                    }
                                    
                                    Text(["Be one.", "Suffer in imagination.", "The moon and stars.", "The beginning of wisdom."][i])
                                        .font(.system(.body, design: .serif))
                                        .foregroundColor(.white)
                                        .lineLimit(2)
                                    
                                    Spacer()
                                }
                                .padding()
                                .frame(height: 120)
                                .background(Color.white.opacity(0.05))
                                .cornerRadius(12)
                            }
                        }
                        .padding(.horizontal)
                    }
                }
            }
        }
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
