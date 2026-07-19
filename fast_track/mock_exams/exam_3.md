# Fast Track — Mock Exam 3

**Python for AI-Driven Automation & Business Data Science**
**Scenario: PayFlow — a fintech payments company**

---

You are a data/AI engineer at **PayFlow**, a fintech that processes card payments and account-to-account transfers. Your world is transactions, fraud scoring, KYC (know-your-customer) document checks, merchant analytics, and the automation/AI systems that keep it all running. Every question below is framed in that world.

**Instructions**

- **Time:** 120 minutes. **Total:** 100 marks.
- The paper has **5 parts (A–E), ~20 marks each**. Attempt **all** questions.
- Marks are shown in brackets, e.g. *(4 marks)*.
- For **MCQ**, write the single letter of the one best answer.
- For **write-the-code** and **debug** questions, write idiomatic, runnable Python (modern pandas / scikit-learn) or SQL. Minor syntax slips are not penalised if the intent is unambiguous.
- Assume the usual imports are available: `import pandas as pd`, `import numpy as np`, and the relevant `sklearn` / `scipy` / `bs4` names where needed. State any extra assumptions you make.
- This is a **parallel-form** exam: it samples the whole fast track (NB 1–22).

---

## Part A — Python foundations *(NB 1–5)* — 20 marks

**A1.** *(2 marks, MCQ)*
While reconciling a refund, a PayFlow script evaluates `int(-3.9)`. What does it return?

- A) `-4`
- B) `-3`
- C) `0`
- D) `4`

**A2.** *(2 marks, MCQ)*
A pagination helper does `size = requested or 50`. A caller passes `requested = 0` (meaning "return no rows"). What is `size`?

- A) `0`
- B) `50`
- C) `None`
- D) It raises `ValueError`

**A3.** *(3 marks, short answer)*
A colleague writes this helper to append a transaction to a batch:

```python
def add_txn(txn, batch=[]):
    batch.append(txn)
    return batch
```

Explain precisely what goes wrong when this function is called on several *different* batches over the life of the program, and rewrite the signature (and body as needed) to fix it.

**A4.** *(5 marks, write-the-code)*
Write a class `Wallet` that models a customer's PayFlow wallet:

- `__init__(self, owner, balance=0.0)` — stores the owner name and an opening balance (default `0.0`).
- `deposit(self, amount)` — increases the balance.
- `withdraw(self, amount)` — decreases the balance, but **raises `ValueError`** if `amount` exceeds the current balance.
- `statement(self)` — returns a string like `"alice: 120.50 EUR"` (balance to 2 decimal places).

**A5.** *(4 marks, debug-this-code)*
A developer wants the three largest transaction amounts:

```python
amounts = [12.0, 340.5, 8.99, 210.0]
top = amounts.sort(reverse=True)
print(top[:3])
```

This raises `TypeError: 'NoneType' object is not subscriptable`. Explain the root cause and give a corrected two-line version.

**A6.** *(4 marks, applied)*
You are given a list of transaction records, each a dict:

```python
txns = [
    {"id": "t1", "category": "groceries"},
    {"id": "t2", "category": "travel"},
    {"id": "t3", "category": "groceries"},
    # ... thousands more
]
```

Using a **comprehension** and `collections.Counter`, write code that (a) counts how many transactions fall in each `category`, and (b) returns the single most common category name.

---

## Part B — Data, pandas, viz & statistics *(NB 6–9)* — 20 marks

**B1.** *(2 marks, MCQ)*
`df` has columns `amount` and `is_fraud` (0/1). Which expression correctly selects transactions with `amount > 1000` **and** `is_fraud == 1`?

- A) `df[df.amount > 1000 and df.is_fraud == 1]`
- B) `df[(df.amount > 1000) & (df.is_fraud == 1)]`
- C) `df[df.amount > 1000 & df.is_fraud == 1]`
- D) `df.loc[df.amount > 1000 or df.is_fraud]`

**B2.** *(2 marks, MCQ)*
You want only merchants whose **total** transaction volume exceeds 1,000,000. Which SQL is correct?

- A) `... GROUP BY merchant WHERE SUM(amount) > 1000000`
- B) `... GROUP BY merchant HAVING SUM(amount) > 1000000`
- C) `... WHERE amount > 1000000 GROUP BY merchant`
- D) `SELECT SUM(amount) > 1000000 FROM transactions`

