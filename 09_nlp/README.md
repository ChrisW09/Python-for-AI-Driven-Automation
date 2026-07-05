# Module 9 — NLP (Text Analytics)

**Goal:** Turn unstructured text — reviews, support tickets, survey verbatims, social posts — into structure you can act on. Discover *what* people are talking about (**topic modeling**) and *how they feel* about it (**sentiment analysis**), using the libraries practitioners actually reach for.

**Estimated time:** 2–4 hours.

**Prerequisites:** Module 4 (NB 14 sklearn basics), Module 6 NB 23 (embeddings & retrieval). NumPy fluency (NB 8) helps.

> 📎 **Optional, reference-style module.** Like the appendices, these notebooks demo a library at work rather than drilling exercises. **Every notebook runs end-to-end offline** via a small built-in scikit-learn stand-in — install the optional library to swap in the real thing.

```
         ┌────────────────────────────────────────────┐
         │   raw text  →  structure you can act on    │
         └─────────────────────┬──────────────────────┘
         ┌─────────────────────┴─────────────────────┐
         ▼                                           ▼
   WHAT are they talking about?             HOW do they feel?
┌──────────────────────────────┐    ┌────────────────────────────────┐
│ NB 35 — BERTopic             │    │ NB 37 — Sentiment analysis     │
│ embed → UMAP → HDBSCAN       │    │ lexicon (VADER) →              │
│ → c-TF-IDF topic labels      │    │ classical ML (TF-IDF+LogReg) → │
│                              │    │ transformers (HF pipeline)     │
│ NB 36 — STREAM               │    └────────────────────────────────┘
│ one API over LDA/NMF/ETM/    │
│ CTM/KmeansTM… + evaluation   │
└──────────────────────────────┘
```

## Notebooks at a glance

| # | Notebook | ⏱ Time | Difficulty | What you'll learn / build |
|---|---|---|---|---|
| 35 | `35_topic_modeling_bertopic.ipynb` | ~45–75 min | Intermediate | **BERTopic** — embedding-based topic modeling (embed → UMAP → HDBSCAN → c-TF-IDF); read `get_topic_info()`, embrace outlier topic `-1`, merge topics, swap custom components |
| 36 | `36_topic_modeling_stream.ipynb` | ~45–75 min | Intermediate | **STREAM** (`stream-topic`) — one `fit`/`get_topics` API over classical, neural *and* clustering topic models, plus a proper evaluation suite (coherence/diversity), `optimize_and_fit`, and downstream prediction |
| 37 | `37_sentiment_analysis.ipynb` | ~45–75 min | Beginner → Intermediate | The **sentiment ladder** — lexicon/rule-based (VADER) → TF-IDF + LogReg workhorse → transformer `pipeline`; aspect-based sentiment & pitfalls |

## Notebook guides

### 35 · Topic Modeling with BERTopic — `35_topic_modeling_bertopic.ipynb`

You have 50,000 support tickets, a year of product reviews, or 3,000 free-text survey answers — nobody will read them all. Topic modeling builds the *map*: which themes exist, how big each cluster is, and where the outliers hide. The notebook's running mental model is the **automatic librarian** — group notes by *meaning*, shelve them, write a spine label per shelf, and keep a "misc" cart (topic `-1`) for notes that fit nowhere.

It explains the four-stage pipeline conceptually, shows the real BERTopic API verbatim, then builds a tiny sklearn-only stand-in so everything runs on a laptop with no downloads. From there: reading `get_topic_info()` / `get_topic()` / `get_document_info()`, visualising topic sizes and words, merging over-split topics with `reduce_topics`, an honest LDA-vs-BERTopic comparison table, and swapping custom components (embedder, UMAP, HDBSCAN, vectorizer) — ending with dynamic, hierarchical, and LLM-enhanced topic representations.

**Learning objectives:**
- Explain the **BERTopic pipeline** — *embed → reduce (UMAP) → cluster (HDBSCAN) → describe (c-TF-IDF)* — and why each stage is there.
- Run `fit_transform` on a list of documents and read `get_topic_info()`, `get_topic()`, and `get_document_info()`.
- Understand **topic `-1`** (the outlier/noise topic) and why it is a feature, not a bug.
- Contrast BERTopic with classical **LDA** and know when each is the right tool.
- Swap in **custom components** (embedding model, UMAP, HDBSCAN, vectorizer) and reduce the topic count.
- Know where this goes next: dynamic, hierarchical, and **LLM-enhanced** topic representations.

