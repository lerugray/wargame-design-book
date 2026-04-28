# WDB Pre-Submission Visual QA

Date: 2026-04-28

Interior reviewed: `print/out/wargame-design-book.pdf`

Table-bearing source files identified with `^|` scan:
- `docs/_chapters/chapter_09.md` (`Combat Resolution`)
- `docs/_chapters/appendix_c_sample_design_exercise.md` (`Appendix C: Sample Design Exercise`)
- `docs/_chapters/appendix_d_march_rates.md` (`Appendix D: Historical Movement Rates`)

## Mechanical Fixes Applied

- `docs/_chapters/chapter_09.md`, PDF page 108: moved the Sedan 1940 national combat matrix figure so it appears after the CRT discussion paragraph instead of floating into the middle of the following sentence. Before: the figure interrupted the paragraph beginning "caring about individual formations." After: the figure and caption sit between complete paragraphs. Severity: MINOR. Fix type: mechanical.

## Taste-Call Findings

- `docs/_chapters/appendix_c_sample_design_exercise.md`, PDF pages 293-297: several intended lists render as run-in hyphen-separated prose after bold lead-ins (`Key locations`, `Terrain types you will need`, `Questions to answer`, `Requirements`, `Decisions to make`, `Required sections`). This is visibly awkward but readable. Severity: MINOR. Proposed fix: add proper Markdown list separation and rebuild; this is mechanical, but it may change pagination, so Ray should approve before KDP upload.

- `docs/_chapters/appendix_d_march_rates.md`, PDF pages 317-318: supply-constraint lists render as run-in hyphen-separated prose after bold lead-ins (`Early modern armies`, `Pre-railroad armies`, `Napoleonic era`, `World War II`). Severity: MINOR. Proposed fix: add proper Markdown list separation and rebuild; test rebuild changed the interior page count from 360 to 362, so this should be a Ray decision because the cover sprint has already shipped.

- `docs/_chapters/appendix_d_march_rates.md`, PDF pages 319-320: the Comparative Summary table breaks across pages with a repeated header and no overflow. It is dense but legible. Severity: COSMETIC. Proposed fix: optional table redesign or split by era; taste call, not applied.

## Pages Reviewed

- Front matter: PDF pages 1-12, 12 pages.
- Table chapter: `chapter_09.md`, PDF pages 97-110, 14 pages.
- Table appendix: `appendix_c_sample_design_exercise.md`, PDF pages 289-300, 12 pages.
- Table appendix: `appendix_d_march_rates.md`, PDF pages 301-322, 22 pages.
- Sample non-table chapter: `chapter_05.md`, PDF pages 47-61, 15 pages.
- Sample non-table chapter: `chapter_13.md`, PDF pages 154-164, 11 pages.
- Sample non-table chapter: `chapter_20.md`, PDF pages 241-252, 12 pages.
- Final pages: PDF pages 356-360, 5 pages.

Total targeted pages reviewed: 103.

## Out-of-Scope Findings

- `print/build.sh` still has CRLF line endings, so `bash print/build.sh` fails before the build starts. I rebuilt with the equivalent direct PowerShell/Python plus Pandoc/LuaLaTeX commands. Severity: MINOR for production workflow, not customer-visible. Proposed fix: normalize `print/build.sh` line endings in a separate tooling pass.

- The regenerated PDF remains 360 pages, matching the pre-QA interior page count. This avoids disturbing the already-shipped cover geometry.

## Verdict

NEEDS-RAY-REVIEW

The table pages do not show KDP-rejection problems: no table overflows into the gutter, no unreadable columns, no empty table rows, and long tables repeat headers when they break. The one applied mechanical fix cleans up the Chapter 9 figure placement without changing page count. Ray should decide whether to accept the visible run-in list formatting in Appendices C/D or approve a pagination-changing cleanup before KDP submission.
