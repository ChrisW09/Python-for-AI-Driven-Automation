"""Django settings for the ChurnScope example project.

Deliberately small. The three production-critical settings (DEBUG, SECRET_KEY,
ALLOWED_HOSTS) are read from the environment with safe-for-dev fallbacks — see
the deployment chapter.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Security: override all three via env vars in production ---------------
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY", "dev-only-insecure-key-change-me-in-production"
)
DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"
ALLOWED_HOSTS = (
    ["*"] if DEBUG else os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
)

# --- Applications ---------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "scoring",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "churnscope.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "churnscope.wsgi.application"

# --- Database: SQLite for the demo; swap this dict for Postgres in prod ----
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
]

# --- Auth: built-in views mounted at /accounts/ in churnscope/urls.py ------
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/history/"
LOGOUT_REDIRECT_URL = "/"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
