# tools/

## budget-calculator.py

The [Budget Engine](../data/budget-engine.md), executable. Zero dependencies, Python 3.8+, stdlib only. Nothing leaves your machine — no network calls, no data collection.

**Why it exists:** the core recommendation is `daily budget ≥ 7.143 × cost per event`. That's simple arithmetic, but it's arithmetic people get wrong or skip. This makes it runnable and checkable.

### Usage

```bash
# Question-and-answer flow
python3 tools/budget-calculator.py

# The reference example from the docs
python3 tools/budget-calculator.py --demo

# Just the learning-floor table
python3 tools/budget-calculator.py --table

# Everything on the command line
python3 tools/budget-calculator.py \
  --revenue 1800 --margin 55 --close-rate 40 \
  --event whatsapp --event-cost 45 --budget 200

# Force the Q&A flow even with piped input
python3 tools/budget-calculator.py --interactive
```

### Options

| Flag | Meaning |
|---|---|
| `--revenue` | Revenue from one closed customer (₹) |
| `--margin` | Gross margin % (default 40) |
| `--close-rate` | Lead → customer close rate % (default 20) |
| `--acquisition-share` | % of gross profit you'll spend to acquire (default 30) |
| `--event` | Optimization event — see list below |
| `--event-cost` | Your **measured** cost per event (₹). Omit and it uses a wide prior, clearly flagged as an estimate |
| `--budget` | Your real daily budget (₹) |
| `--table` | Print the learning-floor table and exit |
| `--demo` | Run the documented reference example |
| `--interactive`, `-i` | Force the Q&A flow |

### Events

`impression` · `thruplay` · `pagelike` · `profile` · `landingpage` · `whatsapp` · `instagramdm` · `form` · `weblead` · `purchase`

### What it tells you

- **T2 recommended** daily budget = `7.143 × cost per event`, and T3 optimal = `2 × T2`
- **Affordable cost per lead** from your own unit economics, with a warning if your event costs more than you can afford
- **Whether your stated budget clears the floor** — and if not, the four honest options including budget concentration
- **The optimization-event ladder** at your budget, marking each rung OK / borderline / too costly
- **The cost-per-result bid constraint** (daily budget must be ≥ 5× your target cost)
- **Which playbook to open next**

### A note on the numbers

If you don't pass `--event-cost`, the tool uses a **wide order-of-magnitude prior** and labels the result `*** ESTIMATED ... PROVISIONAL ***`. That is deliberate. There is no reliable published per-vertical cost-per-lead data for India in INR — see [`../data/benchmarks-india.md`](../data/benchmarks-india.md). Priors are for **choosing a rung**, not predicting your cost.

**Run it again on Day 7 with your real measured cost.** The recommendation will move. That's the design: the formula is fixed, the input is measured.

### Why the floor rounds up

`learning_floor()` uses `math.ceil`. A floor that rounds down isn't a floor. This is why `7.143 × 45` reports **₹322**, not ₹321.

---

**Related:** [`../data/budget-engine.md`](../data/budget-engine.md) · [`../data/best-budget-recommender.md`](../data/best-budget-recommender.md) · [`../examples/worked-example-end-to-end.md`](../examples/worked-example-end-to-end.md)

---

## test-calculator.py

A regression suite for the calculator. No dependencies.

```bash
python3 tools/test-calculator.py
```

30 checks across four groups:

| Group | What it guards |
|---|---|
| Behaviour + documented figures | The calculator still produces the exact numbers printed in the docs (₹322, ₹415, ₹429, ₹1,786, ₹6,429) |
| Exit codes | Invalid input fails cleanly rather than silently |
| Independent arithmetic | The maths re-derived from scratch, not read back from the code |
| Doc / code consistency | The headline figures actually appear in `budget-engine.md`, `best-budget-recommender.md`, the worked example, P00, README and ONE-FILE |

**The last group is the important one.** If someone edits the engine and the ₹322 floor in the docs quietly becomes ₹321, this suite fails. Docs and code can't drift apart without something going red.

Run it after any change to the engine or to the documented examples.
