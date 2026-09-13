# P05 — E-commerce Sales

Optimize for purchases on your online store.

## ⚠️ Budget reality first

Purchase events are the most expensive rung on the ladder. The learning-phase floor is `7.143 × cost per purchase`:

```
₹500 per purchase   →  ₹3,571/day
₹900 per purchase   →  ₹6,429/day
₹2,000 per purchase →  ₹14,286/day
```

**At ₹200–1,000/day, a Purchase-optimized campaign will not exit the learning phase.**

### What to do instead at low budget

| Budget | Do this |
|---|---|
| Under ₹1,000/day | **[P00 Click-to-WhatsApp](P00-BEST-low-budget-campaign.md)** — sell via chat. Confirm orders manually, cut RTO, keep the contact |
| ₹1,000–3,000/day | Optimize for **`AddToCart`** or **`InitiateCheckout`** — cheaper events that exit learning, and still teach Meta who buys |
| ₹3,000+/day | This playbook, optimizing for **Purchase** |

For Indian D2C at low budget, **CTWA often beats website purchase campaigns outright** — you get a conversation, confirm the order before dispatch, and cut return-to-origin losses.

---

## The COD / RTO problem — do this maths first

This is the single most important calculation for Indian e-commerce, and Ads Manager will never show it to you.

```
Ads Manager reports:      100 purchases at ₹400 CPA
COD share of orders:      60%
RTO rate on COD:          30%

Orders actually delivered = 100 − (100 × 0.60 × 0.30) = 82
Real CPA                  = (100 × 400) ÷ 82 = ₹488
```

**Your real CPA is 22% higher than reported.** If you optimize against the reported number, you will scale a campaign that's losing money.

```
Your numbers:
  AOV                    ₹ ______
  Gross margin             ______%
  COD share                ______%
  RTO rate on COD          ______%
  Reported CPA           ₹ ______

  Real CPA = reported CPA ÷ (1 − COD% × RTO%)   = ₹ ______
  Contribution per delivered order = AOV × margin − real CPA = ₹ ______
```

If that last line is negative, stop advertising and fix the offer, pricing or RTO first. More budget accelerates the loss.

**RTO reduction beats CPA reduction.** Prepaid discounts, order-confirmation calls or a WhatsApp confirmation step typically move profit more than any bidding change.

---

## Prerequisites

- [ ] Store with working checkout, fast on Indian mobile data
- [ ] **Pixel + `Purchase` event passing `value` and `currency: INR`** → [`../setup/03-pixel-and-capi.md`](../setup/03-pixel-and-capi.md)
- [ ] `AddToCart` and `InitiateCheckout` also firing
- [ ] **CAPI installed** — for e-commerce this genuinely matters. Use the Shopify/WooCommerce integration
- [ ] **`event_id` deduplication verified** — double-counted purchases halve your apparent CPA and will make you scale a loser
- [ ] Product catalog uploaded (for [P11](P11-catalog-retargeting.md))
- [ ] Your RTO maths done

---

## Step 1 — Campaign

1. **Objective:** **Sales**
2. **Name:** `SALES | [Category] | Sep26`
3. **Advantage+ Shopping Campaign (ASC):** consider it if offered and your budget is ₹3,000+/day — it's largely automated and performs well at scale. **For manual control at lower budget, choose the standard Sales campaign.**
4. **Advantage campaign budget:** OFF below ₹3,000/day
5. **Next**

## Step 2 — Ad set

1. **Name:** `Broad | Purchase | India`
2. **Conversion location:** **Website**
3. **Pixel** → yours
4. **Conversion event:**
   - ₹3,000+/day → **Purchase**
   - ₹1,000–3,000/day → **InitiateCheckout** or **AddToCart**
   - Below ₹1,000/day → don't run this; use P00
5. **Budget:** Daily, ≥ `7.143 × your CPA`
6. **Bid strategy:** **Highest volume**. Add **ROAS goal** only once you have stable conversion history
7. **Location:** where you actually ship. Exclude pin codes you can't serve
8. **Age / Gender:** wide unless the product is genuinely specific
9. **Advantage+ Audience:** **ON**, fields empty
10. **Placements:** Advantage+ ON
11. **Next**

## Step 3 — Ads

**Three ads**, and for e-commerce the format hierarchy is fairly reliable:

- **Ad 1 — Video / UGC.** Product in use, filmed like a real person filmed it. Usually the top performer in India
- **Ad 2 — Carousel.** Multiple products or multiple angles. Good for browsing intent
- **Ad 3 — Static with price + offer.** Clear, direct

**Copy frame:**
```
[HOOK — outcome or problem]

[PRODUCT] — ₹[PRICE]
✓ [Key benefit]
✓ [Differentiator]
✓ [Risk reversal — returns, warranty, COD available]

[Free delivery / offer]. Shop now →
```

**India-specific copy notes:**
- **Say "COD available"** if you offer it — it materially lifts conversion
- Show the price. Hiding it costs you qualified clicks
- Free delivery threshold works well: "Free delivery above ₹499"
- Festive framing (Diwali, wedding season) works, but expect higher CPMs then

---

## Measurement contract

### Day 3 — breakage only
- `Purchase` firing correctly in Events Manager?
- No duplicate events? (Compare Ads Manager purchases against your store's real order count)
- CTR ≥ ~0.8%?
- Checkout funnel intact: view → cart → checkout → purchase?

### Day 7
```
Reported CPA      = spend ÷ purchases            = ₹ ______
Real CPA          = reported ÷ (1 − COD% × RTO%) = ₹ ______
ROAS              = revenue ÷ spend              = ______x
Contribution      = AOV × margin − real CPA      = ₹ ______
True floor        = 7.143 × reported CPA         = ₹ ______ /day
```

| Result | Action |
|---|---|
| Contribution positive, budget ≥ floor | Working → [P12](P12-scaling-ladder.md) + add [P11](P11-catalog-retargeting.md) |
| Contribution positive, below floor | Raise to floor, or concentrate budget into fewer days |
| Contribution negative | Fix RTO / price / offer. **Do not scale** |
| Store orders ≠ Ads Manager purchases | Tracking or dedup problem — fix before deciding anything |
| Traffic but no purchases | Checkout or trust problem, not an ads problem |

### The funnel diagnostic
```
Link clicks → Landing page views → AddToCart → InitiateCheckout → Purchase
```
Find the biggest drop and fix that step. Ads only control the first arrow.

---

## Quick reference

```
Objective        Sales
Event            Purchase (₹3,000+/day) · AddToCart/InitiateCheckout (₹1,000-3,000)
Under ₹1,000/day Use P00 Click-to-WhatsApp instead
Floor            7.143 × cost per purchase
Must have        Pixel + CAPI + value/INR + event_id dedup
Must compute     Real CPA adjusted for COD × RTO
Creative         UGC video > carousel > static
Next step        P11 catalog retargeting
```

---

---

## Facebook vs Instagram for e-commerce

**Run both in one ad set.** Do not split — you'd halve the conversion signal on each, and purchase events are already the hardest rung to accumulate.

| | Facebook | Instagram |
|---|---|---|
| Strength | Marketplace, older buyers, Tier-2/3 reach | Product discovery, visual browsing |
| Best placements | Feed, Video Feeds, Marketplace | **Reels, Explore, Feed** |
| Best format | Carousel, static + price | **Reels video, carousel** |
| Buyer skew | Broader age range, often more price-led | Younger, more brand/aesthetic-led |
| COD messaging | Works well — say it plainly | Works well |

**Practical notes:**
- **Instagram Reels and Explore are usually your cheapest discovery inventory** for D2C. Always upload a 9:16 asset or you forfeit them
- **Facebook Marketplace** can deliver very cheap traffic for physical goods — Advantage+ placements will find it for you
- If you have a **catalog**, connect it so both platforms can serve dynamic product ads → [P11](P11-catalog-retargeting.md)
- Check **Breakdown → Placement** only once you're above ~₹1,000/day. Below that the split is too thin to act on
- If one platform clearly wins at scale, splitting by platform is a legitimate *horizontal* scaling move — but only above ~₹600/day → [P12](P12-scaling-ladder.md)

Full per-goal settings: [`../reference/facebook-vs-instagram.md`](../reference/facebook-vs-instagram.md)

---

**Related:** [`P11`](P11-catalog-retargeting.md) · [`P00`](P00-BEST-low-budget-campaign.md) · [`../setup/03-pixel-and-capi.md`](../setup/03-pixel-and-capi.md) · [`../reference/facebook-vs-instagram.md`](../reference/facebook-vs-instagram.md)
