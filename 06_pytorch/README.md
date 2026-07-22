# Module 6 — Deep Learning with PyTorch

> 🧭  [◀ Machine Learning](../05_machine_learning/)  ·  [🏠 Course home](../README.md)  ·  [Industry Applications ▶](../07_industry_applications/)

**Goal:** Open the black box under every model in the second half of this course. You'll write the training loop that scikit-learn hides, train neural networks *honestly* (validation curves, regularisation, early stopping), give categorical data learned **embeddings**, race your network against gradient boosting with no thumb on the scale — and wrap the result behind a scikit-learn API, ready to serve.

**Estimated time:** ~3.5–4.5 hours (three lessons of ~65–80 min each, plus exercises).
**Prerequisites:** Module 5 is essential — NB 8 (NumPy shapes), NB 17–18 (sklearn workflow, ROC-AUC, the "never tune on test" discipline), NB 19 (encoding & the golden rule). NB 6 (classes) for `nn.Module`. Nothing later than Module 5 is assumed.

```
        scikit-learn gave you  model.fit(X, y)  — this module hands you the inside:

   NB 20 — the machine            NB 21 — the craft             NB 22 — the payoff
   tensors → autograd →           DataLoaders · overfitting     embeddings for categories
   nn.Module → the 5-step         dropout · weight decay        the honest bake-off vs GBM
   training loop · churn MLP      early stopping · schedules    sklearn wrapper · TorchScript
   vs logistic baseline           save/load · seeds · 4 bugs    → serving
                    └────────────────── one dataset throughout: the NB 17/18 SaaS churn customers ─┘
```

Everything in this module runs **100% offline** — PyTorch is a local library, not a service: no API key, no network, and every model trains on a laptop CPU in seconds (the datasets are small on purpose). **Google Colab has PyTorch preinstalled**, so the Colab badges just work; locally, one `pip install torch` (CPU wheel) is the only extra. Without torch installed, every runtime cell checks `HAS_TORCH` and skips gracefully — the code stays readable either way.

> 🗺️ **How this relates to the Module 5 appendix track (A1–A3).** The appendices are the *condensed reference tour* of PyTorch — "watch the library at work", lighter scaffolding. This module is the **full classroom treatment**: slower, on the course's own churn data, with the complete checkpoint/exercise/debug-me apparatus. Do either first; they reinforce each other. Beyond this module, [A2 (vision & sequences)](../05_machine_learning/A2_pytorch_vision_and_sequences.ipynb) and [A3 (fine-tuning transformers)](../05_machine_learning/A3_pytorch_fine_tuning.ipynb) remain the breadth extensions for images, sequences and transfer learning — and [Module 12 (DeepTab)](../12_deeptab/) is NB 22's architecture, industrial-strength.

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll build |
|---|---|---|---|---|
| 50 | `20_pytorch_fundamentals.ipynb` | ~80 min | Intermediate → Advanced | Tensors, autograd, `nn.Module` and the five-step training loop — gradient descent watched live, then an MLP churn classifier racing a logistic baseline |
| 51 | `21_training_neural_networks.ipynb` | ~70 min | Intermediate → Advanced | The training craft: `DataLoader`s, the two-curve overfitting diagnostic, dropout/weight decay/early stopping, LR schedules, `state_dict` save/load, seeds & devices, a live four-bug clinic |
| 52 | `22_pytorch_in_practice.ipynb` | ~65 min | Advanced | `nn.Embedding` for categoricals (watch the model map its own regions), an honest bake-off vs gradient boosting, a sklearn-style `TorchTabularClassifier`, TorchScript export |

## Notebook guides

### 20 · PyTorch Fundamentals — `20_pytorch_fundamentals.ipynb`

Everything AI-shaped in this course — the LLMs of Module 8, the transformers behind BERTopic, DeepTab — is a neural network trained with gradient descent in PyTorch (or a framework on top of it). This lesson builds the four load-bearing ideas in order — **tensors → autograd → `nn.Module` → the training loop** — each verified with your own eyes (autograd is checked against calculus once, so you trust it forever). The mental model: *training is a thermostat loop* — forward (guess), loss (how wrong?), backward (which way is downhill?), step (nudge every knob), zero (clean slate). It ends on familiar ground: an MLP churn classifier on the NB 17/18 SaaS dataset that has to face a logistic-regression baseline — and roughly ties it, which is the honest result that frames the whole module.

