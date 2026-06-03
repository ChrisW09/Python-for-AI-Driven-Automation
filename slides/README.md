# Slides

Lecture decks in the HSBI house style (LaTeX Beamer, Madrid theme, 16:9).

> **Philosophy.** The **notebooks are the single source of truth** for content. Slides exist only for the parts of the course taught as a *lecture* in front of a room — the conceptual / seminar material — where pacing a class through a scrolling notebook is awkward. The **hands-on modules (Python, data science, ML, AI engineering, production, and the Module 9 POC builds) are taught live from the notebook itself** (run a cell, change a number, break something on purpose) — they deliberately have no slides. The decks here are deliberately *thin*: framing, diagrams, and key points, pointing back into the notebooks for the detail. Keep them that way to avoid the two-sources-of-truth drift.

## Decks

| Deck | Lecture | Companion notebook |
|---|---|---|
| `00_course_overview` | Orientation: the big picture, structure, learning paths, how to study, what you'll build | Module 0 (onboarding) |
| `28_digital_transformation` | Why AI now · tasks-not-jobs · maturity model · change strategies · adoption pitfalls | NB 28 |
| `29_architecture_patterns` | Single-tier → 3-tier → service-oriented → microservices · the ML pipeline · choosing the right size | NB 29 |
| `30_ai_assisted_software_development` | IDEs · Git & pull requests · prompt patterns for code · the four failure modes · the 60-second review | NB 30 |
| `31_bpm_governance_poc_mvp` | BPM lifecycle · RACI for AI · POC → MVP → Production · three case studies · the readiness checklist | NB 31 |
| `32_llm_fundamentals` | Tokens · parameters · next-token prediction · the Transformer & attention · prompting · limitations | NB 32 |

The five lecture decks (`28`–`32`) were added in the 2026 review pass; `00_course_overview` is the original onboarding deck. There are intentionally **no decks for the hands-on modules** — teach those from the notebooks.

## Building

A full TeX install (`pdflatex`) is all you need. Run twice so the section-navigation bar and table of contents resolve:

```bash
pdflatex 32_llm_fundamentals.tex
pdflatex 32_llm_fundamentals.tex      # second pass for the nav bar + TOC
# or, simpler:
latexmk -pdf 32_llm_fundamentals.tex
```

All decks compile cleanly (no errors, no slide overflow). They are also Overleaf-ready — upload the `.tex` (and the `images/` folder for the overview deck).

## House style

The preamble matches `00_course_overview.tex`: `\documentclass[aspectratio=169,11pt]{beamer}`, Madrid theme, a horizontal **section-navigation bar** in the headline, auto-generated section "Outline" slides (`\AtBeginSection`), `booktabs` tables, and rounded blocks with **no shadows** (shadows render as black boxes on Overleaf). Content is in English to match the course; each `\begin{frame}` is kept to one physical slide.
