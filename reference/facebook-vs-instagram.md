# Facebook vs Instagram — Settings Per Goal

Both platforms run from the same Ads Manager, but the **settings differ per goal**. This file gives the exact configuration for each of the four goals people actually want, on each platform.

---

## The default rule, and its three exceptions

**Default: leave Advantage+ placements ON.** Meta serves your ad wherever it's cheapest across Facebook and Instagram, which lowers your cost per result. At low budget this is almost always right.

**Three exceptions — restrict placements manually:**

| Goal | Restrict to | Why |
|---|---|---|
| Facebook Page likes/followers ([P13](../playbooks/P13-facebook-page-likes-followers.md)) | **Facebook only** | An Instagram impression can't grow your Facebook Page |
| Instagram followers ([P04](../playbooks/P04-instagram-followers.md)) | **Instagram only** | A Facebook click can't grow your Instagram |
| Platform-specific creative | The matching platform | 9:16 Reels creative shouldn't run in a Facebook right-column slot |

**For everything else — WhatsApp enquiries, leads, sales, footfall — keep both platforms on.** Splitting Facebook and Instagram into separate ad sets at low budget starves both. One ad set across both beats two ad sets at half budget each.

---

## GOAL 1 — Followers

### Facebook Page followers → [P13](../playbooks/P13-facebook-page-likes-followers.md)

```
Objective:          Engagement
Conversion location: On your Page
Performance goal:   Maximise number of Page likes
Placements:         MANUAL → Facebook only
                    (Facebook Feed, Facebook Reels, Facebook Stories,
                     Video Feeds, Marketplace)
Budget:             ₹100-200/day — cheap event, ₹200 comfortably exits learning
CTA:                Like Page / Follow Page
Advantage+ Audience: ON, 2-3 interest signals allowed here
```

**Facebook-specific note:** *like* and *follow* are now separate. You can only optimize for **likes**, but **follows** determine who sees your posts. Track both; expect them to diverge.

### Instagram followers → [P04](../playbooks/P04-instagram-followers.md)

```
Objective:          Engagement
Performance goal:   Instagram profile visits  (if available)
                    else Post engagement
Placements:         MANUAL → Instagram only
                    (IG Feed, IG Reels, IG Stories, IG Explore)
Budget:             ₹200/day works
Creative:           Your best ORGANIC post, Reels 9:16
Advantage+ Audience: ON, 2-3 interest signals allowed
```

**Instagram-specific note:** there is **no "get followers" optimization event.** Profile visits is the closest proxy — you pay for visits, and your *profile* converts them. Half this job is off-platform: bio, pinned posts, grid consistency.

### Honest comparison

| | Facebook | Instagram |
|---|---|---|
| Cost per follower (India) | Usually cheaper | Usually higher |
| Organic reach to followers | Very low | Better, especially Reels |
| Audience skew | Older, Tier-2/3 strong | Younger, metro-heavy |
| Best for | Local services, credibility | Creators, visual products, retail |

> **Both are weak purchases unless you monetise the audience.** The real value of either is the **retargetable custom audience** you build, not the follower count. If you want customers rather than an audience, run [P00](../playbooks/P00-BEST-low-budget-campaign.md).

---

## GOAL 2 — Likes & Engagement

**"Likes" is not a business outcome.** It's useful for exactly two things: social proof on ads you'll reuse, and building a retargetable audience. Time-box it to 2–4 weeks.

### Post likes/engagement (both platforms) → [P08](../playbooks/P08-engagement-social-proof.md)

```
Objective:          Engagement
Conversion location: On your post
Performance goal:   Maximise engagement
Placements:         Advantage+ ON  (both platforms — you want cheap engagement)
Budget:             ₹100-200/day
Creative:           Genuinely useful content, NOT promotion
Duration:           2-4 weeks, then stop
```

### The mechanic most people miss

**Use the same Post ID across campaigns so engagement compounds onto one asset.**

1. Publish the post on your Page
2. Note its **Post ID**
3. In every future ad: **Use existing post → Enter post ID**

All likes, comments and shares accumulate on that single post. Your later lead campaign then launches already looking established, instead of showing 0 likes.

**Facebook-specific:** the Post ID mechanic works cleanly here.
**Instagram-specific:** select the existing Instagram post in the ad; engagement accrues to the real post, which also helps organically.

---

## GOAL 3 — WhatsApp Enquiries

**Runs on both platforms from one ad set. Don't split.** → [P00](../playbooks/P00-BEST-low-budget-campaign.md) · [P01](../playbooks/P01-whatsapp-leads-200.md)

```
Objective:           Engagement          ← NOT "Leads"
Conversion location: WhatsApp
Performance goal:    Maximise number of conversations
Placements:          Advantage+ ON  (Facebook + Instagram both)
Budget:              7.143 × cost per conversation (~₹325 typical)
Bid:                 Highest volume — no cost cap
Advantage+ Audience: ON, fields EMPTY
CTA:                 Send WhatsApp Message
Pre-fill:            "Hi! I'm interested in [SERVICE]. Please share
                      details and pricing."
```

**Requirement:** WhatsApp Business number connected to your Facebook Page, and verified visible in the Ads Manager dropdown → [`../setup/04-whatsapp-business.md`](../setup/04-whatsapp-business.md)

### Platform differences worth knowing

