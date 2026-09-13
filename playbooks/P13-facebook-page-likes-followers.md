# P13 — Facebook Page Likes & Followers

Grow your **Facebook** Page audience. (For **Instagram** followers, use [P04](P04-instagram-followers.md).)

**Works at ₹200/day:** yes. Page likes are a cheap optimization event, so the learning-phase floor is low (~₹50–200/day).

---

## Read this before you spend a rupee

**Page likes are the weakest-value thing you can buy on Meta.** I'd be doing you a disservice not to say that plainly.

Two reasons:

1. **Organic Page reach is very low.** Getting 10,000 Page likes does *not* mean 10,000 people see your posts. A small fraction will. The "build an audience then post to them free" model largely stopped working years ago
2. **Meta's delivery does exactly what you ask.** Optimize for likes and it finds people who are good at *clicking like* — not people who buy. Those are different populations

```
Honest test — answer before proceeding:
  What will you DO with a Facebook follower?          ____________
  What is one follower worth to you in ₹?             ₹ ______
  If the answer is "not sure" or "₹0" → run P00 instead and get enquiries.
```

### Like vs Follow — they're different now

Facebook separated these. Someone can **follow** your Page without **liking** it, and vice versa.

- **Like** = the legacy signal, still the available optimization event
- **Follow** = who actually sees your posts in feed

**Followers are the number that matters.** Likes are what you can buy. That mismatch is worth knowing before you optimize for the buyable one.

### When this playbook IS legitimate

| Situation | Why it's justified |
|---|---|
| Brand new Page, 0 likes | An empty Page kills trust on every other campaign you run |
| Retargeting asset | Page engagers become a warm custom audience — **this is the real value** |
| Social proof for ads | Ads from a Page with 12 likes convert worse |
| Local business credibility | People check the Page before visiting or enquiring |
| Community/group model | You genuinely post and people genuinely engage |

**The strongest reason is the second one.** Treat this as *audience-building for later retargeting*, not as audience-building for organic reach. Framed that way it's a sound ₹100–200/day investment. Framed as "build a following and post free" it's a waste.

---

## Prerequisites

- [ ] Facebook Page, published, complete → [`../setup/01-page-and-business-manager.md`](../setup/01-page-and-business-manager.md)
- [ ] **5–10 genuine posts already published.** Advertising an empty Page converts nobody
- [ ] Profile photo + cover image
- [ ] Payment verified → [`../setup/02-payments-india-gst.md`](../setup/02-payments-india-gst.md)
- [ ] A realistic answer to "what will I do with these followers?"

---

## Step 1 — Campaign

**Ads Manager → + Create**

1. **Buying type:** Auction
2. **Objective:** **Engagement**
   > There is no standalone "Page Likes" objective under ODAX. Page likes live inside Engagement and you narrow to them at ad set level.
3. **Campaign name:** `ENG | Page Likes | Sep26`
4. **Special Ad Category:** blank unless applicable → [`../reference/policy-and-special-categories.md`](../reference/policy-and-special-categories.md)
5. **Advantage campaign budget (CBO):** **OFF**
6. **Next**

## Step 2 — Ad set

1. **Ad set name:** `Broad | Page Likes | [City]`
2. **Conversion location:** **On your Page**
   > If your account words it differently, look for the option that targets your Facebook Page rather than your ad, website or messaging apps.
3. **Facebook Page:** select yours
4. **Performance goal:** **Maximise number of Page likes**
5. **Budget:** Daily, **₹100–200**
   > Floor = `7.143 × cost per like`. Page likes are cheap, so ₹100–200/day genuinely exits learning here — one of the few goals where ₹200/day is comfortable rather than strained
6. **Bid strategy:** **Highest volume**
7. **Location:** your real service area. **Do not target all-India for a local shop** — followers who can never visit you are worthless
8. **Age / Gender:** as wide as genuinely relevant
9. **Advantage+ Audience:** **ON**
   > You may add **2–3 interest signals** here if your niche is specific — for Page likes, topical relevance matters more than purchase intent. Never stack ten.
10. **Languages:** blank — let creative self-select
11. **Placements:** **Manual → Facebook only**
    > ⚠️ **The exception to the usual Advantage+ placements rule.** An Instagram placement can't grow your Facebook Page. Select Facebook Feed, Facebook Reels, Facebook Stories, Facebook Marketplace/Video Feeds
12. **Next**

## Step 3 — Ads

**2–3 ads.** People are deciding "is this Page worth following?", so show value, not a sales pitch.

