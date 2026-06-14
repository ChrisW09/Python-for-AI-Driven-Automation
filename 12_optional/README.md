# Module 12 — Optional: Text Analytics (Topic Modeling & Sentiment)

**Goal:** Turn unstructured text — reviews, support tickets, survey verbatims, social posts — into structure you can act on. Discover *what* people are talking about (**topic modeling**) and *how they feel* about it (**sentiment analysis**), using the libraries practitioners actually reach for.

**Estimated time:** 2–4 hours.
**Prerequisites:** Module 4 (NB 14 sklearn basics), Module 5 NB 18 (embeddings & retrieval). NumPy fluency (NB 8) helps.

> 📎 **Optional, reference-style module.** Like the appendices, these notebooks demo a library at work rather than drilling exercises. **Every notebook runs end-to-end offline** via a small built-in scikit-learn stand-in — install the optional library to swap in the real thing.

```
                 ┌─────────────────────────────────────────────┐
                 │   raw text  →  structure you can act on      │
                 └───────────────────────┬─────────────────────┘
              ┌──────────────────────────┴───────────────────────┐
              ▼                                                   ▼
        WHAT are they talking about?                     HOW do they feel?
        ┌───────────────────────────┐                 ┌──────────────────────┐
        │ NB 43 — BERTopic           │                 │ NB 45 — Sentiment    │
        │ embed → UMAP → HDBSCAN     │                 │ lexicon (VADER) →    │
        │ → c-TF-IDF topics          │                 │ classical ML →       │
        │                            │                 │ transformers         │
        │ NB 44 — STREAM             │                 └──────────────────────┘
        │ one API over LDA/NMF/ETM/  │
        │ CTM/Kmeans… + evaluation   │
        └───────────────────────────┘
```

## Notebooks

| # | Notebook | What you'll learn |
|---|---|---|
| 43 | `43_topic_modeling_bertopic.ipynb` | **BERTopic** — embedding-based topic modeling (embed → UMAP → HDBSCAN → c-TF-IDF), modular components, topic reduction & visualization |
| 44 | `44_topic_modeling_stream.ipynb` | **STREAM** (`stream-topic`) — one unified API over classical *and* neural topic models, plus a proper evaluation suite (coherence/diversity) and downstream prediction |
| 45 | `45_sentiment_analysis.ipynb` | **Sentiment** three ways — lexicon/rule-based (VADER), the classical TF-IDF + LogReg workhorse, and transformer pipelines; aspect-based sentiment & pitfalls |

## The disciplines this module trains

- **Read the topics, don't trust the count.** A "20-topic" model is only as good as the words in each topic — always inspect representations and the outlier topic (`-1`).
- **Embeddings beat bag-of-words for *meaning*** — but classical NMF/LDA are faster, fully interpretable, and a fine baseline. Pick deliberately.
- **Sentiment: start classical.** A TF-IDF + logistic-regression baseline is fast, calibratable, and explainable via its coefficients. Reach for transformers when the baseline plateaus.
- **Beware domain shift & sarcasm.** A model trained on movie reviews will misread financial filings or support tickets. Validate on *your* text.

## Install (optional — every notebook runs offline without these)

```bash
pip install bertopic          # NB 43 — pulls sentence-transformers, umap-learn, hdbscan
pip install stream-topic      # NB 44 — AnFreTh/STREAM
pip install vaderSentiment    # NB 45 — lexicon sentiment
pip install transformers torch  # NB 45 — transformer sentiment pipelines
```

## Where next

→ **Module 13 — DeepTab** (`../13_DeepTab/46_deeptab_tabular_deep_learning.ipynb`) for deep learning on *tabular* data, or
→ back to **Module 5 — AI Engineering** (`../05_ai_engineering/18_embeddings_retrieval.ipynb`) to combine these signals with retrieval and LLMs.
