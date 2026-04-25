# Cover decisions — A Contemporary Guide to Wargame Design

Ray Weiss · Conflict Simulations LLC · 2026
KDP paperback · 6×9 trim · 360pp · white paper · spine 0.8107" *(re-cooked 2026-04-24 evening from 340pp/0.7657" baseline after wdb-011 font swap added 14 interior pages)*

## Palette chosen — A · Cartographic cream + ops-red

- Base `#ECE4D0` (warm cream, aged-paper bias — avoids pure white)
- Accent `#A0342A` (iron-oxide red, not fire-engine — SPI combat-results-
  table energy rather than pulp)
- Ink `#1E1A15` (warm near-black; no pure #000 anywhere)
- Muted ink `#5A4F3F` for subtitle + back-cover body

**Why A over B or C.** The cream-and-red pairing does the one job this
cover has to do: it says "historical wargame" to someone who has ever
pulled an Avalon Hill or SPI counter tray out of a box, without saying
anything at all to a reader who hasn't. That's exactly the "initiated
handshake + quiet-academic surface" the brief asked for. Palette B
(parchment + navy) reads more institutional but gives up the hobby
signal — you'd need a stronger diegetic cue to recover it. Palette C
(slate + amber) is the most distinctive statement and would work
beautifully on a shelf, but it pushes the register toward "art-book
edition" and asks the typography to share the wheel with the color. A
keeps the typography supreme and lets the counter do the signaling.

B and C are preserved in the review document so Ray can flip through
them live without rebuilding the file.

## Diegetic cue chosen — Move 1 · Single NATO counter

A flat 1.1" infantry counter (X-in-a-box symbol, `4-6-2` combat factors)
in the accent red, offset rule-of-thirds on the front cover with a
slight -3.2° rotation so it reads as *physical but typographic* — not
a rendered 3D chit, not an airbrushed reproduction, just the same
illustration language the book's own interior diagrams will use.

Hard-edge shadow (no drop-shadow smoothing), chipboard-authentic
proportions, numerals set in the same mono face used for the back-
cover kicker so the counter feels connected to the rest of the page
rather than pasted in.

**Why Move 1 over 2, 3, or 4.** The counter is the single most
universally legible shorthand for a historical board wargame — more
recognizable than an empty hex, more compact than an ops-map fragment.
Move 4 (typographic-only) is the most restrained move, and it's the
strongest statement *if* the title composition is confident enough
to carry the cover alone; the current title setting comes close, but
the counter gives the front a focal point that balances the vertical
weight of the title block and prevents the lower third from reading
empty. Moves 2 (empty hex) and 3 (ops-map fragment) are both still
selectable as live tweaks in the review document.

## Typography — Cormorant Garamond (single-family discipline)

One serif family for everything. Cormorant Garamond is a classical
Garamond revival that sits comfortably next to Sabon, Baskerville,
Hoefler Text, and the NYRB / Oxford Academic register called for in
the brief, and it's web-hosted on Google Fonts so the review renders
predictably without font-swapping surprises.

- Title display: 0.78" caps weight 600, +0.042 tracking
- Title subordinate "guide to": 0.38" italic
- Subtitle: 0.155" italic, muted ink
- Author on front: 0.24" small-caps-style tracked at +0.06
- Spine title: 0.20" caps, +0.025 tracking
- Spine author: 0.16" italic, accent red
- Back-cover body: 0.115–0.155" roman / italic

One monospace (Roboto Mono) carries the kicker lines, publisher
imprint, and counter combat factors. This is deliberate: the mono
reads as *interior diagram typography* rather than display type, so
it does not compete with the serif for register. It also matches the
Consolas monofont stack already declared in `print/metadata.yaml`
for the book interior.

No secondary display face. No swashes, no flourishes, no decorative
caps. The tracking and scale carry the class.

## Spine

Title runs head-to-foot (rotate +90° so the text reads top-to-bottom
when the book lies face-up — KDP's left-to-right convention). Title
(0.20" caps) + author (0.16" italic, accent) + a small CS-in-hex
publisher glyph at the foot. Two accent hairlines top and bottom as
tick-marks. All text stays 0.0625" inside the spine edges, well
within the 0.8107" usable width.

The spine uses a subtly darker tone of the base (#E3D9BF at 45%
opacity over the cream) to create library-binding depth when the
book sits on a shelf — optional but elegant.

## Back cover

Hierarchy, top to bottom:

1. Top accent hairline
2. Kicker: "A FIELD MANUAL FOR WARGAME DESIGNERS" (mono, accent, tracked)
3. Hook paragraph (italic serif, pretty-wrapped, 5" column)
4. Divider rule (short, accent)
5. "ABOUT THE AUTHOR" kicker (mono, muted)
6. Bio block (roman serif)
7. ISBN / barcode zone — clean white 2.0 × 1.2" rectangle at bottom-
   right, 0.25" inside the trim. Nothing drawn over it.
8. Publisher imprint + URL (mono, muted, at the bottom-left)

## Deviations from the brief

**None substantive.**

Minor notes:

- The SVG template form (`cover-template-filled.svg`) preserves
  Mustache placeholders (`{{BACK_COVER_COPY}}`, `{{BIO}}`,
  `{{TITLE_UPPER}}`, `{{AUTHOR}}`, `{{AUTHOR_UPPER}}`, `{{ISBN}}`)
  so the file re-templates cleanly for future Ray books. The
  populated form (`cover-final.svg`) has the real copy baked in.
- The `<g id="guides">` group is kept as a single trailing group so
  step 5 of the README workflow is literally one-block-delete before
  PDF export.
- The SVG uses inch units natively — downstream tools (Inkscape, the
  KDP uploader) consume them directly. If a raster preview is needed,
  render at 300 DPI → 3904.71 × 2775 px.
- The back cover's hook paragraph and bio use `foreignObject` + HTML
  for comfortable multi-line italic wrapping. At PDF export time Ray
  should convert both `foreignObject` blocks to native SVG `<text>` +
  `<tspan>` (one-time, trivial) so the PDF engine renders them as
  outlineable paths rather than raster-rendered HTML.
- Iron-oxide reds sometimes warm unpredictably in the KDP press's
  sRGB→CMYK conversion. `#A0342A` was chosen conservatively on the
  safe side of that shift. If the first KDP proof comes back
  reading too brown, shift toward `#A8372B` or `#AD3A2C`; if it
  reads too orange, drop to `#9A3027`.

## Files delivered

- `print/cover/cover-final.svg` — populated, drop-in for KDP workflow
- `print/cover/cover-template-filled.svg` — template form with
  `{{PLACEHOLDERS}}` preserved for reuse
- `print/cover/cover.jsx` — React source that powers the review
  canvas; not used in the print workflow
- `cover-review.html` — interactive review canvas with live
  Tweaks (palette A/B/C, cue Move 1–4, guide toggle, final-vs-
  placeholder copy toggle)
- `print/cover/cover-decisions.md` — this file
