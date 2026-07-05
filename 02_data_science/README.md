# Module 2 — Data Science

> 🧭  [◀ Foundations](../01_foundations/)  ·  [🏠 Course home](../README.md)  ·  [Real-world I/O ▶](../03_real_world_io/)

**Goal:** Master the library stack that powers every analytical Python codebase — pandas, NumPy, seaborn/matplotlib, statsmodels — plus the statistics you need to interpret what they show you.

**Estimated time:** 8–10 hours of focused study (core lessons 7–11; the optional forecasting appendices add ~4–5 hours more).

**Prerequisites:** Module 1 (functions, comprehensions).

> 🧭 **Where this fits.** Module 1 gave you Python; this module turns data into *insight* — the analytical half of every AI-automation project, and the groundwork for the I/O, machine-learning and AI-engineering modules that follow.

```
       pandas        ◄──►   NumPy           ◄──►  seaborn/matplotlib
   (NB 7 — tables)         (NB 8 — math)         (NB 9 — plots)
                                  │
                                  ▼
                              Statistics
                          (NB 10 — making
                           sense of the numbers)
                                  │
                                  ▼
                            Time series
                          (NB 11 — forecasting)
                                  │
                                  ▼  (optional deep-dives)
                     Forecasting appendices A1 → A4
                  (ARIMA/ETS → Prophet & libraries →
                   deep learning → foundation models)
```

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll learn / build |
|---|---|---|---|---|
| 7 | `07_pandas_fundamentals.ipynb` | ~30–40 min | Beginner | DataFrames end to end — inspect, slice, filter, derive columns, `groupby`, plot — on an LLM API-call log, answering *"what is driving our API spend?"* |
| 8 | `08_numpy_fundamentals.ipynb` | ~35–50 min | Beginner / Intermediate | Arrays, boolean masks, broadcasting, axis aggregation — building to a vectorised latency A/B test of two LLM providers |
| 9 | `09_matplotlib_basics.ipynb` | ~35–50 min | Beginner | Charts in 1–3 lines with pandas `.plot()` + seaborn (`hue=`, `ax=`) — building to a 2×2 AI-ops executive dashboard |
| 10 | `10_statistics_basics.ipynb` | ~55–75 min | Beginner / Intermediate | Mean vs median, confidence intervals, t-tests, effect size, sample-size planning — one honest A/B test, unfolding |
| 11 | `11_time_series_forecasting.ipynb` | ~60–75 min | Intermediate | Resampling, rolling windows, decomposition, forecast baselines + Holt-Winters, walk-forward backtesting — a 90-day forecast you can defend |

## Optional appendices at a glance

The A-series is an optional specialised forecasting track that deepens Notebook 11. Appendices are written in *reference style* — demos of real libraries rather than fully scaffolded lessons — and every one runs end-to-end offline via a built-in stand-in; installing the real library just swaps the stand-in for the real thing.

| Appendix | Notebook | ⏱ Time | Focus |
|---|---|---|---|
| A1 | `A1_forecasting_classical.ipynb` | ~75–90 min | ARIMA / SARIMA / ETS deep dive — stationarity, ACF/PACF, residual diagnostics, rolling-origin CV |
| A2 | `A2_forecasting_prophet_libraries.ipynb` | ~60–75 min | Prophet, NeuralProphet, sktime, Darts, Nixtla — when to reach for which |
| A3 | `A3_forecasting_deep_learning.ipynb` | ~75–90 min | LSTM + Transformer forecasters in PyTorch, from scratch |
| A4 | `A4_forecasting_foundation_models.ipynb` | ~45–60 min | TimesFM, Chronos, TabPFN-TS — zero-shot pretrained forecasters |

## Notebook guides

### 07 · Pandas Fundamentals: Your First Real DataFrame — `07_pandas_fundamentals.ipynb`

You can do real data work with the lists and dicts from Module 1 — but past a handful of rows it hurts: no column labels, a hand-written loop for every filter. What you want is a **proper table you can program**, and that is pandas. One running dataset carries the whole notebook — a log of LLM API calls (model, token usage, cost, latency, customer segment) — and one business question keeps getting asked: *"What is actually driving our API spend?"* Each new pandas tool is introduced as the next move in answering it: build the table, inspect it, slice it, filter to the expensive calls, derive a cost column, group by model, then plot the answer.

