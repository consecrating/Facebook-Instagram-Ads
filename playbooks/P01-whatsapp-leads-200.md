# P01 — Click-to-WhatsApp: Advanced Variants

**[P00](P00-BEST-low-budget-campaign.md) is the build. This is the tuning.** Read P00 first and launch it. Come back here when you have 7 days of data and want to improve a specific outcome.

---

## Which variant do you need?

| Your problem after 7 days | Variant |
|---|---|
| Enough enquiries, but they're unqualified | [A — Qualification-first](#variant-a) |
| Too few enquiries | [B — Volume-first](#variant-b) |
| Enquiries don't reply after the first message | [C — Conversation design](#variant-c) |
| Costs are fine but plateaued | [D — Creative rotation](#variant-d) |
| Want cheaper leads than cold traffic gives | [E — Warm-audience CTWA](#variant-e) |
| Selling something expensive | [F — High-ticket](#variant-f) |

---

## Variant A — Qualification-first

**Use when:** volume is fine, quality is poor. People ask the price and vanish.

Changes to P00:

1. **Put the price in the ad, prominently.** Not "affordable rates" — an actual number. `Starting ₹2,500` or `₹15,000–40,000 range`
2. **Add a disqualifier line.** Counter-intuitive but effective:
   ```
   Serving [AREA] only · Minimum order ₹[X] · Not for [WRONG FIT]
   ```
3. **Change the pre-filled message to require a choice:**
   ```
   Hi! I need [SERVICE]. My budget is around ₹______ and I need it by ______.
   ```
4. **First WhatsApp reply asks one qualifying question**, before quoting:
   ```
   Thanks for reaching out! Quick question so I can give you an accurate price:
   what's your approximate budget range?
   ```

**Expect:** 30–50% fewer enquiries, materially higher close rate. Cost per *enquiry* rises; cost per *customer* usually falls. Judge on the second number.

---

## Variant B — Volume-first

**Use when:** too few enquiries to learn anything.

In order of what to try first:

1. **Widen location.** 15 km → 30 km. Biggest single lever, lowest risk
2. **Widen age.** Remove the bounds you can't justify with evidence
3. **Remove the price from the ad** (accepting lower quality) — reverses Variant A
4. **Soften the pre-fill** to the lowest-friction version:
   ```
   Hi! Please share details about [SERVICE].
   ```
5. **Add a fourth creative** with a distinctly different angle
6. **Raise budget** toward the computed floor — `7.143 × your measured cost per conversation`

**Do not** add more ad sets. Widening one ad set is right; splitting into several at low budget is wrong.

---

## Variant C — Conversation design

**Use when:** conversations start and die. This is usually the real problem, and it isn't an ads problem.

The ad's job ends at the first message. Everything after is yours.

**The 4-message frame:**

```
1. ACKNOWLEDGE (instant, automated greeting)
   "Hi! Thanks for messaging [BUSINESS]. Checking this now —
    which area are you in?"

2. QUALIFY (one question, not five)
   "Got it. And roughly what budget are you working with?"

3. VALUE BEFORE PRICE
   "For [their need] we'd do [specific approach]. That includes
    [X] and [Y]. Most customers in your situation spend ₹[range]."

4. SINGLE CLEAR NEXT STEP
   "Shall I book you in for [specific slot]?"
```

**Rules:**
- One question per message. Multi-question messages get one-word answers
- Never open with a price list. Qualify first, then price
- **Reply within 5 minutes.** This matters more than every setting in Ads Manager
- Voice notes work unusually well in India for explaining something complex
- Follow up **inside 24 hours** — after that the free messaging window closes and re-engagement needs approved templates

**Follow-up sequence for non-responders** (all within 24h):
```
+2h:  "Just checking you got my message about [SERVICE]?"
+8h:  "Happy to answer any questions — no obligation."
+20h: "Closing this enquiry, but message anytime. Here's our
       price list for reference: [attach]"
```

---

## Variant D — Creative rotation

**Use when:** costs were good, now drifting up. Check **frequency** — above ~3.0 on a 7-day window means you're re-showing the same people.

**Rotate the hook, not the offer.** Six angles for the same service:

| Angle | Opening line pattern |
|---|---|
| Problem | "AC not cooling even after service?" |
| Price | "AC service from ₹499 in [City]" |
| Speed | "AC repaired today. Same-day slots." |
| Proof | "1,200+ ACs serviced in [City] this year" |
| Objection | "No hidden charges. Price confirmed before we start." |
| Story | "A customer called us after paying twice elsewhere…" |

**Method:** keep the winner, replace the weakest ad with a new angle. Never replace all three at once — you lose your baseline and can't tell what changed.

Refresh roughly every 2–3 weeks at low budget, or whenever frequency exceeds 3.

---

## Variant E — Warm-audience CTWA

**Use when:** cold CTWA works but you want cheaper.

Build these audiences (**Audiences → Create audience → Custom audience**):

| Audience | Source | Retention |
|---|---|---|
| `Video 50%` | Video views | 365 days |
| `Page + IG engagers` | Page / Instagram | 365 days |
| `Website visitors` | Pixel (if you have one) | 180 days |

Then either:
- **Separate warm ad set at ₹80–100/day**, Advantage+ Audience **OFF**, custom audiences only — *only if* total budget is ₹400+/day. Below that you're splitting too thin
- **Or** just run [P07](P07-video-retarget-funnel-200.md), which is this idea built properly from the start

Warm audiences typically convert several times better than cold. That's the whole reason P07 exists.

---

## Variant F — High-ticket

**Use when:** one sale is worth ₹50,000+.

The economics invert. You can afford expensive leads — but the learning-phase floor gets expensive too (`7.143 × CPA`), so plan for a real budget.

Changes:
1. **Optimize for conversations**, but treat the *conversation* as a qualification gate, not a lead
2. **Lead with authority, not price.** Credentials, track record, case studies
3. **Video is close to mandatory.** Trust doesn't transfer through a static image at this price point
4. **Expect a longer cycle.** Attribution windows will understate you — someone enquiring today may buy in six weeks. Track manually
5. **Two-step is usually better:** [P07](P07-video-retarget-funnel-200.md) to build trust, then CTWA to the warm audience
6. **Never chase cheap leads here.** A ₹500 conversation that closes ₹1,00,000 is excellent

---

## Diagnostic table

| Symptom | Most likely cause | Fix |
|---|---|---|
| High CPM, low CTR | Creative | New hook (Variant D) |
| Good CTR, few conversations | CTA or pre-fill friction | Simplify pre-fill (Variant B) |
| Conversations start, die instantly | Reply speed | Fix response time (Variant C) |
| Many enquiries, no sales | Wrong audience or wrong offer | Add qualifiers (Variant A) |
| Costs rising over time | Creative fatigue | Rotate (Variant D) |
| Volatile daily costs | Learning-limited | Raise to `7.143 × CPA`, or accept it |
| Sudden delivery stop | Payment or policy | Check Billing + Account Quality |

---

**Back to:** [`P00`](P00-BEST-low-budget-campaign.md) · **Related:** [`P07`](P07-video-retarget-funnel-200.md) · [`P12`](P12-scaling-ladder.md) · [`../reference/troubleshooting.md`](../reference/troubleshooting.md)
