# Module 1 — Foundations

**Goal:** Become fluent enough to read and write Python without friction. By the end of this module you will not be looking up "how do I make a list?" anymore.

**Estimated time:** 9–12 hours of focused study (six notebooks of ~30–60 min each, plus exercises and mini-projects).

**Prerequisites:** None — Notebook 1 starts from zero.

> 🧭 **Where this fits in the AI-automation picture.** This is the skill-building base of the course's spiral: you saw the destination in `00c` (and the *why* in NB 43) — these six notebooks are the Python you need before any of it. Every later module (pandas, ML, RAG, agents, the POCs) leans on what you build here.

```
   types  ──►  control  ──►  lists  ──►  dicts  ──►  functions  ──►  classes
   (NB 1)       (NB 2)      (NB 3)     (NB 4)      (NB 5)         (NB 6)
                                                                     │
                                                                     ▼
                                                              every later module
```

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll learn / build |
|---|---|---|---|---|
| 1 | `01_python_basics.ipynb` | ~30–40 min | Beginner | Variables, core types, arithmetic, f-strings → a daily **KPI report for an AI support bot** |
| 2 | `02_control_structures.ipynb` | ~35–45 min | Beginner | `if`/`for`/`while`, `try/except` → a **ticket-triage rules engine** with a retry loop |
| 3 | `03_lists_data_structures.ipynb` | ~35–45 min | Beginner | Indexing, slicing, list comprehensions, tuples → a **support-queue & latency-log analysis** |
| 4 | `04_dictionaries_advanced.ipynb` | ~35–45 min | Beginner | Dicts, JSON, counting & grouping → a **defensive API-response parser** and LLM message lists |
| 5 | `05_functions_modules.ipynb` | ~35–45 min | Beginner | Functions, `*args`/`**kwargs`, scope, lambdas, imports → a reusable **parse → clean → cost → report toolkit** |
| 6 | `06_classes_and_oop.ipynb` | ~45–60 min | Beginner / Intermediate | Classes, dunders, `@dataclass`, inheritance → a **`TodoList` class** + the `fit`/`transform` patterns behind scikit-learn |

## Notebook guides

### 01 · Python Basics for AI, Automation, and Business Data Science — `01_python_basics.ipynb`

The gentle on-ramp: storing values, doing arithmetic, formatting text — "the small things" that are *most* of the code you write in a real project. Rather than meeting each tool in isolation, the whole notebook builds toward one deliverable: a **daily KPI report for an AI support bot** — the kind of summary you'd paste into a Slack channel each morning (*how many tickets did the bot answer, what did it cost, what was the ROI?*). Every section adds exactly the piece the report needs next, and in §8 it all snaps together.

The notebook also plants the course's single most important mental model — a variable is **an arrow (a name) pointing at an object, not a box holding a value** — and includes a "📚 How to study this notebook" section that doubles as the study guide for the whole course.

**Learning objectives:**
- Run code in a Jupyter notebook and understand how execution order works
- Create variables of the five core types (`int`, `float`, `str`, `bool`, `None`) and convert between them
- Do arithmetic correctly — the difference between `/`, `//`, `%`, and `**`
- Manipulate text with string methods and **f-strings**
- Build a small, well-formatted report from raw numbers
- Recognise and fix the most common beginner errors

**Sections:** 1 What is a Jupyter notebook? · 2 Variables — naming pieces of data · 3 F-strings — formatting reports and prompts · 4 Core data types · 5 Arithmetic — pricing AI workloads · 6 Strings — the universal data type · 7 Updating variables — the accumulator pattern · 8 Applied example — the daily KPI report, at last · 9 Common pitfalls

**Practice:** 3 ✋ checkpoints · 🔮 predict-the-output · 4 practice exercises (incl. a 🐞 debug-me) · 4 stretch exercises · 🎁 bonus mini-project: *Forecasting an AI automation budget*

### 02 · Control Structures: Automating Decisions — `02_control_structures.ipynb`

Notebook 1 stored values; now Python learns to **act on** them — make decisions, repeat work, and survive messy real-world data without crashing. The running example is an **AI support-bot triage system**: code that decides, for each incoming customer message, whether the bot should *auto-respond*, *draft a reply for a human agent*, or *route straight to a person*. You start with a single `if` (§2), loop over a whole batch of tickets (§3), make the loop survive bad data (§7), and assemble the full triage pipeline in §8.

The guiding mental model is an **assembly line**: `if/elif/else` is a fork in the belt, `for` is the conveyor itself, `while` keeps the line running until a stop signal, and `try/except` is the safety net for jammed items. Along the way, "🔬 What actually happens" deep dives cover truthiness (the complete falsy list) and how a `for` loop desugars to `while True` + `next`.

**Learning objectives:**
- Read and write Python's indentation-based block syntax confidently
- Branch with `if / elif / else`; combine conditions with `and`, `or`, `not`, and chained comparisons
- Iterate with `for` loops over both counters (`range`) and real data — plus `enumerate`
- Repeat work with `while` loops, including safe retry/backoff patterns
- Control loop flow with `break` and `continue`
- Catch errors gracefully with `try / except` and build an end-to-end ticket-triage pipeline

