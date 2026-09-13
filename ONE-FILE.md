# Facebook + Instagram Ads — India (INR) — Complete System, Single File

**Use this file when the AI assistant can't browse links.** Copy the whole thing and paste it into the chat. It contains everything essential from the repository.

---

## PART 0 — INSTRUCTIONS FOR THE AI ASSISTANT

You are an experienced Indian performance marketer helping a business owner with a small budget. Follow these rules.

**Rule 0 — Never invent a benchmark.** There is no reliable published per-vertical cost-per-lead data for India in INR. Derive budgets from arithmetic and from the user's own unit economics. Label every estimate as an estimate. Replace estimates with the user's real measured data by Day 7.

**Rule 1 — Interview before advising.** Ask the intake questions (Part 5) in batches of 3–4. Wait for answers. Do not produce a plan first.

**Rule 2 — Compute the budget, never guess it.** Use Part 1. Show the arithmetic.

**Rule 3 — Everything in ₹.** Never convert a US figure and present it as an Indian benchmark. Indian CPMs are far below US.

**Rule 4 — Give exact clicks, not concepts.** "Click + Create → Engagement → set Conversion location = WhatsApp", not "set up a lead campaign".

**Rule 5 — End with a measurement contract.** Day 3 checks, Day 7 recalculation, and "do not edit during learning".

---

## PART 1 — THE BUDGET ENGINE (the core)

Meta needs roughly **50 optimization events per ad set per 7 days** to exit the learning phase. Below that, the ad set is *Learning Limited* — delivery stays volatile and expensive.

```
50 ÷ 7 = 7.14 events per day needed

LEARNING FLOOR:   daily budget ≥ 7.143 × cost per event
MAX VIABLE CPA:   CPA ≤ daily budget ÷ 7.143
```

| Daily budget | Max CPA that can still exit learning |
|---|---|
| ₹100 | ₹14 |
| **₹200** | **₹28** |
| ₹300 | ₹42 |
| ₹500 | ₹70 |
| ₹1,000 | ₹140 |
| ₹2,000 | ₹280 |

### The ₹200/day verdict

**At ₹200/day your optimization event must cost ≤ ₹28 to exit learning.** A lead never costs ₹28. Therefore **"₹200/day optimized for Leads" cannot exit the learning phase.** Say this plainly to the user — most low-budget advice ignores it.

### The optimization-event ladder

| Rung | Event | Order of magnitude (India) | Viable at ₹200/day? |
|---|---|---|---|
| 1 | Impressions/Reach | pennies | ✅ |
| 2 | ThruPlay / video view | single-digit ₹ | ✅ |
| 3 | Link click / landing page view | low-double-digit ₹ | ✅ |
| 4 | WhatsApp conversation | tens of ₹ | ⚠️ borderline |
| 5 | Instant Form lead | tens of ₹ | ❌ |
| 6 | Website lead (Pixel/CAPI) | low hundreds ₹ | ❌ |
| 7 | Purchase | hundreds–thousands ₹ | ❌ |

> These bands are deliberately wide order-of-magnitude priors for **choosing a rung** — not predictions. Do not quote them as Indian benchmarks.

**Rule: optimize for the highest rung you can hit 50× per week — not the rung you most want.**

### Other real constraints

- **Cost-per-result bid strategy** requires daily budget ≥ **5 × target cost per result**. At ₹200/day your cost goal can't exceed ₹40. Use **Highest volume** instead.
- **Platform minimums** exist (roughly $1/day-equivalent for impressions, $5/day-equivalent for conversions). Meta sets these per currency — **trust the figure Ads Manager shows you**, not any article.

---

## PART 2 — THE BEST-BUDGET RECOMMENDER

### Affordable cost per lead, from their economics

```
V = revenue per closed customer      ₹____
M = gross margin %                    ____%
C = lead → customer close rate %      ____%
A = % of gross profit to spend acquiring (start 30%)

Affordable CPL = V × M × A × C
```

### The five tiers

| Tier | Definition | Meaning |
|---|---|---|
| T0 | below platform minimum | won't deliver |
| T1 Survival | ~₹200/day, event on rung 2–3 | works, leads as by-product |
| **T2 RECOMMENDED** | **7.143 × goal-event cost** | **exits learning on the real goal** |
| T3 Optimal | 2 × T2 | faster learning + creative testing |
| T4 Scale | +20% every 4 days | growth, only after profitable |

**T2 is the answer to "what should I spend".**

### Worked example (substitute their numbers)

₹20,000 revenue/customer, 40% margin, closes 1 in 5, wants WhatsApp enquiries assumed ~₹45:

```
Affordable CPL = 20,000 × 0.40 × 0.30 × 0.20 = ₹480 per lead
T2 Recommended = 7.143 × 45                  = ₹322/day → round ₹325
T3 Optimal     = 2 × 322                     = ₹644/day
T1 Survival    = ₹200/day, optimizing for landing page views instead
```

**Recommendation: ₹325/day.** Note they can *afford* ₹480/lead — they were never budget-constrained, only uninformed.

### When budget can't reach the floor — four honest options

1. **Drop a rung** — optimize for views/landing page views; leads become a by-product
2. **Accept learning-limited**, built to survive it (one ad set, broad, no edits)
3. **Concentrate the budget** — `₹1,400/day × 4 days` beats `₹200/day × 30 days` on the same ₹5,600, because one exits learning and the other never does. **Most underused low-budget tactic in India**
4. **Raise to the computed floor**, now that it's a number rather than a guess

---

## PART 3 — THE BEST LOW-BUDGET CAMPAIGN: Click-to-WhatsApp

Best default for most Indian businesses. No website, no Pixel, no landing page. Reported **30–50% lower CPL** than standard lead-gen.

**Prerequisite that isn't optional:** someone must reply within **5 minutes** during business hours. Indian buyers contact 3–4 businesses at once. If nobody answers, 100% of the spend is wasted.

### Build

```
Campaign
  Objective:              Engagement        (NOT "Leads" — WhatsApp lives here)
  Name:                   CTWA | WhatsApp | Sep26
  Special Ad Category:    blank unless credit/employment/housing/political
  Advantage campaign budget (CBO):  OFF

Ad set
  Conversion location:    WhatsApp  (select your connected number)
  Performance goal:       Maximise number of conversations
  Budget:                 Daily = 7.143 × cost per conversation (₹325 typical)
  Bid strategy:           Highest volume  (NO cost cap)
  Location:               your service area — local: city + 10-25 km radius
                          use "People living in or recently in this location"
  Age:                    widest plausible, e.g. 25-55
  Gender:                 All
  Advantage+ Audience:    ON, suggestion fields EMPTY
  Languages:              blank (let creative self-select)
  Placements:             Advantage+ (automatic) ON

Ads — EXACTLY THREE in the one ad set
  Ad 1: static image + offer
  Ad 2: video 15-30s (usually cheapest CPM; phone-shot is fine)
  Ad 3: carousel or a second static angle
  Media:  4:5 (1080×1350) feed + 9:16 (1080×1920) reels/stories
  CTA:    Send WhatsApp Message
  Pre-filled message:
          "Hi! I'm interested in [SERVICE]. Please share details and pricing."
```

### At ₹200/day — six mitigations (all of them)

1. **One ad set only.** Splitting is the most expensive low-budget mistake
2. **Broad targeting, no interest layers**
3. **Exactly 3 ads**
4. **Advantage+ placements ON**
5. **No edits for 7 days** — a significant edit resets the 50-event clock
6. **Judge on 7-day totals**, never single days

### India copy rules

- **Put the price in the ad.** Filters out tyre-kickers; builds trust
- Name the **locality**, not just the city, and use a **landmark**
- One clear action
- No fake urgency — reads as a scam
- No before/after imagery in health/fitness/beauty

---

## PART 4 — THE ₹200/DAY FUNNEL THAT ACTUALLY EXITS LEARNING

Use when ₹200/day is a hard ceiling, or the user is brand new with no audience.

**Logic:** a lead costs more than ₹28, but a **video view costs a few rupees**. So buy cheap views, build an audience, then retarget it.

```
PHASE 1 — ₹120/day  (run ALONE for the first 7-14 days)
  Objective:        Engagement → Video views
  Performance goal: Maximise ThruPlay views
  Broad, Advantage+ ON, Advantage+ placements ON
  2 ads, video 30-60s, 9:16, CAPTIONS ON

  → Day 1, immediately create audience:
    Audiences → Custom audience → Video
    "People who watched at least 50% of your video"
    Retention: 365 days.  Name: Video 50% - 365d
    (50% not 3-sec — a 3-sec view is an accidental scroll-stop)

PHASE 2 — ₹80/day  (start only when audience ≥ ~1,000 people)
  Objective:        Engagement → WhatsApp
  Performance goal: Maximise conversations
  Audience:         Custom audiences ONLY (Video 50% + Page/IG engagers)
  Advantage+ Audience: OFF  ← the one place you deliberately narrow
  2 ads, offer-led (they already know you)
```

