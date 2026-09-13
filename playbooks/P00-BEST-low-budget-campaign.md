# P00 — The Best Low-Budget Campaign for India ⭐

**Start here if you have a small budget and want the highest chance of results.**

This is the single campaign I'd run for almost any Indian business spending ₹200–₹700/day. It's **Click-to-WhatsApp (CTWA)** with a deliberately minimal structure.

- Works at **₹200/day**
- Recommended at **₹325/day** (computed, see below)
- No website needed
- No Meta Pixel needed
- No landing page needed
- Every lead becomes a WhatsApp contact you keep

---

## Why this one wins in India

| Reason | Why it matters at low budget |
|---|---|
| WhatsApp is where Indians already are | Zero new-app friction. No "loading…" drop-off |
| No website or landing page required | Removes the biggest cost and the biggest leak |
| A chat is warmer than a form | Form leads go cold; a chat is a live conversation |
| Reported **30–50% lower CPL** than standard lead-gen ads | At ₹200/day, a 40% cost saving is the difference between working and not |
| You keep the contact | Follow up later. One ₹45 conversation can be worked for months |
| Nothing to break | No Pixel, no CAPI, no tracking debugging |

At small budgets, **removing friction beats clever targeting.** This campaign removes almost all of it.

> **Not for you if:** you sell purely online with instant checkout and no human conversation (→ [P05](P05-ecommerce-sales.md)), you're a creator chasing followers (→ [P04](P04-instagram-followers.md)), or you have zero WhatsApp presence and won't reply to chats. **If nobody answers the WhatsApp, this campaign wastes 100% of your money.**

---

## Before you start

- [ ] Facebook Page (published, with profile photo + cover)
- [ ] Instagram account, ideally linked to the Page
- [ ] **WhatsApp Business app** installed, with a business number — see [`../setup/04-whatsapp-business.md`](../setup/04-whatsapp-business.md)
- [ ] Payment method added and working — see [`../setup/02-payments-india-gst.md`](../setup/02-payments-india-gst.md)
- [ ] **You (or someone) can reply to WhatsApp within 5 minutes during business hours**

That last one isn't optional. Indian buyers enquire with 3–4 businesses at once. Reply speed is the whole game — a ₹45 lead answered in 2 minutes is worth more than three ₹45 leads answered tomorrow.

---

## Step 1 — Compute your budget first

Don't skip this. Two minutes here decides whether the campaign can work at all.

```
Your numbers:
  Revenue per closed customer    V = ₹ ______
  Gross margin                   M = ______%
  Lead → customer close rate     C = ______%

  Affordable cost per lead  = V × M × 0.30 × C   = ₹ ______
```

Then the budget:

```
  Recommended daily budget  = 7.143 × (cost per WhatsApp conversation)
```

Because Meta needs ~50 optimization events per ad set per 7 days to exit the learning phase (50 ÷ 7 = 7.14 events/day).

**If a WhatsApp conversation costs you ~₹45, your recommended budget is ₹322/day — round to ₹325.**

| Your budget | What actually happens |
|---|---|
| ₹200/day | Runs, but stays **Learning Limited** for the conversation event. Volatile costs. Use the mitigations in Step 5 |
| **₹325/day** | **Recommended.** Exits learning on conversations. Costs stabilise in 7–10 days |
| ₹650/day | Optimal. Exits learning fast, and you can test creatives in parallel |

Full reasoning: [`../data/best-budget-recommender.md`](../data/best-budget-recommender.md)

> If ₹200/day is your hard ceiling, consider **₹1,400/day for 4 days** instead of ₹200/day for 30. Same ₹5,600, but one of them actually exits learning. See the concentration section in the recommender.

---

## Step 2 — Create the campaign

In **Meta Ads Manager** → **Campaigns** → **+ Create**

1. **Buying type:** Auction
2. **Objective:** **Engagement**
   > Not "Leads". Under ODAX, WhatsApp conversations live under Engagement. Choosing Leads pushes you toward Instant Forms instead.