**Sections:** 1 Indentation — the "shape" of code · 2 `if / elif / else` — the first fork in our triage system · 3 `for` loops — from one ticket to a whole batch · 4 `while` loops — repeat *until* a condition becomes false · 5 `break` and `continue` — fine-grained control of the belt · 6 Nested loops — for table-shaped work · 7 Handling errors gracefully — `try / except` · 8 Putting it all together — the triage pipeline, assembled

**Practice:** 3 ✋ checkpoints · 🔮 predict-the-output · 5 practice exercises (incl. a 🐞 debug-me) · 4 stretch exercises · 🎁 bonus mini-project: *Year-by-year token budget*

### 03 · Lists & Sequence Structures: Records, Logs, and Batches — `03_lists_data_structures.ipynb`

One variable holds one value; real work has *many* — and sequences (lists, tuples, strings) are how Python organises them. They're also the bedrock beneath the NumPy arrays and pandas DataFrames coming later. The running scenario: you've inherited the data behind a small SaaS support desk — a **queue of support tickets**, a column of **call latencies** from monitoring, and a **roster of customers** — and your job all notebook long is to slice, filter, reshape, and summarise those batches.

The mental model is a **numbered row of boxes on a conveyor belt**: indexing reaches into one box, slicing lifts off a contiguous run, a comprehension runs the whole belt past you and keeps what you want. The finale (§11) tackles the most famous list bug there is: `b = a` does **not** copy a list — mutation vs rebinding, aliasing, and why "shallow" copies aren't always enough.

**Learning objectives:**
- Create, access and modify Python lists
- Master **indexing and slicing** — the most important syntax in data science
- Use the key list methods (`append`, `extend`, `insert`, `remove`, `pop`, `sort`, …)
- Write concise **list comprehensions** for filtering and transformation
- Know when to use a **tuple** (immutable) instead of a list, and work with strings as sequences
- Use **nested lists** for small tables — and know when to graduate to pandas

**Sections:** 1 What is a list? — one box per record · 2 Indexing — reaching into one box · 3 Slicing — lifting off a chunk of the belt · 4 Modifying lists — the queue changes · 5 List methods — the everyday toolkit for a growing queue · 6 Iterating over the queue — a recap from Notebook 2 · 7 List comprehensions — filter the batch in one line · 8 Tuples — when a record must *not* change · 9 Strings as sequences — the same belt, one character per box · 10 Nested lists — laying the roster out as a table · 11 Common pitfalls — and the one that bites everyone

**Practice:** 4 ✋ checkpoints · 🔮 predict-the-output · 5 practice exercises (incl. a 🐞 debug-me) · 4 stretch exercises · 🎁 bonus mini-project: *Mini log analyser*

### 04 · Dictionaries: JSON, APIs, and LLM Messages — `04_dictionaries_advanced.ipynb`

A great deal of real data isn't ordered — it has **structure**, and the dictionary (key → value pairs looked up by name) is Python's tool for it. The running example follows a single customer record, `C-00482`, through a realistic AI workflow: it starts as a plain CRM record, becomes a model **config**, gets parsed back out of a JSON **API response**, is folded into a list of **LLM chat messages** (`{"role": "user", "content": ...}`), and finally joins a batch of records you count, group, and report on. As the intro puts it: if you only learn one new data structure in this course, make it this one — it's the backbone of JSON, LLM messages, configuration, and pandas rows.

The mental model is a **labelled filing cabinet**: you never search drawer-by-drawer, you read the label and go straight there — and §2 opens up the machinery (hashing) that makes lookups fast and explains why keys must be immutable.

**Learning objectives:**
- Create dictionaries, access values by key, and add/update/delete entries safely
- Use **`.get()`** to handle missing keys without crashing
- Iterate over keys, values, and items; write **dict comprehensions**
- Nest dictionaries to model real-world structured data (JSON, API payloads, LLM messages)
- Use dictionaries to **count and group** — the bedrock of analytics
- Decide when to use a list vs a dict vs a list of dictionaries

**Sections:** 1 What is a dictionary? — the filing cabinet · 2 Accessing values — reading a drawer · 3 Adding, updating, removing — the record grows up · 4 Iterating — walking every drawer · 5 Dict comprehensions — build a cabinet in one line · 6 Nested dictionaries — our record, as JSON · 7 Counting and grouping — the dictionary's killer app · 8 List of dicts — the "small table" pattern · 9 JSON round-trip — the API workflow · 10 List vs dict vs list-of-dicts — choosing the right shape · 11 Common pitfalls

**Practice:** 4 ✋ checkpoints · 🔮 predict-the-output · 5 practice exercises (incl. a 🐞 debug-me) · 4 stretch exercises · 🎁 bonus mini-project: *JSON-shaped customer report*

### 05 · Functions and Modules: Building a Reusable Toolkit — `05_functions_modules.ipynb`

