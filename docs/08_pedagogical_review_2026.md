# Pedagogical Review & Revision Pass — 2026

A full-course pedagogical review from the perspective of a **first-time learner**, with fixes applied directly in place. Scope: all 34 numbered notebooks + 2 onboarding notebooks + 11 appendices + 9 fast-track notebooks + 6 quizzes (63 notebooks total), plus `README.md` and `requirements.txt`.

Editing was **surgical and in-place**: no notebooks were renumbered on disk, no content was moved between notebooks. Every notebook still parses, every edited code cell is valid Python, and the reference checker (`scripts/check_nb_references.py`) is green. 39 files changed (~+217 / −128 lines).

---

## 1. Major structural changes

### 1.1 Course-wide numbering & navigation repair (the headline fix)
The course had been migrated from an old flat **19-notebook** layout to the current **9-module** layout (files `01`–`36`), but the *content inside* many notebooks still carried the **old numbers** in their titles, module labels, prerequisites, cross-references, and "Next step" pointers. The link-checker didn't catch it because it only verifies that an `NB n` token resolves to *some* file — not that the number is the *right* one, and it ignores spelled-out "Notebook n" titles entirely.

Concretely, before this pass:

| File (canonical) | Title said… | Should be |
|---|---|---|
| `05_functions_modules` | Notebook **6** | Notebook 5 |
| `07_apis_and_http` | Notebook **12** | Notebook 7 |
| `08_sql_fundamentals` | Notebook **13** | Notebook 8 |
| `10_pandas_fundamentals` | Notebook **5** | Notebook 10 |
| `11_numpy_fundamentals` | Notebook **7** | Notebook 11 |
| `12_matplotlib_basics` | Notebook **8** | Notebook 12 |
| `15_sklearn_basics` | Notebook **9** | Notebook 15 |
| `18_ai_workflows` | Notebook **11** | Notebook 18 |
| `19_embeddings_retrieval` | Notebook **15** | Notebook 19 |
| `20_tools_and_agents` | Notebook **16** | Notebook 20 |
| `21_document_processing` | Notebook **17** | Notebook 21 |
| `23_from_notebook_to_project` | Notebook **18** (+ Module "Software Engineering") | Notebook 23 (Module: Production) |
| `24_scheduling_orchestration` | Notebook **19** (+ "Software Engineering") | Notebook 24 (Module: Production) |
| `26_capstone_analytics` | Notebook **10** | Notebook 26 |

All **14 stale titles** and the **2 stale module labels** are fixed; all 34 numbered notebooks now have a title number that matches their filename.

**Why it mattered for a beginner.** In a self-paced course the notebook number *is* the progress indicator and the navigation. Two different files both rendered as "Notebook 13"; prerequisite lists pointed at notebooks that taught something else entirely; and "NB 11" referred to three different topics across the course. A first-time learner literally could not trust a single cross-reference.

### 1.2 Broken "Next step" chains rerouted
Several next-step pointers sent the learner to the **wrong notebook** — not just a wrong number, but a pedagogically wrong destination:

- **Dictionaries (NB 4) → "Pandas Preview"** — skipped Functions (NB 5) and Classes (NB 6). Now → **Functions (NB 5)**.
- **Functions (NB 5) → "NumPy"** — skipped Classes (NB 6). Now → **Classes & OOP (NB 6)**.
- **SQL (NB 8) → "Time Series"** — skipped *all* of pandas, NumPy, matplotlib, statistics. Now → **Pandas (NB 10)**.
- **Pandas (NB 10) → "Functions"** — pointed *backwards*. Now → **NumPy (NB 11)**.
- **Matplotlib (NB 12) → "Scikit-Learn"** — skipped Statistics (NB 13). Now → **Statistics (NB 13)**.
- **Time Series (NB 14) → "Embeddings"** — skipped all of ML. Now → **Scikit-Learn (NB 15)**.
- **Document processing (NB 21) → "From Notebook to Project"** — skipped AI Evaluation (NB 22). Now → **AI Evaluation (NB 22)**.

### 1.3 Two false "course is over" endings fixed
- **NB 24 (Scheduling)** ended with *"Congratulations — you've completed the 19-notebook journey… you've reached the end."* A complete-beginner following the course in order would have **stopped before the capstones**. Replaced with a proper Module 6 → Module 7 (Capstones) hand-off.
- **NB 31 (BPM/Governance)** declared *"you have completed the course"* with no mention of **Module 9** (NB 32–36). Reworded to point forward to Module 9 if not yet done.