**Learning objectives:**
- Manipulate `torch.Tensor`s (shapes, dtypes, broadcasting, NumPy interop) and name the two things they add over NumPy (autograd + devices).
- Use autograd (`requires_grad` → `.backward()` → `.grad`) and explain why gradients must be **zeroed** every step.
- Write gradient descent **by hand**, then rebuild it idiomatically with `nn.Module`, `nn.MSELoss`/`nn.BCEWithLogitsLoss` and `SGD`/`Adam` — mapping every idiom back to the by-hand version.
- Explain what hidden layers + ReLU buy (learned feature engineering) and read **logits → sigmoid → probabilities** correctly.
- Train a churn MLP and compare it honestly (ROC-AUC) against `LogisticRegression`.

**Sections:** 1 Where scikit-learn stops · 2 Setup & smoke test · 3 Tensors · 4 Autograd · 5 Gradient descent, watched live (fit a line to ad spend) · 6 The same fit, the PyTorch way · 7 From line to network — why hidden layers · 8 The real thing: a churn classifier (logits, BCE, the baseline scoreboard).

**Practice:** 4 ✋ checkpoints · 5 🧪 practice exercises (⭐–⭐⭐, incl. a 🐞 debug-me on the missing `zero_grad`) · 4 🧠 stretch exercises (be-the-optimizer, lr sweep, multiclass `CrossEntropyLoss`, logistic-regression-*is*-a-one-layer-net) · 🎁 bonus mini-project: your own `fit()` with train/val history · ✅ self-assessment.

**Offline:** synthetic data generated in-notebook (same seed as NB 17/18); `HAS_TORCH` guard throughout.

### 21 · Training Neural Networks Well — `21_training_neural_networks.ipynb`

"The loss went down" is a low bar: a network will happily **memorise** the training set and call it learning. This lesson is the craft of catching and preventing that. The mental model: *capacity is a loan; the validation curve is the repayment schedule.* A deliberately oversized network on deliberately tiny data makes overfitting visible (the unforgettable two-curve plot), then each treatment is applied and *watched working*: dropout + weight decay, early stopping with patience and best-weight restore, learning-rate schedules. Around that core, the professional habits: proper train/val/test three-way splits, `Dataset`/`DataLoader` batching, `state_dict` save/load, seeds, device-agnostic code — and a **bug clinic** that runs the four classic failures live (exploding/NaN loss, frozen loss, silent shape broadcasting, forgotten `train()`/`eval()` modes).

**Learning objectives:**
- Batch with `TensorDataset` + `DataLoader`; define step vs. epoch; say what mini-batches buy.
- Read overfitting off the two-curve diagnostic and treat it with dropout, weight decay and early stopping.
- Replace lr-fiddling with `StepLR` / `ReduceLROnPlateau`.
- Save/load via `state_dict` (with `map_location`), snapshot best weights, and write reproducible, device-agnostic code.
- Diagnose the four classic bugs from their symptoms, fast.

**Sections:** 1 Setup — a proper three-way split · 2 Mini-batches (`Dataset`/`DataLoader`) · 3 The two-curve diagnostic — watch a network memorise · 4 Dropout & weight decay · 5 Early stopping · 6 LR schedules · 7 Saving & loading · 8 Reproducibility & devices · 9 The bug clinic.

**Practice:** 4 ✋ checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. a 🐞 debug-me: validating in `train()` mode with dropout firing) · 4 🧠 stretch exercises (gradient clipping, 5-fold CV for a net, a custom `Dataset`, optimizer bake-off) · 🎁 bonus mini-project: a mini-`Trainer` (batching + schedule + early stopping + restore — Lightning in miniature) · ✅ self-assessment.

**Offline:** same churn data rebuilt in-notebook; `HAS_TORCH` guard throughout.

### 22 · PyTorch in Practice: Embeddings, Baselines & Serving — `22_pytorch_in_practice.ipynb`

