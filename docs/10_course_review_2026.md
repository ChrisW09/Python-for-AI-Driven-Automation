> **Note (July 2026).** This document predates the learning-order renumbering (modules 0–17 / lessons 1–52 were re-sequenced); lesson and module numbers below refer to the **old** numbering and are kept as a historical record. The dated notebook/figure counts in the body are that review's findings *at the time* and are likewise left intact.

> **📌 Current course snapshot (verified 2026-07-19).** The course now holds **113 notebooks** — **58** numbered lessons + **13** appendices + **22** fast-track (plus 1 fast-track onboarding) + **16** quizzes + **3** onboarding — with **243** rendered figures. The reference checker is green over the whole NB 0–53 graph, and the most recent full-execution snapshot is **113/113 clean** (2026-07-17). The **Fast track** is **22 content notebooks (~26 h)**. For the live per-module index see [`README.md`](../README.md) and [`fast_track/README.md`](../fast_track/README.md).

# Course Review & Improvement Report

**Course:** Python for AI-Driven Automation and Business Data Science
**Scope:** 87 notebooks (46 numbered + 13 appendices + 15 fast-track + 10 quizzes + 3 onboarding) plus `README.md`, `requirements.txt`, and supporting docs.
**Status at time of writing:** all 87 notebooks parse as valid JSON, **0 syntax errors**, **0 stored error outputs**, the reference checker is green over the whole NB 0–46 graph, and every worked `<details>` solution executes cleanly in context. **132 figures** are rendered across the course.

---

## 1. Overall assessment

This is, unusually, an **already-excellent** course. It has a clear "why before how" voice, a consistent six-part notebook template, two-tier exercises with worked solutions *and* reasoning, honest treatment of evaluation/leakage/calibration, and an **offline-first design** (every AI notebook runs against a built-in `MockLLM`, so the whole course works with no API key). It had previously been through multiple documented review passes (`docs/01`–`08`), which fixed a course-wide renumbering, broken navigation, and a set of latent runtime bugs.

The improvement work captured in this report therefore concentrated on the **next tier of quality**: making the course *visual* (canonical teaching charts where they teach), splitting over-long cells for live lecturing, eliminating a remaining wave of stale post-renumber cross-references, fixing several real code/output contradictions, and verifying — by execution — that every worked solution still runs after those changes. The course is now in a consistent, figure-rich, runtime-clean, reference-consistent state.

**Bottom line:** content and instructional design were already top-tier; this pass closed the gaps in *visualization, intra-notebook teachability, cross-reference accuracy, and verified correctness*.

---

## 2. What the course teaches & who it is for

**Subject.** A practical, business-flavoured path from Python fundamentals to shipping AI-driven automation: Python → data science (pandas/NumPy/matplotlib/statistics/time-series) → real-world I/O (APIs, SQL) → machine learning (scikit-learn, evaluation, feature engineering) → industry ML applications (churn/CLV, fraud, segmentation, demand/maintenance) → AI engineering (LLM workflows, embeddings/RAG, tools/agents, document processing, evaluation/observability) → building POCs → agents/tools/MCP → NLP → production → capstones → business-AI judgement.

**Audience.** Self-paced learners and a lecture cohort: beginners on the Foundations/Fast-track side, advancing to intermediate ML/AI-engineering practitioners and business/technical leads by the Industry/AI-Engineering/Business modules.

**Sequence & build-up.** A deliberate **motivation-first spiral**: a 5-minute "see it work" demo (`00c`) up front, then a strict dependency-clean skill spine (Python → data → ML → AI), with professional tooling (Git/Copilot) pulled early, and the *build it / ship it* judgement (POCs, production, business) clustered near the end. Notebooks build on one another with explicit prerequisites and "Next step" pointers; a **Fast track** mirrors the spine in 22 trimmed notebooks, and **quizzes** check each module.

**Strengths.** Offline-first reproducibility; consistent template; worked solutions with reasoning; honest ML evaluation; strong business framing (everything ends in a costed decision rule).

