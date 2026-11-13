import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import ChurnForm
from .models import Prediction
from .scorer import churn_probability

THRESHOLD = 0.5


def index(request):
    """The churn form: GET shows it, POST scores + logs + shows the result."""
    result = None
    if request.method == "POST":
        form = ChurnForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            p = churn_probability(**data)
            will_churn = p >= THRESHOLD
            Prediction.objects.create(probability=p, will_churn=will_churn, **data)
            result = {"probability": p, "will_churn": will_churn}
    else:
        form = ChurnForm()
    return render(
        request,
        "scoring/form.html",
        {"form": form, "result": result, "threshold": THRESHOLD},
    )


@login_required
def history(request):
    """Paginated prediction log, newest first (per the model's Meta.ordering)."""
    paginator = Paginator(Prediction.objects.all(), per_page=10)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "scoring/history.html", {"page_obj": page_obj})


@csrf_exempt  # stateless JSON API; use token auth (DRF/Ninja) in production
@require_POST
def api_score(request):
    """Score one customer sent as JSON, log it, and return the verdict.

    The payload is validated by the same ``ChurnForm`` as the HTML form, so
    both surfaces enforce one set of rules (required fields, whole numbers,
    value ranges, known contract types, finite charges). Anything the form
    rejects gets a 400 and never reaches the scorer or the audit log.

    Parameters
    ----------
    request : django.http.HttpRequest
        A POST whose body is a JSON object with the keys ``tenure_months``,
        ``monthly_charges``, ``support_tickets`` and ``contract``.

    Returns
    -------
    django.http.JsonResponse
        200 with ``{"probability": float, "will_churn": bool}`` on success.
        400 with ``{"error": str}`` if the body is not a JSON object, or
        ``{"error": str, "fields": {name: [message, ...]}}`` if the form
        rejects one or more fields.
    """
    try:
        payload = json.loads(request.body or "{}")
    except ValueError as exc:  # json.JSONDecodeError and UnicodeDecodeError
        return JsonResponse({"error": f"invalid JSON: {exc}"}, status=400)
    if not isinstance(payload, dict):
        return JsonResponse({"error": "invalid request: expected a JSON object"}, status=400)

    form = ChurnForm(payload)
    if not form.is_valid():
        fields = {name: list(errors) for name, errors in form.errors.items()}
        return JsonResponse({"error": "invalid request", "fields": fields}, status=400)

    data = form.cleaned_data
    p = churn_probability(**data)
    will_churn = p >= THRESHOLD
    Prediction.objects.create(probability=p, will_churn=will_churn, **data)
    return JsonResponse({"probability": round(p, 4), "will_churn": will_churn})