### 1.4 New content added to close a genuine gap
- **Fast-track NB 03 (`03_lists_and_dicts`)** was titled and advertised as covering dictionaries, `defaultdict`, and `Counter`, but contained **zero dictionary content** — while fast-track NB 02 and NB 03's own exercises *use* dicts. Added a compact **"Dictionaries — a 2-minute primer"** (markdown + runnable cell: literals, `.get()`, `.items()`, `Counter`) so the fast-track is self-consistent.
- **NB 2 (Control Structures)** defined functions (`def route_ticket(...)`) in its second teaching cell, but functions aren't introduced until NB 5. Added a **🔭 forward-reference** (matching the course's existing convention from NB 1) so a beginner can *read* `def`/`return` without being expected to write them yet.

---

## 2. Topics reordered (pointers, not files)

Per the brief's "surgical, in-place" constraint, **no files were renumbered and no content was moved**. The *reordering* was of the navigation that had drifted out of sync with the real module order. After the fixes the linear path reads cleanly end-to-end:

```
1→2→3→4→5→6  (Foundations)
   →7→8       (Real-world I/O)
   →10→11→12→13→14  (Data Science)
   →15→16→17  (Machine Learning)
   →18→19→20→21→22  (AI Engineering)
   →23→24     (Production)
   →26→27     (Capstones)
   →28–31     (Business AI)  →  32–36  (Building AI POCs)
```

The fast-track was likewise re-sequenced to its own `01–09` scheme with `(fast track)` labels, and its pandas→functions *backwards* jump was corrected to pandas→sklearn.

---

## 3. Redundancies / inconsistencies removed or consolidated

- **Onboarding module table (NB 00 §4)** had broken markdown — rows 7 (Capstones) and 8 (Business AI) were missing their "What you'll build" cell, and row 9's description ("Two end-to-end projects to ship") actually belonged to the Capstones row. Table completed and corrected.
- **"Seven modules" vs ten.** The master onboarding, the overview, and the README all said "7 modules" while listing modules 0–9. Reworded consistently to "the modules" / "core modules (1–7)".
- **Stale dual reference in NB 30** ("NB 11 — legacy" *and* "NB 18 — canonical" for the same AI-workflows notebook) collapsed to a single correct pointer (NB 18).
- **`costkit` mis-attribution** ("NB 5's costkit_demo") reconciled to NB 23, where the package is actually built.
- **`darts` package name** in `requirements.txt` (`u8darts` vs `darts`) standardised to the current `darts`.

---

## 4. Explanations simplified / corrected

- **NB 14 seasonal-naive baseline** — the *simplest* baseline had the *most* cryptic code (`fc_snaive = test.copy() * 0.0` + a `-7 + (i % 7)` index trick). Rewritten to a transparent `last_week[i % 7]` tile. **Verified numerically identical** to the original output.
- **NB 7 (APIs)** — replaced a confusing `r = requests.get(...) if True else None` scaffold (dead `if True`, unreachable `hasattr` guard) with a clean `try/except RequestException` offline fallback that matches the rest of the notebook.
- **NB 10 (pandas)** — added one-line comments where `.map(lambda …)` and `pd.cut(…)` first appear (the densest, previously-uncommented lines), including the classic `bins` needs one-more-edge-than-`labels` gotcha.
- **NB 13 (statistics)** — added a one-line plain-English explanation of `stats.t.ppf` (inverse CDF) at first use.
- **NB 11 (NumPy)** — added a `💡` note explaining `.std()`'s `ddof=0` default vs `ddof=1`, so the later switch to `ddof=1` in a Stretch exercise isn't a silent surprise.
- **NB 18 (AI workflows)** — added a `💡` explaining *how the MockLLM decides what to return* (system-prompt keyword routing) and that every provider returns the same dict shape — the missing mental model behind why later "structured output" cells "magically" produce JSON.
- **NB 14 intro** — removed an unfulfilled promise ("a touch of ARIMA"); ARIMA now correctly lives in (and is pointed to via) the forecasting appendices.

### Correctness bugs fixed
- **Appendix A1 (classical forecasting)** — `fit_naive` raised `TypeError: 'int' object is not subscriptable` (`(h // 7 + 1)[:h]`). Fixed to `(… * (h // 7 + 1))[:h]`. **Verified it now runs.**
- **Appendix A4 (TabPFN)** — removed the deprecated `N_ensemble_configurations` kwarg (a `TypeError` under TabPFN v2, which the notebook explicitly targets).
- **Appendix A2 (PyTorch)** — removed a dead `… if False else …` smoke-test line that read like a mistake.
- **NB 20 (tools & agents)** — two Stretch *solutions* monkey-patched a non-existent/no-op method (`MockLLM._should_call.__func__`, `_should_call_rules = lambda…`) that silently did nothing. Replaced with an honest note (the offline mock routes by keyword; a real provider routes from the tool description) plus a direct call so the cell actually demonstrates something.
- **Fast-track NB 08 & 09** — `from llm_providers import …` raised `ModuleNotFoundError` when run from the `fast_track/` folder (the module lives at the repo root). Added a 3-line `sys.path` bootstrap that walks up to find it. **Verified the import now succeeds from the fast-track folder.** Also fixed a broken back-link (`./A1_llm_providers_guide.ipynb` → `../05_ai_engineering/…`).
- **`requirements.txt`** — bumped `matplotlib>=3.7` to `>=3.9`; the notebooks use `ax.boxplot(tick_labels=…)`, which only exists in matplotlib ≥ 3.9 (a hard crash on 3.7/3.8).
- **NB 00b time estimator** — the interactive estimator's `TIMES_MIN` table stopped at NB 27, silently scoring Modules 8–9 as 0 minutes. Added entries for NB 28–36 and a warning for any unknown notebook.

