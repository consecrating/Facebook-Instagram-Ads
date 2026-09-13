# Troubleshooting

Find your symptom. Fix the cause, not the symptom.

---

## Nothing is delivering

| Symptom | Likely cause | Fix |
|---|---|---|
| Status "In review" | Normal — can take hours | Wait up to 24h |
| "Not delivering" | Payment failed | Billing → check method, clear balance |
| "Not delivering" | Account spending limit reached | Billing → raise or reset the limit |
| "Not delivering" | Schedule starts in the future | Check start date |
| "Rejected" | Policy | [`policy-and-special-categories.md`](policy-and-special-categories.md) |
| Ad set off | Toggled off, or campaign paused | Check toggles at all three levels |
| Delivery stopped suddenly | Payment failure or new policy flag | Billing, then Account Quality |
| Budget rejected as too low | Below your account's minimum for that event | Raise it — Ads Manager states the real minimum |

**First three checks, always:** Billing → Account Quality → toggles at campaign/ad set/ad level.

---

## Spending but no results

| Symptom | Cause | Fix |
|---|---|---|
| Impressions, no clicks | Creative isn't working | New hook. CTR under 0.5% = creative problem |
| Clicks, no conversions | Broken destination or tracking | Test the whole flow yourself, end to end |
| Zero events despite spend | Wrong event configured, or tracking broken | Events Manager → Test Events; verify WhatsApp number / form / pixel |
| Conversions in Ads Manager, none in your inbox | Tracking or dedup problem | Check `event_id` dedup; test lead delivery |
| Leads arriving but unreachable | Wrong numbers, or too slow | Measure contact rate; if under 50% it's a follow-up problem |

**Before blaming the ads, complete your own funnel as a customer.** Click your own ad, submit your own form, message your own WhatsApp. Most "ads don't work" problems are broken plumbing found in five minutes.

---

## Costs too high

Work through in this order — the order matters, because most people jump to targeting when creative is the problem.

### 1. Is it actually too high?
Compare against **your affordable CPA**, not against something you read. And judge on 7-day totals, not a bad day.

### 2. Is it still in learning?
Check Delivery. **Learning-phase costs run inflated and volatile.** If it says Learning, wait. If it says Learning Limited, that's the budget-floor problem, not a targeting problem → [`../data/budget-engine.md`](../data/budget-engine.md).

### 3. Is CTR the problem?
```
CTR (link) under 0.5%  →  creative problem. Fix that first.
CTR fine, cost high     →  offer or audience problem.
```

Creative is the highest-leverage fix and the one most people skip.

### 4. Is frequency high?
Above 3.0 means you're re-showing the same people. Refresh creative or widen the audience.

### 5. Is the audience too narrow?
Narrow audiences carry a CPM premium. Remove interest layers, widen age, widen radius.

### 6. Is the optimization event too expensive for the budget?
The most common structural error. If cost per event × 7.143 exceeds your budget, you're asking for something the budget can't support → drop a rung on the ladder.

---

## Learning phase problems

| Symptom | Meaning | Fix |
|---|---|---|
| Stuck in "Learning" | Under ~50 events in 7 days | Wait, or raise budget, or cheaper event |
| "Learning Limited" | Can't reach ~50/week | Raise to `7.143 × CPA`, drop a rung, or accept volatility |
| Learning reset unexpectedly | You made a significant edit | **Stop editing.** Budget, audience, optimization-event and creative changes can all reset it |
| Exited learning, then costs rose | Creative fatigue or audience saturation | Check frequency; refresh creative |

**The most expensive habit in low-budget advertising:** editing on day 3 because it "isn't working". Every significant edit restarts the 50-event clock. You can spend ₹6,000 across a month and never once let an ad set finish learning.

---

## Lead quality problems

| Symptom | Cause | Fix |
|---|---|---|
| Cheap leads, nobody answers | Too-low friction + slow follow-up | Add a qualifier; reply within 5 min → [P01 Variant A](../playbooks/P01-whatsapp-leads-200.md) |
| Everyone asks price then vanishes | Price not in the ad | Put the price/range in the creative |
| Wrong city / out of service area | Location too wide | Tighten radius; add "Serving [area] only" |
| Leads want something you don't sell | Creative is ambiguous | Be specific about what you actually offer |
| Good leads, no closes | Sales process, not ads | Fix the conversation → [P01 Variant C](../playbooks/P01-whatsapp-leads-200.md) |
| Accidental form submissions | "More volume" form type | Switch to Higher intent |

---

## WhatsApp problems

| Symptom | Fix |
|---|---|
| Number not in Ads Manager dropdown | Must be **WhatsApp Business** app; must be connected to the Page; you must be Page admin |
| Conversations counted but no messages arrive | Check the number is active; send yourself a test click |
| People click but don't message | Pre-filled message too vague or too committal — simplify |
| Chats start then die | Reply speed. Under 5 minutes → [P01 Variant C](../playbooks/P01-whatsapp-leads-200.md) |
| Can't message a lead after a day | The 24-hour window closed. Qualify and quote within 24h |

---

## Pixel / tracking problems

| Symptom | Fix |
|---|---|
| Pixel not firing | Pixel Helper extension; confirm base code on every page |
| Events fire in test but not live | Check the event is on the live page, not just a test route |
| Purchases double-counted | Pixel **and** CAPI both sending without matching `event_id` |
| Store orders ≠ Ads Manager | Attribution window + tracking loss. Trust your store |
| Dynamic ads show wrong products | `content_ids` mismatch between Pixel and catalog |
| "Low event match quality" | Send more parameters (email, phone, name) where you legitimately can |

---

## Account problems

| Symptom | Action |
|---|---|
| Ad account disabled | Account Quality → read reason → appeal. Don't create a new account to evade — that escalates it |
| Page restricted | Account Quality → appeal |
| Business Manager restricted | Complete business verification; appeal |
| Lost access | Another admin can restore. **This is why you add a second admin** |
| Suspected compromise | Change password, check active sessions, enable 2FA, review admins |

**Appeals genuinely work.** Automated enforcement makes mistakes often. Write a short, specific, polite appeal explaining what your business does and why the ad complies.

---

## The 5-minute diagnostic

When something's wrong and you don't know where to start:

```
1. Is it delivering?           → Delivery column
2. Is payment healthy?         → Billing
3. Any policy flags?           → Account Quality
4. Is it in learning?          → Delivery status
5. Is CTR above 0.8%?          → creative check
6. Does my funnel work?        → complete it yourself as a customer
7. Am I judging one day?       → switch to 7-day totals
8. Is my budget above floor?   → 7.143 × cost per result
```

Seven times out of ten the answer is #5 (creative), #6 (broken plumbing) or #7 (reacting to noise).

---

## When to stop and rethink

Sometimes the answer isn't a fix.

| Situation | Honest conclusion |
|---|---|
| 14 days, cost per result 3× affordable CPA | The **offer** is wrong, not the ads |
| Leads plentiful, closes zero | Product/market or pricing problem |
| Profitable but volume tiny | Working — you need more budget, not more optimization |
| Can't reply to the leads you get | Reduce budget until capacity catches up |
| Budget genuinely can't reach any floor | Concentrate spend into fewer days → [`../data/best-budget-recommender.md`](../data/best-budget-recommender.md) |

**More budget cannot fix a bad offer.** It just buys more evidence that the offer is bad, faster.

---

**Related:** [`metrics-dictionary.md`](metrics-dictionary.md) · [`../data/budget-engine.md`](../data/budget-engine.md) · [`policy-and-special-categories.md`](policy-and-special-categories.md)
