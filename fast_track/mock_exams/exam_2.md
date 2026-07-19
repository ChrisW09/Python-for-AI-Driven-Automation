# Fast Track — Mock Exam 2

**Python for AI-Driven Automation & Business Data Science**
Prof. Dr. Christoph Weisser · HSBI · Summer Semester 2026

---

## Scenario: ShopSphere

Throughout this exam you work as a data/AI engineer at **ShopSphere**, a mid-sized online retailer. ShopSphere's systems produce data about **orders, products, shopping carts, returns, and customer reviews**. Every question is framed in this world — you will analyse return rates, forecast SKU demand, mine product-review sentiment, scrape a competitor's catalogue, and ship a retention model.

## Instructions

- **Time:** 120 minutes. **Total: 100 marks** (5 parts × 20 marks).
- Answer **all** questions. Marks are shown in brackets, e.g. **[4]**.
- For **multiple-choice** questions, write the letter of the *single* best option.
- For **write-the-code** questions, small, self-contained snippets are expected — assume the usual imports (`pandas as pd`, `numpy as np`, etc.) are already done unless the question says otherwise.
- For **debug** questions, state *what* is wrong and give the corrected line(s).
- Modern pandas / scikit-learn idioms are expected. Partial credit is available.

| Part | Topic | Marks |
|------|-------|-------|
| A | Python foundations | 20 |
| B | Data, pandas, visualization & statistics | 20 |
| C | Machine learning, evaluation & feature engineering | 20 |
| D | AI engineering: LLM workflows, RAG, tools/agents, MCP, document AI | 20 |
| E | Applied & production: time series, NLP, deployment, web scraping | 20 |

---

## Part A — Python foundations (NB 1–5) · 20 marks

**A1 (MCQ) [2].** ShopSphere stores a raw discount adjustment `-3.9`. A junior dev writes `int(-3.9)` to "round it down". What does Python actually return?

- A) `-4`
- B) `-3`
- C) `3`
- D) `ValueError`

**A2 (MCQ) [2].** Consider this cart helper:

```python
def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart
```

A colleague calls `add_to_cart("mug")` and then, separately, `add_to_cart("pen")`. What does the **second** call return?

- A) `['pen']`
- B) `['mug', 'pen']`
- C) `['mug']`
- D) `[]`

**A3 (Short answer) [3].** An order total is stored as `total = 1234.5` and a product's return rate as `return_rate = 0.0873`. Write two f-strings that produce **exactly**:

```
€1,234.50
8.7%
```

**A4 (Write the code) [4].** Today's orders each carry a product category:

```python
categories = ["mug", "pen", "mug", "lamp", "mug", "pen"]
```

Using `collections.Counter`, build a count of orders per category and print the single **most-ordered** category name. (Any correct approach earns full marks.)

**A5 (Debug) [4].** This function should sum the prices in a cart but always returns the last price. State the bug and give the fix.

```python
def cart_total(prices):
    total = 0
    for p in prices:
        total = p
    return total
```

**A6 (Write the code) [5].** Write a class `ShoppingCart` with:

- a **class attribute** `TAX_RATE = 0.19`;
- an `__init__` that stores an **empty** `items` list (do **not** use a mutable default argument);
- `add_item(self, name, price, qty=1)` that appends a dict `{"name": ..., "price": ..., "qty": ...}` to `items`;
- `subtotal(self)` returning the sum of `price * qty` over all items;
- `total(self)` returning the subtotal including tax (`subtotal × (1 + TAX_RATE)`).

---

## Part B — Data, pandas, visualization & statistics (NB 6–9) · 20 marks

You have a DataFrame `orders` with columns `order_id`, `category`, `total` (float, €), and `returned` (a 0/1 integer flag).

**B1 (MCQ) [2].** Which expression correctly selects **returned** orders whose `total` exceeds €100?

- A) `orders[orders.returned and orders.total > 100]`
- B) `orders[(orders.returned == 1) & (orders.total > 100)]`
- C) `orders[orders.returned == 1 & orders.total > 100]`
- D) `orders[orders.returned == 1, orders.total > 100]`

