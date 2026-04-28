# Cover Decisions - A Contemporary Guide to Wargame Design

Ray Weiss, 2026. KDP paperback, 6x9 trim, 364 pages, B&W white paper,
spine `0.8197 in`.

## Palette

The refreshed cover follows the live Jekyll site instead of the earlier
red/Cormorant concept:

- Paper: `#fdfbf7`
- Alternate spine paper: `#f5f0e8`
- Display ink: `#1c1c2e`
- Body ink: `#2c2c3a`
- Muted text: `#5a5a6e`
- Brown accent: `#7a3b1e`
- Gold rule: `#b5933a`
- Safety/rule color: `#c4b49a`

This keeps the book visually tied to the web edition: light paper, dark
ink, brown/gold accents, and no gradients or SaaS-style decoration.

## Typography

- Title: Playfair Display, matching the site headings.
- Subtitle, author, back-cover blocks: Lora, matching the site body.
- Fallbacks: Georgia and Times New Roman for systems without the web fonts.

The front cover uses a Playfair title stack with "WARGAME DESIGN" as the
dominant accent line. Subtitle and author stay quieter in Lora.

## Structure

- Front: title, subtitle, one flat infantry-counter cue, author, year.
- Spine: bottom-to-top title/author orientation per US paperback convention,
  with the title split into a small kicker and larger display line so it fits
  the `0.8197 in` spine.
- Back: placeholder region for Ray's back-cover copy, placeholder region for
  the author line, and a clean 2.0 x 1.2 in KDP barcode box. No ISBN is
  printed in the source file.
- Guides: bleed, trim, front/back safety, spine boundaries, spine safety, and
  barcode clearance remain in the trailing `<g id="guides">` group.

## Reuse

`build-cover.py` parameterizes title, subtitle, author, spine title, spine
kicker, trim, paper, and page count. It writes both WDB-filled SVG and
placeholder SVGs, and renders PDF/PNG when CairoSVG, Inkscape, or
`rsvg-convert` is available.

## Open Review Points

- Ray still needs to supply back-cover hook copy and the author line in
  `wdb-008`.
- The small counter is intentionally restrained; Ray may decide whether it
  should remain the sole wargame cue or be replaced by a hex-only mark.
- The brown accent comes from the site. A KDP proof should confirm it does
  not print too dark or too red after Amazon's internal conversion.
