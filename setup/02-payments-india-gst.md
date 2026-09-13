# 02 — Payments, GST & Billing (India)

The part that blocks more first-time Indian advertisers than any targeting question.

> ⚠️ **Tax and payment rules change.** Treat this file as orientation, then verify current rates and requirements with Meta's billing screens and **your own CA**. Nothing here is tax advice.

---

## Setting up payment

**Ads Manager → Billing & payments → Payment settings → Add payment method**

Commonly available in India:

| Method | Notes |
|---|---|
| **Credit card** | Most reliable for automatic billing |
| **Debit card** | Works, but depends on your bank's 3D-Secure/OTP handling and recurring-payment support |
| **UPI** | Widely used for Indian ad accounts |
| **Net banking** | Availability varies |
| **Prepaid balance / add funds** | You top up first, ads spend from the balance |

**Availability differs by account.** Don't trust any article — including this one — for what your account offers. Open the screen and look.

### Prepaid vs automatic billing

| | Prepaid (add funds) | Automatic (postpaid) |
|---|---|---|
| How it works | Top up, ads draw down | Meta charges you at thresholds |
| Spend control | Hard stop at zero | Continues until you pause |
| Best for | Low budgets, strict control | Established, uninterrupted campaigns |
| Risk | Campaign stops dead at ₹0 | Surprise charges |

**At ₹200–500/day, prepaid is usually the safer choice** — it makes overspend structurally impossible. The trade-off is that hitting zero pauses delivery, and a pause plus restart can disturb the learning phase. Set a calendar reminder to top up.

### The RBI recurring-payment issue

Indian regulations on recurring card mandates have caused auto-debit failures for some advertisers. Symptoms: campaigns pause unexpectedly, "payment failed" notifications, or ads stopping overnight.

Mitigations:
- Keep a **backup payment method** on file
- Prefer **prepaid top-ups** if failures recur
- Watch for payment-failure emails and act quickly — a failed payment can pause everything

---

## Verify with a real charge before you launch

A payment method that *looks* added is not proven. Run a **₹100/day campaign for one day**, confirm the charge actually settles, then build the real campaign.

Discovering a broken payment method mid-campaign costs you the learning phase, not just a day.

---

## GST on Meta ads

**Digital advertising in India attracts GST — commonly 18% for advertising services.** Verify the current rate with your CA; rates and rules change.

### What this means for your budget

**GST is generally on top of your ad spend, not inside it.**

```
Ad spend         ₹6,000/month  (₹200/day × 30)
GST at 18%       ₹1,080
Total outflow    ₹7,080
```

Budget for the total, not the ad spend. People routinely plan ₹6,000 and get billed more.

### If you have a GSTIN

- **Add your GSTIN to your ad account:** Billing & payments → Payment settings → add GST registration number
- With a valid GSTIN, GST paid on advertising is generally available as **input tax credit** against your output GST liability — meaning the effective cost of the tax can be recovered. **Confirm eligibility and mechanism with your CA.**
- Depending on how Meta bills your account, the transaction may fall under **reverse charge mechanism (RCM)**, where you self-account for the GST. Your CA will tell you which applies to your invoices

### If you don't have a GSTIN

You pay GST and cannot claim credit. It's a real 18%-ish cost. If you're spending meaningfully on ads and are otherwise eligible to register, this is worth discussing with your CA — the recoverable tax alone can justify registration.

### Getting invoices

**Billing & payments → Transactions → download invoice.** Download monthly and hand them to your accountant. Ensure the GSTIN and legal entity name on the invoice are correct — a wrong GSTIN can jeopardise your input credit claim.

---

## Spend limits worth setting

**Account spending limit** — a lifetime cap for the ad account. Once reached, all campaigns stop.

**Billing & payments → Account spending limit → Set limit**

At low budgets this is a genuine safety net against a misconfigured campaign. Set it to something like one month's intended spend. Note it's cumulative for the account, so you'll need to raise or reset it as you continue.

**Campaign spending limit** — a cap per campaign, set at campaign level. Useful when testing.

---

## Troubleshooting

| Symptom | Likely cause | Action |
|---|---|---|
| "Payment method declined" | Bank blocked international/recurring transaction | Call your bank; enable online/international use; try UPI |
| Ads paused overnight, no warning | Payment failure or spending limit reached | Check Billing; check account spending limit |
| Charged more than expected | GST added on top, or overdelivery on peak days | Download invoice and reconcile; daily budget can flex up to ~25% on a given day |
| Ad account disabled for payment | Repeated failures or unpaid balance | Clear the balance, then appeal in Account Quality |
| Can't add GSTIN | Wrong field or unverified entity | Payment settings → business info; ensure legal name matches |
| Campaign stopped at ₹0 | Prepaid balance exhausted | Top up; consider automatic billing or reminders |

---

## Checklist

- [ ] Ad account currency = **INR**, timezone = **Asia/Kolkata** (permanent — verify now)
- [ ] Payment method added **and proven with a real ₹100 charge**
- [ ] Backup payment method on file
- [ ] GSTIN added, if you have one
- [ ] Budget planned **including** GST
- [ ] Account spending limit set
- [ ] You know where to download invoices

---

**Next:** [`04-whatsapp-business.md`](04-whatsapp-business.md) for P00/P01 · [`03-pixel-and-capi.md`](03-pixel-and-capi.md) for website campaigns