**B2 (MCQ) [2].** In SQL, which clause filters **groups after aggregation** (e.g. keep only categories whose total revenue exceeds a threshold)?

- A) `WHERE`
- B) `HAVING`
- C) `GROUP BY`
- D) `ORDER BY`

**B3 (Short answer) [3].** Write a single pandas expression that returns the **mean return rate per category** (the fraction of returned orders in each category), sorted from highest to lowest.

**B4 (Write the code) [4].** ShopSphere ran an A/B test on delivery: array `express` and array `standard` hold customer satisfaction scores for the two shipping options (unequal variances, unequal sizes). Using `scipy.stats`, write code that runs the appropriate two-sample test and prints the **p-value**. Name the test you used.

**B5 (Write the code) [4].** The `orders` table also lives in a SQL database. Write a SQL query that returns, **per category**, the total revenue as `revenue`, keeping only categories whose revenue exceeds **€10,000**, ordered by `revenue` descending.

**B6 (Debug) [3].** A colleague's query errors out. State what is wrong and fix it.

```sql
SELECT category, SUM(total) AS revenue
FROM orders
WHERE SUM(total) > 10000
GROUP BY category;
```

**B7 (Applied scenario / MCQ) [2].** The delivery A/B test in B4 returns `p = 0.03`. Which interpretation is correct?

- A) There is a 3% chance the two means are equal.
- B) At α = 0.05 there is evidence the means differ, but the p-value alone says nothing about how *large* the difference is.
- C) The difference is large and business-important.
- D) There is a 97% chance the result is real.

---

## Part C — Machine learning, evaluation & feature engineering (NB 8, 16, 17) · 20 marks

ShopSphere is building a model that flags orders likely to be **returned**.

**C1 (MCQ) [2].** You run `tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()`. In which order does scikit-learn return the four values?

- A) `tp, fp, fn, tn`
- B) `tn, fp, fn, tp`
- C) `tp, tn, fp, fn`
- D) `tn, fn, fp, tp`

**C2 (MCQ) [2].** A teammate fits a `StandardScaler` on the **whole** dataset *before* calling `train_test_split`. Why is this a problem?

- A) Scaling is never needed for tree models, so it wastes time.
- B) Test-set statistics leak into the training data, so the reported score is optimistically inflated.
- C) It changes the class balance of the split.
- D) `StandardScaler` cannot be fitted twice.

**C3 (Short answer) [3].** The return-flagging model produces this confusion matrix on the test set: **TP = 40, FP = 10, FN = 20, TN = 930**. Compute the **precision** and **recall** (show the formulas and the numbers).

**C4 (Write the code) [4].** Using scikit-learn, write a **leakage-free** classification workflow on a feature matrix `X` and label `y`: split into train/test with a **stratified** 20% test set, build a `Pipeline` of `StandardScaler` → `LogisticRegression`, fit on the training data, and produce predictions for the test set.

**C5 (Applied scenario) [5].** ShopSphere can send a €8 retention offer to customers at risk of churning. A customer has estimated **CLV = €400**; the offer's **save rate** (fraction of would-be churners it rescues) is **s = 0.25**; the **offer cost** is **C = €8**.

- (a) **[2]** Compute the **break-even churn probability** `p*` above which the offer has positive expected value, using `p* = C / (s · CLV)`.
- (b) **[2]** The model predicts this customer's churn probability as `p = 0.10`. Compute the **expected value** of sending the offer, `EV = p · s · CLV − C`.
- (c) **[1]** Based on (a) and (b), should ShopSphere send this customer the offer? Justify in one sentence.

**C6 (Debug) [4].** This code is meant to compute precision but reports the wrong number. State the bug and give the corrected line.

```python
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
precision = tp / (tp + fn)
```

---

## Part D — AI engineering: LLM workflows, RAG, tools/agents, MCP, document AI (NB 10–14, 18) · 20 marks

ShopSphere is automating product-review triage and a returns-policy assistant.

**D1 (MCQ) [2].** You are building a classifier that tags each review as `positive` / `neutral` / `negative` and needs **reproducible** output. What temperature should you use?