The mental model to keep: a DataFrame is a **spreadsheet you can program** — rows are records, columns are `Series`, and every operation hands back a new table or column you can keep working on. Two "🔬 What actually happens" interludes demystify `.loc` vs `.iloc` and boolean masks, and a ⚠️ pitfall box covers chained indexing and the `ChainedAssignmentError`.

**Learning objectives:**
- Build a `DataFrame` from a dict and from a CSV.
- Inspect a new dataset with the standard "first five commands".
- Select columns and rows (`.loc` vs `.iloc`).
- Filter rows with **boolean masks** — the pandas idiom.
- Add derived columns from formulas and compute aggregates by category with `groupby`.
- Draw a first plot directly from a DataFrame.

**Sections:** 1 The pandas mental model · 2 Creating a DataFrame from a dict · 3 Inspecting a DataFrame · 4 Selecting columns · 5 Selecting rows — `loc` vs `iloc` · 6 Filtering — the boolean-mask idiom · 7 Adding and modifying columns · 8 Summary statistics & `value_counts` · 9 `groupby` — the most useful pandas verb · 10 Reading and writing CSV files · 11 A first plot — `df.plot()` · 12 The pandas patterns you'll see everywhere

**Practice:** 4 ✋ quick-exercise checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. a "Debug me 🐞") · 4 🧠 stretch exercises (⭐⭐⭐: growth rates, pivot tables, IQR outlier detection) · 🎁 mini-project: *A one-page report on `api_log.csv`*.

**Files/datasets:** The lesson body is self-contained (the demo CSV is embedded via `StringIO`); the 🎁 mini-project loads the repository's `../data/api_log.csv` (50 LLM API calls) from disk and saves an enriched copy back out.

### 08 · NumPy Fundamentals: Vectorised Math for AI Workloads — `08_numpy_fundamentals.ipynb`

NumPy is the bedrock of the Python data-science ecosystem — pandas, scikit-learn, TensorFlow and PyTorch all store data as NumPy arrays under the hood. For AI work specifically, *everything* (token counts, costs, latencies, probabilities, embeddings, model weights) eventually lives in an array. The running example is the **latencies of our LLM API calls**: first a few raw call times, then a matrix of 3 models × 4 latency stats, building up to an end-of-notebook A/B test of two providers.

The one mental model behind all of it: an array is **one flat, typed block of memory**, not a Python list of boxed objects — the speed, slices-as-views behaviour, broadcasting, and `dtype` surprises all follow from that single fact. "🔬 What actually happens" deep-dives cover why `arr * 2` beats a Python loop and walk the broadcasting algorithm step by step.

**Learning objectives:**
- Create and inspect NumPy arrays (`shape`, `dtype`, `ndim`).
- Index and slice 1-D and 2-D arrays, including with **boolean masks**.
- Perform **vectorised arithmetic** and use **ufuncs**.
- Understand **broadcasting** — how arrays of different shapes combine.
- Aggregate **along an axis** (`axis=0` vs `axis=1`); reshape, stack, and split arrays.
- Generate **reproducible** random data with `default_rng` and apply it all to a cost-and-latency analysis.

**Sections:** 1 Why NumPy? · 2 Creating arrays · 3 Inspecting an array — meet the running dataset · 4 Indexing and slicing · 5 Vectorised arithmetic · 6 Broadcasting · 7 Aggregations along an axis · 8 Reshape, stack, split · 9 Random data — reproducibly · 10 Putting it all together — the latency A/B test

**Practice:** 3 ✋ quick-exercise checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. a "Debug me 🐞") · 4 🧠 stretch exercises (⭐⭐⭐: 3σ outliers, law of large numbers, rolling mean, pairwise distances via broadcasting) · 🎁 mini-project: *Simulate an A/B test of two models*.

**Files/datasets:** None — fully self-contained synthetic data.

### 09 · Visualization Basics: Great Charts in a Few Lines — `09_matplotlib_basics.ipynb`

