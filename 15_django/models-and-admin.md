# Models & the admin

> Chapter 4 of [Module 15 — Django for AI Web Apps](README.md).

## Models = tables, in Python

A **model** is a Python class; each attribute is a column. ChurnScope logs every prediction (`scoring/models.py`):

```python
class Prediction(models.Model):
    created_at      = models.DateTimeField(auto_now_add=True)
    tenure_months   = models.PositiveIntegerField()
    monthly_charges = models.FloatField()
    support_tickets = models.PositiveIntegerField()
    contract        = models.CharField(max_length=20)
    probability     = models.FloatField()
    will_churn      = models.BooleanField()
```

You never write `CREATE TABLE`. Instead:

```bash
python manage.py makemigrations   # writes scoring/migrations/0001_initial.py
python manage.py migrate          # applies it to the database
```

**Migrations** are versioned, reviewable schema changes — like Git commits for your database. Change a model, `makemigrations`, `migrate`; Django figures out the SQL and keeps every environment in sync.

## The ORM = queries without SQL

The view logs a prediction with one line:

```python
Prediction.objects.create(tenure_months=3, monthly_charges=95, ...,
                          probability=0.81, will_churn=True)
```

…and reading is just as fluent:

```python
Prediction.objects.count()                              # how many so far
Prediction.objects.filter(will_churn=True)              # only churners
Prediction.objects.filter(contract="month-to-month").order_by("-created_at")[:10]
```

Each call returns lazily-evaluated objects and compiles to parameterised SQL (so it's injection-safe by construction).

## The admin — a back-office for free

Register the model (`scoring/admin.py`) and Django builds a full CRUD dashboard:

```python
@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ("created_at", "contract", "probability", "will_churn")
    list_filter  = ("contract", "will_churn")
```

Create a login (`python manage.py createsuperuser`), visit `/admin/`, and a non-engineer can search, filter, and inspect every prediction — no extra code. **This is Django's killer feature**: the back-office that would take days in Flask is one file here.
