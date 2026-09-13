# P14 — Your First 30 Days

**Sequencing is where beginners lose money — not settings.** The right campaign run in the wrong order still fails.

This is a day-by-day calendar. Two tracks; pick one on Day 0.

---

## Pick your track

| | **Track A — Direct** | **Track B — Funnel** |
|---|---|---|
| Choose if | You can reach the computed floor (usually ~₹325+/day) | **₹200/day is a hard ceiling** |
| Week 1 | [P00](P00-BEST-low-budget-campaign.md) Click-to-WhatsApp | [P07](P07-video-retarget-funnel-200.md) Phase 1, video views |
| Exits learning | Yes, on conversations | Yes, on ThruPlays |
| Enquiries arrive | Week 1 | Week 2–3 |
| Month 2 cost | Flat | **Lower — the audience compounds** |

**Unsure?** Run the calculator. If your budget is below `7.143 × your event cost`, take Track B.

```bash
python3 tools/budget-calculator.py --interactive
```

> **One rule that overrides everything below: do not edit an ad set during its first 7 days.** Any significant edit resets the ~50-event learning clock. Most wasted low-budget spend traces back to a Day-3 panic edit.

---

# WEEK 0 — Setup (Days −3 to 0)

**Do not launch until this week is finished.** Every item is something that, if missing, wastes real money.

### Day −3
- [ ] Facebook Page complete: profile photo, cover, bio, contact, hours, address → [`../setup/01-page-and-business-manager.md`](../setup/01-page-and-business-manager.md)
- [ ] **Post 5–10 genuine things.** People check your Page before enquiring. An empty Page kills conversions you already paid for
- [ ] Instagram switched to a professional account, linked to the Page

### Day −2
- [ ] Business Manager created; Page + Instagram + ad account inside it
- [ ] **Ad account: currency INR, timezone Asia/Kolkata** — ⚠️ both permanent, verify twice
- [ ] 2FA on your personal login; a second admin added
- [ ] Payment method added → [`../setup/02-payments-india-gst.md`](../setup/02-payments-india-gst.md)
- [ ] **Prove the payment method with a real ₹100/day test for one day.** A method that merely *looks* added is not proven

### Day −1
- [ ] WhatsApp Business app installed on a business number → [`../setup/04-whatsapp-business.md`](../setup/04-whatsapp-business.md)
- [ ] Greeting message, away message, quick replies (`/price`, `/area`, `/book`), labels
- [ ] **Verified: your number appears in the Ads Manager WhatsApp dropdown**
- [ ] Creative ready: 1 video (30–60s, 9:16, **captions on**) + 2 statics (4:5 **and** 9:16)
- [ ] Copy written, with the **price or range in the ad**

### Day 0 — the gate
- [ ] **Know your numbers:** revenue per customer, margin, close rate
- [ ] **Computed your budget:** `7.143 × expected event cost`. Write the estimate down so Day 7 is a measurement, not a vibe
- [ ] Special Ad Category checked — credit / employment / housing / political? → [`../reference/policy-and-special-categories.md`](../reference/policy-and-special-categories.md)
- [ ] **Reply capacity confirmed:** who answers enquiries, within 5 minutes, during which hours
- [ ] Ad schedule matches hours you can actually cover

```
Write it down, today:
  Event I'm optimizing for : ________________
  My assumed cost per event: ₹______
  Budget I'm setting       : ₹______/day
  Affordable cost per lead : ₹______
```

---

# WEEK 1 — Launch and leave it alone (Days 1–7)

### Day 1
**Launch.** Then close Ads Manager.

- Track A → build [P00](P00-BEST-low-budget-campaign.md): 1 campaign, 1 ad set, 3 ads
- Track B → build [P07](P07-video-retarget-funnel-200.md) **Phase 1 only** at ₹120/day

**Both tracks, do this on Day 1:** create your retargeting audiences now so they start filling — they take 24–48 hours to populate.
- `Video 50% - 365d` (from your video)
- `Page + IG engagers - 365d`

Ads may sit **In Review** for a few hours. Delivery will be erratic. That's the learning phase, not a fault.

### Day 2
**Do nothing.** Check that it's delivering. That's all.

### Day 3 — breakage check only