A plot answers questions that tables cannot — and you do **not** need twenty lines of matplotlib boilerplate to get one. Modern Python gives excellent charts in 1–3 lines: pandas `.plot()` straight from the DataFrame, seaborn for statistical charts with smart defaults, and matplotlib as the engine underneath, called directly only for final tweaks. One realistic DataFrame carries the whole notebook — **500 LLM support calls** (model, channel, tokens, cost, latency, satisfaction) — and each chart type answers a new question about the same calls, building toward one deliverable: the **2×2 executive dashboard** that returns in the capstone.

The workflow to internalise: **question → one-liner → `hue=`/`ax=`** — match the chart type to the question (trend → line, categories → bar, distribution → histogram/box, relationship → scatter, matrix → heatmap), draw it in one line, then split by category or compose panels with a single argument. A closing showcase reruns the whole toolkit on a real dataset, Palmer Penguins.

**Learning objectives:**
- Draw **line, bar, scatter, histogram, and box plots in 1–3 lines** of code.
- Plot directly from a DataFrame or Series with **`.plot()`**.
- Split any chart by category with seaborn's **`hue=`** — one argument instead of a loop.
- Build a **correlation heatmap** and a **pairplot** as one-liners.
- Compose a **2×2 dashboard** by passing `ax=` to pandas/seaborn.
- Add just enough polish (title, labels, size) and **save figures to PNG**.

**Sections:** 1 Setup — three imports and one style line · 2 The dataset — 500 LLM support calls · 3 Line plots · 4 Bar charts · 5 Histograms · 6 Scatter plots · 7 Box plots · 8 Heatmaps · 9 Many charts at once (pairplot + 2×2 dashboard) · 10 Polish & saving · 11 Which tool when — and the classic pitfalls · 📊 The same toolkit on a real dataset — Palmer Penguins

**Practice:** 3 ✋ quick-exercise checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. a "Refactor me 🐞") · 4 🧠 stretch exercises (⭐⭐⭐: the everything-plot, small multiples, stacked shared-axis panels, grouped box plots) · 🎁 mini-project: *Build a 2×2 AI-ops dashboard*.

**Files/datasets:** `../data/penguins.csv` for the Palmer Penguins showcase (falls back to seaborn's built-in copy if the file isn't found); the 500-call dataset is generated in-notebook.

### 10 · Statistics That Pay for Themselves — `10_statistics_basics.ipynb`

Most data work needs very little formal statistics — but the bit you *do* need pays for itself within a week. Every section serves one concrete decision: *"We measured **Model A** (fast) against **Model B** (slow). Should we tell the team B is worse — and how confident can we be?"* The same two simulated latency datasets are carried from §2 to §8: first describe them honestly (mean vs median), then ask *is the gap real?* (CI, t-test), *is it big?* (effect size), and *did we even have enough data to ask?* (sample size). The whole notebook is one A/B test, unfolding — no theorem-proving, just careful use on the kind of data this course generates.

The tying mental model is the **sampling distribution**: your dataset is one draw from a machine that would spit out a slightly different sample every time, so the sample mean is a random variable with its own spread (`SE = σ/√n`). Confidence intervals, t-tests, p-values and power are bookkeeping on top of that one picture — the notebook even simulates the null hypothesis to show what a p-value actually is.

**Learning objectives:**
- Pick the right summary statistic (mean / median / robust stats) for a distribution.
- Read a **histogram + box plot** and explain distribution shape and tails.
- Compute a **confidence interval** for a mean by hand and with a library.
- Run a **t-test** (two-sample, two-sided) and *correctly* interpret its p-value.
- Compute an **effect size** (Cohen's *d*) and calculate the **sample size** needed to detect a chosen effect.
- Recognise the three classical statistical mistakes that ruin AI A/B tests in production.

**Sections:** 1 Setup · 2 Two latency datasets — see them before you summarise them · 3 Mean vs median — when each one lies · 4 Confidence intervals · 5 The t-test — is the difference *real*? · 6 Effect size — the number managers care about · 7 Sample size — how much data do I need? · 8 A complete A/B-test report · 9 The three classical mistakes (and the fixes)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. a "Debug me 🐞") · 4 🧠 stretch exercises (⭐⭐⭐: paired t-test, bootstrap CI, permutation test, t-test from summary stats) · 🎁 mini-project: *Power analysis dashboard*.

