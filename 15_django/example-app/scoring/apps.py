from django.apps import AppConfig


class ScoringConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "scoring"

    def ready(self):
        # The seam for loading a real model ONCE at startup (a pickled
        # scikit-learn estimator, a warmed LLM client, ...). ChurnScope's
        # scorer is pure Python, so there is nothing to load here yet.
        return
