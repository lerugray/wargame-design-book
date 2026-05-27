# WDB print rebuild — home-PC handoff (2026-05-27)

**Filed:** 2026-05-27 Mac-morning session.
**Receiving session:** home-PC CC, in `wargame-design-book/`.
**Goal:** rebuild the KDP-ready paperback interior PDF from current
source so Ray can upload it to KDP via Amazon's UI.

This is the rebuild step queued in
`kdp/kdp-resubmit-2026-05-23.md` (the master KDP-resubmit doc). Read
that file first if you want the full audit-history context; this
handoff just covers the build step itself.

## What's already done

- Post-audit cleanup is fully merged on `main` (`6181825` +
  `8a6a151`). All audit-2026-05-21 Tier 1/2/3/4/8 fixes are in source.
- The live website at <https://lerugray.github.io/wargame-design-book/>
  reflects the cleaned text (GitHub Pages auto-deploy on push to main).
- The cosmetic stub for `print/back-matter/about-the-author.md` +
  `also-by.md` (`{{AUTHOR_BIO}}` / `{{ALSO_BY_LIST}}` placeholders) is
  Ray's call whether to populate before this build OR skip (no
  regression vs prior edition). **Surface the question before
  building** if the placeholders are still present; don't decide
  unilaterally. If Ray says skip, proceed; if he says populate, get
  the content from him first.

## What this session does

1. **Sync the repo.**
   - `git -C <wdb-path> pull --ff-only origin main` (the WDB default
     branch is `main`, not `master` — confirmed on commit `a6302b6`).
   - Confirm `git status` is clean. If there are uncommitted local
     changes, surface them — don't blindly stash.
2. **Check the build prerequisites.**
   - `print/build.sh` uses `lualatex` (TeX Live) + Lora + Playfair
     Display fonts. Home-PC has these installed (the build has run
     here before). If `lualatex` isn't on PATH or the fonts can't be
     resolved, surface the gap — do NOT try to install TeX Live or
     fonts autonomously (that's a major install Ray should drive).
3. **Run the build.**
   - From the repo root: `bash print/build.sh`.
   - The script generates `print/out/wargame-design-book.pdf`.
   - Builds typically take ~1-3 minutes; lualatex is verbose. Capture
     stdout/stderr to a file for diagnostic if anything goes wrong.
4. **Verify the artifact.**
   - The PDF exists at `print/out/wargame-design-book.pdf`.
   - File size is sane (the prior PDF was ~12-15 MB — anything
     drastically smaller suggests a truncated build; drastically
     larger suggests a font-embed regression).
   - `mtime` is fresh (today, not the May-9 stale PDF flagged in
     yesterday's session note).
   - Optional spot check: open the PDF, flip to chapter 7
     (Franco-Prussian War) or chapter 21 (Van Riper) and confirm the
     audit-2026-05-21 text-fix language is present. Not strictly
     required — `git log 0f5925d..8a6a151 -- docs/_chapters/` confirms
     the source has the fixes; the PDF inherits them.
5. **Report to Ray.**
   - "Built PDF at `print/out/wargame-design-book.pdf` (size XXX MB,
     mtime <today>). Ready for the KDP UI upload step."
   - Don't go further. The KDP upload is Ray's manual step via Amazon's
     web UI — see `kdp/kdp-resubmit-2026-05-23.md` §"What Ray does"
     steps 3-5.

## What this session does NOT do

- **Do not upload to KDP.** That's Ray's manual step.
- **Do not bump edition** ("Second Edition" vs "First Edition,
  revised"). Per the kdp-resubmit doc, in-place revision is the simpler
  path; staying at First Edition revised preserves reviews + Look
  Inside continuity.
- **Do not touch the cover.** Interior-only re-upload; cover hasn't
  changed.
- **Do not modify metadata / BISAC / keywords / description / A+
  content / pricing.** None of those changed this round.
- **Do not auto-populate the back-matter stub** without surfacing the
  question first (see step 1 above).

## Common build hazards

If the build fails:

- **Font not found** ("Lora-Regular.ttf not found" / similar): fonts
  aren't installed at the OS level OR not on the lualatex font path.
  Surface to Ray; this is a setup gap, not a code issue.
- **Lualatex undefined commands** (rare; lualatex is stable): try a
  clean rebuild by deleting `print/out/` first and re-running.
- **`prepare-chapters.py` errors**: the script preprocesses the
  Jekyll source into LaTeX-friendly chapter files. If it fails,
  surface the error; don't edit `_chapters/` source as a workaround.
- **Image / asset missing**: same shape — surface, don't paper over.

## Reference

- Master KDP-resubmit doc: `kdp/kdp-resubmit-2026-05-23.md`
- Full audit findings: `kdp/audit-2026-05-21.md`
- Print build script: `print/build.sh`
- Source chapters: `docs/_chapters/`
- Audit-applied commit range: `git log 0f5925d..8a6a151 -- docs/_chapters/`

## Status

- [ ] Repo synced (git pull clean)
- [ ] Build prerequisites verified (lualatex + Lora + Playfair Display)
- [ ] Back-matter stub question surfaced to Ray (if placeholders present)
- [ ] `bash print/build.sh` ran clean
- [ ] `print/out/wargame-design-book.pdf` exists, fresh mtime, sane size
- [ ] Build location reported back to Ray