**Files/datasets:** None — simulated latency batches generated in-notebook.

### 11 · Time Series and Forecasting Basics — `11_time_series_forecasting.ipynb`

Most of the data a business runs on is **time-shaped** — revenue per day, tickets per hour, signups per week — yet the course has so far treated rows as exchangeable. This notebook fixes that. Everything works on **two years of one daily metric**: the support bot's *automation rate* (the share of conversations it resolves without a human), aimed at one deliverable — *"forecast that rate for the next 90 days, and prove the forecast is trustworthy."* First tame the noise (resample, roll), then expose the structure (diff, decompose), then predict (baselines → Holt-Winters), and finally test honestly (walk-forward backtest).

Two mental models to carry: **(1) a time series = trend + seasonality + noise** — almost every technique here separates those three; **(2) you train on the past and test on the *future* — never shuffle**, because the moment you scramble time order, the future leaks into training and your error estimate becomes a lie. A closing ecosystem section shows the same forecast contract in statsmodels and previews sktime and Darts.

**Learning objectives:**
- Convert string dates to `datetime`, set a `DatetimeIndex`, and select date ranges.
- **Resample** from daily → weekly → monthly with the right aggregation per column.
- Compute **rolling means** and **expanding sums** for trend smoothing.
- **Decompose** a series into trend + seasonality + residual.
- Build four forecasts: **naive**, **seasonal-naive**, and **moving-average** baselines, plus **Holt-Winters** exponential smoothing.
- Evaluate honestly with **MAE/RMSE/MAPE** and **walk-forward backtesting** — and know which baseline to beat before declaring a model "good".

**Sections:** 1 The shape of a time series · 2 Setup — generate the series · 3 Selecting by date · 4 Resampling · 5 Rolling windows · 6 Date arithmetic — `.shift` and `.diff` · 7 Decomposition · 8 Forecasting — three baselines you must beat + Holt-Winters · 9 Visualising the forecasts · 10 Evaluating — MAE, RMSE, MAPE · 11 Walk-forward backtesting · 12 The full forecast — 90 days ahead · 13 The forecasting ecosystem

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. a "Debug me 🐞") · 4 🧠 stretch exercises (⭐⭐⭐: residual anomaly detection, two horizons, MAPE/sMAPE, walk-forward backtest) · 🎁 mini-project: *A weekly forecasting report*.

**Files/datasets:** None — the two-year daily series is generated in-notebook.

## Appendix guides

### A1 · Classical Forecasting: ARIMA / SARIMA / ETS — `A1_forecasting_classical.ipynb`

The deep dive behind Notebook 11's Holt-Winters: stationarity, the Box–Jenkins family (AR, MA, ARIMA, SARIMA) and the modern state-space ETS framework, all on a synthetic 18-month series of daily product searches with weekly seasonality, an upward trend, and a one-off promo bump. You'll diagnose stationarity with ADF + KPSS, watch "🔬 What actually happens" builds of differencing and the ACF by hand, read ACF/PACF plots to pick orders, fit `SARIMAX` with prediction intervals that survive a stakeholder review, check residual diagnostics, and compare models honestly with rolling-origin cross-validation — closing with a decision rubric for picking a classical model.

