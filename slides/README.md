# Slides

Lecture decks in the HSBI house style (LaTeX Beamer, Madrid theme, 16:9).

> **Philosophy.** The **notebooks are the single source of truth** for content. Slides exist only for the parts of the course taught as a *lecture* in front of a room — the conceptual / seminar material — where pacing a class through a scrolling notebook is awkward. The **hands-on modules (Python, data science, ML, AI engineering, production, the Module 9 POC builds, the Module 7 industry applications, and the Module 10 agents/tools/MCP notebooks) are taught live from the notebook itself** (run a cell, change a number, break something on purpose) — they deliberately have no slides. The decks here are deliberately *thin*: framing, diagrams, and key points, pointing back into the notebooks for the detail. Keep them that way to avoid the two-sources-of-truth drift.

## Decks

| Deck | Lecture | Companion notebook |
|---|---|---|
| `00_course_overview` | Orientation: the big picture, structure (modules 0–19), learning paths, how to study (checkpoints · quizzes · fast track), what you'll build | Module 0 (onboarding) |
| `49_digital_transformation` | Why AI now · tasks-not-jobs · maturity model · change strategies · adoption pitfalls | NB 49 |
| `50_architecture_patterns` | Single-tier → 3-tier → service-oriented → microservices · **frontend↔backend interaction with FastAPI** (request/response cycle + code) · the ML pipeline · choosing the right size | NB 50 |
| `51_ai_assisted_software_development` | IDEs · Git & pull requests · prompt patterns for code · the four failure modes · the 60-second review | NB 51 |
| `52_bpm_governance_poc_mvp` | BPM lifecycle · RACI for AI · POC → MVP → Production · three case studies · the readiness checklist | NB 52 |
| `27_llm_fundamentals` | Tokens · parameters · next-token prediction · the Transformer & attention · prompting · limitations | NB 27 |

The five lecture decks were added in the 2026 review pass and are numbered after their companion notebook (`27`, `49`–`52`); `00_course_overview` is the original onboarding deck, last revised for the **module 0–19** structure (adding Compound AI Evaluation and Containers & Docker, and refreshing the 117-notebook / 322-checkpoint / 17-quiz counts). There are intentionally **no decks for the hands-on modules** — teach those from the notebooks.

> ⚠️ **The overview deck states counts** (modules, lessons, labs, appendices, notebooks, checkpoints, quizzes) on its structure and study slides, and the four generated infographics encode the module list. Both go stale the moment a module is added. After any structural change, update `MODULES` / `DEPS` / `SHORT` in [`../scripts/generate_course_images.py`](../scripts/generate_course_images.py), rerun it, and re-check those numbers in `00_course_overview.tex` against [`../README.md`](../README.md), which is the source of truth.

**Structural infographics.** The overview deck's roadmap, dependency-graph, learning-paths and weekly-timeline PNGs in `images/` are *generated*, not drawn — after any module renumber or addition, edit the `MODULES` / `DEPS` / `PATHS` / `WEEKS` tables at the top of [`../scripts/generate_course_images.py`](../scripts/generate_course_images.py), rerun it (`.venv/bin/python scripts/generate_course_images.py`), and recompile the deck.

## Speaker notes & presenter view

Every deck carries **speaker notes** on its content frames: a time estimate, the
one point the slide must land, a question to put to the room, and the
misconception to pre-empt. They are written for someone teaching the slide
cold.

Each deck therefore builds two ways:

| PDF | What it is | Use it for |
|---|---|---|
| `<deck>.pdf` | the slides alone — **notes compiled out entirely** | projecting |
| `<deck>_notes.pdf` | double-width: slide on the left, notes on the right | your laptop / presenter screen |

Open the `_notes` PDF on your screen and the normal deck on the projector, or
use a PDF viewer's presenter mode with the double-width file on the second
display.

> The notes never reach the projected deck: `\note{...}` renders only when the
> deck is built with `\notesmode` defined, so `<deck>.pdf` is byte-for-byte the
> deck it always was.

## Building

A full TeX install (`pdflatex`) is all you need. The `Makefile` runs both
passes (so the section-navigation bar and table of contents resolve) and builds
both variants:

```bash
make                                   # every deck + every presenter deck
make slides                            # just the projected decks
make notes                             # just the presenter decks
make 27_llm_fundamentals.pdf           # one deck
make 27_llm_fundamentals_notes.pdf     # one presenter deck
make clean                             # remove LaTeX aux files (keeps PDFs)
```

By hand, if you prefer — note the second pass:

```bash
pdflatex 27_llm_fundamentals.tex
pdflatex 27_llm_fundamentals.tex      # second pass for the nav bar + TOC

# presenter version
pdflatex -jobname=27_llm_fundamentals_notes \
         "\def\notesmode{}\input{27_llm_fundamentals.tex}"
```

All decks compile cleanly in both modes (no errors, no slide overflow). They are
also Overleaf-ready — upload the `.tex` (and the `images/` folder for the
overview deck); Overleaf builds the projected deck by default.

## House style

The preamble matches `00_course_overview.tex`: `\documentclass[aspectratio=169,11pt]{beamer}`, Madrid theme, a horizontal **section-navigation bar** in the headline, auto-generated section "Outline" slides (`\AtBeginSection`), `booktabs` tables, and rounded blocks with **no shadows** (shadows render as black boxes on Overleaf). Content is in English to match the course; each `\begin{frame}` is kept to one physical slide.

Every preamble also carries the four-line `\ifdefined\notesmode` block that
enables presenter view. Copy it into any new deck, and put a `\note{...}` inside
each content frame, just before `\end{frame}` — title, "Contents" and the
auto-generated "Outline" frames deliberately have none. Keep notes in the house
voice: **a time estimate, the point, a question for the room, the misconception
to pre-empt** — written so a stand-in lecturer could teach the slide cold.