---

## 5. Remaining areas for future improvement

These were identified during review but **not changed** in this pass — either because they need an author-level judgement call, fall outside "surgical/in-place", or are lower priority. They are good candidates for a future revision.

**Structural / sequencing (author decision needed)**
- **Module 2 ↔ Module 3 ordering.** Real-world I/O (NB 7–8) genuinely *uses* pandas, but pandas is taught in Module 3 (NB 10). This pass added forward-reference notes so the pandas usage is acknowledged; the deeper option is to **reorder pandas (NB 10) before Module 2**, which would remove the forward-dependency entirely but requires renumbering.
- **Cross-document time estimates.** The README path table (`~35 h` for a complete beginner) and the NB 00b estimator (`~66 h`) disagree by roughly 2× (read-only vs full-engagement pace). Pick one convention and propagate it.

**Redundancy to consolidate (Modules 8–9 deliberately overlap Module 5)**
- **NB 30 ↔ NB 33** re-teach IDE choice, prompt patterns, and an identical "team prompt-style guide" Stretch exercise. Keep the split (seminar vs hands-on) but dedupe the duplicated stretch and signpost NB 33 as "applying" NB 30.
- **NB 35 §6 ↔ NB 36 §3** present nearly the same vector-store landscape table twice. Make NB 36 canonical; reduce NB 35 to a pointer.
- **NB 16** teaches the cost-optimal-threshold pattern three times (§5, Exercise 1, Stretch C); Stretch C could be repurposed. **NB 17**'s Stretch C duplicates the §5 cyclical-encoding demo.

**Content design**
- **NB 36 (agentic AI)** — the main ReAct POC teaches a brittle free-text/regex parser that the notebook's own Stretch solution calls the wrong approach; consider promoting the structured tool-calling API to the POC and keeping the regex version as an aside.
- **NB 19 / NB 21** — the inlined-vs-imported `MockLLM`/`MockEmbedder` duplication is worth a one-line "these are the same class" note.
- **NB 32 §6** — define `d_k` and the one-hot convention for the attention/cross-entropy formulas (the most intimidating page for a non-maths learner).
- **NB 34** — two stray German words ("Faustregel") should be translated; add a Module-4 prerequisite note before the XGBoost POC 3.

**Cross-cutting**
- **Appendix on-ramps.** The ML module README has no appendix table (the Data Science one does), and NB 14 doesn't point forward to its forecasting appendices (now added). Add a PyTorch-appendix table to `04_machine_learning/README.md`.
- **Quiz scope for fast-track learners.** Quizzes 2 (I/O) and 3 (NumPy/stats) test material the fast-track intentionally skips; add a one-line scope note. (All quiz answer keys were independently verified **correct**.)
- **Notebook import robustness.** The canonical Module 5 notebooks use the same bare `from llm_providers import …` that broke the fast-track; they work under the test runner but may fail if a learner opens them directly. Consider the same `sys.path` bootstrap repo-wide.

---

## 6. Overall assessment

**Before:** pedagogically this is an unusually strong, thoughtfully designed course — clear "why before how" prose, a consistent six-section template, two-tier exercises with worked solutions and *reasoning*, honest treatment of evaluation/leakage/calibration, and an offline-first design that lets everything run without an API key. Its one serious, pervasive weakness was that an incomplete renumbering had left the **navigation layer broken**: wrong titles, wrong prerequisites, wrong "next step" pointers, and two endings that told learners the course was over before it was. For a self-paced course, that is a first-order defect — it breaks the single thing a lone learner relies on to know where they are and where to go next.

**After:** the navigation is internally consistent end-to-end and verified by the link-checker; the linear path and the fast-track both flow correctly; a handful of real correctness bugs (a `TypeError`, a version-dependent crash, a `ModuleNotFoundError` that killed two fast-track notebooks, no-op exercise solutions) are fixed and verified; and several of the densest explanations now carry the same kind of beginner-friendly notes the best notebooks already used. The genuine content gap in the fast-track (dictionaries) is closed, and a premature-`def` jump in NB 2 is now scaffolded.

**Net:** the course was already in the top tier on *content and instructional design*; it was being held back by a broken *navigation and consistency layer* plus a few latent bugs. With those resolved, it now delivers the clean, trustworthy, front-to-back beginner journey its content always deserved. The remaining items in §5 are refinements, not blockers.
