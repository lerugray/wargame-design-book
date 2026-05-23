# KDP re-submit — post audit-2026-05-21 cleanup

**Filed:** 2026-05-23 (Mac-evening session).
**Owner:** Ray (manual via KDP UI; requires Amazon login).
**Target:** This weekend.

## Context

The first editorial audit of *A Contemporary Guide to Wargame Design*
ran 2026-05-21 (`kdp/audit-2026-05-21.md`). Two waves of fixes landed:

- **2026-05-22 morning merge** (`6181825`): 5 hard factual errors,
  Tier 4 editorial defects, Tier 8 global-consistency passes
  (game-title italics, en-dashes, hex-and-counter hyphenation,
  OOB-on-first-use, number style).
- **2026-05-23 evening** (`8a6a151`): remaining Tier 3 judgment
  calls — Ch 7 Franco-Prussian War precision (army not country,
  formidable reputation vs highly regarded), Ch 10 Panzer Campaigns
  ("fluidity of its activations" not "fluid turn structure"),
  Ch 21 Van Riper ("stepped down as commander" not "resigned his
  command"). Tier 2.1 Roman march-rates was already addressed via
  the Vegetius framing sentence in the 2026-05-22 merge.

All audit-flagged items are now closed. The live website at
`https://lerugray.github.io/wargame-design-book/` reflects the cleaned
text (auto-deployed via GitHub Pages on push to `main`).

## Next step

The KDP paperback interior PDF needs to be rebuilt from the updated
`docs/_chapters/` source and uploaded to KDP as a revised edition.

### What Ray does (manual, ~30 min):

1. **Rebuild the print PDF.** Ask Claude in a fresh session: "rebuild
   the WDB print PDF from current source." Claude runs `bash
   print/build.sh` and produces the updated paperback interior in
   `print/out/`. (Cover unchanged — only interior needs re-upload
   unless Ray also wants to bump the edition number on the cover
   spine/back, which would require a cover rebuild.)
2. **Skim the new PDF** for layout regressions (page breaks, table
   formatting, font rendering). The text changes are minor (~6 lines
   across 23 chapters) so this should be quick.
3. **Log into KDP** at `kdp.amazon.com`. Go to the paperback's
   product page → "Edit paperback content" → upload the new interior
   PDF. KDP will run its automated review (~24-72 hr typical).
4. **Edition decision:** bump to "Second Edition" only if Ray wants
   the version delta visible to customers. For audit-cleanup tier
   fixes (mostly factual corrections), staying at "First Edition,
   revised" via in-place update is the simpler path — no spine/cover
   change needed and existing reviews/Look Inside roll over cleanly.
5. **Publish** when KDP review clears. Live listing updates within a
   few hours of approval.

### What Ray does NOT need to do this round:

- No metadata changes (title, subtitle, BISAC, keywords all unchanged).
- No price change (royalty-analysis.md figures still apply).
- No cover rebuild (unless choosing the "Second Edition" path).
- No description / A+ content update (text edits don't affect the
  listing copy in `print/copy/`).

## Reference

- Full audit findings: `kdp/audit-2026-05-21.md`
- Print build script: `print/build.sh`
- Launch checklist (fresh-launch playbook, mostly N/A here): `kdp/launch-checklist.md`
- Commits: `git log 0f5925d..8a6a151 -- docs/_chapters/` (the audit-applied range)

## Status

- [ ] Print PDF rebuilt
- [ ] PDF skimmed for layout regressions
- [ ] Uploaded to KDP
- [ ] KDP review cleared
- [ ] Live listing reflects new text