3. **Continue** → choose **Manual** setup if offered
4. **Campaign name:** `CTWA | WhatsApp | Sep26`
5. **Special Ad Category:** leave **blank** unless you advertise credit, employment, housing, or social/political issues — see [`../reference/policy-and-special-categories.md`](../reference/policy-and-special-categories.md). Declaring it when required is mandatory; declaring it when not required cripples your targeting.
6. **Campaign Budget Optimization (Advantage campaign budget):** **OFF**
   > At low budget you want one ad set with one budget. CBO splits money across ad sets and at ₹200–325/day there's nothing to split.
7. **Next**

---

## Step 3 — The ad set (this is where it's won or lost)

1. **Ad set name:** `Broad | WhatsApp | 18-55 | All India`
2. **Conversion location:** **WhatsApp**
   - Select your connected WhatsApp Business number
   - If it isn't listed → [`../setup/04-whatsapp-business.md`](../setup/04-whatsapp-business.md)
3. **Performance goal:** **Maximise number of conversations**
   > Not link clicks. Clicks are cheap and worthless here; you're paying for conversations.
4. **Budget:** **Daily**, set your Step 1 number (e.g. `325`)
5. **Schedule:** start tomorrow 00:00, no end date
6. **Bid strategy:** **Highest volume** (default)
   > Do **not** use a cost cap. At this budget a cost cap will throttle delivery to nothing. Also: a Cost-Per-Result goal requires daily budget ≥ 5× the target cost — at ₹325/day your cap couldn't exceed ₹65 anyway.

### Audience — keep it broad, and mean it

7. **Location:** your actual service area
   - Local business → city + radius (start **10–25 km**)
   - Serve all India → select India, exclude nothing
   - Multiple cities → list them; don't make one ad set per city
8. **Age:** the widest range that's genuinely plausible, e.g. `25–55`
   > Every year you cut shrinks Meta's optimization space. Cut only what's truly irrelevant.
9. **Gender:** All, unless your product is genuinely gender-specific
10. **Advantage+ Audience:** **ON** — leave the suggestion fields **empty**
    > Counter-intuitive but correct at low budget. Interest stacking at ₹325/day starves the algorithm. Advantage+ treats inputs as *signals* anyway, not boundaries — so a narrow list mostly just slows learning. Let the creative do the targeting.
11. **Languages:** leave blank, unless you're specifically running Hindi/Tamil/Telugu/Marathi/Bengali creative — see [`../reference/targeting-india.md`](../reference/targeting-india.md)
12. **Placements:** **Advantage+ placements (automatic)** — ON
    > More placements = more auctions = cheaper conversations. Manual placement selection at low budget is self-harm.
13. **Next**

---

## Step 4 — The ads: exactly three

Create **3 ads in this one ad set**. Not one. Not eight.

Three lets Meta find a winner without splitting your budget across ad sets. Eight ads at ₹325/day gives each one ~₹40/day — none of them learn anything.

### Ad structure

- **Ad 1 — Static image + offer.** Clearest, most direct version
- **Ad 2 — Short video, 15–30s.** Usually the cheapest CPM. Phone-shot is fine and often outperforms polished
- **Ad 3 — Carousel or a second static angle.** Different hook, e.g. problem-first instead of offer-first

For each ad:
1. **Identity:** your Facebook Page + Instagram account
2. **Format:** as above
3. **Media:** **4:5 or 1:1** for feed, **9:16** for Reels/Stories. Full specs: [`../reference/creative-specs.md`](../reference/creative-specs.md)
4. **Primary text:** hook in the **first line** — everything after is hidden behind "…more"
5. **Call to action:** **Send Message** or **Send WhatsApp Message**
6. **Message template:** pre-fill the opening message. This matters more than people expect

### Pre-filled message — use this pattern

```
Hi! I'm interested in [SPECIFIC SERVICE]. Please share details and pricing.
```

Pre-filling does two jobs: it removes the "what do I even type" hesitation, and it self-qualifies — someone who sends it has stated intent. Ready-to-use ₹-priced copy: [`../reference/copy-templates-india.md`](../reference/copy-templates-india.md)

### Copy rules that matter in India

