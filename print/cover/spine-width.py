#!/usr/bin/env python3
"""
KDP paperback spine-width calculator.

KDP's documented paper factors (inches per interior page):
  - Black & white on white paper:  0.002252
  - Black & white on cream paper:  0.0025
  - Premium color:                 0.002347

Spine width = interior page count * paper_factor

Also emits full-cover canvas dimensions for a given trim size.
KDP full-cover canvas:
  width  = (trim_width * 2) + spine_width + (bleed * 2)
  height = trim_height + (bleed * 2)
Bleed is 0.125" on all outer edges for KDP paperbacks.

Usage:
  python spine-width.py --pages 340
  python spine-width.py --pages 340 --paper cream
  python spine-width.py --pages 340 --trim 6x9 --unit mm
"""

from __future__ import annotations

import argparse
import sys

PAPER_FACTORS = {
    "white": 0.002252,
    "cream": 0.0025,
    "color": 0.002347,
}

TRIM_SIZES_IN = {
    "5x8":     (5.00, 8.00),
    "5.25x8":  (5.25, 8.00),
    "5.5x8.5": (5.50, 8.50),
    "6x9":     (6.00, 9.00),
    "7x10":    (7.00, 10.00),
    "8.5x11":  (8.50, 11.00),
}

BLEED_IN = 0.125
SPINE_TEXT_SAFETY_IN = 0.0625  # KDP requires >= 80pp before spine text; keep text 1/16" off spine edges

MIN_PAGES_FOR_SPINE_TEXT = 80
IN_TO_MM = 25.4


def spine_width_in(pages: int, paper: str) -> float:
    if paper not in PAPER_FACTORS:
        raise ValueError(f"unknown paper type: {paper!r}; choose from {sorted(PAPER_FACTORS)}")
    if pages < 24:
        raise ValueError("KDP paperback minimum is 24 pages")
    if pages > 828:
        raise ValueError("KDP paperback maximum is 828 pages (B&W on white)")
    return pages * PAPER_FACTORS[paper]


def cover_canvas_in(pages: int, paper: str, trim: str) -> dict:
    if trim not in TRIM_SIZES_IN:
        raise ValueError(f"unknown trim {trim!r}; choose from {sorted(TRIM_SIZES_IN)}")
    tw, th = TRIM_SIZES_IN[trim]
    spine = spine_width_in(pages, paper)
    width = (tw * 2) + spine + (BLEED_IN * 2)
    height = th + (BLEED_IN * 2)
    return {
        "trim_width":   tw,
        "trim_height":  th,
        "spine_width":  spine,
        "bleed":        BLEED_IN,
        "cover_width":  width,
        "cover_height": height,
        "front_left":   BLEED_IN + spine + tw,  # x-offset where the front cover starts
        "spine_left":   BLEED_IN + tw,          # x-offset where the spine starts
        "back_left":    BLEED_IN,               # x-offset where the back cover starts (after left bleed)
    }


def convert(value_in: float, unit: str) -> float:
    return value_in * IN_TO_MM if unit == "mm" else value_in


def main() -> int:
    p = argparse.ArgumentParser(description="KDP paperback spine-width calculator.")
    p.add_argument("--pages", type=int, required=True, help="interior page count")
    p.add_argument("--paper", choices=sorted(PAPER_FACTORS), default="white")
    p.add_argument("--trim", choices=sorted(TRIM_SIZES_IN), default="6x9")
    p.add_argument("--unit", choices=["in", "mm"], default="in")
    args = p.parse_args()

    try:
        dims = cover_canvas_in(args.pages, args.paper, args.trim)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    u = args.unit
    def fmt(v: float) -> str:
        return f"{convert(v, u):.4f} {u}"

    print(f"KDP paperback cover — {args.trim} trim, {args.paper} paper, {args.pages} pages")
    print(f"  spine width     : {fmt(dims['spine_width'])}")
    print(f"  cover canvas    : {fmt(dims['cover_width'])} x {fmt(dims['cover_height'])}")
    print(f"  bleed (each side): {fmt(dims['bleed'])}")
    print(f"  back-cover x    : {fmt(dims['back_left'])}  (width {fmt(dims['trim_width'])})")
    print(f"  spine x         : {fmt(dims['spine_left'])}  (width {fmt(dims['spine_width'])})")
    print(f"  front-cover x   : {fmt(dims['front_left'])}  (width {fmt(dims['trim_width'])})")
    if args.pages < MIN_PAGES_FOR_SPINE_TEXT:
        print(f"  note: {args.pages} pages < {MIN_PAGES_FOR_SPINE_TEXT} — KDP disallows spine text at this page count")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
