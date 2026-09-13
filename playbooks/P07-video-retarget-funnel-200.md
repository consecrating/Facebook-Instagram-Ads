# P07 — Video → Retargeting Funnel (₹200/day) ⭐

**The only structure in this repo that genuinely exits the learning phase at ₹200/day.**

If ₹200/day is a hard ceiling — not a starting point you'll raise — this is the correct playbook. It's also the right first campaign for anyone with no audience, no social proof and no past ad data.

---

## The logic

At ₹200/day your optimization event must cost **≤ ₹28** to hit ~50 events per 7 days and exit learning.

A lead costs far more than ₹28. A **video view costs far less.**

So instead of asking Meta to find buyers directly (which it can't learn to do on ₹200/day), you:

1. **Phase 1** — pay for cheap video views. Optimize for ThruPlay. Exits learning easily, because views cost a few rupees
2. Meta learns who watches your content — a real, owned audience asset
3. **Phase 2** — retarget only the people who watched 50%+ with your actual offer

Phase 2 audiences are warm, so they convert at a far higher rate than cold traffic. You get leads without ever having asked Meta to optimize for an event you couldn't afford.

**What you're really buying with Phase 1 is an audience, not views.** The views are the receipt.

---

## Budget split

| Phase | Daily budget | Optimization event | Exits learning? |
|---|---|---|---|
| Phase 1 — Video views | **₹120/day** | ThruPlay | ✅ Yes, easily |
| Phase 2 — Retarget offer | **₹80/day** | WhatsApp / Instant Form | Learning-limited, but the audience is warm |
| **Total** | **₹200/day** | | |

> Run **Phase 1 alone for the first 7–10 days.** Phase 2 has nobody to retarget until Phase 1 has built an audience. Starting both together wastes Phase 2's budget entirely.

Check the maths yourself: at ₹120/day, a ThruPlay costing ₹3 gives 40 views/day = 280/week — comfortably past 50. That ad set will exit learning. This is the whole trick.

---

## Prerequisites

- [ ] Facebook Page + Instagram, both complete
- [ ] Payment method proven → [`../setup/02-payments-india-gst.md`](../setup/02-payments-india-gst.md)
- [ ] **One video, 30–60 seconds** (see below — this is the only real work)
- [ ] For Phase 2: WhatsApp Business connected → [`../setup/04-whatsapp-business.md`](../setup/04-whatsapp-business.md)

### The video — don't overthink it

Shot on a phone is fine and often outperforms polished production, which can read as an ad and get skipped.

**Structure that works:**

```
0–3s    HOOK. A problem your customer recognises instantly.
        "AC not cooling even after service?"
3–15s   The problem, specifically. Show it. Make them nod.
15–40s  What you do about it. Show real work, real results.
40–55s  Who you are, where you serve, price range.
55–60s  Soft CTA: "WhatsApp us for a free quote."
```

**Rules:**
- **First 3 seconds decide everything.** Most people leave there
- **Add captions.** A large share of feed viewing is muted
- Vertical **9:16** or square **1:1**. Never landscape
- Speak the language your customers speak — Hindi/Tamil/Telugu/Marathi creative typically faces less competition than English
- Genuine and specific beats generic and slick

---

# PHASE 1 — Build the audience

## Step 1 — Campaign

**Ads Manager → + Create**

1. **Objective:** **Engagement**
2. **Campaign name:** `VIDEO | Audience Build | Sep26`
3. **Special Ad Category:** blank unless required → [`../reference/policy-and-special-categories.md`](../reference/policy-and-special-categories.md)
4. **Advantage campaign budget (CBO):** **OFF**
5. **Next**

## Step 2 — Ad set

1. **Ad set name:** `Broad | Video Views | Cold`
2. **Conversion location / Engagement type:** **Video views**
3. **Performance goal:** **Maximise ThruPlay views**
   > ThruPlay = watched to completion (or 15s+). It's the cheapest meaningful event available, and cheap is the entire point of Phase 1.
4. **Budget:** Daily, **₹120**
5. **Bid strategy:** **Highest volume**
6. **Location:** your service area (city + 10–25 km radius, or the states you serve)
7. **Age:** wide — e.g. `25–55`
8. **Gender:** All
9. **Advantage+ Audience:** **ON**, suggestion fields **empty**
10. **Placements:** **Advantage+ (automatic)** ON
11. **Next**

## Step 3 — Ads

Create **2 ads** (Phase 1 needs less testing than a lead campaign):

- **Ad 1:** your video, 9:16, captions on
- **Ad 2:** the same video cut to ~15s, or a different hook in the first 3 seconds

Settings for each:
- **Identity:** Page + Instagram
- **Primary text:** short. Nobody reads copy on a video ad — the video *is* the copy
- **CTA:** **Learn more** (or **Send Message** — a few will convert here for free)

**Publish.** Then leave it alone for 7 days.

---

## Step 4 — Create the retargeting audience (Day 1, do it now)

Do this immediately so it starts filling. It takes 24–48 hours to begin populating.

**Ads Manager → Audiences → Create audience → Custom audience → Video**

1. **Engagement:** *People who watched at least 50% of your video*
   > Why 50% and not 3 seconds: a 3-second view is often an accidental scroll-stop. Someone who watched half your video has genuinely chosen to. Smaller audience, dramatically better quality.
2. **Select videos:** both your Phase 1 videos
3. **Retention:** **365 days** (maximum — you want the biggest possible pool at this budget)
4. **Name:** `Video 50% - 365d`
5. **Create**

Also create, while you're here:
- `Page + IG engagers - 365d` (Custom audience → Facebook Page / Instagram account)

---

# PHASE 2 — Convert the warm audience

**Only start this once `Video 50% - 365d` has roughly 1,000+ people.** Check under Audiences → Size. Below that there isn't enough to deliver against, and you'll just waste the ₹80.

At ₹120/day you'll typically reach that in 7–14 days. Be patient — this is the phase people skip, and skipping it is why they conclude the funnel doesn't work.

## Step 5 — Phase 2 campaign

1. **Objective:** **Engagement**
2. **Campaign name:** `CTWA | Retarget Warm | Sep26`
3. **CBO:** OFF

## Step 6 — Phase 2 ad set

1. **Ad set name:** `Retarget | Video 50% | WhatsApp`
2. **Conversion location:** **WhatsApp** (or Instant Form if you prefer → [`../setup/05-instant-forms.md`](../setup/05-instant-forms.md))
3. **Performance goal:** **Maximise number of conversations**
4. **Budget:** Daily, **₹80**
5. **Audience → Custom audiences:** select **`Video 50% - 365d`** and **`Page + IG engagers - 365d`**
6. **Advantage+ Audience:** **OFF** for this ad set
   > This is the one place in the entire repo where you deliberately narrow. The whole point is to reach *only* the people who already watched. Letting Advantage+ expand beyond them defeats the design.
7. **Location:** same as Phase 1 (a safety net)
8. **Age / Gender:** as wide as Phase 1
9. **Placements:** Advantage+ ON

## Step 7 — Phase 2 ads

**2 ads**, and this time lead with the offer — they already know who you are:

- **Ad 1:** static image, offer + price, strong CTA
- **Ad 2:** short video testimonial or a specific result

**Copy angle that works here:** acknowledge the prior contact.

```
Still thinking about [SERVICE]?

We're [BUSINESS] in [CITY]. [KEY BENEFIT].
[SERVICE] starting ₹[PRICE].

WhatsApp us — we'll reply in 5 minutes.
```

**Pre-filled message:**
```
Hi! I saw your video about [SERVICE]. Please share details and pricing.
```

---

## Measurement contract

### Phase 1, Day 3

| Check | Healthy | If not |
|---|---|---|
| ThruPlays accumulating | Yes | Check delivery/payment |
| Cost per ThruPlay | Single-digit ₹ | Hook is weak — recut the first 3s |
| 50% video-view audience growing | Yes | Video is too long, or hook is failing |

**Don't touch the ad set.** Only swap creative if cost per ThruPlay is clearly bad.

### Phase 1, Day 7

```
Audience size of Video 50% - 365d:  ______
Cost per ThruPlay:                 ₹ ______
```

- **1,000+ people** → launch Phase 2
- **Under 1,000** → run Phase 1 alone another week. Consider shifting the full ₹200 into Phase 1 to build faster

### Phase 2, Day 7

```
Cost per conversation (warm) = spend ÷ conversations = ₹ ______
```

Compare this to what a cold WhatsApp campaign costs you (from P00, if you've run it). The warm number should be **materially lower** — that difference is the entire return on Phase 1.

### Day 30 — the strategic decision

```
Blended cost per lead = (Phase1 spend + Phase2 spend) ÷ total leads
```

| Result | Action |
|---|---|
| Blended CPL below your affordable CPL | Working. Shift budget toward Phase 2, or scale both → [P12](P12-scaling-ladder.md) |
| Phase 2 cheap but starved of audience | Move budget to Phase 1; grow the pool |
| Both expensive | The **offer** is the problem, not the structure |

---

## Why this beats "just run lead ads at ₹200/day"

| | Lead ads at ₹200/day | This funnel |
|---|---|---|
| Exits learning phase | ❌ Never (needs CPA ≤ ₹28) | ✅ Phase 1 does |
| Cost stability | Volatile indefinitely | Stabilises in ~7 days |
| Builds an asset | No | ✅ A growing warm audience |
| Month 2 costs | Same or worse | **Lower** — the audience compounds |
| Social proof | None | Video accumulates views/comments |

The compounding is the real argument. A lead campaign at ₹200/day costs the same in month six as in month one. This funnel gets cheaper, because Phase 2 retargets an audience that keeps growing.

---

## Quick reference

```
PHASE 1  Engagement → Video views → Maximise ThruPlay
         ₹120/day · broad · Advantage+ ON · 2 ads · 9:16 + captions
         → creates "Video 50% - 365d" audience (365-day retention)

PHASE 2  Engagement → WhatsApp → Maximise conversations
         ₹80/day · Custom audience ONLY · Advantage+ OFF · 2 ads
         → start only when audience ≥ ~1,000

TIMING   Phase 1 alone for 7-14 days, then add Phase 2
EDITS    None for 7 days
```

---

**Related:** [`P00`](P00-BEST-low-budget-campaign.md) if you can reach ~₹325/day · [`P08`](P08-engagement-social-proof.md) to add credibility · [`P12`](P12-scaling-ladder.md) to scale · [`../data/budget-engine.md`](../data/budget-engine.md) for the maths
