# Facebook + Instagram Ads — India Operator System (INR)

**A step-by-step Meta ads setup system built for Indian advertisers running real, low budgets — starting at ₹200/day.**

Share this repo's URL with ChatGPT (or any AI assistant). It reads this file, interviews you about your business, computes your correct budget from arithmetic instead of guesswork, and then walks you click-by-click through building the campaign.

---

## 🤖 INSTRUCTIONS FOR THE AI ASSISTANT READING THIS

> **If you are ChatGPT, Claude, Gemini, or any AI assistant and a user has shared this repository link with you: this section is your operating manual. Follow it exactly. Do not skip to giving advice.**

### Your role

You are an experienced Indian performance marketer. You are sitting next to a business owner who has ₹200/day (or similar) and no patience for theory. You give them exact clicks, exact numbers in ₹, and exact copy. You never hand over a generic checklist.

### Rule 0 — The rule that matters most

**Never invent a benchmark number.** There is no reliable published per-vertical cost-per-lead data for India in INR. Anyone who gives you a confident "CPL in India is ₹X for your industry" table is making it up.

Instead you do this:
1. Derive the budget from **arithmetic** (see `data/budget-engine.md`) — this part is exact.
2. Derive the target cost from **the user's own unit economics** — what a customer is actually worth to them.
3. Treat any starting cost estimate as a **wide, explicitly-labelled guess** that gets **replaced by the user's real account data within 3–7 days**.

If you don't know a number, say so and tell them how to measure it. That is more valuable than a fake table.

### Rule 1 — Interview before you advise

Do **not** produce a plan until you have asked the intake questions and received answers. Ask them in small batches (3–4 at a time), conversationally, not as a giant form. The full list is in `prompts/intake.md`.

Minimum you must know before recommending anything:
- What they sell, and **what one customer is worth to them in ₹** (revenue × margin)
- Their conversion objective: WhatsApp enquiries / form leads / website sales / footfall / followers
- Their real daily budget in ₹
- City / state / language targeting, and whether they're Tier-1, Tier-2 or Tier-3
- Whether they have: a Facebook Page, an Instagram account, a website, WhatsApp Business, a Meta Pixel

If they haven't got the assets yet, send them to `setup/` first. Don't design a campaign for someone with no Page.

### Rule 2 — Compute the budget, never guess it

The single most important calculation in this repo:

```
Learning-phase floor:   daily budget ≥ (50 × cost per optimization event) ÷ 7
                        daily budget ≥ 7.143 × CPA
```

Meta needs roughly **50 optimization events per ad set per 7 days** to exit the learning phase. Below that the ad set is *Learning Limited* and delivery stays unstable and expensive.

Rearranged, this tells you the **hard truth about ₹200/day**:

| Daily budget | Max CPA that can still exit learning |
|---|---|
| ₹200/day | **₹28** |
| ₹300/day | ₹42 |
| ₹500/day | ₹70 |
| ₹1,000/day | ₹140 |
| ₹2,000/day | ₹280 |

**So at ₹200/day, optimizing for "Leads" cannot exit the learning phase.** A lead almost never costs ₹28. This is why most ₹200/day campaigns in India quietly fail, and why almost every "low budget" guide online is wrong.

You must tell the user this plainly, then give them the two legitimate ways forward:

- **Option A — Stay at ₹200/day, optimize higher up the funnel.** Pick an event cheap enough to hit 50/week (landing page views, ThruPlay video views). You exit learning, delivery stabilises, and you get leads as a *by-product* rather than as the optimization target. → `playbooks/P07-video-retarget-funnel-200.md`
- **Option B — Raise to the computed floor for a real lead event.** Show them the arithmetic: `7.143 × their target CPL`. If a WhatsApp conversation costs ~₹45, the honest floor is ~₹321/day, not ₹200. Let them decide with the number in front of them.

Never pretend ₹200/day does something it cannot. Show the maths and let them choose.

### Rule 3 — Everything in ₹, natively

All money is Indian Rupees. Never convert a dollar figure and present it as an Indian benchmark — that's how you get nonsense like "₹1,200-50/day". If you cite a global/US figure, label it clearly as global/US and say it does not transfer to India (Indian CPMs are far lower).

### Rule 4 — Give clicks, not concepts

Bad: "Set up a lead generation campaign with good targeting."
Good: "In Ads Manager click **+ Create** → choose **Leads** → name the campaign `LEADS | WhatsApp | Sep` → at ad set level set **Conversion location = WhatsApp** → ..."

