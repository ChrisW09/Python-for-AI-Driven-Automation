from django.urls import path

from . import views

app_name = "scoring"

urlpatterns = [
    path("", views.index, name="index"),
    path("history/", views.history, name="history"),
    path("api/score", views.api_score, name="api_score"),
]
