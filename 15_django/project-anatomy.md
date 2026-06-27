# Project anatomy

> Chapter 3 of [Module 15 — Django for AI Web Apps](README.md).

Django splits your code into a **project** (the deployable site) and one or more **apps** (reusable feature modules). ChurnScope has one project (`churnscope`) and one app (`scoring`):

```
example-app/
├── manage.py              # the CLI: runserver, migrate, test, createsuperuser, …
├── churnscope/            # the PROJECT (site-wide config)
│   ├── settings.py        # installed apps, database, templates, security
│   ├── urls.py            # the root URL map
│   ├── wsgi.py / asgi.py  # the entry points a production server talks to
└── scoring/               # an APP (one feature: churn scoring)
    ├── models.py          # data → database tables (the ORM)
    ├── views.py           # request → response (calls the scorer)
    ├── urls.py            # this app's URL map
    ├── forms.py           # input validation
    ├── admin.py           # what shows up in /admin/
    ├── scorer.py          # the model stand-in (plain Python)
    ├── templates/         # HTML
    └── migrations/        # versioned schema changes
```

## `manage.py` — your control panel

Every Django task goes through `manage.py`:

| Command | What it does |
|---|---|
| `python manage.py runserver` | Start the dev server on `:8000` |
| `python manage.py makemigrations` | Turn model changes into migration files |
| `python manage.py migrate` | Apply migrations to the database |
| `python manage.py createsuperuser` | Make an admin login |
| `python manage.py test` | Run the test suite |
| `python manage.py shell` | A Python REPL with Django loaded |

## `settings.py` — the wiring

The important knobs (see `churnscope/settings.py`):

- `INSTALLED_APPS` — which apps are active (the admin, auth, sessions… **and `scoring`**).
- `DATABASES` — ChurnScope uses **SQLite** (a single file, zero setup) for the demo; swap in Postgres for production by changing this one dict.
- `TEMPLATES` — with `APP_DIRS=True`, Django finds `scoring/templates/` automatically.
- `DEBUG`, `SECRET_KEY`, `ALLOWED_HOSTS` — the three settings you **must** change for production (see the [deployment chapter](deployment.md)).

## The request cycle, end to end

When you submit the form:

1. The browser sends `POST /` to the dev server.
2. `churnscope/urls.py` includes `scoring/urls.py`, which maps `""` → `views.index`.
3. `views.index` validates the **form**, calls the **scorer**, writes a row via the **model** (ORM), and renders the **template** with the result.
4. The filled-in HTML comes back as the response.

That's MTV in motion. The next chapters open each box.
