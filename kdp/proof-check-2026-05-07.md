# KDP proof-check followup — 2026-05-07

Scheduled agent fired 5 days after proof order (ordered 2026-05-02).

---

## Where the KDP submission stands as of 2026-05-02

The KDP draft was saved on 2026-05-02 with the following parameters (commits `61b2375` and earlier):

- **Interior:** `print/out/wargame-design-book.pdf` — 360pp B&W cream paper, 6×9 in.
- **Cover:** `print/out/wargame-design-book-cover.pdf` — wraparound, spine 0.9000 in (canvas 13.150 × 9.250 in), matte finish.
- **List price:** $24.99 USD, 60% royalty plan → $9.67/copy net (KDP-verified).
- **Marketplace prices:** C$34.99 / ¥3,799 / £19.99 / A$37.99 / €22.99 (DE/ES/FR/IT) / auto-converted for BE/IE/NL/PL/SE.
- **Territories:** All worldwide. **Expanded Distribution:** OFF. **Primary marketplace:** Amazon.com.
- **KDP previewer:** Passed with one informational notice (Pandoc annotations stripped from front-matter pages 3–9 — Ray reviewed and accepted).
- **Status:** Draft saved; physical proof ordered 2026-05-02; **Publish not yet clicked.**

---

## New development since 2026-05-02

**Commit `b1cb117` (2026-05-06)** landed on main after the proof order. It files the first-proof physical review in `print/PROOF-FEEDBACK-2026-05-06.md`. The proof **arrived and was reviewed on 2026-05-06**. Three issues were flagged.

---

## Proof status: Arrived — issues found, revision required

The proof arrived but it is **not clean**. The following three issues must be resolved before publishing. Section B gate items that are now blocked are called out below.

### Issue 1 — Back cover placeholder text

The back cover still prints `BACK COVER` placeholder text instead of real back-cover copy. The layout source was not swapped before submission.

**Section B gate impact:** B.1 item 4 (all proof-round fixes applied, final proof shows no remaining markups) — **BLOCKED.**

### Issue 2 — Single-word orphan page

One chapter ends with a single word on an otherwise blank page (widow/orphan page-break problem).

**Section B gate impact:** B.1 item 4 — **BLOCKED** (same gate item; must be batched with the back-cover fix).

### Issue 3 — Images print dark / hard to read

Generated images (diagrams) do not reproduce cleanly on KDP's standard B&W printer. Three options were evaluated. A Hammerstein audit (2026-05-06, archived in the proof feedback file) ranked them:

1. **Remove images entirely** — highest leverage; eliminates the problem and slightly reduces page count (lower print cost).
2. **Batch all fixes into one KDP revision** — don't split into a hotfix + image revision; that doubles proof-shipping cost and adds 3–14 days.
3. ~~Keep with web-version disclaimer~~ — not recommended; trains readers to distrust the physical product.
4. ~~Regenerate light-mode palette~~ — deprioritized as "stupid-industrious"; pipeline rework, color validation, likely reflowing text and adding pages.

**Counter-observation in the audit:** If any of the images are functional diagrams (hex maps, unit counters, mechanic flowcharts that readers need while designing), the correct move flips to convert the 3–5 load-bearing ones to high-contrast vector/line art and cut the rest. If they are purely atmospheric or decorative, cut all.

**Section B gate impact:** B.1 items 3 and 4 — **BLOCKED** until revision is submitted and a second proof is ordered, received, and reviewed clean.

---

## Decision required from Ray before acting

**Classify the existing images by function:**

