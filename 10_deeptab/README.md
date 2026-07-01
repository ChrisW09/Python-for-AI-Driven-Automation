# Module 10 — Optional: DeepTab (Deep Learning for Tabular Data)

**Goal:** Meet the modern deep-learning toolkit for *structured* data. Gradient-boosted trees (XGBoost/LightGBM) still win most tabular problems — but **DeepTab** ([OpenTabular/DeepTab](https://github.com/OpenTabular/DeepTab)) wraps 15 deep architectures (Mamba, FT-Transformer, SAINT, NODE, TabM, ResNet…) behind a clean scikit-learn API, and unlocks things trees can't: **distributional regression**, **learned embeddings**, and end-to-end multimodal models.

**Estimated time:** 1–2 hours.
**Prerequisites:** Module 4 (NB 14 sklearn basics, NB 16 feature engineering) and the Module 4 PyTorch appendices **A1–A3**. Appendix **A5** (conformal prediction) pairs naturally with the uncertainty section.

> 📎 **Optional, reference-style module.** This notebook demos a library at work rather than drilling exercises. It **runs end-to-end offline** via a scikit-learn (`MLP` / `HistGradientBoosting`) stand-in — install `deeptab` to swap in the real models.

```
        scikit-learn API  ──►  15 deep tabular architectures
        model.fit(X, y)        Mambular · FTTransformer · SAINT · NODE
        model.predict(X)       TabM · ResNet · MLP · TabTransformer …
        model.predict_proba    each ships as  *Classifier / *Regressor / *LSS
        model.encode(X)
              │
   ┌──────────┼─────────────────────┬────────────────────────┐
   ▼          ▼                     ▼                         ▼
 classify   regress           distributional (LSS)      latent embeddings
                              predict a whole            feed into any
                              distribution, not          downstream model
                              just a point
```

## Notebook

| # | Notebook | What you'll learn |
|---|---|---|
| 38 | `38_deeptab_tabular_deep_learning.ipynb` | The DeepTab value proposition (and **when to prefer GBMs**), classification & regression with a one-line model swap, **distributional regression (LSS)** for uncertainty, latent embeddings via `encode()`, and hyper-parameter tuning (`optimize_hparams` + `RandomizedSearchCV`) |

## The disciplines this module trains

- **Try gradient boosting first.** On small/medium tabular data, a tuned LightGBM is usually the bar to beat. Deep tabular models earn their keep with **large data, multimodal inputs, transfer, or distributional needs**.
- **Predict distributions, not just points.** For pricing, risk, demand and inventory, the *spread* matters as much as the mean — that's what the `*LSS` variants give you. Pair with conformal prediction (A5) for calibrated intervals.
- **One API, many architectures.** Swapping `MambularClassifier` → `FTTransformerClassifier` is a one-word change — so benchmark several, don't marry the first.

## Install (optional — the notebook runs offline without it)

```bash
pip install deeptab     # pulls torch + lightning
```

## Where next

→ This is the end of the optional track. Loop back to **Module 4 — Machine Learning** (`../04_machine_learning/`) to compare against tree ensembles, or to **Module 5 — Industry Applications** (`../05_industry_applications/`) to put churn/demand/risk models into a business context.
