#!/usr/bin/env python3
"""
budget-calculator.py — the Budget Engine, executable.

Turns the maths in data/budget-engine.md and data/best-budget-recommender.md
into something you can run, so nobody has to trust hand arithmetic.

Zero dependencies. Python 3.8+. Nothing leaves your machine.

USAGE
  Interactive:
      python3 budget-calculator.py

  Non-interactive (all in INR except rates):
      python3 budget-calculator.py --revenue 20000 --margin 40 --close-rate 20 \
                                   --event whatsapp --budget 200

  See the reference example from the docs:
      python3 budget-calculator.py --demo

  Just the learning-floor table:
      python3 budget-calculator.py --table

WHY 7.143
  Meta needs roughly 50 optimization events per ad set per 7 days to exit the
  learning phase.  50 / 7 = 7.143 events per day.  So:

      daily budget  >=  7.143 x cost per optimization event

  Rearranged, that is the whole reason "Rs 200/day optimized for Leads" cannot
  exit the learning phase: 200 / 7.143 = Rs 28, and leads do not cost Rs 28.
"""

from __future__ import annotations

import argparse
import math
import sys

# ── Constants from the engine ────────────────────────────────────────────────

EVENTS_PER_WEEK = 50          # Meta's approximate learning-phase threshold
LEARNING_DAYS = 7
FACTOR = EVENTS_PER_WEEK / LEARNING_DAYS          # 7.142857...
DEFAULT_ACQUISITION_SHARE = 30.0                  # % of gross profit to spend
COST_GOAL_MULTIPLE = 5                            # cost-per-result bid rule

# Optimization events: key -> (label, rung, low prior, high prior)
# Priors are deliberately WIDE order-of-magnitude bands for CHOOSING A RUNG.
# They are not predictions. See data/benchmarks-india.md.
EVENTS = {
    "impression":  ("Impressions / Reach",             1, 0.05, 0.30),
    "thruplay":    ("ThruPlay / video view",           2, 1.0,  8.0),
    "landingpage": ("Link click / Landing page view",  3, 4.0,  25.0),
    "whatsapp":    ("WhatsApp conversation started",   4, 20.0, 90.0),
    "instagramdm": ("Instagram Direct conversation",   4, 20.0, 90.0),
    "form":        ("Instant Form lead",               5, 25.0, 150.0),
    "pagelike":    ("Facebook Page like",              2, 2.0,  15.0),
    "profile":     ("Instagram profile visit",         2, 2.0,  15.0),
    "weblead":     ("Website lead (Pixel/CAPI)",       6, 100.0, 500.0),
    "purchase":    ("Purchase",                        7, 300.0, 3000.0),
}

RULE = "─" * 74


# ── Core maths ───────────────────────────────────────────────────────────────

def learning_floor(cost_per_event: float) -> float:
    """Minimum daily budget to reach ~50 events in 7 days.

    Rounded UP: this is a floor, so landing a rupee below it defeats the
    purpose.  Ceiling-rounding is why 7.143 x 45 reports Rs 322, not Rs 321.
    """
    return float(math.ceil(FACTOR * cost_per_event))


def max_viable_cpa(daily_budget: float) -> float:
    """Most expensive event that can still exit learning at this budget."""
    return daily_budget / FACTOR


def affordable_cpl(revenue: float, margin_pct: float,
                   close_rate_pct: float,
                   acquisition_share_pct: float = DEFAULT_ACQUISITION_SHARE) -> dict:
    """What you can afford to pay per lead, from your own unit economics."""
    gross_profit = revenue * (margin_pct / 100.0)
    max_cac = gross_profit * (acquisition_share_pct / 100.0)
    max_cpl = max_cac * (close_rate_pct / 100.0)
    return {
        "gross_profit": gross_profit,
        "max_cac": max_cac,
        "max_cpl": max_cpl,
    }


def band(lo: float, hi: float) -> str:
    """Render a prior band, keeping sub-rupee values legible."""
    def one(v: float) -> str:
        if v < 1:
            return f"{v:.2f}".rstrip("0").rstrip(".")
        return rupees(v).replace("Rs ", "")
    return f"Rs {one(lo)}-{one(hi)}"


def rupees(x: float) -> str:
    """Indian-style grouping: 1,20,000 not 120,000."""
    n = int(round(x))
    s = str(abs(n))
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ",".join(parts) + "," + tail
    return ("-" if n < 0 else "") + "Rs " + s


