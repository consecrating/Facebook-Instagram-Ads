# P02 — Instant Form Leads

Leads collected in a form that opens **inside** Facebook/Instagram. No website needed, no page load, fields pre-fill from the user's profile.

**Choose this over [P00 WhatsApp](P00-BEST-low-budget-campaign.md) when:** you need structured data (budget, timeline, documents), you'll call rather than chat, or you're feeding a CRM.
**Choose P00 instead when:** you'd rather have a conversation, or you can't call leads back quickly.

---

## Budget reality

Instant Form leads typically cost **tens of rupees**, so the learning-phase floor (`7.143 × CPA`) lands around **₹300–700/day**.

**At ₹200/day this ad set will be Learning Limited.** It still produces leads — costs are just volatile and higher than they'd be at the floor. Compute your own number:

```
Your measured cost per lead × 7.143 = your true floor = ₹ ______ /day
```

If ₹200/day is fixed, [P07](P07-video-retarget-funnel-200.md) is the better structure.

---

## Prerequisites

- [ ] Page + Instagram
- [ ] Payment verified → [`../setup/02-payments-india-gst.md`](../setup/02-payments-india-gst.md)
- [ ] **Privacy policy URL** — mandatory, ads get rejected without it
- [ ] **Lead delivery set up and tested** → [`../setup/05-instant-forms.md`](../setup/05-instant-forms.md)
- [ ] Someone who will call leads back within minutes

> ⚠️ **Test lead delivery before launching.** The most expensive failure in this playbook is leads accumulating in a Forms Library nobody opens.

---

## Step 1 — Campaign

**Ads Manager → + Create**

1. **Objective:** **Leads**
2. **Campaign name:** `LEADS | Instant Form | Sep26`
3. **Special Ad Category:** declare if you advertise credit, employment, or housing — **required**, and it restricts targeting → [`../reference/policy-and-special-categories.md`](../reference/policy-and-special-categories.md)
4. **Advantage campaign budget:** **OFF**
5. **Next**

## Step 2 — Ad set

1. **Ad set name:** `Broad | Form | [City] | 25-55`
2. **Conversion location:** **Instant forms**
3. **Performance goal:** **Maximise number of leads**
4. **Budget:** Daily — your computed number (₹200 minimum, floor is higher)
5. **Bid strategy:** **Highest volume**
   > A cost-per-result goal needs daily budget ≥ 5× the target cost. At ₹200/day your cap couldn't exceed ₹40 — not workable. Use Highest volume.
6. **Location:** your service area
7. **Age:** wide. `25–55` unless you have evidence to narrow
8. **Gender:** All
9. **Advantage+ Audience:** **ON**, fields empty
10. **Placements:** **Advantage+** ON
11. **Next**

## Step 3 — The form

At ad level → **Instant form → Create form**. Full detail in [`../setup/05-instant-forms.md`](../setup/05-instant-forms.md).

Key decisions:

| Setting | Recommendation |
|---|---|
| Form type | **Higher intent** — adds a review step, ~30–40% fewer leads, noticeably better quality |
| Fields | 3–4 maximum. **Name + Phone + one qualifier** |
| Email | Optional. In India phone matters far more |
| Qualifier | Multiple choice on budget or timeline |
| Intro | State your price range — the strongest filter you have |
| Completion screen | Expectation + a WhatsApp button |

**The qualifier that does the most work:**

```
What's your budget range?
  ○ Under ₹XX,000
  ○ ₹XX,000 – ₹XX,000
  ○ Above ₹XX,000
  ○ Just researching
```

"Just researching" self-identifies who not to call first. That's free prioritisation.

## Step 4 — Ads

**Three ads** in the one ad set:

- **Ad 1:** static image, offer + price
- **Ad 2:** 15–30s video
- **Ad 3:** carousel, or a second static with a different hook

