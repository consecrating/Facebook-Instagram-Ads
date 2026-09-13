# The Kickoff Prompt

**Copy everything in the box below and paste it into ChatGPT.** That's the whole setup.

---

```
I want to set up Facebook and Instagram ads for my business in India.

Use this repository as your complete operating manual:
https://github.com/consecrating/Facebook-Instagram-Ads

Read the README first — it contains a section called "INSTRUCTIONS FOR THE
AI ASSISTANT" that tells you exactly how to work with me. Follow it.

Key things about me:
- I'm in India. All budgets and costs must be in INR (₹).
- I want to start at a low budget, around ₹200/day.
- I also want to know what my BEST budget would be, calculated from my
  actual business numbers — not a generic recommendation.
- I need step-by-step instructions with exact clicks, not general advice.

Before giving me any plan, interview me. Ask the intake questions in small
batches and wait for my answers. Do not assume anything about my business.

Then:
1. Compute my recommended budget using the formula in data/budget-engine.md
   and show me the arithmetic.
2. Tell me honestly whether ₹200/day can work for what I want.
3. Pick the right playbook from playbooks/README.md.
4. Walk me through it step by step, pausing for me to confirm each stage.
5. End with what to check on Day 3 and Day 7.

Start by asking me the intake questions.
```

---

## What should happen next

ChatGPT should **ask you questions**, not immediately produce a plan. If it starts dumping generic advice, reply:

```
Stop. Read the "INSTRUCTIONS FOR THE AI ASSISTANT" section of the README
and follow it. Interview me first.
```

## If ChatGPT says it can't access the link

Some ChatGPT modes can't browse. Two fallbacks:

**Option 1 — paste the raw README:**
```
https://raw.githubusercontent.com/consecrating/Facebook-Instagram-Ads/main/README.md
```
Open that, copy all of it, paste it into the chat with:
> "This is my operating manual. Follow the AI assistant instructions in it."

**Option 2 — paste the single-file version:**
Open [`ONE-FILE.md`](../ONE-FILE.md), copy the whole thing, paste it in. It contains the entire system condensed into one file.

---

## Shorter version

If you just want the budget answer:

```
Read https://raw.githubusercontent.com/consecrating/Facebook-Instagram-Ads/main/data/budget-engine.md

I'm in India, budget ₹200/day, and I want WhatsApp enquiries for my
[YOUR BUSINESS]. One customer is worth about ₹[AMOUNT] to me at
[MARGIN]% margin, and I close about [N] out of 10 enquiries.

Compute my recommended daily budget and show the arithmetic. Tell me
honestly whether ₹200/day works.
```

---

## What good output looks like

You should get:
- **Questions first**, before any recommendation
- A **calculated** budget with visible arithmetic — e.g. `7.143 × ₹45 = ₹322/day`
- An **honest answer** about ₹200/day, including its limitations
- **Exact clicks** — "click + Create → choose Engagement → set Conversion location = WhatsApp"
- A named playbook
- A **Day 3 / Day 7** measurement plan

If you get a generic listicle instead, the assistant hasn't read the README. Point it back.

**Want to see a correct answer before you ask for yours?**
Open [`../examples/worked-example-end-to-end.md`](../examples/worked-example-end-to-end.md) — a complete 30-day run, every number checked. That's the standard to hold ChatGPT to.

---

## Check the maths yourself

You don't have to trust anyone's arithmetic, including ChatGPT's:

```bash
python3 tools/budget-calculator.py --interactive
```

Zero dependencies, nothing leaves your machine. If ChatGPT's recommended budget doesn't match the calculator's, the calculator is right — ask ChatGPT to redo it.

---

## Don't know what to do on which day?

Ask for the calendar:

```
Walk me through playbooks/P14-first-30-days.md for my situation.
Tell me which track I'm on and what I do this week.
```

---

**Next:** [`intake.md`](intake.md) — the questions it should ask you
