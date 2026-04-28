#!/usr/bin/env python3
"""Reusable KDP paperback cover math and SVG rendering helpers."""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from pathlib import Path
from textwrap import wrap

PAPER_FACTORS = {
    "white": 0.002252,
    "cream": 0.0025,
    "color": 0.002347,
}

TRIM_SIZES_IN = {
    "5x8": (5.00, 8.00),
    "5.25x8": (5.25, 8.00),
    "5.5x8.5": (5.50, 8.50),
    "6x9": (6.00, 9.00),
    "7x10": (7.00, 10.00),
    "8.5x11": (8.50, 11.00),
}

BLEED_IN = 0.125
SPINE_TEXT_SAFETY_IN = 0.0625
MIN_PAGES_FOR_SPINE_TEXT = 80
IN_TO_MM = 25.4

SITE_PALETTE = {
    "paper": "#fdfbf7",
    "paper_alt": "#f5f0e8",
    "ink": "#1c1c2e",
    "body": "#2c2c3a",
    "muted": "#5a5a6e",
    "accent": "#7a3b1e",
    "accent_dark": "#5a2c14",
    "gold": "#b5933a",
    "rule": "#c4b49a",
    "white": "#ffffff",
}


@dataclass(frozen=True)
class CoverDimensions:
    pages: int
    paper: str
    trim: str
    trim_width: float
    trim_height: float
    spine_width: float
    bleed: float
    cover_width: float
    cover_height: float
    back_left: float
    spine_left: float
    front_left: float


@dataclass(frozen=True)
class CoverParams:
    title: str
    subtitle: str
    author: str
    pages: int = 360
    paper: str = "white"
    trim: str = "6x9"
    spine_title: str = "Wargame Design"
    spine_kicker: str = "A Contemporary Guide to"
    front_kicker: str = "On the Craft of"
    website: str = "lerugray.github.io/wargame-design-book"
    year: str = "2026"
    back_cover_copy: str = ""
    author_bio: str = ""


def spine_width_in(pages: int, paper: str = "white") -> float:
    """Return KDP spine width in inches: page count times paper factor."""
    if paper not in PAPER_FACTORS:
        raise ValueError(f"unknown paper type: {paper!r}; choose from {sorted(PAPER_FACTORS)}")
    if pages < 24:
        raise ValueError("KDP paperback minimum is 24 pages")
    if pages > 828 and paper == "white":
        raise ValueError("KDP paperback maximum is 828 pages for B&W white paper")
    return pages * PAPER_FACTORS[paper]


def cover_dimensions(pages: int = 360, paper: str = "white", trim: str = "6x9") -> CoverDimensions:
    if trim not in TRIM_SIZES_IN:
        raise ValueError(f"unknown trim {trim!r}; choose from {sorted(TRIM_SIZES_IN)}")
    trim_width, trim_height = TRIM_SIZES_IN[trim]
    spine = spine_width_in(pages, paper)
    return CoverDimensions(
        pages=pages,
        paper=paper,
        trim=trim,
        trim_width=trim_width,
        trim_height=trim_height,
        spine_width=spine,
        bleed=BLEED_IN,
        cover_width=(trim_width * 2) + spine + (BLEED_IN * 2),
        cover_height=trim_height + (BLEED_IN * 2),
        back_left=BLEED_IN,
        spine_left=BLEED_IN + trim_width,
        front_left=BLEED_IN + trim_width + spine,
    )


def convert(value_in: float, unit: str) -> float:
    return value_in * IN_TO_MM if unit == "mm" else value_in


def fmt_in(value: float) -> str:
    return f"{value:.4f}"


def _text_block(lines: list[str], x: float, y: float, class_name: str, size: float,
                line_height: float, anchor: str = "start", extra: str = "") -> str:
    attrs = f'class="{class_name}" font-size="{size:.3f}" text-anchor="{anchor}"'
    if extra:
        attrs = f"{attrs} {extra}"
    out = [f'    <text x="{fmt_in(x)}" y="{fmt_in(y)}" {attrs}>']
    for index, line in enumerate(lines):
        dy = 0 if index == 0 else line_height
        out.append(f'      <tspan x="{fmt_in(x)}" dy="{fmt_in(dy)}">{escape(line)}</tspan>')
    out.append("    </text>")
    return "\n".join(out)


