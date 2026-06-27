# Exercises

> Chapter 8 of [Module 15 — Django for AI Web Apps](README.md). Do these against the running [`example-app/`](example-app/).

Each exercise has a worked solution — try first, then peek.

### 1. Add a field
Add `region` (a `ChoiceField`: north/south/east/west) to `ChurnForm`, the `Prediction` model, and the admin `list_display`. Re-run `makemigrations` + `migrate`.

<details><summary>💡 Solution</summary>

Add `region = forms.ChoiceField(choices=[("north","North"),...])` to `ChurnForm`; add `region = models.CharField(max_length=10)` to `Prediction`; add `"region"` to `PredictionAdmin.list_display`; then `python manage.py makemigrations scoring && python manage.py migrate`. (The scorer can ignore `region` or add a small per-region offset.)
</details>

### 2. A "recent predictions" page
Add a view + template at `/history/` that lists the 20 most recent predictions from the ORM.

<details><summary>💡 Solution</summary>

```python
# views.py
def history(request):
    rows = Prediction.objects.all()[:20]              # Meta.ordering handles the sort
    return render(request, "scoring/history.html", {"rows": rows})
# urls.py
path("history/", views.history, name="history"),
```
Template: loop `{% for p in rows %}` over the rows in a `<table>`.
</details>

### 3. Validate the API
Make `api_score` return HTTP 400 with a helpful message when a field is missing or non-numeric (instead of a 500).

<details><summary>💡 Solution</summary>

Wrap the parse in `try/except (KeyError, ValueError, TypeError) as exc:` and `return JsonResponse({"error": str(exc)}, status=400)`. (The shipped `api_score` already does this — read it, then make the error messages friendlier.)
</details>

### 4. Test the threshold
Write a test asserting that a month-to-month customer with high charges and many tickets scores **higher** than a two-year customer with the opposite profile.

<details><summary>💡 Solution</summary>

```python
def test_contract_matters(self):
    high = churn_probability(tenure_months=2, monthly_charges=110, support_tickets=6, contract="month-to-month")
    low  = churn_probability(tenure_months=40, monthly_charges=40, support_tickets=0, contract="two-year")
    self.assertGreater(high, low)
```
</details>

### 5. (Stretch) Swap in a real model
Train a small scikit-learn classifier on the synthetic churn data from NB 14, `joblib.dump` it, load it once in `ScoringConfig.ready()`, and call it from `churn_probability`. The views, forms, templates, and admin stay untouched — proof the seams are in the right place.
