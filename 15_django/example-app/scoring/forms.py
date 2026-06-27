from django import forms

CONTRACT_CHOICES = [
    ("month-to-month", "Month-to-month"),
    ("one-year", "One year"),
    ("two-year", "Two year"),
]


class ChurnForm(forms.Form):
    """Validates one customer's details before they reach the scorer."""

    tenure_months = forms.IntegerField(min_value=0, max_value=120, initial=6)
    monthly_charges = forms.FloatField(min_value=0, initial=70.0)
    support_tickets = forms.IntegerField(min_value=0, max_value=50, initial=2)
    contract = forms.ChoiceField(choices=CONTRACT_CHOICES)
