# KDP Proof Copy Workflow

A reusable checklist for ordering and reviewing KDP paperback proofs. Written for 6x9 black-ink interior paperbacks but the review steps generalize.

## 1. Before ordering a proof

Don't order until all of these are true:

- Interior PDF passes KDP's online previewer with zero warnings (not just zero errors — warnings matter).
- Every raster image embedded at **300 DPI minimum** at its printed size. A 600px-wide image printed at 3 inches = 200 DPI and will look fuzzy.
- All fonts embedded. KDP will flag missing fonts, but the previewer sometimes passes PDFs that substitute metrics-compatible fonts silently. Flatten to outlines if unsure.
- Cover PDF matches the trim size + spine width KDP calculated from your final page count. If you change page count by even one page, regenerate spine width.
- Bleed: 0.125" on all outside edges for covers. Interior bleed only if you have full-page images that run to the edge — otherwise skip it.
- ISBN set. KDP's free ISBN is fine for paperback-only; buy your own only if you plan to distribute outside Amazon.

## 2. Ordering the proof

In KDP dashboard:

1. Finish the paperback setup through the Pricing page. Do **not** hit Publish.
2. Bottom of the Pricing page → "Request Printed Proofs".
3. Order **two copies**. One for marking up, one for the shelf / a reader. Proofs are printed at cost (no royalty), around $3–5 per copy plus shipping for a 300-page 6x9 B&W.
4. Expect 7–10 business days in the US. Slower internationally.

Proofs arrive stamped "Not For Resale" across the cover — do not photograph them for promo.

## 3. Proof review checklist

Work through these with the physical book in hand. Mark up with sticky flags, not pen.