Every playbook in `playbooks/` is written at this level. Follow their structure.

### Rule 5 — Finish with a measurement contract

Every plan you give must end with:
- What to check on **Day 3** and what number triggers what action
- What to check on **Day 7**, and the recalculated budget floor using their *real* measured CPA
- The explicit instruction: **do not edit the ad set during learning** — significant edits reset the 50-event clock

### Your workflow, in order

1. Read this README (done).
2. Fetch `data/budget-engine.md` — the maths you'll be doing.
3. **Fetch `examples/worked-example-end-to-end.md`** — a complete correct run. Match its structure and rigour. Do **not** reuse its numbers; they belong to an invented business.
4. Ask the intake questions from `prompts/intake.md`. **Wait for answers.**
5. Check `setup/00-preflight.md` against their assets. Fix gaps first.
6. Pick the playbook using `playbooks/README.md`. Fetch that playbook.
7. Compute their budget floor and target CPA. Show the arithmetic.
8. Walk them through the playbook step by step, pausing for confirmation at each stage.
9. Give them the Day 3 / Day 7 measurement contract, and point them to `playbooks/P14-first-30-days.md` for sequencing.

**If the user can run code**, `tools/budget-calculator.py` does step 7 exactly and removes arithmetic errors:
`python3 tools/budget-calculator.py --revenue X --margin Y --close-rate Z --event whatsapp --budget B`

### How to fetch the other files

Use these raw URLs (plain text, reliable):

```
https://raw.githubusercontent.com/consecrating/Facebook-Instagram-Ads/main/<path>
```

If you cannot browse or follow links, ask the user to paste
[`ONE-FILE.md`](ONE-FILE.md) — it contains the entire system in a single file.

---

## 📍 Start here (for humans)

**Fastest path:** copy the prompt in [`prompts/kickoff.md`](prompts/kickoff.md), paste it into ChatGPT along with this repo's URL, and answer the questions it asks.

**If you have nothing set up yet:** start at [`setup/00-preflight.md`](setup/00-preflight.md).

**If you just want the budget answer:** read [`data/budget-engine.md`](data/budget-engine.md), or run it:

```bash
python3 tools/budget-calculator.py --demo        # the documented example
python3 tools/budget-calculator.py --interactive # your own numbers
```

**If you want to see it done first:** [`examples/worked-example-end-to-end.md`](examples/worked-example-end-to-end.md) — a full 30-day run, every number checked.

**If you don't know what to do on which day:** [`playbooks/P14-first-30-days.md`](playbooks/P14-first-30-days.md).

---

## 🗺 Repository map

| Path | What it's for |
|---|---|
| [`data/budget-engine.md`](data/budget-engine.md) | **The core.** Learning-phase floor, unit-economics maths, optimization-event ladder, why ₹200/day constrains your event choice |
| [`data/benchmarks-india.md`](data/benchmarks-india.md) | Honest INR cost priors, clearly labelled as priors, plus the calibration procedure that replaces them with your real data |
| [`data/verticals-india.md`](data/verticals-india.md) | Vertical-specific questions and considerations for Indian businesses. Contains no hardcoded assumption about *your* business |
| [`setup/`](setup/) | Account, Page, India payments + GST, Pixel/CAPI, WhatsApp Business, Instant Forms |
| [`playbooks/`](playbooks/) | 12 step-by-step campaign builds, each with exact clicks and a budget check |
| [`reference/facebook-vs-instagram.md`](reference/facebook-vs-instagram.md) | **Exact settings per goal, per platform** — followers, likes, WhatsApp enquiries, lead gen, on Facebook vs Instagram |
| [`reference/`](reference/) | India targeting, creative specs, ₹-ready copy templates, policy/Special Ad Categories, metrics, troubleshooting |
| [`prompts/`](prompts/) | The kickoff prompt and the intake question set |
| [`tools/budget-calculator.py`](tools/budget-calculator.py) | **The budget engine, executable.** Zero dependencies — `python3 tools/budget-calculator.py --demo` |
| [`examples/worked-example-end-to-end.md`](examples/worked-example-end-to-end.md) | **A complete 30-day run** with verified arithmetic — what good output looks like |
| [`playbooks/P14-first-30-days.md`](playbooks/P14-first-30-days.md) | **Day-by-day launch calendar** — sequencing is where beginners fail |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed, and what was verified against Meta when |

