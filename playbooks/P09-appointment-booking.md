# P09 — Appointment & Booking

For clinics, salons, gyms, consultants, tuition demos, property site visits, test drives.

**Works at ₹200/day:** yes, learning-limited. Floor is roughly `7.143 × cost per booking`.

---

## The strategic move: sell the appointment, not the service

Don't advertise the ₹40,000 treatment. Advertise the ₹0 consultation.

| | Selling the service | Selling the appointment |
|---|---|---|
| Commitment asked | High | Low |
| Cost per action | High | Much lower |
| Learning-phase floor | High | Lower — often reachable at ₹200–400/day |
| Where you close | In the ad | In person, where you're strongest |

**This is the ladder principle applied to your offer, not just your optimization event.** A free consultation is a cheaper event, so it exits learning on a smaller budget — and you close in person, which almost every service business does better than a landing page.

**Also a policy benefit:** for healthcare and fitness, advertising a consultation is far safer than advertising treatments or outcomes. See [`../reference/policy-and-special-categories.md`](../reference/policy-and-special-categories.md).

---

## Choose your booking mechanism

| Mechanism | Friction | Best when |
|---|---|---|
| **WhatsApp** → book in chat | Lowest | Default choice in India. Flexible, human |
| **Instant Form** with appointment request | Low | You need structured details first |
| **Website booking system** | Higher | You have real-time slot management |
| **Call now** | Low | You reliably answer the phone |

**Recommended: WhatsApp.** Booking in chat lets you qualify, handle objections and reschedule — none of which a form can do. Slot-picker tools look tidy but leak bookings in India.

---

## Build — WhatsApp booking (recommended)

### Step 1 — Campaign
1. **Objective:** **Engagement**
2. **Name:** `BOOK | [Service] | Sep26`
3. **Special Ad Category:** ⚠️ declare if this is housing (property visits) — see policy file
4. **Advantage campaign budget:** OFF

### Step 2 — Ad set
1. **Name:** `Broad | Booking | [Area]`
2. **Conversion location:** **WhatsApp**
3. **Performance goal:** Maximise conversations
4. **Budget:** Daily, ₹200+ (floor = `7.143 × cost per booking`)
5. **Bid:** Highest volume
6. **Location:** realistic travel radius — people must physically come. 5–15 km for most
7. **Age / Gender:** as wide as genuinely relevant
8. **Advantage+ Audience:** ON, fields empty
9. **Placements:** Advantage+ ON

### Step 3 — Ads

**Three ads.** Lead with the free/low-commitment appointment:

**Copy frame:**
```
[PROBLEM they recognise]

Free [CONSULTATION/TRIAL/SITE VISIT] at [BUSINESS], [LOCALITY]

✓ [What happens in the appointment — be specific]
✓ [Duration — "takes 20 minutes"]
✓ No obligation

📍 [Landmark address]  🕐 [Hours]
WhatsApp to book your slot →
```

**Say what actually happens in the appointment.** "Free consultation" is vague and slightly suspicious. "20-minute check-up, we'll assess X and give you a written quote" converts far better because it removes uncertainty.

**Pre-filled message — collect the slot preference immediately:**
```
Hi! I'd like to book a free [SERVICE]. My preferred time is ______.
```

---

## Step 4 — The no-show problem

This is where booking campaigns actually fail. Free appointments have high no-show rates, and a no-show is 100% wasted ad spend.

**The confirmation sequence:**

```
On booking:   "Booked! [Day] at [Time] at [Address + landmark].
               Reply CONFIRM to hold your slot."
              → asking for a reply filters out casual bookers immediately

Day before:   "Hi [Name], reminder: [Service] tomorrow at [Time].
               Reply YES to confirm or tell me a better time."

2h before:    "See you at [Time]! Here's the location: [Maps link]"
```

**What genuinely reduces no-shows:**
- Ask for a confirmation reply — non-repliers rarely show
- Offer a specific slot, not "come anytime". Vague appointments don't get honoured
- Send a Google Maps link, not an address
- Take a small refundable/adjustable booking amount for high-value appointments. Even ₹100 transforms show-up rates
- Book close in — tomorrow beats next week

