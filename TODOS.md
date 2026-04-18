# PocketWisdom — TODOs

## P2 — Widget Feature

### Lock screen save button
**What:** Test whether the AppIntent save button (heart icon) fits and works on
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

## Future Expansions (from CEO review 2026-04-18)

- Apple Watch complication — App Groups container is already the right foundation
- Configurable widget cadence (morning only / evening only / 6h)
- Category filter for widget pool
- iCloud deck sync across devices
- Siri shortcut ("show me a quote")