| Check | Healthy | If not |
|---|---|---|
| Delivery status | Active | Billing → Account Quality → toggles |
| Impressions | Accumulating | Budget may be under account minimum |
| CTR (link) | ≥ ~0.8% | **Creative problem** — swap the weakest ad only |
| Events arriving | Some | Verify WhatsApp number / form / pixel |
| Reply time | Under 5 min | Fix this before anything else |

> **Change nothing except a clearly failing creative.** Not budget. Not targeting. Not the optimization event.

### Days 4–6
**Reply to every enquiry within 5 minutes.** That's the job this week.

Log outcomes: Contacted / Not reachable / Quoted / Won / Lost. You'll need the close rate on Day 7.

### Day 7 — the first real measurement

```
Spend                  ₹______
Impressions             ______
Link clicks             ______
Your events             ______
Enquiries answered      ______
Customers closed        ______

CPM              = spend ÷ impressions × 1000  = ₹______
CTR (link)       = clicks ÷ impressions        = ______%
Cost per event   = spend ÷ events              = ₹______   ← the number
TRUE floor       = 7.143 × cost per event      = ₹______/day
Close rate       = customers ÷ enquiries       = ______%
Cost per customer= spend ÷ customers           = ₹______
```

Now compare against Day 0. **Your estimate was probably wrong — that's expected and it's the whole point.** Priors choose a strategy; your account sets the budget.

---

# WEEK 2 — The first real decision (Days 8–14)

### Day 8 — decide

| Your situation | Action |
|---|---|
| Cost per event ≤ affordable CPL **and** budget ≥ true floor | Working and stable → hold, then scale from Day 15 |
| Cost per event ≤ affordable CPL **but** budget < true floor | **Profitable but learning-limited.** Raise to the true floor, or concentrate into fewer days |
| Cost per event > affordable CPL | **Offer problem, not budget problem.** Rework the offer/price. More budget accelerates the loss |
| Barely any events | Drop a rung → Track B ([P07](P07-video-retarget-funnel-200.md)) |
| Enquiries fine, nobody answering your calls | Contact-rate problem → [P01 Variant A](P01-whatsapp-leads-200.md) |

**Track B specifically:** check your `Video 50% - 365d` audience size.
- **1,000+** → launch [P07](P07-video-retarget-funnel-200.md) **Phase 2** at ₹80/day
- **Under 1,000** → keep Phase 1 running another week. Consider putting the full ₹200 into Phase 1 to build faster

> If you raised the budget on Day 8, **you just reset learning.** Accept one more unstable week — that's the price of exiting learning permanently. No edits until Day 15.

### Days 9–13
Reply fast. Log outcomes. **Don't touch the ad set.**

Optional and useful: start [P08](P08-engagement-social-proof.md) at ₹100/day on a separate campaign to build social proof and grow your engager audience. It doesn't disturb your main ad set.

### Day 14 — second measurement
Same calculation as Day 7. You're looking for a **trend**, not a snapshot.

```
Week 1 cost per event   ₹______
Week 2 cost per event   ₹______
Direction               falling / flat / rising
Frequency (7-day)       ______
```

- **Falling** → learning is working. Good
- **Flat** → stable. Fine
- **Rising** → creative fatigue or saturation. Check frequency

---

# WEEK 3 — Creative, not settings (Days 15–21)

By now the settings are right or they aren't. **This week is about creative**, which is the highest-leverage thing you control.

### Day 15
**Frequency check** (7-day window):

| Frequency | Meaning | Action |
|---|---|---|
| Under 2.0 | Healthy | Continue |
| 2.0–3.0 | Watch it | Prepare new creative |
| Above 3.0 | Burning the same people | **Add creative now**, or widen audience |

### Days 16–18 — rotate one creative
Replace your **weakest** ad with a new **angle** — not a new colour. Keep the winner. Never replace all three; you lose your baseline.

Angles: problem · price · speed · proof · objection · story → [P01 Variant D](P01-whatsapp-leads-200.md) and [`../reference/copy-templates-india.md`](../reference/copy-templates-india.md)

### Days 19–21 — lead quality
Volume is one thing; quality is another.

| Symptom | Fix |
|---|---|
| Everyone asks price then vanishes | **Put the price in the ad** |
| Wrong area | Tighten radius; add "Serving [area] only" |
| Not serious | Add a qualifying question in your first reply |
| Good leads, no closes | Sales conversation → [P01 Variant C](P01-whatsapp-leads-200.md) |

