# Why Django?

> Chapter 2 of [Module 15 — Django for AI Web Apps](README.md).

You already know two ways to put Python on the web from this course:

- **FastAPI** (Modules 7, 12) — a thin, fast, async-friendly **API** layer. You hand it functions, it gives you JSON endpoints and auto-docs. Perfect for *serving a model*.
- **Flask** — a tiny, unopinionated micro-framework. You assemble the pieces you want.

**Django** is the opposite of micro: it's **batteries-included**. Out of the box you get an **ORM** (database access without SQL), **migrations** (versioned schema changes), a generated **admin** site, a **forms** system (validation + rendering), **authentication**, **templating**, **security middleware** (CSRF, XSS, clickjacking), and **sessions** — all wired together with sensible defaults.

## The trade-off in one line

| | Flask / FastAPI | Django |
|---|---|---|
| Philosophy | Bring your own pieces | Batteries included |
| Best at | A focused API / microservice | A full application with data + users + back-office |
| ORM / migrations / admin / auth | add libraries | built in |
| Learning curve | gentle | steeper, then very productive |

## When to pick which

- **Serving a single model as an endpoint?** FastAPI. (You did this in Module 12.)
- **A real application around the model** — a login, many pages, a database you'll evolve, an admin dashboard for non-engineers, a back-office? **Django.** The admin and ORM alone save weeks.
- **You want both?** Common in production: Django for the app + a FastAPI/Django-Ninja service for the hot prediction path. They coexist happily.

## The mental model: MTV

Django calls its shape **MTV** — *Model, Template, View* (Django's spin on MVC):

- **Model** — your data, defined as Python classes; the ORM turns them into database tables.
- **View** — a function (or class) that takes a request and returns a response. *This is where your model gets called.*
- **Template** — the HTML, with placeholders the view fills in.

A request flows **URL → View → (Model + Template) → Response**. The next chapter walks that path through the ChurnScope project.
