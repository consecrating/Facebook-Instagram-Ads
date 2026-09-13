# Playbooks — Choose Your Campaign

Every playbook is a step-by-step build: exact objective, exact settings, exact clicks, plus a budget check and a Day 3 / Day 7 measurement contract.

---

## Fast chooser

**Answer one question: what should happen after someone sees your ad?**

| They should… | Playbook | Works at ₹200/day? |
|---|---|---|
| Message me on WhatsApp | **[P00 ⭐](P00-BEST-low-budget-campaign.md)** | Yes (learning-limited) |
| Message me — advanced variants | [P01](P01-whatsapp-leads-200.md) | Yes (learning-limited) |
| Fill a form (I have no website) | [P02](P02-instant-form-leads-200.md) | Yes (learning-limited) |
| Enquire on my website | [P03](P03-website-leads.md) | ❌ needs ~₹1,800/day |
| Follow my Instagram | [P04](P04-instagram-followers.md) | Yes |
| Buy from my online store | [P05](P05-ecommerce-sales.md) | ❌ needs ~₹3,000+/day |
| Visit my shop/clinic | [P06](P06-local-footfall.md) | Yes |
| Nothing yet — I have almost no budget | **[P07 ⭐](P07-video-retarget-funnel-200.md)** | **Yes — actually exits learning** |
| Engage, so my page looks credible | [P08](P08-engagement-social-proof.md) | Yes |
| Book an appointment | [P09](P09-appointment-booking.md) | Yes (learning-limited) |
| Install my app | [P10](P10-app-installs.md) | ❌ needs high budget |
| Come back and finish buying | [P11](P11-catalog-retargeting.md) | Partly |
| I'm profitable and want more | [P12](P12-scaling-ladder.md) | — |

---

## If you're unsure, read this

**Two playbooks cover the majority of Indian low-budget cases:**

- **[P00 — Click-to-WhatsApp](P00-BEST-low-budget-campaign.md)** — the default best choice. Most Indian businesses sell through conversation, and WhatsApp removes all friction. Start here unless you have a specific reason not to.
- **[P07 — Video → Retargeting Funnel](P07-video-retarget-funnel-200.md)** — the honest answer when ₹200/day is a hard ceiling. It's the only structure in this repo that *actually exits the learning phase* at ₹200/day, because it optimizes for cheap video views instead of expensive leads.

**Choose P00 if** you can stretch to ~₹325/day and can reply to chats quickly.
**Choose P07 if** ₹200/day is fixed, or you're brand new with no audience and no social proof.

---

## The budget reality table

Computed from the learning-phase floor: `daily budget ≥ 7.143 × cost per optimization event`. See [`../data/budget-engine.md`](../data/budget-engine.md).

| Playbook | Optimization event | Rough floor to exit learning |
|---|---|---|
| P07 | ThruPlay / video view | **~₹30–100/day** ✅ |
| P04, P08 | Engagement / profile visit | ~₹50–200/day ✅ |
| P06 | Landing page view / message | ~₹100–400/day ✅ |
| P00, P01 | WhatsApp conversation | ~₹200–500/day ⚠️ |
| P02, P09 | Instant Form lead | ~₹300–700/day ⚠️ |
| P03 | Website lead (CAPI) | ~₹1,000–2,500/day ❌ |
| P05, P11 | Purchase | ~₹3,000–8,000/day ❌ |

> These are order-of-magnitude figures derived from wide priors — not predictions. Replace with your own measured cost on Day 7. See [`../data/benchmarks-india.md`](../data/benchmarks-india.md) for why no honest table can be more precise than this.

**Reading the table:** ❌ doesn't mean "impossible", it means "will not exit the learning phase, so expect volatile and inflated costs". You can still run it — you just shouldn't expect it to stabilise.

---

## Rules that apply to every playbook

These come up in every single build. They're collected here so each playbook doesn't have to repeat them.

1. **One campaign → one ad set → three ads.** Under ₹1,000/day, never split into multiple ad sets. Splitting is the most common and most expensive low-budget mistake.
2. **Advantage+ Audience ON, suggestion fields empty.** Interest stacking at low budget starves the algorithm. Targeting inputs are treated as signals anyway, not hard boundaries.
3. **Advantage+ placements ON.** More placements = more auctions = cheaper results.
4. **Highest volume bidding.** No cost caps at low budget — they throttle delivery to nothing. (Also: a cost-per-result goal requires daily budget ≥ 5× the target cost.)
5. **CBO / Advantage campaign budget OFF.** With one ad set there's nothing to optimize across.
6. **No edits for 7 days.** Significant edits reset the ~50-event learning clock. Changing budget on Day 3 because "it's not working" is how ₹6,000 disappears with nothing learned.
7. **Judge on 7-day totals.** At ₹200/day a single day is statistical noise.
8. **Creative beats targeting.** When results are poor, change the creative and the offer before you touch the audience.
9. **Compute the budget, never guess it.** `7.143 × your event cost`. Every playbook has this step.
10. **Reply within 5 minutes.** Indian buyers contact several businesses at once. This single habit outperforms every optimization in Ads Manager.

---

## Naming convention

Use one consistently or you'll lose track by month two:

```
Campaign:  OBJECTIVE | Offer | Month        →  CTWA | AC Repair | Sep26
Ad set:    Audience | Location | Age        →  Broad | Jaipur 15km | 25-55
Ad:        Format | Angle | Version         →  Video | Price-led | v1
```

---

## Suggested progression

Most people should not start with their end goal.

```
No audience, no social proof, ₹200/day
        ↓
   P07 (video views — builds a warm audience cheaply)
        ↓
   P08 (engagement — makes the page look credible)
        ↓
   P00 (WhatsApp leads — now retargeting a warm audience, so cheaper)
        ↓
   P12 (scale what works)
```

Trying to run P05 (purchases) on day one with ₹200/day and no audience is the single most common way to conclude "Facebook ads don't work".

---

**Start:** [`P00 ⭐`](P00-BEST-low-budget-campaign.md) · [`P07 ⭐`](P07-video-retarget-funnel-200.md) · budget maths in [`../data/best-budget-recommender.md`](../data/best-budget-recommender.md)