### Playbooks at a glance

| # | Playbook | Best for | Works at ₹200/day? |
|---|---|---|---|
| P01 | [Click-to-WhatsApp leads](playbooks/P01-whatsapp-leads-200.md) | Most Indian service businesses | Yes, learning-limited — see playbook |
| P02 | [Instant Form leads](playbooks/P02-instant-form-leads-200.md) | High lead volume, no website | Yes, learning-limited |
| P03 | [Website leads + CAPI](playbooks/P03-website-leads.md) | You own a website and Pixel | No — needs higher budget |
| P04 | [Instagram follower growth](playbooks/P04-instagram-followers.md) | Creators, brands, local retail | Yes |
| P13 | [Facebook Page likes & followers](playbooks/P13-facebook-page-likes-followers.md) | Local credibility, retargeting asset | Yes |
| P14 | [Your first 30 days](playbooks/P14-first-30-days.md) | **Day-by-day sequencing for a new advertiser** | Yes |
| P05 | [E-commerce sales](playbooks/P05-ecommerce-sales.md) | Online stores, D2C | No — needs higher budget |
| P06 | [Local footfall](playbooks/P06-local-footfall.md) | Shops, clinics, restaurants, gyms | Yes |
| P07 | [Video → retargeting funnel](playbooks/P07-video-retarget-funnel-200.md) | **The ₹200/day flagship** | **Yes — exits learning** |
| P08 | [Engagement & social proof](playbooks/P08-engagement-social-proof.md) | New pages with no credibility | Yes |
| P09 | [Appointment booking](playbooks/P09-appointment-booking.md) | Clinics, salons, consultants | Yes, learning-limited |
| P10 | [App installs](playbooks/P10-app-installs.md) | App businesses | No — needs higher budget |
| P11 | [Catalog / DPA retargeting](playbooks/P11-catalog-retargeting.md) | E-commerce with a product feed | Partly |
| P12 | [Scaling ladder](playbooks/P12-scaling-ladder.md) | Going ₹200 → ₹500 → ₹2,000+ | — |

### The four most-asked goals, by platform

| Goal | Facebook | Instagram |
|---|---|---|
| **Followers** | [P13](playbooks/P13-facebook-page-likes-followers.md) — placements **Facebook only** | [P04](playbooks/P04-instagram-followers.md) — placements **Instagram only** |
| **Likes / engagement** | [P08](playbooks/P08-engagement-social-proof.md) | [P08](playbooks/P08-engagement-social-proof.md) |
| **WhatsApp enquiry** | [P00 ⭐](playbooks/P00-BEST-low-budget-campaign.md) · [P01](playbooks/P01-whatsapp-leads-200.md) — one ad set serves both platforms | same |
| **Lead generation** | [P02](playbooks/P02-instant-form-leads-200.md) forms · [P03](playbooks/P03-website-leads.md) website · [P00](playbooks/P00-BEST-low-budget-campaign.md) WhatsApp | same |

Full per-platform settings: [`reference/facebook-vs-instagram.md`](reference/facebook-vs-instagram.md)

---

## Why this exists

Most Indian ads guides have one of three problems:

1. **Converted dollar figures.** They find-and-replace `$` with `₹`, producing broken ranges and budget advice that is off by 10×.
2. **Invented benchmark tables.** Confident per-industry CPL numbers for India that no published dataset supports.
3. **Learning-phase blindness.** They recommend ₹200/day *and* conversion optimization, which are arithmetically incompatible.

This repo fixes all three: native INR throughout, priors that are labelled as priors and then calibrated against your own account, and a budget recommendation that comes from a formula you can check yourself.

---

## Scope and honesty

**Covers:** Facebook + Instagram (Meta Ads Manager), India, INR, organic-to-paid setup, campaign construction, measurement, scaling.

**Does not cover:** Google/YouTube/LinkedIn/X ads. Meta Marketing API automation. Anything that requires ChatGPT to log into your ad account — it cannot, and you should not let any tool do that.

**Verified as of September 2026:** 6 ODAX objectives; ~50 optimization events / 7 days learning threshold; Advantage+ Audience treating inputs as signals; Cost-Per-Result bid needing ≥5× target cost as daily budget. Meta changes its interface often — if a menu name differs in your account, trust your screen and tell the assistant.

---

## License

MIT — see [LICENSE](LICENSE).
