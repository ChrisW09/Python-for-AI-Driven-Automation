# previous_versions/

This folder is an **archive**. Nothing in here is part of the current course.

Before the 2026 refinement pass, the course shipped as a flat list of 19 numbered notebooks at the repo root, alongside their own `data/`, `slides/`, and `requirements.txt`. That layout is preserved verbatim under [`flat_19_notebook_layout/`](./flat_19_notebook_layout/) so any old bookmarks, blog posts, or course links keep resolving.

If you've landed here looking for the course itself, you want the parent directory:

- 🚀 [`../00_onboarding/00_master_onboarding.ipynb`](../00_onboarding/00_master_onboarding.ipynb)
- 🗺️ [`../00_onboarding/00b_course_overview.ipynb`](../00_onboarding/00b_course_overview.ipynb)
- 📚 [`../README.md`](../README.md)

## What's in here

```
previous_versions/
├── README.md                          ← you are here
│
└── flat_19_notebook_layout/           ← the pre-2026 course
    ├── 01_python_basics.ipynb         ← NB 01 — 19 in a flat list
    ├── …
    ├── 19_scheduling_orchestration.ipynb
    ├── data/                          ← original CSVs (identical to the canonical data/)
    ├── slides/                        ← older technical-deck slides (different from slides/00_course_overview.pdf)
    ├── requirements.txt               ← legacy requirements (subset of the canonical one)
    ├── llm_providers.py               ← local copy so the legacy NB 11 keeps working standalone
    └── README.md                      ← the original top-level README
```

You may also see folders like `_residual_*_to_delete/` here — those are leftover macOS-locked files from the reorganisation (LICENSE duplicates, `.pyc` caches, `.DS_Store`). They're safe to delete from the Finder whenever you get around to it; they have no effect on the active course.

## Why keep this around?

Three reasons:

1. **Reproducibility.** If anyone has notes, screenshots, or downstream notebooks that reference the old paths, they still work.
2. **Diffability.** You can compare the legacy NB 7 (`07_numpy_fundamentals.ipynb` in the flat layout) with its successor (`03_data_science/11_numpy_fundamentals.ipynb`) to see exactly what the refinement pass changed.
3. **No content was lost.** The current course supersedes everything here; this folder ensures nothing was deleted.

## What's excluded from the helper scripts

The helper scripts in `../scripts/` (`check_nb_references.py`, `run_all_notebooks.py`) **skip** this folder. References inside these notebooks point to other files inside the same folder, which would otherwise produce false positives when the link checker walked here.