**Where it was weakest (now addressed).** (a) Almost no rendered figures outside two showcase notebooks; (b) some teaching-core cells were too long to explain line-by-line; (c) a residual layer of stale `NB n` / `Module n` references survived the renumber; (d) a handful of code cells whose printed output contradicted the surrounding lesson.

---

## 3. Review methodology

Work proceeded incrementally and was verified at every step:

1. **Structure first** — mapped every notebook, the module graph, the README/requirements, and the historical review docs.
2. **Per-notebook inspection** — cell by cell for correctness, clarity, structure, execution order, and consistency, with attention to whether a student could follow it unaided.
3. **Execution** — notebooks were executed end-to-end with the real scientific stack (numpy 2.4.6 / pandas 3.0.3 / scikit-learn 1.8.0 / scipy 1.17.1 / statsmodels 0.14.6 / matplotlib 3.10.9 / torch 2.12.0) to render figures and surface runtime errors. Heavy-/network-dependent appendices were validated statically (see §7).
4. **Worked-solution execution** — every collapsed `<details>` solution (391 blocks across 50 notebooks) was executed in the namespace state a learner meets it in — the failure mode that ordinary notebook runs never catch.
5. **Multi-agent fan-out** — parallel agents were used for breadth (auditing module clusters, applying a vetted cross-reference sweep, and a per-notebook visualization check), with **central verification by hand** after each wave.
6. **Central verification gate** — after every change: JSON validity, `ast.parse` on every code cell, zero error outputs, and the repo's `scripts/check_nb_references.py` link checker.

---

## 4. Major improvements implemented (thematic)

### 4.1 Visualization (the headline improvement)
The course went from a handful of rendered figures to **132 rendered figures**, adding the *canonical teaching visuals* that were missing and rendering existing-but-stripped charts:

- **ML core:** the line a linear model learns (with residuals); the **bias–variance / overfitting curve** (train vs test vs depth); **decision boundaries** for four classifiers; a **learning curve**; **permutation vs impurity importance**; a **Pipeline diagram**; a **confusion-matrix-at-cost-optimal-threshold** payoff; **calibration reliability** diagrams.
- **Statistics:** mean-vs-median skew, the **CLT** (sampling distribution narrowing with n), the **p-value as a tail area**, and the **sample-size/1-d² cost curve** — added to both the canonical and fast-track stats notebooks.
- **Feature engineering:** a **scaling-effect** demo (k-NN 0.64→0.74 with scaling; trees unaffected), a **leakage-detection** distribution plot, and a **feature-selection F-score** chart.
- **Industry:** PR curve vs prevalence + a static **queue-economics** curve (fraud); RFM segment value + **hit-rate@k vs popularity** (recommenders); a **forecast backtest** plot (demand).
- **AI engineering:** a **document-similarity heatmap** and rendered retriever comparison (embeddings); **confusion-matrix heatmaps** + a rendered cost dashboard (evaluation); a **batch KPI dashboard** (workflows).
- **Foundations/IO (selective):** Counter/GROUP-BY/latency/cost bars where real data exists — and **pure-syntax notebooks deliberately left chart-free** (no fabricated data).

Every added visual follows one house style (seaborn whitegrid, a consistent blue/red/green/orange palette) and is framed with a short markdown intro + a "how to read it" note.

### 4.2 Teachability — splitting over-long cells
Over-long code cells in the teaching core were partitioned into consecutive, lecture-friendly cells at safe top-level boundaries (never inside a function/class/loop), e.g. NB14 47→34, NB15 58→28, NB13 65→38, NB05 58→25. Single coherent units (one class, one query walk-through) were kept whole.

### 4.3 Cross-reference accuracy (post-renumber cleanup)
A residual wave of stale references was corrected: NB 21 "Module 7"→6 and forward-refs NB 27–30 → 22/23/24/26; NB 24/25 prereq "NB 18 (retrieval)" → **23**; NB 34's false "you've finished the 42-lesson course" ending reframed to end-of-Module-8 with refs 39/40/41 → 31/32/33; NLP module labels 12 → 9; DeepTab 13 → 10; the `MockLLM` "NB 17" misattribution → NB 22; plus several prereq/typo fixes and onboarding manager-path alignment.

