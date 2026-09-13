# 05 — Instant Forms (Lead Forms)

For [P02](../playbooks/P02-instant-form-leads-200.md) and [P09](../playbooks/P09-appointment-booking.md).

Instant Forms open **inside** Facebook/Instagram — no website needed, no page load, and fields pre-fill from the user's profile. On Indian mobile connections, removing a page load is a genuine conversion advantage.

---

## Requirement you cannot skip

**You need a privacy policy URL.** Meta requires it on every Instant Form and will reject ads without one.

Options: a `/privacy-policy` page on your site, a free generator, or a public Google Doc set to view-only. It must be a working public URL.

---

## Form type: the decision that shapes lead quality

Chosen when you create the form.

| | **More volume** | **Higher intent** |
|---|---|---|
| Flow | Submit directly | Adds a review/confirm step |
| Volume | Higher | Roughly 30–40% lower |
| Quality | Mixed — includes accidental taps | Noticeably better |
| Use when | You need volume and can filter later | Your time per lead is expensive |

**At low budget, "Higher intent" is usually correct.** Fewer leads that actually respond beats more leads you can't work through. Your constraint at ₹200–500/day is rarely lead volume — it's your capacity to follow up.

---

## Creating a form

In the **ad** level → **Instant form** → **Create form**

### 1. Form name
`[Service] - Higher Intent - Sep26` — you'll accumulate many; name them so you can find them.

### 2. Intro (optional but recommended)
Headline + a short "what you get" list. This is where you set expectations and filter.

```
Headline:  Free Site Visit — [Project], [City]
Benefits:  • 2 & 3 BHK from ₹XX lakh
           • RERA registered
           • Site visit at your convenience
```

Stating the price range here is one of the strongest quality filters available.

### 3. Questions

**Keep it to 3–4 fields.** Every extra field costs you completions.

**Prefill fields** (pulled from profile, high completion):
- Full name
- Phone number
- Email

> In India, **phone matters more than email.** Most follow-up happens by call or WhatsApp. Prioritise phone.

**Custom questions** — add one or two, no more:

| Type | Good for |
|---|---|
| Multiple choice | Budget range, timeline, service needed — **preferred**, easy to tap |
| Short answer | Specific detail. Reduces completion — use sparingly |
| Conditional | Follow-up questions based on an earlier answer |
| Appointment request | Booking flows ([P09](../playbooks/P09-appointment-booking.md)) |

**The single best qualifying question** is budget or timeline as multiple choice:

```
What's your budget range?
  ○ Under ₹XX,000
  ○ ₹XX,000 – ₹XX,000
  ○ Above ₹XX,000
  ○ Just researching
```

"Just researching" is doing real work for you — it self-identifies the leads not to call first.

### 4. Privacy policy
Paste your URL. Add a custom disclaimer if you need consent for WhatsApp/marketing contact.

### 5. Completion screen
Don't waste it. Set expectations and offer an immediate next step:

```
Thanks [Name]! We've got your details.
We'll call you within [X] hours during business hours.

Can't wait? WhatsApp us now: [link]
Button: [View website] or [WhatsApp us]
```

A CTA button here gives motivated leads a way to reach you instantly instead of waiting.

---

## Getting the leads out — do this before launching

**A lead you never see is money burned.** Choose a retrieval route and test it.

| Route | Notes |
|---|---|
| **Manual CSV** | Page → Lead Center / Forms Library → download. Free but slow. **Not viable if you need 5-minute response** |
| **Instant notifications** | Enable Page notifications so you see leads immediately |
| **CRM integration** | Business settings → Integrations → connect your CRM |
| **Zapier / Make** | Route leads to Google Sheets, WhatsApp, email, SMS |
| **Google Sheets via automation** | Cheap and effective for small teams |

### Recommended minimum setup
1. Enable instant notifications
2. Automate to a Google Sheet **and** an alert (WhatsApp/SMS/email)
3. **Submit a test lead yourself** and confirm it arrives everywhere

Then time yourself: from submission to your alert. If it's over 5 minutes, fix it before spending.

---

## Reality check on speed

Lead-form submissions are low-friction — people often fill several forms across several businesses in one sitting. The follow-up gap is brutal: response within minutes versus hours changes contact rates dramatically.

If you cannot commit to fast follow-up, **use [P00 WhatsApp](../playbooks/P00-BEST-low-budget-campaign.md) instead** — a WhatsApp chat at least sits in a thread the person will see, whereas an unanswered form lead simply goes cold.

---

## Common mistakes

| Mistake | Consequence |
|---|---|
| 8 form fields | Completion collapses |
| Email but no phone | Can't actually reach Indian leads |
| "More volume" with no filter | Drowning in unqualified taps |
| No qualifying question | No idea who to call first |
| Never testing lead delivery | Leads accumulate unseen |
| Empty completion screen | Losing your hottest moment |
| No price indication | Every call starts with "kitna hai?" |

---

## Checklist

- [ ] Privacy policy URL live and working
- [ ] Form type chosen deliberately (Higher intent recommended)
- [ ] 3–4 fields maximum, **phone included**
- [ ] One multiple-choice qualifying question
- [ ] Intro states price range or key filter
- [ ] Completion screen with expectation + WhatsApp CTA
- [ ] Lead delivery automated **and tested with a real submission**
- [ ] Time-to-alert measured and under 5 minutes

---

**Next:** [`../playbooks/P02-instant-form-leads-200.md`](../playbooks/P02-instant-form-leads-200.md)
