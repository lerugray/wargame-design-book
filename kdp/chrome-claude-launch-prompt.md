# Chrome-Claude launch prompt (KDP listing entry)

Open the Chrome Claude extension on the kdp.amazon.com tab once
you're signed in and on the "Create a new title → Paperback" flow.
Copy everything below the `--- PROMPT START ---` line into the
chat. The prompt inlines every value Chrome-Claude needs so it
doesn't have to ask you for the listing copy mid-flow.

After paste, walk through KDP's three pages (Paperback Details,
Paperback Content, Paperback Rights & Pricing) in order. The
prompt walks Chrome-Claude through what each page wants and what
to verify before you click Publish.

For the BISAC top-100 spot-check (the one judgment call that needs
your eyes on the actual Amazon shelf), Chrome-Claude will pause
and ask you to open a second tab to the Amazon browse node it
names — that pause is by design.

Cross-reference doc (do not paste): `kdp/launch-checklist.md`
Section A is the field-by-field worksheet; this prompt is the
operational version that Chrome-Claude executes against KDP.

---

--- PROMPT START ---

I'm publishing my first paperback on KDP. Title:
**A Contemporary Guide to Wargame Design** by Ray Weiss. Standalone
title, no series, no subtitle, English, 360 pages, 6x9, B&W
interior on cream paper, matte cover. Print files are local
(`print/out/wargame-design-book.pdf` interior +
`print/out/wargame-design-book-cover.pdf` wraparound cover, spine
0.8197 in). I'll handle the file uploads myself when KDP asks.

Your job: be my second pair of eyes inside the KDP UI. Walk me
through each of the three KDP pages (Paperback Details, Paperback
Content, Paperback Rights & Pricing) field by field, hold the
pre-launch gate before I click Publish, and flag anything KDP shows
that disagrees with the values below.

## Paperback Details — values to enter

| Field | Value |
|---|---|
| Language | English |
| Book Title | A Contemporary Guide to Wargame Design |
| Subtitle | (leave blank) |
| Series | (leave blank) |
| Edition number | 1 |
| Author | Ray Weiss |
| Contributors | (leave blank) |
| Publishing rights | I own the copyright and hold the necessary publishing rights |
| Primary audience | Adults |
| Reading age | (leave blank) |
| Adult content | No |

### Description (long, paste verbatim into the Description field)

```
A Contemporary Guide to Wargame Design shows how historical board wargames get built. Ray Weiss has spent more than a decade designing and publishing them. The book covers the full path from first idea to finished prototype: research, scope, scale, orders of battle, movement, combat systems, sequence of play, supply, morale, victory conditions, playtesting, rules writing, development, and publication.

Wargames look complicated from the outside: dense maps, counters full of numbers, rulebooks that run for dozens of pages. Under that complexity, a good wargame is a small set of decisions: what the game is about, what the players can do, what to leave out.

The book treats design as work. Why does one combat results table feel right and another feel arbitrary? How do you decide whether a hex represents 500 meters or 50 kilometers, and when a unit needs separate ratings for attack, defense, morale, and movement?

A tactical game about infantry combat needs different tools than an operational game about supply lines. A card-driven game needs different habits than a hex-and-counter design. The book shows you how experienced designers think through those problems, test their assumptions, and cut what does not serve the game.

The primary audience is hobbyist wargamers designing their first game. Board game designers curious about conflict simulation, professional wargamers studying the commercial craft, and experienced designers stuck on a project will also find it useful.

You do not need a publishing contract, a warehouse, or a giant art budget to start. You need a subject you care about, enough research to understand it, and a design small enough to finish. This book shows you the rest.
```

### Keywords (7 total, one per slot)

1. wargame design
2. board game design
3. tabletop game design
4. conflict simulation
5. designing wargames
6. hex and counter wargames
7. historical board games

All ≤50 characters. None duplicates the exact title.

### Categories (2 total) — judgment call needed

**Primary (locked):** GAMES & ACTIVITIES / Board Games (BISAC GAM001000).
Path in KDP picker: `Crafts, Hobbies & Home → Games & Activities → Board Games`.

**Secondary — judgment call:** I'm choosing between two options.
Default leaning is HIS027060 (cleaner audience). Before I lock the
secondary, I want you to pause me and have me open a second Amazon tab
to spot-check the top 20 in each candidate shelf. Look for: at
least 30% of the top 20 should be plausibly the same audience as
a wargame design book.

- **Candidate A — DESIGN / Games (BISAC DES016000)**
  - Amazon browse node: `Books → Computers & Technology → Programming → Game Programming` (`/zgbs/books/10806593011`)
  - Risk: Amazon maps this to the video-game programming shelf.
    Top-100 includes Roblox / Unity / Blender programming books.
    If I see <30% tabletop-relevant titles in top 20, reject this.
- **Candidate B — HISTORY / Military / Strategy (BISAC HIS027060)**
  - Amazon browse node: `Books → History → Military → Strategy`
  - Cleaner audience match per my pre-flight note. Wargamers read
    this shelf. Risk: "design" angle disappears from category browse.

When we get to the Categories step, ask me which I want and have me
verify with the spot-check before I click Save.

