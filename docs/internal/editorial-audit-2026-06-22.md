# WDB editorial "human-editor" audit — 2026-06-22

Cross-chapter repetition + per-chapter artifice pass. All 23 chapters. LLM reads routed to
Ollama (glm-5.2). Triggered by Ray catching the AMFIOG-in-ch21+ch22 redundancy in the printed
proof. Triage order below.

## PLUS (Ray, 2026-06-22): book-wide em-dash strip
The book was meant to be stop-slopped but still contains em-dashes. Ray's standard: little to
no em-dashes except in charts / where absolutely needed. Treat em-dashes as a defect from an
incomplete prior pass, NOT voice. A book-wide em-dash strip (replace with periods / commas /
colons / restructure; preserve meaning + charts) is part of this cleanup.

## (A) Cross-chapter repetition — highest priority
1. **AMFIOG — ch21 + ch22 (consecutive).** Both run a marquee "Case Study: A Mighty Fortress
   Is Our God" with the same Munster scene-setting. FIX IN PROGRESS: ch21 swapped to a
   *Veridian Contraption* case study (drafts/ch21-vc-casestudy-draft.md). Also trim the
   duplicated scene-setting in ch22 and cross-reference.
2. **Prigozhin's March of Justice — ch06 + ch15.** Marquee case study twice (OOB ratings in
   ch06; prototyping speed in ch15). Ch15 opens "discussed in detail in Chapter 6" then retells
   the premise anyway — the disclaimer is itself a tell. Fix: ch15 references ch06 and keeps
   ONLY the prototyping-speed lesson, no premise re-tell.
3. **Rostov '41 — ch12 + ch19.** Marquee case study twice (victory conditions; publisher
   development). Non-consecutive, lower urgency, but the same premise paragraph repeats.
4. **1916 / Sedan 1940 — recurring pair across 7+ chapters.** ch01 and ch04 use a near-identical
   "I chose strategic level for Verdun" framing. One should change angle or compress to a ref.
5. **Imperial Bayonets — default operational example in 8+ chapters** (ch04-11). Different facet
   each time, but reads like a crutch by ch11. Lower priority.

## (B) Per-chapter artifice — most blatant
- **ch22 ("AI and the Designer's Toolkit") — heaviest tells in the book** (ironic). "## What AI
  Does Poorly / ## What AI Does Well" listicle headers; anaphora triads ("It cannot... It
  cannot... It cannot..."); balanced-clause AI-summarizing-AI ("Used well... Used poorly...");
  "what becomes possible when time is no longer the bottleneck" essay-opener. Ray's voice shows
  in the case study + the burnout passage; the scaffolding sections don't match.
- **ch01** — "It includes... It includes... It includes..." audience triad; "You do not need...
  You do not need... You do need..." parallel.
- **ch13 ("Naval and Air")** — "You have three options. First... Second... Third..." + "exists
  on a spectrum from full abstraction to standalone simulation."
- **ch20 ("Publishing")** — rigid "Traditional publishing means... / Self-publishing means... /
  Digital-first means..." definitional openers (textbook, not an author who ran a publisher).
- **ch16 ("Playtesting")** — anaphora triads ("Every X is a Y", "If they X, you need to Y").
- **ch10 ("Sequence of Play")** — rhetorical-question triad + verbatim restatement of the
  opening thesis as the closing paragraph.
