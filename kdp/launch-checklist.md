# KDP Launch Checklist

A reusable, fill-in-the-blanks playbook for taking a KDP paperback from "interior + cover approved" to "live and selling on Amazon." Sister doc to `proof-workflow.md` (which gets you to an approved proof) and `royalty-analysis.md` (which sets the price).

This doc is content-neutral. The actual listing copy, author bio, keywords, BISAC categories, and final price live in their own files because they are voice-sensitive or business decisions Ray makes:

- **Listing description (short hook + long body)** → drafted in `kdp/listing-description.md` (task wdb-007)
- **Author bio + back-cover hook** → drafted in `kdp/author-bio.md` (task wdb-008)
- **7 keywords + 2 BISAC categories** → chosen in `kdp/keywords-and-categories.md` (task wdb-009)
- **Final retail price** → decided in `kdp/pricing-decision.md` (task wdb-010, downstream of `royalty-analysis.md`)

This checklist references those files; it does not duplicate their content.

---

## Section A — Listing fields worksheet

These are the fields KDP's "Paperback Details" + "Paperback Content" + "Paperback Rights & Pricing" pages ask for. Fill the worksheet in this doc as you go, then copy-paste into KDP. Do not type into KDP first — saving partial state in their UI is unreliable.

### A.1 Paperback Details

| Field | Value | Source |
|---|---|---|
| Language | English | — |
| Book Title | A Contemporary Guide to Wargame Design | — |
| Subtitle | _(fill in or leave blank)_ | Ray decides |
| Series | _(blank — this is a standalone)_ | — |
| Series number | _(N/A)_ | — |
| Edition number | 1 | bump for revised editions |
| Author (primary) | Ray Weiss | matches docs site + manuscript |
| Contributors | _(blank unless adding editor / illustrator credit)_ | — |
| Description | → see `kdp/listing-description.md` | wdb-007 |
| Publishing rights | I own the copyright and hold the necessary publishing rights | — |
| Primary audience | Adults | wargame audience is adult |
| Reading age | _(leave blank for adult title)_ | — |
| Keywords (up to 7) | → see `kdp/keywords-and-categories.md` | wdb-009 |
| Categories (up to 2) | → see `kdp/keywords-and-categories.md` | wdb-009 |
| Adult content | No | — |

### A.2 Paperback Content

| Field | Value | Source |
|---|---|---|
| Print ISBN | _(KDP-assigned free ISBN)_ unless Ray buys own | KDP free ISBN is fine for Amazon-only distribution |
| Imprint | _(if KDP free ISBN: leave default)_ / _(if own ISBN: "Conflict Simulations LLC" or other)_ | depends on ISBN choice |
| Publication date | _(leave blank — KDP fills with go-live date)_ | — |
| Print options | Black & white interior, cream paper, 6 x 9 in, paperback, matte cover | matches print pipeline (`print/metadata.yaml`) |
| Bleed | No bleed | interior has no full-bleed art; flip to "Bleed" only if that changes |
| Manuscript | upload `print/out/wargame-design-book.pdf` | from wdb-001 build |
| Cover | upload `print/cover/out/cover-final.pdf` | from wdb-002 once interactive cover work lands |

### A.3 Paperback Rights & Pricing

| Field | Value | Source |
|---|---|---|
| Territories | All territories (worldwide rights) | default unless rights are encumbered |
| Primary marketplace | Amazon.com | — |
| Royalty plan | 60% (only option for paperback) | — |
| List price (US) | → see `kdp/pricing-decision.md` | wdb-010 |
| Other marketplace prices | "Calculate from US price" (KDP auto-converts) | re-check after launch — currency rounding can land at ugly numbers |
| Expanded Distribution | _(leave OFF by default)_ | enables only after launch settles; cuts royalty further and rarely moves units for niche non-fiction |

---

## Section B — Pre-launch readiness gate

Do not hit "Publish" until every box below is checked. Each unchecked box is a launch you'll regret.

