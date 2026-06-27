# ChurnScope — Django example app

A minimal but complete Django project: a churn-scoring **web form**, a **JSON API**,
an **admin dashboard**, and the **ORM** logging every prediction. The only
dependency is Django (the scorer is plain Python).

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver          # http://127.0.0.1:8000/
python manage.py createsuperuser    # then visit /admin/
python manage.py test               # run the tests
```

API:

```bash
curl -X POST http://127.0.0.1:8000/api/score \
     -H "Content-Type: application/json" \
     -d '{"tenure_months": 3, "monthly_charges": 95, "support_tickets": 4, "contract": "month-to-month"}'
```

See the chapters in [`../`](..) for the full walkthrough.
