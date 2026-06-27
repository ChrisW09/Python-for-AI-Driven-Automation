from django.db import models


class Prediction(models.Model):
    """One churn score, logged for the admin dashboard and audit trail."""

    created_at = models.DateTimeField(auto_now_add=True)
    tenure_months = models.PositiveIntegerField()
    monthly_charges = models.FloatField()
    support_tickets = models.PositiveIntegerField()
    contract = models.CharField(max_length=20)
    probability = models.FloatField()
    will_churn = models.BooleanField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        verdict = "churn" if self.will_churn else "stay"
        return f"{self.contract}: p={self.probability:.2f} ({verdict})"