### B.1 Files
- [ ] Interior PDF passes KDP previewer with zero errors AND zero warnings
- [ ] Cover PDF matches the spine width KDP calculated for the final page count
- [ ] At least one physical proof has been ordered, received, and reviewed against `proof-workflow.md`
- [ ] All proof-round fixes applied; final proof shows no remaining markups

### B.2 Listing copy
- [ ] `kdp/listing-description.md` has both short hook (≤200 char) and long description (≤4000 char) and has been run through `/stop-slop`
- [ ] `kdp/author-bio.md` final draft approved by Ray (bio appears on Amazon Author Central + back cover)
- [ ] Title + subtitle + series fields match across: KDP listing, back cover, copyright page, title page

### B.3 Discoverability
- [ ] 7 keywords selected (`kdp/keywords-and-categories.md`); each is ≤50 chars; none duplicate the title
- [ ] 2 BISAC categories selected; both have been spot-checked against existing top-100 books in that category to confirm fit
- [ ] Amazon Author Central page exists for Ray Weiss; bio, photo, and at least one prior title (if applicable) are populated

### B.4 Pricing & royalty
- [ ] Final list price set per `kdp/pricing-decision.md`
- [ ] Royalty per copy at chosen price recalculated and recorded (KDP shows it on the pricing page; sanity-check against `royalty-analysis.md`)
- [ ] Marketplace prices (UK, DE, etc.) sanity-checked — KDP's auto-convert can land at £19.97 or €22.49; round manually to memorable numbers if it does

### B.5 Operational
- [ ] Conflict Simulations LLC bank account on file with KDP for royalty deposits
- [ ] Tax interview completed (W-9 for US; W-8BEN if non-US)
- [ ] Two separate review-request lists prepared (see Section C)
- [ ] Launch-day calendar slot blocked — minimum 2 hours for the first-24h checks

---

## Section C — Review-request email templates

KDP launches die in the first two weeks if there are no reviews — Amazon's algorithm needs social proof to start surfacing the book. Lining up reviews **before** launch is the single highest-leverage thing you can do.

Two lists, two templates. Send the prelaunch list one week before launch, the launch-day list on go-live morning.

### C.1 Prelaunch list (people who already have / are getting a free copy)

Audience: friends in the wargame design community, playtesters who saw drafts, fellow CSL designers, anyone Ray has given a PDF or proof to.

```
Subject: my book is going up on Amazon next [WEEKDAY] — small ask

Hey [NAME],

Quick heads-up: A Contemporary Guide to Wargame Design goes live on
Amazon paperback next [WEEKDAY]. You've already [seen the draft / got
a proof / heard me complain about it for two years], so you know what
it is.

The ask: when it goes live, would you grab the Amazon link, buy a
copy if you don't have one, and leave an honest review? Even three
sentences makes a real difference for a new title — Amazon's
algorithm needs early signal to start showing the book to people
who'd actually want it.

I'll send the link the morning it's live. No pressure if the timing
is bad — just wanted to flag it now so it's not a surprise.

Thanks,
Ray
```

Notes:
- Do NOT offer free copies in exchange for reviews. Amazon ToS prohibits incentivized reviews and will pull them (and possibly suspend the listing).
- "Honest review" is the magic phrase — it's what Amazon expects to see in any pre-launch outreach.
- Personalize line one. A list of identical emails reads as a list of identical emails.

### C.2 Launch-day list (broader network)

Audience: Twitter/Mastodon followers, mailing list, Discord/forum communities Ray is part of, BGG presence.

```
Subject: out now: A Contemporary Guide to Wargame Design (paperback)

After [N years/months] of working on it, A Contemporary Guide to
Wargame Design is live on Amazon as a paperback today.

[ AMAZON LINK ]

23 chapters on the design choices behind hex-and-counter wargames —
how scale, ZOC, sequence of play, victory conditions, and combat
resolution actually drive the feel of a game. Free web version is
still up at lerugray.github.io/wargame-design-book/ if you want to
sample before buying.

If you read it and have thoughts, an Amazon review (even a short
one) helps more than you'd think. And if you know someone designing
their first game, please pass it along.

Thanks for following the project,
Ray
```

