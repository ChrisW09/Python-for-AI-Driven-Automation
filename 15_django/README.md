# 15 · Optional: Django for AI Web Apps

So far you've *built* models and *shipped* them as scripts, notebooks, and small FastAPI services (Modules 7, 11, 12). This optional module adds the other end of the spectrum: **Django**, the "batteries-included" web framework — the fastest way to wrap a model in a real, multi-page web application with a database, an admin dashboard, forms, and authentication, with almost no glue code.

> 📎 **Optional, reference-style module — no notebooks.** Like Module 12 (CI/CD), Django is a *project*, not a sequence of notebook cells. So this module is a short **mini-book** (the chapters below) plus a **runnable example app** you read, run, and extend. It runs **offline** — the only dependency is Django itself.

Our running example is **ChurnScope** — the churn-scoring tool you prototyped in Module 7 (NB 27–30) — rebuilt as a proper Django app: a form-driven UI, a JSON API, an admin dashboard, and the ORM logging every prediction to a database.

---

## What you'll learn

By the end of this module you will be able to:

- Explain **when to reach for Django** versus Flask / FastAPI — and what "batteries included" actually buys you.
- Describe Django's **MTV** request cycle (URL → view → template) and the **project vs app** split.
- Define data with **models**, evolve the schema with **migrations**, and query it through the **ORM** — then browse and edit it for free in the **admin site**.
- Route URLs, write **views**, render **templates**, and validate user input with **forms**.
- **Serve a model** from a view and a JSON API — and keep the heavy lifting *off* the request hot path.
- **Test** with Django's test client and harden settings for **production**, plugging straight into the Docker/CI pipeline from Module 12.

---

## Table of contents (read in this order)

| # | Chapter | What it covers |
|---|---|---|
| 1 | **README** (this file) | The big picture, vocabulary, and how to run the example app |
| 2 | [Why Django](why-django.md) | Django vs Flask/FastAPI; what "batteries included" means; when to pick which |
| 3 | [Project anatomy](project-anatomy.md) | `project` vs `app`, `manage.py`, `settings.py`, `urls.py`, and the MTV request cycle |
| 4 | [Models & admin](models-and-admin.md) | Models, migrations, the ORM, and the free admin dashboard |
| 5 | [Views, templates & forms](views-templates-forms.md) | URL routing, views, templates, and validated forms |
| 6 | [Serving a model](serving-a-model.md) | Calling the scorer from a view + a JSON API; where to load the model |
| 7 | [Testing & deployment](deployment.md) | The test client, production settings, gunicorn, and the link to Module 12 |
| 8 | [Exercises](exercises.md) | Extend ChurnScope — with worked solutions |

---

## The example app — ChurnScope

A complete, minimal Django project lives in [`example-app/`](example-app/). It has:

- a **form page** (`/`) where you enter a customer's details and get a churn probability,
- a **JSON API** (`POST /api/score`) for programmatic scoring,
- an **admin dashboard** (`/admin/`) that lists every prediction the ORM logged,
- a transparent **scorer** (`scoring/scorer.py`) — a stand-in for a trained model, so the app runs with *only* Django installed.

### Run it (≈2 minutes)

```bash
cd 15_django/example-app
python -m venv .venv && source .venv/bin/activate   # optional but recommended
pip install -r requirements.txt                     # just Django
python manage.py migrate                            # create the SQLite database
python manage.py runserver                          # http://127.0.0.1:8000/
```

Open <http://127.0.0.1:8000/>, score a customer, then create an admin login to inspect the log:

```bash
python manage.py createsuperuser                    # then visit /admin/
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

## Prerequisites

- **Module 1** (functions, classes), **Module 7** (you built ChurnScope as a POC), and a terminal.
- Helpful: **Module 12** (Docker/CI) — the deployment chapter hands off to it.

## Where this fits

Flask/FastAPI (Modules 7 & 12) are perfect for a thin model-serving API. Reach for **Django** when the thing around the model grows — users, an admin back-office, many pages, a real schema. Same model, a bigger house to put it in.

→ Deploy what you build here with **[Module 12 — CI/CD & Deployment](../12_cicd/)** (Docker, GitHub Actions, HTTPS).
