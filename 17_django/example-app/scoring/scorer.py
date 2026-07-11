"""A transparent stand-in for a trained churn model.

Pure Python so the app runs with only Django installed. The coefficients mirror
the synthetic churn logic used across the course (Module 5 / Module 12): a
month-to-month contract and lots of support tickets push risk up; tenure pushes
it down. Swap this out for a pickled scikit-learn model without touching the
views, forms, templates, or admin.
"""
import math

CONTRACT_RISK = {"month-to-month": 0.9, "one-year": 0.0, "two-year": -0.9}


def churn_probability(*, tenure_months, monthly_charges, support_tickets, contract):
    """Return P(churn) in [0, 1] for one customer."""
    z = (
        -0.5
        + 1.4 * CONTRACT_RISK.get(contract, 0.0)
        - 0.05 * float(tenure_months)
        + 0.015 * float(monthly_charges)
        + 0.25 * float(support_tickets)
    )
    return 1.0 / (1.0 + math.exp(-z))