### Trim & binding
- Measure the trim with a ruler. 6x9 should be exactly that, ±1/16". Bigger variance means KDP printed wrong size — contact support.
- Open the book flat at the middle. Text should not disappear into the gutter. If it does, your inside margin is too small (KDP's minimum is 0.375" for 151–300 pages, 0.5" for 301–500, 0.625" for 501–700, 0.75" for 701+).
- Hold the spine up to the light. Cover art should hit the spine edges without wrapping onto front/back. If the spine text is drifting toward front or back cover, your spine width was miscalculated.

### Cover
- Front cover: title and author legible at arm's length. Playfair Display at 48pt looks large in InDesign and small on paper.
- Back cover: the hook paragraph reads cleanly. Author bio fits without crowding. Barcode area (bottom right, ~2" x 1.2") is clear of art and text.
- Color: compare to your RGB mockup. KDP prints CMYK, so saturated blues/greens/purples will shift. If the cover looks muddy, rework in CMYK before reordering.

### Interior — typography
- Body text (Lora, ~11pt for 6x9) reads comfortably at arm's length. If it looks small, bump to 11.5 or 12 and accept a higher page count.
- Line length: 60–75 characters per line. Longer is hard to track; shorter looks choppy.
- Leading: body leading around 14–15pt for 11pt Lora. Check for rivers (vertical streaks of whitespace) on dense pages.
- Chapter openings: Playfair Display heading doesn't crash into the text block. Drop caps (if used) align with the x-height of line 2, not the baseline of line 1.
- Widows (single line of paragraph at top of page) and orphans (single line of paragraph at bottom). One or two are acceptable; a book full of them looks amateur.

### Interior — images
- Every diagram crisp, not pixelated. Hold the page 12" from your face — if you can see pixel edges on lines, the image was exported too small.
- Line weight on diagrams ≥ 0.5pt. Thinner lines can drop out entirely on POD presses.
- Captions present, correctly numbered, positioned consistently (below image, same font).
- Grayscale conversion: anything that was color in the web version should have been re-rendered in grayscale, not just desaturated. Desaturated color images lose contrast between hues that were distinct.

### Interior — structure
- Running heads correct on every page (verso = book title, recto = chapter title is the standard, but reversed is fine — just be consistent).
- Page numbers present on every body page, absent on chapter-opening pages and front matter (front matter uses lowercase roman if numbered at all).
- Table of contents page numbers match actual page numbers. Regenerate the TOC if anything shifted.
- Chapter breaks always recto (right-hand page). If a chapter ends on a recto, insert a blank verso so the next chapter starts recto.
- No orphaned section heads at the bottom of a page.

### Paper & print quality
- Cream paper is standard for fiction/narrative non-fiction and is the right call for this book. White paper looks harsher and is better suited to reference/technical.
- Show-through: hold a page up to a lamp. Some text from the opposite side is normal; heavy show-through means the ink density is too high or the paper is too thin (you can't fix the paper on KDP).
- Ink smudge test: rub a page firmly with a dry thumb across a dense paragraph. Modern KDP rarely smudges but check.

## 4. Iteration loop

Almost every first proof has fixes. Expect 2–3 proof rounds before approving.

1. Mark up the proof with sticky flags (color-coded: one color for interior, another for cover).
2. Log every issue in a single file — `kdp/proof-notes.md` alongside this doc is a reasonable home. Include page number, description, and fix.
3. Apply fixes to source. Rebuild interior PDF and cover PDF.
4. Re-run KDP's previewer. Don't skip this — previewer catches issues the proof can't, like PDF compatibility warnings.
5. Upload new files. KDP will ask you to re-approve the preview. Order a new proof.
6. Repeat.

Budget 3–6 weeks from first proof to approval if you want the book to look right.

## 5. Common gotchas

- **Spine text drift**: you changed the page count and forgot to regenerate the cover. The cover template's spine calculator takes page count as input — re-run it on every interior change.
- **Image downsampling**: some PDF export paths silently downsample images to 150 DPI "for web". Check the export settings — you want "Press Quality" or "High Quality Print" presets, not "Standard" or "Smallest File Size".
- **Font substitution on body text**: if you use a font Pandoc can't find, LaTeX falls back to Computer Modern without warning. Your proof will look wrong and you won't know why until you diff the font metadata. Embed the font explicitly in the template.
- **Color images going to grayscale badly**: reds and blues of similar luminance become indistinguishable. Re-render diagrams as grayscale-native, don't rely on the print pipeline to convert.
- **Mirror margins not set**: inside margin should be larger than outside (the gutter). If both are the same, text crawls into the binding. Pandoc's `geometry` package needs `twoside` and separate `inner`/`outer` values, not `left`/`right`.
- **Chapter one starts on verso**: lazy TOC = even-page chapter one. Always insert a blank page to force recto start.
- **Cover art resolution**: KDP rejects covers under 300 DPI at final size. A 6x9 cover at 300 DPI is 1800x2700 px for front alone; the full wraparound with spine is larger. If you're upscaling from a smaller original, regenerate at target size instead.
- **Approving too fast**: once you hit "Approve", the book goes live for sale within 72 hours. Do not approve on a proof you haven't physically received and reviewed. KDP's "Approve for publishing" button is not the same as "Order another proof".

## 6. When the proof is good

- All flagged issues resolved across at least two proof rounds.
- Someone other than the author has held the book and flipped through it without wincing.
- The cover looks right under different lighting (warm indoor, cool daylight, phone camera).
- You can open the book at random pages and the typography reads cleanly every time.

Then — and only then — approve.

## 7. Reusing this for future books

This workflow assumes 6x9 black-ink interior paperback. For other formats, adjust:

- **Trim size**: KDP's minimum inside margin changes with page count, not trim. Outside margins scale with trim — tighter margins on smaller trims look cramped.
- **Color interior**: triples printing cost per copy. Review at real printed size; color shifts on cream paper are larger than on white.
- **Hardcover**: KDP's hardcover spec is different (case bind, different gutter math). This doc does not cover hardcover.
- **Series**: first-book proof review is the expensive one. Subsequent books in the same series reuse typography and cover template — review cycles shorten to 1–2 proofs.