**Demos:** `statsmodels` (SARIMAX, ETS) — bundled with the course requirements, so this appendix runs fully offline with no extra installs. **Practice:** 4 ✋ checkpoints · 2 🧪 exercises (add a regressor via SARIMAX's "X"; auto-search the best `(p, d, q)`).

### A2 · Prophet & Modern Forecasting Libraries — `A2_forecasting_prophet_libraries.ipynb`

A guided tour of the modern forecasting ecosystem on the *same series as A1*, so results stay comparable: **Prophet** (Meta's additive decomposition with built-in holiday handling), **NeuralProphet** (its neural successor), **sktime** (scikit-learn-style API), **Darts** (one library, dozens of models) and the **Nixtla** speed-and-scale stack (`statsforecast` / `mlforecast` / `neuralforecast`) — ending in a decision rubric for which library to reach for when.

**Demos:** Prophet, NeuralProphet, sktime, Darts, Nixtla — real-library recipes are shown as ready-to-uncomment code, while the notebook runs offline via a **Prophet-style additive decomposition** stand-in (trend + seasonal + residual, recovered with statsmodels' `seasonal_decompose` from a series with known pieces), including a "🔬 What actually happens inside Prophet" walkthrough. **Practice:** 3 ✋ checkpoints · 2 🧪 exercises (add a holiday calendar to the hand-rolled decomposition; find where Prophet *under*-performs).

### A3 · Deep-Learning Forecasting (LSTM, Transformer) — `A3_forecasting_deep_learning.ipynb`

When you have lots of related series, rich covariates, or long horizons with strong non-linearities, deep-learning forecasters genuinely move the needle. This appendix implements two forecasters **from scratch in PyTorch** — an LSTM and a Transformer-encoder — on the same demand-flavoured series as A1/A2, with a careful "🔬 What actually happens" build of time-series windowing (`(n_samples, timesteps, n_features)`, one-step vs multi-step targets, windows built by hand). It closes with reference code for the production-grade alternatives: Darts (N-BEATS, N-HiTS, TFT) and `pytorch-forecasting`.

**Demos:** PyTorch (plus Darts / pytorch-forecasting as reference code). Runs offline: all torch cells are guarded by a `HAS_TORCH` flag, so without PyTorch installed the notebook still executes end-to-end and simply skips the training cells. **Practice:** 3 ✋ checkpoints · 2 🧪 exercises (train on multiple related series; probabilistic forecast via MC dropout).

### A4 · Forecasting Foundation Models (TimesFM, Chronos, TabPFN-TS) — `A4_forecasting_foundation_models.ipynb`

In 2024 forecasting had its *ChatGPT moment*: pretrained foundation models that **zero-shot a forecast** on a series they've never seen, often matching well-tuned classical models out of the box. This appendix surveys the three you'll hear about most — **Google TimesFM** (decoder-only patch transformer pretrained on ~100 B time points), **Amazon Chronos** (reuses T5 by quantising values into tokens) and **PriorLabs TabPFN-TS** — shows each API on the same demand series as A1–A3, and finishes with an honest discussion of when foundation models beat classical and when they don't.

**Demos:** `timesfm`, `chronos-forecasting`, `tabpfn-time-series` — each shown as ready-to-uncomment API recipes. Runs offline via §6's stand-in: a strong classical baseline compared against an "ensemble of priors" proxy that mimics the pretrained-then-condition behaviour, plus a tiny offline "history in, forecast out, no fitting" analogy. **Practice:** 3 ✋ checkpoints · 2 🧪 exercises (a "cold-start" sweep; a hybrid foundation-forecast + residual-GBM model).

## How these notebooks work

Every lesson opens with a metadata line (module · estimated time · difficulty) and a 🎯 objectives list, then teaches in short sections punctuated by **✋ Quick exercises (~2 min)** with collapsible solutions, "🔬 What actually happens" internals and 🔮 predict-the-output moments. Each core lesson ends with 🧪 practice exercises (⭐-rated, including a broken-code "Debug me 🐞"), 🧠 stretch exercises, a 🎁 bonus mini-project, key takeaways and a self-assessment. Everything runs **100% offline** — datasets are generated in-notebook or shipped in `../data/`. The A1–A4 appendices are optional reference-style demos of real forecasting libraries (Prophet, PyTorch, TimesFM, Chronos, …): they run offline via built-in stand-ins, and installing the real library (heavy deps are commented out at the bottom of `requirements.txt`) is optional.

## Where next

→ **Module 3 — Real-world I/O** (`../03_real_world_io/12_apis_and_http.ipynb`)

---

📝 **Finished this module?** Test yourself with the [Module 2 quiz](../quizzes/quiz_02_data_science.ipynb) — five questions, ~10 minutes.
