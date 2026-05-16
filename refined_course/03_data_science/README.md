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

## Optional appendices — specialised forecasting

For a deep dive into time-series forecasting beyond Holt-Winters:

| Appendix | Notebook | Focus |
|---|---|---|
| A1 | `A1_forecasting_classical.ipynb` | ARIMA / SARIMA / ETS deep dive — stationarity, ACF/PACF, residual diagnostics, rolling-origin CV |
| A2 | `A2_forecasting_prophet_libraries.ipynb` | Prophet, NeuralProphet, sktime, Darts — when to reach for which |
| A3 | `A3_forecasting_deep_learning.ipynb` | LSTM + Transformer forecasters in PyTorch from scratch |
| A4 | `A4_forecasting_foundation_models.ipynb` | TimesFM, Chronos, TabPFN-TS — zero-shot pretrained forecasters |

## The four mental models you should leave with

1. **pandas: split → apply → combine.** Every analytical question is "for each X, compute Y". `groupby` is the verb.
2. **NumPy: shape is everything.** Most ML bugs are shape mismatches. `print(x.shape)` is your first debugging move.
3. **matplotlib: figure / axes.** `fig, ax = plt.subplots(...)` scales from one plot to a 12-panel dashboard.
4. **Time series: trend + seasonality + residual.** Decompose before modelling. Always beat the *seasonal-naive* baseline.

## Where next

→ **Module 4 — Machine Learning** (`../04_machine_learning/15_sklearn_basics.ipynb`)
