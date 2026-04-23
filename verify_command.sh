#!/usr/bin/env bash
# wargame-design-book — cycle verification gate.
#
# Runs AFTER the bot's claude -p cycle commits, from the dispatcher's
# worktree context (cwd is .bot-worktree/). Returns 0 if the cycle's
# changes are acceptable; non-zero causes verified_weak rollback.
#
# First-cut scope (matches the scaffolding-only engineer_command.sh):
#   1. Reject empty diffs — a cycle with zero changes didn't do the work.
#   2. Reject commits that touched the manuscript (defense-in-depth
#      against a hands_off bypass).
#   3. Reject commits that touched the Jekyll site config / layouts.
#   4. Parse-check any markdown file in the diff to catch obviously
#      broken YAML frontmatter before it lands on main.
#
# What this does NOT check (yet):
#   - Pandoc build output for wdb-001 (pandoc not installed on this
#     machine; wdb-001 stays interactive_only until the pipeline is
#     scaffolded + pandoc is on PATH).
#   - SVG validity for wdb-002 cover work (would need an SVG parser;
#     not worth the dep churn for a first cut).
#   - KDP proof / royalty-analysis arithmetic correctness. The bot
#     produces drafts; Ray reviews the numbers before they drive a
#     pricing decision.

set -euo pipefail

# 1. Non-empty diff against the prior commit (the bot committed its
#    work, so HEAD~1..HEAD should contain the cycle's changes).
if git diff --quiet HEAD~1 HEAD 2>/dev/null; then
  echo "verify: empty diff between HEAD~1 and HEAD — nothing shipped" >&2
  exit 1
fi

CHANGED="$(git diff --name-only HEAD~1 HEAD || true)"

if [ -z "$CHANGED" ]; then
  echo "verify: no files changed" >&2
  exit 1
fi

# 2. Block manuscript touches. Hands_off is enforced by the dispatcher
#    pre-cycle, but verifying post-cycle catches any path that slipped
#    through a mistaken bot claim.
if echo "$CHANGED" | grep -E '^docs/_chapters/|^docs/chapter_[0-9]+\.md$|^docs/appendix_[a-f]_.*\.md$|^docs/acknowledgements\.md$|^docs/appendices\.md$|^docs/index\.md$' >/dev/null; then
  echo "verify: cycle touched manuscript content (hands_off violation)" >&2
  echo "$CHANGED" | grep -E '^docs/_chapters/|^docs/chapter_[0-9]+\.md$|^docs/appendix_[a-f]_.*\.md$|^docs/acknowledgements\.md$|^docs/appendices\.md$|^docs/index\.md$' >&2
  exit 1
fi

# 3. Block Jekyll site config / layouts. The site is frozen; scaffolding
#    work is adjacent, not inside.
if echo "$CHANGED" | grep -E '^docs/_config\.yml$|^docs/_includes/|^docs/_layouts/|^docs/assets/' >/dev/null; then
  echo "verify: cycle touched Jekyll site surface (hands_off violation)" >&2
  echo "$CHANGED" | grep -E '^docs/_config\.yml$|^docs/_includes/|^docs/_layouts/|^docs/assets/' >&2
  exit 1
fi

# 4. Lightweight markdown sanity check. Catches obviously broken YAML
#    frontmatter (unterminated --- fences) before it lands on main.
#    Only runs on .md files added or modified in the cycle.
MD_FILES="$(echo "$CHANGED" | grep '\.md$' || true)"
if [ -n "$MD_FILES" ]; then
  while IFS= read -r md; do
    [ -z "$md" ] && continue
    [ ! -f "$md" ] && continue
    # Count leading --- fences. If the file starts with ---, there must
    # be a matching closing --- before any non-fence content begins.
    if head -n 1 "$md" | grep -q '^---$'; then
      if ! awk 'NR==1 && /^---$/{count=1; next} count==1 && /^---$/{count=2; exit} END{exit count!=2}' "$md"; then
        echo "verify: $md has unterminated YAML frontmatter" >&2
        exit 1
      fi
    fi
  done <<< "$MD_FILES"
fi

echo "verify: ok — $(echo "$CHANGED" | wc -l | tr -d ' ') file(s) changed, no hands_off violations"
exit 0
