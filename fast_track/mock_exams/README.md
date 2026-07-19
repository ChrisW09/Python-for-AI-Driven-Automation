# 📝 Fast Track — Mock Exams

> 🧭  [◀ Fast Track](../README.md)  ·  [🏠 Course home](../../README.md)

Three full-length **mock exams** for the [Fast Track](../README.md), each a *parallel form* that samples the whole path (NB 1–22) — take them as practice attempts or timed dry runs before an assessment. Each exam ships with a **worked-solutions slide deck** (HSBI house style, built to PDF) so you can self-mark.

To keep the three genuinely distinct, each is set in its own business world — same skills, different scenario:

| # | Exam paper | Solutions deck | Scenario | Format |
|---|---|---|---|---|
| 1 | [`exam_1.md`](./exam_1.md) | [`exam_1_solutions.pdf`](./exam_1_solutions.pdf) · [`.tex`](./exam_1_solutions.tex) | **CloudDesk** — SaaS customer support | 120 min · 100 marks · 30 Q |
| 2 | [`exam_2.md`](./exam_2.md) | [`exam_2_solutions.pdf`](./exam_2_solutions.pdf) · [`.tex`](./exam_2_solutions.tex) | **ShopSphere** — e-commerce retail | 120 min · 100 marks · 33 Q |
| 3 | [`exam_3.md`](./exam_3.md) | [`exam_3_solutions.pdf`](./exam_3_solutions.pdf) · [`.tex`](./exam_3_solutions.tex) | **PayFlow** — fintech payments | 120 min · 100 marks · 30 Q |

## Structure (every exam)

Five parts of 20 marks, mirroring the fast-track arc, each mixing **multiple-choice · short-answer · write-the-code · debug-this-code · applied-scenario**:

| Part | Coverage | Notebooks |
|---|---|---|
| **A** | Python foundations | NB 1–5 |
| **B** | Data, pandas, visualization & statistics | NB 6–9 |
| **C** | Machine learning, evaluation & feature engineering | NB 8, 16, 17 |
| **D** | AI engineering: LLM workflows, RAG, tools/agents, MCP, document AI | NB 10–14, 18 |
| **E** | Applied & production: time series, NLP, deployment, web scraping, capstone | NB 15, 19, 20, 21, 22 |

## How to use

1. **Sit the paper.** Open `exam_N.md`, give yourself 120 minutes, no notebooks open.
2. **Self-mark** against `exam_N_solutions.pdf` — the deck restates each question, gives the full worked answer with code, and (for MCQs) explains why each distractor is wrong.
3. **Follow the thread back.** Every part maps to fast-track notebooks (above) — revisit any you fumbled, then try a different scenario's paper.

## Rebuilding a solutions deck

The PDFs are committed, but to rebuild from source you need a TeX install (`pdflatex`):

```bash
cd fast_track/mock_exams
latexmk -pdf exam_1_solutions.tex     # runs the passes; produces exam_1_solutions.pdf
latexmk -c                            # tidy aux files (keeps the .pdf)
```

> Build them **one at a time** — running several `latexmk` jobs concurrently in this folder makes their cleans race and delete each other's output.

The decks use the same HSBI Beamer house style as [`../../slides/`](../../slides/) (Madrid theme, 16:9, one physical slide per question).
