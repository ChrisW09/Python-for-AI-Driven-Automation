# Companion slides

A 61-slide LaTeX Beamer deck that walks through the whole course — one section per
notebook module, with the same business-AI framing and the same figures the course
uses internally.

## Files

| File | What it is |
|---|---|
| `course_slides.tex` | The deck source (~700 lines, English, 16:9 Madrid theme) |
| `course_slides.pdf` | The compiled deck (~1.5 MB) |
| `images/*.png` | 15 figures generated from the same code patterns as the notebooks |

## Compile from source

```bash
cd slides
pdflatex course_slides.tex     # run twice to resolve TOC and section bar
pdflatex course_slides.tex
```

Tested with TeX Live 2022+. The deck uses Latin Modern (`lmodern`) fonts which
ship with every standard TeX distribution.

## Regenerate the figures

The figures in `images/` are produced by a single Python script in the
`outputs/build/` folder of the course repo (`build_slide_figures.py`). It uses
only `numpy`, `pandas`, `matplotlib`, and `scikit-learn` — the same libraries
the course teaches. To rebuild them after editing:

```bash
python build_slide_figures.py
```

All 15 PNGs land back in `slides/images/`.

## Design notes

- **Madrid theme** with a horizontal section navigation bar at the top of every
  slide. The entries are clickable in the PDF — you can jump straight between
  sections.
- **One idea per slide** — frames are split aggressively so nothing overflows.
- **Three block styles** map to the course's tone:
  *block* (definitions), *exampleblock* (worked examples), *alertblock* (pitfalls).
- **Code is real**, not pseudocode — every snippet runs as-is in the matching
  notebook.

## How to use the deck

- **Self-study companion** — open it next to the notebooks for a visual map of
  what each section is about.
- **Workshop / classroom** — projects well; one section per ~60-minute session.
- **Pitch / overview** — slides 1–7 are a self-contained 5-minute overview of
  the entire course.