def _wrap_placeholder(label: str, token: str, width: int = 46) -> list[str]:
    lines = [label, token]
    lines.extend(wrap("Ray fills this block in wdb-008; keep the space clear for now.", width=width))
    return lines


def _lines_from_prose(
    text: str,
    width: int,
    *,
    separate_paragraphs: bool = True,
) -> list[str]:
    """Wrap body copy. If separate_paragraphs is False, join all paragraphs and wrap as one block (denser)."""
    text = text.strip()
    if not separate_paragraphs:
        single = " ".join(text.split())
        return wrap(single, width=width, break_long_words=False)
    chunks = [p.strip() for p in text.split("\n\n") if p.strip()]
    lines: list[str] = []
    for index, para in enumerate(chunks):
        if index:
            lines.append("")
        lines.extend(wrap(para, width=width, break_long_words=False, replace_whitespace=False))
    return lines


# Back-cover layout (inches): hook and bio panels stay inside trim safe area; barcode y=7.52–8.72.
_BACK_HOOK_RECT = (1.1000, 5.0000, 3.5000)  # y, width, height
_BACK_BIO_RECT = (5.2600, 5.0000, 1.7000)
_BACK_HOOK_FONT = 0.130
_BACK_HOOK_LEADING = 0.205
_BACK_BIO_FONT = 0.115
_BACK_BIO_LEADING = 0.138
_BACK_HOOK_WRAP = 56
_BACK_BIO_WRAP = 74


def _front_title_lines(title: str) -> list[tuple[str, float, str, str]]:
    if title.lower() == "a contemporary guide to wargame design":
        return [
            ("A CONTEMPORARY", 0.545, "display ink", "font-weight=\"800\" letter-spacing=\"0.008\""),
            ("guide to", 0.360, "display ink", "font-weight=\"700\" letter-spacing=\"0.018\""),
            ("WARGAME", 0.665, "display accent", "font-weight=\"900\" letter-spacing=\"0.022\""),
            ("DESIGN", 0.665, "display accent", "font-weight=\"900\" letter-spacing=\"0.022\""),
        ]

    words = title.upper().split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        trial = " ".join(current + [word])
        if len(trial) > 17 and current:
            lines.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(" ".join(current))
    return [(line, 0.560 if len(lines) > 2 else 0.660, "display ink", "font-weight=\"800\" letter-spacing=\"0.020\"") for line in lines[:4]]