The business lesson. First, deep learning's genuinely new gift to tabular data: **`nn.Embedding`** turns categories into *learned vectors* — the notebook trains a 2-D region embedding and plots the map the model drew for itself (high-churn markets end up neighbours; nobody told it). Those embeddings join scaled numerics in a **tabular network** — the entity-embeddings architecture behind Module 12's DeepTab — complete with the UNK-at-index-0 convention that survives unseen categories. Then the reckoning: an **honest bake-off** against logistic regression, random forest and `HistGradientBoosting` (spoiler: on 600 near-linear rows the thirty-second baseline wins — and the lesson is *why*, and what would flip it). Finally, shipping: a `TorchTabularClassifier` that speaks fluent sklearn (`fit`/`predict_proba`, `clone`-able, survives `cross_val_score`), the three serving artifacts (weights + scaler + vocab), and TorchScript export — with ONNX/quantization pointers into appendix A3. Closes with the module's decision guide: boosting vs. embeddings vs. TabPFN vs. transfer learning, chosen by problem, not ideology.

**Learning objectives:**
- Explain `nn.Embedding` as a trainable lookup table; pick dimensions (`min(50, (card+1)//2)`); handle unseen categories with the UNK convention.
- Build the embeddings ⊕ numerics tabular architecture.
- Run a fair bake-off and state from evidence when deep learning earns its keep on tables.
- Wrap a torch model behind the sklearn API so NB 18's whole evaluation toolkit applies untouched.
- Package a model for serving (three artifacts; TorchScript) and route new problems through the decision guide.

**Sections:** 1 The tabular reality check · 2 Setup — churn data with a second categorical (`region`) · 3 `nn.Embedding` — a lookup table that learns (the region map) · 4 The tabular network · 5 The bake-off · 6 A sklearn-style wrapper · 7 Serving — TorchScript & the three artifacts · 8 The decision guide.

**Practice:** 4 ✋ checkpoints · 4 🧪 practice exercises (⭐–⭐⭐, incl. a 🐞 debug-me: the LATAM customer that crashes a vocab with no UNK slot) · 4 🧠 stretch exercises (high-cardinality one-hot vs embedding, embeddings-as-features for simpler models, a two-head multi-task net, `EmbeddingBag` text classification) · 🎁 bonus mini-project: DeepTab-lite certified via `cross_val_score`, raced against boosting with error bars · ✅ self-assessment.

**Offline:** synthetic data in-notebook; `HAS_TORCH` guard throughout; TorchScript demo cleans up after itself.

## The discipline this module trains

1. **The loop is the whole game.** Forward → loss → backward → step → zero trains everything from a 2-parameter line to an LLM; every framework is packaging around it.
2. **Validation curves over vibes.** Capacity is a loan; every dial (epochs, width, dropout, lr) is set against data the model hasn't seen — and the test set is opened once.
3. **Baselines are brutal, on purpose.** Both bake-offs in this module end with the humble model tying or winning on small tabular data. Deep learning's rent comes from embeddings, modalities, transfer and scale — reasons, or no network.
4. **Models are artifacts.** `state_dict` + fitted scaler + vocab travel together; reload and verify before anything ships. A PyTorch model in production is a file plus a function, subject to Module 13/12 discipline like everything else.

## How these notebooks work

Each lesson follows the course rhythm: short teaching sections punctuated by **✋ Quick exercise (~2 min)** checkpoints with collapsible solutions (executed in a fresh kernel), then a graded block — 🧪 practice exercises (⭐-rated, each set with a 🐞 debug-me), 🧠 stretch exercises, and a 🎁 bonus mini-project — closing with key takeaways, a ✅ self-assessment and the 🚀 next step. One dataset (the NB 17/18 SaaS churn customers) carries through all three lessons, so every new mechanism lands on familiar ground.

## Where next

→ **Module 7 — Industry Applications** (`../07_industry_applications/`) — the spine continues: churn value, fraud, segmentation and demand, with your new deep-learning judgment in your back pocket.
→ **Module 12 — DeepTab** (`../12_deeptab/`) — NB 22's entity-embedding architecture, industrial-strength (FT-Transformer, SAINT, Mamba) behind the same sklearn API you just built by hand.
→ **Module 5 appendices A2–A3** (`../05_machine_learning/`) — CNNs, RNNs, a tiny Transformer, then fine-tuning pretrained transformers: the modalities and transfer learning this module kept pointing at.
→ **Module 13 — Production** (`../13_production/`) — your wrapper is an artifact; ship it like one.

---

📝 **Finished this module?** Test yourself with the [Module 6 quiz](../quizzes/quiz_06_pytorch.ipynb) — five questions, ~10 minutes.
