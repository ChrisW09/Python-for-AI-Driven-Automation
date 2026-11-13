# Exercises

> Chapter 9 of [Module 17 — Django for AI Web Apps](README.md). Do these against the running [`example-app/`](example-app/).

Each exercise has a worked solution — try first, then peek.

### 1. Add a field
Add `region` (a `ChoiceField`: north/south/east/west) to `ChurnForm`, the `Prediction` model, and the admin `list_display`. Re-run `makemigrations` + `migrate`.

<details><summary>💡 Solution</summary>

Add `region = forms.ChoiceField(choices=[("north","North"),...])` to `ChurnForm`; add `region = models.CharField(max_length=10)` to `Prediction`; add `"region"` to `PredictionAdmin.list_display`; then `python manage.py makemigrations scoring && python manage.py migrate`. (The scorer can ignore `region` or add a small per-region offset.)
</details>

### 2. Filter the history
The shipped `/history/` page shows every prediction. Add a `?contract=` filter: `/history/?contract=month-to-month` should show only those rows, pagination intact, and the page should offer the three contract types as links.

<details><summary>💡 Solution</summary>

```python
# views.py — filter BEFORE paginating, so page counts stay correct
@login_required
def history(request):
    rows = Prediction.objects.all()
    contract = request.GET.get("contract")
    if contract:
        rows = rows.filter(contract=contract)
    paginator = Paginator(rows, per_page=10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "scoring/history.html",
                  {"page_obj": page_obj, "contract": contract})
```
Template: three links like `<a href="?contract=month-to-month">month-to-month</a>` (plus one plain `?` link for "all"), and carry the filter through the pager links: `?page={{ page_obj.next_page_number }}&contract={{ contract }}`. Querysets are lazy, so stacking `.filter()` before the paginator costs one SQL query either way.
</details>

### 3. Validate the API
Make `api_score` return HTTP 400 with a helpful message when a field is missing, non-numeric **or out of range** (a negative tenure, an unknown contract) — instead of a 500, and without logging the bad row.

<details><summary>💡 Solution</summary>

A `try/except (KeyError, ValueError, TypeError)` around hand-written `int(...)` casts only covers the first two: `int("-3")` parses fine, and the negative value then crashes the `PositiveIntegerField` insert. Bind the payload to the form you already have instead — `form = ChurnForm(payload)`, and on `not form.is_valid()` return `JsonResponse({"error": "invalid request", "fields": {name: list(errs) for name, errs in form.errors.items()}}, status=400)`. (The shipped `api_score` already does this — read it and its `ApiValidationTests`, then make the messages friendlier, e.g. add the allowed range to each one.)
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
Train a small scikit-learn classifier on the synthetic churn data from NB 17 (`05_machine_learning/17_sklearn_basics.ipynb`), `joblib.dump` it, load it once in `ScoringConfig.ready()`, and call it from `churn_probability`. The views, forms, templates, and admin stay untouched — proof the seams are in the right place. (Stuck? [Chapter 7](serving-a-model.md) now walks the full pattern — attempt it first, then compare.)
