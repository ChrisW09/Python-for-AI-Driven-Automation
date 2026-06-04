# Pedagogical Review & Revision Pass — 2026

A full-course pedagogical review from the perspective of a **first-time learner**, with fixes applied directly in place. Scope: all 34 numbered notebooks + 2 onboarding notebooks + 11 appendices + 9 fast-track notebooks + 6 quizzes (63 notebooks total), plus `README.md` and `requirements.txt`.

> ⚠️ **Numbering note (read first).** Sections 1–10 are the historical record of the review passes and use the **pre-renumber** notebook numbers (1–36 with gaps at 9 and 25, Real-world I/O before Data Science). In the final pass the course was **fully renumbered** — contiguous NB 1–34, Data Science moved ahead of Real-world I/O. The old→new map is in **§11**; all *course* files use the new numbers.

Editing in passes 1–10 was **surgical and in-place**: no notebooks were renumbered on disk, no content was moved between notebooks. Every notebook still parses, every edited code cell is valid Python, and the reference checker (`scripts/check_nb_references.py`) is green. 39 files changed (~+217 / −128 lines).

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

---

## 7. Second consistency pass (final review)

A follow-up pass built an authoritative map of **every** `Notebook N` / `NB N` reference in all 63 notebooks + READMEs and cross-checked each against the canonical topic for that number. It also executed the notebooks whose dependencies are installable, to prove the edits don't break execution.

### 7.1 A real course-wide bug found and fixed: `llm_providers` import
The biggest find of the second pass. The AI notebooks import the shared helper with a bare `from llm_providers import …`, but `llm_providers.py` lives **only at the repo root**. JupyterLab starts a kernel with its working directory set to the *notebook's own folder*, and the project's own `run_all_notebooks.py` runs each notebook with `cwd = notebook's folder` too. Verified empirically: `from llm_providers import MockLLM` raises **`ModuleNotFoundError` from `05_ai_engineering/`**. So a learner opening NB 18–19 or appendices A1–A3 directly in JupyterLab would hit a hard import error on the first AI cell. (The recorded "pass" snapshot was produced with the repo root forced onto the path.)

**Fix:** added a 3-line, cwd-independent bootstrap (walks up from the working directory to find `llm_providers.py` and puts it on `sys.path`) to the five notebooks that import it — `18_ai_workflows`, `19_embeddings_retrieval`, `A1_llm_providers_guide`, `A2_vector_stores_survey`, `A3_rag_and_agent_frameworks` — the same fix already applied to the two fast-track AI notebooks. **Verified:** NB 18 now runs 18 cells cleanly *from its own folder*, and the import resolves from a subfolder cwd. (NB 28 only *mentions* `llm_providers` in prose — no change needed.)

### 7.2 Remaining stale cross-references (missed by pass 1)
- **NB 12 (matplotlib)** — two more "the NB10 capstone" references (cells 0 and 62) → **NB 26** (pass 1 fixed only the other two).
- **NB 15 (sklearn)** — "The LLM-based approach in **NB11**" → **NB 18** (old layout had AI-workflows at 11).
- **Fast-track `09_embeddings_and_rag`** — five references to "Notebook 11"/"NB11" for the keyword-RAG (which is fast-track notebook 8), plus a prerequisite line citing canonical `NB 5 / 11 / 15` (and NumPy, which the fast track skips) → corrected to fast-track numbers.
- **Fast-track NB 04 & NB 07** — inline "NB 11 / NB 15" canonical references that don't exist in the fast track → reworded.

After this, an authoritative scan reports **0** old-meaning collisions in the main course and **0** canonical-number references in the fast-track.

### 7.3 Structural consistency
- **00b estimator omitted NB 6 (Classes).** The interactive time estimator's `TIMES_MIN` table and default "complete beginner" path skipped NB 6 entirely (and the diagram said "NB 01–05") — the core Classes notebook was invisible to the planning tool. Added `"06"` to both, fixed the diagram to "NB 01–06" (estimator now totals 26 notebooks).
- **NB 6** lacked the `> **Module:** … · **Estimated time:** … · **Difficulty:** …` subtitle every sibling (NB 1–5, 7) has — added.
- **Modules 8–9 (NB 28–36)** had no subtitle line at all — added one to each (Module label + time + difficulty), so all 34 numbered notebooks now share the header format.
- **NB 26** module label "Capstone Project" → "Capstones" (matches NB 27 and the module name).
- **Fast-track titles** unified to "Notebook N (fast track) — …" across all nine.