- **Atmospheric / decorative** → cut all; follow the batched-revision recommendation.
- **Functional diagrams** (hex maps, counters, mechanic flowcharts that readers need while designing) → identify the 3–5 load-bearing ones, convert to high-contrast vector/line art, cut the rest. (The images referenced in `CLAUDE.md` Phase 2 — `hex-scale-comparison.png`, `counter-anatomy.png`, `hex-zoc-basic.png`, etc. — are plausibly functional; Ray's call.)

This is a taste-bearing call. Make it before any revision work starts.

---

## Section B gate — current status

### B.1 Files

- [ ] Interior PDF passes KDP previewer with zero errors AND zero warnings — *was passing; re-check after revision*
- [ ] Cover PDF matches spine width KDP calculated for final page count — *was correct at 360pp; re-check if page count changes after image removal*
- [ ] At least one physical proof has been ordered, received, and reviewed — **PROOF ARRIVED 2026-05-06; review complete; ISSUES FOUND → second proof required after revision**
- [ ] All proof-round fixes applied; final proof shows no remaining markups — **BLOCKED (3 open issues above)**

### B.2 Listing copy

- [ ] `print/copy/amazon-listing.md` — was drafted; confirm no changes needed
- [ ] `print/copy/author-bio.md` — confirm final draft approved by Ray
- [ ] Title + subtitle + series fields match across KDP listing, back cover, copyright page, title page — **back-cover placeholder fix may also touch title block; verify after fix**

### B.3 Discoverability

- [ ] 7 keywords selected — in place (see `kdp/chrome-claude-launch-prompt.md`)
- [ ] 2 BISAC categories — GAM001000 locked; secondary (HIS027060 vs DES016000) spot-check still pending
- [ ] Amazon Author Central page exists for Ray Weiss with bio + photo

### B.4 Pricing & royalty

- [x] List price $24.99 — confirmed
- [x] Royalty $9.67/copy at 360pp — KDP-verified 2026-05-02
- [x] Marketplace prices rounded — confirmed (see draft state above); **re-verify on pricing page if page count changes after revision**

### B.5 Operational

- [ ] Conflict Simulations LLC bank account on file with KDP
- [ ] Tax interview (W-9) completed
- [ ] Two review-request lists prepared (templates in `kdp/launch-checklist.md` Section C)
- [ ] Launch-day calendar slot blocked (minimum 2 hours)

---

## Recommended next actions (batched revision)

Per the Hammerstein sequencing recommendation in `print/PROOF-FEEDBACK-2026-05-06.md`:

1. **Classify the images** (see decision block above). Author's call — do this first.
2. **Replace the BACK COVER placeholder** with real back-cover copy in the layout source.
3. **Fix the single-word orphan page** (page-break adjustment in the relevant chapter).
4. **Apply the image decision** (remove all, or convert load-bearing + remove decorative).
5. **Run the pre-resubmit sweep:** gutter margins ≥0.5 in, font rendering, ToC vs. body alignment, orphans/widows full sweep, copyright/ISBN/colophon, blank-page handling at chapter breaks.
6. **Regenerate ToC** against new page numbers (if page count changes, spine width in cover PDF must be recalculated; KDP's spine formula is 0.0025 in × page count for cream paper).
7. **Submit single revised PDF to KDP.** Do not split into multiple revision cycles.
8. **Order a second physical proof.** Re-schedule a proof-check agent for 5 days after the second proof order date.

**Spine width note:** Current spine = 0.9000 in (360pp × 0.0025). If images are removed and page count drops (e.g., to ~350 pp), new spine = 0.875 in. Recalculate and rebuild the cover PDF before uploading the revision.

---

## When the second proof comes back clean: how to Publish

Once B.1 items 3 and 4 are cleared (second proof received, no markups), Ray clicks Publish in KDP Bookshelf directly:

**URL:** https://kdp.amazon.com/en_US/bookshelf

1. Find the title in KDP Bookshelf → click **"...Continue setup"** or **"Edit paperback content"**.
2. Navigate to the **Paperback Rights & Pricing** page (the final step).
3. Verify on screen before clicking Publish:
   - List price: **$24.99 USD**
   - Royalty displayed: **≈ $9.67** (if substantially different, page count likely drifted — stop and investigate)
   - Territories: **All territories (worldwide)**
   - Expanded Distribution: **OFF**
   - Marketplace prices (spot-check at minimum UK £19.99, DE €22.99, CA C$34.99, JP ¥3,799, AU A$37.99)
4. Click **Publish Your Paperback Book**.
5. KDP will show "your book will be live within 72 hours" — in practice 4–12 hours for a previously-reviewed manuscript. **Do not announce until the listing is live and the Buy button works.**

The operational launch-day sequence (T+0 morning check, emails, social posts) is in `kdp/launch-checklist.md` Section D.

For field-by-field KDP UI assistance on launch day, use the ready-to-paste prompt in `kdp/chrome-claude-launch-prompt.md` with Claude in Chrome.

---

## Physical proof focus points (for second proof review)

When the second proof arrives, pay specific attention to:

- **Pages 311, 313, 315, 316** — these were the wide-table fix sites in commit `d363318`; confirm tables fit within the text block and are legible.
- **Back cover** — barcode landing in the 2.0 × 1.2 in box in the lower-right corner; confirm placeholder text is fully replaced.
- **Spine text** — title and author name readable, not clipped.
- **Chapter endings** — the orphan-page fix; no chapter should end with a single word on an otherwise blank page.
- **Images (if any retained)** — high-contrast, legible without squinting on B&W cream paper in indoor light.

---

*Agent: scheduled 5-day proof-check, fired 2026-05-07. Proof arrived 2026-05-06 with open issues. Publish gate is NOT clear. Second proof required after batched revision.*
