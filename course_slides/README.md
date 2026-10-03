# Course slides

The lecture decks of **AI-Driven Automation** (Prof. Dr. Christoph Weisser, Bielefeld School of Business, HSBI, Winter Semester 2026/27). Each deck covers several sessions, and every content slide has speaker notes.

| | Deck | What it covers | Slides | Presenter version | Source |
|---|---|---|---|---|---|
| 1 | **AI-Assisted Coding: From Idea to Working Prototype** | A ten-minute idea-to-app live demo · setting up VS Code, Git, GitHub & Copilot · working with a coding agent · how apps are built (frontend, backend, database, APIs) · three POCs that build on each other: a **Streamlit** data app → a **FastAPI + SQLite** three-tier app → an **XGBoost** churn model behind the API | [PDF](./01_ai_assisted_coding.pdf) | [PDF + notes](./01_ai_assisted_coding_notes.pdf) | [`.tex`](./01_ai_assisted_coding.tex) |
| 2 | **LLMs, RAG & Agentic AI** | How LLMs work · using LLMs well · limitations and risks · Retrieval-Augmented Generation · vector databases · agentic AI · AI-driven automation in practice · three hands-on LLM prototypes: a **PDF chat**, a **semantic search** and a **support agent** | [PDF](./02_llms_rag_agentic_ai.pdf) | [PDF + notes](./02_llms_rag_agentic_ai_notes.pdf) | [`.tex`](./02_llms_rag_agentic_ai.tex) |

Teach them in this order. Deck 2 reuses the plan → build → review → run → commit workflow from deck 1.

> **`course_slides/` vs. [`slides/`](../slides/).** This folder holds the main lecture series. [`slides/`](../slides/) holds the course-overview deck and the short companion decks for individual notebooks (NB 27, 49–52).

## Which PDF to open

| PDF | What it is | Use it for |
|---|---|---|
| `<deck>.pdf` | slides only | the projector, or sharing with students |
| `<deck>_notes.pdf` | double-width: slide on the left, speaker notes on the right | your laptop / presenter screen (Presentation.app, pdfpc, or any viewer with a presenter mode) |

## Building

You need a TeX distribution with `pdflatex` (TeX Live, MacTeX, or Overleaf). The decks use Fira Sans, Fira Mono, `fontawesome5`, `tcolorbox` and TikZ, which all ship with a full TeX install. `profile.jpg` (the title-slide photo) must stay next to the `.tex` files.

Run `pdflatex` twice so the navigation and cross-references resolve:

```bash
cd course_slides

# slides only
pdflatex 01_ai_assisted_coding.tex
pdflatex 01_ai_assisted_coding.tex

# presenter version (slides + notes on a second screen)
pdflatex -jobname=01_ai_assisted_coding_notes "\def\WITHNOTES{}\input{01_ai_assisted_coding.tex}"
pdflatex -jobname=01_ai_assisted_coding_notes "\def\WITHNOTES{}\input{01_ai_assisted_coding.tex}"
```

To get the same result, you can also uncomment `%\def\WITHNOTES{}` on line 2 of the deck. These decks use `\WITHNOTES` as their notes switch, while the decks in [`slides/`](../slides/) use `\notesmode`, so the `slides/` Makefile does not build them.

`images/` holds the title-slide thumbnails used in the main [README](../README.md). After you change a title slide, regenerate them:

```bash
pdftoppm -f 1 -l 1 -png -scale-to-x 800 -scale-to-y -1 -singlefile 01_ai_assisted_coding.pdf images/01_ai_assisted_coding_cover
pdftoppm -f 1 -l 1 -png -scale-to-x 800 -scale-to-y -1 -singlefile 02_llms_rag_agentic_ai.pdf images/02_llms_rag_agentic_ai_cover
```