### 7.4 Content improvements
- **NB 32** — named the *one-hot* target in the cross-entropy formula and added a one-line definition of `d_k` under the attention table (the lone undefined symbol on the most intimidating page).
- **NB 34** — translated the stray German "**Faustregel:**" → "**Rule of thumb:**".
- **Quizzes 2 & 3** — added a fast-track scope note (they test HTTP/SQL/Pydantic and NumPy/stats that the fast track skips).

### 7.5 Verification performed this pass
- Reference checker: **green** (all NB references resolve).
- **63 / 63** notebooks parse; **769** code cells checked, **0** syntax errors.
- Executed 14 notebooks end-to-end with the available libraries (foundations NB 2–6, NB 7, NB 10–12, NB 20, NB 18, fast-track 03/04/08) — **all clean**, including the previously-broken fast-track and AI-notebook imports. (DS/ML notebooks needing scikit-learn/statsmodels couldn't be executed in the sandbox for lack of disk space; their edited cells were verified by syntax check and, for the behaviour-sensitive ones, by standalone equivalence tests.)
- Confirmed every edit is persisted on disk in the course folder.

### 7.6 Items still open after this pass
Genuinely-future refinements (unchanged from §5, minus what was completed above): Module 8↔5 / 9↔5 overlap consolidation (NB 30↔33, NB 35↔36); NB 36's brittle free-text ReAct parser vs structured tool-calling; and the inline-vs-imported `MockLLM`/`MockEmbedder` duplication note in NB 19/21. None blocks a learner. *(The Module 2 ↔ 3 ordering and the time-estimate reconciliation were addressed in §8.)*

---

## 8. Structural restructuring — the motivation-first spiral (pass 3)

**Diagnosis.** The course built skills strictly bottom-up but deferred *both* motivating elements to the very end: the **why** (Module 8, business context) and the **payoff** (Module 9, actually building an AI POC). A learner spent ~17 notebooks on Python/data/ML before anything looked like "AI-driven automation." The dependency order is correct and can't be scrambled (pandas needs Python, RAG needs embeddings, the POCs need the whole stack), so the fix is a **spiral**: pull the prerequisite-free framing and a working demo to the front, pull professional tooling forward, keep the skill spine in order, and cluster the build + deployment judgement at the end.

**Implemented (low-risk, no file renumbering — so all the consistency work in §1–§7 stays intact):**

- **New `00c_see_it_work.ipynb`** — a 5-minute, fully **offline** orientation demo (AI triage → structured tags, a tiny RAG grounded answer, a business KPI snapshot) so learners see the destination on day one. Runs from any working directory (same import bootstrap as §7.1); **verified it executes cleanly.**
- **Spiral guidance in the master onboarding (NB 00)** — a new "🧭 The recommended order" section at the top: (1) see it work (`00c`) + optionally the *why* (NB 28) and *what an LLM is* (NB 32); (2) build skills Modules 1→6 with **Git/Copilot (NB 30) set up early**; (3) build the real thing (Module 9 POCs + Module 8 deployment judgement); (4) ship a capstone (Module 7). The environment-check success message and the "which file next" section now point to `00c` first.
- **Complete-beginner path re-sequenced to the full spiral** in both the 00b learning-path table and the interactive estimator — and, importantly, it now **includes Modules 8–9**. Those modules carry Modulhandbuch-required competencies (RAG, agentic AI, vector DBs, POC→MVP→Production, BPM, governance), so treating them as "optional companions" under-served the descriptor; the complete path is now the full 36-notebook spiral (~94 h, which the estimator computes). The skill spine inside the spiral stays in strict dependency order.
- **README** updated: a "👀 See it work first" pointer to `00c`, the spiral complete-beginner path, and a note that the 00b estimator is the authoritative time source (which also reconciles the old README ~35 h vs 00b figure — the headline complete-beginner number is now consistent at ~90–94 h).
- **Orientation signposts** (additive 📍 notes) on NB 28 ("recommended early — prerequisite-free"), NB 30 ("do this early — the Git/Copilot workflow pays off everywhere"), and NB 32 ("concepts are prerequisite-free; skim the maths first time"). Plus "🧭 Where this fits" tie-backs in the Foundations and Data-Science module READMEs to sustain the through-line during the long skill-building stretch.

**Why this is safe.** Physical file numbers are unchanged, so every cross-reference, title, and "Next step" fixed in earlier passes still resolves; the spiral is expressed as the *recommended path* + signposts and is fully reversible. **Coverage is strictly improved, not reduced** — nothing was removed, and Modules 8–9 are now correctly part of the complete journey.

**On "can the business/architecture topics be taught well in Jupyter?"** The technical 80 % is ideal for notebooks; much of the "theory" is *better* in a notebook when it's code-backed (the `00c` demo, NB 32's tokeniser/attention, architecture-by-building in NB 34). The genuinely narrative parts (governance philosophy, change management, case-study discussion in Module 8) are only *adequately* served by Jupyter — there the notebook is effectively a formatted reader, best paired with the slide deck for live delivery, with the notebook holding the reflection/case exercises. That split is now reflected in how the spiral positions those notebooks (early, prerequisite-free reading) versus the code-heavy build notebooks (late, hands-on).

