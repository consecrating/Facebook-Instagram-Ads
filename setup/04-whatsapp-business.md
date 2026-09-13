# 04 — WhatsApp Business Setup

Required for [P00](../playbooks/P00-BEST-low-budget-campaign.md) and [P01](../playbooks/P01-whatsapp-leads-200.md) — the best-performing low-budget campaigns for India.

---

## Choose your WhatsApp path

| | **WhatsApp Business app** | **WhatsApp Business Platform (API)** |
|---|---|---|
| Cost | Free | Paid, via a provider |
| Setup | Minutes | Days, needs a provider |
| Automation | Basic (greeting, away, quick replies) | Full chatbots, CRM, routing |
| Multiple agents | Very limited | Yes |
| Conversion signals back to Meta | Limited | Richer — improves optimization |
| Good for | Starting out, ₹200–1,000/day | Scale, teams, high volume |

**Start with the free Business app.** It's genuinely sufficient at low budget. Move to the API only when reply volume exceeds what a person can handle, or when you need proper CRM integration.

---

## Setup — WhatsApp Business app

### 1. Use a separate number
Ideally a number not already on personal WhatsApp. A cheap second SIM is a sound investment — it keeps business enquiries out of your personal chats and lets someone else handle replies later.

If you must convert an existing personal WhatsApp, back up chats first; the number can only be on one WhatsApp at a time.

### 2. Install and register
Install **WhatsApp Business** (Play Store / App Store) → register the number → verify by OTP.

### 3. Complete the business profile
Settings → Business tools → Business profile. Fill in **all** of it:
- Business name (match your Facebook Page name)
- Category
- Description — what you do, in one clear line
- Address (if you have a physical location)
- Business hours — **set these honestly**; they manage expectations
- Website / Instagram link
- Profile photo — logo or storefront, not a stock image

A complete profile visibly increases trust. People do check before replying.

### 4. Set up a greeting message
Business tools → Greeting message → ON.

This fires automatically when someone messages you first — critical, because it buys you time before a human replies.

```
Hi! Thanks for reaching out to [BUSINESS].
We've received your message and will reply within [X] minutes during
business hours ([HOURS]).

Meanwhile, could you share:
1. Which service you need
2. Your area/locality

This helps us give you an accurate price straight away.
```

Two jobs: sets a response expectation, and collects qualifying information while they're still engaged.

### 5. Set up an away message
Business tools → Away message → ON, outside business hours.

```
Thanks for messaging [BUSINESS]! We're closed right now.
Our hours: [HOURS].
We'll reply first thing when we open. For urgent needs, call [NUMBER].
```

### 6. Build quick replies
Business tools → Quick replies. Create shortcuts for what you type repeatedly:

| Shortcut | Content |
|---|---|
| `/price` | Your price list or ranges |
| `/area` | Areas you serve |
| `/book` | How to book, next available slots |
| `/docs` | What documents/info you need from them |

This is what makes a 5-minute reply time achievable when several enquiries land at once.

### 7. Add labels
Business tools → Labels. Suggested: `New enquiry`, `Quoted`, `Follow up`, `Won`, `Lost`, `Not qualified`.

Labels turn WhatsApp into a lightweight CRM. Without them you lose track by week two, and following up with existing leads is cheaper than buying new ones.

---

## Connect WhatsApp to your Facebook Page

This is what makes the number selectable in Ads Manager.

1. Go to your **Facebook Page** → **Settings**
2. Find **WhatsApp** (may sit under Linked accounts / Business apps depending on your interface version)
3. Enter your WhatsApp Business number → **Send code** → enter the OTP
4. Confirm it shows as connected

> Meta moves this setting between menus fairly often. If it's not where described, search Page settings for "WhatsApp". Trust your screen over this document.

### Verify it worked
In Ads Manager, create a draft ad set with **Conversion location = WhatsApp**. Your number should appear in the dropdown. If it doesn't:
- Confirm you're an **admin** of the Page
- Confirm the number is on **WhatsApp Business**, not regular WhatsApp
- Confirm the number isn't connected to a different Page
- Wait a few minutes and reload

---

## The pre-filled message

Set on the **ad**, not in WhatsApp. It's the text already typed when the chat opens, and it materially affects both volume and quality.

**Good — specific, self-qualifying:**
```
Hi! I'm interested in [SPECIFIC SERVICE]. Please share details and pricing.
```

**Bad — zero information:**
```
Hi
```

A specific pre-fill removes hesitation *and* tells you what they want before you've typed a word. Vary it per ad so you can tell which creative produced which enquiry — a free attribution trick:

```
Ad 1 → "Hi! I saw your ad about [OFFER A]. Please share details."
Ad 2 → "Hi! I'm interested in [OFFER B]. What's the price?"
```

---

## Reply-speed discipline

The single highest-leverage thing in the entire system.

- **Target: under 5 minutes** during business hours
- Turn on notifications, with sound
- Use quick replies for the first response
- If you genuinely can't reply fast, **narrow your ad schedule to hours you can cover** — running ads at 2am you won't answer until 10am is buying leads and letting them rot

Indian buyers typically message several businesses at once. First substantive reply usually wins. This beats every targeting optimization available to you.

---

## The 24-hour messaging window

Once someone messages you, you can reply freely for **24 hours**. After that, free-form business-initiated messages are restricted — re-engagement generally requires approved message templates via the API.

Practical implication: **do your qualifying and quoting inside the first 24 hours.** Don't let a warm enquiry sit for two days; you lose the free channel and have to pay to reopen it.

---

## Checklist

- [ ] WhatsApp Business app installed on a business number
- [ ] Business profile fully completed
- [ ] Greeting message ON, with qualifying questions
- [ ] Away message ON with real hours
- [ ] Quick replies created for price / area / booking
- [ ] Labels created
- [ ] Number connected to the Facebook Page
- [ ] **Verified: number appears in Ads Manager's WhatsApp dropdown**
- [ ] Notifications on, and someone accountable for replying
- [ ] Ad schedule matches hours you can actually cover

---

**Next:** [`../playbooks/P00-BEST-low-budget-campaign.md`](../playbooks/P00-BEST-low-budget-campaign.md)