For each:
- **CTA:** **Get quote**, **Apply now**, **Book now**, or **Learn more** — match your actual offer
- **Primary text:** hook in line 1; everything else is hidden behind "…more"
- **Media:** 4:5 or 1:1 feed, 9:16 stories/reels → [`../reference/creative-specs.md`](../reference/creative-specs.md)

**Copy frame:**

```
[HOOK — the problem or the outcome]

[SPECIFIC OFFER with ₹ price or range]
✓ [Benefit 1]
✓ [Benefit 2]
✓ [Trust signal — years, count, certification]

[LOCATION]. Fill the form, we'll call within [X] hours.
```

**Publish.**

---

## Step 5 — The follow-up system

This playbook lives or dies here. A form lead is colder than a WhatsApp chat — they filled a form and moved on. Your only advantage is speed.

**Non-negotiables:**

1. **Call within 5 minutes** during business hours
2. **Three attempts minimum**, spread across different times of day
3. **WhatsApp after the second missed call** — often gets a reply when calls don't:
   ```
   Hi [Name], this is [You] from [Business]. You enquired about
   [SERVICE] — tried calling but couldn't reach you.
   Happy to share details here if easier?
   ```
4. **Log every outcome.** Contacted / Not reachable / Quoted / Won / Lost

**Track your contact rate:**
```
Contact rate = leads reached ÷ leads received
```
Under ~50% and your problem is follow-up, not ads. More budget will not help.

---

## Measurement contract

### Day 3 — breakage check only

| Check | Healthy | If not |
|---|---|---|
| Delivering | Active | Check payment, review status, privacy URL |
| CTR (link) | ≥ ~0.8% | Creative problem — swap weakest ad |
| Form opens vs leads | Reasonable ratio | Form too long — cut fields |
| Leads reaching you | Yes | **Fix delivery immediately** |

**No budget or targeting edits on Day 3.**

### Day 7 — the real read

```
Cost per lead     = spend ÷ leads              = ₹ ______
Contact rate      = reached ÷ received         = ______%
Effective CPL     = spend ÷ leads reached      = ₹ ______   ← the honest number
True floor        = 7.143 × cost per lead      = ₹ ______ /day
```

**Effective CPL is what matters.** ₹50 leads with a 40% contact rate is really ₹125 per usable lead.

| Result | Action |
|---|---|
| Effective CPL ≤ affordable CPL | Working → [P12](P12-scaling-ladder.md) |
| Contact rate under 50% | Fix follow-up before anything else |
| Leads cheap but never buy | Switch to Higher intent + add qualifiers |
| Too few leads | Widen location/age; add creative |
| Volatile costs | Learning-limited — raise to floor or accept |

---

## Instant Forms vs WhatsApp — honest comparison

| | Instant Form | WhatsApp (P00) |
|---|---|---|
| Structured data | ✅ Yes | ❌ You must ask |
| Lead warmth | Colder | Warmer |
| Reported CPL | Higher | 30–50% lower |
| CRM-friendly | ✅ | Harder |
| Needs fast callback | Critical | Less brittle |
| Contact rate risk | High — wrong numbers, no answer | Lower — message sits in the thread |
| Best for | Volume + structured qualification | Conversation-led selling |

**For most Indian small businesses, P00 outperforms this playbook.** Use P02 when you specifically need the structured data or a CRM handoff.

---

## Quick reference

```
Objective        Leads
Conversion loc   Instant forms
Performance goal Maximise number of leads
Form type        Higher intent
Fields           Name + Phone + 1 multiple-choice qualifier
Structure        1 campaign → 1 ad set → 3 ads
Bid              Highest volume
Advantage+       Audience ON (empty), Placements ON
Floor            7.143 × your cost per lead
Follow-up        Call in 5 min · 3 attempts · WhatsApp backup
```

---

**Related:** [`P00`](P00-BEST-low-budget-campaign.md) · [`P09`](P09-appointment-booking.md) for bookings · [`../setup/05-instant-forms.md`](../setup/05-instant-forms.md)
