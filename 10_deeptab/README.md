# Module 10 — DeepTab (optional)

**Goal:** Meet the modern deep-learning toolkit for *structured* data. Gradient-boosted trees (XGBoost/LightGBM) still win most tabular problems — but **DeepTab** ([OpenTabular/DeepTab](https://github.com/OpenTabular/DeepTab)) wraps 15 deep architectures (Mamba, FT-Transformer, SAINT, NODE, TabM, ResNet…) behind a clean scikit-learn API, and unlocks things trees can't: **distributional regression**, **learned embeddings**, and end-to-end multimodal models.

**Estimated time:** 1–2 hours.

**Prerequisites:** Module 4 (NB 14 sklearn basics, NB 16 feature engineering) and the Module 4 PyTorch appendices **A1–A3**. Appendix **A5** (conformal prediction) pairs naturally with the uncertainty section.

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

## Notebook at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll build |
|---|---|---|---|---|
| 38 | `38_deeptab_tabular_deep_learning.ipynb` | ~60–90 min | Intermediate → Advanced | One customer-churn table, many tools through one socket: a churn **classifier** benchmarked against a `HistGradientBoosting` baseline, a revenue **regressor**, a **distributional (LSS)** model with an uncertainty band, row **embeddings** via `.encode()`, and two ways to **tune** — all through DeepTab's sklearn-style API |

## Notebook guide

### 38 · DeepTab: Deep Learning for Tabular Data — `38_deeptab_tabular_deep_learning.ipynb`

For two decades, tabular data — the spreadsheets, transaction logs and feature stores that run most of a business — has belonged to gradient-boosted trees. The notebook opens by taking that seriously: on the median tabular benchmark, XGBoost/LightGBM are still the thing to beat. But architectures designed *specifically for tables* — FT-Transformer, SAINT, NODE, TabM, ResNet, and sequence models such as Mamba — now match or beat boosting on large, complex datasets, and they natively do things trees cannot: predict full distributions, learn reusable row embeddings, fuse tables with text/image towers, and transfer-learn across tables. **DeepTab** (from the OpenTabular project) wraps 15 stable models behind a single scikit-learn `BaseEstimator` API, each shipping as a matching `<Name>Classifier` / `<Name>Regressor` / `<Name>LSS` trio.

The notebook's mental model is *one socket, many power tools*: the sklearn `.fit`/`.predict` interface is the wall socket, the gradient-boosted tree is the trusty cordless drill you grab first, and DeepTab's architectures are specialist tools that plug into the same socket — swapping `MambularClassifier` for `FTTransformerClassifier` is a one-word change. A single synthetic customer-churn frame (tenure, monthly charges, support tickets, contract type, region) runs through every section: you predict churn, predict revenue, get an uncertainty band, and pull row embeddings from it.

It also showcases DeepTab **v2's split-config API**: instead of one long list of keyword arguments, a model is configured through three small objects — `MambularConfig` (architecture), `PreprocessingConfig` (input handling) and `TrainerConfig` (the training loop) — and because everything is a `BaseEstimator`, nested params like `model_config__d_model` drop straight into `RandomizedSearchCV`.

**Learning objectives:**
- Decide **when** a tabular deep-learning model is worth it versus a gradient-boosted tree (spoiler: try the trees first)
- Train a **classifier** and a **regressor** with DeepTab's sklearn-style `.fit` / `.predict` / `.predict_proba` API, and swap architectures by name
- Use **distributional regression (LSS)** to predict full distributions and reason about uncertainty for risk and pricing
- Extract **latent embeddings** with `.encode()` and feed them to a downstream model
- **Tune** hyperparameters with both DeepTab's built-in `optimize_hparams` and sklearn's `RandomizedSearchCV`

**Sections** (the notebook's arc, group by group):

*Setup & the offline gate*
- 🔌 Smoke test: is DeepTab installed? — imports `deeptab` and sets the single `HAS_DEEPTAB` flag every later cell branches on
- The offline stand-in — drop-in classes with DeepTab v2's exact constructors and methods, backed by small sklearn neural nets
- One factory, two backends — `make_classifier(...)` & friends return real or stand-in models, so the rest of the notebook never needs another `if HAS_DEEPTAB`

*Why — and on what data*
- 1 · The value proposition — and when *not* to use it — the "start with gradient boosting" discipline: the drill already in your hand
- 2 · A synthetic business dataset (churn) — build and eyeball the mixed-type table (tenure/charges/tickets + contract/payment/region)

*The core sklearn-style API*
- 3 · Classification with `MambularClassifier` — honest `HistGradientBoosting` baseline first, then the deep model, then swapping the architecture by class name (✋ threshold tuning for churn)
- 4 · Regression with `MambularRegressor` — same socket, continuous `revenue` target

*What trees can't do natively*
- 5 · Distributional regression (LSS) with `MambularLSS` — why a distribution beats a point estimate; per-row `(mean, σ)` for risk/pricing/inventory (✋ stock to the 90th percentile)
- 6 · Latent embeddings via `model.encode(X)` — dense row vectors for similarity search and downstream models (✋ find the most similar customer)

*Making it good*
- 7 · Hyperparameter tuning — (a) built-in Bayesian `optimize_hparams`, (b) sklearn `RandomizedSearchCV` with nested `model_config__d_model` params
- 🧪 Exercises · 🧠 Key takeaways · ✅ Self-assessment · 🚀 Next step

**Models covered:** `MambularClassifier`, `MambularRegressor`, `MambularLSS` trained in-notebook, each configured via the v2 split-config trio (`MambularConfig` + `PreprocessingConfig` + `TrainerConfig`); one-line-swap siblings named for every architecture (`FTTransformerClassifier`, `TabTransformerClassifier`, `ResNetClassifier`, `MLPClassifier`, `SAINTClassifier`, `TabMClassifier`, `NODEClassifier`, …); `HistGradientBoostingClassifier` as the tree baseline to beat.

**Practice:** 3 ✋ quick exercises (~2 min each, collapsible solutions) — threshold tuning for churn, stock to the 90th percentile, find the most similar customer — plus 6 end-of-notebook 🧪 exercises (architecture bake-off, bigger data, Poisson vs normal LSS families, embeddings-for-retrieval, real tuning, and a conformal-prediction stretch pairing with NB A5). Reference-style module, so exercises are a numbered list — no ⭐ ratings, Debug-me or 🎁 mini-project here.

**Datasets:** one synthetic **customer-churn** table (400 rows), generated inline with `make_classification` plus categorical `contract` / `payment` / `region` columns and an engineered churn signal; a continuous **revenue** target derived from it powers the regression and LSS sections. Nothing is downloaded.

**Offline behaviour:** the whole notebook branches on a single `HAS_DEEPTAB` flag. Without `deeptab` installed, drop-in stand-in classes mimic the v2 estimators — same split-config constructors and methods, backed by sklearn `MLPClassifier`/`MLPRegressor` behind an ordinal encoder; `.encode()` returns last-hidden-layer activations, the LSS stand-in returns per-row `(mean, σ)` with a constant residual σ, and `optimize_hparams` is a no-op. `pip install deeptab` (pulls PyTorch + Lightning) swaps in the real Mamba/Transformer models with no other code changes.

## Folder artifacts

`lightning_logs/` (version_0…3) and `model_checkpoints/` (`best_model*.ckpt`) are by-products of running the notebook with the real `deeptab` installed — PyTorch Lightning writes training logs and best-model checkpoints there. Safe to browse or delete; they regenerate on the next real training run.

## How this notebook works

Module 10 is **optional** and written in the reference style of the appendices: it focuses on *seeing* a library at work, with ✋ checkpoint exercises (collapsible solutions) at the key decision points rather than a drill-heavy exercise block. It runs **100% offline end-to-end** — the sklearn stand-in keeps every cell executable so you can study the API shape and the GBMs-first reasoning now, and installing `deeptab` later upgrades the same code to the genuine deep models:

```bash
pip install deeptab     # optional — pulls torch + lightning
```

The disciplines the notebook keeps hammering:

- **Try gradient boosting first.** On small/medium tabular data, a tuned GBM is usually the bar to beat — on the 400-row churn table it holds its own, exactly as the rule predicts. Deep tabular models earn their keep with **large data, multimodal inputs, transfer, or distributional needs**.
- **Predict distributions, not just points.** For pricing, risk, demand and inventory, the *spread* matters as much as the mean — that's what the `*LSS` variants give you. Pair with conformal prediction (A5) for calibrated intervals.
- **One API, many architectures.** Swapping `MambularClassifier` → `FTTransformerClassifier` is a one-word change — so benchmark several, don't marry the first.

## Where next

→ This is the end of the optional track. Loop back to **Module 4 — Machine Learning** (`../04_machine_learning/`) to compare against tree ensembles, or to **Module 5 — Industry Applications** (`../05_industry_applications/`) to put churn/demand/risk models into a business context.