**Track it:**
```
Show-up rate = attended ÷ booked = ______%

Real cost per attended appointment = spend ÷ attended = ₹______
```

Under 50% show-up and your problem is confirmation discipline, not ads.

---

## Measurement contract

### Day 3
Delivery healthy? CTR ≥ ~0.8%? Conversations arriving? Are you replying within 5 minutes?

### Day 7
```
Conversations:                  ______
Bookings made:                  ______
Appointments attended:          ______
Customers closed:               ______
Spend:                         ₹______

Cost per conversation:         ₹______
Cost per booking:              ₹______
Cost per ATTENDED appointment: ₹______   ← the real number
Cost per customer:             ₹______
Floor = 7.143 × cost/booking:  ₹______ /day
```

| Result | Action |
|---|---|
| Cost per customer < affordable CAC | Working → [P12](P12-scaling-ladder.md) |
| Bookings fine, attendance poor | Fix the confirmation sequence. Consider a token deposit |
| Attendance fine, closing poor | In-person process problem, not an ads problem |
| Few bookings | Widen radius; make the appointment more concrete |
| Volatile costs | Learning-limited — raise toward floor |

---

## Vertical notes

| Vertical | Appointment offer | Watch out for |
|---|---|---|
| Dental / clinic | Free check-up or consultation | Health-claim policy. No before/after |
| Gym / fitness | Free trial session or day pass | Body-transformation imagery restricted |
| Salon / spa | Free consultation, or discounted first service | Discount-hunters who never return |
| Tuition / coaching | Free demo class | **Target parents, not students**, where parents decide |
| Real estate | Free site visit | ⚠️ Housing may be a Special Ad Category — check first |
| Auto | Free test drive | Confirm licence/eligibility in chat |
| Consultant / B2B | Free 30-min strategy call | Qualify hard, or you'll fill your calendar with tyre-kickers |

---

## Quick reference

```
Objective        Engagement → WhatsApp
Sell             the APPOINTMENT (cheap event), not the service
Budget           ₹200/day viable; floor = 7.143 × cost per booking
Location         realistic travel radius, 5-15 km
Pre-fill         asks for preferred time
Critical         confirmation sequence — ask for a reply
Real KPI         cost per ATTENDED appointment, not per booking
Deposit          even ₹100 transforms show-up rates
```

---

---

## Facebook vs Instagram for bookings

**Run both in one ad set.** Booking events are already scarce at low budget; splitting makes learning worse.

| | Facebook | Instagram |
|---|---|---|
| Audience skew | Older — better for clinics, dental, diagnostics, tuition | Younger — better for salon, spa, fitness, aesthetics |
| Booking channel | WhatsApp, Messenger, Instant Form | WhatsApp, **Instagram Direct** |
| Trust signals | Reviews, Page history, address | Visual portfolio, Reels, Highlights |
| Format that works | Static + clear offer, testimonial video | Reels showing the space/process |

**The channel decision:**

| Conversion location | When to use |
|---|---|
| **WhatsApp** ⭐ | Default. Follow-up, reminders and rescheduling all work, and you keep the contact |
| **Instagram Direct** | Your audience is young and Instagram-native and won't leave the app |
| **Instant Form** | You need structured details before contact ([P02](P02-instant-form-leads-200.md)) |

**WhatsApp is usually right in India** — the confirmation sequence in Step 4 depends on being able to message reliably before the appointment, and that's where no-shows are actually won.

**Instagram-specific caution:** Instagram Direct conversations are easy to start and easy to abandon. If you use it, your greeting message and reply speed matter even more than on WhatsApp.

**Vertical routing:** clinics, dental, diagnostics, tuition → lean Facebook. Salon, spa, fitness, aesthetics → lean Instagram, and make Reels of the actual space. Both still run in the one ad set; you're just choosing where the creative effort goes.

Full per-goal settings: [`../reference/facebook-vs-instagram.md`](../reference/facebook-vs-instagram.md)

---

**Related:** [`P00`](P00-BEST-low-budget-campaign.md) · [`P06`](P06-local-footfall.md) · [`P02`](P02-instant-form-leads-200.md) · [`../reference/facebook-vs-instagram.md`](../reference/facebook-vs-instagram.md)
