# The Budget Engine

**This is the core of the system.** Everything else is execution detail. Read this and you'll understand why almost all "low budget Facebook ads" advice for India is arithmetically impossible.

There are no invented benchmarks in this file. Every number is either a formula you can verify, or a number *you* supply about your own business.

---

## Part 1 — The learning phase is a budget constraint, not a phase

When you create or significantly edit an ad set, Meta enters a **learning phase**: it explores placements, audiences and times to find who converts. It needs roughly **50 optimization events per ad set per 7 days** to gather enough signal. Below that, the ad set is flagged **Learning Limited** — delivery stays volatile and your cost per result stays inflated.

Most people treat this as a delivery footnote. It isn't. It's a hard floor on your budget.

### The formula

```
50 events ÷ 7 days = 7.14 events needed per day

daily budget = events per day × cost per event

  ⇒  daily budget ≥ (50 × CPA) ÷ 7
  ⇒  daily budget ≥ 7.143 × CPA
```

That's it. That's the whole thing. Two useful directions:

**Direction A — I know my budget. What CPA must I hit?**
```
max viable CPA = daily budget ÷ 7.143
```

**Direction B — I know my CPA. What budget do I need?**
```
required daily budget = 7.143 × CPA
```

### Direction A, computed

| Your daily budget | Max CPA that can still exit learning | Monthly (30d) |
|---|---|---|
| ₹100/day | ₹14 | ₹3,000 |
| **₹200/day** | **₹28** | **₹6,000** |
| ₹300/day | ₹42 | ₹9,000 |
| ₹500/day | ₹70 | ₹15,000 |
| ₹750/day | ₹105 | ₹22,500 |
| ₹1,000/day | ₹140 | ₹30,000 |
| ₹2,000/day | ₹280 | ₹60,000 |
| ₹5,000/day | ₹700 | ₹1,50,000 |

### The ₹200/day verdict

**At ₹200/day your optimization event must cost ₹28 or less to exit the learning phase.**

A lead does not cost ₹28. Not a form lead, not a WhatsApp enquiry, not a website lead, and certainly not a purchase. So:

> **"₹200/day optimized for Leads" cannot exit the learning phase. Ever.**
> Not because you're doing it wrong — because 200 ÷ 7.143 = 28, and leads cost more than ₹28.

This single sentence invalidates most low-budget ad advice written for Indian audiences. Anyone recommending ₹200/day with conversion optimization either hasn't done the division or is hoping you won't.

---

## Part 2 — The optimization event ladder

The way out is to understand that **you choose what Meta optimizes for**, and the cheaper the event, the easier it is to hit 50/week.

Events from cheapest to most valuable:

| Rung | Optimization event | Rough cost band | Budget floor to exit learning | Viable at ₹200/day? |
|---|---|---|---|---|
| 1 | Impressions / Reach | pennies | ~₹20/day | ✅ Easily |
| 2 | ThruPlay / 2-sec video view | very low | ~₹20–40/day | ✅ Easily |
| 3 | Link click / Landing page view | low | ~₹40–100/day | ✅ Yes |
| 4 | Messaging conversation started (WhatsApp) | moderate | ~₹200–500/day | ⚠️ Borderline |
| 5 | Instant Form lead | moderate–high | ~₹300–700/day | ❌ No |
| 6 | Website lead (Pixel/CAPI) | high | ~₹1,000–2,500/day | ❌ No |
| 7 | Purchase | highest | ~₹3,000–8,000/day | ❌ No |

> ⚠️ **The cost bands above are wide deliberately.** They are order-of-magnitude priors to help you *choose a rung*, not predictions of your cost. Your actual cost depends on your vertical, city tier, creative and offer, and can sit outside these bands. Replace them with your own measured numbers after 3–7 days — see Part 5. Do not quote these bands to anyone as "Indian benchmarks".

### The rule this gives you

> **Optimize for the highest rung you can afford to hit 50× per week. Not the rung you most want.**

Wanting purchases doesn't let you optimize for purchases. At ₹200/day you optimize at rung 2 or 3 and let the higher-value actions happen as a downstream consequence.

This is the core strategy of [`P07 — Video → Retargeting Funnel`](../playbooks/P07-video-retarget-funnel-200.md), the flagship ₹200/day playbook.

---

## Part 3 — What your target cost *should* be (from your economics, not a table)

The budget engine tells you what's *mechanically possible*. Your unit economics tell you what's *worth paying*. You need both.

Fill in your own numbers:

```
V  = revenue from one closed customer            ₹ ______
M  = gross margin %                              ______%
C  = lead → customer conversion rate %           ______%
A  = share of margin you'll spend to acquire     ______%   (start at 30%)
```

Then:

```
Gross profit per customer      GP   = V × M
Max cost per acquisition       CAC  = GP × A
Max cost per lead              CPL  = CAC × C
Budget floor for that CPL           = 7.143 × CPL
```

### Worked example (illustration only — substitute your own figures)

A business where one closed customer brings ₹20,000 revenue at 40% margin, closing 1 in 5 leads, willing to spend 30% of gross profit to acquire:

