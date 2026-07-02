# Auth & the history page

> Chapter 6 of [Module 15 — Django for AI Web Apps](README.md).

Every prediction ChurnScope makes is logged to the database — but so far the only way to *see* that log is the admin site, and the admin is for staff, not for everyday users. This chapter adds a proper **history page** and, along the way, the last big battery in the box: **authentication**. You will write almost none of it yourself — that's the point.

## Django's auth is already installed

Look at `INSTALLED_APPS` in `churnscope/settings.py`: `django.contrib.auth` has been there since `startproject`. That app ships a `User` model, password hashing, sessions, login/logout views, password-reset flows, and permission checks. The admin login you created with `createsuperuser`? That *is* Django auth — you've been using it since chapter 4.

To use it in your own pages you need exactly three things.

**1. Mount the built-in views.** One line in `churnscope/urls.py`:

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    # Django's built-in login/logout/password views — no custom auth code needed.
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("scoring.urls")),
]
```

That single `include` gives you `/accounts/login/`, `/accounts/logout/`, and the whole password-change/reset family — routed, validated, and secure.

**2. Tell Django where things are.** Three settings (`churnscope/settings.py`):

```python
LOGIN_URL = "/accounts/login/"        # where @login_required sends strangers
LOGIN_REDIRECT_URL = "/history/"      # where a fresh login lands
LOGOUT_REDIRECT_URL = "/"             # where logout drops you
```

**3. Give the login view a template.** By convention it looks for `registration/login.html`. Ours is nine lines (`scoring/templates/registration/login.html`) — extend the base, render `{{ form.as_p }}`, add a button. The *view logic* — checking the password, creating the session, redirecting — is all Django's.

## Protecting a view: one decorator

The history view itself is four lines plus a decorator (`scoring/views.py`):

```python
@login_required
def history(request):
    """Paginated prediction log, newest first (per the model's Meta.ordering)."""
    paginator = Paginator(Prediction.objects.all(), per_page=10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "scoring/history.html", {"page_obj": page_obj})
```

One more line wires it up in `scoring/urls.py` — the same pattern as every route so far:

```python
path("history/", views.history, name="history"),
```

`@login_required` is the whole security story: anonymous visitors get bounced to `LOGIN_URL` with a `?next=/history/` parameter, and after logging in they land right back where they were heading. No session-checking code in your view, ever.

Two more things worth noticing:

- **`Paginator` is a battery too.** Hand it any queryset and a page size; `get_page()` clamps bad input (page `"banana"` → page 1, page 9999 → last page) instead of crashing. The template asks `page_obj.has_previous` / `has_next` and renders prev/next links only when they exist — look at `scoring/templates/scoring/history.html`.
- **The queryset stays lazy.** `Prediction.objects.all()` doesn't fetch every row; the paginator slices it, and the database only ever returns the ten rows for the current page. Ordering comes free from the model's `Meta.ordering` — the newest-first rule lives in *one* place, and the admin, the history page, and any future consumer all inherit it.

## Logging out is a POST

One modern gotcha, visible in `scoring/templates/scoring/base.html`: the logout control is a tiny **form**, not a link.

```html
{% if user.is_authenticated %}
  <form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button type="submit">Log out ({{ user.username }})</button>
  </form>
{% endif %}
```

Django 5 removed GET logout on purpose: anything that *changes state* (and destroying a session is a state change) should be a POST, so a stray prefetch or a malicious image tag can't log your users out. The `{% if user.is_authenticated %}` guard works in every template — Django injects `user` into the context automatically.

## Testing auth without a browser

The test client can log in, so the whole flow is testable in milliseconds (`scoring/tests.py`, `HistoryTests`):

```python
def test_anonymous_redirected_to_login(self):
    resp = self.client.get(reverse("scoring:history"))
    self.assertRedirects(resp, "/accounts/login/?next=/history/")

def test_logged_in_user_sees_prediction(self):
    self.client.login(username="analyst", password="pass1234")
    resp = self.client.get(reverse("scoring:history"))
    self.assertContains(resp, "month-to-month")
```

Redirect-for-strangers and content-for-members: those two assertions pin down the security behaviour, so a refactor that accidentally drops `@login_required` fails CI instead of leaking data.

**Try it:** `python manage.py runserver`, score a customer or two, then open <http://127.0.0.1:8000/history/> — you'll be bounced to the login page; sign in with the superuser from the README and the log appears.

→ Next: [Serving a model](serving-a-model.md) — where the number in that table actually comes from, and how to swap the stand-in for a real one.