- **Put the price or price range in the ad.** Counter-intuitive, but it filters out the "kitna hai?" tyre-kickers who eat your reply time. Fewer, better conversations at the same spend
- Name the city — "in Jaipur" outperforms "near you"
- One clear action. Not "call, WhatsApp, DM or visit"
- No fake urgency. Indian buyers are sceptical and it costs you trust
- Avoid before/after claims in health/fitness/beauty — policy risk, see [`../reference/policy-and-special-categories.md`](../reference/policy-and-special-categories.md)

**Publish.**

---

## Step 5 — If you're at ₹200/day: mitigations

At ₹200/day you'll be Learning Limited on the conversation event (you'd need CPA ≤ ₹28). That's survivable if you follow all six:

1. **One ad set. Only one.** Splitting is the single most common low-budget mistake
2. **Broad targeting, no interest layers.** Maximum delivery options
3. **Exactly 3 ads.** Enough to find a winner, not enough to fragment
4. **Advantage+ placements ON.** Every extra placement is another cheap auction
5. **Do not edit for 7 full days.** Any significant edit resets the 50-event clock. Changing budget on Day 3 because "it's not working" is how people spend ₹6,000 and learn nothing
6. **Judge on 7-day totals, not daily.** At ₹200/day, one day is statistical noise

---

## Step 6 — The measurement contract

### Day 1–2: don't touch anything
Ads may sit **In Review** for a few hours. Delivery is erratic at first — that's the learning phase, not a fault.

### Day 3: check for breakage only

| Check | Healthy | If not |
|---|---|---|
| Delivery status | Active | Read the Delivery column; check payment + review status |
| Impressions | Accumulating | Budget may be under your account minimum — Ads Manager will say |
| CTR (link) | Roughly ≥ 0.8% | **Creative problem.** Swap the weakest ad. Don't touch targeting |
| Conversations | At least a few | Check the WhatsApp number is reachable and the CTA is right |

**Do not change budget or targeting on Day 3 unless delivery is actually broken.**

### Day 7: the real read

```
Actual cost per conversation = spend ÷ conversations = ₹ ______

Your true recommended budget = 7.143 × that number = ₹ ______
```

Now decide:

| Result | Meaning | Action |
|---|---|---|
| Cost ≤ affordable CPL | Working | Move to [P12 scaling](P12-scaling-ladder.md) |
| Cost slightly above | Close | Improve creative + offer before adding budget |
| Cost far above | Offer problem, not budget problem | Rework the offer. More money will not fix it |
| Barely any conversations | Below useful signal | Drop to [P07](P07-video-retarget-funnel-200.md) and build a warm audience first |

### Day 14+
Recompute. Refresh creative when CTR decays or frequency climbs. Then scale via P12.

---

## The lead-quality lever

Cheap leads that never reply are worse than no leads.

If volume is fine but quality is poor:
- **Put the price in the ad** — the strongest filter available
- Add a qualifying line: *"Serving Jaipur only"* / *"Minimum order ₹5,000"*
- Ask one qualifying question as your first WhatsApp reply
- Reply within 5 minutes. Quality is often just a speed problem wearing a disguise

If quality is fine but volume is low:
- Widen location radius before touching anything else
- Add a fourth creative angle
- Raise budget toward the computed T2

---

## Quick reference card

```
Objective            Engagement
Conversion location  WhatsApp
Performance goal     Maximise conversations
Structure            1 campaign → 1 ad set → 3 ads
Budget               Daily, = 7.143 × cost per conversation
Bid strategy         Highest volume (no cost cap)
Advantage+ audience  ON, suggestion fields empty
Advantage+ placement ON
CBO                  OFF
Edits                NONE for 7 days
Judge on             7-day totals
```

---

**Related:** [`P01`](P01-whatsapp-leads-200.md) deeper CTWA variants · [`P07`](P07-video-retarget-funnel-200.md) the ₹200/day funnel that *does* exit learning · [`P12`](P12-scaling-ladder.md) scaling · [`../data/best-budget-recommender.md`](../data/best-budget-recommender.md) the budget maths
