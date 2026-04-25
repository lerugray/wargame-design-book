# WDB Cover — Claude Design Brief

For upload to **claude.ai/design**. Purpose: generate a finished
wraparound paperback cover (front + spine + back) for Amazon KDP
print-on-demand. Output lands as drop-in artwork for the
existing `print/cover/cover-template.svg` scaffold.

Scope: **the full wraparound at 6×9 trim, 360 pages,
white-paper B&W interior** — spine width ~0.76 inches, canvas
~13.02 × 9.25 inches including 0.125" bleed on all outer edges.
(Exact spine width is computed by `print/cover/spine-width.py`
once the interior page count is final; brief assumes the
360-page-reference number noted in `print/cover/README.md`.)

---

## What the book is

**Title:** *A Contemporary Guide to Wargame Design*
**Author:** Ray Weiss
**Year:** 2026
**Publisher imprint:** Conflict Simulations LLC

**One-line pitch:** *A practical, opinionated guide to designing
historical board wargames — from choosing your subject to getting
published.*

**Structure:** 23 chapters + 6 appendices. Covers foundations
(why design wargames, subject selection, research, scale, time/
space/hex), core systems (OOBs, movement, formations, combat,
sequence of play, supply/morale, victory conditions), advanced
topics (naval/air systems, card-driven games), prototype-to-
publication (concept, playtesting, rules writing, development),
and "the bigger picture" (beyond hex-and-counter, AI tools).

**Audience:** working and aspiring historical-wargame designers.
SPI / Avalon Hill / GMT / Compass readership, not Kickstarter
Euros. Readers know what OOB means. Readers own games with
cardboard counters. Readers care about the difference between
"hex-and-counter" and "area movement."

**Register:** practical + opinionated + academic-adjacent.
Closer to Perla's *The Art of Wargaming* or Dunnigan's *Wargames
Handbook* than to a trade-press introduction. Not a pop-history
book. Not a coffee-table artifact.

---

## Ray's aesthetic direction (the briefer version)

*Classic / simple / slick / classy. Minimal. Wargame-counter /
hex art if anything.*

The cover should **signal wargame-design to anyone who recognizes
the medium**, without shouting it. No airbrushed tank art, no
battle photos, no flames. A reader scanning a table at a
convention should see the cover and know immediately what kind
of book it is — the signal is for the initiated. A reader who
doesn't recognize it should see an elegant, restrained,
professional book cover.

The design move is **one diegetic wargame cue + everything else
restraint.** The cue carries the signal; nothing else competes
with it.

---

## Anchor register: academic-press book cover × wargame insider

Pick the canonical reference pool deliberately. The cover should
sit comfortably next to:

- **Peter Perla, *The Art of Wargaming*** (Naval Institute Press,
  1990 — muted background, strong serif type, minimal ornament)
- **James Dunnigan, *The Complete Wargames Handbook*** (third
  edition — restrained cover, title-driven)
- **Richard Simpkin, *Race to the Swift*** (academic military-
  theory press aesthetic)
- **Matthew Kirschenbaum, *Track Changes*** (MIT Press
  monograph — single typographic anchor, 2-color restraint)
- **Oxford Academic monograph series** (e.g. the Oxford History
  of Modern War volumes — institutional discipline, elegant
  serif wordmarks, one illustrative anchor)
- **NYRB Classics** (single image + elegant type + colored
  stripe — for the "restrained + collectible" register)
