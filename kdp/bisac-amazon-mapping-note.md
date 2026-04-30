# BISAC code → Amazon shelf mapping (sanity check, 2026-04-30)

Decision-support note for the **B.3.2 launch-checklist gate** (top-100
spot-check of chosen BISAC categories). Top-100 spot-checks need
hands-on KDP UI access and Amazon UI browse, neither of which this
session can do directly. What this note can do: flag a structural
audience-fit risk before Ray opens the KDP picker tomorrow.

**TL;DR:** GAM001000 is a clean primary. DES016000 may land WDB next
to Roblox / Unity / Blender programming books, which is the wrong
audience. Worth re-checking the secondary slot against HIS027060
(HISTORY / Military / Strategy) before locking the BISAC selection.

## What the keyword worksheet currently recommends

Per `print/copy/keywords-worksheet.md`:

1. **GAMES & ACTIVITIES / Board Games (GAM001000)** — primary
2. **DESIGN / Games (DES016000)** — secondary

## What the BISG canonical list says

- **GAM001000** confirmed as `GAMES & ACTIVITIES / Board Games`. Has
  sub-codes for Backgammon (010), Chess (030), etc. Correct code, no
  inactive-code redirect.
- **DES016000** confirmed as `DESIGN / Games`. Active code.

Both codes exist. The codes themselves are not the question.

## What Amazon does with these codes (the actual top-100 destination)

Amazon doesn't expose BISAC codes directly to readers; it maps each
BISAC into its own browse-node tree. Two relevant findings from the
2026-04-30 spot-check:

**GAM001000 → Amazon `Books → Crafts, Hobbies & Home → Games &
Activities → Board Games`** (browse node `/zgbs/books/4403`).

This is a books-about-board-games shelf, not a games-on-amazon
shelf. WDB lands alongside the population the keyword worksheet
already names — Dunnigan, Priestley & Lambshead, broader board-game
design books in the high-teens-to-mid-$20s pricing band. **Audience
fit: clean.** This is where wargame and tabletop-design readers
browse.

**DES016000 → Amazon `Books → Computers & Technology → Programming →
Game Programming` ↔ `Computer & Video Game Design` (browse node
`/zgbs/books/10806593011`).**

Amazon's mapping for "DESIGN / Games" lands in the **video-game
programming shelf**, not the tabletop-design shelf. Bestseller-level
neighbors include:
- *The Advanced Roblox Coding Book*
- *3D Game Development with Blender 5 / Unity 6 / Godot Engine 4
  Mastery*
- Jesse Schell's *Art of Game Design: A Book of Lenses* (the only
  shelf-mate that genuinely overlaps with WDB's audience)
- Raph Koster's *Theory of Fun for Game Design* (same — overlaps but
  thin)

**Audience fit: weak.** Most readers browsing this shelf are looking
for video-game programming or design-theory-for-digital-games.
WDB's top-100 neighbors here would be 80%+ wrong-audience books.

## Alternative secondaries worth considering

The keyword worksheet's "Candidate BISAC Categories" section already
lists these as wildcards. Both have stronger Amazon-shelf alignment
than DES016000 for this specific book:

**HIS027060 — HISTORY / Military / Strategy.** Strategy- and
operationally-minded military-history readers are the cross-over
audience the long bio explicitly pitches ("From the German Peasants'
War of 1525 to the Russo-Ukrainian War"). Top-100 in this shelf is
operational military history — *Wages of Destruction*, *Storm of
Steel*, *Carnage and Culture* register. WDB's design-of-historical-
wargames angle reads natively in that population.

**TEC025000 — TECHNOLOGY & ENGINEERING / Military Science.** Defense
education / professional-wargaming wildcard. Smaller shelf, more
specialized audience. The 2022 Ukraine NATO-adoption claim (in the
bio) is its own credential here.

## Recommendation framework (Ray's call)

The choice is between three coherent secondary positions:

| Secondary | Pro | Con |
|---|---|---|
| **DES016000** (current) | "Game Design" search-keyword visibility | Amazon shelf is video-game-programming heavy; WDB reads as outlier |
| **HIS027060** (military / strategy) | Cleanest cross-over with bio's military-history register; wargamers read this shelf | "Design" angle disappears from category browse |
| **TEC025000** (military science) | Targets the 2022 Ukraine NATO-adoption credential directly | Small shelf; misses general design audience |

A defensible read: **GAM001000 + HIS027060** for the secondary slot,
then leave DES016000 and TEC025000 in the keyword pool (where they
pull search traffic without consuming a category slot).

But this is a bet on which audience surfaces the book first
post-launch. If marketing emphasis is design-craft-first → DES016000
defensible. If emphasis is wargame-history-readers-as-discovery
audience → HIS027060.

## What to do with this note

Tomorrow's KDP-listing session uses this when actually picking BISAC
in the KDP UI:

1. Open KDP "Categories" picker
2. Verify GAM001000 path exists in the picker tree (it does — Crafts
   & Hobbies & Home → Games & Activities → Board Games is the canonical
   path)
3. **Try DES016000 first** — open the actual top-100 in that Amazon
   browse node, skim the first 20 titles. If <30% of the top 20 are
   wargame/tabletop-design-relevant, switch to HIS027060.
4. If switching to HIS027060, Amazon's HIS027060 browse node is
   `Books → History → Military → Strategy` — verify the top-20 there
   tracks operational/strategic military history.

This only matters once. Once chosen, KDP categories are
hard-but-not-impossible to change later via Author Central support
ticket, but rank-history starts over each time so changes have a real
cost.
