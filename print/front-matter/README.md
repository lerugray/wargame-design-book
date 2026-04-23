# Front matter (print edition)

Scaffolding for the pages that precede Chapter 1 in the KDP paperback.
Assembly order here mirrors trade-paperback convention:

| Page | File                 | Purpose                                                  |
|------|----------------------|----------------------------------------------------------|
| i    | `half-title.md`      | Title only, on a recto (right-hand) page                 |
| ii   | —                    | Blank verso                                              |
| iii  | `title-page.md`      | Full title, subtitle, author, publisher imprint          |
| iv   | `copyright.md`       | Copyright, ISBN, edition, printing history               |
| v    | `dedication.md`      | Short dedication (optional — can be pulled if unused)    |
| vi   | —                    | Blank verso                                              |
| vii… | `toc.md`             | Table of contents (generated — see below)                |

The print build (`wdb-001`) concatenates these files in order before the
chapters, numbered with lowercase Roman numerals. Chapter 1 starts on
page 1 (Arabic) on the next available recto.

## Auto-generated table of contents

`toc.md` is a placeholder. The real TOC is produced at build time from the
front matter in `docs/_chapters/*.md`:

```
python generate-toc.py > toc.generated.md
```

`generate-toc.py` parses each chapter file's YAML front matter (title,
chapter_number, nav_order) and emits a clean markdown list. It deliberately
does NOT read the source `docs/_chapters/` files for anything but front
matter — the manuscript is hands-off.

## Placeholders

Fields that need human input are marked `{{TOKEN}}`. Current tokens:

- `{{ISBN_13}}` — paperback ISBN (KDP assigns one at publish time, or Ray
  supplies his own)
- `{{COPYRIGHT_YEAR}}` — first-publication year (currently 2026)
- `{{EDITION}}` — "First Edition", "Second Edition", etc.
- `{{BACK_COVER_HOOK}}`, `{{AUTHOR_BIO}}` — filled by `wdb-008`

The print build substitutes these via Pandoc metadata. Do not hand-edit them
in the final PDF.
