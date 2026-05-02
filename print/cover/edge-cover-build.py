#!/usr/bin/env python3
"""Convert cover-final.svg to PDF via Edge headless print.

Fallback when cairosvg / Inkscape / rsvg-convert aren't available
on a Windows machine. Uses Microsoft Edge's --headless --print-to-pdf
mode (which is on every modern Windows install).

Usage:
    python edge-cover-build.py

Reads:
    cover-final.svg
Writes:
    ../out/wargame-design-book-cover.pdf
"""

from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

COVER_DIR = Path(__file__).resolve().parent
SVG_PATH = COVER_DIR / "cover-final.svg"
OUT_PDF = COVER_DIR.parent / "out" / "wargame-design-book-cover.pdf"

EDGE_CANDIDATES = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
]


def find_edge() -> Path:
    for p in EDGE_CANDIDATES:
        if p.exists():
            return p
    raise SystemExit("ERROR: msedge.exe not found in standard locations.")


def parse_svg_dims(svg: str) -> tuple[float, float]:
    m = re.search(r'width="([\d.]+)in"\s+height="([\d.]+)in"', svg)
    if not m:
        raise SystemExit("ERROR: could not parse width/height from SVG (expected inch units).")
    return float(m.group(1)), float(m.group(2))


def build_html(svg: str, w_in: float, h_in: float) -> str:
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>cover</title>
<style>
  @page {{ size: {w_in:.4f}in {h_in:.4f}in; margin: 0; }}
  html, body {{ margin: 0; padding: 0; width: {w_in:.4f}in; height: {h_in:.4f}in; }}
  svg {{ display: block; width: {w_in:.4f}in; height: {h_in:.4f}in; }}
</style>
</head>
<body>
{svg}
</body>
</html>
"""


def main() -> int:
    edge = find_edge()
    if not SVG_PATH.exists():
        raise SystemExit(f"ERROR: {SVG_PATH} not found.")
    svg = SVG_PATH.read_text(encoding="utf-8")
    w_in, h_in = parse_svg_dims(svg)
    html = build_html(svg, w_in, h_in)

    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        html_path = Path(f.name)

    try:
        url = html_path.as_uri()
        cmd = [
            str(edge),
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={OUT_PDF}",
            url,
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            print("STDOUT:", result.stdout, file=sys.stderr)
            print("STDERR:", result.stderr, file=sys.stderr)
            raise SystemExit(f"ERROR: edge --print-to-pdf exited {result.returncode}")
    finally:
        try:
            html_path.unlink()
        except OSError:
            pass

    if not OUT_PDF.exists():
        raise SystemExit("ERROR: edge claimed success but no PDF was written.")
    print(f"OK: wrote {OUT_PDF} ({OUT_PDF.stat().st_size:,} bytes)")
    print(f"     canvas: {w_in:.4f} x {h_in:.4f} in")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
