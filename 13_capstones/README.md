# Module 13 — Capstones

> 🧭  [◀ CI/CD & Deployment](../12_cicd/)  ·  [🏠 Course home](../README.md)  ·  [Business AI ▶](../14_business_ai/)

**Goal:** Apply everything from the technical track (NB 01–40) to ship two real-shape projects you can talk about in an interview or a code review.

**Estimated time:** 6–10 hours each if you work them as full projects — the guided run alone is ~75–120 min (Capstone A) and ~90–120 min (Capstone B). Capstone A is mostly analytical; Capstone B is mostly engineering.

**Prerequisites:** Capstone A: Notebooks 1–16 (Modules 1–4: Python, pandas, NumPy, visualization, statistics, scikit-learn). Capstone B: Notebooks 1–40 — especially AI engineering (NB 21–26) and production (NB 39–40).

```
                        The whole course (NB 01–40)
                                    │
             ┌──────────────────────┴──────────────────────┐
             ▼                                             ▼
  Capstone A — Analytics (NB 41)           Capstone B — AI Assistant (NB 42)
  fed by Modules 1–4:                      fed by Modules 6 & 11:
  Python · pandas · NumPy · seaborn ·      prompting · structured output ·
  statistics · scikit-learn                RAG · validation · tracing ·
                                           eval gates · scheduling
             │                                             │
  the *numbers* of a support               the *text* the same support
  operation → one executive summary        operation produces → routed,
                                           answered, costed tickets
             │                                             │
             └──────────────────────┬──────────────────────┘
                                    ▼
                         Two artefacts you can ship.
```

## Capstones at a glance

| # | Notebook | ⏱ Time | Difficulty | Project |
|---|---|---|---|---|
| 41 | `41_capstone_analytics.ipynb` | ~75–120 min | Intermediate | A complete analytical study of an AI support-bot deployment — 5 channels × 12 months of ops data → `groupby` analysis, a 2×2 executive dashboard, a Simpson's-paradox regression, channel clustering, and a 5-bullet executive summary |
| 42 | `42_capstone_ai_assistant.ipynb` | ~90–120 min | Advanced | A complete AI feature — 50 overnight feedback messages classified with structured LLM output, validated, priority-routed, RAG-answered, and shipped as a scheduled daily report with tracing, a cost dashboard, and an eval gate |

## Capstone guides

### 41 · Capstone A: AI-Driven Customer Support Analytics — `41_capstone_analytics.ipynb`

You've just joined a SaaS company that introduced an **AI-powered support bot** at the start of the year. The product manager wants one review document that answers four questions: which channels is the bot working well in, is the automation rate improving over the year, what's the trade-off between bot cost and customer satisfaction, and where should the team invest next? You answer with a small, polished analytical report — using everything from the earlier notebooks (variables, control flow, functions, NumPy, pandas, the pandas/seaborn plotting toolkit, scikit-learn) on one coherent business-AI problem. It's the very same support-ops bot you automated a weekly report for in NB 40: there you made it *run*; here you find out *what it's actually doing*.

The notebook runs on one mental model — **you're a detective building one case file**. The dataset is the crime scene, exploration is dusting for prints, the `groupby`/`pivot_table` work is interviewing witnesses, the 2×2 dashboard is the evidence board, the regression and clustering are forensics, and the executive summary is your closing argument to a jury (the PM, who has 30 seconds). The forensics section springs the course's best statistical trap: the global latency-vs-satisfaction correlation looks damning, but conditioning on channel reveals **Simpson's paradox** — the real lever is moving volume between channels, not shaving milliseconds.

This is the *analytical* version of "shipping a project". The deliverable is a document a manager could read in five minutes and take to a meeting — and the notebook is explicit that the 5-bullet summary *is* the deliverable: everything you compute exists to support it.

**Learning objectives / skills exercised:**
- Build and sanity-check a reproducible dataset (schema, missing values, category balance) before trusting any conclusion
- Answer manager questions with `groupby` / `pivot_table`, plus `apply`-based feature engineering (quarter tags, a bot-economics "health" label)
- Condense a study into a 2×2 executive dashboard (`plt.subplots(2, 2)`) worth pasting into a slide deck
- Test a causal-sounding claim with correlation + regression — and catch Simpson's paradox by conditioning on channel
- Group channels via a distance matrix over their 12-month automation profiles (K-means in the stretch)
- Write a 5-bullet executive summary: one insight per bullet, concrete numbers, actionable