### 4.4 Real correctness fixes
- **NB16 scaling demo** used accuracy (all 0.75 — the imbalance baseline), contradicting "scaling helps"; switched the demonstrator to **k-NN with ROC-AUC** (LogisticRegression is scale-robust once converged — the original premise was wrong) so the lesson holds; the simulated leak was strengthened so its correlation is genuinely −0.98.
- **NB20 "leak" Debug-me** actually scored *below* the honest model (no real leak on this data); reframed honestly to "scores the same but peeks at *today's* reading — the bug is *when* the feature is known."
- **NB14 Ex5 Debug-me** moved from LogisticRegression (train≈test, leak invisible, "suspiciously perfect" false) to an **unbounded DecisionTree** → train **1.000** / test 0.767, making the train-on-test leak dramatic and the framing true.
- **NB42 capstone** golden-set labels disagreed with the deterministic mock, so the regression gate **halted the flagship demo**; rewrote the 7 examples to be both semantically correct *and* matched by the mock — the gate now passes (100%) and the assistant processes all 50 messages.
- **NB15** corrected the overstated "calibration halves the Brier score"; **NB10 / fast-track 07** stale stats prose corrected to the real outputs (t≈−12, p≈3×10⁻²⁶, d≈1.2); **fast_track/08** "~0% churn" → "~27%"; **fast_track/11** `rag_answer` default-arg `NameError` fixed.

### 4.5 Reference-data accuracy (verified, not from memory)
`A1_llm_providers_guide` was corrected against the current Anthropic reference: `claude-opus-4-6` → `claude-opus-4-8`, context window 200K → up to 1M (Opus/Sonnet), Haiku pricing $0.0008/$0.004 → $0.001/$0.005 (Sonnet pricing was already correct). OpenAI/Google figures were left as the notebook already caveats them as "verify with provider."

### 4.6 Environment hardening
The NLP installs (`bertopic`, `sentence-transformers`, and the now-removed `stream_topic`/`deeptab`) had transiently **downgraded pandas 3.0.3→2.3.3 and torch 2.12→2.9.1**; the documented stack was restored, and NB38 (DeepTab) was patched to be backend-agnostic so it renders (4 figs) via its intended offline scikit-learn stand-in.

---

## 5. Module-by-module findings & changes

Legend: **figs** = rendered figures now in the notebook.

