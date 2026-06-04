# 🏎️ Fast Track

The whole curriculum, condensed to its essentials. **9 notebooks. About 10 hours.** A shortcut you can finish in two work weeks of evenings — not a substitute for the full course, but a credible introduction that touches every layer of the stack.

> 🚀 **Start here:** [`00_fast_track_onboarding.ipynb`](./00_fast_track_onboarding.ipynb)

**~7 exercises per notebook, every one with a worked solution.** Every fast-track notebook keeps the canonical Practice exercises (3–5 each) *and* two of the harder Stretch exercises (C + D) — the same two-tier exercise design as the full course, just with the very-deep Stretch A/B and the Bonus mini-project trimmed out so the path stays under ~9 h.

---

## What's here

| # | Notebook | What it teaches | Time |
|---|---|---|---|
| 0 | `00_fast_track_onboarding.ipynb`     | What the fast track is, what's been left out, environment check | ~10 min |
| 1 | `01_python_basics.ipynb`             | Types, casting, f-strings, defensive string handling | ~50 min |
| 2 | `02_control_structures.ipynb`        | if/elif, for/while, comprehensions, early return | ~55 min |
| 3 | `03_lists_and_dicts.ipynb`           | Lists, tuples, sets, dicts, `defaultdict`, `Counter` | ~60 min |
| 4 | `04_functions.ipynb`                 | Functions, default args, `*args/**kwargs`, decorators | ~65 min |
| 5 | `05_classes_basics.ipynb`            | Classes, `__init__`, `self`, methods, `__repr__`, `@dataclass` | ~60 min |
| 6 | `06_pandas_fundamentals.ipynb`       | DataFrames, groupby, merge, missing data, plotting | ~80 min |
| 7 | `07_sklearn_basics.ipynb`            | train/test split, fit/predict, evaluation, pipelines | ~85 min |
| 8 | `08_ai_workflows.ipynb`              | LLM prompting, classification, JSON output, validation | ~65 min |
| 9 | `09_embeddings_and_rag.ipynb`        | Embeddings, cosine similarity, retrieval, basic RAG | ~65 min |
| | **Total** | | **~10 h** |

Each notebook (except the onboarding) is a **trimmed copy** of its canonical counterpart in the parent folders. The first cell of every trimmed notebook links back to the full version.

---

## What's intentionally missing

Compared to the full course, these are gone:

- **🧠 Stretch exercises A and B** (the very-deep problems) — the fast track keeps Stretch C and D, which are still notably harder than the Practice ones but realistic for the time budget.
- **🎁 Bonus mini-project** at the end of every notebook.
- **`04_dictionaries_advanced.ipynb`** — merged into the fast-track NB 3.
- **APIs / HTTP / SQL** — these matter once you have a real I/O task; defer them.
- **NumPy / matplotlib / statistics / time series** — pandas covers ~80 % of what beginners need to read code.
- **Model evaluation, feature engineering, tools & agents, document processing, AI evaluation, production wiring** — defer these to the full course when you need the depth.
- **Both capstones**, **Module 10's industry applications** (churn value, fraud, segmentation, forecasting), and **all 11 optional appendices**.

The full course is at the parent level — entry point: `../00_onboarding/00_master_onboarding.ipynb`.

---

## When to switch to the full course

Three good signals:

1. **You want interview prep.** The full course has 88 Stretch exercises (A–D in every notebook) that are deliberately interview-grade. None of those are here.
2. **You want to ship code.** The full course's Module 6 covers packaging, scheduling, and config & secrets — none of which is here.
3. **You're curious about a specific topic.** The full course has dedicated notebooks on NumPy, matplotlib, statistics, time-series forecasting, agents, document processing, and AI evaluation. Pick the one that matters for your work.

---

## Setup

Same dependencies as the full course:

```bash
pip install -r ../requirements.txt
```

You don't need anything extra — the `llm_providers.py` shim at the repo root means the AI notebooks (NB 8 and 9) run offline by default with the built-in `MockLLM`.

---

## How notebooks here relate to the canonical course

```
fast_track/                    canonical full course
  01_python_basics      ←  01_foundations/01_python_basics
  02_control_structures ←  01_foundations/02_control_structures
  03_lists_and_dicts    ←  01_foundations/03_lists_data_structures
  04_functions          ←  01_foundations/05_functions_modules
  05_classes_basics     ←  01_foundations/06_classes_and_oop
  06_pandas_fundamentals←  02_data_science/07_pandas_fundamentals
  07_sklearn_basics     ←  04_machine_learning/14_sklearn_basics
  08_ai_workflows       ←  05_ai_engineering/17_ai_workflows
  09_embeddings_and_rag ←  05_ai_engineering/18_embeddings_retrieval
```

The fast-track notebooks are flat-numbered 1–9 deliberately — when there are only nine things in front of you, finishing feels achievable. Inside each notebook the cross-references still use the canonical NB numbers (e.g. *"in NB 8 with NumPy"*), so you can always follow a thread back to the depth notebook.