| | Facebook | Instagram |
|---|---|---|
| WhatsApp CTA support | ✅ Yes | ✅ Yes |
| Typical enquiry volume in India | Often higher | Often higher intent |
| Where it shows | Feed, Reels, Stories, Marketplace | Feed, Reels, Stories, Explore |

**Instagram-specific:** Instagram Direct is a separate conversion location from WhatsApp. If you'd rather receive Instagram DMs than WhatsApp messages, set **Conversion location = Instagram Direct**. WhatsApp is usually better in India — it's where follow-up actually happens, and you keep the contact.

**Facebook-specific:** Messenger is also available as a conversion location. WhatsApp generally outperforms Messenger in India.

> **Attribution tip:** vary the pre-filled message per ad so you can tell which creative and platform produced which enquiry. Free attribution, no tooling needed.

---

## GOAL 4 — Lead Generation

Three routes. Pick by what you have.

### 4a — Instant Forms (no website needed) → [P02](../playbooks/P02-instant-form-leads-200.md)

```
Objective:           Leads
Conversion location: Instant forms
Performance goal:    Maximise number of leads
Placements:          Advantage+ ON (both platforms)
Form type:           Higher intent  (at low budget)
Fields:              Name + Phone + 1 multiple-choice qualifier
Budget:              7.143 × cost per lead (~₹300-700/day floor)
Required:            privacy policy URL
```

**Facebook-specific:** forms pre-fill from the Facebook profile — high completion rates.
**Instagram-specific:** Instant Forms work on Instagram too, but pre-fill can be less complete, so **keep the form shorter for Instagram traffic**. Fewer fields matters more here.

### 4b — WhatsApp as lead gen → [P00](../playbooks/P00-BEST-low-budget-campaign.md)

For most Indian businesses this **outperforms Instant Forms** — reported 30–50% lower CPL and warmer leads. See Goal 3 above.

### 4c — Website leads (needs Pixel) → [P03](../playbooks/P03-website-leads.md)

```
Objective:           Leads
Conversion location: Website
Conversion event:    Lead
Placements:          Advantage+ ON
Budget:              7.143 × CPL — usually ₹1,500+/day
Required:            Pixel + verified Lead event
```

⚠️ **Not viable under ~₹1,500/day.** Website leads cost too much to hit 50 events/week on a small budget. Use 4a or 4b instead.

### Which lead route?

| You have | Use |
|---|---|
| WhatsApp + can reply fast | **4b** ⭐ best for India |
| No website, need structured data | 4a |
| Website + Pixel + ₹1,500+/day | 4c |
| Can't reply within minutes | 4a with slower follow-up, or reconsider |

---

## Creative, per platform

| | Facebook | Instagram |
|---|---|---|
| Feed ratio | 4:5 (1080×1350) | 4:5 or 1:1 |
| Reels/Stories | 9:16 (1080×1920) | 9:16 — **highest priority on IG** |
| Copy length | Tolerates longer | Keep short; visual carries it |
| Text on image | Keep minimal | Keep minimal |
| Captions on video | Essential | Essential |
| Polish level | Authentic wins | Authentic wins, Reels especially |

**Upload a separate 9:16 asset rather than letting a 4:5 be auto-cropped.** Ads Manager allows per-placement assets — a cropped landscape image in a Reels slot looks amateurish and performs like it.

---

## Master settings matrix

| Goal | Objective | Conversion location | Performance goal | Placements | ₹200/day? |
|---|---|---|---|---|---|
| FB followers | Engagement | On your Page | Page likes | **FB only** | ✅ |
| IG followers | Engagement | — | IG profile visits | **IG only** | ✅ |
| Likes/engagement | Engagement | On your post | Engagement | Advantage+ | ✅ |
| WhatsApp enquiry | Engagement | **WhatsApp** | Conversations | Advantage+ | ⚠️ limited |
| Instagram DMs | Engagement | Instagram Direct | Conversations | Advantage+ | ⚠️ limited |
| Form leads | Leads | Instant forms | Leads | Advantage+ | ⚠️ limited |
| Website leads | Leads | Website | Lead event | Advantage+ | ❌ |
| Sales | Sales | Website | Purchase | Advantage+ | ❌ |
| Footfall | Engagement | WhatsApp | Conversations | Advantage+ | ✅ |

**Legend:** ✅ exits learning · ⚠️ runs but Learning Limited · ❌ needs materially more budget

Always compute your own floor: `daily budget ≥ 7.143 × cost per event` → [`../data/budget-engine.md`](../data/budget-engine.md)

---

## The five things people get wrong

1. **Splitting Facebook and Instagram into separate ad sets at low budget.** Halves the learning signal for both. One ad set, both platforms
2. **Forgetting to restrict placements for follower campaigns.** Paying for Instagram impressions while trying to grow a Facebook Page
3. **Choosing "Leads" objective for WhatsApp.** WhatsApp lives under **Engagement**
4. **Only uploading a 4:5 asset.** You lose Reels and Stories — the cheapest inventory on both platforms
5. **Buying followers or likes with no plan to monetise them.** The audience is the asset; the count is not

---

**Related:** [`../playbooks/README.md`](../playbooks/README.md) · [`creative-specs.md`](creative-specs.md) · [`targeting-india.md`](targeting-india.md) · [`../data/budget-engine.md`](../data/budget-engine.md)
