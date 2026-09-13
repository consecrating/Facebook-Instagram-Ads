# Changelog

Meta changes Ads Manager often. This file records what was verified when, so you can judge how current the guidance is.

---

## v1.2 — 2026-09-13

**Added**
- `tools/budget-calculator.py` — the budget engine, executable. Zero dependencies, stdlib only. Interactive, CLI, `--demo` and `--table` modes. Reproduces the documented figures exactly (₹322 floor for a ₹45 event, ₹415 for ₹58)
- `tools/README.md` — usage and options
- `examples/worked-example-end-to-end.md` — one complete 30-day run with fully verified arithmetic, from intake through Day-7 recalibration to a month-2 projection. Written so the AI assistant can pattern-match correct output
- `playbooks/P14-first-30-days.md` — day-by-day launch calendar with two tracks (Direct at the computed floor, Funnel at a hard ₹200/day ceiling)
- Facebook vs Instagram sections for **P05, P06, P09, P11, P12** — the gap flagged in the v1.1 audit

**Fixed**
- Budget floor now rounds **up** (`math.ceil`). A floor that rounds down isn't a floor. This resolved a ₹321-vs-₹322 mismatch between the calculator and the docs
- Sub-rupee prior bands rendered as `Rs 0-0`; now display as `Rs 0.05-0.3`
- Piped stdin could not reach the interactive flow; added `--interactive`

**Notes**
- P12 now warns about the most common platform mistake: concluding Instagram "doesn't work" when only a 4:5 asset was uploaded, so Advantage+ was serving cropped creative into Reels and Stories
- P11 explains why retargeting should keep Advantage+ placements **ON** — small audiences need breadth to hold frequency down, which is the opposite of the usual "narrow your retargeting" instinct

---

## v1.1 — 2026-09-13

**Audit finding:** of the four goals users ask for most, two were uncovered.

| Goal | Status before |
|---|---|
| WhatsApp enquiry | ✅ covered |
| Lead generation | ✅ covered |
| Followers | ⚠️ Instagram only |
| Likes | ❌ not a goal anywhere |

A search for `page like` / `page follower` / `like your page` returned nothing — there was no way to grow a Facebook Page.

**Added**
- `playbooks/P13-facebook-page-likes-followers.md` — Engagement → conversion location **On your Page** → maximise Page likes, with placements restricted to **Facebook only**
- `reference/facebook-vs-instagram.md` — exact settings for each goal on each platform, plus a master matrix

**Changed**
- P08 now explicitly owns the "likes" goal and routes to P13/P04
- P04 clarified as Instagram-only, with a Facebook comparison
- `prompts/intake.md` asks which platform matters, and challenges follower goals with *"what is one follower worth to you in ₹?"*
- README, playbooks index and ONE-FILE carry a four-goals-by-platform table

**Key correction captured:** never split Facebook and Instagram into separate ad sets at low budget — it halves the learning signal for both. Restrict placements **only** for follower campaigns, where it's mandatory.

---

## v1.0 — 2026-09-13

Initial release.

**The core idea**

```
learning-phase floor:  daily budget ≥ (50 × CPA) ÷ 7 = 7.143 × CPA
```

Meta needs roughly 50 optimization events per ad set per 7 days to exit the learning phase. Rearranged, at ₹200/day your event must cost ≤ ₹28 — and a lead never costs ₹28. So **"₹200/day optimized for Leads" cannot exit the learning phase**, which most low-budget advice written for Indian advertisers ignores.

**Included**
- `README.md` as an AI bootloader with an explicit operating manual (Rules 0–5)
- `data/` — budget engine, best-budget recommender (5 tiers), honest benchmarks, 15 Indian verticals
- `setup/` — preflight, Business Manager, India payments/GST/UPI, Pixel+CAPI, WhatsApp Business, Instant Forms
- `playbooks/` — P00–P12, each with exact clicks, a budget check and a Day 3 / Day 7 measurement contract
- `reference/` — targeting, creative specs, ₹ copy templates, Special Ad Categories, metrics, troubleshooting
- `ONE-FILE.md` — the whole system in one file, for assistants that can't browse

**Deliberately excluded:** any invented per-vertical CPL table for India. No reliable published dataset exists in INR, so the system uses wide order-of-magnitude priors to pick a strategy, then calibrates against your own account on Day 7.

---

## Verified against Meta behaviour

Last checked **September 2026**:

| Item | Status |
|---|---|
| 6 ODAX objectives (Awareness, Traffic, Engagement, Leads, App Promotion, Sales) | Verified |
| ~50 optimization events per ad set per 7 days to exit learning | Verified (observed threshold, not a hard rule) |
| Advantage+ Audience treats inputs as signals, not hard boundaries | Verified |
| Location remains a hard constraint even with Advantage+ | Verified |
| Cost-per-result bidding requires daily budget ≥ 5× target cost | Verified |
| WhatsApp lives under **Engagement**, not Leads | Verified |
| Page likes live under Engagement → On your Page | Verified |
| GST on Indian digital advertising, commonly 18%, charged on top of spend | Verified — confirm the current rate with your CA |

**If a menu name in your account differs from this repo, trust your screen.** Meta renames things frequently, and the repo may lag.
