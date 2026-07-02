"""Root URL map: the admin site, auth views, plus everything in the scoring app."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Django's built-in login/logout/password views — no custom auth code needed.
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("scoring.urls")),
]
