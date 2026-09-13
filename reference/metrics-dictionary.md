# Metrics — What to Watch and What to Ignore

Ads Manager shows hundreds of columns. At low budget, about eight matter.

---

## The only metrics that matter at ₹200–500/day

| Metric | What it tells you | Rough healthy zone |
|---|---|---|
| **Amount spent** | Reality check against your plan | = your budget |
| **Cost per result** | ⭐ The number. Cost per your optimization event | ≤ your affordable CPA |
| **Results** | Volume of your actual goal event | ≥ 50/week to exit learning |
| **CTR (link)** | Creative and hook quality | ≥ ~0.8%; under 0.5% = problem |
| **CPM** | Audience competitiveness | Compare to your own history only |
| **Frequency** | How often the same person sees it | Under 2.0 good; over 3.0 = refresh |
| **Delivery status** | Is it even running | Active, not Learning Limited |
| **Landing page views ÷ link clicks** | Page speed and relevance | ≥ ~70% |

**Set up a custom column preset with exactly these** and stop looking at the rest. More columns at low budget produce more noise, not more insight.

---

## Cost per result — the one to build decisions on

This is cost per **your chosen optimization event**, not a generic CPA.

```
Cost per result = amount spent ÷ results
```

Then always:
```
Budget floor = 7.143 × cost per result
```

Compare against your affordable CPA from [`../data/best-budget-recommender.md`](../data/best-budget-recommender.md). Those two comparisons drive every decision in this system.

---

## Metrics that mislead at low budget

| Metric | Why to ignore it |
|---|---|
| **Reach / Impressions** | Vanity unless awareness is genuinely your goal |
| **Post engagement** | Likes don't pay. Only matters in [P08](../playbooks/P08-engagement-social-proof.md) |
| **CTR (all)** | Includes clicks on your Page name, reactions, "…more". **Use CTR (link)** |
| **Relevance/quality rankings** | Only populate at volume; noisy at ₹200/day |
| **ROAS on day 1–3** | Meaningless during the learning phase |
| **Cost per 1,000 people reached** | Rarely actionable |
| **Video plays (3-sec)** | Often accidental scroll-stops. **Use ThruPlay** |
| **Daily fluctuation of anything** | At ₹200/day, one day is noise. Use 7-day totals |

**The biggest low-budget mistake is reacting to daily numbers.** At ₹200/day a single day might contain 2 results. Two results is not data.

---

## Learning phase indicators

Check the **Delivery** column:

| Status | Meaning | Action |
|---|---|---|
| **Learning** | Gathering data, under 50 events | Wait. Do not edit |
| **Active** | Exited learning | Now you can judge performance |
| **Learning Limited** | Unlikely to reach ~50 events/week | Raise budget to `7.143 × CPA`, or drop to a cheaper event, or accept volatility |
| **Not delivering** | Something's wrong | Check payment, review status, schedule |

**Learning Limited is not a bug** — at ₹200/day for a lead event it's the mathematically expected state. See [`../data/budget-engine.md`](../data/budget-engine.md).

---

## Attribution — read this before trusting any number

**Default attribution is typically 7-day click, 1-day view.** Meaning: a conversion is credited to Meta if the person clicked within 7 days, or merely *saw* the ad within 1 day.

Implications:

1. **View-through credit can overstate Meta's contribution** — someone who saw your ad and would have bought anyway gets attributed
2. **Long consideration cycles get understated** — a property enquiry today that closes in 8 weeks may not be credited at all
3. **Meta's numbers won't match Google Analytics.** Different models, different windows. Neither is lying
4. **Your inbox and your bank account are the ground truth**

**The practical answer for Indian small businesses:** ask customers how they found you, and use offer codes in ads. Low-tech manual attribution beats platform attribution for a single-location or single-channel business.

Set the comparison window: **Columns → Customise columns → Comparing windows** to see click-only vs view-through side by side. If most of your "conversions" are view-through, be sceptical.

---

## The one report worth building

**Columns → Customise columns → save as a preset.** Include:

```
Amount spent · Results · Cost per result · CTR (link) · CPM ·
Frequency · Delivery status · Landing page views (if website)
```

Then **breakdowns** worth checking occasionally (Breakdown → By delivery):

| Breakdown | Look for |
|---|---|
| **Placement** | Which placement is cheapest. Don't act below ₹500/day — you'll starve the rest |
| **Age / Gender** | Genuine skews. Only act on strong, sustained differences |
| **Region** | Which cities perform. Useful before splitting geographically |
| **Time of day** | Only useful if considering dayparting |

**Warning:** breakdowns fragment small data into meaningless slices. At ₹200/day, a placement breakdown might show 3 conversions across 6 placements. Don't optimize on that.

---

## The weekly review — 10 minutes

Once a week, not daily:

```
Week ending: ______

Spend                        ₹______
Results                       ______
Cost per result              ₹______
vs last week                  ______%
CTR (link)                    ______%
Frequency                     ______
Delivery status               ______

Floor = 7.143 × cost/result  ₹______/day
Current budget               ₹______/day
Above floor?                  yes / no

Affordable CPA               ₹______
Profitable?                   yes / no

Customers actually closed     ______
Real cost per customer       ₹______

ACTION: ______________________
```

**"Customers actually closed" is the line that matters most and the one people skip.** Leads are an intermediate metric. Closed customers pay for the ads.

---

## Quick reference

```
WATCH            cost per result · results · CTR(link) · frequency · delivery
IGNORE           reach · CTR(all) · engagement · daily fluctuation · rankings
ALWAYS COMPUTE   floor = 7.143 × cost per result
JUDGE ON         7-day totals, never single days
LEARNING         "Learning Limited" at ₹200/day for leads is EXPECTED
ATTRIBUTION      7-day click / 1-day view by default. Your inbox is truth
REVIEW           weekly, 10 minutes, ending in one ACTION
```

---

**Related:** [`../data/budget-engine.md`](../data/budget-engine.md) · [`troubleshooting.md`](troubleshooting.md) · [`../data/benchmarks-india.md`](../data/benchmarks-india.md)
