# Module 2 — Data Science

**Goal:** Master the library stack that powers every analytical Python codebase — pandas, NumPy, seaborn/matplotlib, statsmodels — plus the statistics you need to interpret what they show you.

**Estimated time:** 8–10 hours of focused study.
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
```

## Notebooks

| # | Notebook | What you'll build |
|---|---|---|
| 7 | `07_pandas_fundamentals.ipynb` | LLM-call log analysis with filter/groupby/plot |
| 8 | `08_numpy_fundamentals.ipynb` | A/B test of two LLM providers, vectorised |
| 9 | `09_matplotlib_basics.ipynb` | Charts in 1–3 lines (pandas/seaborn) + a 2×2 AI-ops executive dashboard |
| 10 | `10_statistics_basics.ipynb` | A/B-test analysis with t-tests and confidence intervals |
| 11 | `11_time_series_forecasting.ipynb` | 3-month forecast with Holt-Winters + walk-forward backtest |

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
3. **Plotting: reach for the one-liner first.** `df.plot(...)` for quick looks, seaborn's `hue=` instead of loops; matplotlib's `ax` is the escape hatch, not the starting point.
4. **Time series: trend + seasonality + residual.** Decompose before modelling. Always beat the *seasonal-naive* baseline.

## Where next

→ **Module 3 — Real-world I/O** (`../03_real_world_io/12_apis_and_http.ipynb`)