---

# WEEK 4 — Scale or fix (Days 22–30)

### Day 22 — the scaling gate

**All four must be true before you scale:**
- [ ] Exited learning, or 14 days of data if deliberately learning-limited
- [ ] Cost per result ≤ affordable CPA
- [ ] **You've closed real customers** — not just collected enquiries
- [ ] **You can handle 2× the volume**

> The fourth is the one people skip. Doubling enquiries when you already reply late just doubles your waste. **Capacity is part of the campaign.**

### Days 23–30 — if scaling
**+20%, wait 4 days, verify, repeat.** Bigger jumps are significant edits that reset learning.

```
Day 22   ₹______/day   (baseline)
Day 26   ₹______  (+20%)   cost per result ₹______  frequency ______
Day 30   ₹______  (+20%)   cost per result ₹______  frequency ______
```

If cost per result rises materially, **hold** — don't raise again. Full rules: [P12](P12-scaling-ladder.md)

### Days 23–30 — if not working

Diagnose in this order. Most people jump to targeting when creative is the problem.

```
1. CTR under 0.8%?          → creative problem. Fix that first
2. Clicks but no events?     → destination/tracking broken. Test it yourself
3. Events but no customers?  → offer or sales-process problem
4. Costs volatile?           → learning-limited. Raise to floor or drop a rung
5. Everything fine, tiny volume? → it's working. You need budget, not fixes
```

→ [`../reference/troubleshooting.md`](../reference/troubleshooting.md)

### Day 30 — the month-1 review

```
MONTH 1
  Total ad spend                     ₹______
  GST at ~18%                        ₹______   ← don't forget this
  Total outflow                      ₹______
  Events delivered                    ______
  Cost per event                     ₹______
  Customers closed                    ______
  Cost per customer                  ₹______
  Revenue generated                  ₹______
  Gross profit (revenue × margin)    ₹______
  Contribution (profit − ad spend)   ₹______

  Profitable?                        yes / no
  True floor = 7.143 × cost/event    ₹______/day
  Month-2 budget decision            ₹______/day
```

**Contribution is the only line that matters.** Leads are an intermediate metric; enquiries don't pay bills.

---

## The 30-day sequencing rules

1. **Week 0 is not optional.** Launching without a proven payment method or a reply plan wastes week 1
2. **Never edit during the first 7 days of any ad set.** Every significant edit restarts the 50-event clock
3. **Judge on 7-day totals.** At ₹200/day a single day is statistical noise
4. **Create retargeting audiences on Day 1**, even if you won't use them for weeks. They need time to fill
5. **Fix creative before targeting.** Creative is the bigger lever and the cheaper experiment
6. **Reply within 5 minutes.** This outperforms every setting in Ads Manager
7. **Recompute the floor every time your CPA changes.** The formula is fixed; the input is measured
8. **Don't scale past your capacity to serve**

---

## What month 2 looks like

| Track A | Track B |
|---|---|
| Scale [P00](P00-BEST-low-budget-campaign.md) via [P12](P12-scaling-ladder.md) | Phase 2 now has a real audience — costs drop |
| Add [P07](P07-video-retarget-funnel-200.md) for cheaper retargeting | Shift budget toward Phase 2 |
| Add [P08](P08-engagement-social-proof.md) if credibility is thin | Add [P00](P00-BEST-low-budget-campaign.md) once you can reach its floor |
| Consider [P13](P13-facebook-page-likes-followers.md) / [P04](P04-instagram-followers.md) **only** if you monetise an audience | Same |

**The compounding is real on Track B.** A cold lead campaign costs the same in month six as month one. A funnel gets cheaper, because the warm audience keeps growing.

---

**See it done:** [`../examples/worked-example-end-to-end.md`](../examples/worked-example-end-to-end.md) — a full 30-day run with real arithmetic

**Related:** [`P00`](P00-BEST-low-budget-campaign.md) · [`P07`](P07-video-retarget-funnel-200.md) · [`P12`](P12-scaling-ladder.md) · [`../setup/00-preflight.md`](../setup/00-preflight.md) · [`../data/best-budget-recommender.md`](../data/best-budget-recommender.md)
