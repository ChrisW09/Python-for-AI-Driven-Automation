# Sample datasets

The notebooks generate their datasets inline (so every run is reproducible), but
the three CSVs in this folder are exactly the same data dumped to disk. You can
use them whenever you want to practise `pd.read_csv` against a real file rather
than synthetic in-memory data.

| File | Rows | Schema | Used by |
|---|---|---|---|
| `support_ops.csv` | 60 | `channel`, `month`, `month_num`, `tickets_total`, `tickets_auto`, `automation_rate`, `latency_ms`, `satisfaction`, `cost_per_ticket` | NB 26 (capstone analytics) |
| `api_log.csv` | 50 | `request_id`, `model`, `segment`, `quarter`, `tokens_in`, `tokens_out`, `latency_ms` | NB 10 (pandas fundamentals) |
| `customer_feedback.csv` | 15 | `id`, `text`, `sentiment`, `topic` | NB 15 (sklearn text classification) and NB 18 (LLM workflows) |

To load any of them inside a notebook:

```python
import pandas as pd
df = pd.read_csv("data/support_ops.csv")
df.head()
```

All three files are tiny on purpose — they fit on a single screen and travel
with this repo. For real-world projects you'd typically point `pd.read_csv` at
a much bigger file (or a database connection) — the technique is identical.
