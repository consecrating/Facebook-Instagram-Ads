# P03 — Website Leads (Pixel / CAPI)

Send people to your site and optimize for enquiries submitted there.

## ⚠️ Budget warning — read before building

Website leads typically cost **low hundreds of ₹**. The learning-phase floor is `7.143 × CPA`:

```
₹250 per lead  →  ₹1,786/day  to exit learning
₹400 per lead  →  ₹2,857/day
```

**At ₹200–500/day this campaign will not stabilise.** Meta can't gather 50 website-lead events per week on that budget, so delivery stays volatile and expensive indefinitely.

**If your budget is under ~₹1,500/day, use [P00 WhatsApp](P00-BEST-low-budget-campaign.md) or [P02 Instant Forms](P02-instant-form-leads-200.md) instead.** They reach the same outcome for far less, because the event is cheaper.

Build this when your budget genuinely supports it — or when you specifically need people on your site (detailed product info, long-form proof, a booking system).

---

## Prerequisites

- [ ] Website that loads fast on Indian mobile data — **test on 4G, not office WiFi**
- [ ] **Meta Pixel installed and verified** → [`../setup/03-pixel-and-capi.md`](../setup/03-pixel-and-capi.md)
- [ ] A `Lead` event firing on form submission — **verified in Test Events**
- [ ] CAPI if low-effort (Shopify/WooCommerce integration)
- [ ] Budget at or near `7.143 × expected CPL`

> Page speed is the silent killer. If your landing page takes 6 seconds on mobile data, you're paying for clicks that never become page views. Check the **landing page views ÷ link clicks** ratio — below ~70% and you have a speed or relevance problem.

---

## Step 1 — Campaign

1. **Objective:** **Leads**
2. **Name:** `LEADS | Website | Sep26`
3. **Special Ad Category:** declare if applicable
4. **Advantage campaign budget:** OFF
5. **Next**

## Step 2 — Ad set

1. **Name:** `Broad | Website Lead | [City]`
2. **Conversion location:** **Website**
3. **Pixel:** select yours
4. **Conversion event:** **Lead**
   > If you're getting fewer than ~50 Leads/week, temporarily optimize for a **cheaper upstream event** instead — `Landing page view` or `Contact`. You'll exit learning, and Meta still learns who engages. Move up to `Lead` once volume supports it. This is the ladder principle from [`../data/budget-engine.md`](../data/budget-engine.md).
5. **Budget:** Daily, your computed floor
6. **Bid strategy:** Highest volume
7. **Location / Age / Gender:** your service area, wide age, All
8. **Advantage+ Audience:** ON, fields empty
9. **Placements:** Advantage+ ON
10. **Next**

## Step 3 — Ads

**Three ads.** URL must include UTM parameters so you can reconcile Meta's numbers against your own analytics:

```
https://yoursite.com/enquiry?utm_source=facebook&utm_medium=cpc&utm_campaign=leads_sep26&utm_content=ad1
```

- **CTA:** **Learn more**, **Get quote**, **Sign up**
- **Media:** 4:5 / 1:1 feed, 9:16 stories → [`../reference/creative-specs.md`](../reference/creative-specs.md)

### The landing page rules that matter

The ad gets the click; the page decides everything after.

- **Message match.** The page headline must repeat the ad's promise. Mismatch is the biggest leak
- **One action.** Remove nav, remove alternative links
- **Form above the fold**, 3–4 fields, **phone first**
- **Price or range visible** — otherwise every enquiry starts from zero
- **Trust signals:** real photos, real testimonials, GST/registration number, address
- **WhatsApp button as a fallback** — many Indian users prefer it to a form. Capture them rather than losing them

---

## Measurement contract

### Day 3 — breakage only

| Check | Healthy | If not |
|---|---|---|
| Pixel firing `Lead` | Yes, in Events Manager | **Stop and fix tracking** |
| Landing page views ÷ link clicks | ≥ ~70% | Page too slow or mismatched |
| CTR (link) | ≥ ~0.8% | Creative problem |

### Day 7

```
Cost per lead        = spend ÷ leads (Ads Manager)    = ₹ ______
Actual enquiries     (from your own inbox/CRM)          ______
Real cost per lead   = spend ÷ actual enquiries        = ₹ ______
True floor           = 7.143 × cost per lead           = ₹ ______ /day
```

> Reconcile Meta's reported leads against your real inbox. Discrepancies mean tracking problems, duplicate events (check `event_id` deduplication), or attribution-window effects. Trust your inbox.

| Result | Action |
|---|---|
| Real CPL ≤ affordable CPL, budget ≥ floor | Working → [P12](P12-scaling-ladder.md) |
| Profitable but volatile | Learning-limited — raise to floor or drop to a cheaper event |
| Clicks but no leads | Landing page problem, not an ads problem |
| Meta reports leads you never received | Tracking or dedup issue → [`../setup/03-pixel-and-capi.md`](../setup/03-pixel-and-capi.md) |

---

## Quick reference

```
Objective        Leads
Conversion loc   Website
Event            Lead  (or a cheaper upstream event if under 50/week)
Budget           7.143 × expected CPL  — usually ₹1,500+/day
Bid              Highest volume
Advantage+       Audience ON (empty), Placements ON
Must verify      Pixel Lead event, page speed on 4G, UTMs
Under ₹1,500/day Use P00 or P02 instead
```

---

**Related:** [`P00`](P00-BEST-low-budget-campaign.md) · [`P02`](P02-instant-form-leads-200.md) · [`../setup/03-pixel-and-capi.md`](../setup/03-pixel-and-capi.md)