| Module | Notebooks | Findings | Changes implemented |
|---|---|---|---|
| **00 Onboarding** | 00, 00b, 00c | Manager-path scope/hours disagreed between 00 and 00b | Aligned the manager path; added a KPI bar to `00c` (1 fig). |
| **01 Foundations** | 01–06 | Pure-Python topics; a few over-long cells; "next step" wording | Split long cells (02/05/06); added Counter/latency/cost bars to 02/03/04 where real data exists; **01/05/06 deliberately chart-free** (no data to plot); reworded NB1 next-step. |
| **02 Data Science** | 07–11 + A1–A4 | Visualization-light for the most visual topics; stale stats prose in NB10 | Rendered/expanded charts across 07–11 (40 figs); added the four canonical stats visuals to NB10; corrected stale t/p/d/CI prose. Forecasting appendices already figure-rich. |
| **03 Real-world I/O** | 12, 13 + A1 | I/O-mechanics; little plottable data | Added a GROUP BY bar to NB13; removed dead code in the scraping appendix; NB12 left chart-free (live-HTTP, illustrative status text). |
| **04 Machine Learning** | 14–16 + A1–A5 | The clearest viz gap; some long cells; two output-vs-lesson contradictions | Added line/overfitting/decision-boundary/pipeline-diagram visuals (NB14, 8 figs); threshold/calibration/learning-curve visuals (NB15, 8 figs); scaling/leak/selection visuals + the k-NN scaling fix and stronger leak (NB16); strengthened Ex5 Debug-me; PyTorch/TabPFN/conformal appendices reviewed (clarity notes). |
| **05 Industry Applications** | 17–20 | Decision-rule-heavy, under-visualized | PR/queue-economics (fraud), RFM/hit-rate (recommenders), forecast backtest (demand), EV/risk bars (churn) — 10 figs total; fixed the NB20 leak-exercise premise. |
| **06 AI Engineering** | 21–26 + A1–A3 | 0 figures despite intensely visual topics; stale cross-refs; reference-data drift | Added embedding similarity heatmap (NB23) + confusion/cost dashboards (NB26) + batch KPI dashboard (NB22); fixed Module-6 cross-references; corrected `A1` model/pricing/context; HNSW O(log n) caveat (A2); offline-mock caveat (A3). |
| **07 Building POCs** | 27–30 | Build/narrative; mostly correctly chart-free | Fixed cross-refs (NB28 §5/Module-14). No forced charts (kNN-scaling curve in NB30 is a candidate future add). |
| **08 Agents/Tools/MCP** | 31–34 | Architecture/agentic; the false "course over" ending in NB34 | Fixed NB34's ending + all stale 39/40/41 → 31/32/33 references (prereqs, takeaways, code comments). Charts not applicable. |
| **09 NLP** | 35–37 | 35 needs `bertopic`; 36 needs an uninstallable dep | Module labels 12 → 9; NB37 already has confusion + token-influence charts; NB35 rendered (1 fig). NB36 remains a reference notebook (see §7). |
| **10 DeepTab** | 38 | Lost its renders; library API drift | Patched to backend-agnostic; **figures restored (4)**; module label 13 → 10. |
| **11 Production** | 39, 40 | Packaging/scheduling; correctly chart-free | Trimmed NB39's over-claimed packaged-code list. |
| **13 Capstones** | 41, 42 | NB42 regression gate broke the demo | Fixed the golden set so the gate passes and the assistant runs end-to-end; 41 already figure-rich. |
| **14 Business AI** | 43–46 | Narrative/governance; charts don't fit | Cross-ref/typo fixes (NB44 diagram ref, NB46 "(NB 41, 25)"→42). Intentionally prose-and-code. |
| **Fast track** | 00–14 | 07/08 are the rendered showcases; stale stats in 07; small bugs | Stats prose fix + churn-% fix (07/08); selective bars (02/03/09/14); `rag_answer` default-arg fix (11); header/time consistency; pure-syntax notebooks chart-free. |
| **Quizzes** | 10 | — | All 30 answer keys independently re-verified **correct**; scope notes accurate. No changes needed. |

---

## 6. Code-quality & consistency work

- **Determinism/seeds** were already pervasive (`RANDOM_STATE`, seeded `default_rng`); preserved throughout.
- **Plotting** standardized to one palette + labelled axes/titles + "how to read it" notes.
- **Imports** kept local-to-cell where pedagogically useful (so each cell is copy-runnable); not over-refactored.
- **Structure** — every numbered notebook already follows the Title → Motivation → Objectives → Setup → Sections → Exercises → Summary → Next-step template; new cells were inserted to match it, and section numbering was kept sequential after splits.
- **No new required dependencies** were introduced. (The temporary `bertopic`/`deeptab` installs were rolled back; the documented stack is intact.)

---

## 7. Cells / notebooks that could not be executed end-to-end

These are **reference notebooks by design** and were reviewed statically; they are not on the runtime-clean executable path:

- `09_nlp/36_topic_modeling_stream.ipynb` — its `stream_topic` → `pkuseg` dependency does **not compile on Python 3.11** (its C++ source needs the removed `longintrepr.h`); the maintained fork installs under a different module name. The notebook guards every real call behind `HAS_STREAM` with an offline stand-in, so it reads correctly without running.
- `02_data_science/A2_forecasting_prophet_libraries`, `A3/A4` heavy-lib paths; `04_machine_learning/A1–A4` (torch/transformers/peft/tabpfn); `06_ai_engineering/A1–A3` provider/vector-store/RAG-framework appendices; `03_real_world_io/A1` (Firecrawl/network) — each needs an optional library or network and is framed as reference; the offline portions run.
- Several **bonus** worked solutions use `pd.read_csv("data/…")`, which resolves only when Jupyter is launched from the repo root (the documented setup) — a convention, not a defect.

