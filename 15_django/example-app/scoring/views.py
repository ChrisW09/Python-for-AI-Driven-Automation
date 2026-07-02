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
    """POST JSON -> {"probability": float, "will_churn": bool}."""
    try:
        payload = json.loads(request.body or "{}")
        p = churn_probability(
            tenure_months=int(payload["tenure_months"]),
            monthly_charges=float(payload["monthly_charges"]),
            support_tickets=int(payload["support_tickets"]),
            contract=str(payload["contract"]),
        )
    except (KeyError, ValueError, TypeError) as exc:
        return JsonResponse({"error": f"invalid request: {exc}"}, status=400)

    will_churn = p >= THRESHOLD
    Prediction.objects.create(
        tenure_months=int(payload["tenure_months"]),
        monthly_charges=float(payload["monthly_charges"]),
        support_tickets=int(payload["support_tickets"]),
        contract=str(payload["contract"]),
        probability=p,
        will_churn=will_churn,
    )
    return JsonResponse({"probability": round(p, 4), "will_churn": will_churn})
