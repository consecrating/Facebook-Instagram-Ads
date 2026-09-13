# 03 — Meta Pixel & Conversions API

Needed for [P03](../playbooks/P03-website-leads.md), [P05](../playbooks/P05-ecommerce-sales.md), [P11](../playbooks/P11-catalog-retargeting.md).

**Not needed** for [P00](../playbooks/P00-BEST-low-budget-campaign.md) / [P01](../playbooks/P01-whatsapp-leads-200.md) (WhatsApp) or [P02](../playbooks/P02-instant-form-leads-200.md) (Instant Forms) — one of the main reasons those are the right starting point at low budget.

---

## Honest framing for low budgets

Website conversion campaigns need roughly 50 conversion events per ad set per week to exit the learning phase. If a website lead costs ~₹250, that's about **₹1,786/day**. At ₹200–500/day, a website-conversion campaign will not stabilise.

**So install the Pixel now for measurement and audience-building, but don't optimize for website conversions until your budget supports it.** Use WhatsApp or Instant Forms meanwhile. The Pixel still earns its keep by building retargeting audiences you'll use later.

---

## Step 1 — Create the Pixel (dataset)

1. **Events Manager** → **Connect data sources** → **Web** → **Meta Pixel**
2. Name it after your business → **Continue**
3. Note the **Pixel ID** (a long number)

## Step 2 — Install it

| Platform | Method |
|---|---|
| **WordPress** | Official *Meta pixel for WordPress* plugin, or paste base code into `<head>` via your theme/header plugin |
| **Shopify** | Settings → Apps → Facebook & Instagram, or paste Pixel ID in the sales-channel settings |
| **WooCommerce** | *Facebook for WooCommerce* plugin — handles standard e-commerce events automatically |
| **Wix / Squarespace** | Built-in Facebook Pixel field in marketing settings |
| **Custom site** | Paste the base code in `<head>` on every page |
| **Google Tag Manager** | Custom HTML tag, fire on All Pages |

## Step 3 — Set up events

**PageView** fires automatically from the base code. You need to define the events that represent business outcomes.

| Event | Fires when |
|---|---|
| `Lead` | Enquiry form submitted |
| `Contact` | Contact/callback requested |
| `Schedule` | Appointment booked |
| `AddToCart` | Item added to cart |
| `InitiateCheckout` | Checkout started |
| `Purchase` | Order confirmed — **always send a value** |
| `CompleteRegistration` | Signup finished |

Easiest route without a developer: **Events Manager → your Pixel → Add events → From the Pixel → Open Event Setup Tool.** It lets you click elements on your own site and map them to events visually.

For `Purchase`, always pass `value` and `currency: 'INR'`. Without value you cannot measure ROAS.

## Step 4 — Verify

1. Install the **Meta Pixel Helper** Chrome extension
2. Visit your site — it should show the Pixel firing
3. Complete a test enquiry/purchase — confirm the event appears
4. **Events Manager → Test events** — enter your URL and watch events arrive live

**Verify before spending.** A campaign optimizing for an event that never fires burns the entire budget and teaches Meta nothing.

---

## Conversions API (CAPI)

Browser-based tracking loses events to ad blockers, iOS privacy settings, and network drops. CAPI sends events **server-side**, recovering much of that loss.

### Is it worth it at low budget?

**Install if it's easy** (Shopify/WooCommerce integration, or a Conversions API Gateway). **Skip if it needs developer time** you'd rather spend on creative — at ₹200–500/day, better creative returns more than better tracking.

| Route | Effort |
|---|---|
| Shopify / WooCommerce official integration | Low — mostly toggles |
| Conversions API Gateway | Low–medium, may cost |
| Partner integration (Zapier, CRM connectors) | Medium |
| Direct server-side implementation | High — needs a developer |

### Deduplication matters

If both Pixel and CAPI send the same event, you must send a matching **`event_id`** so Meta deduplicates. Otherwise every conversion double-counts and your reported CPA looks half its real value — which is worse than no CAPI at all, because you'll make budget decisions on fantasy numbers.

---

## Audiences the Pixel unlocks

Even while optimizing for WhatsApp or forms, your Pixel quietly builds assets:

**Audiences → Create audience → Custom audience → Website**

| Audience | Use |
|---|---|
| All visitors, 30 days | Broad retargeting |
| Visitors, 180 days | Larger pool for lookalikes |
| Specific page visitors | Intent-based (e.g. pricing page) |
| Top 25% by time on site | Your most engaged visitors |
| `AddToCart` but not `Purchase` | Cart abandonment — usually the highest-ROI retargeting there is |

Then **Lookalike audiences** from your best source (purchasers or leads). A 1% lookalike of purchasers is typically the strongest prospecting audience available — but you need a source of roughly 1,000+ people for it to work well, so this is a later-stage tool.

> At low budget, don't split into many retargeting ad sets — you'll starve them all. One broad ad set beats five precise ones under ₹500/day.

---

## Checklist

- [ ] Pixel created, ID noted
- [ ] Base code on every page
- [ ] Business-outcome events defined
- [ ] `Purchase` passes value + `INR`
- [ ] **Verified with Pixel Helper AND Test Events**
- [ ] CAPI installed *if* low-effort, with `event_id` deduplication
- [ ] Retargeting audiences created (they need time to populate)
- [ ] You've checked whether your budget supports website-conversion optimization at all

---

**Next:** [`05-instant-forms.md`](05-instant-forms.md) · or [`../playbooks/README.md`](../playbooks/README.md)
