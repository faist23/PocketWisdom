import SwiftUI

struct MarketingView: View {
    var body: some View {
        TabView {
            // Slide 1: Welcome / Main Deck
            MarketingSlide(
                headline: "Wisdom for your day.",
                subheadline: "A curated collection of timeless insight and modern reflection.",
                backgroundColor: Color(hex: "0F172A") // Deep Slate
            ) {
                MockupPhone {
                    MockHomeView()
                }
                .padding(.bottom, -100) // Bleed off the bottom
            }

            // Slide 2: Library
            MarketingSlide(
                headline: "Build your library.",
                subheadline: "Save the quotes that resonate most with your journey.",
                backgroundColor: Color(hex: "1E1B4B") // Deep Indigo
            ) {
                MockupPhone {
                    MockLibraryView()
                }
                .padding(.bottom, -100) // Bleed off the bottom
            }

            // Slide 3: Widgets
            MarketingSlide(
                headline: "Wisdom on your home screen.",
                subheadline: "Inspiration at a glance, delivered throughout your day.",
                backgroundColor: Color(hex: "431407") // Deep Rust
            ) {
                VStack(spacing: 40) {
                    MockWidget(size: .small)
                    MockWidget(size: .medium)
                }
                .padding(.bottom, 60) // Keep widgets safely above the bottom edge
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
    let content: () -> Content

    var body: some View {
        ZStack {
            backgroundColor.ignoresSafeArea()
            
            // Subtle background decoration
            Circle()
                .fill(Color.white.opacity(0.05))
                .frame(width: 600, height: 600)
                .offset(x: -200, y: -300)
            
            VStack(spacing: 30) {
                VStack(spacing: 12) {
                    Text(headline)
                        .font(.system(size: 32, weight: .bold, design: .serif))
                        .multilineTextAlignment(.center)
                        .foregroundColor(.white)
                        .fixedSize(horizontal: false, vertical: true)
                    
                    Text(subheadline)
                        .font(.system(size: 17, weight: .medium, design: .default))
                        .multilineTextAlignment(.center)
                        .foregroundColor(.white.opacity(0.8))
                        .fixedSize(horizontal: false, vertical: true)
                }
                .frame(width: UIScreen.main.bounds.width - 80) // Force width for wrapping
                .padding(.top, 70)
                
                Spacer()
                
                content()
            }
        }
    }
}

struct MockupPhone<Content: View>: View {
    let content: () -> Content
    
    var body: some View {
        ZStack {
            // Device Frame
            RoundedRectangle(cornerRadius: 44)
                .stroke(Color.white.opacity(0.2), lineWidth: 8)
                .background(Color.black)
                .cornerRadius(44)
                .shadow(color: .black.opacity(0.5), radius: 30, x: 0, y: 20)
            
            // Screen Content
            content()
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

struct MockWidget: View {
    let size: WidgetSize
    enum WidgetSize { case small, medium }
    
    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 24)
                .fill(Color(hex: "1F2937"))
                .shadow(color: .black.opacity(0.3), radius: 10, x: 0, y: 5)
            
            VStack(alignment: .leading, spacing: 8) {
                Text("“")
                    .font(.system(size: 32, design: .serif))
                    .foregroundColor(.accentColor)
                
                Text("Nature does not hurry, yet everything is accomplished.")
                    .font(.system(size: size == .small ? 16 : 18, weight: .medium, design: .serif))
                    .foregroundColor(.white)
                
                Spacer()
                
                Text("— Lao Tzu")
                    .font(.caption)
                    .foregroundColor(.white.opacity(0.6))
            }
            .padding()
        }
        .frame(width: size == .small ? 158 : 338, height: 158)
    }
}

// MARK: - Mock Views (Simplified versions of app UI)

struct MockHomeView: View {
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            VStack {
                Spacer()
                ZStack {
                    RoundedRectangle(cornerRadius: 24)
                        .fill(Color(hex: "262626"))
                        .padding(20)
                    
                    VStack(spacing: 20) {
                        Text("“")
                            .font(.system(size: 60, design: .serif))
                            .foregroundColor(.accentColor)
                        
                        Text("The unexamined life is not worth living.")
                            .font(.system(size: 28, weight: .bold, design: .serif))
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, 40)
                        
                        Text("— Socrates")
                            .font(.headline)
                            .foregroundColor(.gray)
                    }
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