## Paperback Content

| Field | Value |
|---|---|
| Print ISBN | KDP-assigned free ISBN (don't buy own for Amazon-only distribution) |
| Imprint | (default — leave whatever KDP fills with the free ISBN) |
| Publication date | (leave blank — KDP fills with go-live) |
| Print options | Black & white interior, cream paper, 6 x 9 in, paperback, matte cover |
| Bleed | No bleed |
| Manuscript | I'll upload `wargame-design-book.pdf` |
| Cover | I'll upload `wargame-design-book-cover.pdf` (wraparound, spine 0.8197 in) |

After upload: KDP will run its previewer. Have me confirm **zero
errors AND zero warnings** before letting me proceed. If anything
fails, do not let me click "Approve" — we abort and fix the file.

## Paperback Rights & Pricing

| Field | Value |
|---|---|
| Territories | All territories (worldwide rights) |
| Primary marketplace | Amazon.com |
| Royalty plan | 60% (only option for paperback) |
| List price (US) | **$24.99** |
| Other marketplace prices | "Calculate from US price" then sanity-check (see below) |
| Expanded Distribution | OFF (leave for post-launch) |

### Royalty sanity check

KDP's pricing page should show a per-copy royalty. At $24.99 on a
360-page B&W 6x9 paperback with $5.32 print cost:

- $24.99 × 0.6 = $14.994
- $14.994 - $5.32 = **$9.67 per copy**

If KDP shows substantially different (under $8 or over $11), flag
it — likely the page count drifted. Do not proceed past the pricing
page until we understand any discrepancy.

### Marketplace currency rounding

KDP auto-converts $24.99 to local currencies. Targets to manually
round toward when KDP lands at "ugly" numbers like £19.97 or €22.49:

| Marketplace | Round to |
|---|---|
| Amazon UK (GBP) | £19.99 |
| Amazon DE/FR/IT/ES (EUR) | €22.99 or €23.99 |
| Amazon CA (CAD) | C$34.99 |
| Amazon AU (AUD) | A$37.99 or A$39.99 |
| Amazon JP (JPY) | ¥3,799 |
| Amazon BR (BRL) | R$129.90 |
| Amazon MX (MXN) | MX$449 or MX$499 |
| Amazon IN (INR) | ₹1,999 |

Don't chase precise currency parity. Pricing memorability matters
more than FX precision. Skip overrides for marketplaces I don't
expect traffic from.

## Pre-Publish gate (hold here before I click Publish)

Before letting me click the final Publish button, walk through
this gate with me. If any item is unchecked, we don't publish.

### Files
- [ ] KDP previewer passed with **zero errors AND zero warnings**
  on both interior and cover
- [ ] Cover spine width matches KDP's calculated value for 360 pages
- [ ] At least one physical proof has been ordered, received, and
  reviewed (this is days of lead time — if I skipped it, ask me)

### Listing copy
- [ ] Description pasted matches the long body above (you can ask
  me to scroll back to the field and read the first sentence aloud)
- [ ] Title + author consistent: "A Contemporary Guide to Wargame
  Design" by Ray Weiss

### Discoverability
- [ ] All 7 keywords entered, each ≤50 chars
- [ ] BISAC categories: GAM001000 + (HIS027060 OR DES016000 — the
  one I locked after the spot-check)
- [ ] Amazon Author Central page exists for Ray Weiss (I should
  have set this up beforehand — ask if I haven't)

### Pricing
- [ ] List price = $24.99
- [ ] Royalty per copy ≈ $9.67 (within $0.50)
- [ ] Marketplace prices manually rounded for any I expect traffic from

### Operational
- [ ] Conflict Simulations LLC bank account on file with KDP
- [ ] Tax interview (W-9) completed
- [ ] Two review-request lists drafted (prelaunch + launch-day —
  templates are in `kdp/launch-checklist.md` Section C)
- [ ] At least 2 hours blocked tomorrow morning for the launch-day
  sequence (T+0 in `kdp/launch-checklist.md` Section D)

## Mode of operation

- Walk one page at a time. After each page, summarize what was
  entered and ask me to confirm before moving on.
- If KDP asks for a field I haven't named here, ask me — don't
  guess.
- For the BISAC step, pause and direct me to open the spot-check
  tabs.
- For the previewer step, do not let me proceed past warnings.
- For the final Publish click, walk the gate above item by item.
  If a box is unchecked, refuse to give the green light.

I'll narrate what I'm seeing on each page. Start by asking which
KDP page I'm currently on so we begin in the right place.

--- PROMPT END ---

## Notes for Ray (don't paste)

- The prompt inlines the listing copy + values so Chrome-Claude
  doesn't depend on file access. If you want to swap any values
  later (e.g. choose a different secondary BISAC after the
  spot-check), edit and re-paste.
- The pre-publish gate's "physical proof" item is the longest-lead
  thing on the list. If you haven't ordered a proof yet, that's
  the real blocker — KDP proof shipping is days, not hours.
- After launch, append a `## Launch retrospective` section to this
  file capturing anything that surprised you in the actual KDP
  flow, so the next book benefits.
