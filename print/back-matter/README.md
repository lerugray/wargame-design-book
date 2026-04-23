# Back matter (print edition)

Scaffolding for pages that follow Chapter 23 (and the appendices) in the
KDP paperback. Assembly order:

| File                      | Purpose                                              |
|---------------------------|------------------------------------------------------|
| `acknowledgements.md`     | Pointer wrapper — content is at `docs/_chapters/acknowledgements.md` |
| `about-the-author.md`     | Author bio stub (populated by `wdb-008`)             |
| `also-by.md`              | "Also by Ray Weiss" list                             |

The print build (`wdb-001`) concatenates these after the last appendix.
Arabic page numbering continues unbroken from the body.

## Acknowledgements

The manuscript already contains `docs/_chapters/acknowledgements.md`, which
is hands-off content. The wrapper here (`acknowledgements.md`) is a thin
include directive that Pandoc resolves at build time — do NOT duplicate the
content into this directory.

## About the Author

`about-the-author.md` is a stub with `{{AUTHOR_BIO}}` tokens. `wdb-008`
replaces those with Ray's actual bio text. The stub defines the layout
(heading, photo slot, prose block) but holds no voiced copy.

## Also By

`also-by.md` lists Ray's other published wargame titles. Initial scaffold
is empty — Ray fills it when he decides which CSL titles to surface. Add
one line per title with year.

## Placeholders

Tokens resolved by Pandoc metadata at build time:

- `{{AUTHOR_BIO}}` — filled by `wdb-008`
- `{{AUTHOR_PHOTO}}` — path to headshot image (optional)
