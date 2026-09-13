# P12 — The Scaling Ladder

How to go from ₹200/day to ₹2,000/day **without destroying what works.**

---

## Gate: do not scale yet

Scaling multiplies whatever you have. If your unit economics are negative, scaling accelerates the loss.

**All four must be true:**

- [ ] **Ad set has exited the learning phase**, or you've deliberately accepted learning-limited and have 14 days of data
- [ ] **Cost per result ≤ your affordable CPA** (from [`../data/best-budget-recommender.md`](../data/best-budget-recommender.md))
- [ ] **You've closed actual customers**, not just collected leads
- [ ] **You can handle 2× the volume** — replies, calls, delivery, stock

> The fourth is the one people ignore. Doubling leads when you're already failing to reply within 5 minutes just doubles your waste. **Capacity is part of the campaign.**

If any box is unticked: fix that first. Scaling is not a fix for anything.

---

## The 20% / 4-day rule

**Raise the budget by no more than ~20%, then wait 4 days.**

Why: significant budget changes can reset the learning phase. A jump from ₹200 to ₹1,000 is a significant edit — Meta re-enters exploration, costs spike, and you conclude "scaling doesn't work" when what actually happened is you reset your own campaign.

```
Day 0    ₹200/day       ← proven baseline
Day 4    ₹240/day       (+20%)
Day 8    ₹290/day       (+20%)
Day 12   ₹350/day
Day 16   ₹420/day
Day 20   ₹500/day
Day 24   ₹600/day
Day 28   ₹720/day
```

₹200 → ₹720/day in four weeks, with the algorithm carried along instead of reset.

**At each step, check before the next raise:**
```
Cost per result vs previous step:   ______
Still ≤ affordable CPA?             yes / no
Frequency under 3?                  yes / no
```

**If cost per result rises materially, hold — don't raise again.** Wait 4 more days. If it doesn't recover, step back down one level.

### When you can move faster
If your ad set is well past learning with strong volume, some accounts tolerate 30–50% jumps. **Test that once**, observe, and go back to 20% if it destabilises. At low budget, 20% is the safe default.

---

## Vertical vs horizontal scaling

| | Vertical | Horizontal |
|---|---|---|
| What | More budget, same ad set | New audiences, placements, geographies, creatives |
| Risk | Frequency climbs, audience saturates | Splits budget, may re-enter learning |
| When | First choice, up to ~₹1,000/day | After vertical stalls |

**Scale vertically first.** It's simpler and keeps your learning intact. Go horizontal only when vertical stops working — usually signalled by **frequency above 3** and rising costs that budget increases don't fix.

### Horizontal moves, in order of safety

1. **New creative in the same ad set** — safest. Always do this first
2. **Widen the existing audience** — bigger radius, wider age. Still one ad set
3. **New geography** — a new city as a second ad set. Only above ~₹600/day total
4. **New audience type** — lookalikes, interest-based, as a second ad set
5. **New playbook** — add [P11](P11-catalog-retargeting.md) retargeting or [P07](P07-video-retarget-funnel-200.md) top-of-funnel

> ⚠️ **Don't add a second ad set below ~₹600/day total.** Two ad sets at ₹300 each learn worse than one at ₹600. The rule from [`README.md`](README.md) still applies: one ad set until the budget genuinely supports splitting.

---

## Recompute your floor as you scale

The learning-phase floor moves with your CPA, and your CPA usually **rises** as you scale — you're reaching less-ideal prospects.

```
At each step:
  Current cost per result:            ₹______
  Floor = 7.143 × that:               ₹______/day
  Current budget:                     ₹______/day
  Comfortably above floor?            yes / no
```

**Rising CPA while scaling is normal, not failure.** The question is whether it's still below your affordable CPA. Scaling until CPA equals affordable CPA is the correct stopping point — that's your maximum profitable spend.

```
Maximum profitable daily spend = the budget at which
                                cost per result = affordable CPA
```

Past that point you're buying unprofitable customers.

---

## Creative is the real scaling constraint

At ₹200/day, three creatives can last months. At ₹2,000/day, you burn through creative roughly 10× faster.

**Frequency is your early-warning system:**

| 7-day frequency | Meaning | Action |
|---|---|---|
| Under 1.5 | Plenty of room | Keep scaling |
| 1.5–2.5 | Healthy | Continue, prepare new creative |
| 2.5–3.5 | Saturating | Add creative now |
| Above 3.5 | Burning the audience | New creative + widen audience |

**Build a creative pipeline before you need it.** Aim to add one new creative per week once you're above ₹500/day. Rotate the weakest out, keep the winner. Never replace everything at once — you lose your baseline.

Angle library for rotation: [`P01` Variant D](P01-whatsapp-leads-200.md).

---

## Scaling by budget band

### ₹200 → ₹500/day
- Pure vertical, 20%/4 days
- Add a 4th creative
- Keep one ad set
- Expect CPA to stay roughly flat

### ₹500 → ₹1,000/day
- Continue vertical
- Widen location or age within the same ad set
- Add creative every 1–2 weeks
- Consider adding retargeting ([P11](P11-catalog-retargeting.md)) or top-of-funnel ([P07](P07-video-retarget-funnel-200.md))
- Expect CPA to rise slightly

### ₹1,000 → ₹2,000/day
- Now you can split: a second ad set for a new city or audience
- Consider **CBO / Advantage campaign budget ON** — with 3+ ad sets it genuinely helps
- Creative pipeline becomes mandatory
- Consider Advantage+ campaign types if applicable
- Expect CPA to rise; watch the affordable-CPA ceiling

### ₹2,000+/day
- Multiple campaigns by funnel stage
- Formal creative testing structure
- Weekly reporting cadence
- CAPI becomes genuinely important for measurement quality

---

## When to scale *down*

Reducing budget is a legitimate move, not an admission of failure.

| Signal | Action |
|---|---|
| CPA above affordable CPA for 7+ days | Cut back to the last profitable level |
| Frequency above 4 with no new creative ready | Reduce budget until creative is ready |
| Can't service the leads you have | Reduce until capacity catches up |
| Seasonal demand collapse | Reduce, wait, resume |
| Cash flow pressure | Reduce rather than pause — pausing loses learning |

**Reduce by 20–30%**, not to zero. A full pause loses accumulated learning; a reduction keeps the ad set alive.

---

## The scaling log

Keep this. It becomes the most useful document you own, and it's the benchmark file no published table can give you.

```
| Date | Budget/day | Cost per result | Frequency | Notes / change made |
|------|-----------|-----------------|-----------|---------------------|
|      |           |                 |           |                     |
```

After three months you'll know your own CPA curve — exactly where costs start rising and where your profitable ceiling sits. That knowledge is worth more than any benchmark article.

---

## Quick reference

```
GATE             exited learning + profitable + closed customers + capacity
RULE             +20% budget, wait 4 days, verify, repeat
ORDER            vertical first, horizontal only when frequency > 3
NO SPLITTING     until total budget ≥ ~₹600/day
RECOMPUTE        floor = 7.143 × current cost per result, at every step
STOP AT          cost per result = affordable CPA  (max profitable spend)
CREATIVE         +1 per week above ₹500/day; watch frequency
SCALE DOWN       by 20-30%, never pause to zero
```

---

**Related:** [`../data/best-budget-recommender.md`](../data/best-budget-recommender.md) · [`P01` Variant D](P01-whatsapp-leads-200.md) · [`../reference/troubleshooting.md`](../reference/troubleshooting.md)
