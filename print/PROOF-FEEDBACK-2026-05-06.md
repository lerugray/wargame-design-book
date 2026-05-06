# WDB first-proof feedback — 2026-05-06

Physical proof received via KDP. Author observations + Hammerstein
audit-this-decision verbatim.

## Author-observed issues

1. **Back cover** still prints `BACK COVER` placeholder text
   instead of real back-cover copy. (Layout / back-matter source
   wasn't replaced before submission.)
2. **One chapter ends with a single word on an otherwise blank
   page** — orphan widow / page-break problem.
3. **Generated images print dark / hard to read.** Three options
   considered: (a) leave + add intro acknowledgement pointing
   readers to the web version, (b) remove images entirely,
   (c) regenerate images in light-mode palette suitable for
   print.

## Hammerstein audit (openrouter qwen3.6-plus, $0.01008, 71s)

### Plain English summary (verbatim)

Fix the back cover and the single-word page immediately — they're
trivial layout corrections that must be clean before shipping.
For the images, remove them. Regenerating a light-mode palette
will burn pipeline time and likely increase page count, while a
disclaimer signals a broken physical product to your audience.
Batch all three fixes into one KDP revision to avoid doubling
proof-cycle delays and shipping costs.

### Ranked priority (verbatim)

1. **Remove images entirely (Option b).** Highest leverage. KDP's
   print cost scales linearly with page count; cutting images
   reduces unit cost and eliminates the dark-print problem at
   zero regeneration cost. Wargame designers reading a design
   book prioritize mechanics, diagrams, and text clarity.
   Pipeline-generated atmospheric art adds visual noise in print
   and competes with dense technical prose. The work gradient is
   zero; the payoff is immediate cost reduction and cleaner
   typography.
2. **Batch all fixes into a single revision.** The back-cover
   placeholder and single-word orphan are <1 hour of layout
   work. Splitting them into a hotfix + image revision burns
   two KDP review cycles (3-7 days each), doubles proof-shipping
   costs, and fragments the correction log. Submit everything
   at once.
3. **Keep with web-version disclaimer (Option a).** Low leverage.
   A disclaimer trains the reader to distrust the physical
   product. It's a structural apology, not a fix. Only viable
   if the images are legally or structurally mandatory (they
   aren't).

### Deprioritize (verbatim)

- **Regenerate light-mode palette (Option c).** Stupid-industrious
  risk. Requires pipeline rework, color-profile validation, KDP
  bleed/margin re-checks, and likely forces text reflow that adds
  pages. The work gradient is steep; the payoff is marginal for a
  POD book where readers will flip to digital if they want color.
  The "smaller version" framing here disguises a pipeline grind
  as a pragmatic compromise.

### Pre-resubmit sweep checklist (verbatim)

- **Gutter margins & spine bleed:** KDP's default margins choke
  text near the binding. Verify ≥0.5" gutter for page counts
  >150.
- **Font rendering collapse:** Screen-optimized fonts (thin
  weights, custom wargame typefaces) lose stroke weight on KDP's
  standard printers. Check for missing glyphs or collapsed
  serifs.
- **ToC vs. body alignment:** Page numbers shift when images are
  removed or page breaks change. Regenerate the ToC *after* all
  layout fixes lock.
- **Orphans/widows sweep:** Run a full chapter-end and
  paragraph-break scan. KDP's formatter frequently leaves 1-2
  line orphans in dense blocks.
- **Copyright/ISBN/colophon:** Verify the ISBN matches the print
  edition (not ebook), copyright year is current, and rights
  statements cover generated imagery if any are retained.
- **Blank-page handling at chapter breaks:** KDP inserts forced
  blank pages for odd/even chapter starts. Ensure they're truly
  blank (no headers/footers/page numbers) or intentionally
  designed.

### Counter-observation (load-bearing — verbatim)

The ranking assumes the images are atmospheric or
pipeline-generated art. If they are actually functional diagrams
(hex maps, unit counters, mechanic flowcharts) that readers
*need* to reference while designing, removing them breaks the
book's utility. In that case, the correct move is a targeted
conversion of only the 3-5 load-bearing images to high-contrast
vector/line-art, then remove the rest. The tradeoff flips from
"cut all" to "convert the essential, cut the decorative."

### Recommendation (verbatim)

Remove images, fix back cover + orphan, regenerate ToC, submit
single revision. Total time: ~2-3 hours. Total cost: one KDP
proof cycle.

---

## Decision still required from author (Ray)

Before acting on the Hammerstein recommendation, classify the
existing images by function:

- **Atmospheric / decorative** → cut all, follow the recommendation.
- **Functional diagrams** (hex maps, counters, mechanic
  flowcharts that readers need while designing) → identify the
  3-5 load-bearing ones, convert to high-contrast vector / line
  art, cut the rest.

The classification call is taste-bearing (audience expectation
of "what counts as a load-bearing diagram in a wargame design
book"). Author's call.

## Sequencing the revision

Per Hammerstein's batched-revision recommendation:

1. Classify the images per the decision above.
2. Replace the BACK COVER placeholder with real back-cover copy.
3. Fix the single-word orphan page (page-break adjustment in the
   relevant chapter).
4. Apply the image decision (remove all, OR convert load-bearing
   + remove decorative).
5. Run the pre-resubmit sweep checklist (gutter, fonts, ToC,
   orphans, copyright, blank-page handling).
6. Regenerate ToC against the new page numbers.
7. Submit the single revised PDF to KDP.

Total estimated effort: 2-3 hours (assumes Option b, image
removal). Add ~1-2 hours per converted load-bearing image if
classification surfaces them.