Everything on the **core executable path** (onboarding, Foundations 1–6, Data Science 7–11, I/O 12–13, ML 14–16, Industry 17–20, AI-Eng 21–26 offline, NLP 37, DeepTab 38 via stand-in, Capstones 41–42, the whole Fast track, all quizzes) runs end-to-end with **0 errors**.

---

## 8. Environment & reproducibility

- `requirements.txt` is **complete, version-capped, and verified** against the installed stack (numpy 2.4.6 / pandas 3.0.3 / matplotlib 3.10.9 / scikit-learn 1.8.0 / statsmodels 0.14.6 / scipy 1.17.1 / jupyterlab 4.5.7), with optional provider/vector/DL/tabular groups commented out — no change needed.
- `README.md` covers **Colab (zero-setup) and local install**, a full per-module notebook index with Colab badges, the fast track, and quizzes — students can clone, install, and run. No change needed.
- A learner can reproduce the rendered figures by running the offline notebooks as-is; the AI notebooks need no key (MockLLM).

---

## 9. Remaining open issues / candidate future work

None block a learner. In rough priority:

1. ~~**Build/architecture cluster figures.**~~ **DONE.** Added the **O(n) brute-force-kNN scaling curve** (log–log) to **NB30**; **NB42** already ships a 4-panel eval/cost dashboard. The rest of the cluster (27–29, 31–34, 39–40, 43–46) is intentionally prose-and-code (no genuine data to plot).
2. ~~**`36_topic_modeling_stream` dependency.**~~ **Resolved/clarified.** The notebook already carries a "📎 Optional module — reference style" banner and guards every real call behind `HAS_STREAM` with an offline stand-in, so it reads/runs offline. The only optional extra is pinning the `spacy-pkuseg` fork for real-library execution (not required).
3. ~~**DeepTab real backend.**~~ **DONE.** The DeepTab notebook (now NB 44) was aligned to **DeepTab v2.0.0's split-config API** (`MambularConfig` / `PreprocessingConfig` / `TrainerConfig`): the smoke test gates on v2+ (`deeptab.configs` import), and the offline stand-ins mirror the same split-config constructors, so real-backend execution works on a current install.
4. ~~**Provider pricing/IDs** in `A1_llm_providers_guide`~~ **Verified 2026-07-22.** All quoted OpenAI, Anthropic, and Google prices/IDs checked against current provider pricing and confirmed accurate; added a note that OpenAI's **GPT-5.6 family** (Sol/Terra/Luna, July 2026) superseded `gpt-5.5` as flagship — the notebook's `gpt-5.4-mini` default remains available at unchanged prices. Re-verify periodically; prices drift.
5. **Output convention.** The course historically ships output-stripped; this work intentionally **rendered figures** in the quantitative/teaching notebooks (the showcase style). If you prefer a uniform convention, decide between "render all" (heavier diffs, instant viewing on GitHub/Colab) vs "strip all but the two showcases" and apply once.

---

## 10. Recommended next steps

1. **Review the rendered diffs** (figures embedded → larger notebook files) and confirm the "render figures" convention is what you want for teaching.
2. **Commit** in logical groups (visuals, cell-splits, cross-ref fixes, correctness fixes) so the history is legible.
3. Optionally green-light the **build-cluster figure pass** (item 9.1) and the **NB36 dependency decision** (9.2).
4. Re-run the verification gate before each release: `python scripts/check_nb_references.py` + a full `nbconvert --execute` of the offline path (or the repo's `scripts/run_all_notebooks.py`).

---

## 11. Verification snapshot (at report time)

- Notebooks: **87** · rendered figures: **132**
- JSON validity: **87/87** · `ast.parse`: **0 failures** · stored error outputs: **0**
- Reference checker (`scripts/check_nb_references.py`): **green** (NB 0–46 all resolve)
- Worked `<details>` solutions: **all real solutions execute cleanly** (only non-issues: optional `tabulate`, live-network stubs, intentional Debug-me snippets)
- Quiz answer keys: **30/30 verified correct**
- Core scientific stack: pandas 3.0.3 · numpy 2.4.6 · scikit-learn 1.8.0 · scipy 1.17.1 · matplotlib 3.10.9 · statsmodels 0.14.6 · torch 2.12.0
