# Serving a model

> Chapter 6 of [Module 15 — Django for AI Web Apps](README.md).

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
