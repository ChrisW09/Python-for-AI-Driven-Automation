# Module 7 — Industry Applications

> 🧭  [◀ Deep Learning with PyTorch](../06_pytorch/)  ·  [🏠 Course home](../README.md)  ·  [AI Engineering ▶](../08_ai_engineering/)

**Goal:** Apply everything from Modules 1–5 to the four use-case families that dominate business data science in practice — and learn the one pattern they share: *model → money → decision*.

**Estimated time:** 10–12 hours of focused study.

**Prerequisites:** Modules 1–5 (especially NB 17–19 — models, honest evaluation, pipelines; NB 11 returns for the forecasting half).

> 🧭 **Where this fits.** Modules 1–5 taught the *tools*; this module is the *job*. Every notebook starts from a business question, ends in a costed decision rule, and carries its own classic failure mode (post-outcome leakage, the accuracy trap, unscaled clustering, unshifted rolling features). It's also deliberately interview-shaped: these four applications are what "tell me about a project" questions are made of.

```
   NB 23  Churn, CLV & retention     →  who is leaving, what are they worth,
                                        who gets the offer?
   NB 24  Fraud & anomaly detection  →  0.5 % positives, asymmetric costs,
                                        an alert queue sized by analyst capacity
   NB 25  Segmentation & recommenders → which customers are similar,
                                        what should each see next? (unsupervised!)
   NB 26  Forecasting & maintenance  →  how much to stock, when to service —
                                        forecasts and sensors become schedules
```

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | Business problem | What you'll build |
|---|---|---|---|---|---|
| 17 | `23_churn_clv_retention.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Who is leaving, what are they worth, who gets the €60 retention offer? | CLV table, expected-value targeting rule, budget-constrained retention campaign simulation |
| 18 | `24_fraud_anomaly_detection.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Catch 0.5 % fraud with ~50 analyst reviews a day | Supervised + Isolation Forest detectors, precision@k alert queue, €-prevented accounting |
| 19 | `25_segmentation_recommenders.ipynb` | ~2 h 50 m | ⭐⭐ (stretch ⭐⭐⭐) | Which kinds of customers do we have, and what should each see next? | RFM + k-means segmentation with named personas, item-item recommender that beats the popularity baseline |
| 20 | `26_demand_maintenance.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | How much to stock, and when to service the machines? | Promo-aware demand forecasts → safety stock & newsvendor orders; sensor-based maintenance schedule |

*Times are the full study budgets from the course overview (`00b`): ~40–45 min core reading plus ~30 min practice, ~1 h of stretch work and ~30 min bonus. Stars use the course's exercise scale — ⭐ warmup, ⭐⭐ standard, ⭐⭐⭐ stretch.*

## Notebook guides

### 17 · Churn, Customer Lifetime Value & Retention Targeting — `23_churn_clv_retention.ipynb`

**The business case notebook.** HelpDeskAI, a subscription support-bot platform, sells three plans; finance supplies the monthly fee and gross margin per plan, marketing supplies a retention offer that costs **€60 per customer** and historically saves **~30 %** of the churners it reaches. NB 17 trained the churn classifier and NB 18 evaluated it honestly — this notebook closes the loop that actually matters: compute what a customer is *worth* (the capped geometric-series CLV, `margin × 1/churn`), derive the offer threshold from euros instead of gut feeling, and simulate a **€18,000** retention campaign under three targeting strategies.

Along the way a threshold sweep on six customers shows why the profit-optimal cutoff isn't 0.5, a profit curve answers "how many offers *should* we send?", and the honest closing section names what was deliberately left out — starting with the uplift caveat ("sleeping dogs").

**Learning objectives:**
- Compute **customer lifetime value (CLV)** for a contractual (subscription) business and explain its assumptions.
- Turn churn probabilities into an **expected-value targeting rule** with a break-even threshold derived from offer cost, save rate, and CLV.
- Simulate a **budget-constrained retention campaign** and compare targeting strategies by realized profit.
- Explain the **uplift caveat**: why high churn risk ≠ high persuadability, and what "sleeping dogs" are.
- Spot **post-outcome leakage** — the classic way churn models look spectacular and then fail in production.

**Sections:**
1. The business: HelpDeskAI, a subscription support-bot platform
2. What is a customer worth? CLV for subscriptions
3. The churn model — NB 17's classifier, production-shaped
4. From probability to decision — the expected-value rule
5. The campaign — €18,000 budget, three targeting strategies
6. How many offers *should* we send? The profit curve
7. What this notebook did *not* solve (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: The 0.99-AUC trap") · 4 🧠 stretch exercises (⭐⭐–⭐⭐⭐, from calibration-vs-money to a first two-model uplift approach) · 🎁 bonus mini-project: the retention playbook memo · ✅ self-assessment checklist.

**Datasets:** Synthetic HelpDeskAI customer base — 4,000 subscription customers across Basic/Pro/Enterprise plans, generated inline with a seeded `default_rng`; the campaign simulation draws save outcomes with its own seed. No files needed, fully offline.

### 18 · Fraud & Anomaly Detection — `24_fraud_anomaly_detection.ipynb`

Fraud is where Module 5's classification skills get stress-tested: positives are **0.5 %** of the data, the two error types have wildly asymmetric costs, the adversary adapts to your model, and the deliverable is not a metric — it's a **review queue** that a small team of human analysts (~50 case reviews per day) can actually work through. The notebook opens with the world's laziest fraud detector scoring 99.5 % accuracy while catching zero fraud — the accuracy trap, dissected box-by-box with the confusion matrix — then rebuilds honest measurement around precision, recall, the PR curve and precision@k.

Two detectors are then built: a cost-aware **supervised** model (`class_weight`) for when labeled history exists, and an **Isolation Forest** for the unlabeled cold start. Both feed the alert queue, where the operating point comes from analyst capacity rather than a metric, and alerts are converted into expected euros prevented.

**Learning objectives:**
- Explain why **accuracy is meaningless** at 0.5 % prevalence and what to report instead (PR-AUC, precision@k, recall@k).
- Train a cost-aware **supervised** detector with `class_weight` and pick the operating point from **analyst capacity**, not from a metric.
- Use **Isolation Forest** for the unlabeled cold-start case and explain how it isolates anomalies.
- Convert alerts into euros with an **expected-loss-prevented** calculation.
- Recognize **concept drift** and explain the rules + model + feedback-loop architecture real fraud teams run.

**Sections:**
1. The data: 90 days of payments
2. The accuracy trap — see it once, never fall for it again
3. Supervised detector — when you have labeled history
4. Isolation Forest — when you have *no* labels yet
5. The alert queue — where metrics meet staffing
6. What production fraud systems add (the honest section)

**Practice:** 3 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: The 99.6 %-accurate disaster") · 4 🧠 stretch exercises (⭐⭐–⭐⭐⭐: drift, per-segment queues, rank-ensembling, the selective-labels problem) · 🎁 bonus mini-project: the morning alert digest · ✅ self-assessment checklist.

**Datasets:** Synthetic payments log — 30,000 transactions over 90 days with ≈0.5 % fraud following three planted patterns (stolen-card night spending, new-device takeovers with high amounts, rapid geo-velocity), generated inline; fully offline.

### 19 · Customer Segmentation & Recommenders — `25_segmentation_recommenders.ipynb`

The course's introduction to **unsupervised learning**. Everything so far predicted a label; this notebook answers two label-free questions every commercial team asks — *"which kinds of customers do we have?"* (segmentation) and *"what should we show each of them next?"* (recommendation). The stage is a B2B webshop run by HelpDeskAI's parent company — office & IT supplies, 12 products, 1,200 business customers, 18 months of orders — with four behavioural archetypes planted in the data generator that you must *recover* without ever being told they exist.

RFM quintile scoring comes first ("segmentation you can build before lunch"), then k-means done properly — including a from-scratch assign/update loop on a tiny 2-D example, cross-checked against sklearn — and the step everyone skips: profiling and *naming* the clusters. The second half builds an item-item collaborative-filtering recommender ("customers who bought X also bought…") and evaluates it honestly with hit-rate@k against the popularity baseline.

**Learning objectives:**
- Build an **RFM segmentation** (recency, frequency, monetary) — the 40-year-old workhorse that still runs most retention email programs.
- Use **k-means** properly: scale first, choose k with the elbow *and* silhouette, then **profile and name** the clusters.
- Explain why clustering without scaling silently becomes "sort by revenue".
- Build an **item-item collaborative-filtering** recommender with cosine similarity and beat the popularity baseline.
- Evaluate a recommender offline with **hit-rate@k / leave-one-out** — and say honestly what offline metrics can't tell you.

**Sections:**
1. The data: a B2B webshop's order history
2. RFM — segmentation you can build before lunch
3. K-means — letting the data draw the lines
4. Profile, then *name* — the step everyone skips
5. The recommender — "customers who bought X also bought…"
6. Is it any good? Hit-rate@k against the popularity baseline
7. When *not* to personalize (the honest section)

**Practice:** 3 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: The revenue-sorted 'clusters'") · 4 🧠 stretch exercises (⭐⭐–⭐⭐⭐: segment stability under resampling, migration early-warning, popularity-backed hybrid CF, both kinds of cold start) · 🎁 bonus mini-project: the segment one-pager · ✅ self-assessment checklist.

**Datasets:** Synthetic 18-month order log — 1,200 B2B customers × 12 products drawn from four planted behavioural archetypes, generated inline with a seeded `default_rng`; fully offline.

### 20 · Demand Forecasting & Predictive Maintenance — `26_demand_maintenance.ipynb`

The operations double feature. **Part I** turns NB 11's forecasting craft into stock orders: a distributor's three SKUs of very different character (a steady seller, a weekday-driven B2B item, a promo-sensitive impulse product) over two years of daily demand, where promotions are *planned* — a known-future feature, not a surprise. Three forecasters (seasonal-naive, Holt-Winters, lag-feature gradient-boosted regression) face one honest backtest on the last 8 weeks; forecast error (σ) then becomes **safety stock** for a target service level, and the **newsvendor** critical ratio Cu / (Cu + Co) sets the order quantity. The same recipe is re-run on real demand with the UCI Bike Sharing dataset.

**Part II** turns sensor streams into repair schedules: 40 machines report daily temperature and vibration, the target is *"fails within the next 7 days"*, features are shifted rolling windows (the no-peeking rule), the split is machine- and time-aware, and the alert threshold is priced from downtime vs false-alarm costs — the cost song's third verse.

**Learning objectives:**
- Forecast SKU-level demand three ways — **seasonal-naive**, **Holt-Winters**, and **lag-feature regression** that handles promotions — and backtest them honestly.
- Convert forecast error (σ) into **safety stock** for a target service level, and explain the z-score behind it.
- Set an order quantity with the **newsvendor** logic: critical ratio = Cu / (Cu + Co).
- Build a **predictive-maintenance** classifier ("fails within 7 days") from rolling sensor features with a machine-aware, time-aware split.
- Choose the maintenance alert threshold from **downtime vs false-alarm costs**.

**Sections:** *Part I — Demand forecasting that ends in a purchase order:*
1. The data: 2 years of daily demand, 3 SKUs, with promotions
2. Three forecasters, one honest backtest
3. From forecast error to safety stock
4. How much to order? The newsvendor in four lines (+ 📊 the same recipe on real demand — UCI Bike Sharing)

*Part II — Predictive maintenance: sensors → repair schedule:*

5. The data: 40 machines, one year of daily telemetry
6. Rolling features + the split that respects reality
7. The maintenance decision — third verse of the cost song
8. What real maintenance programs add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: The forecaster that knew too much") · 4 🧠 stretch exercises (⭐⭐–⭐⭐⭐: promo valuation, forecast-the-total-or-sum-the-parts, lead-time uncertainty, cumulative failure curves → schedule) · 🎁 bonus mini-project: the Monday S&OP one-pager · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline: 3-SKU × 2-year daily demand with planned promotions, and 40-machine daily telemetry (temperature + vibration with pre-failure drift). Plus one real dataset: **UCI Bike Sharing** — daily Washington D.C. rentals 2011–2012 with weather/calendar drivers — bundled at `../data/bike_sharing_daily.csv` (CC BY 4.0) and loaded locally, so the notebook still runs offline.

## How these notebooks work

Each lesson follows the same rhythm: short teaching sections punctuated by **✋ Quick exercise (~2 min)** checkpoints with collapsible `<details>` solutions, plus 🔮 predict-the-output and 🔬 "what actually happens" cells that make you commit to an answer before running the code; a 🧠 one-screen story recap; then the graded work — 🧪 practice exercises (⭐-rated, always including a **Debug me 🐞**), 🧠 stretch exercises and a 🎁 bonus mini-project — closing with a ✅ self-assessment checklist. All data is generated inline (plus one bundled CSV), so everything runs **100 % offline**. The module leans directly on Modules 2 & 4 — the pandas/plotting/statistics craft and the sklearn/evaluation/pipeline discipline — and hammers four shared lessons across its notebooks: a probability is not a decision (scores become actions only via costs — break-even thresholds in NB 23, queue capacity in NB 24, service levels and critical ratios in NB 26); respect time or your metrics lie (temporal splits, shifted rolling features); beat the dumb baseline first (always-legit in NB 24, popularity in NB 25, seasonal-naive in NB 26); and unsupervised output only becomes a business object once you profile, name, and stability-check it (NB 24, NB 25).

## Where next

→ **Module 8 — AI Engineering** (`../08_ai_engineering/28_ai_workflows.ipynb`) if you haven't done it yet — LLMs layered on top of exactly these workflows.
→ **Capstone A** (`../15_capstones/47_capstone_analytics.ipynb`) to prove the analytics half end-to-end.

---

📝 **Finished this module?** Test yourself with the [Module 7 quiz](../quizzes/quiz_07_industry_applications.ipynb) — five questions, ~10 minutes.