| Ad | What to use |
|---|---|
| **Ad 1** | Your best-performing **organic post** (highest shares/comments) |
| **Ad 2** | Short video introducing who you are and what you post |
| **Ad 3** | A genuinely useful tip / price-transparency post |

**Settings:**
- **Identity:** your Page
- **Media:** 4:5 (1080×1350) feed + 9:16 (1080×1920) for Facebook Reels/Stories → [`../reference/creative-specs.md`](../reference/creative-specs.md)
- **CTA:** **Like Page** (or **Follow Page** if offered)

### Copy — make the value of following explicit

Nobody follows a Page because you asked. They follow because they expect something.

```
[WHAT YOU POST], for [WHO], in [CITY].

✓ [Specific value — e.g. "Daily AC care tips"]
✓ [Specific value — e.g. "Honest price lists, no hidden charges"]
✓ [Specific value — e.g. "Same-day service updates"]

Follow for [CONCRETE BENEFIT].
```

**Weak:** "Like our page for updates!"
**Strong:** "We post real repair costs for every AC model in Jaipur. Follow so you never get overcharged again."

The second names a reason. The first names nothing.

---

## Step 4 — Build the audience (Day 1 — the actual payoff)

**Do this immediately.** This is the real return on the campaign.

**Ads Manager → Audiences → Create audience → Custom audience → Facebook Page**

| Audience | Include | Retention |
|---|---|---|
| `FB Page engagers - 365d` | Everyone who engaged with your Page | 365 days |
| `FB Page likers - 365d` | People who liked your Page | 365 days |

Then use them:
- **Retarget** with [P00 Click-to-WhatsApp](P00-BEST-low-budget-campaign.md) — warm audiences convert far better than cold
- **Exclude** from prospecting so you stop paying to reach people you already have
- **Lookalike source** once you're past ~1,000 people

**This is why the campaign is worth running.** The follower count is a by-product; the retargetable audience is the asset.

---

## Measurement contract

### Baseline, before launching
```
Date:                    ______
Page likes:              ______
Page followers:          ______
Avg daily organic growth: ______
```

### Day 7
```
Spend:                          ₹______
Page likes gained:               ______
Cost per Page like:             ₹______
Followers gained:                ______   ← track separately from likes
Minus organic baseline:          ______
Page engagers audience size:     ______   ← THE number that matters
```

| Result | Action |
|---|---|
| Audience past ~1,000 | **Reduce or stop.** Move budget to [P00](P00-BEST-low-budget-campaign.md) and retarget them |
| Likes cheap, followers flat | You're buying likes from people who won't see your posts. Normal — value is the audience, not the count |
| Likes expensive | Content isn't worth following. Fix organic before paying |
| Post reach still tiny after growth | **Expected.** Organic Page reach is low. Don't buy more likes hoping to fix it |

### Time-box it
**Run 2–4 weeks, then stop.** Once you have social proof and a retargetable audience, this has done its job. Buying Page likes indefinitely is buying a number.

---

## Facebook vs Instagram — which to grow?

| | Facebook Page (P13) | Instagram (P04) |
|---|---|---|
| Cost per follower in India | Usually cheaper | Usually higher |
| Organic reach to followers | Very low | Better, especially Reels |
| Best for | Local business credibility, older demographics | Creators, retail, visual products, younger demographics |
| Retargeting value | ✅ High | ✅ High |
| Placement setting | **Facebook only** | **Instagram only** |

**If you only do one and you're a local service business:** Facebook, because it's cheaper and your customers likely check it.
**If your product is visual or your customers are under 35:** Instagram.
**If you want enquiries rather than an audience:** neither — run [P00](P00-BEST-low-budget-campaign.md).

Full platform comparison: [`../reference/facebook-vs-instagram.md`](../reference/facebook-vs-instagram.md)

---

## Quick reference

```
Objective        Engagement
Conversion loc   On your Page
Performance goal Maximise number of Page likes
Budget           ₹100-200/day (cheap event, low floor — ₹200 comfortable here)
Bid              Highest volume
Placements       MANUAL → Facebook only  (the exception)
Advantage+ aud   ON, up to 2-3 interest signals allowed
Creative         Best ORGANIC post + value-led copy
Duration         2-4 weeks, then STOP
Real output      FB Page engager audience (365d) for retargeting
Honest caveat    likes ≠ reach. Buy the audience, not the number.
```

---

**Related:** [`P04`](P04-instagram-followers.md) Instagram followers · [`P08`](P08-engagement-social-proof.md) post engagement & likes · [`P00`](P00-BEST-low-budget-campaign.md) if you want enquiries · [`../reference/facebook-vs-instagram.md`](../reference/facebook-vs-instagram.md)
