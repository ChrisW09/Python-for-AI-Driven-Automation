# Serving a model

> Chapter 7 of [Module 15 — Django for AI Web Apps](README.md).

The whole point: get a prediction in front of a user. Two surfaces ship with ChurnScope — an HTML form and a JSON API.

## The scorer

`scoring/scorer.py` is a transparent stand-in for a trained model — pure Python, so the app runs with only Django:

```python
def churn_probability(*, tenure_months, monthly_charges, support_tickets, contract):
    z = (-0.5
         + 1.4 * CONTRACT_RISK.get(contract, 0.0)   # month-to-month is risky
         - 0.05 * tenure_months                      # loyalty lowers risk
         + 0.015 * monthly_charges                   # pricier plans churn more
         + 0.25  * support_tickets)                  # friction churns
    return 1 / (1 + math.exp(-z))                    # logistic squash → 0..1
```

**Swap in a real model** by loading a pickled scikit-learn estimator (or calling an LLM via `llm_providers.py`) and returning its probability — the rest of the app doesn't change.

## A JSON API

For programmatic callers, `api_score` reads JSON and returns JSON (`scoring/views.py`):

```python
@csrf_exempt                       # stateless API; use token auth in production
@require_POST
def api_score(request):
    data = json.loads(request.body or "{}")
    p = churn_probability(tenure_months=int(data["tenure_months"]), ...)
    return JsonResponse({"probability": round(p, 4), "will_churn": p >= THRESHOLD})
```

```bash
curl -X POST localhost:8000/api/score -H "Content-Type: application/json" \
     -d '{"tenure_months":3,"monthly_charges":95,"support_tickets":4,"contract":"month-to-month"}'
# {"probability": 0.83, "will_churn": true}
```

> For anything beyond a teaching endpoint, reach for **Django REST Framework** or **Django Ninja** (FastAPI-style, with the Pydantic validation and auto-docs you met in Module 7) instead of hand-rolling JSON views.

## Where to load the model — *not* per request

Loading a model file (or warming an LLM client) on **every** request is the classic mistake — it's slow and wasteful. Load it **once at startup** instead. Django's hook is the app's `ready()` (`scoring/apps.py`):

```python
class ScoringConfig(AppConfig):
    name = "scoring"
    def ready(self):
        # load the pickle / warm the client ONCE here, stash it on the module,
        # and have churn_probability() reuse it. (ChurnScope's scorer is pure
        # Python, so there's nothing to load — but this is the seam.)
        ...
```

Rule of thumb: **keep heavy, blocking work off the request path.** Load at boot; for slow models, push scoring to a background worker (Celery/RQ) and return a job id — the same "don't block the user" discipline from Module 11.

## Swapping in a real model

That `ready()` seam is exactly what [Exercise 5](exercises.md) asks you to fill. Here is the full pattern: train offline, ship the artifact, load once, keep the signature. (The shipped app stays pure Python on purpose — `pip install scikit-learn joblib` only when you make this swap.)

**Step 1 — train and dump, outside Django.** Training is a batch job, not web code:

```python
# train_model.py — run once, offline (synthetic churn data: NB 14)
import joblib
from sklearn.linear_model import LogisticRegression

# X columns: contract_risk, tenure_months, monthly_charges, support_tickets
model = LogisticRegression().fit(X, y)
joblib.dump(model, "scoring/churn_model.joblib")
```

**Step 2 — load once at startup.** Fill a module-level cache from `ready()` (`scoring/apps.py`):

```python
class ScoringConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "scoring"

    def ready(self):
        from . import scorer          # import inside ready(): apps are loaded now
        scorer.load_model()
```

```python
# scoring/scorer.py
from pathlib import Path
import joblib

_model = None                         # module-level cache, filled once at boot

def load_model():
    global _model
    _model = joblib.load(Path(__file__).with_name("churn_model.joblib"))
```

Why not load in the view? The view runs on **every** request — `joblib.load` there means disk I/O plus unpickling on the hot path, thousands of times, for a file that only changes at deploy time. `ready()` runs once per process: pay the cost at boot, and every request finds a warm model.

**Step 3 — keep the signature.** `churn_probability()` changes inside, not outside:

```python
def churn_probability(*, tenure_months, monthly_charges, support_tickets, contract):
    row = [[CONTRACT_RISK.get(contract, 0.0), float(tenure_months),
            float(monthly_charges), float(support_tickets)]]
    return float(_model.predict_proba(row)[0, 1])    # column 1 = P(churn)
```

Same name, same keyword arguments, same 0–1 return — so `scoring/views.py`, the form, the templates, and the admin don't change at all. That's the seam this module keeps advertising: the model is a function boundary, and everything else talks to the boundary.

> ⚠️ `ready()` runs for **every** `manage.py` command — `migrate`, `makemigrations`, `test`, all of them. A hefty pickle makes every command slow. If that bites, load lazily instead: have `churn_probability()` start with `if _model is None: load_model()`.

## Keeping the request path fast

A useful test for any line in a view: *does the user need this to finish before they can see a response?*

- **In the request:** validate input → predict → log the `Prediction`. That's all `index` and `api_score` do — milliseconds each.
- **Not in the request:** training or retraining, batch-scoring thousands of customers, retries against a flaky external API. Those take seconds to hours; a browser (and your worker pool) won't wait.

Long work goes to a queue or a schedule — cron, Celery/RQ, or the scheduling patterns from Module 11 ([NB 40](../11_production/40_scheduling_orchestration.ipynb)). The view's job is to *accept* work and answer fast, not to *do* the work.

## Versioning the model file

Once the model is a file, "which model produced this score?" becomes a real question. Answer it in two lines:

```python
# scoring/scorer.py — version string lives next to the artifact it describes
MODEL_VERSION = "2026-07-logreg-v1"
```

Add `model_version = models.CharField(max_length=40)` to `Prediction`, pass `MODEL_VERSION` wherever the views create a row, then `makemigrations` + `migrate` — the same one-command schema evolution from the [models chapter](models-and-admin.md). This is exactly what the `Prediction` audit log is for: when a score looks wrong next quarter, the row tells you which model made it.
