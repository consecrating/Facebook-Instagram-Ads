# Targeting for India

## The 2026 reality: you target less than you think

Meta has spent years removing targeting controls and handing the work to its own AI. With **Advantage+ Audience** on, the age/gender/interest inputs you provide are treated as **signals**, not hard boundaries. If Meta finds someone outside your list who looks likelier to convert, it will deliver there.

**One exception: location is always respected as a hard constraint.** Meta will not show your ad outside the geography you set.

Two consequences that matter at low budget:

1. **Detailed interest targeting is largely theatre now.** Stacking twelve interests mostly just slows learning without meaningfully constraining delivery
2. **Location and creative are your real targeting tools.** Location is enforced; creative self-selects its audience

> **The low-budget rule: broad audience + Advantage+ ON + sharp creative.** Let the creative do the targeting. This is counter-intuitive if you learned Facebook ads in 2018, but it's correct now.

---

## Location — your most powerful control

### Radius targeting

**Ad set → Audience → Location → Edit → drop a pin → set radius**

| Business type | Start radius |
|---|---|
| Restaurant, café, salon | 3–7 km |
| Clinic, gym, tuition centre | 5–10 km |
| Showroom, specialist retail | 10–25 km |
| Service business (you travel to them) | 15–30 km |
| Destination / high-ticket | City-wide |
| Online, ships anywhere | State or all-India |

**Start at the low end and widen only if delivery is starved.** A tight radius in a Tier-2 city is genuinely cheap to saturate — that's the low-budget advantage.

### The four location types — pick deliberately

| Option | Meaning | Use for |
|---|---|---|
| **People living in or recently in this location** | Residents + recent visitors | **Default for most local businesses** |
| People living in this location | Residents only | When commuters/tourists are useless to you |
| People recently in this location | Visitors | Airports, tourist spots, event venues |
| People travelling in this location | Tourists | Hotels, travel services |

### City tiers and cost

Broadly: **Tier-1 metros cost materially more than Tier-2/3.** If you can serve smaller cities, your budget stretches considerably further there.

```
Tier 1   Mumbai, Delhi NCR, Bengaluru, Hyderabad, Chennai, Kolkata, Pune
Tier 2   Jaipur, Lucknow, Indore, Nagpur, Kochi, Coimbatore, Surat,
         Bhopal, Chandigarh, Visakhapatnam, Vadodara, Ludhiana …
Tier 3   District towns
```

**Practical tactic:** if you serve nationally, test Tier-2/3 cities separately from metros — but only once your total budget supports more than one ad set (~₹600+/day). Below that, one broad ad set beats two starved ones.

### Excluding locations
Useful when you can't deliver somewhere, or a region generates junk leads. **Location → Exclude.** Don't over-exclude at low budget; every exclusion shrinks the optimization space.

---

## Language targeting

Leave it **blank** unless you're specifically running non-English creative.

**Why:** language targeting keys off the user's app/interface language, which is a weak proxy in India. Many people whose spoken language is Hindi use Facebook in English. Setting `Language = Hindi` can cut your audience drastically without improving relevance.

**The better approach: let the creative do the language targeting.** A Hindi video naturally self-selects Hindi speakers. Tamil creative self-selects Tamil speakers. No setting required.

**Where language targeting genuinely helps:** you have multiple language versions of the same creative and want to control which audience sees which. Then set it — otherwise leave blank.

**Regional-language creative often faces less competition**, which can mean lower costs. Worth testing if your customers speak a regional language.

---

## Age and gender

**Set the widest range that's genuinely plausible.**

Every year you remove shrinks Meta's optimization space. And under Advantage+ these are suggestions anyway — unless you're in a Special Ad Category, where they become enforced restrictions and often locked.

| Situation | Setting |
|---|---|
| Most businesses | 25–55, All genders |
| Products genuinely for young adults | 18–34 |
| Retirement/senior products | 50–65+ |
| Genuinely gender-specific product | Set gender |
| Special Ad Category | You'll be restricted regardless |

**Common mistake:** targeting 25–34 because "that's my customer". Unless you have data proving 35-year-olds never buy, you're excluding people who would. Let the algorithm find out.

