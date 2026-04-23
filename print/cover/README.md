# Cover template (KDP paperback)

Parametric scaffolding for the wraparound cover. Reusable across future Ray
KDP books — rename tokens and swap the art, the math is the same.

## Files

- `spine-width.py` — CLI calculator. Emits spine width and full-cover canvas
  dimensions for a given page count, paper type, and trim size.
- `cover-template.svg` — wraparound cover with bleed, trim, and spine guides
  marked, plus Mustache-style placeholders for title / subtitle / author /
  back-cover copy / bio / ISBN. Reference canvas: **6x9 trim, white paper,
  340 pages** (spine 0.7657 in, canvas 13.0157 x 9.25 in).
- `cover-art.*` — dropped in later. Replaces the `<rect class="bleed-fill">`
  background and the front-cover art placeholder box. **Hands-off for the
  bot** — human-curated artwork only.

## Workflow

1. Finalize the print PDF (`wdb-001`) so the actual page count is known.
2. Run the calculator with that page count:

   ```
   python spine-width.py --pages 340 --paper white --trim 6x9
   ```

   Note the spine width and the canvas width.

3. Update `cover-template.svg`:
   - `width="..."` and `viewBox="0 0 ... 9.25"` to the new canvas width.
   - Spine boundaries (currently `x=6.125` and `x=6.8907`) to
     `0.125 + 6` and `0.125 + 6 + spine_width`.
   - Front-cover safety rect `x=7.0157` to `0.25 + 6 + spine_width`.
   - Spine text `transform="translate(6.55 ...)` to
     `0.125 + 6 + spine_width/2`.
   - Trim box width `12.7657` to `canvas_width - 0.25`.

4. Drop in cover art and the finalized copy from `wdb-008`.

5. Strip the `<g id="guides">` block before exporting to PDF for KDP upload.

## Paper factor reference

KDP spine width = `pages * paper_factor`:

| Paper            | Factor (in/page) |
|------------------|------------------|
| B&W on white     | 0.002252         |
| B&W on cream     | 0.0025           |
| Premium color    | 0.002347         |

Bleed is 0.125 in on all outer edges. Text safety zone is 0.125 in inside the
trim on front/back; 0.0625 in off each spine edge. Spine text is only
permitted at >= 80 pages.
