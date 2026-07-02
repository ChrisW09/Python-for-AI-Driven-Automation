# Module 4 — Machine Learning

**Goal:** Train your first models with scikit-learn, evaluate them *honestly*, and learn the feature-engineering moves that separate a 0.65 R² from a 0.85.

**Estimated time:** 6–8 hours (core lessons 14–16); the five optional appendices add roughly 5–7 hours more.
**Prerequisites:** Modules 1–3. Especially NB 8 (NumPy shapes) and NB 10 (statistics — for the metrics).

```
                  ┌────────────────────────────────────────┐
                  │  fit → predict → evaluate → iterate    │
                  └────────────┬───────────────────────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                              ▼
    NB 14 — sklearn basics            NB 15 — model evaluation
    Churn + NPS regression,           Confusion matrix, ROC, calibration,
    cross-validation, grid search     thresholds, learning curves
                ▲
                │
          NB 16 — feature engineering
          Encoding, scaling, dates,
          target leakage, selection
   ──────────────────────────────────────────────────────────────
    Optional appendix track — where scikit-learn stops
    A1 PyTorch foundations → A2 vision & sequences → A3 fine-tuning
    A4 TabPFN (tabular foundation model) · A5 conformal prediction
```

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll learn / build |
|---|---|---|---|---|
| 14 | `14_sklearn_basics.ipynb` | ~70–90 min | Intermediate | The full split → fit → predict → evaluate → iterate loop, run twice on one synthetic SaaS company: a churn classifier (four models compared, decision boundaries visualised) and an NPS regression, tuned with cross-validation and `GridSearchCV` |
| 15 | `15_model_evaluation.ipynb` | ~60–75 min | Intermediate | An honest evaluation toolkit for the same churn models: confusion matrix in cost units, threshold trade-offs, ROC/PR curves, calibration, k-fold CV (proved by hand), learning curves |
| 16 | `16_feature_engineering.ipynb` | ~55–70 min | Intermediate | Encoding, scaling, datetime, interaction and ratio features on the churn table — plus target-leakage hunting and feature selection, assembled into one leak-free `Pipeline` |

## Optional appendices at a glance

A five-notebook deep-dive track that picks up where scikit-learn stops. Appendices are optional, reference-style demos of *real* heavy libraries — but every one of them still runs 100% offline via built-in stand-ins or graceful skips, so installing the real library (commented out at the bottom of `requirements.txt`) is entirely optional.

| Appendix | Notebook | ⏱ Time | Focus |
|---|---|---|---|
| A1 | `A1_pytorch_foundations.ipynb` | ~60–90 min | Tensors, autograd, `nn.Module`, the canonical training loop; an MLP on tabular data that beats a logistic baseline |
| A2 | `A2_pytorch_vision_and_sequences.ipynb` | ~60–90 min | CNNs for images; LSTM and a tiny Transformer encoder for sequences; augmentation and transfer learning |
| A3 | `A3_pytorch_fine_tuning.ipynb` | ~60–90 min | Transfer learning on a DistilBERT-class transformer with HuggingFace; LoRA/PEFT; AMP, export and quantization |
| A4 | `A4_tabpfn_priorlab.ipynb` | ~45–60 min | TabPFN (PriorLabs) — a tabular foundation model that predicts in one forward pass; local API + cloud API |
| A5 | `A5_conformal_prediction.ipynb` | ~60–75 min | Distribution-free uncertainty: prediction intervals and sets with a coverage guarantee, built from scratch; MAPIE & friends as reference |

## Notebook guides

### 14 · Scikit-Learn Basics: Customer Churn and Feedback Classification — `14_sklearn_basics.ipynb`

This is where Modules 1–3 converge: NumPy gave you arrays, pandas tables, matplotlib charts — scikit-learn gives you a uniform toolkit for training, evaluating and using models. Rather than the classic Iris/California-housing demos, the notebook follows **one synthetic SaaS company through two questions about the same customers**: *who is about to leave?* (churn classification, Project 1) and *how happy is this customer?* (satisfaction regression, Project 2). Running the identical seven-step workflow twice is the point — once internalised, every new ML problem is a variation on it.

Two mental models carry the whole notebook: every estimator is *the same machine with two buttons* (`fit` = learn-and-remember, `predict` = apply the remembered numbers), and choosing a model means *choosing the shape of border or curve it is allowed to draw* — which you literally see via decision-boundary plots, not just accuracy numbers. A 🔬 deep dive opens up what actually happens inside `.fit()` and `.predict()`.