**Structure:**
1. Setup
2. Build the dataset — simulate 5 channels × 12 months (60 rows) of support-ops metrics: tickets, automation, latency, CSAT, cost per ticket
3. Quick exploration — schema, missing values, category balance
4. Automation analysis — 4.1 which channel automates best · 4.2 seasonal grouping (quarter feature via `apply`)
5. Cost and satisfaction analysis — 5.1 a bot-economics classifier (qualitative health labels)
6. The executive dashboard — the 2×2 evidence board
7. A statistical question — does latency hurt satisfaction? (global vs per-channel correlation → Simpson's paradox)
8. Bonus — clustering channels by automation profile (distance matrix)
9. Your turn — write the executive summary (draft yours, then expand the model answer)

**Practice:** milestone-driven rather than checkpoint-driven — there are no ✋ quick-exercise cells. The built-in writing task in §9 comes with a collapsible model summary; then 🧪 **bonus exercises A–C** (add a composite "bot ROI" column; save the final report with `to_csv` and reload it; predict satisfaction with a `RandomForestRegressor` and read the feature importances) and 🧠 **stretch exercises A–B** (K-means clustering of the channel profiles; a month-15 linear projection of automation rates), each with a collapsible 💡 solution. Closes with 8 project takeaways.

**Datasets:** nothing is loaded from disk — §2 *generates* the dataset in-notebook so the capstone is self-contained and reproducible ("in a real project you would load this with `pd.read_csv(...)` from your operations data warehouse"). Each of the 60 rows is one (channel, month) observation:

| Column | Meaning |
|---|---|
| `channel` | one of 5 channels (Email, Chat, Phone, Web Form, Social) |
| `month` / `month_num` | Jan…Dec + 1–12 |
| `tickets_total` / `tickets_auto` | total tickets vs tickets resolved by the bot alone |
| `latency_ms` | median first-response latency |
| `satisfaction` | mean CSAT that month (1–5) |
| `cost_per_ticket` | average cost in USD (mix of LLM + human time) |

**`support_ops_report.csv`** (in this folder) is the committed reference output of bonus exercises A + B: the final enriched table (60 rows = 5 channels × 12 months) including the engineered `quarter`, `health`, `bot_savings`, and `bot_roi` columns.

### 42 · Capstone B: AI Customer-Feedback Assistant — `42_capstone_ai_assistant.ipynb`

The *engineering* twin of NB 41. One concrete artefact carries the whole notebook: an **overnight support inbox** of 50 raw customer messages — refund complaints, bug reports, feature wishes, praise — that has to be turned, by morning, into a PM-ready report. You build the machine that does it: ingest free-form feedback, classify sentiment + topic as structured LLM output, route high-priority items through a small rules engine, ground answers in your own knowledge base via RAG, and produce a daily report that runs on a schedule with cost tracking and an eval guard. These are the *words* behind the *numbers* you analysed in NB 41 — same support operation, the other half of the job.

The mental model here is a **factory assembly line for messages**: Classify is the stamping press, Validate is quality control, the rules engine is the sorting bins, RAG is the instruction-sheet attacher, and the final station packages everything into a report. Two things run alongside the belt — a **trace log** (the factory's CCTV) and an **eval gate** (the safety inspector who can shut the line down before a bad batch ships). The notebook opens with an ASCII architecture diagram that literally *is* the belt, then builds one station per section:

```
raw feedback ──► Classify (LLM, JSON) ──► Validate (schema)
                       │                        │
                       ▼                        ▼
                 Rules engine (priority)   RAG: ground answer in docs
                       └──────────┬─────────────┘
                                  ▼
                        Aggregate + report ──► daily executive summary
                                            └► cost / latency / eval trace
```

The finished artefact is ~250 lines of self-contained Python demonstrating every AI-engineering pattern in the course: a package-shaped `daily_run` function that refuses to ship a regressed prompt, processes all 50 messages end-to-end, computes a cost/latency/accuracy dashboard from its own trace, saves the trace to disk, and emits a five-bullet executive summary to (mock) Slack — the thing you point to in an interview when asked "what AI project have you built?".

**Learning objectives / skills exercised:**
- Combine prompting, RAG, validation, tracing, and scheduling in one end-to-end pipeline
- Classify sentiment + topic as strict JSON, then schema-validate before anything downstream consumes it
- Keep business rules in reviewable code — a plain-`if` priority engine, deliberately separate from the model
- Ground answers in your own knowledge base so the assistant cites your docs instead of inventing answers
- Build a golden eval set and a regression check that gates prompt changes before they ship
- Compute a cost / latency / accuracy dashboard from the trace log and write the 5-bullet PM summary

**Structure:**
1. Setup — the shared mock infrastructure (an inline, deterministic `MockLLM`)
2. The data — 50 incoming feedback messages + a 7-document knowledge base
3. Step 1 — classify with structured output (strict JSON: `sentiment` + `topic`)
4. Step 2 — validate the structured output before it reaches downstream stations
5. Step 3 — the priority rules engine (escalate now / handle today / route to product / acknowledge)
6. Step 4 — RAG for actually answering the question
7. Step 5 — the full pipeline + tracing (every message records labels, priority, tokens, latency)
8. The KPI dashboard — priority mix, cost, latency, sentiment, read back from the trace
9. The executive summary — what a PM actually wants to read
10. The regression check — would tomorrow's prompt change still pass the golden set?
11. Wiring it all together — a single scheduled task (`daily_run`), the night-shift robot from NB 40 running an AI line

**Practice:** milestone-driven, no ✋ quick-exercise cells. 🧪 **Bonus exercises 1–3** (an English-only filter that overrides priority; VIP-customer routing; baking the daily summary into a `report.md` — "trace.csv for engineers, report.md for managers") and 🧠 **stretch exercises A–B** (a daily cost cap that halts the run and fires a Slack alert; VIP messages that always escalate to p0), each with a collapsible 💡 solution. Closes with "What you've built" and five upgrade paths (real provider, embedding retrieval, tool calling, a Streamlit UI, a feedback loop).

**Datasets:** everything lives in-notebook — the 50-message `FEEDBACK` list, the 7-document `KB`, and the 7-example `GOLDEN` eval set. At runtime the scheduled task writes its trace to `/tmp/feedback_reports/trace.csv`. This capstone does **not** use `support_ops_report.csv`.

## How the capstones work

Like every notebook in the course, both capstones run **100% offline**. Capstone A needs only the standard analytics stack (pandas, NumPy, matplotlib/seaborn, scikit-learn) and generates its own data. Capstone B vendors a deterministic inline `MockLLM` — the twin of `MockLLM` from [`llm_providers.py`](../llm_providers.py) (NB 22) — so the whole assembly line runs with no internet and no API key, producing the same output every time; when you want real intelligence, one line swaps in OpenAI, Anthropic, Gemini, or a local Ollama model (see the [LLM Providers Guide](../06_ai_engineering/A1_llm_providers_guide.ipynb)). Unlike the regular lessons, the capstones aren't punctuated by quick-exercise checkpoints: each numbered section is a **milestone** that adds one piece to a single shippable artefact, and the 🧪 bonus and 🧠 stretch exercises at the end extend that artefact — try each one before expanding its collapsible 💡 solution.

If you have the time, do both — A teaches the analytical mindset, B the engineering mindset, and they analyse the same support operation from opposite sides. If you have to pick one, pick the one that matches the job you want next. In an interview, talk through one of these as your "project I built": you wrote the code, and you understand every part.

## Where next

Congratulations — with NB 01–40 plus these two capstones, the core technical track is complete. One module remains, the *practitioner* layer:

- **Module 14 — Business AI in Practice** (`../14_business_ai/`, NB 43–46) — architecture, governance, and the POC → MVP → Production path for landing AI inside a real organisation.

From there, **what you build is up to you**.
