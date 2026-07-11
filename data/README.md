# Sample datasets

Two kinds of CSV live here:

1. **Synthetic dumps** — the notebooks generate their data inline (so every run is
   reproducible and 100% offline). These three files are the *same* data dumped to
   disk, so you can practise `pd.read_csv` against a real file instead of building
   one in memory.
2. **Small real datasets** — permissively licensed, bundled so the optional
   "📊 try it on real data" sections in the notebooks also run offline.

## Synthetic dumps

| File | Rows | Schema | Used by |
|---|---|---|---|
| `support_ops.csv` | 60 | `channel`, `month`, `month_num`, `tickets_total`, `tickets_auto`, `automation_rate`, `latency_ms`, `satisfaction`, `cost_per_ticket` | NB 47 (capstone analytics) |
| `api_log.csv` | 50 | `request_id`, `model`, `segment`, `quarter`, `tokens_in`, `tokens_out`, `latency_ms` | NB 7 (pandas fundamentals) |
| `customer_feedback.csv` | 15 | `id`, `text`, `sentiment`, `topic` | sample mirroring the inline data in NB 17 & NB 28 |

## Real datasets (permissively licensed)

| File | Rows | What it is | Used by | Licence |
|---|---|---|---|---|
| `penguins.csv` | 344 | Palmer Penguins — species, island, bill/flipper measurements, body mass, sex (includes real missing values) | NB 9 (visualization) | CC0 |
| `bike_sharing_daily.csv` | 731 | UCI Bike Sharing — daily rental counts (2011–2012) with weather + calendar features | NB 26 (demand forecasting) | CC BY 4.0 |

**Attribution (required by CC BY 4.0).** `bike_sharing_daily.csv` is the `day.csv`
file from the **UCI Bike Sharing Dataset** by Hadi Fanaee-T & João Gama (2013) —
<https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset>. Numeric weather
columns are normalised as documented there (`temp` ÷ 41 °C, `atemp` ÷ 50 °C,
`hum` ÷ 100, `windspeed` ÷ 67). **Palmer Penguins** (Horst, Hill & Gorman) is
released CC0 via the Palmer Station LTER.

## Loading

```python
import pandas as pd
df = pd.read_csv("data/penguins.csv")   # or any file above
df.head()
```

All files are small on purpose — they fit on a screen and travel with this repo.
For real-world projects you'd point `pd.read_csv` at a much bigger file (or a
database connection); the technique is identical. See the course README's
**[Datasets → Going further](../README.md#-datasets)** section for more real
datasets you can load in one line.
