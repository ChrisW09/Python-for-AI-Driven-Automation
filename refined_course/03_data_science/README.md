# Module 3 — Data Science

**Goal:** Master the four-library stack that powers every analytical Python codebase — pandas, NumPy, matplotlib, statsmodels — plus the statistics you need to interpret what they show you.

**Estimated time:** 8–10 hours of focused study.
**Prerequisites:** Module 1 (functions, comprehensions). Module 2 is helpful for the CSV-loading examples.

```
       pandas        ◄──►   NumPy           ◄──►   matplotlib
   (NB 10 — tables)         (NB 11 — math)         (NB 12 — plots)
                                  │
                                  ▼
                              Statistics
                          (NB 13 — making
                           sense of the numbers)
                                  │
                                  ▼
                            Time series
                          (NB 14 — forecasting)
```

## Notebooks

| # | Notebook | What you'll build |
|---|---|---|
| 10 | `10_pandas_fundamentals.ipynb` | LLM-call log analysis with filter/groupby/plot |
| 11 | `11_numpy_fundamentals.ipynb` | A/B test of two LLM providers, vectorised |
| 12 | `12_matplotlib_basics.ipynb` | 2×2 AI-ops executive dashboard |
| 13 | `13_statistics_basics.ipynb` | A/B-test analysis with t-tests and confidence intervals |
| 14 | `14_time_series_forecasting.ipynb` | 3-month forecast with Holt-Winters + walk-forward backtest |

## The four mental models you should leave with

1. **pandas: split → apply → combine.** Every analytical question is "for each X, compute Y". `groupby` is the verb.
2. **NumPy: shape is everything.** Most ML bugs are shape mismatches. `print(x.shape)` is your first debugging move.
3. **matplotlib: figure / axes.** `fig, ax = plt.subplots(...)` scales from one plot to a 12-panel dashboard.
4. **Time series: trend + seasonality + residual.** Decompose before modelling. Always beat the *seasonal-naive* baseline.

## Where next

→ **Module 4 — Machine Learning** (`../04_machine_learning/15_sklearn_basics.ipynb`)
