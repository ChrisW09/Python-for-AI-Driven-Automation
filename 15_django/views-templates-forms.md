# Views, templates & forms

> Chapter 5 of [Module 15 — Django for AI Web Apps](README.md).

## URLs → views

`churnscope/urls.py` delegates to the app, which maps paths to view functions (`scoring/urls.py`):

```python
app_name = "scoring"
urlpatterns = [
    path("", views.index, name="index"),
    path("api/score", views.api_score, name="api_score"),
]
```

Named routes (`name="index"`) let templates and tests refer to URLs without hard-coding them (`reverse("scoring:index")`).

## Views = request → response

A **view** takes a `request` and returns a response. The form view (`scoring/views.py`, simplified):

```python
def index(request):
    result = None
    if request.method == "POST":
        form = ChurnForm(request.POST)
        if form.is_valid():
            p = churn_probability(**form.cleaned_data)      # call the model
            result = {"probability": p, "will_churn": p >= THRESHOLD}
            Prediction.objects.create(**form.cleaned_data, **result)  # log it
    else:
        form = ChurnForm()
    return render(request, "scoring/form.html", {"form": form, "result": result})
```

`render(request, template, context)` is the workhorse: it fills the template with the context dict and returns an `HttpResponse`.

## Forms = validation you don't write twice

A **form** declares fields once and gets validation, error messages, and HTML rendering for free (`scoring/forms.py`):

```python
class ChurnForm(forms.Form):
    tenure_months   = forms.IntegerField(min_value=0, max_value=120, initial=6)
    monthly_charges = forms.FloatField(min_value=0, initial=70.0)
    support_tickets = forms.IntegerField(min_value=0, max_value=50, initial=2)
    contract        = forms.ChoiceField(choices=CONTRACT_CHOICES)
```

`form.is_valid()` runs every rule and populates `form.cleaned_data` with typed, trusted values — so your view (and your model) never see a raw string where they expect an int.

## Templates = HTML with holes

Templates live in `scoring/templates/scoring/`. They use `{{ variables }}` and `{% tags %}`:

```html
<form method="post">
  {% csrf_token %}        {# Django's CSRF protection, one tag #}
  {{ form.as_p }}         {# renders every field, with labels + errors #}
  <button type="submit">Score</button>
</form>
{% if result %}
  <p>Churn probability: <b>{{ result.probability|floatformat:2 }}</b></p>
{% endif %}
```

`{% csrf_token %}` is mandatory on POST forms — it's the anti-forgery protection Django gives you by default.