**Check the maths:** ₹120/day at ~₹3 per ThruPlay = ~40 views/day = 280/week. Comfortably past 50. **That ad set exits learning.** That's the whole trick.

**Why it beats lead ads at ₹200/day:** it exits learning, it stabilises, and it **compounds** — the warm audience grows, so month 2 is cheaper. A lead campaign at ₹200/day costs the same in month six as in month one.

### Video structure

```
0-3s    HOOK — a problem they recognise instantly (decides everything)
3-15s   The problem, specifically. Show it.
15-40s  What you do about it. Real work, real results.
40-55s  Who you are, where, price range.
55-60s  Soft CTA.
```

---

## PART 5 — INTAKE QUESTIONS (ask in batches of 3–4)

**Block A — What you sell**
1. What does your business do, in one line?
2. What do you want to advertise right now?
3. Which city/area? How far will a customer travel?
4. Which language do your customers speak?

**Block B — Numbers (unlocks the budget maths)** ⭐
5. Revenue from one closed customer? ₹____
6. Gross margin? ____%
7. Out of 10 enquiries, how many buy? ____
8. Real daily budget? ₹____
9. Is that a hard ceiling?

**Block C — The action**
10. What should someone DO after seeing the ad? (WhatsApp / form / website / buy / visit / book / follow)
11. How do you get customers now?
12. **Can you reply within 5 minutes during business hours? Who?**

**Block D — Assets**
13. Which exist: Page · Instagram · Website · WhatsApp Business · Pixel · Business Manager · INR ad account · working payment method
14. Run Meta ads before? What happened?

**Block E — Risk**
15. Do you advertise **credit / loans / insurance / jobs / property / political**? → ⚠️ **Special Ad Category**: must declare, targeting gets restricted, costs rise
16. Seasonal? Peak when?
17. Do you have a GSTIN?

**Block F — Creative**
18. Can you shoot a 30–60s phone video? (unlocks Part 4)
19. Real photos? Testimonials?
20. Willing to put your price in the ad?

**If they can't answer 5–7:** use placeholders, **say out loud they're assumptions**, and mark the recommendation provisional.

---

## PART 6 — PLAYBOOK SELECTOR

| They want | Objective + conversion location | Works at ₹200/day? |
|---|---|---|
| WhatsApp enquiries | Engagement → WhatsApp | Yes, learning-limited |
| Form leads, no website | Leads → Instant forms | Yes, learning-limited |
| Website enquiries | Leads → Website (Pixel) | ❌ ~₹1,800/day |
| Instagram followers | Engagement → IG profile visits, **Instagram-only placements** | Yes |
| Online sales | Sales → Website, Purchase | ❌ ~₹3,000+/day |
| Shop footfall | Engagement → WhatsApp, tight 5 km radius | Yes |
| Nothing yet / no audience | **Part 4 funnel** | ✅ exits learning |
| Credibility first | Engagement → On your post, ₹100-200/day, 2-4 weeks | Yes |
| Appointments | Engagement → WhatsApp, **sell the free appointment** | Yes |
| Cart recovery | Sales + Catalog ON, cart abandoners 7-14d, Advantage+ OFF | Partly |

---

## PART 7 — SETUP ESSENTIALS (India)

**Ad account:** currency **INR**, timezone **Asia/Kolkata**. ⚠️ **Both permanent — cannot be changed.** Verify before creating.

**Payments:** card / UPI / net banking / prepaid top-up. **Prepaid is safer at low budget** (hard stop at zero). Indian recurring-card mandate rules cause auto-debit failures — keep a backup method. **Prove the method with a real ₹100/day test before launching.**

**GST:** digital advertising in India attracts GST, commonly **18%**, generally **on top of** ad spend.
```
₹6,000 ad spend + ₹1,080 GST = ₹7,080 actual outflow
```
Budget for the total. With a **GSTIN** added to the ad account, the GST is generally available as **input tax credit** — confirm with your CA. Verify the current rate; rules change.

**WhatsApp:** use the free **WhatsApp Business app** on a separate business number. Set greeting + away messages, quick replies, labels. Connect to the Page (Page Settings → WhatsApp → OTP). **Verify the number appears in Ads Manager's WhatsApp dropdown before building.** The free reply window is **24 hours** — qualify and quote inside it.

**Instant Forms:** need a **privacy policy URL** (mandatory). Choose **Higher intent** at low budget. 3–4 fields, **phone before email** in India. One multiple-choice qualifier (budget or timeline). **Test lead delivery with a real submission** — leads nobody sees are pure waste.

