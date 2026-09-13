# India Cost Priors — and Why You Shouldn't Trust Them

## Read this first

**There is no reliable, published, per-vertical cost-per-lead dataset for Meta ads in India denominated in INR.**

I looked. What exists publicly is overwhelmingly US/global data in USD — "average CPL $28–42", "CPC $0.70", "CPM $11.62". Those are real numbers from real datasets, but they are **not Indian numbers**, and India is one of the cheapest Meta markets in the world. Global average CPM sits around $6.59 while the US is around $23.00 — India is materially below the global average.

This creates the trap that ruins most Indian ads guides:

> Someone takes a US benchmark table, runs a find-and-replace from `$` to `₹`, multiplies by 80-something, and publishes it as "Facebook Ads Cost in India".

The result is confidently wrong numbers. Sometimes it's visibly broken — real examples found on a live Indian ads site: `₹1,200-50/day`, `₹25,000-40,00020`, `₹80,000-2`, `₹18,000100-200`. Those are what happens when only the first number of a range gets converted. But the invisible failures are worse: a clean-looking table that's off by 10×, which you then use to plan a budget.

**This file therefore contains no per-vertical CPL table.** Anyone who gives you one for India is guessing. Here's what to use instead.

---

## What you get instead: order-of-magnitude priors

These are **wide bands for choosing a strategy**, not predictions of your cost. Their only job is to help you pick a rung on the optimization ladder in [`budget-engine.md`](budget-engine.md).

| Optimization event | Order of magnitude in India | Confidence |
|---|---|---|
| Impression (CPM) | Tens of ₹ per 1,000 | Moderate — India is a low-CPM market |
| ThruPlay / video view | Single-digit ₹ or less | Moderate |
| Link click (CPC) | Single to low-double-digit ₹ | Moderate |
| Landing page view | Low-double-digit ₹ | Low |
| WhatsApp conversation started | Tens of ₹ | Low |
| Instant Form lead | Tens of ₹ | Low |
| Website lead (Pixel/CAPI) | Low hundreds of ₹ | Low |
| Purchase | Hundreds to low thousands of ₹ | Very low — depends entirely on price point |

**How to use this table:** to answer "is a WhatsApp conversation closer to ₹5 or ₹500?" — it's tens of rupees, so at ₹200/day you'll be learning-limited, so use P00's mitigations or move to P07. That's a strategy decision, and the table is precise enough for it.

**How not to use it:** "conversations cost ₹45 so I'll get 7 per day." You don't know that. Nobody does until you run it.

### What genuinely moves your cost

Ordered roughly by impact:

1. **Creative quality and hook** — the biggest lever by far. A good hook can halve CPM
2. **Offer strength** — a compelling offer beats every targeting trick
3. **Vertical competitiveness** — insurance/real-estate/education bid far above local services
4. **City tier** — Tier-1 metros (Mumbai, Delhi NCR, Bengaluru) cost significantly more than Tier-2/3
5. **Optimization event choice** — the rung you pick
6. **Audience breadth** — narrow audiences pay a premium
7. **Season** — festive periods (Diwali, wedding season) and election periods push CPMs up
8. **Placement mix** — Reels/Audience Network cheaper than Feed
9. **Account history** — established accounts with conversion history deliver cheaper
10. **Language** — regional-language creative often cheaper per result, less competition

Note that **the top two are things you control** and neither appears in any benchmark table. This is the real argument against benchmark-chasing: the dominant variables are your creative and your offer.

---

## The calibration procedure (this replaces benchmarks)

### Step 1 — Record your assumption, on the record

```
Date: __________
Event I'm optimizing for: __________________
My assumed cost per event: ₹ ______
Source of that assumption: ☐ my past campaigns  ☐ priors above  ☐ pure guess
Budget I set (7.143 × assumption): ₹ ______ /day
```

Writing the guess down is the point. It makes Day 7 a measurement rather than a vibe.

### Step 2 — Run 7 days untouched

No edits. Significant edits reset the ~50-event learning clock and you lose the week.

### Step 3 — Measure

From Ads Manager, for the ad set:

```
Amount spent                    ₹ ______
Impressions                       ______
Link clicks                       ______
Your optimization events          ______

CPM               = spend ÷ impressions × 1000   = ₹ ______
CTR (link)        = link clicks ÷ impressions     = ______%
Cost per event    = spend ÷ events                = ₹ ______   ← the number that matters
```

### Step 4 — Recompute your budget

```
True recommended daily budget = 7.143 × (measured cost per event) = ₹ ______
```

Compare to what you set. The difference between your Day-0 guess and this number is exactly how wrong the priors were for *your* business — which is why the system is built to measure rather than to look up.

### Step 5 — Build your own benchmark file

Keep a running record. After three campaigns you'll have something no published table can give you: **your** costs, in **your** vertical, in **your** city, with **your** creative.

```
| Date | Campaign | Event | Spend | Events | Cost/event | Notes |
|------|----------|-------|-------|--------|-----------|-------|
|      |          |       |       |        |           |       |
```

This becomes the most valuable file you own. It's the only benchmark that's actually about you.

---

## Diagnostic ratios (these travel better than absolute costs)

Absolute ₹ costs vary wildly. **Ratios** are much more stable and more diagnostic:

| Ratio | Rough healthy zone | What it tells you |
|---|---|---|
| CTR (link) | ≥ ~0.8%; under ~0.5% is a problem | Creative and hook quality |
| Frequency (7-day) | Under ~2.0 | Above ~3 and you're burning the same people — refresh creative or widen |
| Landing page view ÷ link clicks | ≥ ~70% | Below that, your page is slow or mismatched. Big issue on Indian mobile data |
| Cost per event, week 2 vs week 1 | Should fall | If it rises, you're fatiguing or stuck in learning |
| WhatsApp reply rate | The higher the better | Low = wrong audience or a mismatched pre-filled message |

Use these to decide **what to fix**. Use your own measured costs to decide **what to spend**.

---

## Honest summary

- No trustworthy INR per-vertical CPL table exists publicly. This file will not invent one
- Priors here are order-of-magnitude only, for choosing a rung
- Your Day-7 measured cost is worth more than every published benchmark combined
- The two biggest cost drivers — creative and offer — appear in no table anywhere
- Global/US figures are real but do not transfer: India is a low-CPM market

---

**Next:** [`budget-engine.md`](budget-engine.md) · [`best-budget-recommender.md`](best-budget-recommender.md) · [`verticals-india.md`](verticals-india.md)
