# Module 7 — Industry Applications

> 🧭  [◀ Deep Learning with PyTorch](../06_pytorch/)  ·  [🏠 Course home](../README.md)  ·  [AI Engineering ▶](../08_ai_engineering/)

**Goal:** Apply everything from Modules 1–5 to the four use-case families that dominate business data science in practice — and learn the one pattern they share: *model → money → decision*.

**Estimated time:** 10–12 hours of focused study (core NB 23–26); the three optional appendices add ~8 h 15 m.

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

Three appendices, all written at **full lesson weight** (same rhythm and ✋/🧪/🧠 exercise ladder as NB 23–26) rather than in the reference style of the Module 2 and 5 appendices — because each sits squarely on this module's *model → money → decision* spine. They are optional only in the sense that the core four do not depend on them.

They also close loops the core notebooks deliberately leave open. NB 23, NB 24 and A1 all end by recommending an experiment; **A2** is that experiment. NB 24 mentions the selective-labels problem in one stretch exercise; **A3** makes it the centrepiece and prices it.

| Appendix | Notebook | ⏱ Time | Difficulty | Business problem | What you'll build |
|---|---|---|---|---|---|
| A1 | `A1_pricing_promotions.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | What should we charge for three very different SKUs, and was last year's promo calendar worth running? | Confound-corrected price elasticities, the headroom rule and inverse-elasticity price, a bootstrap + support-range guardrail that produces *hold / raise / test* rather than three prices, and a break-even discount rule that settles the promo P&L |
| A2 | `A2_experiments_ab_testing.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Three teams want to test something. Which of these tests can actually answer its question? | MDE-first test planning that *cancels* one test before it runs, CUPED variance reduction that doubles power for free, a peeking simulation and a boundary calibrated by Monte Carlo, SRM + multiple-comparisons validity checks, and the winner's curse quantified at two power levels |
| A3 | `A3_credit_risk_scorecards.ipynb` | ~2 h 45 m | ⭐⭐ (stretch ⭐⭐⭐) | Who gets trade credit, how much, and what do we do about the applicants we have never approved? | A WOE/IV scorecard with IV screen, sign check and points transform, a calibration check, the `PD* = m/(m+LGD)` cutoff and profit curve, risk-banded limits priced as an overlay, reason codes for decline letters, and the selective-labels problem measured in euros |

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

## How these notebooks work

Each lesson follows the same rhythm: short teaching sections punctuated by **✋ Quick exercise (~2 min)** checkpoints with collapsible `<details>` solutions, plus 🔮 predict-the-output and 🔬 "what actually happens" cells that make you commit to an answer before running the code; a 🧠 one-screen story recap; then the graded work — 🧪 practice exercises (⭐-rated, always including a **Debug me 🐞**), 🧠 stretch exercises and a 🎁 bonus mini-project — closing with a ✅ self-assessment checklist. All data is generated inline (plus one bundled CSV), so everything runs **100 % offline**. The module leans directly on Modules 2 & 4 — the pandas/plotting/statistics craft and the sklearn/evaluation/pipeline discipline — and hammers five shared lessons across its notebooks: a probability is not a decision (scores become actions only via costs — break-even thresholds in NB 23, queue capacity in NB 24, service levels and critical ratios in NB 26, elasticity against contribution margin in A1, the confidence interval against the cost of acting in A2, `PD* = m/(m+LGD)` in A3); respect time or your metrics lie (temporal splits, shifted rolling features); beat the dumb baseline first (always-legit in NB 24, popularity in NB 25, seasonal-naive in NB 26, the legacy rulebook in A3); unsupervised output only becomes a business object once you profile, name, and stability-check it (NB 24, NB 25); and **ask how the data came to exist before you fit anything** — leakage in NB 23, unshifted windows in NB 26, your own pricing department writing the history you are about to regress on in A1, and in A3 the fact that you only observe repayment for the applicants you approved.

The three appendices add a sixth that the core four only gesture at: **know what your evidence could have shown you.** A1 refuses to extrapolate a demand curve beyond the prices it has observed; A2 computes an experiment's resolution before running it and shows that low power corrupts the effect sizes you *do* find; A3 shows a validation set that cannot detect the model's largest error because it has the same hole in it. All three end in "run this experiment" or "we cannot answer that yet" at least once — which is the most under-taught deliverable in applied data science.

## Where next

→ **The appendices** if you skipped them, in order: `A1` (pricing — the fastest lever on the P&L, and the one place where the *data itself* is the adversary), `A2` (experiments — the missing prerequisite that A1, NB 23 and NB 24 all lean on), `A3` (credit risk — a regulated industry's idiom, and the deepest version of "your own decisions wrote your training data").
→ **Module 8 — AI Engineering** (`../08_ai_engineering/28_ai_workflows.ipynb`) if you haven't done it yet — LLMs layered on top of exactly these workflows.
→ **Capstone A** (`../15_capstones/47_capstone_analytics.ipynb`) to prove the analytics half end-to-end.

---

📝 **Finished this module?** Test yourself with the [Module 7 quiz](../quizzes/quiz_07_industry_applications.ipynb) — five questions, ~10 minutes. (The quiz covers the core NB 23–26; the appendix is not examined.)