**Pixel:** not needed for WhatsApp or Instant Forms. Install it anyway to build audiences, but don't optimize for website conversions until budget supports it. If using both Pixel and CAPI, **match `event_id`** or purchases double-count and you'll scale a loser.

---

## PART 8 — MEASUREMENT CONTRACT

**Day 1–2:** don't touch anything. "In review" and erratic delivery are normal.

**Day 3 — breakage check only:**

| Check | Healthy | If not |
|---|---|---|
| Delivering | Active | Billing, then Account Quality |
| CTR (link) | ≥ ~0.8% | **Creative problem** — swap weakest ad only |
| Events arriving | Some | Verify WhatsApp number / form / pixel |
| Leads reaching you | Yes | Fix delivery immediately |

**Do not change budget or targeting on Day 3 unless delivery is broken.** Editing resets the 50-event clock.

**Day 7 — the real read:**
```
Actual CPA        = spend ÷ events          = ₹____
True budget floor = 7.143 × actual CPA      = ₹____/day
Effective CPL     = spend ÷ leads REACHED   = ₹____   ← the honest number
```

| Result | Action |
|---|---|
| CPA ≤ affordable CPL, budget ≥ floor | Working → scale +20% every 4 days |
| Profitable but below floor | Raise to floor, or concentrate into fewer days |
| CPA far above affordable CPL | **Offer problem.** More budget won't fix it |
| Contact rate under 50% | Follow-up problem, not an ads problem |

**Day 14+:** recompute. Refresh creative when frequency > 3.

### Scaling
**+20% budget, wait 4 days, verify, repeat.** Big jumps are significant edits and reset learning. Scale vertically (more budget, same ad set) before horizontally. **Don't add a second ad set below ~₹600/day total.** Stop when cost per result reaches your affordable CPA — that's your maximum profitable spend.

---

## PART 9 — WATCH / IGNORE

**Watch:** cost per result · results · CTR (link) · frequency · delivery status · landing-page-views ÷ link-clicks

**Ignore at low budget:** reach · impressions · CTR (all) · post engagement · quality rankings · **daily fluctuation of anything**

**Learning phase statuses:** *Learning* (wait) · *Active* (now judge) · *Learning Limited* (raise to floor, drop a rung, or accept volatility) · *Not delivering* (payment/policy/schedule)

**Attribution:** default 7-day click / 1-day view. Meta won't match Google Analytics. **Your inbox and bank account are ground truth.** For local businesses, use an offer code in the ad and ask "how did you hear about us" — beats platform attribution.

---

## PART 10 — POLICY (protect the account)

**Special Ad Categories** — Credit · Employment · Housing · Social/Political. Must declare. Declaring **removes most targeting** (age locked 18-65+, gender All, detailed targeting gone, radius restricted, lookalikes limited) and **raises costs**. Not declaring when required risks **permanent account loss**.

**Health / fitness / beauty** — no before/after imagery, no guaranteed outcomes, never imply you know a personal attribute of the viewer. **Advertise the consultation, not the outcome.** This is both compliant and higher-converting.

**Landing pages must comply too**, and must match the ad's promise.

**If rejected:** read the named policy → fix the real issue → create a **new** ad (don't resubmit the same one repeatedly) → appeal via Account Quality if wrong. Automated rejections are often overturned. **Never attempt evasion** — treated far more seriously than the original violation.

**Protect the asset:** 2FA on all admins, a second admin, never buy/rent ad accounts, never share logins.

---

## PART 11 — THE TEN RULES

1. One campaign → one ad set → three ads. Never split under ₹1,000/day
2. Advantage+ Audience ON, suggestion fields empty
3. Advantage+ placements ON (except Instagram-follower campaigns)
4. Highest volume bidding. No cost caps at low budget
5. CBO OFF with a single ad set
6. **No edits for 7 days** — edits reset the learning clock
7. Judge on 7-day totals, never single days
8. **Creative beats targeting.** Fix creative and offer before audience
9. **Compute the budget: `7.143 × event cost`.** Never guess
10. **Reply within 5 minutes.** Beats every setting in Ads Manager

---

## PART 12 — THE FOUR SENTENCES THAT MATTER

1. At ₹200/day, your optimization event must cost under ₹28 to exit the learning phase.
2. Leads cost more than ₹28 — so at ₹200/day, optimize for video views or landing page views and let leads arrive as a by-product.
3. Affordability and learnability are different constraints; check both.
4. Concentrating a small monthly budget into fewer, higher-spend days usually beats spreading it thin.

---

*Full repository, with 13 detailed playbooks and step-by-step setup guides:*
**https://github.com/consecrating/Facebook-Instagram-Ads**
