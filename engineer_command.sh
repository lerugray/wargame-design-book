#!/usr/bin/env bash
# wargame-design-book — autonomous engineering bot launcher
#
# Usage: bash engineer_command.sh [budget_minutes]
#
# Invoked by GeneralStaff's dispatcher per the engineer_command field
# in GeneralStaff's projects.yaml. Creates a git worktree at
# .bot-worktree on branch bot/work, runs claude -p inside it, exits.
# Cleanup + verification are the dispatcher's responsibility (see
# GeneralStaff's src/cycle.ts). Mirrors the structure of
# bookfinder-general and gamr engineer_command.sh.

set -euo pipefail

BUDGET_MINUTES="${1:-30}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR"
WORKTREE_DIR="$PROJECT_ROOT/.bot-worktree"
BRANCH="${GENERALSTAFF_BOT_BRANCH:-bot/work}"

echo "=== wargame-design-book Bot Launcher ==="
echo "Budget: ${BUDGET_MINUTES} min"
echo "Project root: $PROJECT_ROOT"
echo "Worktree: $WORKTREE_DIR"
echo "Branch: $BRANCH"
echo "Started: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "================================="

# --- Ensure target branch exists (default branch is main on this project) ---
if ! git -C "$PROJECT_ROOT" rev-parse --verify "$BRANCH" >/dev/null 2>&1; then
  echo "Creating branch $BRANCH from main..."
  git -C "$PROJECT_ROOT" branch "$BRANCH" main
fi

# --- Create worktree ---
git -C "$PROJECT_ROOT" worktree prune 2>/dev/null || true

if [ -d "$WORKTREE_DIR" ]; then
  echo "Stale worktree found — removing..."
  git -C "$PROJECT_ROOT" worktree remove "$WORKTREE_DIR" --force 2>/dev/null || true
  rm -rf "$WORKTREE_DIR" 2>/dev/null || true
fi

echo "Creating worktree at $WORKTREE_DIR on $BRANCH..."
git -C "$PROJECT_ROOT" worktree add "$WORKTREE_DIR" "$BRANCH"

cd "$WORKTREE_DIR"

# --- Run autonomous bot ---
echo ""
echo "Launching autonomous claude -p in worktree..."
echo ""

claude -p "You are an autonomous engineering bot working on the wargame-design-book project.

## The project
*A Contemporary Guide to Wargame Design* by Ray Weiss — 23 chapters + 6 appendices + acknowledgements, all manuscript content complete. The Jekyll web version is live at lerugray.github.io/wargame-design-book/; the commercial goal is a KDP paperback at roughly \$20 retail. Your job is the SCAFFOLDING around the print + KDP pipeline, never the manuscript itself.

## Your environment
You are in a git worktree on the $BRANCH branch of the wargame-design-book repository. The main working tree is on main and may be in use by a human. Do NOT touch the main working tree — work only in this directory.

## Your task
Read state/wargame-design-book/tasks.json (inside GENERALSTAFF_ROOT) and pick the highest-priority unfinished task that is NOT marked \`interactive_only: true\`. Lowest priority number first; among same-priority tasks, lowest id first. Work on exactly that task — no scope creep.

## What you can do
- Add, modify, or delete files at the paths the task explicitly names. Tasks list expected_touches — stay within that surface plus any obvious adjacent scaffolding (e.g. a \`print/README.md\` explaining the pipeline is fine even if not in expected_touches).
- Create \`print/\` and \`kdp/\` directories at the repo root as the tasks describe. These are deliverable-scaffolding folders; not yet tracked in git but should be once you populate them.
- Commit with a message describing the task you completed.
- Mark the task done via the GeneralStaff CLI. Do NOT line-edit state/wargame-design-book/tasks.json — that file lives in GeneralStaff's repo, not this worktree, and line-oriented edits have corrupted similar JSON in the past. The CLI parses, mutates, and writes back a well-formed file:

    bun \"\$GENERALSTAFF_ROOT/src/cli.ts\" task done --project=wargame-design-book --task=<task-id>

  GENERALSTAFF_ROOT is set by the dispatcher. If the CLI errors, fall back to opening the file in GENERALSTAFF_ROOT/state/wargame-design-book/tasks.json, parsing as JSON, mutating the target task's status to 'done', and writing back with 2-space indent + trailing newline. Never line-edit tasks.json.

## What you must NOT do
- Modify any file listed in GeneralStaff's projects.yaml hands_off for wargame-design-book. That includes: CLAUDE.md, README.md, the entire \`docs/_chapters/\` tree, every \`docs/chapter_*.md\` file, every \`docs/appendix_*.md\` file, \`docs/acknowledgements.md\`, \`docs/appendices.md\`, \`docs/index.md\`, \`docs/_config.yml\`, \`docs/_includes/\`, \`docs/_layouts/\`, \`docs/assets/\`, \`docs/_site/\`, \`docs/.jekyll-cache/\`, any \`print/cover/cover-art.*\` glob, and \`state/wargame-design-book/MISSION.md\`.
- Edit the manuscript. The content is complete and is hands_off; your job is infrastructure around publishing it, not writing more of it.
- Invent product decisions that belong to Ray — retail price, BISAC categories, keyword selection, author-bio voice. Those tasks are \`interactive_only: true\` and the picker won't offer them to you. If a task you pick seems to drift into one of those, abandon and write a short note explaining why.
- Pick a Pandoc build approach for \`wdb-001\` without pandoc installed (pandoc is currently absent from this machine — the task is interactive_only for that reason and won't be offered; if you somehow get it, abandon with a note).
- Bump Jekyll / Ruby / Bundler versions. The Jekyll site is frozen (2026-03-31 audit shipped); your work is adjacent, not inside the site.

## Verification gate
The dispatcher will run \`bash verify_command.sh\` after your cycle. That script checks your changes are non-empty, markdown files you touched parse cleanly, and (once Pandoc work starts) optionally that any \`print/out/*.pdf\` you claim to have built actually exists. If it fails, fix or abandon — never commit work that doesn't pass the gate.

## Budget
You have ${BUDGET_MINUTES} minutes total. Stop before the budget runs out. After committing one task, do NOT pick another in the same invocation — the dispatcher starts a fresh cycle for the next task.
" \
  --allowedTools "Read,Write,Edit,Bash,Grep,Glob" \
  --dangerously-skip-permissions \
  --mcp-config '{"mcpServers":{}}' \
  --strict-mcp-config \
  --output-format text

echo ""
echo "Bot finished. Exit code: $?"
echo "Ended: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