**Learning objectives:**
- Walk the scikit-learn workflow: split → fit → predict → evaluate → iterate.
- Build and compare classifiers (Logistic Regression, Random Forest, k-NN, …) and *see* the decision boundary each one draws.
- Bundle preprocessing with the model in a `Pipeline` to avoid data leakage.
- Evaluate with the confusion matrix, precision/recall and F1 (classification) and MAE, RMSE, R² (regression).
- Run cross-validation for honest scores and tune hyperparameters with `GridSearchCV`.
- Diagnose overfitting via the bias–variance curve and read feature importances.

**Sections:** 1 The ML workflow in one picture · 2 Setup · 3 Project 1 — customer churn prediction (generate & explore → train/test split → the sklearn API contract → a preprocessing pipeline → four classifiers compared → decision boundaries → confusion matrix → probabilities on new customers → feature importance) · 4 Project 2 — predicting customer satisfaction (linear regression → random forest → predicted-vs-actual diagnostics → the bias–variance trade-off → cross-validation → `GridSearchCV`) · 5 Common ML pitfalls (and how to avoid them).

**Practice:** 4 ✋ quick-exercise checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. a "Debug me 🐞") · 4 🧠 stretch exercises (⭐⭐⭐) · 🎁 bonus mini-project ("Your own ML cycle") · key takeaways + self-assessment.

**Datasets:** a synthetic SaaS customer table generated in-notebook (a latent "happiness" drives both the NPS score and the churn label — so classification and regression share one dataset); sklearn's built-in **Iris** and **Wine** appear only in stretch exercises C and D.

### 15 · Model Evaluation Deep Dive — `15_model_evaluation.ipynb`

NB 14 looked at accuracy; that's enough to get started, not enough to ship. This notebook carries the **same churn dataset and the same two models** (logistic regression and random forest) the whole way through and asks one escalating question: *is this model safe to ship?* Each section is a different lens on that question — read the mistakes (confusion matrix), price the mistakes (cost), choose where to act (threshold), check whether the probabilities can be trusted (calibration), and confirm the score wasn't luck (cross-validation).

The mental model: a classifier doesn't hand you a decision, it hands you a **score**, and evaluation is everything that happens between that score and a real-world action. Two knobs turn a score into a defensible decision — the *threshold* (a business choice driven by mistake costs, not a fixed 0.5) and *trust* (what calibration and CV measure). A 🔬 deep dive plus a 🧪 hand-written k-fold loop prove that `cross_val_score` isn't magic.

**Learning objectives:**
- Read a confusion matrix in *cost units*, not just counts.
- Pick between precision, recall and F1 based on which error is more expensive.
- Slide the decision threshold and visualise the precision–recall trade-off.
- Plot and interpret ROC and precision-recall curves — and know when each matters.
- Diagnose miscalibrated probabilities and recalibrate them post-hoc.
- Use cross-validation correctly (stratified folds, `Pipeline` discipline) and read learning curves to decide whether more data would help.

**Sections:** 1 Setup — load the same churn dataset · 2 Two models, same dataset, different probabilities · 3 The confusion matrix in cost units · 4 Precision, recall, F1 · 5 The threshold trade-off (incl. the confusion matrix at the cost-optimal threshold) · 6 ROC and PR curves · 7 Calibration — when probabilities lie · 8 Cross-validation — the honest evaluation · 9 Learning curves.

**Practice:** 4 ✋ quick-exercise checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. a "Debug me 🐞" that fits the scaler on all the data) · 4 🧠 stretch exercises (⭐⭐⭐: F-beta, permutation importance, expected-cost thresholds, PR-curve model comparison) · 🎁 bonus mini-project (a model-comparison report) · key takeaways + self-assessment.

**Datasets:** the synthetic churn dataset recreated exactly from NB 14; sklearn's built-in **breast-cancer** dataset in stretch exercise D.

### 16 · Feature Engineering — `16_feature_engineering.ipynb`

*"Most of what looks like a model problem is actually a feature problem."* A model can only learn what the features tell it, and better features almost always beat a fancier model — at a fraction of the cost. The notebook keeps **one dataset the whole way through** — the SaaS churn customers from NB 14/15, now enriched with a `signup_date` and a `region` — and takes one messy column at a time (a category, a wildly-scaled number, a date, a leaky shortcut) and turns it into something a model can compute with. By the end the individual moves assemble into one leak-free `Pipeline` ready for the honest cross-validation of NB 15.

