#!/usr/bin/env python3
"""
Generate the print-edition table of contents from chapter front matter.

Reads every *.md under docs/_chapters/, parses YAML front matter (no PyYAML
dependency — a small line-oriented parser handles the flat schema Jekyll
uses here), and emits a markdown TOC sorted by nav_order.

Output layout matches trade-paperback convention:
  - Chapters listed by number and title
  - Appendices listed separately (no number prefix)
  - Acknowledgements last

Page numbers are NOT emitted here. Pandoc fills those in when it builds the
PDF — the TOC entries are cross-references (Pandoc `\ref{}` via the
`--toc` pipeline). This script just produces the headings and order.

Usage:
    python generate-toc.py                  # print to stdout
    python generate-toc.py -o toc.generated.md

The script resolves docs/_chapters/ relative to the repo root so it runs
from anywhere. Exit codes: 0 on success, 2 on parse error.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
CHAPTERS_DIR = REPO_ROOT / "docs" / "_chapters"

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FIELD_RE = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*):\s*"?(.*?)"?\s*$')


def parse_front_matter(text: str) -> dict:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}
    fields: dict = {}
    for line in m.group(1).splitlines():
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        fm = FIELD_RE.match(line)
        if not fm:
            continue
        key, value = fm.group(1), fm.group(2)
        if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
            fields[key] = int(value)
        else:
            fields[key] = value
    return fields


def collect_entries(chapters_dir: Path) -> list[dict]:
    if not chapters_dir.is_dir():
        raise SystemExit(f"error: chapters dir not found: {chapters_dir}")
    entries = []
    for path in sorted(chapters_dir.glob("*.md")):
        fm = parse_front_matter(path.read_text(encoding="utf-8"))
        if "title" not in fm or "nav_order" not in fm:
            print(f"warning: skipping {path.name} — missing title/nav_order", file=sys.stderr)
            continue
        entries.append({
            "title": fm["title"],
            "nav_order": fm["nav_order"],
            "chapter_number": fm.get("chapter_number"),
            "path": path,
        })
    entries.sort(key=lambda e: e["nav_order"])
    return entries


def render(entries: list[dict]) -> str:
    lines = ["# Contents", ""]
    chapters = [e for e in entries if e["chapter_number"] is not None]
    appendices = [
        e for e in entries
        if e["chapter_number"] is None and not e["title"].lower().startswith("acknowledg")
    ]
    acks = [e for e in entries if e["title"].lower().startswith("acknowledg")]

    if chapters:
        for e in chapters:
            lines.append(f"{e['chapter_number']}. {e['title']}")
        lines.append("")

    if appendices:
        lines.append("## Appendices")
        lines.append("")
        for e in appendices:
            lines.append(f"- {e['title']}")
        lines.append("")

    if acks:
        for e in acks:
            lines.append(f"- {e['title']}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate print TOC from chapter front matter.")
    parser.add_argument("-o", "--output", type=Path, help="write to file instead of stdout")
    parser.add_argument(
        "--chapters-dir",
        type=Path,
        default=CHAPTERS_DIR,
        help=f"override chapters dir (default: {CHAPTERS_DIR})",
    )
    args = parser.parse_args()

    entries = collect_entries(args.chapters_dir)
    out = render(entries)

    if args.output:
        args.output.write_text(out, encoding="utf-8")
    else:
        sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
