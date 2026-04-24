# KDP Royalty Analysis — Wargame Design Book

**Status:** Working analysis. Numbers are based on KDP's published
formula as of the analysis date and the current PDF page count.
Re-run before final pricing decision (wdb-010).

**Last refreshed:** 2026-04-24 (post-wdb-011 font polish)
**Book:** *A Contemporary Guide to Wargame Design*, 6x9 paperback,
black-and-white interior, **360 pages** (per `print/out/wargame-design-book.pdf`).

> **Note:** the page count grew from 346 → 360 when wdb-011 swapped
> the body font from Georgia to Lora. Lora is slightly wider per
> em-width. The math below uses the post-swap 360-page figure.
> Difference vs. the pre-swap analysis: print cost +$0.17/copy
> (~$0.17 less royalty per copy). Recommendation unchanged
> ($24.99 launch).

---

## TL;DR

| List price | Royalty per copy (US, Amazon.com) | Comment |
|------------|-----------------------------------|---------|
| $19.99     | ~$6.67                            | Low — leaves money on the table for a 360-page niche-hobby technical book |
| $24.99     | ~$9.67                            | **Recommended primary target.** Matches niche-hobby paperback comparables. |
| $29.99     | ~$12.67                           | Defensible for a 360-page reference work. Stretch the band; watch reviews. |
| $34.99     | ~$15.67                           | Top of the band for self-published wargaming. Likely too high without a name. |

At any of these list prices, **monthly net at 100 copies/month sits in the $660–$1,560 range** before tax and assuming Amazon-direct only (no expanded distribution). The 360-page count is what unlocks the upper band — KDP only allows the 60% royalty option above the printing cost minimum, and a 360-page book has enough printing cost to support a healthy spread on a $25–$30 list.

---

## Inputs

### KDP printing cost formula (US, 6x9 B&W paperback)

