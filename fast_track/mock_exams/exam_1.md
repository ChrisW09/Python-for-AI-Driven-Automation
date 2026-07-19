# Fast Track — Mock Exam 1

**Python for AI-Driven Automation & Business Data Science**
Prof. Dr. Christoph Weisser · HSBI · Summer Semester 2026

---

## Scenario: **CloudDesk**

**CloudDesk** is a SaaS customer-support platform. Businesses plug CloudDesk into their
email, chat, phone and web-form channels; CloudDesk stores every **ticket**, tracks
**CSAT** (customer-satisfaction score, an integer 1–5), records whether a ticket was
**escalated** to a human specialist, and manages customer **subscriptions** (plans:
`free`, `pro`, `enterprise`). Throughout this paper, all data and code questions are set
in the CloudDesk world.

---

## Instructions

- **Time: 120 minutes. Total: 100 marks.**
- The paper has **five parts (A–E), each worth 20 marks**; every question shows its mark value.
- **Multiple-choice questions have exactly one correct option.** Write the letter (A/B/C/D).
- For **write-the-code** questions, assume the usual imports are available unless the question
  says otherwise (`import pandas as pd`, `import numpy as np`). Code should be short and correct;
  minor syntax slips are not penalised if the intent is clear.
- For **debug** questions, state what is wrong *and* give the corrected code or line.
- Show your working on any calculation — method marks are available even if the final number is off.
- Answer **all** questions.

---

# Part A — Python foundations (NB 1–5) · 20 marks

### A1 (2 marks) — Multiple choice
CloudDesk stores a refund adjustment as a float and casts it to a whole number of euros.
What does the following print?

```python
print(int(-3.9))
```

- **A)** `-4`
- **B)** `-3`
- **C)** `-3.9`
- **D)** `ValueError`

### A2 (2 marks) — Multiple choice
An auto-resolution **rate** is held as a fraction. What string does this produce?

```python
rate = 0.234
print(f"{rate:.1%}")
```

- **A)** `"0.2%"`
- **B)** `"23.4%"`
- **C)** `"23%"`
- **D)** `"0.234%"`

### A3 (3 marks) — Short answer
Explain what the snippet below prints and *why*. In your answer, state the difference between
`is` and `==`.

```python
a = [1, 2, 3]
b = a
b.append(4)
print(len(a))
```

### A4 (4 marks) — Write the code
You are given a list `channels` holding the channel string (e.g. `"chat"`, `"phone"`, `"email"`)
of every ticket opened today. Using `collections.Counter`, write code that assigns to `channel`
and `n` the **single most common channel** and **how many tickets** it received.

### A5 (4 marks) — Debug this code
This helper is meant to start a *fresh* batch each time it is called with no batch supplied, but
it doesn't. Identify the bug, explain it in one sentence, and give the corrected function.

```python
def log_ticket(ticket_id, batch=[]):
    batch.append(ticket_id)
    return batch

print(log_ticket("T1"))   # ['T1']
print(log_ticket("T2"))   # want ['T2'], but prints ['T1', 'T2']
```

### A6 (5 marks) — Applied / OOP
Write a class `SupportTicket` that:

- is constructed with a `ticket_id` (str) and a `csat` score (int 1–5);
- keeps a **class attribute** `count` that increases by 1 every time a new ticket is created;
- has a method `is_happy()` returning `True` when `csat >= 4`, else `False`.

---

# Part B — Data, pandas, viz & statistics (NB 6–9) · 20 marks

### B1 (2 marks) — Multiple choice
CloudDesk has a DataFrame `df` with columns `csat` and `channel`. Which expression correctly
selects the rows that are **phone** tickets with a **CSAT below 3**?

- **A)** `df[df["csat"] < 3 and df["channel"] == "phone"]`
- **B)** `df[(df["csat"] < 3) & (df["channel"] == "phone")]`
- **C)** `df[df["csat"] < 3 & df["channel"] == "phone"]`
- **D)** `df[df["csat"] < 3, df["channel"] == "phone"]`

### B2 (2 marks) — Multiple choice
You draw `sns.barplot(data=df, x="channel", y="csat")`. By default, what do the vertical error
bars on each bar represent?

- **A)** ± one standard deviation
- **B)** the 95% confidence interval of the mean
- **C)** the min–max range of the data
- **D)** the interquartile range

