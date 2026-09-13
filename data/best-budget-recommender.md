# The Best-Budget Recommender

[`budget-engine.md`](budget-engine.md) tells you what's *possible* at a given budget. This file answers the question you actually care about:

> **"Forget the minimum — what budget should I actually spend?"**

It produces **one number**, derived from your business. Not a range, not "it depends", not ₹500 because ₹500 sounds reasonable.

---

## The five budget tiers

Every advertiser sits in one of five tiers. They are defined by arithmetic, not by opinion.

| Tier | Name | Definition | What you get |
|---|---|---|---|
| **T0** | Below viable | < platform minimum | Ad won't deliver, or delivers so thinly it's noise |
| **T1** | Survival | ₹200/day-ish, event on rung 2–3 | Exits learning on a cheap event. Leads as by-product. Real, but slow |
| **T2** | **Recommended** | `7.143 × target CPA` | Exits learning **on your actual goal event**. Stable, predictable cost |
| **T3** | Optimal | `2 × T2` | Exits learning fast + affords creative testing in parallel |
| **T4** | Scale | T3 and rising, +20%/4 days | Growth mode. Only enter after T2/T3 proved profitable |

**T2 is the answer to "what should I spend".** T3 is the answer to "what if I want this to work faster".

---

## Compute your recommendation in 5 steps

### Step 1 — Your affordable cost per lead

```
V = revenue from one closed customer       ₹ ______
M = gross margin %                           ______%
C = lead → customer close rate %             ______%
A = % of gross profit you'll spend to win it  ______%   (30% is a sane start)

Affordable CPL = V × M × A × C
```

### Step 2 — Your goal event, and its rung

Pick the event that *is* your business outcome:

| Your outcome | Optimization event | Rung |
|---|---|---|
| WhatsApp enquiries | Messaging conversations started | 4 |
| Form leads, no website | Instant Form lead | 5 |
| Website enquiries | Website lead (Pixel/CAPI) | 6 |
| Online sales | Purchase | 7 |
| Footfall | Landing page view / Messaging | 3–4 |
| Followers | Profile visits / Engagement | 2–3 |

### Step 3 — Estimate that event's cost

Use your own data if you have any — even one week of past campaigns beats any published table.

If you have none, use the **wide priors** in [`benchmarks-india.md`](benchmarks-india.md), and treat the output as provisional until Day 7. Being explicitly uncertain is fine. Being confidently wrong is not.

### Step 4 — Compute the tiers

```
T2  Recommended = 7.143 × (cost of your goal event)
T3  Optimal     = 2 × T2
T1  Survival    = your real budget, with the event dropped to rung 2–3
```

### Step 5 — Reality check against affordability

```
If  T2 ≤ (Affordable CPL × 7.143)   → T2 is genuinely affordable. Spend it.
If  T2 >  your maximum monthly budget ÷ 30   → you're in T1. Use P00 or P07.
```

---

## Worked example — substitute your own numbers

A service business: ₹20,000 revenue per customer, 40% margin, closes 1 in 5 leads, will spend 30% of gross profit to acquire. Wants WhatsApp enquiries, and assumes ~₹45 per conversation.

```
Affordable CPL = 20,000 × 0.40 × 0.30 × 0.20   = ₹480 per lead   ← comfortably profitable

T2 Recommended = 7.143 × 45                    = ₹322/day  (≈ ₹9,650/month)
T3 Optimal     = 2 × 322                       = ₹644/day  (≈ ₹19,300/month)
T1 Survival    = ₹200/day, optimizing for landing page views instead
```

**The recommendation: ₹322/day — round to ₹325.**

Note what just happened. The advice wasn't "₹500/day" or "start small and scale". It was ₹322, because 7.143 × 45 = 322. If their conversation cost turns out to be ₹60 on Day 7, the recommendation moves to ₹429. The formula is fixed; the input is measured.

And note the gap: they can *afford* ₹480/lead but only need ₹322/day. They're not budget-constrained at all — they're constrained by not knowing the number. That's the common case.

---

## The ₹200/day question, answered directly

**Is ₹200/day worth it?** Yes — but only in a specific configuration, and you should know what you're trading away.

| | ₹200/day (T1) | ₹325/day (T2) |
|---|---|---|
| Exits learning phase | Only on rung 2–3 events | Yes, on your actual goal event |
| Cost per result | Volatile, inflated | Stabilises after ~7 days |
| Optimizes for | Views / landing page views | WhatsApp conversations |
| Leads arrive | As a by-product | As the target |
| Time to signal | 3–4 weeks | 7–10 days |
| Monthly | ₹6,000 | ₹9,750 |

**The gap is ₹3,750/month.** That's the honest price of moving from "ads that technically run" to "ads the algorithm can actually optimize". Whether that's worth it is your call — but now it's a decision, not an accident.

### If ₹200/day is genuinely your ceiling

Use the concentration trick instead of spreading thin:

```
Spreading:      ₹200/day × 30 days   = ₹6,000   → never exits learning
Concentrating:  ₹1,400/day × 4 days  = ₹5,600   → exits learning in one burst
```

Same money. One of them teaches Meta's algorithm who your buyer is; the other never accumulates enough signal. Run 4–5 day bursts, learn, pause, reload. This is the single most underused low-budget tactic in India.

---

## The recommendation script (for the AI assistant)

When a user asks "what budget should I use", do this — in this order:

1. Ask for `V`, `M`, `C` (revenue, margin, close rate). If they don't know `C`, use 20% and **label it as an assumption**.
2. Compute Affordable CPL.
3. Ask their goal event → get its rung.
4. Get a cost estimate for that event — their own data first, priors only as fallback.
5. Compute **T2 = 7.143 × event cost**. Present it as *the* recommendation, and show the multiplication.
6. Present T1 and T3 as the two alternatives, with the trade-off table.
7. State the Day 7 recalculation explicitly: *"On Day 7, replace my estimate with your real CPA and recompute — your recommendation will move."*

**Never** skip to a round number. **Never** say "start with ₹500/day and see". If you don't have their inputs, ask for them.

---

## Tier summary

```
T0  Below viable   — won't deliver
T1  Survival       — ₹200/day, rung 2–3, leads as by-product        → P00, P07
T2  RECOMMENDED    — 7.143 × goal-event cost                        → P01, P02
T3  Optimal        — 2 × T2, adds creative testing headroom         → P01 + P08
T4  Scale          — +20% every 4 days once profitable              → P12
```

---

**Next:** [`../playbooks/P00-BEST-low-budget-campaign.md`](../playbooks/P00-BEST-low-budget-campaign.md) — the best campaign to run at T1/T2 · [`benchmarks-india.md`](benchmarks-india.md) — priors and their limits
