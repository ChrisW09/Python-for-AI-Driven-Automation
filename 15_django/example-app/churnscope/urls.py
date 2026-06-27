"""Root URL map: the admin site, plus everything in the scoring app."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("scoring.urls")),
]