### B3 (3 marks) — Short answer
`escalated` is a column of `0`/`1` values. Explain what
`tickets.groupby("channel")["escalated"].mean()` returns, and why the **mean of a 0/1 column
equals the escalation rate**.

### B4 (4 marks) — Write the code
Given a DataFrame `tickets` with columns `channel` and `csat`, write **one line** that returns
the **mean CSAT per channel, sorted from lowest to highest** (so the worst-performing channel
is first).

### B5 (4 marks) — Write the code (SQL)
A SQLite table `tickets(ticket_id, channel, csat, escalated)` is loaded. Write a SQL query that
returns each `channel` and its **average CSAT**, **only for channels with more than 100 tickets**,
ordered by average CSAT **descending**.

### B6 (5 marks) — Applied statistics
To compare satisfaction on two channels you run:

```python
from scipy import stats
stats.ttest_ind(chat_csat, phone_csat, equal_var=False)
# -> statistic = -2.85, pvalue = 0.004
```

- **(a)** Name this test and explain what `equal_var=False` changes. *(2)*
- **(b)** At significance level α = 0.05, what do you conclude about the two channels' mean CSAT? *(2)*
- **(c)** Give one reason a statistically significant difference might still not matter to CloudDesk. *(1)*

---

# Part C — Machine learning, evaluation & feature engineering (NB 8, 16, 17) · 20 marks

### C1 (2 marks) — Multiple choice
Which of the following is an example of **data leakage**?

- **A)** Fitting `StandardScaler` on the training set only.
- **B)** Passing `stratify=y` to `train_test_split`.
- **C)** Fitting `StandardScaler` on the **whole dataset** before splitting into train/test.
- **D)** Wrapping the scaler and model in a `Pipeline`.

### C2 (2 marks) — Multiple choice
For a binary churn classifier you write
`tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()`. In what order does `.ravel()`
return the four counts (for labels `[0, 1]`)?

- **A)** true-positive, false-positive, false-negative, true-negative
- **B)** true-negative, false-positive, false-negative, true-positive
- **C)** true-negative, false-negative, false-positive, true-positive
- **D)** precision, recall, f1, support

### C3 (3 marks) — Short answer
CloudDesk's fraud-flag dataset is ~0.5% positive. A model that predicts "not fraud" for every
ticket scores **99.5% accuracy**. Explain why this accuracy is misleading, and name **one**
metric that would expose the model's uselessness.

### C4 (4 marks) — Write the code
Using scikit-learn, build a pipeline that **standardises the features then fits logistic
regression**, train it on `X_train`, `y_train`, and store in `proba` the predicted **probability
of churn** for `X_test`.

### C5 (5 marks) — Applied: expected-value threshold
An Enterprise customer has monthly margin **m = €300** and monthly churn rate **c = 0.02**.
A retention offer costs **C_offer = €60** and, when accepted, saves the customer with
probability **s = 0.30**.

- **(a)** Compute the customer's **CLV** using `CLV = m / c`. *(1)*
- **(b)** Compute the **break-even churn probability** `p* = C_offer / (s · CLV)`, above which the
  expected value of sending the offer is positive. *(2)*
- **(c)** The model predicts this customer's churn probability at **0.06**. Should you send the
  offer? Justify with the expected-value rule (show the EV). *(2)*

### C6 (4 marks) — Debug this code
An engineer adds a "per-plan churn rate" feature, then splits and trains. Identify the
**leakage**, explain it in one sentence, and describe the corrected procedure.

```python
data["plan_churn_rate"] = data.groupby("plan")["churned"].transform("mean")
X = data.drop(columns=["churned"])
y = data["churned"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
```

---

# Part D — AI engineering: LLM workflows, RAG, tools/agents, MCP, document AI (NB 10–14, 18) · 20 marks

### D1 (2 marks) — Multiple choice
In the Model Context Protocol (MCP), which primitive is **controlled by the model** — the one the
model itself decides to call, like a POST endpoint?

- **A)** resources
- **B)** prompts
- **C)** tools
- **D)** sampling

### D2 (2 marks) — Multiple choice
For two **L2-normalised** embedding vectors, the cosine similarity is equal to:

- **A)** their Euclidean distance
- **B)** their dot product
- **C)** always exactly 1
- **D)** the sum of their elements

### D3 (3 marks) — Short answer
In an LLM extraction pipeline you parse the model's reply with `json.loads`.