# ── Output sections ──────────────────────────────────────────────────────────

def print_header() -> None:
    print()
    print("=" * 74)
    print("  META ADS BUDGET CALCULATOR  —  India (INR)")
    print("  Learning floor:  daily budget >= 7.143 x cost per event")
    print("=" * 74)


def print_floor_table() -> None:
    print()
    print("LEARNING-PHASE FLOOR — max CPA that can still exit learning")
    print(RULE)
    print(f"  {'Daily budget':>14}   {'Max CPA':>10}   {'Monthly (30d)':>15}")
    print(RULE)
    for b in (100, 200, 300, 500, 750, 1000, 2000, 5000):
        star = "  <-- Rs 200/day" if b == 200 else ""
        print(f"  {rupees(b):>14}   {rupees(max_viable_cpa(b)):>10}   "
              f"{rupees(b * 30):>15}{star}")
    print(RULE)
    print(f"  Every ad set needs ~{FACTOR:.2f} events/day "
          f"({EVENTS_PER_WEEK} per {LEARNING_DAYS} days).")


def print_rung_ladder(daily_budget: float) -> None:
    print()
    print(f"OPTIMIZATION-EVENT LADDER at {rupees(daily_budget)}/day")
    print(RULE)
    cap = max_viable_cpa(daily_budget)
    print(f"  At {rupees(daily_budget)}/day your event must cost "
          f"<= {rupees(cap)} to exit learning.")
    print(RULE)
    print(f"  {'Rung':<5} {'Event':<32} {'Prior band':>17} {'Verdict':>12}")
    print(RULE)
    for _key, (label, rung, lo, hi) in sorted(
            EVENTS.items(), key=lambda kv: (kv[1][1], kv[1][2])):
        mid = (lo + hi) / 2
        if hi <= cap:
            verdict = "OK"
        elif mid <= cap:
            verdict = "borderline"
        else:
            verdict = "too costly"
        print(f"  {rung:<5} {label:<32} {band(lo, hi):>17} {verdict:>12}")
    print(RULE)
    print("  Priors are WIDE order-of-magnitude bands for CHOOSING A RUNG.")
    print("  They are NOT predictions. Replace with your own Day-7 numbers.")
    print("  Rule: optimize for the highest rung you can hit 50x per week —")
    print("        not the rung you most want.")