- **Penguin Modern Classics** (typographic covers, two-color
  restraint — when there's no image at all)

**Hex-and-counter heritage to borrow FROM:**

- **Squad Leader (Avalon Hill, 1977)** — the grid of red/beige
  counters that *became* the genre's visual signature
- **SPI's Strategy & Tactics magazine covers (1970s)** — muted
  cartographic illustrations, clean block serif titles, two-
  color discipline
- **GMT Games flagship titles (e.g. *Paths of Glory*, *For the
  People*)** — elegant ops-map aesthetics, period typography,
  restrained color
- **Compass Games *The Dark Valley*** — austere cartographic
  cover, serious register
- **Classical unit counters themselves** — a single NATO symbol
  in a colored box, with combat values, is the most universally
  recognizable shorthand in the hobby

**Hex-and-counter to NOT borrow from:**

- Airbrush war-art box covers (Squad Leader's interior mechanic
  was revolutionary, but the *cover art* was pulpy; that's the
  anti-reference)
- Full-painted historical battle scenes (too busy, too
  theme-park)
- Modern Euro-game graphic-design (bright, multi-color,
  illustration-heavy — wrong register entirely)
- Ameritrash war-game covers (Warzone, Twilight Imperium — 180°
  off from where this book sits)
- Anything that looks like a Kickstarter campaign preview

---

## Visual constraints

### Color discipline

**Two colors plus black, maximum.** Ideally two-color (a base
tint + a single accent + black for type). The one-accent-color
decision carries the "slick" energy; a third color dilutes it.

Candidate palettes (pick one; Ray will approve):

**A · Cartographic cream + ops-red** *(recommended default)*
- Base: warm cream / aged paper (~#F3EEE0 to #EDE6D3)
- Accent: muted ops-map red (~#A0342A — iron-oxide, not fire
  engine)
- Type: near-black warm (~#1E1A15), never pure black

The cream + red evokes SPI's 1970s covers + the red of a
classic combat-results-table. Familiar to the reader; strong
signal.

**B · Parchment + navy (quiet-academic)**
- Base: cool parchment (~#F0EBDF)
- Accent: staff-officer navy (~#1F3A5F)
- Type: warm black

Reads as institutional / academic. If the reader looks twice
it's for the typography, not the color pop. Safer, maybe too
safe.

**C · Slate + amber (dusk briefing)**
- Base: slate grey (~#3A3C42 or #4A4D54)
- Accent: restrained amber / ops-gold (~#C89A4A)
- Type: warm near-white

Darker, more "late-night wargaming with a single lamp on."
Riskier but distinctive. Works if the front-cover anchor is a
single gleaming counter on dark field.

**Forbidden:**
- Pure white (#FFFFFF) — clinical, undercuts the print-book
  feel
- Pure black (#000000) — always warm-bias toward ink-brown
- Saturated electric colors (neon, hot pink, Kickstarter
  orange)
- Gradients of any kind — the book is not a landing page
- Rainbow category palettes

### Typography

**One serif face for the title, same serif for the subtitle +
author + spine + back cover.** No secondary display face.

Candidates:

- **Hoefler Text** or **Mercury** (Matthew Carter / H&Co — the
  restrained-academic workhorse)
- **Baskerville** (Monotype — classical, NYRB register)
- **Caslon** (Adobe Caslon Pro — period-appropriate for a
  1970s-SPI vibe)
- **Sabon** (Jan Tschichold — scholarly, Oxford register)
- **Mrs Eaves** (Emigre — Baskerville descendant with more
  presence on a book cover)

**Title treatment:** uppercase or title-case depending on face.
Track it open (~+50 tracking for set-at-display-size, ~+25 for
body). Weight: Regular or Semibold, never Black or Extrabold
— restraint carries the class.

**Subtitle treatment:** one step down in weight + italic +
smaller size. Example hierarchy:

```
A CONTEMPORARY GUIDE TO
WARGAME DESIGN

a practical, opinionated guide
to designing historical board
wargames

RAY WEISS
```

Title stack is 60-75% of the cover height. Author block is 8-12%
of the cover height, bottom-anchored with 0.75-1.0" from trim.
Subtitle sits between title and author, at ~45-55% down.

**Spine text:** title + author + publisher imprint, all the same
serif, running top-to-bottom (head-to-foot per KDP convention for
left-to-right readers — when the book lies face-up, the spine
reads left-to-right). 8-10pt title, 7-9pt author, spine text
0.0625" inside the spine edges.

**Back cover copy** — one or two paragraphs, justified body
serif, same face. Register below.

### The one diegetic cue (pick ONE)

The front cover needs exactly one visual anchor that says
"wargame" to insiders without competing with the typography.
Four acceptable moves:

**Move 1 · Single unit counter (RECOMMENDED)**

A single 0.75" to 1.25" square counter centered or offset-weighted
(rule-of-thirds). Colored in the accent color. Contains a
classical NATO-symbol silhouette (infantry X, armor oval, artillery
dot, or a generic "X inside a box" infantry mark) + a 3-number
combat factor (e.g. `4-6-2` or `7-10-4`). Rendered with slight
rectangular shadow or a single pixel-line border (not drop-shadow
smoothing — hard-edge, chipboard authentic). The counter is the
reader's handshake.

Do not render it 3D, do not airbrush it, do not photograph an
actual die-cut counter — keep it flat, typographic, as if
illustrated for the book's own interior diagrams.

**Move 2 · Single hex outline**

A single regular hexagon (1-1.5" flat-to-flat) rendered as a thin
stroke in the accent color, set somewhere on the front cover.
Could contain a single counter inside (combines Move 1+2), OR
could sit empty as the shape itself — the blank hex is the
medium's most universal signifier.

**Move 3 · Sparse ops-map fragment**

A minimal cartographic schematic — 3-5 hex outlines connected by
a thin river/road line, maybe one elevation contour or a fort
symbol. Rendered in accent color only. Feels like a
reconnaissance sketch, not a full map. Best for covers that want
"briefing-table aesthetic" rather than "single counter."

**Move 4 · Typographic-only (no image)**

No visual at all. The title, set in a classical serif at display
size, with precise tracking + leading, carries the whole cover.
Penguin Modern Classics energy. A colored accent bar or the
author's name in accent color is the only ornament. This is the
strongest statement if the typography is right — but it needs a
confident type designer's eye.

---

## Front cover (6 × 9, plus 0.125" bleed on three outer edges)

Layout zones (from top):

1. **Optional top-band** (~0.5-0.75"): empty or hairline accent
   rule. A flat colored band here is classic SPI-magazine move
   but can feel too retro; prefer empty.
2. **Title block** (~40-55% of height): title set large, serif.
   Subtitle beneath, italic, smaller.
3. **Diegetic cue** (~15-25% of height): the chosen anchor from
   the 4 moves. Positioned to breathe (rule-of-thirds, not dead
   center unless typographic-only).
4. **Author block** (~10% of height, bottom-weighted): "RAY
   WEISS" in small-caps or title-case. Can sit directly below
   the diegetic cue or at true bottom with a rule above.
5. **Bottom margin** (~0.75-1.0"): empty. Publisher imprint
   *Conflict Simulations LLC* optional at very bottom, 6-7pt.

### Safety zone

All text must sit at least **0.125" inside the trim line** (so
0.25" from the bleed edge). The title and subtitle typically
sit much deeper (~0.5-0.75" inset) for visual comfort — the
safety zone is the minimum, not the target.

---

## Spine (narrow strip, ~0.81" × 9" for 360pp)

Layout (reading head-to-foot):

- **Top 10-15%:** empty (just color)
- **Upper 25-40%:** title, all-caps serif, tracked open, centered
  on the spine width
- **Middle 20%:** empty spacing
- **Lower 30%:** author "RAY WEISS" in smaller serif, centered
- **Bottom 10%:** publisher imprint *Conflict Simulations LLC*
  in tiny caps (can also be one of the classical Avalon Hill /
  SPI style logo marks if a clean glyph is available — a hex
  outline with "CS" inside, for instance)

Spine text size must fit within **0.0625" off each spine edge**
(per KDP spec) — effective usable spine width at 0.76" is
~0.63". Plan type sizes accordingly.

If the design goes with the dark-slate palette (C), the spine
color may differ subtly from the front cover (slightly darker or
lighter tone) to create a subtle 3D depth when the book sits on
a shelf — this is a library-binding move, optional but elegant.

---

## Back cover (6 × 9, plus 0.125" bleed on three outer edges)

Layout (from top):

1. **Optional accent bar / wordmark strip** (~0.5"): repeats the
   front cover's color or one narrow diegetic element
2. **Pull quote / hook paragraph** (~25-30% of height): 2-3
   sentences of marketing copy, serif, justified or ragged-right,
   set at 11-13pt with comfortable leading. This is the copy
   Ray will supply separately in `wdb-008`. For now, reserve
   the space and use placeholder Lorem/filler that matches the
   visual weight of real copy. Example placeholder:
   > *"A working designer's field manual for turning history
   > into playable systems. From choosing a subject to crossing
   > the finish line at publication, this is the guide I wish
   > I'd had when I started."*
3. **About-the-author block** (~20-25% of height): single
   short paragraph + optional small headshot. Structure:
   - Optional small portrait (~1.5" square) left or right of text
   - 3-5 sentences at 10-11pt, same serif
   - Placeholder text: *"Ray Weiss is an independent wargame
     designer and the founder of Conflict Simulations LLC. This
     book distills lessons learned from designing games, studying
     the craft, and making plenty of mistakes along the way."*
4. **ISBN + barcode zone** (~2" × 1.2" at bottom-right):
   reserved blank white rectangle, ~2" wide × 1.2" tall,
   typically bottom-right 0.25" inside the trim. KDP inserts the
   barcode automatically; the cover must leave a clean white
   box. **Do not design anything over this zone.**
5. **Publisher imprint + URL** (~0.4" at very bottom): *Conflict
   Simulations LLC · lerugray.github.io/wargame-design-book*
   or similar. 6-7pt, muted.

### Back-cover hierarchy

The hook paragraph reads first, the bio supports it. If the
designer wants to be restrained, **the bio is small and the hook
carries the cover.** If a pull quote from a named reviewer
becomes available later (wdb-008), it replaces the hook
paragraph.

---

## What to preserve from the existing scaffold

The cover template file `print/cover/cover-template.svg` is the
canvas. Claude Design should:

1. **Preserve the Mustache placeholder tokens** (`{{TITLE}}`,
   `{{SUBTITLE}}`, `{{AUTHOR}}`, `{{BACK_COVER_COPY}}`,
   `{{BIO}}`, `{{ISBN}}`) if possible, so the file can be
   re-templated for future Ray books without redrawing.
2. **Preserve the `<g id="guides">` group** — the bleed/trim/
   spine guide lines — as a SEPARATE LAYER that gets stripped
   before KDP upload (per the README workflow step 5). Don't
   fuse guides into the design.
3. **Respect the canvas dimensions** — 13.0607" × 9.25" for
   the 360-page reference build. If the art is vector (SVG) it
   scales cleanly when the final page count nudges the spine.
4. **Output both a populated example** (title + subtitle +
   author filled in with the real copy above) **and the
   template form** (with `{{PLACEHOLDERS}}`) so the workflow
   survives future edits.

---

## Deliverables from Claude Design

Target output:

1. **`cover-final.svg`** — populated design with real title /
   subtitle / author / placeholder back-cover copy, ready for
   Ray to review, add cover art if Move 3 or Move 4 needs
   custom pixels, and export to PDF for KDP.
2. **`cover-template-filled.svg`** — same design but with
   `{{PLACEHOLDERS}}` where the populated copy sits, so future
   Ray books reuse the template.
3. **Front-cover PNG at display size** — ~1600 × 2400 px
   for review on-screen and for social-media preview.
4. **Back-cover PNG at display size** — same, for review.
5. **Spine-only PNG at display size** — so Ray can review the
   spine typography separately from the wraparound.
6. **A short `cover-decisions.md`** — one page max, explaining:
   - Which palette was chosen (A/B/C) and why
   - Which diegetic cue was chosen (Moves 1-4) and why
   - Which serif was used + why
   - Any deviations from the brief and the reasoning

Optional bonus if Claude Design's agent has time:

- **Alternative front-covers** (2-3 variants) showing different
  diegetic-cue moves against the same color palette, so Ray can
  A/B the approach before finalizing.

---

## Constraints on the final cover

**Must clear:**

- Front-cover text safety (0.125" off trim all four sides)
- Back-cover text safety (same) + 2" × 1.2" clean white
  barcode zone at bottom-right
- Spine text safety (0.0625" off each spine edge)
- All bleed fills extend to the 0.125" bleed line, not only the
  trim line
- Vector-first output (SVG); rasterize only for previews
- Color profile: **sRGB for screen preview, but flag for CMYK
  conversion in notes** — KDP's press actually consumes the
  uploaded PDF as sRGB and converts internally, so sRGB is
  correct for the file, but the designer should verify the
  accent color survives the gamut shift (iron-oxide reds
  sometimes warm unpredictably in press)
- Type rendered as outlines/paths in the final PDF export
  (don't rely on KDP having the font) — this is a post-export
  step Ray handles; the SVG can keep live text

**Must avoid:**

- Pure black (#000000) ink anywhere — always warm-bias
  (#1E1A15 or similar)
- Pure white (#FFFFFF) page fields — always cream-bias if the
  palette is A or B
- Text within 0.125" of any trim edge
- Any design element over the barcode zone
- Airbrushed / photographic / painterly illustration
- More than one diegetic cue (one counter, one hex, or one ops-
  map fragment — pick one, not three)
- Clip-art or stock hex grids that don't match the counter's
  line weight
- AI-generated "pixel art" counters that look smoothed or
  anti-aliased (the counter is a typographic element, not a
  pixel sprite)
- Three colors of accent; keep to two-plus-black
- Decorative swashes, curlicues, or Victorian flourishes — the
  register is 1970s-SPI, not 1890s-drawing-room
- Emoji / Unicode dingbats

---

## Voice for the cover copy

Ray hasn't finalized the back-cover hook yet (that's wdb-008
in the internal backlog), but the voice calibration is:

- **Direct, declarative, practical.** Not coy, not marketed-up,
  not self-congratulatory.
- Naming specific structural concerns ("choosing your subject,"
  "getting published") is in range. The book is a field manual,
  not a memoir.
- Author bio: "independent wargame designer and founder of
  Conflict Simulations LLC" is the canonical phrase (from the
  README). Do not paraphrase. Do not expand into speculative
  credits.
- Do not invent pull-quote blurbs. If a blurb slot is included
  as layout reference, use a generic "PRAISE FOR THE BOOK" kicker
  + placeholder — Ray fills real blurbs in wdb-008 once they
  exist.

---

## Reference anchors (summary)

**Visual:**
- Peter Perla, *The Art of Wargaming* (Naval Institute Press)
- James Dunnigan, *The Complete Wargames Handbook* (3rd ed)
- GMT Games *Paths of Glory* cover
- SPI Strategy & Tactics magazine covers, 1970s
- Avalon Hill *Squad Leader* rulebook interior counter plates
  (NOT the box cover)
- NYRB Classics, Penguin Modern Classics (typographic registers)
- Oxford Academic / MIT Press monograph covers

**Tonal:**
- Peter Perla's prose register — matter-of-fact, technical,
  measured
- SPI's mid-1970s editorial voice — "we are telling you how to
  do it"
- A staff college publication — institutional, not marketed

**Anti-references:**
- Airbrushed war-art box covers (Squad Leader, Panzerblitz cover
  paintings)
- Kickstarter campaign graphics
- Ameritrash / Fantasy Flight theme-game covers
- Modern Euro-game graphic design (Feld, Rosenberg-era)
- *For Whom the Bell Tolls* / Hemingway-era trade-press covers
  (wrong register — too literary)
- AI-generated "pixel art" cover attempts
- Stock hex-grid backgrounds

---

## Output target

Final cover files land in `print/cover/` alongside the existing
scaffold (`spine-width.py`, `cover-template.svg`, `README.md`).
The `cover-final.svg` drops into the workflow at step 4 of the
existing README ("Drop in cover art and the finalized copy"),
replacing the `<rect class="bleed-fill">` background and
front-cover art placeholder box. Ray strips the `<g id="guides">`
block and exports to PDF for KDP upload (existing README step 5).

---

## Files to read for grounding (Claude Design will want these)

Upload alongside the brief:

1. `print/cover/README.md` (54 lines) — technical scaffold spec
2. `print/cover/cover-template.svg` (135 lines) — the SVG canvas
3. `print/cover/spine-width.py` (116 lines) — canvas math
4. `print/metadata.yaml` — title, author, year, font stack
5. `README.md` (repo root) — one-paragraph book pitch + author
   bio + chapter structure
6. `print/back-matter/about-the-author.md` — bio layout stub
   (for the back-cover about-author block)

Optional but useful:

7. One or two chapter openings from `_chapters/` — to calibrate
   the book's interior typographic register against the cover
   (so the cover's serif feels consistent with the body text,
   which is Georgia at 11pt)

---

## One-line summary of the ask

*Make the most restrained, classically-designed book cover this
kind of book has ever had — confident serif typography, two-color
discipline, one diegetic wargame cue, everything else left quiet
— so that when it sits on a shelf next to Perla and Dunnigan it
looks like it belongs there.*
