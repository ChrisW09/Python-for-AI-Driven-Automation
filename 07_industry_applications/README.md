# Module 7 — Industry Applications

> 🧭  [◀ Deep Learning with PyTorch](../06_pytorch/)  ·  [🏠 Course home](../README.md)  ·  [AI Engineering ▶](../08_ai_engineering/)

**Goal:** Apply everything from Modules 1–5 to the four use-case families that dominate business data science in practice — and learn the one pattern they share: *model → money → decision*.

**Estimated time:** 10–12 hours of focused study (core NB 23–26); the fourteen optional appendices add ~38 h 30 m.

**Prerequisites:** Modules 1–5 (especially NB 17–19 — models, honest evaluation, pipelines; NB 11 returns for the forecasting half).

> 🧭 **Where this fits.** Modules 1–5 taught the *tools*; this module is the *job*. Every notebook starts from a business question, ends in a costed decision rule, and carries its own classic failure mode (post-outcome leakage, the accuracy trap, unscaled clustering, unshifted rolling features, confounded price elasticity). It's also deliberately interview-shaped: these applications are what "tell me about a project" questions are made of.

```
   NB 23  Churn, CLV & retention     →  who is leaving, what are they worth,
                                        who gets the offer?
   NB 24  Fraud & anomaly detection  →  0.5 % positives, asymmetric costs,
                                        an alert queue sized by analyst capacity
   NB 25  Segmentation & recommenders → which customers are similar,
                                        what should each see next? (unsupervised!)
   NB 26  Forecasting & maintenance  →  how much to stock, when to service —
                                        forecasts and sensors become schedules
   ──────────────  optional appendices  ──────────────────────────────────────
   A1     Pricing & promotion ROI    →  what should we charge, and was that
                                        discount worth it? (causal inference!)
   A2     Experiments & A/B testing  →  can this test even answer the question?
                                        (the "run a test" that A1/23/24 defer to)
   A3     Credit risk & scorecards   →  who do we lend to, how much, and what
                                        about the applicants we never approved?
   A4     Causal inference & uplift  →  did the campaign actually work, and who
                                        should get the offer? (risk ≠ persuadability)
   ──────────────  the business-function tour (A5–A8)  ───────────────────────
   A5     People analytics (HR)      →  who is leaving, what does it cost —
                                        and is the pay gap real? (censoring!)
   A6     Receivables & cash (Fin)   →  when do invoices actually pay, whom to
                                        chase, and will we need the credit line?
   A7     Sales pipeline & forecast  →  are the CRM's numbers any good, and
                                        what really lands this quarter?
   A8     Procurement & suppliers    →  where does the money go, and which
                                        supplier is *actually* good? (averages lie)
   ──────────────  growth & operations (A9–A14)  ─────────────────────────────
   A9     Marketing mix & budget     →  which channels actually create demand,
                                        and where should the €2.4M go?
   A10    Service operations         →  how many agents, at what service level —
                                        and what does the bot really save?
   A11    Routing & allocation       →  the module's first *plan*: assignments,
                                        time windows, and slack that pays
   A12    Insurance pricing          →  frequency × severity, and what happens
                                        if you refuse to differentiate
   A13    Product analytics          →  funnels, cohort curves, and the metric
                                        the team gets held to (but shouldn't)
   A14    Bandits & adaptation       →  learn while you earn — and re-break
                                        your own inference doing it
```

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | Business problem | What you'll build |
|---|---|---|---|---|---|
| 17 | `23_churn_clv_retention.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Who is leaving, what are they worth, who gets the €60 retention offer? | CLV table, expected-value targeting rule, budget-constrained campaign simulation — and expected profit checked against realized |
| 18 | `24_fraud_anomaly_detection.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Catch 0.5 % fraud with ~50 analyst reviews a day | Supervised + Isolation Forest detectors, precision@k alert queue, €-prevented accounting, and sizing the queue (a bigger one is not a better one) |
| 19 | `25_segmentation_recommenders.ipynb` | ~2 h 50 m | ⭐⭐ (stretch ⭐⭐⭐) | Which kinds of customers do we have, and what should each see next? | RFM + k-means segmentation with named personas, item-item recommender that beats the popularity baseline |
| 20 | `26_demand_maintenance.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | How much to stock, and when to service the machines? | Promo-aware demand forecasts → safety stock & newsvendor orders (which inherit any bias in the forecast beneath them); sensor-based maintenance schedule |

*Times are the full study budgets from the course overview (`00b`): ~40–45 min core reading plus ~30 min practice, ~1 h of stretch work and ~30 min bonus. Stars use the course's exercise scale — ⭐ warmup, ⭐⭐ standard, ⭐⭐⭐ stretch.*

## Optional appendices

Fourteen appendices, all written at **full lesson weight** (same rhythm and ✋/🧪/🧠 exercise ladder as NB 23–26) rather than in the reference style of the Module 2 and 5 appendices — because each sits squarely on this module's *model → money → decision* spine. They are optional only in the sense that the core four do not depend on them.

The first four close loops the core notebooks deliberately leave open. NB 23, NB 24 and A1 all end by recommending an experiment; **A2** is that experiment. NB 24 mentions the selective-labels problem in one stretch exercise; **A3** makes it the centrepiece and prices it. NB 23 warns twice that *risk is not persuadability* and sketches a two-model uplift estimator in a stretch exercise; **A4** is that warning developed into a full causal toolkit — and the reason the warning matters is measured in euros.

**A5–A8 are the business-function tour:** the same toolkit walked into the four offices the core notebooks never visit — HR, finance, sales and procurement — because "tell me about a project" interviews come from all of them, not just from marketing. Each one imports the module's lessons into a new domain and adds the failure mode native to that domain. **A5** takes NB 23's churn machinery to the employer side and discovers the snapshot lies (*censoring* — most employees haven't left yet), plus the one analysis where controls can hide the problem instead of revealing it (pay equity). **A6** is A3's direct sequel: A3 decided *who gets credit*, A6 manages what happens next — when invoices actually pay, whom the two collectors should chase, and whether the CFO needs the credit line. **A7** is the module's leakage lesson in its natural habitat — a CRM whose fields are edited *after* deals close, and whose rep-entered probabilities are the antagonist. **A8** flips NB 25/A1/A3's webshop around and walks into its *buying* office, where the classic failures are averaging away lead-time variance (NB 26's safety-stock formula prices the difference) and claiming savings on price while total cost rises.

**A9–A14 are growth & operations** — and they exist because the first eight appendices, for all their range, share a shape: predict something, threshold it, act. These six break that mould in ways the module needed. **A9** is the missing commercial function: A1 owns price and A7 owns the sales motion, but nothing owned the marketing budget, which needs two effects no other notebook has — carryover and diminishing returns — and delivers an *allocation* rather than a score. **A10** sets capacity instead of ranking within it, and brings the course its only queueing theory; its punchline is that the conversion from volume to headcount is non-linear, which is why a plan built on daily averages hits its target on paper and fails in half of all intervals. **A11** is the module's first genuine *plan under constraints* — an assignment and a sequence, where the lesson is that an optimiser answers the question you actually asked, and that the schedule which looks best on paper is the one that collapses on Tuesday. **A12** takes A3's regulated-pricing idiom somewhere A3 cannot go: a loss that is a count *times* an amount, a severity with a real tail, and a strategic trap (refuse to differentiate and your good risks leave) that has no analogue in approve/decline. **A13** works upstream of NB 23, in cohorts rather than customer-months, and asks the question that decides how a product team spends its quarter — is this metric *diagnostic* or *actionable*? **A14** closes the module's longest argument: NB 23 targeted with a model, A3 found its own decisions in its training data, A4 measured the damage, A2 randomized to fix it — and A14 shows what happens when the randomization itself adapts, which fixes the cost of learning and re-breaks the inference.

All fourteen run ~2 h 45 m at ⭐⭐ (stretch ⭐⭐⭐), and all are independent of each other — pick by the question you actually have:

| Track | Appendices | Pick one when you want… |
|---|---|---|
| **Closing the loops** | [A1](#a1--pricing-elasticity--promotion-roi--a1_pricing_promotionsipynb) · [A2](#a2--experiment-design--ab-testing-for-business-decisions--a2_experiments_ab_testingipynb) · [A3](#a3--credit-risk-scorecards-expected-loss--the-approvedecline-decision--a3_credit_risk_scorecardsipynb) · [A4](#a4--causal-inference--uplift-who-to-target-not-who-will-churn--a4_causal_upliftipynb) | the questions NB 23–26 raise and then defer — pricing, the experiment they keep recommending, regulated lending, and the causal machinery behind "risk ≠ persuadability" |
| **The business-function tour** | [A5](#a5--people-analytics-attrition-survival--pay-equity--a5_people_analyticsipynb) · [A6](#a6--finance-late-invoices-collections--the-13-week-cash-forecast--a6_finance_ar_cashflowipynb) · [A7](#a7--sales-lead-scoring-pipeline-truth--the-quarter-forecast--a7_sales_pipelineipynb) · [A8](#a8--procurement-spend-supplier-scorecards--total-cost--a8_procurement_spendipynb) | the same toolkit in the four offices the core notebooks never visit: HR, finance, sales, procurement |
| **Growth & operations** | [A9](#a9--marketing-mix--incrementality--a9_marketing_mixipynb) · [A10](#a10--service-operations-arrivals-erlang-c--the-staffing-plan--a10_service_operationsipynb) · [A11](#a11--from-prediction-to-allocation-routing-dispatch--slack--a11_routing_allocationipynb) · [A12](#a12--pricing-risk-frequency--severity--adverse-selection--a12_insurance_pricingipynb) · [A13](#a13--product-analytics-funnels-cohort-curves--the-activation-metric--a13_product_analyticsipynb) · [A14](#a14--bandits--adaptive-allocation-learning-while-you-earn--a14_bandits_adaptiveipynb) | a deliverable that is not a score: a budget, a headcount, a schedule, a rate table, a roadmap call, a policy |

#### Closing the loops — A1–A4

| Appendix | Notebook | ⏱ Time | Difficulty | Business problem | What you'll build |
|---|---|---|---|---|---|
| A1 | `A1_pricing_promotions.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | What should we charge for three very different SKUs, and was last year's promo calendar worth running? | Confound-corrected price elasticities, the headroom rule and inverse-elasticity price, a bootstrap + support-range guardrail that produces *hold / raise / test* rather than three prices, and a break-even discount rule that settles the promo P&L |
| A2 | `A2_experiments_ab_testing.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Three teams want to test something. Which of these tests can actually answer its question? | MDE-first test planning that *cancels* one test before it runs, CUPED variance reduction that doubles power for free, a peeking simulation and a boundary calibrated by Monte Carlo, SRM + multiple-comparisons validity checks, and the winner's curse quantified at two power levels |
| A3 | `A3_credit_risk_scorecards.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Who gets trade credit, how much, and what do we do about the applicants we have never approved? | A WOE/IV scorecard with IV screen, sign check and points transform, a calibration check, the `PD* = m/(m+LGD)` cutoff and profit curve, risk-banded limits priced as an overlay, reason codes for decline letters, and the selective-labels problem measured in euros |
| A4 | `A4_causal_uplift.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Last quarter's retention report says the discount backfired. Did it — and who should get it this quarter? | The naive-vs-causal decomposition computed exactly (effect + selection bias), the four uplift segments priced in euros, a T-learner with a break-even targeting depth, a difference-in-differences + placebo analysis of an un-randomized rollout, and adjustment methods shown working — then failing with the wrong sign — on targeted data |

#### The business-function tour — A5–A8

| Appendix | Notebook | ⏱ Time | Difficulty | Business problem | What you'll build |
|---|---|---|---|---|---|
| A5 | `A5_people_analytics.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Who is leaving, what does attrition actually cost — and is the pay gap real? | A hand-built Kaplan–Meier survival curve that exposes the censoring trap, an attrition bill per function (the highest *rate* is not the biggest *bill*), an honest leaves-within-12-months model with a per-function break-even threshold and a budgeted retention list, and a raw-vs-adjusted pay-gap decomposition with the mediator caveat spelled out |
| A6 | `A6_finance_ar_cashflow.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | When will these invoices actually pay, whom should the two collectors chase, and will we need the credit line? | A days-late model built on as-of features (persistence is the signal), a collections queue ranked by expected cash acceleration rather than amount, a Monte-Carlo 13-week cash forecast that turns into a credit-line decision with a probability attached, and a walk-forward backtest that prices the due-date spreadsheet's optimism in euros |
| A7 | `A7_sales_pipeline.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Are the CRM's own numbers any good — and what actually lands this quarter? | An as-of snapshot rebuild that deflates a leaked AUC 1.000 to an honest 0.853, a reliability curve that prices rep-entered probabilities, a calibrated quarter forecast with Monte-Carlo bands backtested over six quarters, and an EV-ranked lead queue with a break-even calling depth |
| A8 | `A8_procurement_spend.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Where does the €11M actually go, which suppliers are actually good, and should we consolidate the tail? | A spend cube with Pareto/ABC and a maverick-spend bill, a naive savings claim collapsed to its honest number, a supplier scorecard where lead-time *variance* is priced via NB 26's safety stock, total cost of ownership that dethrones the cheapest invoice, and a consolidation plan with payback and the dual-sourcing premium worth paying |

#### Growth & operations — A9–A14

| Appendix | Notebook | ⏱ Time | Difficulty | Business problem | What you'll build |
|---|---|---|---|---|---|
| A9 | `A9_marketing_mix.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Which channels actually create demand, and where should next year's €2.4M go? | Adstock and saturation curves fitted and recovered against planted truth, last-click's 12× ROAS on branded search set beside its true 1.72×, a marginal-return reallocation worth +€193k a year on the same budget, identification limits priced in euros, and a geo holdout that buys the answer |
| A10 | `A10_service_operations.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | How many agents does next quarter need, at what service level — and what does the deflection bot really save? | Interval-level arrival forecasting, Erlang C from scratch checked against simulation, the occupancy cliff and shrinkage in FTE and euros, a cost-optimal (not maximal) service level, and an AI-deflection business case walked from the vendor's 30% down to an honest 11.2% |
| A11 | `A11_routing_allocation.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Forty jobs, six vans, two-hour promises — what does tomorrow's schedule look like? | A travel-time model whose *error* matters more than its mean, the distance-optimal plan that misses 27 of 40 windows, a euro-optimal assignment (`linear_sum_assignment` + greedy insertion + 2-opt) that drives further and costs €4,836 less, and slack chosen from a 400-day simulation because the on-paper optimum always picks zero |
| A12 | `A12_insurance_pricing.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | What should a device-protection plan cost, and what happens if we keep charging everyone €89? | Exposure as the actuarial form of censoring, a Poisson GLM with log-exposure offset that recovers every planted relativity, a fat-tailed Gamma severity with large-loss capping, a technical rate table exposing €1.3M of cross-subsidy, and an adverse-selection death spiral simulated over renewal cycles |
| A13 | `A13_product_analytics.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Where do we lose people, is the product improving, and which metric should the team chase? | A funnel that collapses because its denominator changed, cohort curves compared at equal age (and the young-cohort censoring trap), an activation metric whose 2.75× retention lift survives adjustment at 8pp and a randomized nudge at 1.9pp, LTV with its tail assumption exposed, and two roadmap items priced |
| A14 | `A14_bandits_adaptive.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Six offers, one hero slot — should this be a bandit or an experiment? | ε-greedy, UCB1 and Thompson sampling from scratch scored in euros of regret, the adaptive-sampling bias that makes your winner's reported lift a fiction, contextual bandits as A4's online twin (with a warm start that locks onto the wrong arm), and four honest cases where a bandit is the wrong tool |

## Notebook guides

### 23 · Churn, Customer Lifetime Value & Retention Targeting — `23_churn_clv_retention.ipynb`

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

### 24 · Fraud & Anomaly Detection — `24_fraud_anomaly_detection.ipynb`

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

### 25 · Customer Segmentation & Recommenders — `25_segmentation_recommenders.ipynb`

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

### 26 · Demand Forecasting & Predictive Maintenance — `26_demand_maintenance.ipynb`

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

### A1 · Pricing, Elasticity & Promotion ROI — `A1_pricing_promotions.ipynb`

**The causal-inference notebook.** The other four take the data at face value; this one starts by refusing to. Back at NB 25's B2B webshop, the January price review is due on three SKUs of very different character — a commodity (A4 paper, €4.99, 34 % margin), a locked-in consumable (toner, €69, 43 %) and a considered big-ticket purchase (a 27" monitor, €249, 33 %) — with two years of weekly units, prices and costs. Prices moved a lot (±26 % to ±49 %), which looks like a gift until you ask *why* they moved: supplier costs track the season, the merchandiser marks up harder in peak weeks, and the flyer goes out in the trough. Every one of those habits ties price to something that also moves demand.

So the naive `log(units) ~ log(price)` regression hands back three wrong answers biased toward "customers don't care" — and on the monitor it reports **p = 0.118, R² = 0.02**, i.e. *no evidence that price affects demand*, for a product whose true elasticity is −1.15. Four controls (a Fourier seasonality pair, the promo flag, a trend) recover all three elasticities inside their confidence intervals, and a time-honest backtest (5–7 % MAPE on held-out non-promo weeks) buys the right to keep going.

Then the money. The **headroom rule** — raise the price iff |ε| · CM < 1 — gives the direction in one line, and the **inverse-elasticity rule** `p* = c · ε/(1+ε)` gives the number, cross-checked against a numeric profit grid (which also shows why the *revenue*-optimal price is always the grid's floor). The guardrails are the real lesson: bootstrap the elasticity, refuse to leave the price range you have actually charged, and remember profit is flat near its peak. The three SKUs therefore end in three *different kinds* of answer — **hold** the paper (its headroom CI straddles 1.00 and the modelled gain is €24 a quarter), **raise** the toner 28 % (+€18k/year, and volume falls 35 %, which is the politically hard part), and **run an experiment** on the monitor (its `p*` is unidentifiable to within a factor of 15). Part III turns to promotions, deriving the break-even multiplier `M* = (p−c)/((1−d)p−c)` and settling last year's calendar at **+€7.0k, +€2.6k and −€20.2k** — with the display effect explaining why the *same* 15 % discount pays for a week and loses forever.

**Learning objectives:**
- Explain **price endogeneity**, name the mechanism, and predict the *direction* of the bias from how a company sets its prices.
- Estimate a **price elasticity** from a log-log demand model with credible controls, and validate it out-of-sample before trusting it.
- Decide a price's direction in one line (**raise iff |ε| · CM < 1**) and derive the profit-maximizing price from the **inverse-elasticity rule**.
- Put **guardrails** on it: bootstrap the elasticity, respect the support of the data, and recognise a boundary solution as a request for an experiment.
- Price a **promotion** with the break-even discount rule, and separate the price effect from the **display effect**.

**Sections:**
1. The business: three SKUs, two years, one price review
2. The naive elasticity — and why it is a lie
3. Identifying the demand curve — controls that earn their keep
4. From elasticity to a price — the rule you can do in your head
5. Guardrails — the confidence interval, the support, and the flat peak
6. Was the promotion worth it? The break-even discount
7. What this notebook did *not* solve (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: The promotion that became a price cut") · 4 🧠 stretch exercises (⭐⭐⭐: cannibalisation and the portfolio optimum, instrumental variables by hand, sizing the price test, segmented pricing and the fence you could print on the invoice) · 🎁 bonus mini-project: the price-change memo · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline — 104 weeks × 3 SKUs with cost-plus prices, peak-season markups and trough-scheduled promotions, plus planted elasticities and display lifts the notebook has to recover. Uses `statsmodels` (already a course dependency); fully offline.

### A2 · Experiment Design & A/B Testing for Business Decisions — `A2_experiments_ab_testing.ipynb`

**The notebook the rest of the module keeps promising.** NB 23 wants a randomized holdout for uplift, NB 24 raises selective labels, A1 §5 concludes that the monitor needs a price test rather than a price — each time the recommendation is "run an experiment," and each time we moved on. This is that experiment, and the framing is deliberately unflattering: **most A/B tests run in industry cannot answer the question they were built to answer**, for reasons knowable before the test starts.

The organising idea is that an experiment is a **measuring instrument with a resolution**. Three teams at the webshop want to test something — a checkout redesign (2,500 sessions/week), a loyalty offer (1,200 customers), and A1's monitor price rise (12 regions) — and §2's minimum-detectable-effect calculation immediately **cancels the first one**: at that traffic a 4-week test resolves ±0.99 pp against a hypothesis of +0.5 pp, so its answer ("no significant difference") was knowable in advance and would have been wrong.

The loyalty test then carries the notebook. Its raw analysis reports **+5.5 %, p = 0.27, CI [−4.3 %, +15.3 %]** and recommends shutting down an offer that genuinely lifts revenue **9 %** — a false negative the simulation puts at ~61 %. **CUPED** fixes it for free: pre-period revenue correlates 0.82 with post, variance falls by ρ² ≈ 66 %, and power goes **39 % → 86 %** on the same customers in the same eight weeks. Then the ways a live test goes wrong: peeking turns a 5 % test into a **23 %** test (weekly looks only get it to ~15 %), and a per-look boundary of ~0.008 — found by simulating the design under the null rather than by looking anything up — restores the guarantee. Two validity checks come before interpretation: a bland-looking **51.2/48.8 split is p = 0.0007** sample-ratio mismatch, and twelve dashboard metrics give a **46 %** chance of a spurious winner.

The closing section is the one worth the price of admission. Selecting on significance inflates effect sizes — winners overstate their lift by **+50 %** under the underpowered analysis and only **+8 %** with CUPED — so power is not merely insurance against missing effects, it is **what makes the effects you find real**.

**Learning objectives:**
- Compute an experiment's **MDE** for a proportion and a mean, and use it to decide whether a test is worth running at all.
- Demonstrate why **"not significant" is not "no effect"**, and quantify an underpowered test's false-negative rate by simulation.
- Apply **CUPED** and predict its gain from the pre/post correlation alone (variance reduction = ρ²).
- Show what **peeking** does to the error rate and calibrate an honest stopping boundary by Monte Carlo.
- Run the **validity checks** that precede interpretation: SRM and the multiple-comparisons tax.
- Explain the **winner's curse** and decide from the interval against the cost of acting.

**Sections:**
1. Three decisions waiting on evidence
2. Before you run it: the MDE, and the test you should cancel
3. D2: the loyalty offer, and a test that says nothing
4. CUPED: the cheapest power you will ever buy
5. Peeking: how a 5 % test becomes a 23 % test
6. Two checks before you interpret anything
7. From p-value to decision — and the winner's curse
8. What real experimentation platforms add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the dashboard that found a winner") · 4 🧠 stretch exercises (⭐⭐⭐: clustered randomization and the design effect, an always-valid confidence sequence from scratch, designing A1's monitor price test properly, heterogeneous effects without fooling yourself) · 🎁 bonus mini-project: the pre-registration one-pager · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline and vectorised so thousands of simulated experiments run in seconds — heavy-tailed B2B revenue with a sticky pre-period, plus toy frames for the SRM and multiple-comparisons demos. Core stack only; fully offline.

### A3 · Credit Risk: Scorecards, Expected Loss & the Approve/Decline Decision — `A3_credit_risk_scorecards.ipynb`

**The notebook where your own past decisions wrote the training data.** The webshop's growth lever is trade credit — "Invoice 30" — which makes it a lender. Two things follow that nothing else in the module has. The deliverable is a **document a credit committee signs**, not a model object; and the labels only exist for applications you *approved*, so every declined applicant is a permanent question mark.

§2 builds the industry's actual artefact: quantile binning, **weight of evidence**, information value, a logistic fit, a **sign check**, and the points transform with its points-to-double-the-odds convention — ending in a table you could print, complete with the **base points** from the intercept, so the page reproduces the model's score to ten decimal places by hand. (That check is what most scorecard write-ups omit, and without it the table is decorative.) Two features get dropped along the way, and both are instructive. `payment_score` has a healthy univariate IV of 0.118 but comes back **wrong-signed** (the bureau score is built from age and size, which are already in the model) and dropping it costs **zero** AUC. And `director_changes` has IV **0.000** — not because it doesn't matter, but because the legacy rule declined everyone with two or more, so the book contains no variation to measure. That is selective labels leaving a fingerprint on the IV table before §6 even starts. Gradient boosting with every feature scores 0.690 against the scorecard's 0.694, so here explainability is free — worth saying plainly, because the argument is usually framed as a trade.

§4 derives the only formula that matters: **`PD* = m/(m + LGD) = 15.6 %`**, limit-independent, the same cost-ratio move as NB 23's break-even threshold and A1's headroom rule. The profit curve confirms it and then teaches restraint — **every cutoff from 0.14 to 0.26 is within 1 % of peak**, and re-drawing only the cross-validation folds walks the argmax from 0.14 to 0.22, so the argmax is noise with four decimal places and the formula (which doesn't move with the sample) is what ships. §5 prices credit limits honestly as a **risk-appetite overlay**: banding cuts expected loss from 3.33 % to 2.47 % of exposure and costs a quarter of the profit, which is what buying insurance looks like rather than an optimisation win.

§6 is the honest heart. The approvals-only model understates declined applicants' risk by ~30 % (**10.5 % predicted vs 14.6 % true**) and over-approves exactly where it has no data — and a validation set drawn from the same censored book **cannot detect this**. It costs **€177k**; the model still beats the legacy rulebook by **€1.02 m**, raising approvals from 75.8 % to 88.7 % while the bad rate barely moves. A randomized exploration budget is the only real fix, and the section's most interesting result is that here it *pays for itself*, because 66 % of the declined pool should have been approved.

**Learning objectives:**
- Build a **WOE/IV scorecard** end to end — binning, IV screen, logistic fit, sign check, points transform.
- Say honestly when a scorecard beats a gradient-boosted model, and why the industry ships it anyway.
- Explain why credit decisions need **calibration**, not just ranking, and check it.
- Derive **`PD* = m/(m + LGD)`** from expected loss and read a profit curve without over-reading its argmax.
- Set **credit limits** as a risk-appetite overlay and state what the overlay costs.
- Diagnose the **selective-labels** problem, quantify it, and price a randomized exploration budget.

**Sections:**
1. The business: "Invoice 30", and what a bad decision costs
2. WOE, IV, and the scorecard you can print
3. Ranking is not enough — the level has to be right
4. The decision: expected loss and the profit-optimal cutoff
5. How much? Credit limits as a risk-appetite overlay
6. The selective-labels problem
7. What real credit systems add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the scorecard that got better by cheating" — WOE fitted before the split) · 4 🧠 stretch exercises (⭐⭐⭐: the cutoff with a lifetime instead of a cycle, reject inference and its limits, proxy discrimination and the cost of a fairness constraint, vintage curves and PSI) · 🎁 bonus mini-project: the credit policy one-pager · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline — 6,000 trade-credit applications over two years, with a bureau score deliberately **blind** to the exposure ratio, board churn and sector that carry most of the real risk, and a judgemental legacy approval rule that screens on the variables you later want to model. That construction is what makes §6 measurable. Core stack only; fully offline.

### A4 · Causal Inference & Uplift: Who to Target, Not Who Will Churn — `A4_causal_uplift.ipynb`

**The notebook where the report's arithmetic is correct and its conclusion is wrong.** Brightloop's retention team discounted its riskiest customers; the treated group churned *more*; the report recommends cancelling the program. Because the notebook simulates both potential outcomes for every customer (`y0`, `y1` — god mode), it can compute what no analyst can: the naive **+1.8 pp** decomposes *exactly* into a **−5.4 pp** real effect on the treated plus **+7.3 pp** of selection bias. The program was making money; the comparison was rigged by its own targeting.

§2 prices the four uplift segments for this offer — persuadable **+€170.50**, sure thing **−€9.50**, lost cause **€0**, sleeping dog **−€180** — and plots the punchline: risk is the x-axis, value of targeting is the y-axis, and they are not the same axis. §3 randomizes this quarter's campaign and watches the selection term die by construction (−4.3 ± 1.5 pp against a planted −3.0). §4 builds the T-learner NB 23 only sketched, validates it the production way (observed uplift by predicted-uplift quintile: −3 pp to +17 pp, monotone), sets the targeting depth from the **break-even uplift `D/V` = 5.3 pp**, and races policies at a 30 % budget: **€25k by uplift vs €13k by risk vs −€13k for treat-everyone** — a causally effective program that still torches money when untargeted, because 94 % of recipients aren't persuadables. §5 handles the rollout nobody randomized with difference-in-differences (−1.44 pp against a planted −1.50, placebo ≈ 0), and §6 is the honest heart: regression adjustment and IPW recover most of the truth when treatment depended on *measured* features — then the same code, on a quarter where agents also read the (unmeasured) support-call notes, confidently reports the **wrong sign**. No error, no warning. Stretch C shows even a cross-fitted doubly-robust AIPW estimator dies on the same hill.

**Learning objectives:**
- Decompose a naive treated-vs-untreated gap into **effect + selection bias**, numerically.
- Name and **price** the four uplift segments, and explain why risk-targeting buys lost causes and sleeping dogs.
- Fit and honestly evaluate a **T-learner**, and set the targeting depth from the break-even uplift `D/V`.
- Estimate an un-randomized rollout's effect with **DiD**, defend parallel trends, and run a placebo.
- Say exactly when **regression adjustment / IPW** are trustworthy, and demonstrate their silent failure mode.
- Ask "who decided who got treated?" before asking "which estimator?".

**Sections:**
1. The business, and a campaign report that smells wrong
2. Potential outcomes — the two-worlds bookkeeping
3. This quarter: randomize, and the bias term dies
4. Uplift modeling — estimating *who* reacts
5. No experiment allowed — difference-in-differences
6. Adjusting the targeted quarter — and the confounder you can't see
7. What real causal systems add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the uplift model that killed a working program" — trained on confounded data, its *level* is fiction even though its ranking survives) · 3 🧠 stretch exercises (⭐⭐⭐: the Qini curve with bootstrap error bars, a DiD event-study with permutation placebos, cross-fitted AIPW) · 🎁 bonus mini-project: the retention decision memo, where every causal claim must name its design · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline — 20,000 subscription customers with *both* potential outcomes materialized, split into an observationally-targeted quarter (risk-list coverage kept probabilistic so overlap holds), a randomized quarter, and a hidden-confounder variant where treatment chased an unmeasured "anger" signal; plus a 12-month two-region panel for the DiD rollout. The exercise-2 verdict is deliberately anti-folklore: on this data the S-learner *beats* the T-learner, and the solution explains why the shrinkage rule of thumb is a tendency to check, not a law. Core stack only; fully offline.

### A5 · People Analytics: Attrition, Survival & Pay Equity — `A5_people_analytics.ipynb`

**The notebook where "still here" is not a label.** Nordwerk Group — the parent of NB 25's webshop and NB 23's HelpDeskAI — employs 1,344 people across warehouse, support, sales and engineering, and HR opens with two asks: an attrition analysis before the budget round, and a pay-equity analysis before the works council meeting. The intro names why this is *not* NB 23 with employees: most employees haven't left yet, so the data is **censored** — and the naive "average tenure of leavers" (13.1 months) is off by a factor of three from the honest **Kaplan–Meier median of 41 months**, computed by hand from risk sets and event tables (no lifelines, core stack only). Function-level medians (warehouse 13 / support 50 / sales 70 / engineering 90 months) then feed the attrition *bill*: **€3.82 m a year**, with the module's favourite rank flip — warehouse has the highest *rate* (16.6 %) but engineering the biggest *bill* (€1.54 m vs €1.01 m), because a replacement costs 6–9 months of salary and engineers earn more. Rate-chasers fund the wrong retention program.

The model section is deliberately humble: a calibrated logistic regression (AUC **0.744**) beats gradient boosting (0.727) and the "flag everyone in their first year" rule (0.599), and the interesting part is downstream — NB 23's break-even move, per function: `p* = C/(s·R)` puts the threshold at 0.23 for engineering and 0.79 for warehouse, and at a €60k budget the economics-driven list earns **+€9.8k expected** where flag-the-first-years loses **€38.5k**. The pay-equity section is the careful one: the raw gap is **13.1 %**, the within-level adjusted gap **−2.4 %** (CI [−3.0, −1.8]), the Oaxaca-style split is 9.9 pp composition + 2.4 pp within-job — and the honest caveat gets its own subsection: *controls can be mediators*; if level itself is assigned unfairly, adjusting for it hides the problem (A4's confounder language, A3's proxy-discrimination stretch). The notebook ends with the two numbers the works council actually needs and what each one does — and does not — mean.

**Learning objectives:**
- Explain **censoring** and why leaver-vs-stayer classification on a snapshot lies; build a **Kaplan–Meier curve** by hand from risk sets.
- Turn a hazard into an **attrition bill** per function, and explain why the highest rate is not the biggest bill.
- Build an honest "leaves within 12 months" model on a **time-aware cohort**, and derive a per-function **break-even threshold** from replacement cost and save rate.
- Run a **budget-constrained retention campaign** and beat the tenure heuristic in euros.
- Decompose a pay gap into **raw vs adjusted** with a composition/within-job split — and state the **mediator caveat** that keeps the adjusted number honest.
- Name the guardrails that make people analytics different: small n, privacy, and scores that support conversations, never terminations.

**Sections:**
1. The business: one HR extract, three questions
2. The censoring trap — why the snapshot lies
3. From survival curves to euros
4. Who is at risk — and who is worth €3,000
5. The pay-equity question — raw gap, adjusted gap, and what each means
6. What real people-analytics teams add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the attrition model that predicted the past" — a terminal survey wave leaks 0.968 AUC of fiction) · 4 🧠 stretch exercises (⭐⭐–⭐⭐⭐: bootstrap CI on the KM median, the pilot before the program + HR sleeping dogs, the pay gap at n=38 and the k-anonymity line at n=5, hazard-shaped intervention timing) · 🎁 bonus mini-project: the CHRO one-pager · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline with a seeded `default_rng` — 2,550 employees hired over eight years with a true per-person monthly hazard matrix (god mode, used only for checking), planted first-year/overtime/engagement/pay-band drivers, censoring at the snapshot date, and a pay gap that is part composition, part −2.5 % within-level residual. Fully offline.

### A6 · Finance: Late Invoices, Collections & the 13-Week Cash Forecast — `A6_finance_ar_cashflow.ipynb`

**A3's direct sequel — the credit you granted becomes the cash you wait for.** "Invoice 30" worked: approvals rose to ~89 %, and finance now owns the consequence — a **€4.25 m** book of 828 open invoices, a DSO of **60.4 days** (one DSO day = **€70k** of cash), a two-person collections team good for ~40 calls a week, and a CFO who asks every Monday whether the quarter's cash clears the €250k buffer. The prediction section teaches AR's humbling lesson in one table: "everyone pays on the due date" errs by 15.3 days, the *customer's own historical mean* already gets to 9.3, and the gradient-boosted model earns its keep at **8.6 days** — persistence is the signal, and saying so out loud is the point. Features are built **as-of the invoice date** (NB 26's shifted-window discipline), and the planted month-end payment-run batching is why per-day evaluation flatters no one.

The collections queue is NB 24's move wearing finance clothes: rank by **expected cash acceleration** (success rate × days pulled forward × cost of capital + insolvency exposure), not by amount and not by days overdue — the three rankings genuinely disagree, and the trap is priced: the €45k invoice already sitting in a payment run is worth **−€4** per call while a €24k chronic offender is worth **+€139**. Then the CFO's actual question: per-invoice payment-date *distributions* (not point estimates) Monte-Carloed into a 13-week cash curve — median minimum cash **€293k** in week 2, **P(breach the buffer) = 25 %** — where the point-estimate version of the same forecast claims €422k and zero risk. The walk-forward backtest settles whose spreadsheet to trust: the model runs ~€121k conservative per quarter; the due-date spreadsheet runs **€1.49 m optimistic**.

**Learning objectives:**
- Read an AR book like a finance team: **DSO**, the aging waterfall, and what one DSO day is worth.
- Predict days-late with **as-of features** and beat two named baselines — then admit how strong the dumb one was.
- Rank a **collections queue by expected cash acceleration** and show why amount-ranked and overdue-ranked calling both lose money.
- Build a **13-week cash forecast** from per-invoice payment distributions, and explain why summing point forecasts understates tail risk.
- Turn the forecast into a **credit-line decision** with a probability attached, and backtest it walk-forward against realized cash.
- Spot the optimism bias of **due-date accounting** and price it.

**Sections:**
1. The business: a €4.2M ledger, a credit line, and Monday's question
2. When will this invoice pay? Predicting days-late
3. The collections queue — NB 24's move, wearing finance clothes
4. From invoices to the cash curve — the 13-week forecast
5. Backtest the forecast honestly — four past Mondays
6. What real treasury & FP&A systems add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the collections model that knew the payment date" — a `reminders_sent` feature buys an impossible 3.4-day MAE) · 4 🧠 stretch exercises (⭐⭐⭐: shrinkage for the customer league table, the P90 payment date by quantile regression, *when* to call rather than whom, pricing a factoring offer with A3's loss numbers) · 🎁 bonus mini-project: the Monday treasury one-pager · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline with a seeded `default_rng` — 9,066 invoices across 592 B2B-webshop customers over 18 months, with planted customer-persistent lateness, size and amount effects, month-end payment-run batching, a 3 % dispute tail and a ~1 % insolvency tail. Fully offline.

### A7 · Sales: Lead Scoring, Pipeline Truth & the Quarter Forecast — `A7_sales_pipeline.ipynb`

**The module's leakage lesson in its natural habitat.** HelpDeskAI has grown a 12-rep sales team, and three artifacts rule its Mondays: the CRM pipeline (rep-entered stages and win probabilities), the inbound lead queue (more leads than SDRs), and the quarterly forecast the VP gives the board. The antagonist is the CRM itself. Train a win-probability model on the *current* CRM table and you get **AUC 1.000** — because deal size, stage and days-in-pipeline were all edited after the deals closed; rebuild every feature **as-of a snapshot date** from the stage-history log and the honest number is **0.853**. That one deflation, plus the censoring footnote (open deals at snapshot time haven't resolved — you can only train on cohorts old enough to know), is the section the rest of the notebook stands on.

Then the reps' numbers face a reliability curve: deals entered at "20 %" win **9.9 %**, deals at "80 %" win **55.6 %** — sandbagging at the bottom, happy ears at the top — and the embarrassing baseline is that plain stage-level win rates (Brier 0.111) crush the reps (0.175) while the model only edges further to **0.108**: *the win is calibration, not clairvoyance*, and the notebook says so. The forecast section rolls calibrated probabilities into the quarter — model **€64k** vs the CRM rollup's **€184k** (2.9× inflated) — with Monte-Carlo bands widened for the macro-correlation caveat, and a six-quarter walk-forward that settles the leaderboard: model 12.6 % MAPE, stage rates 16.6 %, the VP 80.8 %, the CRM 149.2 %. The lead queue closes the loop: EV-ranked calling yields **€80k of expected pipeline per SDR-week** vs €41.6k first-come-first-served, with a break-even depth (~103 of 120 capacity) where an SDR hour stops paying — and an A2/A4 citation ordering a 10 % random holdout of leads, because a score that changes who gets called writes targeted training data for next quarter.

**Learning objectives:**
- Rebuild CRM features **as-of a snapshot** from the stage-history log, and demonstrate what post-outcome edits do to AUC.
- Read a **reliability curve** and price rep-entered probabilities against realized outcomes.
- Beat the reps with the dumbest possible baseline (**stage-level win rates**) and say honestly what the model adds beyond it.
- Roll calibrated probabilities into a **quarter forecast** with Monte-Carlo bands, and backtest it walk-forward against realized bookings.
- Rank a **lead queue by expected value**, not conversion probability, and derive the break-even calling depth.
- Explain why a deployed score needs a **random holdout** — A4's selection bias, arriving in sales clothes.

**Sections:**
1. The business: one CRM extract, three Monday questions
2. The snapshot discipline — reconstructing what you knew, when
3. Are the reps' numbers any good? Calibration before modeling
4. From probabilities to the quarter forecast
5. The lead queue — scoring what to call first
6. What real revenue-ops teams add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the 0.97-AUC pipeline model" — NB 23's 0.99-AUC trap, CRM edition) · 4 🧠 stretch exercises (⭐⭐⭐: per-rep calibration with shrinkage, a survival view of deal staleness, a quantile forecast with a coverage audit, and a Goodhart simulation where reps game the model's features for a +75 % forecast and €0 of reality) · 🎁 bonus mini-project: the board forecast memo · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline with a seeded `default_rng` — ~39,000 leads over 130 weeks feeding 2,466 opportunities through a five-stage engine with full timestamped stage history, 12 planted rep calibration personalities, and post-close CRM field edits (the contamination is the curriculum). Fully offline.

### A8 · Procurement: Spend, Supplier Scorecards & Total Cost — `A8_procurement_spend.ipynb`

**The buying office — where the module's data skepticism meets a purchase order.** NB 25, A1 and A3 looked at the webshop's customers; A8 walks into the room where its **€10.9 m a year** gets spent: 14,000 PO lines, 60 suppliers, 12 categories, one new head of procurement with the three standard questions. The intro stakes the methodological claim: procurement analytics is mostly *not* prediction — it is honest accounting plus a handful of distributions, and its classic failures are averaging away variance and claiming savings on price while total cost rises. The spend cube and Pareto/ABC land first (17 suppliers carry 69.5 % of spend), then the maverick-spend bill — **€117k a year** of off-contract buying at a +9 % premium — a number that funds the analytics team; the notebook says so.

The price-variance lens carries the module's honesty flag: the naive "if every line had paid the minimum price" savings claim is **€969k**; adjust for legitimate lot-size price breaks and it collapses to **€175k** — and the €793k gap *is* the lesson (a should-cost regression then finds the genuinely overpriced supplier, +3.7 % above model on 150 lines). The scorecard section stages the planted twins: two suppliers with the *same* mean lead time (7.1 vs 6.8 days) and σ of 0.81 vs 3.58 — NB 26's safety-stock formula prices the difference (+90 units of stock, or a service level quietly sliding from 95 % to 72 %), and the "rank by average lead time" baseline crowns the company's *worst* supplier (OTIF 75.9 %). Weights derived from € impact instead of the arbitrary 25/25/25/25 re-rank 25 of 52 suppliers; total cost of ownership dethrones the cheapest invoice (€104.88 on paper, **€113.80** all-in, beaten by a €109.50 rival); and the consolidation section ends the module the right way — 16 tail suppliers consolidated for **€47k/yr at a 10-month payback**, and two categories deliberately *not* consolidated, with the dual-sourcing premium priced as insurance (A3 §5's framing, third appearance).

**Learning objectives:**
- Build a **spend cube** and run Pareto/ABC — and put a euro figure on **maverick spend**.
- Deflate a naive **price-variance savings claim** to its like-for-like honest number, and fit a **should-cost regression** that finds real overpricing rather than small lots.
- Score suppliers where it matters: **OTIF**, and lead-time **variance priced via safety stock** (NB 26), with weights derived from € impact.
- Fold defects, discounts and payment terms into **total cost of ownership** — and watch the cheapest invoice lose.
- Decide a **consolidation plan** with switching costs, payback, and the concentration-risk math that keeps two categories dual-sourced.
- Explain why the 2/10-net-30 discount you skip is a **45 % APR** loan you just took out.

**Sections:**
1. The business: 14,000 PO lines, one spend cube
2. The price-variance lens — same item, many prices
3. The supplier scorecard — where averages lie
4. Defects, discounts and terms — small print in euros
5. The consolidation decision — the tail and the risk
6. What real procurement systems add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the savings that weren't" — a year-over-year price comparison broken by a lot-size mix shift; the fix is a like-for-like index) · 4 🧠 stretch exercises (⭐⭐–⭐⭐⭐: bootstrap + Wilson error bars for the supplier league table, a Kraljic-style 2×2, a category price index against the planted input-cost wave, pricing the second source under different failure probabilities) · 🎁 bonus mini-project: the category strategy one-pager · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline with a seeded `default_rng` — two years / 14,000 PO lines for the NB 25 webshop's buying office, 12 categories × 60 suppliers with planted ground truth: a +9 % maverick premium, lot-size price breaks, a steel-indexed category, a same-mean/high-σ supplier twin, and a 2025 lot-size mix shift. Fully offline.

### A9 · Marketing Mix & Incrementality — `A9_marketing_mix.ipynb`

**The notebook where the best-performing channel turns out to be a mirror.** The webshop spends **€2.4M a year** across six channels, and the CFO has noticed that branded search reports a **12.00× ROAS** — so why not move the whole budget there? Because last-click attribution ranks who *closed*, not who *caused*: branded search's spend rises with demand it did not create, and its true return is **1.72×**, while trade shows report **0.66×** and are truly **3.39×**. Acting on the last-click ranking destroys **€1.6M a year**.

The fix needs two effects no other notebook in the module has: **adstock** (this week's spend still working three weeks from now) and **saturation** (the tenth euro buying less than the first). Both are implemented as small functions, fitted per channel, and checked against planted truth — the model decomposes a €19.9M year into a €249,919/week baseline (truth: €245,000) and €118,487/week of marketing (truth: €120,874), and backtests at **1.39% MAPE** against seasonal-naive's 5.05%. §3 then does something most MMM write-ups skip: it prices what 156 weekly observations **cannot** identify. Email's contribution interval is **[€0, €10,266]** — the channel may be doing nothing, and this data cannot tell; branded search carries a VIF of 17.2, and a synchronised budget would push VIFs to 73. The ridge penalty is taught rather than hidden, because cross-validation picks 0.02 for *prediction* and attribution needs 0.09 — prediction and attribution are different jobs, and that gap is what makes §5 necessary.

§4 turns curves into a budget by equalising **marginal** returns, moving **€335,303** of the same €2.4M for **+€193,490 a year** (god mode says the ideal move was worth €522,505 — the gap is what imperfect estimation costs). A1's guardrails return in force: bootstrap the response curves, refuse to extrapolate past the spend range you have actually run, and accept that the optimum is flat. §5 is the honest fix and the notebook's best section — a **geo holdout** on branded search across 12 of 24 regions for 26 weeks, with an MDE of 2.54%, measuring incrementality at **1.70%** against the planted 1.72×. It costs €104,868 of revenue and *gains* €58,248 of gross profit, because the ad spend it switches off was mostly buying customers who were already coming.

**Learning objectives:**
- Explain why **last-click attribution** systematically over-credits closers, and name **reverse causality** as the separate, second error.
- Implement **adstock** and **saturation** transforms and fit them, checking recovered contributions against a known truth.
- Diagnose what a 156-week MMM **cannot identify** — flat spend, collinear channels — and report those limits as intervals rather than point estimates.
- Reallocate a fixed budget by **equalising marginal returns**, with bootstrap and support-range guardrails.
- Design a **geo holdout** to measure incrementality directly, and price the test against the budget it protects.
- Say what MMM can never do: it sizes channels, never people (that is A4's job).

**Sections:**
1. The business: €2.4M, six channels, one budget meeting
2. Last-click is a ranking of who closed, not who caused
3. The MMM: adstock, saturation, and what 156 weeks can identify
4. From coefficients to a budget
5. The honest fix: buy the answer with a geo holdout
6. What real MMM teams add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the model that discovered branded search is the whole company" — drop the seasonality and promo controls and Christmas gets handed to whichever channel tracks demand hardest, inflating branded search from €30,182 to €187,524 a week and 49% of revenue) · 4 🧠 stretch exercises (⭐⭐⭐: bootstrap the whole allocation into a range, model brand/non-brand cannibalisation, contour the near-flat likelihood surface to make identifiability visible, and calibrate the MMM with the geo result as a prior) · 🎁 bonus mini-project: the budget memo · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline with a seeded `default_rng` — 156 weeks of the webshop's weekly spend across six channels, revenue, orders, A1's promo calendar, a price index and a competitor ad-pressure index, with per-channel geometric adstock and Hill saturation planted as recoverable ground truth, plus a 75,541-order touchpath log tied to the same P&L. Fully offline.

### A10 · Service Operations: Arrivals, Erlang C & the Staffing Plan — `A10_service_operations.ipynb`

**The notebook where the average day never happens.** HelpDeskAI's own support floor handles ~8,974 contacts a week at a 6.90-minute average handle time, and must hit "80% of chats answered in 20 seconds". The opening figure settles the notebook's thesis before any model appears: the mean interval carries 45.9 contacts, but only **14.9%** of intervals land within ±20% of it, and Monday 10:30 runs **40× busier** than Sunday 20:30. Anything you compute from a daily average is a statement about a day that does not exist.

Erlang C is implemented from scratch (offered load, P(wait), service level, average speed of answer) and — the step that makes it teachable — **validated against a simulation**: 0.209 vs 0.199 for P(wait), 83.6% vs 84.7% for service level. Then the three lessons the formula exists to teach. The staffing curve is a **staircase, not a line**: +5% volume needs +4.0% agents at the median but **+14.3%** in the 20:00 interval, and a 30% volume drop returns only 26.2% of the agents. The **occupancy cliff** is dissected at fixed load — 80% occupancy gives an 83.6% service level and a 17-second answer; **95.2% gives 27.5% and 315 seconds**, which is why "run everyone flat out" is an operational death wish rather than an efficiency drive. And **shrinkage** — rostering paid hours rather than productive ones — is worth 15.8 FTE and **€316,545** of the quarter's €1,055,151 plan.

§5 buys a service level instead of assuming one: an abandoned contact costs €15.24, and the total-cost curve bottoms out at **88%**, not at the contracted 80% (which costs €22,056 more) and certainly not at 98% (€103,100 more). The baseline is then executed properly: the flat-average plan looks **€216,111 cheaper in wages** and is **€1,024,996 worse per quarter**, because it misses the SLA in 52.4% of intervals and delivers a contact-weighted service level of 24.2%. §6 is the Module 8 bridge and the section support leaders will recognise: a bot with 30.2% containment is walked down a waterfall — the staffing staircase (−25.6%), **mix shift** as the bot eats the easy contacts and AHT rises from 6.90 to 8.03 minutes (−15.6%), the interval profile (−15.9%), and harder escalations at 8.57 minutes — landing at **−11.2%**, or **€118,099 honest against the vendor's €319,118**. Break-even containment is 20.1%.

**Learning objectives:**
- Forecast **interval-level** arrivals and explain why daily totals cannot staff a queue.
- Implement **Erlang C** from scratch and check it against a simulation.
- Explain the **staffing staircase** and the **occupancy cliff**, and apply **shrinkage** correctly.
- Choose a **cost-optimal service level** from the cost of waiting versus the cost of an agent.
- Build the quarter's staffing plan and beat the flat-average baseline in euros.
- Audit an **AI deflection** business case: staircase, mix shift, interval profile and escalation quality.

**Sections:**
1. The business: 9,000 contacts a week, one SLA
2. Forecasting the arrivals — a prerequisite, not the point
3. Erlang C from scratch — and a simulation to check it
4. What the formula teaches: a stepped curve and a cliff
5. The money: shrinkage, the cost of waiting, and the service level to buy
6. The AI deflection question — what the vendor's slide leaves out
7. What real workforce-management teams add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the plan that hits its SLA on paper" — an Erlang plan built on the daily average reports 80.1% attainment and misses in 50.5% of intervals, at a €945,286 cost of averaging) · 4 🧠 stretch exercises (⭐⭐⭐: Erlang A with a patience distribution by simulation, a two-skill floor where the formula has no answer, buying a forecast **quantile** instead of a point, and turning the requirement curve into a roster with a set-covering LP) · 🎁 bonus mini-project: the staffing plan one-pager for the CFO · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline with a seeded `default_rng` — 20,468 half-hour intervals (two years, 07:00–21:00) of support arrivals with an intraday double hump, day-of-week and annual waves and six launch spikes, split into four contact types whose easy share deliberately thins out at the peak, plus a one-week contact-level log with lognormal handle times by channel × type. Fully offline.

### A11 · From Prediction to Allocation: Routing, Dispatch & Slack — `A11_routing_allocation.ipynb`

**The module's first plan.** Every other notebook here ends in a threshold or a ranked list; this one ends in an assignment, a sequence, and a promise you either keep or pay for. Forty field-service jobs, six technicians, two-hour arrival windows, and a costed board: a missed window is €150, a rebooking agreed the night before is €60, overtime is €48/hour, driving is €0.42/km.

§2 makes the pivot that justifies the notebook. The travel-time model is fine (**MAE 9.20 minutes** against the dispatcher's 30 km/h rule at 11.35), but for a schedule the **error distribution matters more than the mean**: the ratio of actual to predicted has a median of 0.947 and a 90th percentile of 1.39, errors accumulate down a route, and a hand-built route that is feasible on paper **misses a window on 59% of days**. §3 then runs the baseline honestly — nearest-neighbour distance minimisation produces the shortest plan in the notebook at **287.1 km**, hits **13 of 40** windows, books 1,120 minutes of overtime, leaves vans parked for 26.4 hours, and costs **€5,067 a day**. The exchange rate is printed so nobody forgets it: one missed window equals 357 km of driving.

§4 optimises the thing that actually matters — `scipy.optimize.linear_sum_assignment` for jobs-to-technicians, greedy insertion plus 2-opt for sequencing, all scored in euros — and lands **39 of 39 promised windows for €231 on paper**, while driving 11 km *further* than the distance-optimal plan and costing **€4,836 less**. Then §5 undercuts its own answer, which is the best thing in the notebook. Simulated over 400 Tuesdays, that €231 plan really costs **€742**, has only **9% clean days**, and in the worst case a single 184-minute delay takes out **six consecutive windows** and sends a technician home at 20:34 against a sheet that said 16:57. Sweeping **slack** finds an interior optimum at **12 minutes per leg** — €548/day, 60% clean days, worth **€48,500 a year** — and the closing observation is the one to remember: on-paper cost rises monotonically with slack, so anyone optimising the sheet will choose zero, every time. Insurance, for the third time in this module after A3's credit limits and A8's dual sourcing.

**Learning objectives:**
- Explain why a schedule needs a travel-time **distribution**, not a point estimate, and why errors compound along a route.
- Recognise a **wrong objective**: minimise distance and watch the promises break.
- Build an assignment with `linear_sum_assignment` and sequence it with **greedy insertion + 2-opt**, scored in euros under skill, shift and window constraints.
- Stress-test a plan by simulation and quantify **cascade failure**.
- Choose **slack** as a priced decision variable, and explain why the on-paper optimum never will.
- Say what makes a routing deliverable adopted: a plan the dispatcher understands.

**Sections:**
1. The business: 40 jobs, 6 vans, one promise
2. Predict travel time — and notice which part matters
3. The dumb baseline, and the wrong objective
4. Optimising the thing you actually care about
5. The plan that survives Tuesday
6. What real routing systems add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the schedule that validated perfectly" — feasibility checked with mean travel times and no service duration; the fix validates at a service level and finds 10 of 39 promises kept less than 90% of the time) · 4 🧠 stretch exercises (⭐⭐⭐: start the vans from home — and lose, €581 against €548; SLA-weighted misses so the *business* job stops being the one sacrificed; a fleet-size sweep where the 7th technician saves €66/day against a €272/day wage; intraday re-dispatch after a 90-minute over-run, at €124 per incident) · 🎁 bonus mini-project: tomorrow's dispatch sheet **plus** the note answering the dispatcher's four questions · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline with a seeded `default_rng` — one day's board of 40 jobs (location, duration, skill, SLA class, two-hour window) across a 30 × 30 km metro with five customer clusters and six skill-constrained technicians, plus 12,000 historical trip records with planted rush-hour congestion and a right-skewed delay tail, and a 4,000-job duration log. Core stack plus `scipy.optimize`; fully offline.

### A12 · Pricing Risk: Frequency × Severity & Adverse Selection — `A12_insurance_pricing.ipynb`

**A3's sequel in a different industry — where the loss is a count times an amount.** The webshop sells a device protection plan at a flat **€89** to everyone. The book looks healthy in aggregate (loss ratio 0.729, a combined ratio of 0.953, €151,832 of margin) and is quietly catastrophic in one corner: consumer-monitor plans run a **0.24** loss ratio while trade-laptop plans run **2.50**, against a pure premium of €222.74. A3 decided approve or decline on a binary event; here the decision is a *price*, the severity has a real tail, and there is a strategic trap A3 never faces.

§2 is why this notebook sits beside A5: **exposure is the actuarial form of censoring**. Policies written mid-year have not finished their year, and the naive claims-per-policy frequency of 0.0799 understates the earned 0.1307 per policy-year by **38.9%**. With `offset=np.log(exposure)`, the Poisson GLM recovers **all ten planted relativities inside their confidence intervals** (laptop 1.89 against a planted 1.86; trade 1.69 against 1.75). The dispersion check then does what a good diagnostic should — variance/mean of 2.01 sends you to a negative binomial whose α of 2.82 matches the planted 2.86, the relativities move 0.3%, and the **standard errors widen 12–18%**: the point estimate survives, your certainty does not. §4 refuses to summarise severity with a mean (€497 against a €269 median and a €25,953 maximum, with the top 1% of claims carrying 17.1% of the euros) and is explicit that capping at €2,500 does not delete the tail, it **moves** it — €8.12 per policy-year, 12.5% of incurred, that someone still pays.

The rate table runs **€41.88 to €229.97** and averages €90.50 — within €1.50 of the flat price, which is the point: the flat price is roughly right *on average* and wrong for almost everybody, hiding **€1,299,810 a year of cross-subsidy, 39.8% of earned premium**. §6 then simulates what the analysis is really for. Hold the flat price while good risks lapse and the loss ratio walks **0.722 → 1.038** as the book shrinks from 60,000 to 23,999 and premium falls €5.34M → €2.14M; chase it with a single higher flat rate and you reach €129.51 with 18,928 plans; differentiate and the loss ratio stays flat at 0.71 with 44,090 plans and €3.99M. A3's fairness discipline is imported explicitly — `credit_band` looks 1.44× predictive univariately and collapses to **1.01× (p = 0.71)** once legitimate factors are in, failing on statistics as well as ethics — and the +25% year-over-year cap is priced as the business constraint it is: €464,879 in year one, €990,224 cumulative.

**Learning objectives:**
- Treat **exposure** correctly with a log-offset, and connect it to censoring (A5).
- Fit a **Poisson/negative-binomial frequency GLM**, check dispersion, and say what overdispersion does and does not change.
- Model **severity** with a Gamma GLM, respect the tail, and price a **large-loss cap** honestly.
- Build a **technical rate table** and quantify the **cross-subsidy** a flat price conceals.
- Simulate **adverse selection** and show what refusing to differentiate costs over renewal cycles.
- Separate **permissible** rating factors from merely predictive ones, and price a rate-change glide path.

**Sections:**
1. The business: 60,000 plans, one price, and a loss ratio nobody owns
2. Exposure — the actuarial version of censoring
3. Frequency: a Poisson GLM with an offset
4. Severity, and why the mean is a bad summary
5. The technical price and the cross-subsidy
6. Adverse selection: what happens if you refuse to differentiate
7. What real pricing teams add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the model that priced new business a third too cheap" — frequency fitted without the exposure offset files €174.50 against a correct €273.33, −36.2%) · 4 🧠 stretch exercises (⭐⭐⭐: credibility shrinkage for a thin cell, a Tweedie GLM fitted directly on pure premium against the two-part model, a bootstrap that says which cells are genuinely distinguishable, and a €150 excess and who selects into it) · 🎁 bonus mini-project: the rate-change memo for the product committee · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline with a seeded `default_rng` — 60,000 device-protection plans (device × segment × channel × district × declared usage × exposure) with planted frequency relativities, a gamma frailty producing genuine overdispersion, and 4,794 lognormal claims plus rare €4k–€26k fleet thefts and batch defects. Uses `statsmodels`; fully offline.

### A13 · Product Analytics: Funnels, Cohort Curves & the Activation Metric — `A13_product_analytics.ipynb`

**Upstream of NB 23, and the notebook that decides how a squad spends its quarter.** HelpDeskAI's self-serve product takes 60,000 signups through activate → habit → paid (47.5% / 46.7% / 26.0%, or 5.8% end to end), and the PM arrives with three questions. The first is answered by a decomposition rather than a model: during a paid-social push, signup-to-paid conversion collapses **5.8% → 4.2%**, every step looks worse, and nothing got worse — paid social went from 13.8% to 47.9% of signups and activates at 26.1% against organic's 53.2%. Mix-adjusted, activation is 48.4% against a pre-push 47.5%. A funnel is a ratio whose denominator has a marketing department attached to it.

§3 rebuilds retention properly — 54.8% at week 1, 32.1% at week 12, 22.4% at week 52 — and compares cohorts **at equal age**, because the calendar-snapshot view credits the month-15 release with **+10.2 pp** when the honest like-for-like figure is **+4.4 pp**. That gap is right-censoring: young cohorts look wonderful because you have only seen their good weeks, which is A5's lesson wearing a product-management badge. §4 is the centrepiece. "Users who invite three teammates in week 1 retain 2.75× better" is **true in the data** (+46.5 pp), and it is mostly intent: adjusting for measured proxies leaves **+8.0 pp**, and the randomized nudge — the only thing that settles it — moves the metric **+24.6 pp** while moving retention **+1.90 pp ± 1.54**, against the +11.4 pp the correlation promised. The distinction the notebook exists to teach: a *diagnostic* metric predicts, an *actionable* metric changes the outcome when you move it, and teams are routinely handed the first and held to it as if it were the second — a mistake billed here at **€292,224** in squad time plus forgone work.

§5 converts curves into decisions. LTV is **€374** per payer, with **28% of it sitting in the unobserved tail** (47% for the newest cohorts) — stated plainly, because that share is an assumption, not a measurement. The channel table ranks by payback rather than volume: referral 8.75 LTV:CAC at 1.3 months, content SEO 3.97 at 2.9 months, paid search 1.23 at 9.2 months, and **paid social 0.71 at 16.0 months** — the cheapest signup at €9 and the only losing channel, with the push itself returning €56,110 on €78,912. And the roadmap choice inverts the usual instinct: +5 pp at the *leakiest* early step is worth €15,628/year against **€121,224** for the later one, because the steps carry different traffic and very different downstream value.

**Learning objectives:**
- Decompose a funnel that moved because its **traffic mix** moved, and report the mix-adjusted rate.
- Build a **cohort triangle** and compare cohorts **at equal age**, recognising young-cohort censoring.
- Distinguish a **diagnostic** metric from an **actionable** one, and design the randomized nudge that settles it.
- Integrate a retention curve into **LTV**, and state how much of it is assumption.
- Rank acquisition channels by **LTV:CAC and payback**, not by volume or cost per signup.
- Price two roadmap options in euros and explain why the leakiest step is not automatically the best fix.

**Sections:**
1. The business: 60,000 signups and one funnel
2. The funnel that got worse without anything getting worse
3. Cohort retention curves, and the trap of the young cohort
4. The activation metric — the one the team gets held to
5. From curves to money — LTV, payback, and two roadmap items
6. What real product-analytics teams add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the dashboard that found the best cohort in company history" — cohorts compared as of today rather than at equal age; the fix is age alignment and censoring the incomplete cells) · 4 🧠 stretch exercises (⭐⭐⭐: fit the tail instead of assuming it and watch LTV move with the assumption, a payback table that admits it does not know CAC, size the nudge experiment the way A2 would, and Goodhart in twenty lines) · 🎁 bonus mini-project: the quarterly product review one-pager, every metric labelled diagnostic or actionable · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline with a seeded `default_rng` — 60,000 self-serve signups over 24 months with acquisition channel, latent intent, weekly step timestamps, subscription lifetimes, week-1 invite counts and six measured intent proxies, plus two planted events: a paid-social push in months 10–14 (the mix shift) and a genuine onboarding release in month 15. Fully offline.

### A14 · Bandits & Adaptive Allocation: Learning While You Earn — `A14_bandits_adaptive.ipynb`

**The closing argument of the module's longest thread.** NB 23 targeted with a model; A3 discovered its own approvals had written its training data; A4 measured what that does to an estimator; A2 randomized to fix it. A14 asks what happens when the randomization itself adapts — which fixes the cost of learning and **re-breaks the inference**. Six offers compete for one hero slot, and because they carry different margins the best *click* arm is deliberately not the best *euro* arm.

§2 implements ε-greedy, UCB1 and Thompson sampling from scratch and scores them in the only unit that matters: **regret**, in euros. Thompson sampling costs **€3,212** a quarter against ε-greedy's €12,933 and a correctly-run four-week equal-split test's €24,656 — worth **€21,444 a quarter**. Textbook UCB1 comes in at €65,685 and is therefore *worse than the experiment*, which the notebook refuses to hide: rescale the reward from €41 to €1.50 and the same algorithm drops to €8,794. An exploration bonus that is not on the scale of your rewards is not a bonus, it is a random number.

§3 is why this notebook belongs in Module 7 rather than a generic ML course. After an adaptive run, the arms' naive sample means are **biased**: offer B's true 4.10% reports as 3.68% off 962 sessions, and the winner's reported lift over the incumbent comes in at **+63.8% against a true +43.2%** — where the equal-split test reports +43.7%. Hence the rule the notebook hands you: **bandits optimise, experiments estimate.** If the deliverable is a decision, adapt; if it is a number someone will reuse in a business case, randomize. §4 bridges to A4 with contextual bandits worth a further **€39,958 a quarter** — and shows the hybrid everyone actually deploys biting back, because a *stale* warm start costs €138,720, worse than not personalising at all, with forced exploration (A3's exploration budget, third costume) as the €10,352 fix. §5 then argues against the tool in four quantified ways: 30-day delayed rewards cut the advantage from €21,458 to €8,039; a stale winner burns €23,158 in six weeks unless the bandit forgets; and at three decisions a year the fixed test wins by €141,547.

**Learning objectives:**
- Frame an allocation problem as **regret in euros**, and reward on margin rather than conversion.
- Implement **ε-greedy, UCB1 and Thompson sampling**, and explain why UCB's bonus is scale-sensitive.
- Demonstrate **adaptive-sampling bias** and decide, per brief, whether to adapt or randomize.
- Extend to **contextual** bandits, connect them to A4's offline uplift, and handle a bad warm start.
- Quantify the conditions that break a bandit: **delayed rewards, non-stationarity, too few decisions**.
- Name what production systems add — off-policy evaluation, guardrails, ramped exposure.

**Sections:**
1. Six offers, one hero slot, and the price of learning
2. Three algorithms, from scratch
3. The bill for adaptivity: your estimates are now biased
4. Contextual bandits — the bridge back to A4
5. When a bandit is the wrong tool
6. What real adaptive systems add (honest section)

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. "Debug me 🐞: the bandit that optimised itself broke" — reward the click instead of the margin and it converges confidently on the worst offer, €116,046 against €3,462, or €450k a year; and exercise 2, which finds that a *right-length* seven-day test costs €10,440 rather than €24,656, so two-thirds of the headline "bandit win" was really just test duration) · 4 🧠 stretch exercises (⭐⭐⭐: batched Thompson sampling for nightly updates, IPS/SNIPS off-policy evaluation with its positivity failure made visible, successive halving versus Thompson when you want the *answer* rather than the revenue, and three ways to forget under non-stationarity) · 🎁 bonus mini-project: the merchandising decision memo — which of next quarter's four questions get a bandit and which get an experiment · ✅ self-assessment checklist.

**Datasets:** Synthetic, generated inline with a seeded `default_rng` — six hero-slot offers with planted true conversion rates and differing contribution margins, served to 360,000 simulated sessions a quarter in 1,800 batches of 200, plus an eight-segment (new/returning × mobile/desktop × basket size) response matrix for the contextual section. Fully offline.

## How these notebooks work

Each lesson follows the same rhythm: short teaching sections punctuated by **✋ Quick exercise (~2 min)** checkpoints with collapsible `<details>` solutions, plus 🔮 predict-the-output and 🔬 "what actually happens" cells that make you commit to an answer before running the code; a 🧠 one-screen story recap; then the graded work — 🧪 practice exercises (⭐-rated, always including a **Debug me 🐞**), 🧠 stretch exercises and a 🎁 bonus mini-project — closing with a ✅ self-assessment checklist. All data is generated inline (plus one bundled CSV), so everything runs **100 % offline**. The module leans directly on Modules 2 & 4 — the pandas/plotting/statistics craft and the sklearn/evaluation/pipeline discipline — and hammers five shared lessons across its notebooks: a probability is not a decision (scores become actions only via costs — break-even thresholds in NB 23, queue capacity in NB 24, service levels and critical ratios in NB 26, elasticity against contribution margin in A1, the confidence interval against the cost of acting in A2, `PD* = m/(m+LGD)` in A3); respect time or your metrics lie (temporal splits, shifted rolling features); beat the dumb baseline first (always-legit in NB 24, popularity in NB 25, seasonal-naive in NB 26, the legacy rulebook in A3); unsupervised output only becomes a business object once you profile, name, and stability-check it (NB 24, NB 25); and **ask how the data came to exist before you fit anything** — leakage in NB 23, unshifted windows in NB 26, your own pricing department writing the history you are about to regress on in A1, and in A3 the fact that you only observe repayment for the applicants you approved.

The appendices add a sixth that the core four only gesture at: **know what your evidence could have shown you.** A1 refuses to extrapolate a demand curve beyond the prices it has observed; A2 computes an experiment's resolution before running it and shows that low power corrupts the effect sizes you *do* find; A3 shows a validation set that cannot detect the model's largest error because it has the same hole in it; A4 shows an estimator that answers confidently and wrongly because the one variable that mattered was never collected. All four end in "run this experiment" or "we cannot answer that yet" at least once — which is the most under-taught deliverable in applied data science.

The business-function tour (A5–A8) then replays the module's lessons where most readers will actually use them. Censoring — the observation that hasn't finished happening — appears twice (employees who haven't left in A5, open deals in A7); post-outcome leakage gets its most realistic staging yet (a CRM edited after the fact, A7; a terminal survey wave, A5; a reminder counter that only exists once the invoice paid, A6); the break-even threshold returns in four new costumes (`p* = C/(s·R)` for a retention package, expected cash acceleration per call, an SDR-hour's break-even lead depth, the dual-sourcing premium); and the humbling baselines keep winning more than dignity allows (the customer's own mean in A6, stage-level win rates in A7). A8 contributes the tour's quietest lesson: sometimes the most valuable analytics in the building is honest accounting with error bars.

Growth & operations (A9–A14) then widen the module's idea of what a deliverable can be. Four of the six do not end in a score at all: A9 ends in a **budget**, A10 in a **headcount**, A11 in a **schedule**, A14 in a **policy** — and each needed machinery the module had never used (carryover and saturation, queueing, constrained assignment, sequential allocation). They also sharpen the module's oldest habits rather than repeating them. "Beat the dumb baseline" gets its most humiliating outing in A10, where the flat-average plan is €216k cheaper in wages and a million euros worse in total. "Averages lie" moves from A8's supplier lead times to A10's intervals and A12's claim severities, where the mean sits nearly twice the median. Censoring appears for the third and fourth time — A12's unexpired policies, A13's young cohorts — under two more names. And the module's insistence that a number must survive contact with uncertainty produces its best single result in A11: a schedule that is optimal on paper has a 9% chance of a clean day, and the slack that fixes it can never be discovered by optimising the paper.

Two of them end by arguing against their own tools, which is the disposition the whole module has been building toward. A14 finds that two-thirds of its headline "bandit beats experiment" win was really just a badly-sized experiment, and that its own textbook UCB1 loses to the test it was supposed to replace. A11's stretch exercises contradict the folklore they were written to confirm. A notebook that cannot report a result its author did not want is not teaching analysis; it is teaching advocacy.

## Where next

→ **The appendices** if you skipped them, in order: `A1` (pricing — the fastest lever on the P&L, and the one place where the *data itself* is the adversary), `A2` (experiments — the missing prerequisite that A1, NB 23 and NB 24 all lean on), `A3` (credit risk — a regulated industry's idiom, and the deepest version of "your own decisions wrote your training data"), `A4` (causal inference & uplift — the sequel NB 23's caveat promised, and the reason every campaign should keep a randomized holdout).
→ **The business-function tour (A5–A8)** in any order — each stands alone: `A5` (HR — censoring and the pay-gap decomposition), `A6` (finance — A3's sequel: collections and the 13-week cash forecast), `A7` (sales — leakage's natural habitat, and the calibrated quarter forecast), `A8` (procurement — spend transparency, scorecards where averages lie, and total cost of ownership). Pick the one whose Monday meeting you sit in.
→ **Growth & operations (A9–A14)**, also standalone: `A9` (marketing mix — the budget, and why the best-looking channel is a mirror), `A10` (service operations — Erlang C, and the bot that saves a third of what the vendor claims), `A11` (routing — the module's only plan under constraints, and the slack that pays), `A12` (insurance pricing — frequency × severity and the death spiral), `A13` (product analytics — cohorts, and the metric your team should not be chasing), `A14` (bandits — learning while you earn, and the inference it costs you).
→ **Module 8 — AI Engineering** (`../08_ai_engineering/28_ai_workflows.ipynb`) if you haven't done it yet — LLMs layered on top of exactly these workflows.
→ **Capstone A** (`../15_capstones/47_capstone_analytics.ipynb`) to prove the analytics half end-to-end.

---

📝 **Finished this module?** Test yourself with the [Module 7 quiz](../quizzes/quiz_07_industry_applications.ipynb) — five questions, ~10 minutes. (The quiz covers the core NB 23–26; the appendices are not examined.)
