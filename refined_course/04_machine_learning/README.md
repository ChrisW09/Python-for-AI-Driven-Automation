# Module 4 — Machine Learning

**Goal:** Train your first models with scikit-learn, evaluate them *honestly*, and learn the feature-engineering moves that separate a 0.65 R² from a 0.85.

**Estimated time:** 6–8 hours.
**Prerequisites:** Modules 1–3. Especially NB 11 (NumPy shapes) and NB 13 (statistics — for the metrics).

```
                  ┌────────────────────────────────────────┐
                  │  fit → predict → evaluate → iterate    │
                  └────────────┬───────────────────────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                              ▼
    NB 15 — sklearn basics            NB 16 — model evaluation
    Churn prediction + NPS            Confusion matrix, ROC, calibration,
    regression end-to-end             cross-validation, learning curves
                ▲
                │
          NB 17 — feature engineering
          Encoding, scaling, dates,
          target leakage, selection
```

## Notebooks

| # | Notebook | What you'll build |
|---|---|---|
| 15 | `15_sklearn_basics.ipynb` | Customer-churn classifier + NPS regression |
| 16 | `16_model_evaluation.ipynb` | Honest model-evaluation toolkit |
| 17 | `17_feature_engineering.ipynb` | Real feature pipelines on tabular data |

## The disciplines this module trains

- **Always split.** Train on train, score on held-out test. Never the other way round.
- **Never tune on test.** Use cross-validation for tuning; touch the test set once at the end.
- **Read the confusion matrix, not just accuracy.** Asymmetric costs change which metric matters.
- **Probabilities ≠ labels.** `predict_proba` carries information `predict` throws away.
- **Avoid target leakage** — the single most common cause of "too-good-to-be-true" results.

## Where next

→ **Module 5 — AI Engineering** (`../05_ai_engineering/18_ai_workflows.ipynb`)