def print_recommendation(event_key: str, event_cost: float | None,
                         budget: float | None, econ: dict | None) -> None:
    label, rung, lo, hi = EVENTS[event_key]
    estimated = event_cost is None
    cost = event_cost if event_cost is not None else (lo + hi) / 2

    t2 = learning_floor(cost)
    t3 = 2 * round(t2)

    print()
    print("YOUR BUDGET RECOMMENDATION")
    print(RULE)
    print(f"  Goal event      : {label}  (rung {rung})")
    if estimated:
        print(f"  Cost per event  : {rupees(cost)}   *** ESTIMATED from a wide")
        print(f"                    prior band ({band(lo, hi)}). PROVISIONAL. ***")
    else:
        print(f"  Cost per event  : {rupees(cost)}   (your figure)")
    print()
    print(f"  T2 RECOMMENDED  = 7.143 x {rupees(cost).replace('Rs ', '')}"
          f" = {rupees(t2)}/day   ({rupees(t2 * 30)}/month)")
    print(f"  T3 Optimal      = 2 x T2          = {rupees(t3)}/day   "
          f"({rupees(t3 * 30)}/month)")
    print(RULE)

    if econ:
        print()
        print("  AFFORDABILITY (from your own unit economics)")
        print(f"    Gross profit per customer   = {rupees(econ['gross_profit'])}")
        print(f"    Max cost per acquisition    = {rupees(econ['max_cac'])}")
        print(f"    Max affordable cost/lead    = {rupees(econ['max_cpl'])}")
        if cost <= econ["max_cpl"]:
            head = round(econ["max_cpl"] / cost, 1) if cost else 0
            print(f"    -> Your event cost is WITHIN budget "
                  f"({head}x headroom). Economics work.")
        else:
            print(f"    -> WARNING: event cost {rupees(cost)} EXCEEDS what you")
            print(f"       can afford ({rupees(econ['max_cpl'])}). Fix the offer")
            print("       or margins first. More budget will not fix this.")

    if budget is None:
        return

    print()
    print(f"  YOUR STATED BUDGET: {rupees(budget)}/day")
    print(RULE)
    cap = max_viable_cpa(budget)
    print(f"    Max CPA that exits learning at this budget = {rupees(cap)}")

    if budget >= t2:
        print(f"    STATUS: OK — at or above the {rupees(t2)}/day floor.")
        print("            This ad set can exit the learning phase.")
    else:
        gap = t2 - budget
        print(f"    STATUS: BELOW FLOOR by {rupees(gap)}/day "
              f"({rupees(gap * 30)}/month).")
        print("            This ad set will be LEARNING LIMITED: volatile,")
        print("            inflated cost per result, indefinitely.")
        print()
        print("    FOUR HONEST OPTIONS")
        cheaper = [
            (lbl, r, l, h) for (lbl, r, l, h) in EVENTS.values()
            if (l + h) / 2 <= cap
        ]
        cheaper.sort(key=lambda t: -t[1])
        if cheaper:
            names = ", ".join(f"{lbl}" for lbl, _r, _l, _h in cheaper[:3])
            print(f"    1. Drop a rung — optimize for: {names}")
            print("       Leads then arrive as a by-product. See playbook P07.")
        else:
            print("    1. Drop a rung — even the cheapest events are strained")
            print("       at this budget. See playbook P07.")
        print("    2. Accept learning-limited, built to survive it:")
        print("       one ad set, broad targeting, 3 ads, no edits for 7 days.")
        days = max(1, int(round((budget * 30) / t2)))
        print(f"    3. CONCENTRATE the budget — instead of {rupees(budget)}/day")
        print(f"       for 30 days, spend {rupees(t2)}/day for ~{days} days.")
        print(f"       Same ~{rupees(budget * 30)} total, but this one actually")
        print("       exits learning. Most underused low-budget tactic in India.")
        print(f"    4. Raise to {rupees(t2)}/day — now a number, not a guess.")

    print()
    print("  BID-STRATEGY CONSTRAINT")
    print(f"    Cost-per-result bidding needs daily budget >= "
          f"{COST_GOAL_MULTIPLE}x the target cost.")
    print(f"    At {rupees(budget)}/day your cost goal cannot exceed "
          f"{rupees(budget / COST_GOAL_MULTIPLE)}.")
    print("    At low budget use HIGHEST VOLUME bidding instead (no cost cap).")


def print_next_steps(event_key: str) -> None:
    routes = {
        "whatsapp":    "playbooks/P00-BEST-low-budget-campaign.md  (best low-budget campaign)",
        "instagramdm": "playbooks/P00-BEST-low-budget-campaign.md  (set location = Instagram Direct)",
        "form":        "playbooks/P02-instant-form-leads-200.md",
        "weblead":     "playbooks/P03-website-leads.md",
        "purchase":    "playbooks/P05-ecommerce-sales.md",
        "thruplay":    "playbooks/P07-video-retarget-funnel-200.md  (exits learning at Rs 200/day)",
        "landingpage": "playbooks/P07-video-retarget-funnel-200.md",
        "impression":  "playbooks/P08-engagement-social-proof.md",
        "pagelike":    "playbooks/P13-facebook-page-likes-followers.md  (Facebook-only placements)",
        "profile":     "playbooks/P04-instagram-followers.md  (Instagram-only placements)",
    }
    print()
    print("NEXT STEPS")
    print(RULE)
    print(f"  Playbook : {routes.get(event_key, 'playbooks/README.md')}")
    print("  Then     : run 7 days with NO edits, and on Day 7 recompute")
    print("             using your REAL measured cost per event.")
    print()
    print("  Day 7:   true floor = 7.143 x (your measured cost per event)")
    print("           Your recommendation WILL move. That is the point —")
    print("           the formula is fixed, the input is measured.")
    print()
    print("  Full repo: https://github.com/consecrating/Facebook-Instagram-Ads")


# ── Input handling ───────────────────────────────────────────────────────────

def ask_float(prompt: str, default: float | None = None,
              allow_blank: bool = False) -> float | None:
    while True:
        suffix = f" [{default}]" if default is not None else ""
        raw = input(f"  {prompt}{suffix}: ").strip().replace(",", "")
        if not raw:
            if default is not None:
                return default
            if allow_blank:
                return None
            print("    Please enter a number.")
            continue
        try:
            val = float(raw)
            if val < 0:
                print("    Must be zero or positive.")
                continue
            return val
        except ValueError:
            print("    Not a number — try again.")


