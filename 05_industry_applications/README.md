# Module 5 — Industry Applications

**Goal:** Apply everything from Modules 1–4 to the four use-case families that dominate business data science in practice — and learn the one pattern they share: *model → money → decision*.

**Estimated time:** 10–12 hours of focused study.
**Prerequisites:** Modules 1–4 (especially NB 14–16 — models, honest evaluation, pipelines; NB 11 returns for the forecasting half).

> 🧭 **Where this fits.** Modules 1–4 taught the *tools*; this module is the *job*. Every notebook starts from a business question, ends in a costed decision rule, and carries its own classic failure mode (post-outcome leakage, the accuracy trap, unscaled clustering, unshifted rolling features). It's also deliberately interview-shaped: these four applications are what "tell me about a project" questions are made of.

```
   NB 17  Churn, CLV & retention     →  who is leaving, what are they worth,
                                        who gets the offer?
   NB 18  Fraud & anomaly detection  →  0.5 % positives, asymmetric costs,
                                        an alert queue sized by analyst capacity
   NB 19  Segmentation & recommenders → which customers are similar,
                                        what should each see next? (unsupervised!)
   NB 20  Forecasting & maintenance  →  how much to stock, when to service —
                                        forecasts and sensors become schedules
```

## Notebooks (run in order)

| # | Notebook | What you'll build |
|---|---|---|
| 35 | `17_churn_clv_retention.ipynb` | CLV table, expected-value targeting rule, budget-constrained retention campaign simulation |
| 36 | `18_fraud_anomaly_detection.ipynb` | Supervised + Isolation Forest detectors, precision@k alert queue, €-prevented accounting |
| 37 | `19_segmentation_recommenders.ipynb` | RFM + k-means segmentation with profiles, item-item recommender that beats the popularity baseline |
| 38 | `20_demand_maintenance.ipynb` | Promo-aware demand forecasts → safety stock & newsvendor orders; sensor-based maintenance schedule |

## The four mental models you should leave with

1. **A probability is not a decision.** Every application converts scores into actions via costs: break-even thresholds (35), queue capacity (36), campaign budgets (35/36), service levels and critical ratios (38).
2. **Respect time or your metrics lie.** Temporal splits, shifted rolling features, frozen bin edges — the same discipline in three costumes (35, 36, 38).
3. **Beat the dumb baseline first.** Always-honest (36), popularity (37), seasonal-naive (38) — if the model can't beat them, ship the baseline.
4. **Unsupervised needs naming.** Clusters and anomalies only become business objects when you profile them, name them, and check they're stable (36, 37).

## Where next

→ **Module 6 — AI Engineering** (`../06_ai_engineering/22_ai_workflows.ipynb`) if you haven't done it yet — LLMs layered on top of exactly these workflows.
→ **Capstone A** (`../13_capstones/41_capstone_analytics.ipynb`) to prove the analytics half end-to-end.