KDP charges a fixed cost plus a per-page cost. The formula has been
updated periodically — **verify against
[kdp.amazon.com/help/topic/A1HZJSDOSEDUHB](https://kdp.amazon.com/help/topic/A1HZJSDOSEDUHB)
before final pricing.** Numbers below use the formula KDP has published
as of analysis date; bump the inputs in the per-page-rate table below
if KDP has updated rates since.

```
Black ink, 6x9 trim, 110+ pages, US (Amazon.com):

  Print cost = $1.00 fixed + $0.012 × page_count   (white paper)
  Print cost = $1.00 fixed + $0.0145 × page_count  (cream paper)
```

For 360 pages:

| Paper  | Per-page rate | Print cost      |
|--------|--------------:|----------------:|
| White  | $0.012        | $1.00 + $4.32 = **$5.32** (rounded up to KDP's penny rule) |
| Cream  | $0.0145       | $1.00 + $5.22 = **$6.22** |

White paper is cheaper and is the right default for a primarily-text
technical book. Cream is the trade convention for novels and
narrative work — not what this book is. Use **white**.

**Print cost used in the rest of this doc: $5.32.**

### KDP royalty formula (US, paperback, Amazon-direct)

```
Royalty per copy = (list_price × 0.60) − print_cost     [60% option]
                 = (list_price × 0.40) − print_cost     [if Expanded Distribution opted in, on non-Amazon channels]
```

KDP requires the list price to be at least the printing-cost minimum
for the 60% royalty option. For our 360-page book, that minimum
is approximately:

```
list_price_min = print_cost / 0.60 = $5.32 / 0.60 = $8.87
```

So any reasonable hobby/specialty list price ($15+) is well above the
minimum and qualifies for the 60% royalty.

**Recommendation: 60% royalty, Amazon-direct only.** Expanded
Distribution drops the royalty to 40% on those channels — for a
niche-hobby technical book, the marginal sales through B&N and
ingram-distributed indie shops aren't likely to make up for the
royalty hit. Ray can flip ED on later if a niche bookstore
specifically asks for it.

---

## Per-copy royalty table

White paper, 60% royalty, US, Amazon.com only:

| List price | Royalty (60% × list) | − print cost ($5.32) | Royalty per copy |
|-----------:|----------------------:|---------------------:|-----------------:|
| $14.99     | $8.99                 | − $5.32              | **$3.67**        |
| $17.99     | $10.79                | − $5.32              | **$5.47**        |
| $19.99     | $11.99                | − $5.32              | **$6.67**        |
| $22.99     | $13.79                | − $5.32              | **$8.47**        |
| $24.99     | $14.99                | − $5.32              | **$9.67**        |
| $27.99     | $16.79                | − $5.32              | **$11.47**       |
| $29.99     | $17.99                | − $5.32              | **$12.67**       |
| $34.99     | $20.99                | − $5.32              | **$15.67**       |

The break is around the $20 line — below it, you're effectively
working for $4–$7 a copy after print cost; above it, the royalty
scales linearly because print cost is already paid.

---

## Monthly income scenarios

Royalty per copy × monthly copies sold. Excludes returns, tax, and
Amazon's optional discounting.

### At $19.99 list ($6.67/copy)

| Copies/month | Monthly royalty | Annual |
|-------------:|----------------:|-------:|
| 10           | $66.70          | $800   |
| 50           | $333.50         | $4,002 |
| 100          | $667.00         | $8,004 |
| 250          | $1,667.50       | $20,010|
| 500          | $3,335.00       | $40,020|

### At $24.99 list ($9.67/copy) — **recommended**

| Copies/month | Monthly royalty | Annual  |
|-------------:|----------------:|--------:|
| 10           | $96.70          | $1,160  |
| 50           | $483.50         | $5,802  |
| 100          | $967.00         | $11,604 |
| 250          | $2,417.50       | $29,010 |
| 500          | $4,835.00       | $58,020 |

### At $29.99 list ($12.67/copy)

| Copies/month | Monthly royalty | Annual  |
|-------------:|----------------:|--------:|
| 10           | $126.70         | $1,520  |
| 50           | $633.50         | $7,602  |
| 100          | $1,267.00       | $15,204 |
| 250          | $3,167.50       | $38,010 |
| 500          | $6,335.00       | $76,020 |

### At $34.99 list ($15.67/copy)

| Copies/month | Monthly royalty | Annual  |
|-------------:|----------------:|--------:|
| 10           | $156.70         | $1,880  |
| 50           | $783.50         | $9,402  |
| 100          | $1,567.00       | $18,804 |
| 250          | $3,917.50       | $47,010 |
| 500          | $7,835.00       | $94,020 |

---

## Comparables — niche-hobby technical paperbacks

For calibration. None of these are ground truth (Amazon prices fluctuate); refresh before pricing.

| Title                                                    | Pages  | Approx list | Notes |
|----------------------------------------------------------|-------:|------------:|-------|
| *Wargames According to Mark* (Mark Herman, GMT 2024)     | ~260+  | $35-40      | Sold via GMT direct, not KDP — different cost structure (offset print). |
| *Designers & Dragons* series (John Tynes / Shannon Appelcline) | ~400 | $20-25 | Reference history of RPG industry. |
| Wargames-related Osprey monographs                       | 64-96  | $18-22      | Glossy color, very different production. |
| Self-published board game design books on KDP            | 150-300 | $15-25      | Most cluster in the $19.99-$24.99 band. |

The 360-page count puts this book in the *substantial reference* category, not the *thin guide* category. The substantial-reference band on KDP self-published comparables is closer to $24.99-$29.99 than $19.99.

---

## Recommendation

**Launch at $24.99 list.** Reasoning:

1. **The book justifies it on length alone.** 360 pages is 2-3x longer than the typical self-published design guide on KDP. Pricing it at $19.99 implicitly tells the reader it's the same product class as a 150-page primer, which it isn't.

2. **The royalty math is meaningfully better.** $9.67/copy vs $6.67/copy is a 45% increase per sale. At 100 copies/month that's $300/month, or $3,600/year, of free margin from a list-price decision that takes thirty seconds to make.

3. **Buyers in this niche aren't price-sensitive at this band.** Wargame designers and serious hobbyists routinely buy $40+ rulebooks and $80+ games. A $24.99 reference book is well below the noise floor for the audience.

4. **Headroom for promotion.** A $24.99 list lets Amazon discount to $19.99-$22.99 during promo periods without going below the print-cost floor. A $19.99 list has no discount headroom — a sale would push the royalty toward $4-$5/copy.

**Don't go higher than $29.99 at launch.** The wargame design audience is small enough that review volume matters; a $34.99 list invites comparison shopping that hurts conversion. Once the book has 50+ reviews and an established BGG presence, a price bump to $29.99 is defensible. The launch list should sit one band below the eventual ceiling.

**What this analysis is NOT:**

- Not a replacement for checking KDP's current published printing-cost rates. Verify before final pricing.
- Not a sales projection. The "100 copies/month" line is a benchmark, not a forecast — wargame design is a small market and 100/month is an above-average outcome that requires sustained marketing, not a default.
- Not factoring tax. US self-employment tax + state income tax is roughly 20-30% of net royalty depending on Ray's bracket; the gross numbers above are pre-tax.
- Not factoring returns. KDP paperback returns are uncommon (~1-3%) but exist.

---

## Inputs that change this analysis

If any of these change, re-run before pricing:

- **Page count.** Each ±10 pages shifts print cost by ±$0.12 (white). Currently 360.
- **KDP per-page rate.** Currently $0.012 (white) for B&W 6x9 in the US. KDP has bumped this 2-3 times since 2018; verify before launch.
- **Paper choice.** Cream costs ~$1/copy more than white. Default white for this book.
- **Royalty option.** 60% Amazon-only is the recommended path. Flipping on Expanded Distribution drops to 40% on non-Amazon channels.
- **Launch market.** Numbers above are US Amazon.com only. UK/EU/JP have separate cost structures (different per-page rates, different exchange rates) — handled by KDP automatically once published, but each market has its own breakeven.

---

## Next decisions (downstream of this doc)

- **wdb-010** — final retail price decision. This doc supports $24.99 launch.
- **wdb-007** — Amazon listing description, voice-calibrated.
- **wdb-008** — author bio + back-cover hook.
- **wdb-009** — keywords + BISAC categories.
- **wdb-002** — finalize cover (front + spine + back). Spine width depends on final page count via the formula in `print/cover/spine-width.py`.
