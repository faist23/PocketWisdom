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
