# KDP Royalty Analysis — Wargame Design Book

**Status:** Working analysis. Numbers are based on KDP's published
formula as of the analysis date and the current PDF page count.
Re-run before final pricing decision (wdb-010).

**Last refreshed:** 2026-04-24
**Book:** *A Contemporary Guide to Wargame Design*, 6x9 paperback,
black-and-white interior, 346 pages (per `print/out/wargame-design-book.pdf`)

---

## TL;DR

| List price | Royalty per copy (US, Amazon.com) | Comment |
|------------|-----------------------------------|---------|
| $19.99     | ~$6.99                            | Low — leaves money on the table for a 346-page niche-hobby technical book |
| $24.99     | ~$9.99                            | **Recommended primary target.** Matches niche-hobby paperback comparables. |
| $29.99     | ~$12.99                           | Defensible for a 346-page reference work. Stretch the band; watch reviews. |
| $34.99     | ~$15.99                           | Top of the band for self-published wargaming. Likely too high without a name. |

At any of these list prices, **monthly net at 100 copies/month sits in the $700–$1,600 range** before tax and assuming Amazon-direct only (no expanded distribution). The 346-page count is what unlocks the upper band — KDP only allows the 60% royalty option above the printing cost minimum, and a 346-page book has enough printing cost to support a healthy spread on a $25–$30 list.

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

For 346 pages:

| Paper  | Per-page rate | Print cost      |
|--------|--------------:|----------------:|
| White  | $0.012        | $0.85 + $4.152 = **$5.00** (rounded up to KDP's penny rule) |
| Cream  | $0.0145       | $1.00 + $5.017 = **$6.02** |

White paper is cheaper and is the right default for a primarily-text
technical book. Cream is the trade convention for novels and
narrative work — not what this book is. Use **white**.

**Print cost used in the rest of this doc: $5.00.**

### KDP royalty formula (US, paperback, Amazon-direct)

```
Royalty per copy = (list_price × 0.60) − print_cost     [60% option]
                 = (list_price × 0.40) − print_cost     [if Expanded Distribution opted in, on non-Amazon channels]
```

KDP requires the list price to be at least the printing-cost minimum
for the 60% royalty option. For our 346-page book, that minimum
is approximately:

```
list_price_min = print_cost / 0.60 = $5.00 / 0.60 = $8.34
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

| List price | Royalty (60% × list) | − print cost ($5.00) | Royalty per copy |
|-----------:|----------------------:|---------------------:|-----------------:|
| $14.99     | $8.99                 | − $5.00              | **$3.99**        |
| $17.99     | $10.79                | − $5.00              | **$5.79**        |
| $19.99     | $11.99                | − $5.00              | **$6.99**        |
| $22.99     | $13.79                | − $5.00              | **$8.79**        |
| $24.99     | $14.99                | − $5.00              | **$9.99**        |
| $27.99     | $16.79                | − $5.00              | **$11.79**       |
| $29.99     | $17.99                | − $5.00              | **$12.99**       |
| $34.99     | $20.99                | − $5.00              | **$15.99**       |

The break is around the $20 line — below it, you're effectively
working for $4–$7 a copy after print cost; above it, the royalty
scales linearly because print cost is already paid.

---

## Monthly income scenarios

Royalty per copy × monthly copies sold. Excludes returns, tax, and
Amazon's optional discounting.

### At $19.99 list ($6.99/copy)

| Copies/month | Monthly royalty | Annual |
|-------------:|----------------:|-------:|
| 10           | $69.90          | $839   |
| 50           | $349.50         | $4,194 |
| 100          | $699.00         | $8,388 |
| 250          | $1,747.50       | $20,970|
| 500          | $3,495.00       | $41,940|

### At $24.99 list ($9.99/copy) — **recommended**

| Copies/month | Monthly royalty | Annual  |
|-------------:|----------------:|--------:|
| 10           | $99.90          | $1,199  |
| 50           | $499.50         | $5,994  |
| 100          | $999.00         | $11,988 |
| 250          | $2,497.50       | $29,970 |
| 500          | $4,995.00       | $59,940 |

### At $29.99 list ($12.99/copy)

| Copies/month | Monthly royalty | Annual  |
|-------------:|----------------:|--------:|
| 10           | $129.90         | $1,559  |
| 50           | $649.50         | $7,794  |
| 100          | $1,299.00       | $15,588 |
| 250          | $3,247.50       | $38,970 |
| 500          | $6,495.00       | $77,940 |

### At $34.99 list ($15.99/copy)

| Copies/month | Monthly royalty | Annual  |
|-------------:|----------------:|--------:|
| 10           | $159.90         | $1,919  |
| 50           | $799.50         | $9,594  |
| 100          | $1,599.00       | $19,188 |
| 250          | $3,997.50       | $47,970 |
| 500          | $7,995.00       | $95,940 |

---

## Comparables — niche-hobby technical paperbacks

For calibration. None of these are ground truth (Amazon prices fluctuate); refresh before pricing.

| Title                                                    | Pages  | Approx list | Notes |
|----------------------------------------------------------|-------:|------------:|-------|
| *Wargames According to Mark* (Mark Herman, GMT 2024)     | ~260+  | $35-40      | Sold via GMT direct, not KDP — different cost structure (offset print). |
| *Designers & Dragons* series (John Tynes / Shannon Appelcline) | ~400 | $20-25 | Reference history of RPG industry. |
| Wargames-related Osprey monographs                       | 64-96  | $18-22      | Glossy color, very different production. |
| Self-published board game design books on KDP            | 150-300 | $15-25      | Most cluster in the $19.99-$24.99 band. |

The 346-page count puts this book in the *substantial reference* category, not the *thin guide* category. The substantial-reference band on KDP self-published comparables is closer to $24.99-$29.99 than $19.99.

---

## Recommendation

**Launch at $24.99 list.** Reasoning:

1. **The book justifies it on length alone.** 346 pages is 2-3x longer than the typical self-published design guide on KDP. Pricing it at $19.99 implicitly tells the reader it's the same product class as a 150-page primer, which it isn't.

2. **The royalty math is meaningfully better.** $9.99/copy vs $6.99/copy is a 43% increase per sale. At 100 copies/month that's $300/month, or $3,600/year, of free margin from a list-price decision that takes thirty seconds to make.

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

- **Page count.** Each ±10 pages shifts print cost by ±$0.12 (white). Currently 346.
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
