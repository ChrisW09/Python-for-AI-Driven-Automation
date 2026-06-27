# Testing & deployment

> Chapter 7 of [Module 15 — Django for AI Web Apps](README.md).

## Testing with the test client

Django ships a test runner and a fake browser (the **test client**) — no server needed. ChurnScope's `scoring/tests.py`:

```python
class ViewTests(TestCase):
    def test_form_post_logs_prediction(self):
        resp = self.client.post(reverse("scoring:index"), {
            "tenure_months": 3, "monthly_charges": 95,
            "support_tickets": 4, "contract": "month-to-month"})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Prediction.objects.count(), 1)   # it logged the row
```

```bash
python manage.py test          # spins up a throwaway DB, runs everything
```

Each test runs against a fresh, in-memory database that's torn down afterwards — fast and isolated, the same discipline as the notebook checkpoints.

## The three production settings you MUST change

The dev defaults are deliberately unsafe. Before you deploy:

| Setting | Dev | Production |
|---|---|---|
| `DEBUG` | `True` | **`False`** (never leak tracebacks) |
| `SECRET_KEY` | a dev fallback | from an **environment variable**, never committed |
| `ALLOWED_HOSTS` | `["*"]` | your real domain(s) |

ChurnScope already reads all three from the environment (`churnscope/settings.py`), so production is a matter of *setting* them:

```bash
export DJANGO_DEBUG=0
export DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(50))')"
export DJANGO_ALLOWED_HOSTS="churnscope.example.com"
```

## Serving for real

The dev server (`runserver`) is **not** for production. Run Django under a WSGI server and let Module 12's Nginx sit in front:

```bash
pip install gunicorn
python manage.py collectstatic --noinput        # gather static files
gunicorn churnscope.wsgi:application --bind 0.0.0.0:8000
```

## Hand-off to Module 12

This is exactly the app shape **[Module 12 — CI/CD & Deployment](../12_cicd/)** knows how to ship:

1. **Dockerise** it (a `Dockerfile` running `gunicorn churnscope.wsgi`).
2. **Compose** it with Postgres + Nginx.
3. **GitHub Actions** builds and deploys on every push.
4. **HTTPS** via Let's Encrypt.

Same pipeline, a Django image instead of a FastAPI one. You've now seen both ends — a thin API service and a full batteries-included app — through the *same* deployment door.
