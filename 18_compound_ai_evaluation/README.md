# Module 18 — Compound AI Evaluation with CAFE (optional)

> 🧭  [◀ Django](../17_django/)  ·  [🏠 Course home](../README.md)  ·  [Containers & Docker ▶](../19_containers_docker/)

**Goal:** Learn to answer the question every AI team eventually faces: *we changed the pipeline and quality moved — **which change actually did it, and is the difference real?*** The tool for that question is a century of **design of experiments** (factorial designs, replication, mixed-effects models) pointed at compound AI systems — and **[CAFE](https://github.com/fabian-lu/Cafe)** (*Compound-AI Factorial Evaluation*, [cafe-ai.de](https://cafe-ai.de)), the open-source library that packages the whole workflow: factorial designs over your pipeline's knobs, an LLM-judge layer, scale-correct statistical attribution, cost/quality Pareto frontiers, and a self-hostable web platform.

**Estimated time:** 1.5–2 hours for the lesson notebook, plus 60–75 minutes for the hands-on lab.

**Prerequisites:** Module 8 — especially NB 32 (evaluation & observability: golden datasets, LLM-as-judge) and NB 29 (retrieval). The statistics (ANOVA, p-values, effect sizes) are introduced from scratch, but NB 10's statistics primer makes them land faster. Module 16's Meridian company returns as the running example.

```
      "We shipped a bigger model + retrieval + a new prompt.
                    Quality went up."
                          │
                          ▼        ┌─ the attribution problem ─┐
      Which change did it?  ───────┤  confounded comparison:    │
      Was it worth 5× the cost?    │  3 knobs turned at once    │
                          │        └────────────────────────────┘
                          ▼
      ┌──────────────────────────────────────────────────────────┐
      │   NB 53 — the factorial-evaluation workflow, by hand      │
      │                                                           │
      │   factors & levels  →  full factorial design (2×2×2)      │
      │   → run every config with replication (480 judged runs)   │
      │   → rubric judge (0–3)  →  ANOVA: p-values + partial η²   │
      │   → interactions & mixed-effects  →  Pareto frontier      │
      │   → the same study in a few lines of CAFE                 │
      └──────────────────────────────────────────────────────────┘
```

## A one-minute primer: design of experiments & factorial design

**Design of experiments (DoE)** is a ~100-year-old branch of statistics — it grew out of R. A. Fisher's agricultural field trials in the 1920s — for a deceptively hard problem: *when several things can affect an outcome, how do you change them so you can tell what each one actually did?* The naïve approach, **one factor at a time** (hold everything fixed, wiggle a single knob, repeat), is both wasteful and blind — it needs many runs and it can never reveal that two knobs only help *together*. DoE changes the inputs **deliberately and simultaneously** so that each effect can be estimated cleanly, with fewer runs, and separated from random noise.

The workhorse layout is the **factorial design**: choose your **factors** (the knobs), the **levels** each factor can take, and then test **every combination** of levels — the *full factorial*. Three factors at two levels each is a 2×2×2 = **8-configuration** grid. Because every factor is varied against every setting of the others, you can measure:

- **Main effects** — how much each factor moves the outcome on its own, and
- **Interactions** — whether factors combine (e.g. retrieval helps *only* with the bigger model) — which one-factor-at-a-time testing structurally cannot see.

Add **replication** (running each configuration several times) and statistics can then tell you whether a difference is **real** (significance, p-values) or **big** (effect sizes) rather than just run-to-run noise.

**Why this fits compound AI.** A modern AI pipeline is a stack of knobs — model, retrieval, prompt, temperature, re-ranking — and teams routinely flip several at once, then read a single before/after score that can't attribute the change. Treat the knobs as factors, run the factorial with replication against an LLM judge, and you get a principled answer to *which change moved quality, is it real, and was it worth the cost* — which is exactly the workflow NB 53 builds by hand and CAFE packages.

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll learn |
|---|---|---|---|---|
| 53 | `53_compound_ai_evaluation_cafe.ipynb` | ~1.5 h | Intermediate–Advanced | The attribution problem, factors/levels/configurations, replication vs LLM noise, ANOVA with interactions and effect sizes, ordinal-rubric caveats (CLMM), cost/quality Pareto frontiers, and the CAFE library |
| Lab 01 | `lab01_factorial_capstone_eval.ipynb` | 60–75 min | Intermediate–Advanced | Hands-on: run the full factorial-evaluation loop on the Module 15 capstone assistant — design, replication, ANOVA attribution, Pareto frontier, ship decision |

## Notebook guide

### 53 · Compound AI Evaluation with CAFE — `53_compound_ai_evaluation_cafe.ipynb`

The lesson opens where NB 32 left off: the smoke detector tells you *that* quality moved, not *why*. Meridian (the fictional SaaS company from Module 16) has "improved" its support bot with three changes in one release — bigger model, keyword retrieval, rewritten prompt — and the CFO wants to know whether the 5×-more-expensive model contributed anything at all.

The notebook builds the entire answer **by hand, 100% offline** on a mock compound pipeline (the course's usual MockLLM pattern): enumerate the 2×2×2 factor grid with `itertools.product`, run all 8 configurations over a golden set with 6 replications, judge every answer on a 0–3 rubric, then attribute the variance with `statsmodels` — ANOVA F-tests, partial η² effect sizes, a significant retrieval×model interaction, and a mixed-effects upgrade with a per-question random effect. A cost column turns the same data into a **Pareto frontier** that answers the CFO's question in one chart. The closing section maps every hand-rolled piece onto its **CAFE** counterpart and expresses the same study in a few lines of library code (optional install: Python ≥ 3.11 + R for the scale-correct CLMM/logistic models), plus guidance on fractional factorial designs for when the grid explodes.

**Learning objectives:**
- Explain the attribution problem in compound AI systems and why before/after benchmark scores can't solve it
- Turn pipeline knobs into factors and enumerate a full factorial design
- Justify replication as the defence against LLM run-to-run noise, and demonstrate single-run winner instability on data
- Fit and read an ANOVA with blocking and interaction terms: p-values ("is it real?") and partial η² ("how big?")
- State why an ordinal rubric calls for a cumulative-link mixed model, and which tool fits it for you
- Compute a cost/quality Pareto frontier and use it to kill dominated configurations
- Set up the same study in CAFE with techniques, rubrics, judges, and replications

**Sections:**
1. The attribution problem — "it got better" is not a measurement
2. Factors, levels, configurations — the vocabulary
3. The system under test — a mock compound pipeline
4. The judge — scoring answers on a rubric
5. Replication — running the study
6. Attribution — ANOVA, effect sizes, interactions, mixed-effects
7. Cost/quality trade-offs — the Pareto frontier
8. Doing it for real — CAFE (install, the study in library code, fractional designs)

Plus the standard course closing: 🧪 practice exercises (including a 🐞 debug-me on outcome-conditioning bias), 🧠 stretch exercises A–D, a 🎁 bonus mini-project (a full CAFE study on a real pipeline), and the ✅ self-assessment.

## Hands-on lab

The lesson explains the method; the **lab notebook** makes you run it end-to-end on something you built yourself — the AI Customer-Feedback Assistant from the Module 15 capstone (`../15_capstones/48_capstone_ai_assistant.ipynb`). Like every notebook in this module it runs **100% offline** (deterministic seeded mocks, no API keys), so you can watch every moving part of a factorial study in slow motion before pointing the machinery at a real provider.

| Notebook | ⏱ Time | Companion lesson | What you do |
|---|---|---|---|
| [`lab01_factorial_capstone_eval.ipynb`](lab01_factorial_capstone_eval.ipynb) | 60–75 min | NB 53 | Rebuild the capstone's feedback-assistant pipeline in compact form, turn three upgrade proposals into a 2×2×2 factorial (`prompt_style` × `retrieval_k` × `model_tier`), run 800 judged runs with replication, demonstrate single-run winner instability on your own data, attribute quality with ANOVA + partial η² (including a retrieval×tier interaction), build the cost/quality Pareto frontier, and issue an evidence-backed ship decision — closing with the same study expressed as CAFE config |

The lab embeds ✋ quick checkpoints, 🧪 practice exercises (including a 🐞 debug-me on pseudo-replication), and a 🎁 mini-project (a two-metric study of the whole pipeline), in the same style as the numbered course lessons.

## Installing CAFE (optional)

Both notebooks (lesson and lab) run end-to-end **without** CAFE — the library sections are guarded and skip gracefully. To run the real thing:

```bash
git clone https://github.com/fabian-lu/Cafe.git && cd Cafe
pip install -e "packages/cafe-core[all]"
# macOS: brew install r        Debian/Ubuntu: sudo apt install r-base
Rscript -e 'install.packages(c("ordinal", "lme4"))'
cafe doctor          # verify Python + R + LLM access
cafe run example     # bundled toy study — no API keys needed
```

CAFE requires **Python ≥ 3.11** and **R** (the ordinal/logistic mixed models run through R's `ordinal` and `lme4` packages).

## The web platform & [cafe-ai.de](https://cafe-ai.de)

Everything NB 53 does in code, CAFE also offers as a **self-hostable web application** (FastAPI backend + React front end) — for teams who'd rather point-and-click than script. Instead of writing the study out in Python, you define its factors, levels, judge, and replication count in the browser, launch the run, and watch **live progress** as each configuration is executed and scored. When it finishes you read back the same results you computed by hand in the notebook — which factors moved quality, whether the effects are statistically real, and where each configuration sits on the cost/quality trade-off. The app ships inside the CAFE repo under `apps/web-app` and runs locally with a single `docker compose up`.

Want to see it before installing anything?

- **[cafe-ai.de](https://cafe-ai.de)** is the project's home — a plain-language overview of the framework, with links to the paper, the documentation, and the source.
- **[cafe-ai.de/demo](https://cafe-ai.de/demo)** is a **read-only live demo** of that platform: click through a completed study end-to-end in your browser, with zero setup and no API keys required.

## Links

- 🌐 [cafe-ai.de](https://cafe-ai.de) — project site, with a zero-install [live demo](https://cafe-ai.de/demo) of the web platform
- 📦 [github.com/fabian-lu/Cafe](https://github.com/fabian-lu/Cafe) — source, `cafe-core` package, web platform
- 📚 [Documentation](https://fabian-lu.github.io/Cafe/) — guides, API reference, tutorial notebooks (RAG, routing, agents)
- 📄 [arXiv:2607.10380](https://arxiv.org/abs/2607.10380) — Lukassen, Weisser, Kneib & Silbersdorff, *CAFE: A Compound-AI Factorial Evaluation Framework* (yes — the same Weisser who wrote this course)

🧠 **Quiz:** [`../quizzes/quiz_18_compound_ai_evaluation.ipynb`](../quizzes/quiz_18_compound_ai_evaluation.ipynb)
