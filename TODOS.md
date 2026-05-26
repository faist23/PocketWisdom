# PocketWisdom — TODOs

## P2 — Widget Feature

### Lock screen save button
**What:** Test whether the AppIntent save button (bookmark icon) fits and works on
`.accessoryRectangular` lock screen widget. If cramped or awkward, ship the lock
screen widget as display-only (quote + author, tap to open app).
**Why:** `.accessoryRectangular` is small. Interactive buttons may feel cluttered.
**Start:** After widget is built and running on device. Test on real hardware — simulator
doesn't accurately represent lock screen widget layout.
**Priority:** P2 — decide before App Store submission if applicable.

---

### SharedModels Swift Package
**What:** Refactor the copied `WisdomCard.swift` (duplicated in both app and widget
targets) into a local Swift Package so both targets import a single source of truth.
**Why:** Right now WisdomCard is copied manually into both targets. If the struct
changes, both copies must be updated. Low risk for 6 fields; higher risk if the
model grows or a Watch complication is added.
**When:** When adding Apple Watch complication, or when WisdomCard exceeds ~8 fields.
**Priority:** P3 — defer until a third target needs the model.

---

### DESIGN.md — codify the implicit design system
**What:** Run `/design-consultation` to produce a `DESIGN.md` documenting PocketWisdom's
typography scale, color tokens, spacing system, icon vocabulary (bookmark = save, etc.),
and accessibility standards.
**Why:** Every design decision for the widget required reverse-engineering the app's design
language from source code. The next feature will have the same problem. A DESIGN.md makes
the implicit explicit and speeds up every future design review.
**When:** After shipping the widget. The widget added enough new surfaces to make the
design system worth writing down.
**Priority:** P2 — before the next user-facing feature after the widget.

---

## Future Expansions (from CEO review 2026-04-18)

- Apple Watch complication — App Groups container is already the right foundation
- Configurable widget cadence (morning only / evening only / 6h)
- Category filter for widget pool
- iCloud deck sync across devices
- Siri shortcut ("show me a quote")

---

## Completed

### Content & Notification Polish (2026-05-17)
**What:** Added 100 new mixed quotes (ancient, modern, literary, contemporary), fixed notification deep-linking, generated App Store assets, and fixed extension versioning.
**How:**
- Generated `wisdom.json` updates and performed deduplication prioritizing new quotes.
- Fixed a cold-start race condition by rewriting `NotificationDelegate` as an `ObservableObject` Singleton to cache tapped `cardID`s.
- Updated `jumpToCard` in `WisdomViewModel` to gracefully pluck the requested card and insert it at `currentIndex` to prevent skipping deck content.
- Created `MarketingView.swift` to serve as an in-simulator App Store screenshot generator.
- Synced `MARKETING_VERSION` (1.3.2) across the widget extension and test targets in `project.pbxproj` to resolve build errors.

### Daily notification (2026-05-11)
**What:** Opt-in daily 9am notification with a random unseen quote.
**How:** `NotificationScheduler` (in `App/`) reads `shuffledDeckIDs` + `appCurrentIndex`
from App Groups and pre-schedules 60 `UNCalendarNotificationTrigger` notifications.
Refills when pending count drops below 7 on each app foreground.
New users: prompted via onboarding screen 4 ("One card. Every morning.").
Existing users: one-time system permission dialog on first open after the update,
gated by `hasPromptedForNotifications` in standard `UserDefaults` and
`hasSeenOnboarding` (so the dialog never fires during a new user's first launch).