**Vertical trap worth repeating:** for tuition and coaching, the buyer is usually the **parent**, not the student. Targeting 16–20 when 40-year-olds pay the fees is a common and expensive error.

---

## Audience types

### Custom audiences — your best asset

Built from people who already interacted with you. **Audiences → Create audience → Custom audience**

| Source | Needs | Value |
|---|---|---|
| **Video viewers (50%+)** | A video ad | ⭐ Best low-budget option — cheap to build |
| **Page / Instagram engagers** | Any activity | ⭐ Free, accumulates automatically |
| **Website visitors** | Pixel | High, needs traffic |
| **Customer list upload** | A CSV of phones/emails | ⭐⭐ Highest match value in India |
| **Lead form openers** | Instant Form ads | High intent |

**Set retention to 365 days** for engagement-based audiences at low budget — you want the largest possible pool.

**The customer-list upload is underused in India.** If you have a few hundred customer phone numbers, upload them: use it as an exclusion (stop paying to reach existing customers) and as a lookalike source.

### Lookalike audiences

Finds new people resembling a source audience.

- **1%** = most similar, smallest. Your best prospecting audience
- **5–10%** = broader, less precise
- Source needs roughly **1,000+ people** to work well

**At low budget, lookalikes are usually premature.** You need a decent source audience first, and a separate lookalike ad set splits a budget that can't afford splitting. Build the source now; use lookalikes when you're above ~₹600/day.

### Detailed targeting (interests & behaviours)

**At low budget: leave empty.**

Reasons: Advantage+ treats them as signals anyway; narrow audiences carry a CPM premium; and fewer delivery options means slower learning.

**When to use a few:** genuinely niche products where relevance is non-obvious from creative (specialist equipment, unusual hobbies). Even then, **2–3 broad interests maximum**, never a stack of twelve.

---

## Special Ad Categories — check before you build

If your ad relates to **credit, employment, housing**, or **social issues/elections/politics**, you must declare it. Declaring **removes most targeting options** — age, gender, detailed targeting and radius get restricted, and lookalikes are limited.

**Failing to declare when required risks your ad account.** Declaring when *not* required cripples your targeting for no reason.

Full detail: [`policy-and-special-categories.md`](policy-and-special-categories.md). Read it **before** building if you're in real estate, recruitment, loans, insurance or credit.

---

## Placements

**Advantage+ placements (automatic): ON.** More placements = more auctions = cheaper results.

**The one exception:** [P04 Instagram follower growth](../playbooks/P04-instagram-followers.md), where you restrict to Instagram because a Facebook click can't grow your Instagram.

Worth knowing:
- **Reels and Stories** often carry the cheapest inventory — make 9:16 creative
- **Audience Network** is cheapest but lowest quality. Watch it for app installs especially; exclude it if quality is poor
- Manual placement selection at low budget is almost always self-harm

---

## Audience size guidance

Ads Manager shows an estimated audience size.

| Size | At low budget |
|---|---|
| Under 50,000 | Too narrow. Frequency will spike fast |
| 50,000–500,000 | Workable for tight local targeting |
| 500,000–5 million | **Sweet spot for most** |
| 5 million+ | Fine — Advantage+ handles breadth well |

**Bigger is generally safer at low budget.** With ₹200–500/day you'll never exhaust a large audience, and a large audience gives the algorithm room to find your cheapest converters.

---

## Quick reference

```
LOCATION         your real control. Start tight, widen if starved.
                 "People living in or recently in this location"
LANGUAGE         leave blank — let creative self-select
AGE              widest plausible, e.g. 25-55
GENDER           All, unless genuinely specific
DETAILED         empty at low budget
ADVANTAGE+ AUD   ON, fields empty
PLACEMENTS       Advantage+ ON (except P04)
AUDIENCE SIZE    500k-5M is the sweet spot
BUILD NOW        video-viewer + engager custom audiences, 365-day
CHECK FIRST      Special Ad Category?
```

---

**Related:** [`policy-and-special-categories.md`](policy-and-special-categories.md) · [`creative-specs.md`](creative-specs.md) · [`../playbooks/README.md`](../playbooks/README.md)
