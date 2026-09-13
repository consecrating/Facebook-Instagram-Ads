# P06 — Local Footfall

Get people physically into your shop, clinic, salon, restaurant or showroom.

**Works at ₹200/day:** yes — this is one of the best low-budget use cases, because a tight radius means low competition and low CPMs.

---

## The core insight

**Radius is your best friend at low budget.** Most advertisers target too wide. If your customers realistically travel 5 km to reach you, targeting a 50 km radius means ~90% of your spend reaches people who will never visit.

A 5 km radius in a Tier-2 city can be genuinely cheap to saturate on ₹200/day. That's the whole advantage.

```
Honestly, how far will someone travel to you?
  Restaurant / café / salon:     3–7 km
  Clinic / gym / tuition:        5–10 km
  Showroom / specialist retail:  10–25 km
  Destination / high-ticket:     city-wide
```

Start at the **low end** of your band. Widen only if delivery is starved.

---

## Prerequisites

- [ ] **Page with a correct address** — required for location features
- [ ] Google Maps location accurate (people will check before visiting)
- [ ] Instagram linked
- [ ] Payment verified
- [ ] Photos of the actual place — interior, exterior, product, staff

---

## Choose your conversion path

Meta's "Store traffic" objective is built for multi-location brands. **For a single location, these usually work better:**

| Path | Objective | Best for |
|---|---|---|
| **A — WhatsApp enquiry** | Engagement → WhatsApp | Appointments, bookings, "is it available?" |
| **B — Awareness/reach** | Awareness | Being known locally; pure footfall |
| **C — Traffic to directions** | Traffic | Sending people to Maps |

**Recommended: A.** A WhatsApp enquiry is measurable; footfall largely isn't. You can count conversations. You cannot count people who saw your ad and walked in next Tuesday.

If you truly just want local visibility, B is cheap and honest — but accept you can't attribute it.

---

## Build — Path A (recommended)

### Step 1 — Campaign
1. **Objective:** **Engagement**
2. **Name:** `LOCAL | [Business] | [Area] | Sep26`
3. **Advantage campaign budget:** OFF

### Step 2 — Ad set
1. **Name:** `Radius 5km | WhatsApp | [Area]`
2. **Conversion location:** **WhatsApp** → [`../setup/04-whatsapp-business.md`](../setup/04-whatsapp-business.md)
3. **Performance goal:** Maximise conversations
4. **Budget:** Daily, ₹200 (compute your floor: `7.143 × cost per conversation`)
5. **Bid:** Highest volume
6. **Location — the important part:**
   - Click **Edit** on location → search your address or drop a pin
   - Set radius: start **5 km** (or your band's low end)
   - Choose **"People living in or recently in this location"**
     > Not "People travelling in this location" unless you're targeting tourists, and not "People living in" only if you want commuters and visitors too. For most local businesses, "living in or recently in" is right.
7. **Age:** wide
8. **Gender:** All unless genuinely specific
9. **Advantage+ Audience:** **ON**, fields empty
   > Location is always respected as a hard constraint even with Advantage+ on, so you keep your radius. Only the demographic/interest inputs are treated as signals.
10. **Placements:** Advantage+ ON

### Step 3 — Ads

**Three ads.** For local, authenticity beats polish decisively — people want to see the actual place.

- **Ad 1:** photo of your actual premises/product, with price
- **Ad 2:** short video walkthrough, shot on a phone
- **Ad 3:** offer-led static (first visit discount, combo, etc.)

**Copy frame — name the locality explicitly:**
```
[SERVICE] in [SPECIFIC LOCALITY, not just city]

[OFFER] — ₹[PRICE]
📍 [Landmark-based address]
🕐 Open [hours]

WhatsApp to book: [CTA]
```

**Why landmarks:** "Opposite [known landmark]" works far better in India than a street address. People navigate by landmark.

**Local copy rules:**
- Name the **locality/neighbourhood**, not just the city. "Vaishali Nagar" beats "Jaipur"
- Use the local language if that's what your customers speak
- Show the price
- Include opening hours — it prevents wasted trips and wasted enquiries
- One landmark reference

---

## Dayparting — genuinely useful here

Unlike most low-budget advice, restricting hours makes sense for local businesses: there's no point advertising a restaurant at 4am or a clinic when it's shut.

**Ad set → Budget & schedule → Show ads on a schedule** (requires a **lifetime** budget, not daily).

```
Restaurant:  11:00–14:00 and 18:00–22:00
Salon:       10:00–19:00
Clinic:      08:00–11:00 and 17:00–20:00
Retail:      opening hours only
```

**Trade-off:** lifetime budgets are less flexible and dayparting concentrates your already-small budget into fewer hours — which can actually *help* by increasing spend density during hours that matter. But it also makes the learning phase slower. At ₹200/day, try it only after you have a working baseline from a daily-budget version.

---

## Measurement contract

Footfall is genuinely hard to attribute. Measure what you can, and measure it manually.

### Baseline, before launching
```
Average daily walk-ins:        ______
Average daily enquiries:       ______
Average bill value:           ₹______
```

### Day 7
```
WhatsApp conversations:        ______
Spend:                        ₹______
Cost per conversation:        ₹______
Walk-ins now (daily avg):      ______
Change vs baseline:            ______
```

### The manual attribution that actually works

**Ask every customer: "How did you hear about us?"** Train staff to log it. One line in a notebook.

Better: put a **specific offer code in the ad** — "Mention FB20 for 20% off". Now footfall is countable. This is low-tech and far more reliable than any platform attribution for a single-location business.

| Result | Action |
|---|---|
| Cost per conversation × close rate < margin per visit | Working → widen radius slightly, or [P12](P12-scaling-ladder.md) |
| Conversations but no visits | Distance, price, or hours mismatch. Check what they ask about |
| No conversations | Radius too tight, or offer too weak. Widen to the next band |
| Visits up but unprofitable | Discount too deep — reduce the offer, keep the reach |

---

## Quick reference

```
Objective        Engagement → WhatsApp  (Path A, recommended)
Radius           START TIGHT: 5 km, widen only if starved
Location type    "People living in or recently in this location"
Budget           ₹200/day viable; floor = 7.143 × cost per conversation
Advantage+       Audience ON (location still hard-respected), Placements ON
Creative         Real photos of the real place > polished stock
Copy             Locality name + landmark + price + hours
Dayparting       Useful here, but needs lifetime budget
Attribution      Offer code + "how did you hear about us" log
```

---

**Related:** [`P00`](P00-BEST-low-budget-campaign.md) · [`P09`](P09-appointment-booking.md) · [`../reference/targeting-india.md`](../reference/targeting-india.md)
