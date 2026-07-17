# Module 18 — Compound AI Evaluation with CAFE (optional)

> 🧭  [◀ Django](../17_django/)  ·  [🏠 Course home](../README.md)

**Goal:** Learn to answer the question every AI team eventually faces: *we changed the pipeline and quality moved — **which change actually did it, and is the difference real?*** The tool for that question is a century of **design of experiments** (factorial designs, replication, mixed-effects models) pointed at compound AI systems — and **[CAFE](https://github.com/fabian-lu/Cafe)** (*Compound-AI Factorial Evaluation*, [cafe-ai.de](https://cafe-ai.de)), the open-source library that packages the whole workflow: factorial designs over your pipeline's knobs, an LLM-judge layer, scale-correct statistical attribution, cost/quality Pareto frontiers, and a self-hostable web platform.

**Estimated time:** 1.5–2 hours.

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

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll learn |
|---|---|---|---|---|
| 53 | `53_compound_ai_evaluation_cafe.ipynb` | ~1.5 h | Intermediate–Advanced | The attribution problem, factors/levels/configurations, replication vs LLM noise, ANOVA with interactions and effect sizes, ordinal-rubric caveats (CLMM), cost/quality Pareto frontiers, and the CAFE library |

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

## Installing CAFE (optional)

The notebook runs end-to-end **without** CAFE — the library section is guarded and skips gracefully. To run the real thing:

```bash
git clone https://github.com/fabian-lu/Cafe.git && cd Cafe
pip install -e "packages/cafe-core[all]"
# macOS: brew install r        Debian/Ubuntu: sudo apt install r-base
Rscript -e 'install.packages(c("ordinal", "lme4"))'
cafe doctor          # verify Python + R + LLM access
cafe run example     # bundled toy study — no API keys needed
```

CAFE requires **Python ≥ 3.11** and **R** (the ordinal/logistic mixed models run through R's `ordinal` and `lme4` packages). The self-hostable web platform lives in the repo under `apps/web-app` (`docker compose up`), or click through the read-only [live demo](https://cafe-ai.de/demo).

## Links

- 🌐 [cafe-ai.de](https://cafe-ai.de) — project site & live demo
- 📦 [github.com/fabian-lu/Cafe](https://github.com/fabian-lu/Cafe) — source, `cafe-core` package, web platform
- 📚 [Documentation](https://fabian-lu.github.io/Cafe/) — guides, API reference, tutorial notebooks (RAG, routing, agents)
- 📄 [arXiv:2607.10380](https://arxiv.org/abs/2607.10380) — Lukassen, Weisser, Kneib & Silbersdorff, *CAFE: A Compound-AI Factorial Evaluation Framework* (yes — the same Weisser who wrote this course)

🧠 **Quiz:** [`../quizzes/quiz_18_compound_ai_evaluation.ipynb`](../quizzes/quiz_18_compound_ai_evaluation.ipynb)