**Sections:** 1 Setup & the offline smoke test · 2 A small, honest corpus · 3 How BERTopic thinks — the four-stage pipeline · 4 The real BERTopic API · 5 The offline stand-in — BERTopic in ~40 lines of sklearn · 6 One object, two implementations · 7 Reading the results · 8 Visualising topics · 9 Topic `-1` — outliers are a feature · 10 Too many topics? Merge them · 11 BERTopic vs classical LDA · 12 Custom components — the real power · 13 Beyond the basics · 14 Where this pays off in business

**Practice:** 3 ✋ quick exercises (~2 min, collapsible solutions) · 3 🧪 end-of-notebook exercises (open-ended) · ✅ self-assessment checklist.

**Libraries & offline behaviour:**

```bash
pip install bertopic   # optional — pulls sentence-transformers (+ PyTorch), umap-learn, hdbscan
```

That one line pulls a surprisingly large stack (expect a few hundred MB); the default embedder is `all-MiniLM-L6-v2`. A single `HAS_BERTOPIC` flag guards every real-API cell; without the install, a ~40-line sklearn stand-in (TF-IDF + KMeans) mimics the same interface (`fit_transform`, `get_topic_info`, `get_topic`, `get_document_info`), and charts are drawn with matplotlib/seaborn instead of BERTopic's plotly visualizations.

**Datasets:** 36 short inline documents across five deliberately obvious themes — cloud computing, customer churn, healthcare, sports, cooking — so you can eyeball whether the model recovered them. No files, no downloads.

### 36 · Topic Modeling with STREAM — `36_topic_modeling_stream.ipynb`

