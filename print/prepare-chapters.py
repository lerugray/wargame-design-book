#!/usr/bin/env python
"""
prepare-chapters.py — assemble docs/_chapters/*.md into a single
pandoc-ready markdown file for the KDP print build.

Strips Jekyll YAML front matter from each chapter, promotes its
`title:` field into a markdown `# H1` so pandoc can emit it as a
LaTeX \\chapter{}, and concatenates in canonical book order.
"""

from __future__ import annotations
import re
import sys
from pathlib import Path

CHAPTERS_DIR = Path(__file__).parent.parent / "docs" / "_chapters"

# Canonical book order. Acknowledgements is front matter (placed
# after TOC, before chapter 1). Appendices follow the main chapters
# in a..f order.
ORDER: list[str] = (
    ["acknowledgements.md"]
    + [f"chapter_{i:02d}.md" for i in range(1, 24)]
    + [
        "appendix_a_recommended_reading.md",
        "appendix_b_tools_and_resources.md",
        "appendix_c_sample_design_exercise.md",
        "appendix_d_march_rates.md",
        "appendix_e_the_workshops.md",
        "appendix_f_glossary.md",
    ]
)

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
TITLE_RE = re.compile(r'^title:\s*"?(.+?)"?\s*$', re.MULTILINE)
# Jekyll {{ site.baseurl }} prefix on image paths — pandoc can't interpret
# Liquid templating, so we strip the prefix and rely on --resource-path to
# find the images relative to docs/.
JEKYLL_BASEURL_RE = re.compile(r"\{\{\s*site\.baseurl\s*\}\}/")


def extract_title(frontmatter: str) -> str | None:
    m = TITLE_RE.search(frontmatter)
    return m.group(1).strip() if m else None


def prepare(path: Path) -> str:
    raw = path.read_text(encoding="utf-8")
    fm_match = FRONTMATTER_RE.match(raw)
    if not fm_match:
        # No front matter — keep raw content, no heading injection.
        return raw.rstrip() + "\n"

    frontmatter = fm_match.group(1)
    body = raw[fm_match.end():]
    # Strip Jekyll Liquid prefix so pandoc sees plain `assets/images/...` paths.
    body = JEKYLL_BASEURL_RE.sub("", body)
    title = extract_title(frontmatter)

    # Emit H1 only if the body doesn't already start with one.
    body_stripped = body.lstrip()
    if title and not body_stripped.startswith("# "):
        return f"# {title}\n\n{body.rstrip()}\n"
    return body.rstrip() + "\n"


def main() -> int:
    pieces: list[str] = []
    for name in ORDER:
        path = CHAPTERS_DIR / name
        if not path.exists():
            print(f"WARN: missing {name}", file=sys.stderr)
            continue
        pieces.append(prepare(path))

    # Join with double-newline so pandoc sees clear chapter breaks.
    # Write as raw UTF-8 bytes to sidestep Windows CP1252 stdout default.
    output = "\n\n".join(pieces).encode("utf-8")
    sys.stdout.buffer.write(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
