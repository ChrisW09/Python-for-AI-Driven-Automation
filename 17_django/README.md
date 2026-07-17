# 17 · Optional: Django for AI Web Apps

> 🧭  [◀ Business AI](../16_business_ai/)  ·  [🏠 Course home](../README.md)  ·  [Compound AI Evaluation ▶](../18_compound_ai_evaluation/)

So far you've *built* models and *shipped* them as scripts, notebooks, and small FastAPI services (Modules 9, 13, 14). This optional module adds the other end of the spectrum: **Django**, the "batteries-included" web framework — the fastest way to wrap a model in a real, multi-page web application with a database, an admin dashboard, forms, and authentication, with almost no glue code.

> 📎 **Optional module — a mini-book, two lab notebooks, and an example app.** Django is a *project*, not a sequence of notebook cells, so its core is a short **mini-book** (the chapters below) plus a **runnable example app** you read, run, and extend. Two hands-on **lab notebooks** (below) complement it — they boot *real* Django inside a Jupyter kernel, so you practise the ORM, views, forms, auth, and model-serving cell by cell. Everything runs **offline**; `pip install django` is the only dependency you need (gunicorn joins for the Docker chapter).

Our running example is **ChurnScope** — the churn-scoring tool you prototyped in Module 9 (NB 33–36) — rebuilt as a proper Django app: a form-driven UI, a JSON API, an admin dashboard, and the ORM logging every prediction to a database.

---

## What you'll learn

By the end of this module you will be able to:

- Explain **when to reach for Django** versus Flask / FastAPI — and what "batteries included" actually buys you.
- Describe Django's **MTV** request cycle (URL → view → template) and the **project vs app** split.
- Define data with **models**, evolve the schema with **migrations**, and query it through the **ORM** — then browse and edit it for free in the **admin site**.
- Route URLs, write **views**, render **templates**, and validate user input with **forms**.
- Protect pages with Django's built-in **authentication** (`@login_required`, login/logout views) and paginate query results.
- **Serve a model** from a view and a JSON API — and keep the heavy lifting *off* the request hot path.
- **Test** with Django's test client and harden settings for **production**, plugging straight into the Docker/CI pipeline from Module 14.

---

## Table of contents (read in this order)

| # | Chapter | What it covers |
|---|---|---|
| 1 | **README** (this file) | The big picture, vocabulary, and how to run the example app |
| 2 | [Why Django](why-django.md) | Django vs Flask/FastAPI; what "batteries included" means; when to pick which |
| 3 | [Project anatomy](project-anatomy.md) | `project` vs `app`, `manage.py`, `settings.py`, `urls.py`, and the MTV request cycle |
| 4 | [Models & admin](models-and-admin.md) | Models, migrations, the ORM, and the free admin dashboard |
| 5 | [Views, templates & forms](views-templates-forms.md) | URL routing, views, templates, and validated forms |
| 6 | [Auth & the history page](auth-and-history.md) | Built-in authentication, `@login_required`, pagination, POST logout |
| 7 | [Serving a model](serving-a-model.md) | Calling the scorer from a view + a JSON API; loading models at startup; versioning |
| 8 | [Testing & deployment](deployment.md) | The test client, production settings, gunicorn, Docker, and the link to Module 14 |
| 9 | [Exercises](exercises.md) | Extend ChurnScope — with worked solutions |

---

## The example app — ChurnScope

A complete, minimal Django project lives in [`example-app/`](example-app/). It has:

- a **form page** (`/`) where you enter a customer's details and get a churn probability,
- a **JSON API** (`POST /api/score`) for programmatic scoring,
- a login-protected **history page** (`/history/`) — the paginated prediction log,
- an **admin dashboard** (`/admin/`) that lists every prediction the ORM logged,
- a transparent **scorer** (`scoring/scorer.py`) — a stand-in for a trained model, so running the app needs nothing beyond Django.

### Run it (≈2 minutes)

```bash
cd 17_django/example-app
python -m venv .venv && source .venv/bin/activate   # optional but recommended
pip install -r requirements.txt                     # Django (+ gunicorn for the Docker chapter)
python manage.py migrate                            # create the SQLite database
python manage.py runserver                          # http://127.0.0.1:8000/
```

Open <http://127.0.0.1:8000/>, score a customer, then create an admin login to inspect the log:

```bash
python manage.py createsuperuser                    # then visit /admin/ — the same login opens /history/
```

Score from the command line instead:

```bash
curl -X POST http://127.0.0.1:8000/api/score \
     -H "Content-Type: application/json" \
     -d '{"tenure_months": 3, "monthly_charges": 95, "support_tickets": 4, "contract": "month-to-month"}'
```

Run the tests:

```bash
python manage.py test
```

---

## Hands-on lab notebooks

Prefer to *practise* cell by cell before reading the example app's files? Two lab notebooks boot **real Django inside the notebook kernel** — no `manage.py`, no server process — so every concept is runnable and editable in place. They run 100% offline (`pip install django`) and mirror the ChurnScope model and fields, so the files under [`example-app/`](example-app/) feel familiar afterwards.

| Notebook | ⏱ Time | What you build |
|---|---|---|
| [`lab01_django_in_a_notebook.ipynb`](lab01_django_in_a_notebook.ipynb) | ~60 min | `settings.configure()` + `django.setup()`, the `Prediction` model on real SQLite, the ORM (lazy QuerySets, aggregates, the N+1 trap shown with `connection.queries`), string templates, a URLconf + views exercised through the test `Client`, and validated forms |
| [`lab02_serving_a_model_with_auth.ipynb`](lab02_serving_a_model_with_auth.ipynb) | ~60 min | Train a churn model, serve it behind a `POST /api/score/` JSON endpoint and an HTML form, log every prediction via the ORM, protect a `/history/` page with `@login_required`, test it through the client, and walk the production `Dockerfile` into Module 14 |

Start with lab 1. Each embeds ✋ checkpoints, 🧪 practice exercises, and a 🎁 mini-project, in the same style as the numbered course lessons.

---

## Prerequisites

- **Module 1** (functions, classes), **Module 9** (you built ChurnScope as a POC), and a terminal.
- Helpful: **Module 14** (Docker/CI) — the deployment chapter hands off to it.

## Where this fits

Flask/FastAPI (Modules 9 & 12) are perfect for a thin model-serving API. Reach for **Django** when the thing around the model grows — users, an admin back-office, many pages, a real schema. Same model, a bigger house to put it in.

→ Deploy what you build here with **[Module 14 — CI/CD & Deployment](../14_cicd/)** (Docker, GitHub Actions, HTTPS).

---

📝 **Finished this module?** Test yourself with the [Module 17 quiz](../quizzes/quiz_17_django.ipynb) — five questions, ~10 minutes.
