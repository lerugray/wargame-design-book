# Cover Template (KDP Paperback)

Parametric wraparound cover scaffolding for Ray's KDP paperbacks.
The current reference build is **6x9 trim, B&W white paper, 360 pages**:
spine `0.8107 in`, full canvas `13.0607 x 9.25 in` including bleed.

## Files

- `spine-width.py` calculates KDP spine width and full-cover dimensions.
- `kdp_cover.py` holds reusable KDP math, the site palette, and SVG renderer.
- `build-cover.py` writes editable SVG sources and, when local tooling exists,
  exports print-ready PDF/PNG previews.
- `cover-final.svg` is the WDB editable source with title/author filled and
  Ray-owned copy blocks left as placeholders.
- `cover-template.svg` and `cover-template-filled.svg` keep Mustache-style
  placeholders for future Ray KDP books.

## Build

```bash
python print/cover/spine-width.py --pages 360 --paper white --trim 6x9
python print/cover/build-cover.py --pages 360 --paper white --trim 6x9
```

Expected generated outputs:

- `print/cover/cover-final.svg`
- `print/cover/cover-template.svg`
- `print/cover/cover-template-filled.svg`
- `print/out/wargame-design-book-cover.pdf`
- `print/out/wargame-design-book-cover.png`

PDF/PNG export uses Python `cairosvg` if installed, then falls back to
Inkscape or `rsvg-convert`. The PDF/PNG files live in `print/out/`, which is
gitignored because they are generated artifacts.

## Parameters

The build script accepts the reusable book fields:

```bash
python print/cover/build-cover.py \
  --title "Future Ray Book" \
  --subtitle "Subtitle goes here" \
  --author "Ray Weiss" \
  --spine-title "Future Ray Book" \
  --spine-kicker "A Practical Guide to" \
  --pages 300
```

## Paper Factor Reference

KDP spine width = `pages * paper_factor`.

| Paper | Factor (in/page) |
| --- | ---: |
| B&W on white | `0.002252` |
| B&W on cream | `0.0025` |
| Premium color | `0.002347` |

Bleed is `0.125 in` on all outer edges. Text safety is `0.125 in` inside
front/back trim and `0.0625 in` off each spine edge. KDP allows spine text
only at `>= 80` pages.
