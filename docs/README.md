# docs/

Project artefacts. Not part of the course content — these are reference documents about *how the course was assembled*.

| File | What it is |
|---|---|
| `01_initial_execution_report.docx` | The very first end-to-end execution audit (May 2026). All 55 notebooks were executed in a fresh kernel; this report records which passed and which failed, with first-failing cell + error captured for each. |
| `02_refinement_review.docx` | A structural / hygiene audit that identified eleven refinement opportunities (numbering drift, MockLLM duplicated across notebooks, missing nbformat cell IDs, etc.) — each with evidence and a concrete fix. |
| `03_refinements_applied.docx` | The summary of the refinement pass: what was changed, what was deliberately left alone, and the verification that the post-refinement execution state matched the original (53 / 55 pass, 2 intentional Debug-me fails). |
| `04_pedagogical_audit.docx` | A pedagogical audit of the course: concept-dependency map (where each Python concept is *used* vs *explained*), premature-syntax findings, the surgical fixes applied to the foundations module, and recommendations for future revisions. |
| `05_recommendations_applied.docx` | Follow-up to the audit: each of the eight recommendations paired with what was actually built (f-strings reordered, 🧠 / 🔭 markers added, concept-introduction index, three ASCII diagrams, six module quizzes). |
| `06_final_review.docx` | The end-of-engagement review: full inventory of the repo, journey from audit 01 to here, smoke-test results by section, re-run concept-dependency audit, known limitations, and suggested next moves. |
| `07_submission_ready.docx` | The submission-readiness certificate: a 20-item checklist, the final smoke-test result, and what changed in the last polish pass (consistency fixes, marker count, exercise count, requirements.txt comments). All checklist items PASS. |
| `08_pedagogical_review_2026.md` | The 2026 first-time-learner pedagogical review: course-wide numbering/navigation repair, rerouted 'Next step' chains, correctness-bug fixes, simplified explanations, and remaining future improvements. The current state of the repo reflects everything in this report. |
| `09_module_descriptor_coverage.md` | Curriculum-alignment matrix: maps the official Modulhandbuch Lernergebnisse/Kompetenzen and Inhalte to the notebooks that deliver them, with coverage ratings and two delivery-level notes. |
| `10_course_review_2026.md` | The July 2026 course review & improvement report (formerly `COURSE_REVIEW_REPORT.md` at the repo root): the visualization pass (132 rendered figures), cell-splitting for lecturability, the post-renumber cross-reference sweep, and the correctness fixes — a historical record whose lesson/module numbers use the **pre-renumber** scheme. |
| `notebook_execution_results.json` | The most recent execution snapshot from the helper `scripts/run_all_notebooks.py`. One entry per notebook with `status`, `duration_s`, and first error (if any). Regenerate by re-running the script from the repo root. |

Reading order: 01 → 02 → 03 → … → 10 (numeric). The current state of the repo reflects everything through report 10; report 09 is the curriculum-alignment matrix.

## Output convention

Notebooks ship **with rendered outputs and figures committed** (the "render all" convention chosen in report 10): students see charts and results on GitHub/Colab without executing anything, at the cost of heavier diffs. Don't strip outputs when editing a notebook — re-run it and commit the refreshed outputs instead. The only intentional error outputs are the 🐞 Debug-me cells, each tagged `raises-exception`.

## Reproducing the execution snapshot

```bash
# from the repo root — writes docs/notebook_execution_results.json
python scripts/run_all_notebooks.py . --json docs/notebook_execution_results.json
```

The runner skips `previous_versions/` and `.venv/` automatically, executes each
notebook in memory (notebooks are never modified on disk), and exits non-zero if
any notebook errors. The intentional 🐞 *Debug-me* cells carry the
`raises-exception` cell tag, so they don't abort execution — a fully healthy run
shows `pass` for all notebooks.