- **(a)** Why must this call be wrapped in `try/except json.JSONDecodeError`? *(1.5)*
- **(b)** The record `{"order_id": "INV", "amount": 42.0}` passes your schema validation but is
  still wrong (the real id was `INV-2098`). Explain the principle *"validation checks shape,
  not truth."* *(1.5)*

### D4 (4 marks) — Write the code
Write a function `top_k(query_vec, doc_matrix, k=3)` that returns the **indices** of the `k`
rows of `doc_matrix` (a 2-D NumPy array, one document embedding per row) most similar to
`query_vec` by **cosine similarity**. Assume nothing is pre-normalised.

### D5 (3 marks) — Short answer / calculation
A retriever is evaluated on three queries. The first relevant document is returned at **rank 1**
for query 1, at **rank 3** for query 2, and is **not retrieved at all** for query 3.

- **(a)** Compute the **Mean Reciprocal Rank (MRR)**. *(2)*
- **(b)** In one sentence: what does MRR capture that a plain `retrieval@k` hit-rate does not? *(1)*

### D6 (6 marks) — Applied: LLM-as-judge
CloudDesk auto-drafts reply text, and a **second LLM grades each draft against a rubric**
(LLM-as-judge).

- **(a)** Name and briefly explain **two** known biases of an LLM judge. *(3)*
- **(b)** Give **one concrete mitigation** for each bias you named. *(2)*
- **(c)** You measure that the judge agrees with human ratings **62%** of the time. In one
  sentence, should you trust it to gate deployments? *(1)*

---

# Part E — Applied & production: time series, NLP, deployment, web scraping, capstone (NB 15, 19, 20, 21, 22) · 20 marks

### E1 (2 marks) — Multiple choice
A CloudDesk cleanup job should run **every 15 minutes, only on weekdays (Mon–Fri)**. Which cron
expression is correct? (Recall: cron's day-of-week field uses **Sunday = 0**.)

- **A)** `*/15 * * * 0-4`
- **B)** `15 * * * 1-5`
- **C)** `*/15 * * * 1-5`
- **D)** `0/15 * * * 6-7`

### E2 (2 marks) — Multiple choice
A TF-IDF + LogisticRegression sentiment model built with `TfidfVectorizer(stop_words="english")`
classifies the review **"not helpful at all"** as *positive*. The most likely reason taught in
the course is:

- **A)** LogisticRegression cannot handle text features.
- **B)** `"not"` is an English stop word, so it is dropped before the model ever sees it.
- **C)** TF-IDF vectors are not normalised, so cosine distance fails.
- **D)** The review is too short to be vectorised.

### E3 (3 marks) — Short answer
A CloudDesk `Dockerfile` runs `RUN pip install -r requirements.txt` **before** `COPY src/ ./src/`.

- **(a)** Why is putting the dependency install *above* the code copy the recommended layer
  ordering? *(2)*
- **(b)** If you edit only a source file, roughly how many layers rebuild — and how does that
  compare with bumping `requirements.txt`? *(1)*

### E4 (4 marks) — Write the code
You have the actual and forecast daily ticket volumes as NumPy arrays:

```python
import numpy as np
y_true = np.array([100, 120,  90, 110])
y_pred = np.array([110, 115, 100, 105])
```

Write code that computes and stores **`mae`** (mean absolute error) and **`mape`** (mean absolute
percentage error, as a percentage), using the formulas taught in the forecasting notebook.

### E5 (4 marks) — Debug this code
This scraper reads a priority badge from each ticket card. It crashes on some pages. State the
error and why it happens, then fix it so missing badges default to `"normal"`.

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
badge = soup.select_one(".priority")
priority = badge.get_text(strip=True)   # some cards have no .priority element
```

### E6 (5 marks) — Applied: costed decision (capstone)
CloudDesk's escalation model outputs a probability per ticket. Missing a real escalation costs
**€40** (`COST_MISS`); a false alarm costs **€20** (`COST_FALSE`). At the chosen threshold, the
test-set confusion matrix is **TN = 300, FP = 40, FN = 15, TP = 45**.

- **(a)** Write the total-cost formula in terms of FP, FN and the two unit costs, and **compute
  the total cost**. *(2)*
- **(b)** Why are "escalate nothing" and "escalate everything" usually poor baselines, and how do
  you choose the threshold instead? *(2)*
- **(c)** The executive summary reports **one headline number** from this analysis. Which number,
  and why not the model's AUC? *(1)*

---

*End of Mock Exam 1 — 100 marks.*
