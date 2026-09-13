# P11 — Catalog & Dynamic Retargeting

Show people the exact products they viewed or added to cart. The highest-ROI campaign in e-commerce — but it needs an audience to work.

**Works at ₹200/day:** partly. Retargeting audiences are small, so events are few — but they convert at a much higher rate, so it can be worth running even while learning-limited.

---

## Prerequisites — all of them

- [ ] **Product catalog** uploaded and syncing → Commerce Manager
- [ ] **Pixel with `ViewContent`, `AddToCart`, `Purchase`** all firing, with `content_ids` matching catalog IDs
- [ ] **`content_ids` match exactly** between Pixel and catalog — if they don't, dynamic ads show wrong or no products
- [ ] Enough traffic to build an audience — **roughly 1,000+ website visitors** before this is worth running
- [ ] [P05](P05-ecommerce-sales.md) or another traffic source already running

> ⚠️ **The `content_ids` mismatch is the most common failure.** Verify in Events Manager that the product IDs your Pixel sends are the same IDs in your catalog. If your site sends SKU and your catalog uses a different ID, dynamic retargeting silently fails.

**No traffic yet?** This playbook has nobody to retarget. Run [P05](P05-ecommerce-sales.md) or [P07](P07-video-retarget-funnel-200.md) first.

---

## Step 1 — Upload the catalog

**Commerce Manager → Catalogs → Create catalog → E-commerce**

| Method | Notes |
|---|---|
| **Platform integration** | Shopify / WooCommerce — best option, auto-syncs stock and price |
| **Scheduled feed** | CSV/XML at a URL, refreshed on schedule |
| **Manual upload** | Small catalogues only; goes stale fast |

**Required fields:** `id`, `title`, `description`, `availability`, `condition`, `price` (with `INR`), `link`, `image_link`, `brand`.

**Get these right:**
- `price` must include currency — `499 INR`
- `availability` must be accurate. Advertising out-of-stock products wastes spend and annoys customers
- `image_link` should be a clean product image on a plain background — it appears at small sizes

Then **Catalog → Events → connect your Pixel** so catalog and events are linked.

---

## Step 2 — Build the retargeting audiences

**Audiences → Create audience → Custom audience → Website**

| Audience | Rule | Retention | Priority |
|---|---|---|---|
| `Cart abandoners` | `AddToCart` **AND NOT** `Purchase` | 7–14 days | ⭐ Highest ROI |
| `Product viewers` | `ViewContent` **AND NOT** `Purchase` | 14–30 days | High |
| `All visitors` | Any site visit, not purchasers | 30 days | Medium |
| `Past purchasers` | `Purchase` | 180 days | For upsell — **exclude from prospecting** |

**Cart abandoners with a short window is the highest-intent audience in advertising.** Someone who added to cart two days ago and didn't buy is closer to purchase than anyone else you can reach.

**Always exclude `Past purchasers`** from acquisition campaigns unless you're deliberately upselling. Paying to reacquire existing customers is a quiet, common waste.

---

## Step 3 — Campaign

1. **Objective:** **Sales**
2. **Name:** `RETARGET | Catalog | Sep26`
3. **Advantage campaign budget:** OFF
4. **Next**

## Step 4 — Ad set

1. **Name:** `Cart Abandoners | 14d | DPA`
2. **Conversion location:** **Website**
3. **Catalog:** turn **ON** and select your catalog
4. **Conversion event:** **Purchase**
   > Retargeting audiences convert well enough that Purchase is defensible here even at modest budget — but you'll likely be learning-limited. That's acceptable because intent is doing the work the algorithm normally would.
5. **Budget:** Daily, **₹100–300** is often enough
   > Retargeting audiences are small. Over-funding them causes high frequency and annoyance — people see your ad ten times a day and start disliking you. Watch frequency closely
6. **Bid:** Highest volume
7. **Audience → Retargeting:** select **`Cart abandoners`**
8. **Exclusions:** exclude **`Past purchasers`**
9. **Advantage+ Audience:** **OFF**
   > Deliberate narrowing again. The entire point is to reach only people who already showed intent
10. **Placements:** Advantage+ ON
11. **Next**

## Step 5 — Ads