```
GP   = 20,000 × 0.40          = ₹8,000
CAC  = 8,000 × 0.30           = ₹2,400
CPL  = 2,400 × 0.20           = ₹480      ← can pay up to ₹480 per lead
floor= 7.143 × 480            = ₹3,429/day  ← to exit learning on that lead event
```

Read that last line carefully. This business *can afford* ₹480 leads — that's genuinely profitable. But to get Meta's algorithm to optimize for those leads reliably, it needs ₹3,429/day.

**That gap is the real story of low-budget advertising.** Affordability and learnability are two different constraints, and the binding one is usually learnability.

### What to do when the two conflict

If your affordable CPL is high but your budget is low, you have four honest options:

1. **Optimize lower on the ladder** (rung 2–3) and accept leads as a by-product. → P07
2. **Run learning-limited on purpose**, with the ad set built to survive it (broad targeting, one ad set, no edits). Works, but expect volatile daily costs. → P01, P02
3. **Concentrate the budget in time** rather than lowering it: run ₹200/day × 30 days as ₹1,400/day for 4–5 days instead. Same money, but the ad set can actually learn. Genuinely underused.
4. **Raise the budget** to the computed floor, now that you know the number rather than guessing.

Option 3 deserves emphasis: **₹6,000 spent as ₹1,400/day for 4 days will usually outperform ₹200/day for 30 days**, because one exits the learning phase and the other never does.

---

## Part 4 — Two more real budget constraints

### The Cost-Per-Result bid rule

If you use the **Cost per result goal** bid strategy, Meta requires your **daily budget to be at least 5× your target cost per result**.

```
daily budget ≥ 5 × target cost per result
   ⇒ at ₹200/day, target cost per result ≤ ₹40
```

At ₹200/day you cannot set a cost goal above ₹40. If you need a higher cost goal, use **Highest volume** bidding instead (the default) — which is the right choice at low budgets anyway.

### Platform minimums

Meta enforces minimum daily budgets that scale with how infrequent your optimization event is — roughly **$1/day equivalent for impression-based** objectives and **$5/day equivalent for click/conversion** optimization. Meta sets these per currency, so your INR minimums are set in your own account, not by converting dollars.

**Do not trust any article for your exact minimum, including this one.** Ads Manager will refuse the budget and show you the real figure. That figure is authoritative; go with what your screen says.

---

## Part 5 — Calibration: replacing priors with truth

This is the step that separates this system from every benchmark table you'll find online.

### Day 0
Record your assumption. "I'm assuming a WhatsApp conversation costs about ₹X." Write it down so you can be wrong on the record.

### Day 3 — sanity check only
Look at **CPM**, **CTR (link)** and **cost per your optimization event**.

Do not judge cost per result yet — you're inside the learning phase and it's meaningless. You're only checking for something *broken*:

| Symptom | Likely cause | Action |
|---|---|---|
| Ad not delivering at all | In review, or budget below account minimum | Check Delivery column; wait 24h |
| CTR under ~0.5% | Creative or offer isn't landing | Change the creative, not the targeting |
| CPM wildly high | Audience too narrow, or a Special Ad Category restriction | Broaden; check category |
| Spending but zero events | Wrong event configured, or tracking broken | Verify Pixel/form/WhatsApp wiring |

**Do not touch budget or targeting on Day 3 unless something is broken.** A significant edit resets the 50-event clock and you start over.

### Day 7 — the real calibration
Now compute from your own data:

```
Your actual CPA = total spend ÷ events delivered

Your true budget floor = 7.143 × your actual CPA
```

Then compare against your affordable CPL from Part 3:

| Situation | What it means | Action |
|---|---|---|
| Actual CPA ≤ affordable CPL, and budget ≥ floor | Working and stable | Scale — see P12 |
| Actual CPA ≤ affordable CPL, but budget < floor | Profitable but learning-limited | Raise to floor, or concentrate budget (Part 3, option 3) |
| Actual CPA > affordable CPL | Not economic yet | Fix creative/offer first. More budget won't fix a bad offer |
| Too few events to judge | Below statistical usefulness | Drop to a cheaper rung and retest |

### Day 14+
Recalculate. Your CPA moves with season, competition and creative fatigue. The formula never changes; your inputs do. **Recalculate monthly**, and after every creative refresh.

---

## Part 6 — Quick reference

```
LEARNING FLOOR       daily budget ≥ 7.143 × CPA
MAX VIABLE CPA       CPA ≤ daily budget ÷ 7.143
COST-GOAL RULE       daily budget ≥ 5 × target cost per result
EVENTS NEEDED        7.14 per day  (50 per 7 days)

AFFORDABLE CPL       (revenue × margin × acquisition share) × close rate
DECISION             optimize for the highest rung you can hit 50×/week
₹200/DAY VERDICT     max CPA ₹28 → rung 2–3 only → leads as by-product
```

### The four sentences that matter

1. At ₹200/day, your optimization event must cost under ₹28 to exit learning.
2. Leads cost more than ₹28, so at ₹200/day optimize for views or landing page views instead.
3. Affordability and learnability are different constraints — check both.
4. Concentrating a small monthly budget into fewer, higher-spend days usually beats spreading it thin.

---

**Next:** [`benchmarks-india.md`](benchmarks-india.md) for calibration priors and their limits · [`../playbooks/README.md`](../playbooks/README.md) to choose your campaign
