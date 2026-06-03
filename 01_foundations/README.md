# Module 1 — Python Foundations

**Goal:** Become fluent enough to read and write Python without friction. By the end of this module you will not be looking up "how do I make a list?" anymore.

**Estimated time:** 9–12 hours of focused study.
**Prerequisites:** None — Notebook 1 starts from zero.

> 🧭 **Where this fits in the AI-automation picture.** This is the skill-building base of the course's spiral: you saw the destination in `00c` (and the *why* in NB 28) — these six notebooks are the Python you need before any of it. Every later module (pandas, ML, RAG, agents, the POCs) leans on what you build here.

```
   types  ──►  control  ──►  lists  ──►  dicts  ──►  functions  ──►  classes
   (NB 1)       (NB 2)      (NB 3)     (NB 4)      (NB 5)         (NB 6)
                                                                     │
                                                                     ▼
                                                              every later module
```

## Notebooks (run in order)

| # | Notebook | What you'll build |
|---|---|---|
| 1 | `01_python_basics.ipynb` | A KPI snapshot for an AI support bot |
| 2 | `02_control_structures.ipynb` | A ticket-triage rules engine + retry loop |
| 3 | `03_lists_data_structures.ipynb` | A latency-log analysis |
| 4 | `04_dictionaries_advanced.ipynb` | A defensive API-response parser |
| 5 | `05_functions_modules.ipynb` | A reusable cost / cleaning toolkit |
| 6 | `06_classes_and_oop.ipynb` | A `TodoList` class with full OOP fluency — closes the documented NB 6 gap |

## What "fluent" looks like at the end

You should be able to read a 50-line Python script and explain what each block does *without running it*. You should also be able to *write* a small script (under 30 lines) that loads some data, processes it with a loop and a conditional, and prints a small report — without checking documentation for syntax.

## Common pitfalls in this module

| Symptom | Likely cause | Fix |
|---|---|---|
| `IndentationError` | Mixed tabs and spaces | Pick "Convert indentation to spaces" in your editor |
| `KeyError` on a missing dict key | Forgot to use `.get()` | Replace `d["x"]` with `d.get("x", default)` |
| Mutable default trap | `def f(x=[])` | Use `def f(x=None): if x is None: x = []` |
| `name.upper()` "doesn't work" | Strings are immutable; the result was discarded | Reassign: `name = name.upper()` |

## Where next

→ **Module 2 — Real-world I/O** (`../02_real_world_io/07_apis_and_http.ipynb`)
