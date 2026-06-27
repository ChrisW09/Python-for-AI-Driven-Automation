"""ASGI entry point — for async servers (uvicorn/daphne)."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "churnscope.settings")
application = get_asgi_application()