**Verification (pass 3):** reference checker green; **64 notebooks** parse (the new `00c` included); **773 code cells, 0 syntax errors**; `00c` executes end-to-end from the onboarding folder; the 00b estimator runs and totals the 36-notebook spiral; all edits confirmed on disk.

---

## 9. Runtime + solution-correctness pass (deepest verification)

This pass installed the full scientific stack (scikit-learn, statsmodels, scipy) and did two things prior passes could not: **executed the notebooks end-to-end against real libraries**, and **ran every exercise's *worked solution* in its in-notebook context**. Both surfaced issues that static checks and even `nbclient` miss — because worked solutions live in collapsed markdown blocks that a notebook run never executes.

### 9.1 End-to-end execution — clean
**53 notebooks executed top-to-bottom with the real stack** — the full core path (00c, Notebooks 1–24, 26, 27), Module 8 (28–31), Module 9 (32–36), the entire fast-track (00–09), the two runnable appendices (03/A1, 05/A1), and all six quizzes — **all pass with zero runtime errors**. (The ~9 remaining appendices need heavy optional libraries — torch, prophet, darts, faiss, chromadb, tabpfn — and are reference notebooks by design.) The seasonal-naive rewrite, the import bootstraps, and every earlier content fix were confirmed working in real execution.

### 9.2 Seven broken worked-solutions found and fixed
A custom checker ran each `<details>` solution block in the namespace state it would actually see (the code cells preceding it). It found **seven genuinely broken solutions**, now fixed and re-verified:

| Notebook | Symptom | Root cause | Fix |
|---|---|---|---|
| **NB 16** | bonus `compare_models` — *all CV fits fail* | a later calibration cell did `X, y = load_breast_cancer(...)`, so the churn `prep` (selects columns by name) got an ndarray | restore `X, y` from the churn `df` in the solution |
| **NB 19** | bonus `rag_answer_safe` — `KeyError: 'tech.mobile'` | Stretch C/D reassigned the global `DOCS` to a smaller corpus the retriever wasn't built on | renamed the exercises' local corpus to `KB` |
| **NB 19** | Debug-me solution — `NameError: new_doc_text` | solution wasn't self-contained | define `new_doc_text` in the block |
| **NB 20** | bonus `run_pandas_query` — `'dict' has no attribute 'append'` | Stretch exercises reassigned `TOOLS` (a schema *list*) to a name→function *dict* | renamed the exercises' dict to `TOOL_MAP` |
| **NB 21** | Stretch solution — `'function' has no attribute '__func__'` | `MockLLM._extract` is a `@staticmethod`; `.__func__` is wrong | call `MockLLM._extract(text)` directly |
| **NB 27** | two Stretch solutions — `NameError: send_slack_alert`; `FileNotFoundError` | a helper was never defined; a report dir was never created | add an offline `send_slack_alert` stub; `out_dir.mkdir(exist_ok=True)` |
| **NB 08** | bonus CTE+JOIN — `no such table: channel_meta` | a later cell reset `conn` to a fresh in-memory DB, dropping the lookup table | re-register `channel_meta` on the current connection |
| **fast-track 09** | same Debug-me `NameError` as NB 19 | trimmed copy carried the same gap | same self-containment fix |

**The dominant root cause** — six of the seven — is the same: a **later cell silently reassigns a global** (`X`, `DOCS`, `TOOLS`, `conn`) that an earlier-defined helper or a later bonus/stretch solution still depends on. These only break when the notebook is run **top-to-bottom — exactly how a learner uses it** — and they were invisible to every prior check (and to the original course audits) because the solutions are markdown, never executed by a notebook run. Worked solutions are pedagogy-critical: a broken one either misleads the learner or hangs/crashes their kernel right when they're checking their own attempt.

### 9.3 Confirmed *non*-issues (false positives the checker raised)
- **NB 02 Debug-me** infinite loop — *intentional* puzzle code, with an explicit "don't run this" warning; the real solution is correct.
- **NB 07** bonus `KeyError: 'city'` — the checker ran the `safe_fetch` *stub*; with the real implementation it works online (this is a live-API bonus).
- **NB 23** `SyntaxError` — an illustrative `...`-elided CLI fragment, not standalone code.
- **NB 36** `ModuleNotFoundError: faiss` — an optional-dependency demo, by design.