**B3.** *(4 marks, write-the-code)*
`transactions` is a DataFrame with columns `merchant`, `amount`, `is_fraud` (0/1). Write **one** pandas expression using `groupby().agg()` with **named aggregation** that produces, per merchant:

- `n_txns` — the number of transactions,
- `total_amount` — the summed amount,
- `fraud_rate` — the share of transactions flagged fraud.

**B4.** *(4 marks, short answer / statistics)*
PayFlow A/B-tests two fraud-triage models. Reviewers using model A close a mean of 30 cases/day; model B, 24. A Welch's t-test returns `p = 0.03`.

- (a) Which `scipy.stats` call produces this p-value (include the argument that makes it *Welch's*)?
- (b) State the correct interpretation of `p = 0.03` at `alpha = 0.05`.
- (c) Why should the report also include **Cohen's d**, not just the p-value?

**B5.** *(3 marks, debug-this-code)*
This line is meant to compute the mean transaction amount per merchant but raises a `TypeError`:

```python
transactions.groupby("merchant")["amount"].mean("amount")
```

Explain the mistake and give the corrected line.

**B6.** *(5 marks, applied SQL)*
PayFlow has two tables:

```
transactions(txn_id, merchant_id, amount, status)
merchants(merchant_id, name, country)
```

Write a **single SQL query** that returns, for each merchant **name** in country `'DE'`, the number of *completed* transactions (`status = 'completed'`) and their total amount — but only for merchants with **more than 100** completed transactions — ordered by total amount descending.

---

## Part C — ML, evaluation & feature engineering *(NB 8, 16, 17)* — 20 marks

**C1.** *(2 marks, MCQ)*
You are predicting whether a transaction is fraudulent **at authorisation time**. Which candidate feature is a **data leak**?

- A) transaction amount
- B) merchant country
- C) `chargeback_filed` — a dispute logged by the bank several days *after* the transaction
- D) hour of day

**C2.** *(2 marks, MCQ)*
Only 0.5% of PayFlow transactions are fraud. A model predicts "not fraud" for every transaction. Which statement is correct?

- A) ~50% accuracy; report ROC-AUC
- B) ~99.5% accuracy but it catches **zero** fraud; report **PR-AUC** (`average_precision_score`) with the fraud rate as baseline
- C) ~99.5% accuracy, which proves the model is good
- D) ~0.5% accuracy; report recall

**C3.** *(4 marks, write-the-code)*
Build a scikit-learn `Pipeline` for a churn model. Numeric columns `num_cols` must be standardised; categorical columns `cat_cols` must be one-hot encoded (ignoring categories unseen at fit time); the final estimator is `LogisticRegression`. Use `ColumnTransformer` + `Pipeline`.

**C4.** *(4 marks, short answer + code)*
At PayFlow a **missed fraud** (false negative) costs €200; a **false alarm** (false positive — blocking a legitimate payment) costs €5. You have predicted fraud probabilities `proba` and true labels `y_test`. Write code that sweeps candidate thresholds and returns the **cost-minimising** threshold, and explain in one sentence why `0.5` is the wrong default here.

**C5.** *(3 marks, debug-this-code)*
This snippet is meant to compute recall on the fraud class but is wrong in **two** ways:

```python
tn, fp, fn, tp = confusion_matrix(y_test, y_pred)
recall = tp / (tp + fp)
```

Identify both bugs and give the corrected code.

**C6.** *(5 marks, applied)*
A fraud-review team can manually check only **k = 50** of the day's 10,000 transactions. The model outputs a risk `score` per transaction.

- (a) Write two functions `precision_at_k(y_true, scores, k)` and `recall_at_k(y_true, scores, k)` (`y_true` is a 0/1 array, higher `score` = riskier).
- (b) Suppose that among the top 50 by score, **35** are truly fraud, and there are **200** frauds in total that day. Compute **precision@50** and **recall@50**.

---

## Part D — AI engineering: LLM workflows, RAG, tools/agents, MCP, document AI *(NB 10–14, 18)* — 20 marks

