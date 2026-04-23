# Print Build

KDP-ready paperback PDF pipeline for *A Contemporary Guide to
Wargame Design*.

## First-time setup (one-shot, done 2026-04-23)

1. `winget install JohnMacFarlane.Pandoc` — markdown → LaTeX
2. `winget install MiKTeX.MiKTeX` — LaTeX → PDF via XeLaTeX
3. Enable MiKTeX package auto-install:
   `"C:/Users/rweis/AppData/Local/Programs/MiKTeX/miktex/bin/x64/initexmf.exe" --set-config-value=[MPM]AutoInstall=1`

## Build

```
bash print/build.sh
```

Output: `print/out/wargame-design-book.pdf`

First run pulls LaTeX packages (fontspec, geometry, fancyhdr,
etc.) as MiKTeX encounters them — takes 1-3 extra minutes.
Subsequent runs are ~30-60 seconds.

## Structure

- `metadata.yaml` — pandoc frontmatter (trim size, fonts, margins,
  header style). Edit this to tune typography.
- `prepare-chapters.py` — assembles `docs/_chapters/*.md` into a
  single pandoc-ready markdown file. Strips Jekyll front matter,
  promotes `title:` into `#` headings, orders chapters canonically.
- `build.sh` — the pipeline. Runs prepare-chapters, then pandoc,
  then outputs the PDF.
- `out/` — gitignored build output (PDF + intermediate markdown).

## KDP settings (per current metadata.yaml)

- Trim: 6 × 9 in (KDP standard)
- Inner margin: 0.875 in (gutter-side)
- Outer margin: 0.625 in
- Top/bottom margin: 0.75 in
- Body font: Georgia 11pt (installed on all Windows machines)
- Line spacing: 1.2
- Running heads: chapter name (verso), section name (recto)
- Page numbers: outer-corner footer
- Chapter breaks: always start on recto (openright)

## Known rough edges (first-pass output)

- **Font is Georgia, not Lora/Playfair Display.** Task spec calls
  for Lora body + Playfair Display chapter headings. Using
  Georgia for first-pass because it's installed by default. To
  switch: download Lora + Playfair Display from Google Fonts,
  install to Windows Fonts dir, change `mainfont` in
  metadata.yaml. Optional `header-includes` entry for
  `\setkomafont{chapter}{...}` if you want different font for
  chapter heads.
- **Stray CP1252 em-dash bytes (0x97).** Some chapter markdown
  files have bytes in the CP1252 encoding rather than valid UTF-8
  em-dashes. Shows as missing glyphs in output. Sweep with:
  `python -c "import pathlib; [p.write_bytes(p.read_bytes().replace(b'\\x97', b'\\xe2\\x80\\x94')) for p in pathlib.Path('docs/_chapters').glob('*.md')]"`
- **Front matter incomplete.** No title page, copyright page,
  acknowledgements placement — just a pandoc-generated TOC. Full
  front matter is wdb-003.
- **Cover is separate.** KDP uploads cover as its own artifact.
  See wdb-002.
- **Diagrams not yet verified in PDF.** The 11 diagram PNGs in
  `docs/assets/images/` are referenced in the Jekyll site but
  paths may need adjustment for the print build. Spot-check
  chapters 5, 6, 7, 10.