def ask_event() -> str:
    keys = sorted(EVENTS, key=lambda k: (EVENTS[k][1], EVENTS[k][2]))
    print()
    print("  What should the ad actually achieve?")
    for i, k in enumerate(keys, 1):
        label, rung, _lo, _hi = EVENTS[k]
        print(f"    {i:>2}. {label}  (rung {rung})")
    while True:
        raw = input(f"  Choose 1-{len(keys)}: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(keys):
            return keys[int(raw) - 1]
        print("    Enter a number from the list.")


def interactive() -> int:
    print_header()
    print()
    print("  Answer what you know. Blank = skip (marked as an assumption).")
    print()
    print("YOUR NUMBERS")
    revenue = ask_float("Revenue from ONE closed customer (Rs)", allow_blank=True)
    econ = None
    if revenue:
        margin = ask_float("Gross margin (%)", default=40.0)
        close = ask_float("Out of 100 enquiries, how many buy? (%)", default=20.0)
        share = ask_float("% of gross profit you'll spend to acquire",
                          default=DEFAULT_ACQUISITION_SHARE)
        econ = affordable_cpl(revenue, margin, close, share)

    event_key = ask_event()
    label, _rung, lo, hi = EVENTS[event_key]
    print()
    print(f"  Do you know your actual cost per {label.lower()}?")
    print(f"  (Blank = use a wide prior band {band(lo, hi)}, "
          "flagged as an estimate)")
    cost = ask_float("Cost per event (Rs)", allow_blank=True)

    print()
    budget = ask_float("Your real daily budget (Rs)", default=200.0)

    print_recommendation(event_key, cost, budget, econ)
    print_rung_ladder(budget)
    print_next_steps(event_key)
    print()
    return 0


def main() -> int:
    p = argparse.ArgumentParser(
        description="Meta ads budget calculator for India (INR).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--revenue", type=float, help="Revenue from one closed customer (Rs)")
    p.add_argument("--margin", type=float, default=40.0, help="Gross margin %% (default 40)")
    p.add_argument("--close-rate", type=float, default=20.0,
                   help="Lead-to-customer close rate %% (default 20)")
    p.add_argument("--acquisition-share", type=float, default=DEFAULT_ACQUISITION_SHARE,
                   help="%% of gross profit spent to acquire (default 30)")
    p.add_argument("--event", choices=sorted(EVENTS), help="Optimization event")
    p.add_argument("--event-cost", type=float,
                   help="Your measured cost per event (Rs). Omit to use a wide prior.")
    p.add_argument("--budget", type=float, help="Your real daily budget (Rs)")
    p.add_argument("--table", action="store_true", help="Print the learning-floor table and exit")
    p.add_argument("--demo", action="store_true",
                   help="Run the reference example from the documentation")
    p.add_argument("--interactive", "-i", action="store_true",
                   help="Force the question-and-answer flow (works with piped input)")
    args = p.parse_args()

    if args.interactive:
        return interactive()

    if args.table:
        print_header()
        print_floor_table()
        print()
        return 0

    if args.demo:
        print_header()
        print()
        print("  DEMO — the reference example from data/best-budget-recommender.md")
        print("  A service business: Rs 20,000 revenue per customer, 40% margin,")
        print("  closes 1 in 5 enquiries, wants WhatsApp enquiries.")
        econ = affordable_cpl(20000, 40, 20, 30)
        print_recommendation("whatsapp", 45.0, 200.0, econ)
        print_rung_ladder(200.0)
        print_next_steps("whatsapp")
        print()
        return 0

    if not args.event or args.budget is None:
        if sys.stdin.isatty():
            return interactive()
        p.print_help()
        print("\nNon-interactive use needs at least --event and --budget.")
        print("Try:  python3 budget-calculator.py --demo")
        return 2

    econ = None
    if args.revenue:
        econ = affordable_cpl(args.revenue, args.margin,
                              args.close_rate, args.acquisition_share)

    print_header()
    print_recommendation(args.event, args.event_cost, args.budget, econ)
    print_rung_ladder(args.budget)
    print_next_steps(args.event)
    print()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print("\nCancelled.")
        sys.exit(130)
