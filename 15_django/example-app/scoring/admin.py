from django.contrib import admin

from .models import Prediction


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "contract",
        "tenure_months",
        "monthly_charges",
        "support_tickets",
        "probability",
        "will_churn",
    )
    list_filter = ("contract", "will_churn")
    # A Prediction is an audit log — nobody should edit one after the fact.
    # `_meta.fields` lists every model field, so this stays correct if fields change.
    readonly_fields = [f.name for f in Prediction._meta.fields]