NB 35 gave you one excellent, opinionated pipeline. But which topic model is best for *your* pile of text? **STREAM** ([`stream-topic`](https://github.com/AnFreTh/STREAM)) is a **unified API over many topic models** — classical (`LDA`, `NMF`), neural (`ETM`, `CTM`, `ProdLDA`, `NeuralLDA`, `NSTM`, `TNTM`, `WordCluTM`), and clustering/embedding (`KmeansTM`, `CEDC`, `DCTE`, `SomTM`, `CBC`) — all trained with the same `model.fit(dataset, n_topics=…)` → `model.get_topics()` calls. The mental model is a **test kitchen**: same ingredients (your corpus), swappable chefs (models), and a consistent panel of judges (the evaluation metrics), so you can say which recipe was *actually* better.

The bake-off runs on a voice-of-customer corpus: fit `KmeansTM`, swap to `ProdLDA` with a one-line change, read `get_beta`/`get_theta` (what a probabilistic model gives you that a clustering model doesn't), score topics with embedding-based coherence/diversity metrics plus classic NPMI, sweep the number of topics with `optimize_and_fit`, and finish with STREAM's `DownstreamModel` — an interpretable Neural Additive Model that predicts an outcome from topic proportions.

**Learning objectives:**
- Explain what STREAM adds on top of a single pipeline like BERTopic — a **unified interface** across classical, neural and clustering topic models.
- Load and preprocess a corpus with `TMDataset` and fit a model with the canonical `fit` / `get_topics` flow.
- Swap model families (`KmeansTM` ↔ `ProdLDA`) with no other code change, and know when to reach for **probabilistic** (`get_beta`/`get_theta`) vs **clustering** models.
- Evaluate topics with embedding metrics (`ISIM`/`INT`/`ISH`/`Expressivity`) and classic `NPMI`, and read the difference.
- Search the number of topics with `optimize_and_fit`, and understand the `DownstreamModel` (NAM) idea for prediction.

**Sections:** 1 Setup & offline smoke-test · 2 A small business corpus · 3 The offline stand-in · 4 Fitting a model — the canonical STREAM flow · 5 The killer feature — swap the model, change nothing else · 6 `get_beta` and `get_theta` — what a probabilistic model gives you · 7 Evaluation — is this topic model any good? · 8 How many topics? `optimize_and_fit` · 9 Visualization · 10 Downstream prediction with a Neural Additive Model

**Practice:** 4 ✋ quick exercises (~2 min, collapsible solutions) · 5 🧪 end-of-notebook exercises (the last one needs a real STREAM install) · ✅ self-assessment checklist.

**Libraries & offline behaviour:** `pip install stream-topic` (also pulls `lightning` for the NAM and sentence-transformers for the embedding metrics). A `HAS_STREAM` flag guards every real cell; offline, a `StandInTopicModel` (TF-IDF + sklearn `NMF` — itself a legitimate classical topic model) mirrors the STREAM API (`fit`, `get_topics`, `get_beta`, `get_theta`), a NumPy **NPMI proxy** replaces the metric suite, PCA replaces the built-in visualizations, and plain `LinearRegression` stands in for the downstream NAM.

**Datasets:** ~36 short inline business documents — product reviews, support tickets, and finance/news snippets — with three baked-in themes (shipping/delivery, app/login/technical, price/billing). With the real library, the same docs are wrapped in a `TMDataset` (falling back to the bundled `BBC_News` corpus if that fails).

### 37 · Sentiment Analysis — `37_sentiment_analysis.ipynb`

Sentiment analysis turns free text into a *signal you can aggregate* — positive/negative/neutral or a polarity score — the thing that answers "did sentiment drop after the price change?" or "route this angry ticket to a human now." The running mental model is the **sentiment ladder**: rung 1 a **lexicon** (VADER — no training, instant, transparent), rung 2 **classical ML** (TF-IDF + Logistic Regression — the workhorse, shockingly hard to beat in-domain), rung 3 a **transformer** (context-aware, strongest, heaviest). Golden rule: *climb only as high as the problem forces you to.*

The same six gadget-review snippets — including deliberate negation, sarcasm, and mixed-opinion traps — are scored on every rung so you can watch each method pass or fail on identical text. Along the way you inspect `.coef_` to see which words drive the classical model, compare all three rungs side by side (with a keep-it cheat-sheet), build a toy word-window **aspect-based sentiment** scorer, and close with practitioner pitfalls: sarcasm, domain shift, the neutral class, class imbalance, calibration, and mapping stars to sentiment.

**Learning objectives:**
- Explain the **three families** of sentiment methods and pick one for a given business constraint (latency, labels, accuracy, interpretability).
- Run a **lexicon scorer**, read its `compound` score, and explain the tricks VADER handles (negation, intensifiers, emoji, CAPS, punctuation).
- Train, evaluate, and **inspect** a TF-IDF + LogisticRegression classifier — including reading `.coef_` to see *which words drive the prediction*.
- Call a Hugging Face `pipeline("sentiment-analysis")` and name a few domain-specific models (FinBERT, twitter-roberta).
- Describe **aspect-based** sentiment and the **pitfalls** (sarcasm, domain shift, neutral class, class imbalance, calibration, stars→sentiment).

**Sections:** 0 Setup & imports · 1 Lexicon / rule-based sentiment — VADER · 2 Classical ML — TF-IDF + Logistic Regression (the workhorse) · 3 Transformers — Hugging Face `pipeline` · 4 Side-by-side: the three rungs of the ladder · 5 Aspect-based sentiment (ABSA) · 6 Pitfalls & practitioner notes

**Practice:** 3 ✋ quick exercises (~2 min, collapsible solutions) · 6 🧪 end-of-notebook exercises (one needs `transformers`) · ✅ self-assessment checklist.

**Libraries & offline behaviour:** `pip install vaderSentiment transformers torch` — all optional, behind `HAS_VADER` / `HAS_TRANSFORMERS` capability flags. Offline, VADER is replaced by a minimal built-in lexicon scorer (hand-set word valences + negation flipping), and the transformer rung falls back to the Section-2 classical model — the notebook guards the *model download* too, not just the import, so it survives a no-network machine even with `transformers` installed. The classical rung is plain scikit-learn and always real.

**Datasets:** six running-example review snippets (love/hate/neutral/negated/sarcastic/mixed) plus 62 inline labeled gadget/product reviews (with deliberately "hard" mixed-vocabulary cases) for training the classifier.

## How these notebooks work

Module 9 is optional and written reference-style: each notebook demos a real library's API verbatim, but a `try/except` import sets a capability flag (`HAS_BERTOPIC`, `HAS_STREAM`, `HAS_VADER`, `HAS_TRANSFORMERS`) and every heavy cell degrades gracefully to a built-in scikit-learn/NumPy stand-in — so everything runs 100% offline, and installing the real library simply swaps the backend. Short "✋ Quick exercise (~2 min)" checkpoints with collapsible `<details>` solutions punctuate each notebook, and each one closes with a 🧪 exercise block of open-ended extensions (no autograder here, unlike the core modules), a 🧠 key-takeaways recap, and a ✅ self-assessment checklist to gauge what stuck. The habits this module drills: read the topics, don't trust the count (always inspect topic words and the `-1` outlier topic); pick embeddings vs. bag-of-words deliberately; start sentiment classical before reaching for transformers; and beware domain shift and sarcasm — validate on *your* text.

## Where next

→ **Module 10 — DeepTab** (`../10_deeptab/38_deeptab_tabular_deep_learning.ipynb`) for deep learning on *tabular* data, or
→ back to **Module 6 — AI Engineering** (`../06_ai_engineering/23_embeddings_retrieval.ipynb`) to combine these signals with retrieval and LLMs.
