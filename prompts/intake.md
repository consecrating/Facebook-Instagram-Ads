# Intake Questions

**For the AI assistant:** ask these in batches of 3–4, conversationally. Wait for answers. Do not produce a plan until Blocks A–C are answered.

**For the user:** answering these well is what makes the output specific to you instead of generic. Block B is the one that unlocks the budget maths.

---

## Block A — What you sell

1. What does your business do, in one line?
2. What specifically do you want to advertise right now?
3. Which city/area do you serve? How far will a customer realistically travel to you?
4. Which language do your customers actually speak?

## Block B — Your numbers ⭐ (the budget maths needs these)

5. **When you close one customer, roughly how much revenue is that?** ₹______
6. **Roughly what's your gross margin on that?** ______%
   *(If unsure: what's left after the direct cost of delivering it?)*
7. **Out of 10 genuine enquiries, how many become paying customers?** ______
8. **What's your real daily ad budget?** ₹______
9. Is that a hard ceiling, or could you go higher if the maths justified it?

> **If the user can't answer 5–7:** don't guess silently. Use placeholders, **state them as assumptions out loud**, and tell them the recommendation will be provisional until they know their real numbers.

## Block C — The action

10. What should someone DO after seeing your ad?
    - Message you on WhatsApp
    - Fill a form so you can call them
    - Visit your website
    - Buy online
    - Come to your shop/clinic
    - Book an appointment
    - Follow your Instagram
11. How do you currently get customers, and what's worked before?
12. **Can you reply to an enquiry within 5 minutes during business hours?** Who will do it?

> Question 12 is not administrative. If the answer is no, WhatsApp and form playbooks will underperform badly, and you should say so plainly.

## Block D — What you have

13. Tick what exists:
    - [ ] Facebook Page
    - [ ] Instagram (professional account?)
    - [ ] Website
    - [ ] WhatsApp Business app
    - [ ] Meta Pixel installed
    - [ ] Meta Business Manager
    - [ ] Ad account with INR currency
    - [ ] Payment method that has worked
14. Have you run Meta ads before? What happened — spend, results, costs?
15. Do you have a product catalog / feed? *(e-commerce only)*

## Block E — Constraints & risk

16. Do you advertise anything related to **credit, loans, insurance, jobs/recruitment, property/housing**, or political/social issues?
    > ⚠️ If yes → **Special Ad Category**. Read [`../reference/policy-and-special-categories.md`](../reference/policy-and-special-categories.md) before building. Targeting will be restricted and costs will be higher.
17. Anything you cannot claim, or any past ad rejections?
18. Is your business seasonal? When's your peak?
19. Do you have a GSTIN? *(affects whether the ~18% GST on ads is recoverable)*

## Block F — Creative capability

20. Can you shoot a 30–60 second phone video? *(unlocks [P07](../playbooks/P07-video-retarget-funnel-200.md), the best ₹200/day option)*
21. Do you have real photos of your work/premises/products?
22. Do you have customer testimonials or reviews?
23. Are you willing to put your price in the ad? *(strongest quality filter available)*

---

## What the assistant does with the answers

```
Q5, Q6, Q7  →  Affordable CPL = revenue × margin × 0.30 × close rate
Q10         →  optimization event + its rung on the ladder
Q8          →  compare against learning floor = 7.143 × event cost
Q12         →  whether WhatsApp/forms are viable at all
Q13         →  which setup/ files are needed first
Q16         →  Special Ad Category check BEFORE building
Q20         →  whether P07 is available
Q1–Q4       →  vertical lookup in ../data/verticals-india.md
```

**Then, in order:**
1. Compute affordable CPL → show the arithmetic
2. Compute recommended budget (T2) = `7.143 × event cost` → show the arithmetic
3. State honestly whether their budget reaches that floor
4. If not, offer the four options: cheaper rung / accept learning-limited / concentrate budget into fewer days / raise budget
5. Route to a playbook
6. Fix any setup gaps from Q13 first
7. Walk the playbook step by step
8. End with the Day 3 / Day 7 measurement contract

---

## Minimum viable intake

If the user is impatient, these five are the irreducible minimum:

```
1. What do you sell, and what's one customer worth to you in ₹?
2. What should people DO after seeing the ad?
3. What's your daily budget in ₹?
4. Where do you serve?
5. Can you reply to enquiries within 5 minutes?
```

Everything else can be inferred or asked later. **Without these five, any recommendation is guesswork** — and the assistant should say so rather than producing a confident plan built on nothing.

---

**Related:** [`kickoff.md`](kickoff.md) · [`../data/best-budget-recommender.md`](../data/best-budget-recommender.md) · [`../data/verticals-india.md`](../data/verticals-india.md)
