from django.contrib.auth.models import User
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


class HistoryTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("analyst", password="pass1234")
        Prediction.objects.create(
            tenure_months=3, monthly_charges=95, support_tickets=4,
            contract="month-to-month", probability=0.81, will_churn=True,
        )

    def test_anonymous_redirected_to_login(self):
        resp = self.client.get(reverse("scoring:history"))
        self.assertRedirects(resp, "/accounts/login/?next=/history/")

    def test_logged_in_user_sees_prediction(self):
        self.client.login(username="analyst", password="pass1234")
        resp = self.client.get(reverse("scoring:history"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "month-to-month")
        self.assertContains(resp, "0.81")

    def test_pagination_splits_at_ten(self):
        for _ in range(14):  # 15 total with the one from setUp
            Prediction.objects.create(
                tenure_months=12, monthly_charges=70, support_tickets=1,
                contract="one-year", probability=0.30, will_churn=False,
            )
        self.client.login(username="analyst", password="pass1234")
        page1 = self.client.get(reverse("scoring:history"))
        self.assertEqual(len(page1.context["page_obj"]), 10)
        page2 = self.client.get(reverse("scoring:history"), {"page": 2})
        self.assertEqual(len(page2.context["page_obj"]), 5)
