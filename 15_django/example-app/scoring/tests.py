from django.test import TestCase
from django.urls import reverse

from .models import Prediction
from .scorer import churn_probability


class ScorerTests(TestCase):
    def test_month_to_month_is_riskier(self):
        risky = churn_probability(
            tenure_months=3, monthly_charges=95, support_tickets=4,
            contract="month-to-month",
        )
        safe = churn_probability(
            tenure_months=3, monthly_charges=95, support_tickets=4,
            contract="two-year",
        )
        self.assertGreater(risky, safe)

    def test_probability_in_range(self):
        p = churn_probability(
            tenure_months=12, monthly_charges=70, support_tickets=1,
            contract="one-year",
        )
        self.assertGreaterEqual(p, 0.0)
        self.assertLessEqual(p, 1.0)


class ViewTests(TestCase):
    def test_form_get(self):
        resp = self.client.get(reverse("scoring:index"))
        self.assertEqual(resp.status_code, 200)

    def test_form_post_logs_prediction(self):
        resp = self.client.post(
            reverse("scoring:index"),
            {
                "tenure_months": 3,
                "monthly_charges": 95,
                "support_tickets": 4,
                "contract": "month-to-month",
            },
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Prediction.objects.count(), 1)

    def test_api_score(self):
        resp = self.client.post(
            reverse("scoring:api_score"),
            data='{"tenure_months":3,"monthly_charges":95,'
                 '"support_tickets":4,"contract":"month-to-month"}',
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 200)
        body = resp.json()
        self.assertIn("probability", body)
        self.assertIn("will_churn", body)

    def test_api_bad_request(self):
        resp = self.client.post(
            reverse("scoring:api_score"),
            data='{"monthly_charges":95}',  # missing fields
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 400)
