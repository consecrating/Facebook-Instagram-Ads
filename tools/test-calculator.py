#!/usr/bin/env python3
"""
test-calculator.py — regression suite for budget-calculator.py

Guards two things:
  1. The calculator behaves correctly (exit codes, flags, routing).
  2. The calculator's output still MATCHES THE DOCUMENTED FIGURES.

That second point is the important one.  If someone edits the engine and the
Rs 322 floor in data/best-budget-recommender.md silently becomes Rs 321, this
suite fails.  Docs and code cannot drift apart quietly.

Run:
    python3 tools/test-calculator.py

Exits 0 if everything passes, 1 otherwise.  No dependencies.
"""

from __future__ import annotations

import math
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
CALC = HERE / "budget-calculator.py"
REPO = HERE.parent

FACTOR = 50 / 7


def run(args: list[str]) -> tuple[int, str]:
    r = subprocess.run([sys.executable, str(CALC)] + args,
                       capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


# ── Behaviour + documented-figure checks ─────────────────────────────────────

CASES: list[tuple[str, list[str], list[str]]] = [
    # name, args, substrings that MUST appear
    ("--demo reproduces documented T2/T3",
     ["--demo"], ["Rs 322/day", "Rs 644/day", "Rs 480", "Rs 28"]),

    ("--table matches documented floor table",
     ["--table"], ["Rs 14", "Rs 28", "Rs 42", "Rs 70",
                   "Rs 105", "Rs 140", "Rs 280", "Rs 700"]),

    ("worked example, Day 0 (Rs45 estimate)",
     ["--revenue", "1800", "--margin", "55", "--close-rate", "40",
      "--event", "whatsapp", "--event-cost", "45", "--budget", "200"],
     ["Rs 322/day", "Rs 119", "BELOW FLOOR by Rs 122", "~19 days"]),

    ("worked example, Day 7 recompute (Rs58 actual)",
     ["--revenue", "1800", "--margin", "55", "--close-rate", "40",
      "--event", "whatsapp", "--event-cost", "58", "--budget", "200"],
     ["Rs 415/day", "Rs 12,450/month"]),

    ("budget above floor reports OK",
     ["--event", "whatsapp", "--event-cost", "45", "--budget", "400"],
     ["STATUS: OK"]),

    ("unaffordable economics warn",
     ["--revenue", "500", "--margin", "20", "--close-rate", "10",
      "--event", "weblead", "--event-cost", "250", "--budget", "200"],
     ["WARNING"]),

    ("omitted event cost is flagged provisional",
     ["--event", "form", "--budget", "200"], ["ESTIMATED", "PROVISIONAL"]),

    ("purchase floor matches docs (Rs6,429)",
     ["--event", "purchase", "--event-cost", "900", "--budget", "200"],
     ["Rs 6,429/day"]),

    ("website lead floor matches docs (Rs1,786)",
     ["--event", "weblead", "--event-cost", "250", "--budget", "200"],
     ["Rs 1,786/day"]),

    ("form lead floor matches docs (Rs429)",
     ["--event", "form", "--event-cost", "60", "--budget", "200"],
     ["Rs 429/day"]),

    ("pagelike routes to P13",
     ["--event", "pagelike", "--budget", "200"],
     ["P13-facebook-page-likes-followers"]),

    ("profile routes to P04",
     ["--event", "profile", "--budget", "200"], ["P04-instagram-followers"]),

    ("thruplay routes to P07",
     ["--event", "thruplay", "--budget", "200"], ["P07-video-retarget-funnel"]),

    ("whatsapp routes to P00",
     ["--event", "whatsapp", "--budget", "200"], ["P00-BEST-low-budget-campaign"]),

    ("sub-rupee prior band stays readable",
     ["--event", "thruplay", "--budget", "200"], ["Rs 0.05-0.3"]),

    ("zero budget does not crash",
     ["--event", "thruplay", "--budget", "0"], ["OPTIMIZATION-EVENT LADDER"]),

    ("cost-goal 5x constraint shown",
     ["--event", "whatsapp", "--event-cost", "45", "--budget", "200"],
     ["cannot exceed Rs 40"]),
]

EXIT_CASES: list[tuple[str, list[str], int]] = [
    ("invalid event exits 2", ["--event", "nonsense", "--budget", "200"], 2),
    ("--demo exits 0", ["--demo"], 0),
    ("--table exits 0", ["--table"], 0),
]


def check_docs_consistency() -> list[str]:
    """The engine's headline figures must appear in the docs, verbatim."""
    problems = []
    expectations = [
        ("data/budget-engine.md",            ["7.143", "₹28"]),
        ("data/best-budget-recommender.md",  ["7.143", "₹322", "₹644"]),
        ("examples/worked-example-end-to-end.md",
                                             ["₹322", "₹415", "₹119", "₹28"]),
        ("playbooks/P00-BEST-low-budget-campaign.md", ["7.143"]),
        ("README.md",                        ["7.143", "₹28"]),
        ("ONE-FILE.md",                      ["7.143", "₹28"]),
    ]
    for rel, needles in expectations:
        p = REPO / rel
        if not p.exists():
            problems.append(f"missing file: {rel}")
            continue
        txt = p.read_text(encoding="utf-8")
        for n in needles:
            if n not in txt:
                problems.append(f"{rel}: expected to contain {n!r}")
    return problems


def main() -> int:
    fails = 0

    print("BEHAVIOUR + DOCUMENTED FIGURES")
    for name, args, expects in CASES:
        code, out = run(args)
        missing = [e for e in expects if e not in out]
        ok = code == 0 and not missing
        fails += 0 if ok else 1
        extra = f"   missing={missing}" if missing else (
            f"   exit={code}" if code else "")
        print(f"  {'PASS' if ok else 'FAIL'}  {name}{extra}")

    print("\nEXIT CODES")
    for name, args, want in EXIT_CASES:
        code, _ = run(args)
        ok = code == want
        fails += 0 if ok else 1
        print(f"  {'PASS' if ok else 'FAIL'}  {name} (got {code}, want {want})")

    print("\nINDEPENDENT ARITHMETIC")
    maths = [
        ("ceil(7.143 x 45) == 322", math.ceil(FACTOR * 45) == 322),
        ("ceil(7.143 x 58) == 415", math.ceil(FACTOR * 58) == 415),
        ("ceil(7.143 x 60) == 429", math.ceil(FACTOR * 60) == 429),
        ("ceil(7.143 x 250) == 1786", math.ceil(FACTOR * 250) == 1786),
        ("ceil(7.143 x 900) == 6429", math.ceil(FACTOR * 900) == 6429),
        ("200 / 7.143 == 28", round(200 / FACTOR) == 28),
        ("1000 / 7.143 == 140", round(1000 / FACTOR) == 140),
        ("1800 x .55 x .30 x .40 == 119", round(1800 * .55 * .30 * .40) == 119),
        ("20000 x .40 x .30 x .20 == 480", round(20000 * .40 * .30 * .20) == 480),
    ]
    for label, ok in maths:
        fails += 0 if ok else 1
        print(f"  {'PASS' if ok else 'FAIL'}  {label}")

    print("\nDOC / CODE CONSISTENCY")
    problems = check_docs_consistency()
    if problems:
        fails += len(problems)
        for p in problems:
            print(f"  FAIL  {p}")
    else:
        print("  PASS  headline figures present in all key documents")

    print(f"\n{'ALL PASS' if fails == 0 else str(fails) + ' FAILURE(S)'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