Notes:
- Lead with the link. People skim.
- Mention the free web version. Counterintuitively this drives MORE paperback sales — readers who sample tend to buy the physical.
- Don't beg. One review request, no follow-ups.

---

## Section D — D-day sequence

Pin this somewhere visible on launch day. Times are illustrative — adjust to Ray's morning routine.

### T-3 days
- Final KDP previewer pass on interior + cover. If anything fails, abort launch. Do not "we'll fix it after."
- Confirm prelaunch email list is loaded into your mail client with the link placeholder.
- Double-check `kdp/pricing-decision.md` against KDP's calculated royalty — has anything changed (page count drift, new printing-cost table)?

### T-1 day (the night before)
- Hit "Publish" on KDP.
- KDP says "your book will be live within 72 hours" — in practice for a previously-approved manuscript it's often 4-12 hours. Do not announce until the listing is actually live and the Buy button works.

### T+0 morning (launch day)
- 0700: Check the listing is live. Click the Buy button. If it says "currently unavailable," wait — do not announce.
- 0800: Send launch-day email (template C.2) to broad list.
- 0830: Post to Twitter/Mastodon/Discord/BGG/relevant forums. One post per platform, link prominent. Do not spam multi-post.
- 0900: Send personalized prelaunch follow-ups (template C.1) with the live link, to people who said they'd review.

### T+0 afternoon
- 1300: First sales check. Don't refresh KDP every 10 minutes — it's bad for your blood pressure and the dashboard is delayed by hours anyway.
- 1500: Check the listing page for: Buy button works, "Look Inside" loads (if enabled), price displays correctly, author name links to Author Central page.
- 1700: Reply to any congratulatory comments / replies on social. Don't reply to "I bought it!" with anything that pressures the reviewer. A simple "thank you" is correct.

### T+1 to T+3 (first 72 hours)
- Daily check: review count, sales rank in chosen BISAC categories, "Look Inside" working, no surprise refunds.
- Watch for the first review. Do not respond to it publicly even if it's wrong about something. Authors responding to reviews is a known reputation hit on Amazon.
- If sales rank is moving, leave the price alone. If it's flat after 72 hours, that's a separate decision (Section E).

### T+7 (one week)
- First royalty estimate visible in KDP dashboard (KDP reports with ~48h lag).
- Review the keyword + category fit. KDP allows changing keywords any time; categories are harder to change but possible via support.
- Schedule a `/schedule` agent for T+30 to do a 30-day post-launch report (sales, reviews, rank trajectory, refunds).

---

## Section E — When the launch is flat

If after 7-14 days there are <5 reviews and sales rank is in the millions, do not:
- Drop the price below the floor calculated in `royalty-analysis.md`. You can't recover from an anchored-low price without re-launching.
- Buy reviews / use review-swap services. Both are bannable.
- Run KDP ads before the listing has at least 5 organic reviews. Ads on a no-review listing convert badly and burn budget.

Do, in this order:
1. Audit the listing copy: is the hook clear in 2 seconds? Does the long description bury the lede?
2. Re-check the categories — are you in a category where the top-100 books look nothing like yours?
3. Reach out to 5-10 more specific people from the wargame design community who weren't on the prelaunch list.
4. Then, only then, consider a small ($5-10/day) KDP ad campaign on category targeting (not keyword targeting — keyword ads are for established titles).

---

## Section F — Reusing this checklist for future books

This file is intentionally generic where possible. For Ray's next KDP title:
- Replace the title/subtitle/audience rows in Section A.
- Re-do `kdp/listing-description.md`, `kdp/author-bio.md` (or trim to a one-line "also wrote X" addition), `kdp/keywords-and-categories.md`, `kdp/pricing-decision.md`. The voice and discovery work do not transfer.
- Keep Sections B (gate), C (templates — light edits per book), D (D-day sequence), and E (flat-launch playbook) as-is. They're book-agnostic.
- Update `royalty-analysis.md` for the new page count + chosen retail price.

The checklist itself should rarely change. If a launch surfaces something you wish you'd known, add it to the relevant section here so the next book benefits.
