#!/usr/bin/env python3
"""Build editable SVG cover sources and optional PDF/PNG previews."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

from kdp_cover import CoverParams, cover_dimensions, render_cover_svg, write_svg


ROOT = Path(__file__).resolve().parents[2]
COVER_DIR = Path(__file__).resolve().parent
COPY_DIR = ROOT / "print" / "copy"
OUT_DIR = ROOT / "print" / "out"


def _md_slice(text: str, start_header: str, end_header: str) -> str:
    i0 = text.index(start_header)
    i0 = text.find("\n", i0) + 1
    i1 = text.index(end_header, i0)
    return text[i0:i1].strip()


def load_back_cover_hook() -> str:
    path = COPY_DIR / "back-cover-hook.md"
    body = _md_slice(path.read_text(encoding="utf-8"), "## Selected: Candidate 2", "## Alternates")
    chunks = [p.strip() for p in body.split("\n\n") if p.strip() and p.strip() != "---"]
    return "\n\n".join(chunks)


def load_short_author_bio() -> str:
    path = COPY_DIR / "author-bio.md"
    return _md_slice(path.read_text(encoding="utf-8"), "## Short bio (150 words)", "## Long bio")


def export_with_cairosvg(svg_text: str, pdf_path: Path | None, png_path: Path | None, dpi: int) -> bool:
    try:
        import cairosvg  # type: ignore
    except Exception:
        return False

    if pdf_path:
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        cairosvg.svg2pdf(bytestring=svg_text.encode("utf-8"), write_to=str(pdf_path), dpi=dpi)
    if png_path:
        png_path.parent.mkdir(parents=True, exist_ok=True)
        cairosvg.svg2png(bytestring=svg_text.encode("utf-8"), write_to=str(png_path), dpi=dpi)
    return True


def export_with_cli(svg_path: Path, pdf_path: Path | None, png_path: Path | None, dpi: int) -> bool:
    inkscape = shutil.which("inkscape")
    if inkscape:
        if pdf_path:
            pdf_path.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run([inkscape, str(svg_path), "--export-type=pdf", f"--export-filename={pdf_path}"], check=True)
        if png_path:
            png_path.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run([inkscape, str(svg_path), "--export-type=png", f"--export-dpi={dpi}", f"--export-filename={png_path}"], check=True)
        return True

    rsvg = shutil.which("rsvg-convert")
    if rsvg:
        if pdf_path:
            pdf_path.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run([rsvg, "-f", "pdf", "-o", str(pdf_path), str(svg_path)], check=True)
        if png_path:
            png_path.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run([rsvg, "-f", "png", "-d", str(dpi), "-p", str(dpi), "-o", str(png_path), str(svg_path)], check=True)
        return True

    return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a KDP wraparound paperback cover.")
    parser.add_argument("--title", default="A Contemporary Guide to Wargame Design")
    parser.add_argument("--subtitle", default="A practical, opinionated guide to designing historical board wargames")
    parser.add_argument("--author", default="Ray Weiss")
    parser.add_argument("--pages", type=int, default=364)
    parser.add_argument("--paper", choices=["white", "cream", "color"], default="white")
    parser.add_argument("--trim", choices=["5x8", "5.25x8", "5.5x8.5", "6x9", "7x10", "8.5x11"], default="6x9")
    parser.add_argument("--spine-title", default="Wargame Design")
    parser.add_argument("--spine-kicker", default="A Contemporary Guide to")
    parser.add_argument("--front-kicker", default="On the Craft of")
    parser.add_argument("--website", default="lerugray.github.io/wargame-design-book")
    parser.add_argument("--year", default="2026")
    parser.add_argument("--svg", type=Path, default=COVER_DIR / "cover-final.svg")
    parser.add_argument("--template-svg", type=Path, default=COVER_DIR / "cover-template.svg")
    parser.add_argument("--template-filled-svg", type=Path, default=COVER_DIR / "cover-template-filled.svg")
    parser.add_argument("--pdf", type=Path, default=OUT_DIR / "wargame-design-book-cover.pdf")
    parser.add_argument("--png", type=Path, default=OUT_DIR / "wargame-design-book-cover.png")
    parser.add_argument("--dpi", type=int, default=150)
    parser.add_argument("--no-render", action="store_true", help="write SVG sources only")
    parser.add_argument("--require-render", action="store_true", help="fail if PDF/PNG export tooling is unavailable")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    back_copy = load_back_cover_hook()
    author_bio = load_short_author_bio()
    params = CoverParams(
        title=args.title,
        subtitle=args.subtitle,
        author=args.author,
        pages=args.pages,
        paper=args.paper,
        trim=args.trim,
        spine_title=args.spine_title,
        spine_kicker=args.spine_kicker,
        front_kicker=args.front_kicker,
        website=args.website,
        year=args.year,
        back_cover_copy=back_copy,
        author_bio=author_bio,
    )

    write_svg(args.svg, params, placeholders=False, guides=True)
    write_svg(args.template_svg, params, placeholders=True, guides=True)
    write_svg(args.template_filled_svg, params, placeholders=True, guides=True)

    dims = cover_dimensions(args.pages, args.paper, args.trim)
    print(f"cover SVG: {args.svg}")
    print(f"template SVG: {args.template_svg}")
    print(f"spine width: {dims.spine_width:.4f} in")
    print(f"canvas: {dims.cover_width:.4f} x {dims.cover_height:.4f} in")

    if args.no_render:
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    upload_svg = OUT_DIR / "wargame-design-book-cover-upload.svg"
    upload_svg_text = render_cover_svg(params, placeholders=False, guides=False)
    upload_svg.write_text(upload_svg_text, encoding="utf-8")

    rendered = export_with_cairosvg(upload_svg_text, args.pdf, args.png, args.dpi)
    if not rendered:
        rendered = export_with_cli(upload_svg, args.pdf, args.png, args.dpi)

    if not rendered:
        message = (
            "PDF/PNG export skipped: install Python package cairosvg, Inkscape, "
            "or librsvg's rsvg-convert, then rerun this script."
        )
        if args.require_render:
            print(message, file=sys.stderr)
            return 1
        print(message)
        return 0

    if args.pdf:
        print(f"cover PDF: {args.pdf}")
    if args.png:
        print(f"cover PNG: {args.png}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