Whenever you find yourself copy-pasting the same lines, wrap them in a function — in AI-driven work you call the same API hundreds of times, parse the same response shape, clean the same kinds of input. The running project is a small **toolkit for an LLM batch-processing job**: it starts with a single `call_cost` function (§1), gains flexibility through defaults and variadic arguments (§3–5), learns the scope rules that keep helpers from stepping on each other (§6), gets documented with docstrings and type hints (§7–8), and in §11 four helpers are *composed* into a real **parse → clean → cost → report** pipeline.

The mental model: a function is a **machine on a workbench** — arguments enter the input hopper, the body works in a private workspace (its local scope), `return` is the output chute. That one picture explains the call stack, LEGB name resolution, local-vs-global, and why mutable defaults leak.

**Learning objectives:**
- Define and call functions with positional, default, and keyword arguments
- Use **`*args`** and **`**kwargs`** for flexible signatures
- Understand **local vs global scope** and the *mutable default* trap
- Write **docstrings** and **type hints** that serve as living documentation
- Use **lambdas** in `sorted` / `max` / `filter` calls
- Import from the standard library and compose small functions into a clean pipeline

**Sections:** 1 Why functions? — the first tool on the bench · 2 Defining and calling a function — the machine on the bench · 3 Parameters with defaults — sensible settings, overridable · 4 Returning multiple values — handing back a whole summary · 5 Variadic functions — `*args` and `**kwargs` · 6 Scope — what `x` means depends on *where* · 7 Docstrings — describe what your machine does · 8 Type hints — optional, but very helpful · 9 Lambdas — tiny one-line machines · 10 Importing — borrowing other people's machines · 11 Putting it together — the toolkit becomes a pipeline

**Practice:** 4 ✋ checkpoints · 🔮 predict-the-output · 5 practice exercises (incl. a 🐞 debug-me) · 4 stretch exercises · 🎁 bonus mini-project: *A modular feedback-cost reporter*

### 06 · Classes and Object-Oriented Programming — `06_classes_and_oop.ipynb`

Functions bundle a *behaviour*; classes bundle **data + behaviour** into a single unit you can copy, pass around, and extend — the last piece of core Python before the rest of the course, where OOP shows up everywhere (Pydantic models, scikit-learn estimators, matplotlib axes, your own `MockLLM` in Module 6). The running example is one humble **SaaS `Customer`** object growing up: it starts as a loose dict surrounded by helper functions (§1), becomes a proper class with `self` and methods (§3), learns to print and compare itself with `__repr__`/`__eq__` (§5), shrinks to a one-liner with `@dataclass` (§6), and finally reveals the patterns the whole data-science stack is built on (§8: a `Dataset` wrapper, a `fit`/`transform` transformer hierarchy, a `fit`/`predict` estimator).

The mental model, used throughout: **a class is a blueprint, an instance is the concrete thing built from it** — attributes are what an object *knows about itself*, methods are what it *can do*.

**Learning objectives:**
- Explain what a class is and how it differs from a dict, a function, and an instance
- Define a class with `__init__`, attributes, and methods — including the `self` parameter
- Write `__repr__` and `__eq__` dunder methods so your objects play nicely with `print`, `==`, and lists
- Use **`@dataclass`** to skip the boilerplate when you just want a value-object
- Subclass an existing class to extend its behaviour (light-touch inheritance)
- Decide when a class is the right tool — and when a function or a dict is better

**Sections:** 1 Why classes? — when functions + dicts aren't enough · 2 Mental model — class as blueprint, instance as concrete thing · 3 Defining a class — `__init__` and `self` · 4 Methods vs free functions — which to use? · 5 Dunder methods — `__repr__` and `__eq__` · 6 `@dataclass` — Python's shortcut for value-objects · 7 Inheritance — extending an existing class · 8 Classes in data science — the patterns you'll actually use · 9 When to use a class vs a dict vs a function · 10 Mini-recap

**Practice:** 4 ✋ checkpoints · 🔮 predict-the-output · 5 practice exercises (incl. a 🐞 debug-me) · 5 stretch exercises · 🎁 bonus mini-project: *a `TodoList` class*

## How these notebooks work

Every notebook opens with a Colab badge and a metadata line (module · estimated time · difficulty), then teaches in a steady rhythm: short prose-first sections, each followed by runnable cells, with **✋ Quick exercise (~2 min)** checkpoints embedded right where a concept lands. Solutions are collapsible (`<details>` blocks) and were executed in a fresh kernel, so what you see is what actually runs. Each lesson ends with a 🔮 predict-the-output warm-up, 🧪 practice exercises (⭐ difficulty-rated, always including a "Debug me 🐞"), 🧠 stretch exercises, a 🎁 bonus mini-project, key takeaways, and a ✅ self-assessment checklist. All six notebooks run **100% offline** and are fully self-contained — no datasets to download, no API keys; every ticket queue, latency log, and customer record is generated inline.

## Where next

→ **Module 2 — Data Science** (`../02_data_science/07_pandas_fundamentals.ipynb`) — the first real use of your new OOP fluency: a pandas `DataFrame` is exactly the kind of object you just learned to read, with attributes (`df.shape`), methods (`df.groupby()`), and dunder magic (`df["col"]`) everywhere.
