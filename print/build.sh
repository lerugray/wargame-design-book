#!/usr/bin/env bash
# build.sh — produce the KDP-ready print PDF of
# "A Contemporary Guide to Wargame Design".
#
# Requires:
#   - pandoc (winget install JohnMacFarlane.Pandoc)
#   - MiKTeX with xelatex on PATH (winget install MiKTeX.MiKTeX)
#   - Python 3 (for prepare-chapters.py)
#   - Fonts: Georgia (installed by default on Windows)
#
# Output:
#   print/out/wargame-design-book.pdf
#   print/out/book.md              (intermediate concatenated source)

set -euo pipefail

# Resolve paths relative to this script.
PRINT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$PRINT_DIR/.." && pwd)"
OUT_DIR="$PRINT_DIR/out"

mkdir -p "$OUT_DIR"

# Pandoc + xelatex paths. On Windows pip/winget-installed tools may
# not be on MSYS PATH; reference absolute paths when we know them.
PANDOC="${PANDOC:-C:/Users/rweis/AppData/Local/Pandoc/pandoc.exe}"
XELATEX="${XELATEX:-C:/Users/rweis/AppData/Local/Programs/MiKTeX/miktex/bin/x64/xelatex.exe}"

if [[ ! -x "$PANDOC" ]]; then
  echo "ERROR: pandoc not found at $PANDOC" >&2
  echo "Override via: PANDOC=/path/to/pandoc ./build.sh" >&2
  exit 1
fi

if [[ ! -x "$XELATEX" ]]; then
  echo "ERROR: xelatex not found at $XELATEX" >&2
  echo "Override via: XELATEX=/path/to/xelatex ./build.sh" >&2
  exit 1
fi

echo "[1/3] Assembling front matter + chapters -> $OUT_DIR/book.md"
{
  cat "$PRINT_DIR/front-matter.md"
  echo
  python "$PRINT_DIR/prepare-chapters.py"
} > "$OUT_DIR/book.md"

echo "[2/3] Pandoc -> XeLaTeX -> PDF (first run may be slow; MiKTeX auto-installs packages)"
"$PANDOC" \
  --from=markdown+smart \
  --metadata-file="$PRINT_DIR/metadata.yaml" \
  --pdf-engine="$XELATEX" \
  --pdf-engine-opt=-interaction=nonstopmode \
  --top-level-division=chapter \
  --standalone \
  --resource-path="$PROJECT_ROOT/docs" \
  "$OUT_DIR/book.md" \
  -o "$OUT_DIR/wargame-design-book.pdf"

echo "[3/3] Done: $OUT_DIR/wargame-design-book.pdf"
ls -lh "$OUT_DIR/wargame-design-book.pdf"