### 9.4 One minor item left as-is
A few **bonus** solutions use `pd.read_csv("data/…")`, which resolves only when Jupyter is launched from the repo root (the documented setup). Every notebook's **main** flow generates its data inline, so the course is cwd-robust where it matters; only these optional bonus reads assume the repo-root working directory. Left unchanged (a documentation convention, not a defect); noted here for completeness.

### 9.5 Verification (pass 9)
Reference checker green; 64 notebooks parse; 773 code cells, 0 syntax errors; 53 notebooks execute end-to-end with zero runtime errors; all seven solution fixes re-verified by re-running both the notebook (kernel) and the solution blocks; all edits confirmed on disk.

**Bottom line:** after this pass the course is not just *structurally* and *referentially* clean (passes 1–8) but **runtime-clean and solution-correct** — every notebook on the executable path runs end-to-end, and every worked solution runs in the context a learner meets it in.

---

## 10. Open-items pass (consolidation & framing refinements)

The remaining items logged as "future work" in §5–§9, now addressed:

- **NB 30 ↔ NB 33 overlap (signposted + de-duplicated).** On inspection the two are mostly *complementary*, not duplicated — NB 30 §3 teaches *general* code-prompting patterns; NB 33 §5 teaches *app-scaffolding* prompt structure (stack, files, schemas, demo data). The genuine duplication was the near-identical "team prompt-style guide" stretch in both. Fixes: NB 33 §5 now back-references NB 30 §3 ("there you learned *what* makes a good prompt; here you apply it"); NB 33's Stretch B is reframed as an *Agent-Mode addendum* that builds on NB 30's guide rather than repeating it; and NB 30 §6 now points forward to Module 9 as where the workflow is *practised* ("this notebook is the judgement; Module 9 is the practice").
- **NB 36 ReAct parser (contradiction resolved).** The POC 2 prompt claimed a regex parser of `Thought/Action/Action Input` is "reliable," while the notebook's own Debug-me solution correctly calls free-text regex parsing "brittle" and names structured tool-calling as the fix. The POC bullet now states this honestly: regex *can* drive the loop, but the model deviates in practice, so **production agents use the structured tool-calling API from §8** — the free-text version is kept only because it makes every *Thought*/*Action* visible, which is the point of a teaching POC. This reconciles §8, the POC, and the Debug-me lesson.
- **NB 19 / NB 21 inline-vs-imported mocks (clarified).** Both vendor a tiny `MockLLM` inline while other notebooks import it from `llm_providers.py`. Added a one-line note in each explaining the inline copy is "the same idea as `llm_providers.py`'s (NB 18), vendored for self-containment" — and fixed a stale `from NB11` comment in NB 19 (the mock pattern comes from NB 18, not 11).
- **NB 35 ↔ NB 36 vector-store landscape (already fine — left as-is).** Re-checked: NB 35 §6 is a brief, use-case-mapped 5-bullet list that already says "*(full landscape covered in NB 36)*", and NB 36 §3 is the canonical 6-row table + selection heuristic. That is a sensible split (pick-a-store-now vs the full comparison), not a true duplication, so it was left unchanged.

**Verification (open-items pass):** reference checker green; 64 notebooks parse, 0 syntax errors; the five edited notebooks (NB 19, 21, 30, 33, 36) all execute cleanly; edits confirmed on disk.

**Genuinely remaining at the end of this pass:** whether to physically reorder pandas ahead of Real-world I/O and clean up the numbering. **Resolved in §11** — the author opted for the full renumber.

---

## 11. Full clean renumber (final pass)

At the author's request the numbering was rebuilt from scratch: **contiguous NB 1–34, no gaps**, and **Data Science now precedes Real-world I/O** (removing the long-standing pandas forward-reference from the ETL/SQL notebooks).

### 11.1 What changed structurally
- **Module 2 ↔ Module 3 swapped**: Module 2 is now *Data Science* (`02_data_science/`, NB 7–11), Module 3 is *Real-world I/O* (`03_real_world_io/`, NB 12–13). Folder names, module READMEs, quizzes (`quiz_02` ↔ `quiz_03`), the onboarding diagrams/tables, learning paths, and the time estimator were all updated; pandas is now a stated prerequisite of the API/SQL notebooks instead of a 🔭 preview.
- **Gaps closed**: the placeholders at NB 9 (Pydantic — folded into the SQL notebook) and NB 25 (config & secrets — folded into NB 22) no longer leave holes; every number 1–34 exists.
- **Slides renamed** to match their companion notebooks (`26_digital_transformation` … `30_llm_fundamentals`); subtitles updated and all decks recompiled.
- **Fast track unchanged** (its own 1–9 numbering); its back-references to canonical notebooks were remapped.

