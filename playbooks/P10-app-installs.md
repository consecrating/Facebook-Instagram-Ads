# P10 — App Installs

## ⚠️ Budget warning

App install campaigns are among the most budget-hungry on Meta. Beyond the install itself, you usually need to optimize for a **post-install event** (registration, first purchase) for the campaign to be worth anything — and those events are expensive.

```
Install at ₹40        →  floor ₹286/day       (installs alone)
Registration at ₹150  →  floor ₹1,071/day
First purchase ₹600   →  floor ₹4,286/day
```

**Optimizing for installs alone is usually a mistake.** You'll get cheap installs from people who never open the app again. Install count is the most misleading metric in mobile marketing.

**If your budget is under ~₹1,000/day and you have no SDK set up, this playbook is not where you should start.** Consider [P07](P07-video-retarget-funnel-200.md) to build an audience first, or [P00](P00-BEST-low-budget-campaign.md) if your app solves a problem people would enquire about.

---

## Hard prerequisites

- [ ] App live on **Google Play** and/or **App Store**
- [ ] **App registered in Meta**: Business settings → Apps, or developers.facebook.com
- [ ] **SDK or MMP integrated** — Meta SDK, or an MMP like AppsFlyer/Adjust/Branch
- [ ] **App events defined and verified** — `CompleteRegistration`, `Purchase`, etc.
- [ ] **iOS: SKAdNetwork / Advanced App Campaigns configured** if you target iOS
- [ ] Store listing optimised — screenshots, description, ratings

> Without SDK/MMP integration you are flying blind: you'll see installs but nothing about whether they're worth anything. **Do not run this campaign until events are verified.**

In India, Android dominates. **Start Android-only** — cheaper installs, simpler measurement, no ATT complexity.

---

## Step 1 — Campaign

1. **Objective:** **App promotion**
2. **Name:** `APP | Installs | Android | Sep26`
3. **Campaign type:**
   - **Manual app ads** — you control targeting and creative
   - **Advantage+ app campaigns (AAC)** — automated, needs more budget and event volume
   → At low budget, choose **Manual**
4. **Advantage campaign budget:** OFF
5. **Next**

## Step 2 — Ad set

1. **Name:** `Android | Install | India`
2. **App:** select your app + store
3. **Performance goal:**
   | Goal | Use when |
   |---|---|
   | **App installs** | Starting out, no event data yet |
   | **App events** | You have SDK events and budget ≥ ~₹1,000/day — **preferred** |
   | Value | Mature, revenue-tracking apps |
4. **Budget:** Daily, ≥ `7.143 × your target event cost`
5. **Bid:** Highest volume
6. **Location:** India, or specific states
7. **Age / Gender:** wide
8. **Advantage+ Audience:** ON, fields empty
9. **Placements:** Advantage+ ON
   > Audience Network often delivers very cheap installs — but frequently low-quality ones. Watch post-install retention before celebrating
10. **Device targeting** (Ad set → Devices):
    - **Android only** to start
    - Consider **minimum OS version** if your app requires it — installs on unsupported devices are pure waste
    - Consider excluding very low-end devices if your app is heavy
11. **Next**

## Step 3 — Ads

App ads live or die on creative. **Three ads:**

- **Ad 1 — App preview video, 15–30s.** Show the actual screens and the core action. Usually the top performer
- **Ad 2 — Carousel of screenshots** with benefit captions
- **Ad 3 — Static with the single strongest benefit**

**CTA:** **Install now**, **Download**, **Use app**, **Play game**

**Copy frame:**
```
[THE ONE PROBLEM THE APP SOLVES]

[APP NAME] — [core benefit in 5 words]
✓ [Feature → benefit]
✓ [Feature → benefit]
✓ Free to download

[Social proof: "10,000+ downloads" / "4.5★"]
```

**Creative rules:**
- Show the **app interface**. People want to see what they're installing
- **First 3 seconds** must show the core value
- Captions on — muted viewing is the norm
- 9:16 vertical for Reels/Stories, which usually carry the cheapest app inventory
- Don't over-design. Real screen recordings often beat animated promos

---

## Measurement contract

Ads Manager alone is not enough here. You need the SDK/MMP view.

### Day 3
- Installs registering in Ads Manager **and** in your SDK/MMP?
- Do the two roughly agree? Large gaps mean attribution problems
- CTR ≥ ~0.8%?
- Store listing converting — clicks vs installs?

### Day 7
```
Spend:                          ₹______
Installs:                        ______
Cost per install (CPI):         ₹______
Registrations:                   ______
Cost per registration:          ₹______
Day-1 retention:                 ______%
Day-7 retention:                 ______%
Cost per RETAINED user:         ₹______   ← the number that matters
```

| Result | Action |
|---|---|
| Cheap installs, poor D1 retention | Wrong audience or misleading creative. Switch to app-event optimization |
| Good retention, high CPI | Working — scale carefully via [P12](P12-scaling-ladder.md) |
| Installs in Ads Manager but not SDK | Attribution/SDK problem — fix before spending more |
| Audience Network dominating with bad retention | Exclude Audience Network in placements |
| Volatile costs | Learning-limited — raise budget or optimize for installs rather than deep events |

**Retention is the honest metric.** A ₹15 install that uninstalls in a day costs more than a ₹60 install that stays.

---

## Quick reference

```
Objective        App promotion
Type             Manual app ads (at low budget)
Goal             App installs (starting) → App events (preferred, needs budget)
Platform         Android first in India
Floor            7.143 × target event cost
Must have        SDK/MMP + verified events BEFORE launching
Creative         App preview video showing real screens
Real KPI         cost per retained user, not CPI
Watch            Audience Network install quality
```

---

**Related:** [`P07`](P07-video-retarget-funnel-200.md) to build an audience cheaply first · [`../data/budget-engine.md`](../data/budget-engine.md)