Two mental models again: *a model is just arithmetic* (it can't multiply by the string `"Premium"` or a calendar date — feature engineering translates messy reality into honest numbers without inventing fake structure), and *the golden rule* — a feature may only use information that would exist at prediction time. Every "fit on train only / inside a `Pipeline`" rule is a corollary. 🔬 deep dives open up one-hot encoding mechanics and what a scaler actually *learns* (and why the test set must never be in the room).

**Learning objectives:**
- Choose the right categorical encoding (one-hot, ordinal, target) — and know when each is wrong.
- Apply scaling correctly: when it matters, when it doesn't, where the leak hides.
- Extract useful signals from datetime columns.
- Build interaction and ratio features that help linear models see non-linearity.
- Spot and prevent target leakage before it ships.
- Prune features with `SelectKBest` and assemble a complete leak-free pipeline.

**Sections:** 1 Setup — a slightly richer dataset · 2 Categorical encoding — three options, three trade-offs · 3 Scaling (incl. the leak-proof `Pipeline` pattern) · 4 Datetime features · 5 Interaction and ratio features · 6 Target leakage — the bug that ruins ML projects · 7 Feature selection · 8 A complete leak-free pipeline.

**Practice:** 4 ✋ quick-exercise checkpoints · 3 🧪 practice exercises (⭐–⭐⭐: tenure features, spot the leak, a custom transformer) · 4 🧠 stretch exercises (⭐⭐⭐: interactions, `SelectFromModel`, datetime features for a forecast, one-hot vs target encoding) · 🎁 bonus mini-project (a feature-engineering bake-off) · key takeaways + self-assessment.

**Datasets:** the NB 14/15 synthetic churn customers, rebuilt in-notebook with `signup_date` and `region` columns; a small `make_classification` toy in §7 shows how 20 noise columns drag down a cross-validated score.

## Appendix guides

The appendices are written in reference style: fewer interactive scaffolds, more "watch the library at work". Each carries an install section for the real dependency and a documented offline path — you can read and run everything without installing anything beyond the core course stack.

### A1 · PyTorch Foundations — `A1_pytorch_foundations.ipynb`

When scikit-learn isn't enough and you need to train your own neural network, PyTorch is the de-facto tool. This first notebook of the mini-track gives you the non-negotiable foundations — tensors, autograd, `nn.Module`, optimisers, the canonical training loop — and ends with an MLP on tabular data that beats a logistic-regression baseline, plus the production seasoning: the four classic bugs (NaN loss, frozen gradients, leaked test data, wrong device), regularisation knobs, LR schedules, a reusable `fit()` with early stopping, and reproducibility. A 🔬 deep dive walks through exactly what `.backward()` records and replays.

**Learning objectives:**
- Manipulate `torch.Tensor` with confidence (shapes, devices, dtypes, autograd).
- Build models with `nn.Module` and train them with the canonical training loop.
- Diagnose and avoid the four classic bugs: NaN loss, frozen gradients, leaked test data, wrong device.
- Train a small MLP on a tabular dataset and beat a logistic-regression baseline.

**Sections:** 1 Smoke test · 2 Tensors · 3 Autograd in one minute · 4 A model in 6 lines (`nn.Module`) · 5 The canonical training loop · 6 DataLoaders · 7 A real tabular dataset — beat the logistic baseline · 8 Saving and loading · 9 The four bugs you will hit · 10 Regularisation · 11 Learning-rate schedules · 12 A reusable `fit()` · 13 Reproducibility & device-agnostic code.

**Practice:** 4 ✋ quick-exercise checkpoints · 2 🧪 exercises (add early stopping; compare to a much smaller MLP).

**Real library / offline stand-in:** demos **PyTorch** (`pip install torch`, CPU wheel shown). A `HAS_TORCH` smoke test lets every runtime cell skip gracefully when torch isn't installed — the code stays readable either way. Data is synthetic (`sklearn.datasets.make_classification`), so nothing is downloaded.

### A2 · PyTorch: Vision & Sequences — `A2_pytorch_vision_and_sequences.ipynb`

A1 trained an MLP; this notebook steps into the two most-used architectural families: **CNNs** for grid data and **RNNs / a tiny Transformer encoder** for sequences — both small enough to train on a laptop CPU in under a minute. A 🔬 deep dive computes one convolution output pixel by hand and matches it against `conv2d`, you watch an edge-detector kernel fire, and a decision guide tells you when to pick an RNN vs a Transformer. It closes with the two cheapest accuracy wins in vision — data augmentation and transfer learning — and `nn.Embedding` for turning IDs into vectors.

**Learning objectives:**
- Build a CNN (`Conv2d → ReLU → Pool → … → Linear`) for image classification.
- Build an RNN (LSTM) for sequence classification.
- Build a tiny Transformer encoder and understand each block (self-attention, FFN, residual, layer-norm).
- Pick between RNN and Transformer for a given sequence task.

**Sections:** 1 Convolutional networks (toy 8×8 "digits", convolution mechanics, feature-map sizes) · 2 RNNs — the canonical sequence model · 3 A tiny Transformer encoder · 4 RNN vs Transformer — pick the right tool · 5 Data augmentation · 6 Transfer learning for vision · 7 `nn.Embedding`.

**Practice:** 4 ✋ quick-exercise checkpoints · 2 🧪 exercises (augment the CNN; a masked Transformer).

**Real library / offline stand-in:** demos **PyTorch**, with **torchvision** (`transforms`, `models.resnet18`) appearing only as reference snippets — augmentation is demonstrated with plain PyTorch ops so torchvision isn't required. All datasets are generated in-notebook (synthetic 8×8 images and synthetic sum-threshold sequences); `HAS_TORCH` skips runtime cells if torch is absent.

### A3 · PyTorch: Fine-Tuning a Transformer — `A3_pytorch_fine_tuning.ipynb`

The most useful skill in practical deep learning today: **transfer learning** — adapting a pretrained model to your task with comparatively little data. The running task is business-flavoured text classification: routing customer-support messages into three intents (billing / account / product) with a DistilBERT-class encoder (`distilbert-base-uncased`) via HuggingFace `transformers`. A 🔬 deep dive makes "freeze the body, train the head" concrete with `requires_grad` proofs, then the notebook widens out to LoRA-style PEFT, the fine-tune vs prompt-engineer vs RAG decision map, and serving topics: warmup and schedulers, gradient accumulation, mixed precision (AMP), TorchScript/ONNX export, and dynamic quantization.

**Learning objectives:**
- Load a pretrained transformer + tokenizer from HuggingFace.
- Build a `Dataset`/`DataLoader` for text classification.
- Run a fine-tuning loop with learning-rate scheduling.
- Apply LoRA-style parameter-efficient fine-tuning (PEFT) when a full fine-tune is overkill.

**Sections:** 1 Why fine-tune at all? · 2 The task — classify customer-support messages · 3 Load a pretrained tokenizer and model · 4 The fine-tuning loop (reference code) · 5 Offline stand-in — a tiny MLP on bag-of-words features · 6 LoRA in one paragraph · 7 Inference + saving · 8 Fine-tune vs prompt-engineer vs RAG · 9 Warmup, schedulers & gradient accumulation · 10 Mixed precision (AMP) · 11 Exporting for serving — TorchScript & ONNX · 12 Dynamic quantization.

**Practice:** 4 ✋ quick-exercise checkpoints · 2 🧪 exercises (build the HF fine-tune from scratch in 20 lines; detect overfitting on tiny data).

**Real library / offline stand-in:** demos **PyTorch + HuggingFace `transformers`** (with `datasets`, `accelerate`, and optional `peft`). The HF fine-tuning loop and LoRA config are reference code; the notebook's runnable path is an explicit **offline stand-in** — a tiny MLP trained on bag-of-words features over the same in-notebook support-message dataset — so it works with no downloads and no model weights.

### A4 · TabPFN: Tabular Foundation Models — `A4_tabpfn_priorlab.ipynb`

Gradient-boosted trees have long been the tabular default — TabPFN (PriorLabs; Hollmann et al., ICLR 2023 / Nature 2025) does something genuinely surprising: a transformer *pretrained on millions of synthetic tabular datasets* solves a new task in a **single forward pass** — no gradient descent, no hyperparameter grid. The notebook explains the prior-fitted-network idea, builds the in-context-learning mental model with a runnable weighted-NN analogy (explicitly flagged as an analogy for the data-flow, *not* the mechanism), benchmarks sklearn baselines on a small tabular task, then shows the local TabPFN API, the PriorLabs cloud API for bigger jobs, and TabPFN-TS for zero-shot time-series forecasting — plus the honest limits (~10 k rows × 100 features × 10 classes).

**Learning objectives:**
- Understand the *prior-fitted network* idea: a model pretrained on Bayesian inference itself.
- Install and run TabPFN locally on small tabular datasets (≤ 10 k rows, ≤ 100 features).
- Call the PriorLabs cloud API for bigger jobs.
- Pick between TabPFN, gradient boosting and a neural network for *your* tabular task.

**Sections:** 1 What TabPFN actually is · 2 The mental model (in-context learning for tables) · 3 Hands-on — TabPFN vs gradient boosting on a small tabular task · 4 TabPFN — the API (reference code) · 5 The PriorLabs cloud API · 6 When TabPFN is the right call · 7 TabPFN-TS — same idea, for time series. Ends with 📚 references.

**Practice:** 3 ✋ quick-exercise checkpoints · 2 🧪 exercises (calibration matters; a synthetic small-data sweep).

**Real library / offline stand-in:** demos **`tabpfn`** (local, ~250 MB of weights) and **`tabpfn-client`** (hosted API). Offline, the notebook runs the sklearn side of the comparison (logistic regression + `GradientBoostingClassifier` on a `make_classification` task) and the runnable in-context analogy; the actual TabPFN and cloud-API calls are commented reference code you can activate after installing.

### A5 · Conformal Prediction: Distribution-Free Uncertainty — `A5_conformal_prediction.ipynb`

NB 15 taught you to calibrate probabilities — but a calibrated model still gives no honest error bar on "delivery in 38 minutes". **Conformal prediction** is a thin wrapper around *any* trained model that turns point predictions into **prediction intervals** (regression) or **prediction sets** (classification) with a finite-sample coverage guarantee — "the true value lands in this band ≥ 90% of the time" — resting on a single assumption (exchangeability). The notebook builds split conformal from one idea, proves the coverage empirically, makes the bands adaptive with CQR, reads classification set size as an honesty signal, and shows what to do when the guarantee breaks under time-series drift (ACI / EnbPI).

**Learning objectives:**
- State the conformal guarantee and the **one** assumption it rests on (exchangeability).
- Implement split (inductive) conformal regression and classification from scratch — and prove the coverage holds.
- Make intervals adaptive to local difficulty with CQR (conformalized quantile regression).
- Read prediction sets in classification as an honesty signal (set size = ambiguity).
- Handle the case where the guarantee breaks: time series and distribution shift (ACI / EnbPI).
- Map the idea to the production libraries: MAPIE, crepes, puncc, TorchCP.

**Sections:** 1 The problem — a point prediction is a guess with no guarantee · 2 The one idea (and the one assumption) — split conformal in four moves · 3 The adaptivity problem — CQR · 4 Classification — prediction *sets*, not a single label · 5 Time series & distribution shift — when the guarantee breaks · 6 The packages you'd use in production · 7 When to reach for it — and the traps.

**Practice:** 4 ✋ quick-exercise checkpoints · 2 🧪 exercises (does coverage really track 1 − α?; Mondrian class-conditional coverage).

**Real library / offline stand-in:** references **MAPIE** and **crepes** (plus `puncc` and `TorchCP`), but unlike the other appendices nothing extra is needed at all — every method is implemented *from scratch* on the core stack (`numpy`, `scikit-learn`, `scipy`), and the library snippets (MAPIE v1 regression/CQR/classification, EnbPI/ACI) are copy-ready reference code. Data is synthetic: a delivery-time-style regression task with fan-out noise, plus a `make_classification` task for prediction sets.

## How these notebooks work

Every notebook opens with a Colab badge and a metadata line (module · estimated time · difficulty), then teaches in a steady rhythm: short explained code cells, ✋ **Quick exercise (~2 min)** checkpoints with collapsible solutions, 🔬 "what actually happens" deep dives and 🔮 predict-the-output boxes, then a closing block of 🧪 practice exercises (⭐-rated, including a "Debug me 🐞"), 🧠 stretch exercises, a 🎁 bonus mini-project, key takeaways and a self-assessment. One drumbeat runs through the whole module: always split; never tune on the test set; read the confusion matrix, not just accuracy; treat probabilities — not labels — as the model's real output; and hunt target leakage relentlessly. Everything runs 100% offline on synthetic or sklearn built-in data. The appendices are optional reference-style demos with lighter scaffolding: they showcase real libraries (PyTorch, HuggingFace, TabPFN, MAPIE) but always run end-to-end without them via built-in stand-ins or graceful skips — the heavy dependencies stay commented out at the bottom of `requirements.txt` until you choose to install them.

## Where next

→ **Module 5 — Industry Applications** (`../05_industry_applications/17_churn_clv_retention.ipynb`) to apply Modules 1–4 to churn, fraud, segmentation and forecasting (spiral-path order), or
→ **Module 6 — AI Engineering** (`../06_ai_engineering/22_ai_workflows.ipynb`) to go straight to the LLM layer.
