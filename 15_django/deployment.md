# Testing & deployment

> Chapter 8 of [Module 15 — Django for AI Web Apps](README.md).

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

## Containerising ChurnScope

The example app ships a real **[`Dockerfile`](example-app/Dockerfile)** (plus a [`.dockerignore`](example-app/.dockerignore)). It follows the exact house pattern from [Module 12's backend Dockerfile](../12_cicd/example-app/backend/Dockerfile) — `python:3.12-slim`, requirements layer before code, non-root user, a stdlib `HEALTHCHECK` — with gunicorn instead of uvicorn. Build and run it:

```bash
cd 15_django/example-app
docker build -t churnscope .
docker run -p 8000:8000 \
    -e DJANGO_SECRET_KEY="change-me" \
    -e DJANGO_DEBUG=0 \
    -e DJANGO_ALLOWED_HOSTS=localhost \
    churnscope
```

Open <http://localhost:8000/> and score a customer — same app, now in a box. Three things in the image deserve a pause:

**Migrations at container start.** The `CMD` is `sh -c "python manage.py migrate --noinput && exec gunicorn churnscope.wsgi --bind 0.0.0.0:8000"` — migrate, then serve, so the container sets itself up. Fine for a single-container SQLite demo; in real life run migrations as a separate **release step** (a one-off `docker run … python manage.py migrate`, or a CI job) — otherwise several replicas race to migrate the same database.

**Static files.** The demo serves nothing collected beyond the admin's assets, so the image skips `collectstatic`. The standard production answer: run `python manage.py collectstatic --noinput` at build time and add [WhiteNoise](https://whitenoise.readthedocs.io/) middleware so gunicorn serves the collected files efficiently — or let Module 12's Nginx serve `staticfiles/` directly.

**SQLite in a container is ephemeral.** The database lives in the container's writable layer, so `docker rm` deletes every logged prediction (Module 12, [Docker §8](../12_cicd/docker.md)). Bind-mount the file to keep it:

```bash
touch db.sqlite3       # must exist before Docker can mount it
docker run -p 8000:8000 -v "$PWD/db.sqlite3:/app/db.sqlite3" churnscope
```

For anything real, swap the `DATABASES` dict for Postgres in its own container — which is exactly what Module 12's compose file does.

## Hand-off to Module 12

The image above drops straight into **[Module 12 — CI/CD & Deployment](../12_cicd/)**:

1. **Dockerise** it — done: the `Dockerfile` above.
2. **[Compose](../12_cicd/docker-compose.md)** it with Postgres + Nginx.
3. **[GitHub Actions](../12_cicd/github-actions.md)** builds and deploys on every push.
4. **[HTTPS](../12_cicd/https.md)** via Let's Encrypt.

Same pipeline, a Django image instead of a FastAPI one. You've now seen both ends — a thin API service and a full batteries-included app — through the *same* deployment door.
