# Policy & Special Ad Categories

> ⚠️ **Meta's policies change and are enforced by automated systems that make mistakes in both directions.** This file is orientation, not legal advice. The authoritative source is Meta's Advertising Policies and your Account Quality page. When in doubt, check there.

**Why this matters more than it seems:** repeated policy violations don't just get ads rejected — they can get your **ad account or Business Manager permanently disabled**, and recovery is slow and often unsuccessful. Treat this as risk management for a business asset.

---

## Special Ad Categories — check this before building anything

If your ad relates to any of these, **you must declare it** at campaign level:

| Category | Covers |
|---|---|
| **Credit** | Loans, credit cards, insurance, BNPL, mortgages, financial products |
| **Employment** | Jobs, recruitment, staffing, internships, professional certification |
| **Housing** | Property sale/rent, real estate listings, home loans, brokerage |
| **Social issues, elections, politics** | Political ads, advocacy, campaigns on debated social topics |

### What declaring costs you

Declaration **removes most of your targeting controls**:

- **Age:** typically locked to 18–65+
- **Gender:** locked to All
- **Detailed targeting:** most interests/behaviours removed
- **Location:** radius targeting restricted — often a minimum ~15 mile / ~25 km radius, and postcode targeting disabled
- **Lookalikes:** replaced by restricted "Special Ad Audiences" or unavailable
- **Custom audiences:** limited

**Plan for materially higher costs.** You've lost the tools that make targeting efficient, so your budget floor rises. Recompute using [`../data/budget-engine.md`](../data/budget-engine.md) with a higher expected CPA.

### The two-sided risk

| Mistake | Consequence |
|---|---|
| **Not declaring when required** | Ads rejected; repeated violations risk permanent account loss |
| **Declaring when not required** | Targeting crippled for no reason; wasted budget |

**If you're unsure, check Meta's current policy page for your specific case rather than guessing.** For Indian real estate and recruitment especially, verify the current requirement before building — the rules have varied by jurisdiction and over time.

**Affected playbooks:** [P02](../playbooks/P02-instant-form-leads-200.md) (loans, jobs, property), [P09](../playbooks/P09-appointment-booking.md) (property site visits), [P03](../playbooks/P03-website-leads.md).

---

## The prohibitions that catch Indian advertisers

### Health, fitness, beauty — the most common cause of rejection

| ❌ Don't | ✅ Do instead |
|---|---|
| Before/after body images | Show your clinic, staff, process |
| "Lose 10 kg in 30 days" | "Personalised fitness plans" |
| "Cures diabetes" | "Consult our specialist" |
| Close-ups implying a flaw | Lifestyle or facility imagery |
| Guaranteed outcomes | Describe the service |
| Targeting that implies a condition | Broad targeting, let creative self-select |

**The reliable workaround: advertise the consultation, not the outcome.** "Free 20-minute skin consultation" is compliant and converts better than a transformation claim. This is the core of [P09](../playbooks/P09-appointment-booking.md).

**Personal attributes rule:** you may not imply you know something personal about the viewer. "Are you overweight?" violates it. "Fitness programmes in Jaipur" doesn't. This trips up health, finance and dating advertisers constantly.

### Other common triggers

| Area | Watch for |
|---|---|
| **Financial services** | Guaranteed returns, unrealistic income claims, unlicensed advice |
| **Education** | Guaranteed admission/placement, fake rankings |
| **Real estate** | Missing RERA details where required, misleading pricing |
| **Supplements** | Health claims, prescription-adjacent products |
| **Tobacco, alcohol, weapons, gambling** | Heavily restricted or prohibited |
| **Adult content** | Prohibited |
| **Misleading claims** | Fake countdowns, fake scarcity, fake reviews |
| **Trademark** | Using brand names/logos you don't own |
| **Sensational imagery** | Shock content, accident imagery |

### Landing page policy applies too
Your **destination** must comply, not just the ad. A compliant ad pointing to a page making health claims still gets rejected. Also: no unexpected redirects, no popups that trap the user, and the page must match the ad's promise.

---

## If your ad is rejected

**Don't resubmit the identical ad repeatedly.** Repeated rejections compound into account-level penalties.

1. **Read the actual reason.** Ads Manager → the ad → rejection notice. It names the policy
2. **Read that policy.** The named policy usually makes the specific problem obvious
3. **Fix the actual issue** — text, image, landing page, or category declaration
4. **Create a new ad** rather than editing and resubmitting the same one
5. **Appeal if you believe it's wrong.** Account Quality → request review. Automated rejections are frequently overturned — a clear, specific, polite appeal often works
6. **Don't try to evade** — misspellings, image text tricks, cloaking. Evasion attempts are treated far more seriously than the original violation

### Account Quality is your dashboard
**business.facebook.com/accountquality** — shows account status, violations, and appeal options. **Check it whenever delivery stops unexpectedly.** A silent delivery halt is often a policy issue rather than a technical one.

---

## Protecting the account

The ad account is a business asset. Losing it can mean losing your Page history, audiences, pixel data and conversion history.

- **2FA on every admin's personal login.** Compromise is a leading cause of loss
- **Never buy or rent ad accounts.** Common in India, and it gets accounts permanently banned
- **Don't share logins** — use Business Manager roles
- **Multiple admins**, so one person's problem isn't fatal
- **Complete business verification** if you're a registered entity
- **Keep payments healthy** — repeated failures can trigger disabling
- **Fix violations promptly** rather than accumulating them
- **Be cautious with agencies** demanding your login rather than Business Manager access

---

## Pre-launch policy check

- [ ] Do I fall into **Credit / Employment / Housing / Social-Political**? If yes, declared?
- [ ] Any before/after imagery? (remove)
- [ ] Any guaranteed outcome or specific result claim? (remove)
- [ ] Does anything imply I know a personal attribute of the viewer? (rewrite)
- [ ] Does my landing page comply, and match the ad?
- [ ] Any fake urgency, fake scarcity, fake reviews? (remove)
- [ ] Any trademark I don't own? (remove)
- [ ] Required disclosures present (RERA, licences)?
- [ ] 2FA on, second admin added?

---

## Quick reference

```
SPECIAL CATEGORIES   Credit · Employment · Housing · Social/Political
                     → declare, expect restricted targeting + higher costs
                     → not declaring when required risks the account
HEALTH/FITNESS       no before/after, no guaranteed outcomes
                     → advertise the CONSULTATION instead
PERSONAL ATTRIBUTES  never imply you know something about the viewer
LANDING PAGE         must comply and must match the ad
IF REJECTED          read reason → fix → NEW ad → appeal if wrong
NEVER                evade, buy accounts, share logins
CHECK                Account Quality when delivery stops
```

---

**Related:** [`targeting-india.md`](targeting-india.md) · [`troubleshooting.md`](troubleshooting.md) · [`../data/verticals-india.md`](../data/verticals-india.md)