### 11.2 Old → new map
| Old | New | Notebook |
|---|---|---|
| 1–6 | 1–6 | Foundations (unchanged) |
| 10, 11, 12, 13, 14 | **7, 8, 9, 10, 11** | pandas, NumPy, matplotlib, statistics, time series |
| 7, 8 | **12, 13** | APIs & HTTP, SQL |
| 15, 16, 17 | **14, 15, 16** | sklearn, model evaluation, feature engineering |
| 18, 19, 20, 21, 22 | **17, 18, 19, 20, 21** | AI workflows, embeddings, agents, documents, AI evaluation |
| 23, 24 | **22, 23** | notebook→project, scheduling |
| 26, 27 | **24, 25** | Capstones A & B |
| 28, 29, 30, 31 | **26, 27, 28, 29** | digital transformation, architecture, AI-assisted dev, BPM/governance/POC→MVP |
| 32, 33, 34, 35, 36 | **30, 31, 32, 33, 34** | LLM fundamentals, setup→first POC, three POCs, RAG deep dive, vector DB + agentic AI |
| 9, 25 | — | gaps eliminated (content folded into NB 13 / NB 22) |

### 11.3 Verification
Reference checker green over the whole repo (contiguous 1–34, no stale tokens); every notebook's H1 matches its filename; all 64 notebooks parse; the full execution set re-run clean after the renumber; all six decks recompile with 0 errors / 0 overfull boxes. `docs/` keeps historical numbering by design (this report, sections 1–10); `previous_versions/` untouched.

---

## 12. Final full-course review (latest-library runtime pass)

A fresh end-to-end review against the **current** scientific stack — pandas **3.0.3**, scikit-learn **1.8**, matplotlib **3.10.9**, NumPy 2.x, torch **2.12**, transformers **5.10** — to confirm the course still runs on the libraries a learner installs today, plus an independent content sweep across all 64 notebooks.

### 12.1 Runtime — clean on the latest stack
All **64 notebooks executed fresh** end-to-end (`scripts/run_all_notebooks.py`): **61 pass, 3 xfail** (the intentional 🐞 Debug-me puzzles in NB 1, NB 6, and fast-track 01), **0 unexpected errors**. No pandas-3 / sklearn-1.8 / numpy-2 deprecation breaks surfaced — the notebooks already use modern idioms (`"ME"` offsets, `default_rng`, `sparse_output`, `get_feature_names_out`, `tick_labels=`). Reference checker green; counts verified against the README (34 main, 11 appendices, 6 quizzes, 9 fast-track content notebooks).

### 12.2 Two correctness fixes applied
- **`llm_providers.py` docstring** advertised a non-existent OpenAI model (`o-mini`) and listed vague Anthropic/Google names (`claude-haiku`, `gemini-flash`) that aren't valid API IDs — while the class defaults and notebooks correctly use full versioned IDs. Rewritten so the docstring matches the real defaults (`gpt-4o-mini`, `claude-haiku-4-5-20251001`, `gemini-2.0-flash`); a learner copying a name from the header now gets a name that resolves.
- **NB 10 (statistics) `ab_report`** built the difference-CI from a **z** critical value while reporting a **Welch's t-test** p-value — so the CI and the p-value could disagree at the significance boundary (the exact failure a "safe to send to a manager" report must not have). Switched the CI to the **Welch–Satterthwaite t** critical value (`stats.t.ppf`, already taught earlier in the notebook), with a one-line comment explaining why. Re-executed: module runs 9/9 clean.

### 12.3 Confirmed clean (no change needed)
Independent module-by-module sweeps (onboarding+foundations, data science, I/O+ML, AI engineering, production+capstones, business-AI+POCs, fast-track+quizzes+requirements) found the rest of the course correct: all 30 quiz answer keys verified correct; NB 30's Transformer math (attention, √dₖ scaling, cross-entropy) and NB 33's cosine-similarity worked examples check out; no stale cross-references; no placeholders, TODOs, or untranslated leftovers; capstones self-contained and top-to-bottom runnable. Remaining Module 8↔9 overlaps are the intentional seminar-vs-hands-on split already signposted in §10.

### 12.4 Verification (pass 12)
Reference checker green; 64/64 notebooks parse; fresh full execution 61 pass / 3 xfail / 0 errors on the current library stack; `llm_providers` imports cleanly with corrected docstring; both edits confirmed on disk.