def render_cover_svg(params: CoverParams, *, placeholders: bool = False, guides: bool = True) -> str:
    dims = cover_dimensions(params.pages, params.paper, params.trim)
    p = SITE_PALETTE

    title = "{{TITLE}}" if placeholders else params.title
    subtitle = "{{SUBTITLE}}" if placeholders else params.subtitle
    author = "{{AUTHOR}}" if placeholders else params.author
    author_upper = "{{AUTHOR_UPPER}}" if placeholders else params.author.upper()
    spine_title = "{{SPINE_TITLE}}" if placeholders else params.spine_title
    spine_kicker = "{{SPINE_KICKER}}" if placeholders else params.spine_kicker
    front_kicker = "{{FRONT_KICKER}}" if placeholders else params.front_kicker.upper()
    website = "{{WEBSITE}}" if placeholders else params.website

    cw = dims.cover_width
    ch = dims.cover_height
    back_x = dims.back_left
    spine_x = dims.spine_left
    front_x = dims.front_left
    trim_y = dims.bleed
    front_center = front_x + dims.trim_width / 2
    back_inner_x = back_x + 0.625
    back_right = back_x + dims.trim_width - 0.625
    spine_center = spine_x + dims.spine_width / 2
    spine_safe_left = spine_x + SPINE_TEXT_SAFETY_IN
    spine_safe_right = spine_x + dims.spine_width - SPINE_TEXT_SAFETY_IN
    spine_line_left = spine_x + 0.125
    spine_line_right = spine_x + dims.spine_width - 0.125

    if placeholders:
        back_copy_lines = _wrap_placeholder(
            "BACK COVER COPY PLACEHOLDER", "{{BACK_COVER_COPY}}", width=_BACK_HOOK_WRAP
        )
        bio_lines = _wrap_placeholder(
            "ABOUT THE AUTHOR PLACEHOLDER", "{{ABOUT_AUTHOR_LINE}}", width=_BACK_BIO_WRAP
        )
    else:
        if params.back_cover_copy.strip():
            back_copy_lines = _lines_from_prose(
                params.back_cover_copy, _BACK_HOOK_WRAP, separate_paragraphs=False
            )
        else:
            back_copy_lines = _wrap_placeholder(
                "BACK COVER COPY PLACEHOLDER", "{{BACK_COVER_COPY}}", width=_BACK_HOOK_WRAP
            )
        if params.author_bio.strip():
            bio_lines = _lines_from_prose(
                params.author_bio, _BACK_BIO_WRAP, separate_paragraphs=False
            )
        else:
            bio_lines = _wrap_placeholder(
                "ABOUT THE AUTHOR PLACEHOLDER", "{{ABOUT_AUTHOR_LINE}}", width=_BACK_BIO_WRAP
            )

    hook_y, hook_w, hook_h = _BACK_HOOK_RECT
    bio_y, bio_w, bio_h = _BACK_BIO_RECT

    if placeholders:
        title_lines = [
            ("{{TITLE_LINE_1}}", 0.580, "display ink", "font-weight=\"800\" letter-spacing=\"0.020\""),
            ("{{TITLE_LINE_2}}", 0.580, "display accent", "font-weight=\"900\" letter-spacing=\"0.040\""),
        ]
    else:
        title_lines = _front_title_lines(title)

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<!-- KDP paperback cover: {dims.trim} trim, {dims.paper} paper, {dims.pages} pages, spine {dims.spine_width:.4f} in. -->',
        '<svg xmlns="http://www.w3.org/2000/svg"',
        f'     width="{cw:.4f}in" height="{ch:.4f}in"',
        f'     viewBox="0 0 {cw:.4f} {ch:.4f}">',
        "  <defs>",
        "    <style>",
        "      .paper { fill: " + p["paper"] + "; }",
        "      .paper-alt { fill: " + p["paper_alt"] + "; }",
        "      .ink { fill: " + p["ink"] + "; }",
        "      .body { fill: " + p["body"] + "; }",
        "      .muted { fill: " + p["muted"] + "; }",
        "      .accent { fill: " + p["accent"] + "; }",
        "      .gold { fill: " + p["gold"] + "; }",
        "      .display { font-family: 'Playfair Display', Georgia, serif; }",
        "      .lora { font-family: Lora, Georgia, 'Times New Roman', serif; }",
        "      .small { font-family: Lora, Georgia, 'Times New Roman', serif; text-transform: uppercase; }",
        "      .guide-trim { fill: none; stroke: #00B8D4; stroke-width: 0.010; }",
        "      .guide-safe { fill: none; stroke: #00B8D4; stroke-width: 0.006; stroke-dasharray: 0.035 0.025; }",
        "      .guide-bleed { fill: none; stroke: #E91E63; stroke-width: 0.010; stroke-dasharray: 0.055 0.040; }",
        "      .guide-spine { fill: none; stroke: #FFB300; stroke-width: 0.009; }",
        "    </style>",
        "  </defs>",
        "",
        f'  <rect x="0" y="0" width="{cw:.4f}" height="{ch:.4f}" class="paper"/>',
        f'  <rect x="{spine_x:.4f}" y="0" width="{dims.spine_width:.4f}" height="{ch:.4f}" class="paper-alt"/>',
        "",
        '  <g id="back-cover">',
        f'    <line x1="{back_inner_x:.4f}" y1="0.6200" x2="{back_right:.4f}" y2="0.6200" stroke="{p["rule"]}" stroke-width="0.012"/>',
        _text_block(["BACK COVER"], back_inner_x, 0.930, "small accent", 0.111, 0.155, extra='letter-spacing="0.030" font-weight="700"'),
        f'    <rect x="{back_inner_x:.4f}" y="{hook_y:.4f}" width="{hook_w:.4f}" height="{hook_h:.4f}" fill="none" stroke="{p["rule"]}" stroke-width="0.010" stroke-dasharray="0.060 0.040"/>',
        _text_block(
            back_copy_lines,
            back_inner_x + 0.150,
            hook_y + 0.200,
            "lora body",
            _BACK_HOOK_FONT,
            _BACK_HOOK_LEADING,
        ),
        f'    <line x1="{back_inner_x:.4f}" y1="{hook_y + hook_h + 0.0600:.4f}" x2="{back_inner_x + 1.500:.4f}" y2="{hook_y + hook_h + 0.0600:.4f}" stroke="{p["accent"]}" stroke-width="0.010"/>',
        _text_block(
            ["ABOUT THE AUTHOR"],
            back_inner_x,
            hook_y + hook_h + 0.3800,
            "small muted",
            0.111,
            0.155,
            extra='letter-spacing="0.030" font-weight="700"',
        ),
        f'    <rect x="{back_inner_x:.4f}" y="{bio_y:.4f}" width="{bio_w:.4f}" height="{bio_h:.4f}" fill="none" stroke="{p["rule"]}" stroke-width="0.010" stroke-dasharray="0.060 0.040"/>',
        _text_block(
            bio_lines,
            back_inner_x + 0.150,
            bio_y + 0.1800,
            "lora body",
            _BACK_BIO_FONT,
            _BACK_BIO_LEADING,
        ),
        f'    <rect x="{back_x + 3.750:.4f}" y="7.5200" width="2.0000" height="1.2000" fill="{p["white"]}" stroke="{p["ink"]}" stroke-width="0.006" stroke-dasharray="0.045 0.030"/>',
        _text_block(["KDP BARCODE", "PLACEHOLDER", "KDP auto-fills"], back_x + 4.750, 8.010, "small muted", 0.090, 0.190, anchor="middle", extra='letter-spacing="0.018"'),
    ]

    if website:
        parts.append(_text_block([website], back_inner_x, 8.890, "lora muted", 0.095, 0.110))

    parts.extend([
        "  </g>",
        "",
        '  <g id="spine">',
        f'    <line x1="{spine_line_left:.4f}" y1="0.6400" x2="{spine_line_right:.4f}" y2="0.6400" stroke="{p["gold"]}" stroke-width="0.010"/>',
        f'    <line x1="{spine_line_left:.4f}" y1="8.6100" x2="{spine_line_right:.4f}" y2="8.6100" stroke="{p["gold"]}" stroke-width="0.010"/>',
        f'    <g transform="translate({spine_center - 0.120:.4f} 7.8200) rotate(-90)">',
        f'      <text class="display muted" font-size="0.125" font-weight="700" letter-spacing="0.016">{escape(spine_kicker)}</text>',
        "    </g>",
        f'    <g transform="translate({spine_center + 0.060:.4f} 7.8200) rotate(-90)">',
        f'      <text class="display ink" font-size="0.190" font-weight="900" letter-spacing="0.030">{escape(spine_title.upper())}</text>',
        "    </g>",
        f'    <g transform="translate({spine_center:.4f} 1.8000) rotate(-90)">',
        f'      <text class="lora accent" font-size="0.167" font-weight="700" letter-spacing="0.028">{escape(author)}</text>',
        "    </g>",
        f'    <polygon points="{spine_center:.4f},8.2600 {spine_center + 0.140:.4f},8.3408 {spine_center + 0.140:.4f},8.5025 {spine_center:.4f},8.5833 {spine_center - 0.140:.4f},8.5025 {spine_center - 0.140:.4f},8.3408" fill="none" stroke="{p["accent"]}" stroke-width="0.010"/>',
        "  </g>",
        "",
        '  <g id="front-cover">',
        f'    <line x1="{front_x + 0.750:.4f}" y1="0.7200" x2="{front_x + 5.250:.4f}" y2="0.7200" stroke="{p["rule"]}" stroke-width="0.010"/>',
        _text_block([front_kicker], front_center, 1.080, "small accent", 0.111, 0.155, anchor="middle", extra='letter-spacing="0.045" font-weight="700"'),
    ])

    y = 2.050
    for index, (line, size, class_name, extra) in enumerate(title_lines):
        parts.append(_text_block([line], front_center, y, class_name, size, 0.100, anchor="middle", extra=extra))
        y += 0.640 if index == 0 else 0.760

    subtitle_lines = wrap(subtitle, width=42)
    if placeholders:
        subtitle_lines = ["{{SUBTITLE}}"]
    parts.extend([
        _text_block(subtitle_lines[:2], front_center, 5.030, "lora muted", 0.167, 0.275, anchor="middle", extra='font-style="italic"'),
        f'    <g id="counter" transform="translate({front_center:.4f} 6.1200) rotate(-3.2)">',
        f'      <rect x="-0.5000" y="-0.5000" width="1.0800" height="1.0800" fill="{p["accent_dark"]}" opacity="0.20"/>',
        f'      <rect x="-0.5400" y="-0.5400" width="1.0800" height="1.0800" fill="{p["accent"]}" stroke="{p["ink"]}" stroke-width="0.016"/>',
        f'      <rect x="-0.4860" y="-0.4860" width="0.9720" height="0.9720" fill="none" stroke="{p["paper"]}" stroke-width="0.011" opacity="0.55"/>',
        f'      <rect x="-0.3500" y="-0.2550" width="0.7000" height="0.4600" fill="none" stroke="{p["paper"]}" stroke-width="0.030"/>',
        f'      <line x1="-0.3500" y1="-0.2550" x2="0.3500" y2="0.2050" stroke="{p["paper"]}" stroke-width="0.030"/>',
        f'      <line x1="0.3500" y1="-0.2550" x2="-0.3500" y2="0.2050" stroke="{p["paper"]}" stroke-width="0.030"/>',
        f'      <text class="lora" x="0" y="0.4050" text-anchor="middle" font-size="0.194" font-weight="700" fill="{p["paper"]}" letter-spacing="0.010">4-6-2</text>',
        "    </g>",
        f'    <line x1="{front_center - 1.000:.4f}" y1="7.5800" x2="{front_center + 1.000:.4f}" y2="7.5800" stroke="{p["rule"]}" stroke-width="0.010"/>',
        _text_block([author_upper], front_center, 8.000, "lora ink", 0.225, 0.100, anchor="middle", extra='font-weight="700" letter-spacing="0.060"'),
    ])

    if params.year:
        parts.append(_text_block([params.year if not placeholders else "{{YEAR}}"], front_center, 8.700, "lora muted", 0.095, 0.110, anchor="middle", extra='letter-spacing="0.030"'))

    parts.extend([
        "  </g>",
    ])

    if guides:
        parts.extend([
            "",
            '  <g id="guides">',
            f'    <rect x="0" y="0" width="{cw:.4f}" height="{ch:.4f}" class="guide-bleed"/>',
            f'    <rect x="{BLEED_IN:.4f}" y="{BLEED_IN:.4f}" width="{cw - (BLEED_IN * 2):.4f}" height="{dims.trim_height:.4f}" class="guide-trim"/>',
            f'    <rect x="{back_x + 0.125:.4f}" y="{trim_y + 0.125:.4f}" width="{dims.trim_width - 0.250:.4f}" height="{dims.trim_height - 0.250:.4f}" class="guide-safe"/>',
            f'    <rect x="{front_x + 0.125:.4f}" y="{trim_y + 0.125:.4f}" width="{dims.trim_width - 0.250:.4f}" height="{dims.trim_height - 0.250:.4f}" class="guide-safe"/>',
            f'    <line x1="{spine_x:.4f}" y1="0" x2="{spine_x:.4f}" y2="{ch:.4f}" class="guide-spine"/>',
            f'    <line x1="{front_x:.4f}" y1="0" x2="{front_x:.4f}" y2="{ch:.4f}" class="guide-spine"/>',
            f'    <line x1="{spine_safe_left:.4f}" y1="0" x2="{spine_safe_left:.4f}" y2="{ch:.4f}" class="guide-spine" stroke-dasharray="0.035 0.025"/>',
            f'    <line x1="{spine_safe_right:.4f}" y1="0" x2="{spine_safe_right:.4f}" y2="{ch:.4f}" class="guide-spine" stroke-dasharray="0.035 0.025"/>',
            f'    <rect x="{back_x + 3.750:.4f}" y="7.5200" width="2.0000" height="1.2000" fill="none" stroke="#00C853" stroke-width="0.010" stroke-dasharray="0.040 0.030"/>',
            "  </g>",
        ])

    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def write_svg(path: Path, params: CoverParams, *, placeholders: bool = False, guides: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_cover_svg(params, placeholders=placeholders, guides=guides), encoding="utf-8")