**D1.** *(2 marks, MCQ)*
In the Model Context Protocol (MCP), which primitive is **model-controlled** (the model decides when to invoke it)?

- A) resources
- B) prompts
- C) tools
- D) sampling

**D2.** *(2 marks, MCQ)*
In a tool-calling **agent loop**, what is the primary purpose of `max_steps`?

- A) it improves the accuracy of each individual tool call
- B) it is a fuse that stops a runaway / infinite tool-calling loop
- C) it sets the LLM sampling temperature
- D) it limits how many tools may be registered

**D3.** *(4 marks, write-the-code)*
A model sometimes returns JSON wrapped in Markdown fences (```` ```json … ``` ````) or surrounded by prose. Write `safe_json(text)` that strips Markdown fences, parses the JSON, and on failure returns `{"error": "unparseable", "raw": text}` instead of raising.

**D4.** *(4 marks, short answer)*
PayFlow uses an LLM as a **judge** to grade the quality of automatically generated KYC-rejection explanations against a rubric. Name **two documented biases** of LLM-as-judge and give **one mitigation for each**.

**D5.** *(3 marks, debug-this-code)*
This batch extractor crashes when the model returns prose instead of JSON for a single receipt, losing the whole run:

```python
records = []
for row in receipts:
    data = json.loads(llm_extract(row))
    records.append(data)
```

Rewrite the loop body so one bad response is flagged/skipped without killing the batch.

**D6.** *(5 marks, applied)*
PayFlow builds a mini-RAG over its internal policy documents. You have a list `TEXTS` of policy snippets and a `query` string.

- (a) Build a **TF-IDF** retriever and return the indices of the **top-3** most similar documents to `query` using cosine similarity (`sklearn`).
- (b) The dense embeddings used elsewhere are **L2-normalised**. Explain why, for normalised vectors, cosine similarity equals the plain dot product.

---

## Part E — Applied & production: time series, NLP, deployment, web scraping, capstone *(NB 15, 19, 20, 22, 21)* — 20 marks

**E1.** *(2 marks, MCQ)*
Why must you **not** use `train_test_split(X, y)` with its default settings on a PayFlow daily-transaction time series?

- A) it is too slow on large data
- B) the default `shuffle=True` mixes *future* rows into the training set — leakage
- C) it requires a `stratify` argument
- D) it silently drops the datetime index

**E2.** *(2 marks, MCQ)*
Before scraping a regulator's website for exchange rates, the course's data-acquisition rule says you should:

- A) scrape as fast as possible to finish before rate limits
- B) check for an official **API / data export first**, and only fall back to scraping static HTML if none exists
- C) always render the page with a headless browser
- D) ignore `robots.txt` because the page is public

**E3.** *(4 marks, write-the-code)*
`train` is a daily pandas Series with clear **weekly** seasonality and `test` is the held-out tail; `h = len(test)`. Fit a **Holt-Winters** model with additive trend and additive weekly seasonality, forecast `h` steps ahead, and compute the **MAE** against `test`. (Use `statsmodels`.)

**E4.** *(4 marks, write-the-code)*
Write a decorator `retry(attempts=3, base_delay=0.5, backoff=2.0)` that retries the wrapped function on **any exception** using **exponential backoff** (sleeping `base_delay`, then `base_delay*backoff`, …), and **re-raises** if the final attempt still fails. Preserve the wrapped function's metadata.

**E5.** *(3 marks, debug-this-code)*
This scraper line reads a merchant name from a product card:

```python
title = soup.find("span", class_="merchant").text
```

Some cards have no merchant `span`, so it raises `AttributeError: 'NoneType' object has no attribute 'text'`. Rewrite it so a missing span yields `None` instead of crashing.

**E6.** *(5 marks, applied)*
PayFlow needs the day's exchange rates from a public page at `URL`. Write code that:

- (a) uses `urllib.robotparser` to check whether your bot's user-agent `UA` is **allowed** to fetch `URL` (assume you have already read the site's `robots.txt`);
- (b) **only if allowed**, parses the page's HTML table (`BeautifulSoup`) — each `<tr>` in the table body holds two `<td>` cells, currency then rate — into a list of dicts `[{"currency": ..., "rate": ...}, ...]`, casting the rate to `float`.

---

*End of exam. Total: 100 marks.*