- A) `1.0`
- B) `0.7`
- C) `0.0`
- D) Temperature has no effect on classification.

**D2 (MCQ) [2].** Which three items are the **primitives** of the Model Context Protocol (MCP)?

- A) tools, resources, prompts
- B) host, client, server
- C) GET, POST, PUT
- D) faithfulness, relevancy, recall

**D3 (Short answer) [3].** In ShopSphere's review-retrieval system you compare embedding vectors with **cosine similarity**. (a) Why should the vectors be **L2-normalized** before comparison? (b) For unit-length vectors, what simpler operation does cosine similarity reduce to?

**D4 (Write the code) [4].** Write two small functions using NumPy: `cosine(a, b)` returning the cosine similarity of two 1-D arrays, and `top_k(q, docs, k)` returning the **indices** of the `k` documents in matrix `docs` (rows = documents) most similar to query vector `q`.

**D5 (Write the code) [3].** Write the **JSON-Schema tool definition** (a Python dict) that describes a tool `get_return_rate` to an LLM. It takes one **required** string argument `category` and returns that category's return rate. Include `name`, `description`, and `parameters`.

**D6 (Debug) [3].** This review classifier crashes intermittently in production. Explain why and fix it.

```python
def classify(review):
    r = llm.chat(messages=[{"role": "user", "content": review}])
    return json.loads(r["text"])
```

**D7 (Applied scenario) [3].** ShopSphere's receipt extractor pulls `order_id = "ORD"` from a document whose true order id is `"ORD-5521"`. The value **passes** the schema validator (it is a non-empty string) but is clearly wrong. (a) Explain why validation passed. (b) What is the one thing you need to *catch* this kind of error, and what is it called in the course?

---

## Part E — Applied & production: time series, NLP, deployment, web scraping, capstone (NB 15, 19, 20, 22, 21) · 20 marks

**E1 (MCQ) [2].** You are forecasting weekly demand for a SKU. Why is a **random** `train_test_split(shuffle=True)` the wrong choice here?

- A) It is computationally slower than a time-ordered split.
- B) Future dates leak into the training set, so the error looks great in testing then collapses in production.
- C) Random splits always need more data.
- D) It only affects multiplicative seasonality.

**E2 (MCQ) [2].** In a `Dockerfile`, how do you keep the (slow) `pip install` step **cached** when only your application code changes?

- A) `COPY . .` first, then `RUN pip install -r requirements.txt`.
- B) `COPY requirements.txt` and `RUN pip install` **before** `COPY src/ ./src/`.
- C) Use `FROM python:latest`.
- D) Put the `CMD` instruction first.

**E3 (Short answer) [3].** For three days, actual SKU demand was `[100, 200, 50]` and your forecast was `[110, 180, 60]`. Compute the **MAE** and the **MAPE** (%). Show your working.

**E4 (Write the code) [4].** ShopSphere has a Python list `reviews` of product-review strings. Write code that groups them into **3 topics** using TF-IDF + KMeans: build TF-IDF features (drop English stop-words), fit `KMeans` with 3 clusters (seeded, `n_init=10`), and produce the per-review cluster labels.

**E5 (Write the code) [4].** You are scraping a competitor's product listing. Each product is an `<li class="product">` element containing an `<h2 class="name">` and a `<span class="price">`. Given `html` (a string), use BeautifulSoup to build a list of `(name, price)` tuples. (Assume you have already confirmed `robots.txt` allows this path.)

**E6 (Debug) [3].** The scraper above crashes with `AttributeError: 'NoneType' object has no attribute 'text'` on some products. Explain why and rewrite the extraction so a missing field yields `None` instead of a crash.

```python
name = li.find("h2", class_="name").text
```

**E7 (Applied scenario) [2].** Before running **KMeans** on customers' **RFM** features (Recency, Frequency, Monetary), what single preprocessing step is essential, and what goes wrong if you skip it?

---

*End of Mock Exam 2 — 100 marks. Worked solutions are provided separately (`exam_2_solutions.pdf`).*