**Format: Carousel** or **Collection**, with **dynamic** product population.

Meta fills in the exact products each person viewed. You write the frame, not the products.

**Dynamic text — use catalog placeholders:**
```
Primary text:  Still thinking about it? {{product.name}} is waiting
               in your cart — ₹{{product.price}}.
Headline:      {{product.name}}
Description:   {{product.current_price}}
```

**Retargeting copy that works:**
```
Still interested?

The items in your cart are still available.
✓ Free delivery above ₹[X]
✓ COD available
✓ Easy returns

Complete your order →
```

**Escalate the offer by audience temperature:**

| Audience | Offer |
|---|---|
| Cart abandoners, 1–3 days | Just a reminder. No discount — don't train people to abandon carts |
| Cart abandoners, 4–14 days | Free delivery, or a small nudge |
| Product viewers | Highlight benefits and reviews |
| Past purchasers | Complementary products, loyalty offer |

> **Don't discount immediately.** If every abandoned cart gets 10% off within an hour, customers learn to abandon carts. Wait a few days.

---

## Measurement contract

### Day 7
```
Spend:                        ₹______
Purchases:                     ______
ROAS:                          ______x
Frequency (7-day):             ______   ← watch this
Audience size:                 ______
Real CPA (COD/RTO adjusted):  ₹______
```

| Result | Action |
|---|---|
| High ROAS, frequency under 3 | Working. Retargeting ROAS is normally your best — enjoy it |
| Frequency above 3–4 | **Reduce budget** or widen the audience. You're over-serving |
| Audience too small to spend | Need more top-of-funnel traffic → [P05](P05-ecommerce-sales.md) |
| Dynamic ads showing wrong/no products | **`content_ids` mismatch** — fix Pixel/catalog alignment |
| Good ROAS but tiny volume | Normal. Retargeting scales only as fast as your traffic |

**Important:** retargeting ROAS always looks spectacular because you're harvesting demand you already paid to create. **Don't shift all budget from prospecting into retargeting** — you'll drain the pool and both will collapse. Retargeting captures; prospecting creates.

---

## Quick reference

```
Objective        Sales, with Catalog ON
Audience         Cart abandoners (AddToCart AND NOT Purchase), 7-14 days
Exclude          Past purchasers
Advantage+ aud   OFF (deliberate narrowing)
Budget           ₹100-300/day usually sufficient
Format           Carousel / Collection, dynamic placeholders
Watch            Frequency — above 3 means reduce budget
Must verify      content_ids match between Pixel and catalog
Never            shift all budget from prospecting to retargeting
```

---

---

## Facebook vs Instagram for catalog retargeting

**Run both — and here it matters more than usual.** Your retargeting audience is small, so you want every available placement to find those people cheaply. Restricting platforms would push frequency up fast.

| | Facebook | Instagram |
|---|---|---|
| Dynamic product ads | ✅ Feed, Marketplace, Video Feeds, right column | ✅ Feed, **Explore**, Stories, Reels |
| Best format | Carousel, Collection | **Carousel, Collection, Reels** |
| Strength | Broad reach across age groups | Visual browsing; Explore is strong for retargeting |

**Practical notes:**
- **Keep Advantage+ placements ON.** With a small audience you need breadth to keep frequency down — this is the opposite of the usual "narrow your retargeting" instinct
- **Instagram Explore** is a genuinely strong retargeting surface for product ads — people are already in browse mode
- **Watch frequency, not placement.** Above ~3.0 on a 7-day window, reduce budget or widen the audience window (7 days → 14 days). Restricting a platform is the wrong lever here
- **Product images must read at small sizes** on both platforms — clean background, single focal product. Instagram Explore renders them small
- Ensure `content_ids` match between Pixel and catalog, or dynamic ads break identically on both platforms

Full per-goal settings: [`../reference/facebook-vs-instagram.md`](../reference/facebook-vs-instagram.md)

---

**Related:** [`P05`](P05-ecommerce-sales.md) · [`../setup/03-pixel-and-capi.md`](../setup/03-pixel-and-capi.md) · [`P12`](P12-scaling-ladder.md) · [`../reference/facebook-vs-instagram.md`](../reference/facebook-vs-instagram.md)
