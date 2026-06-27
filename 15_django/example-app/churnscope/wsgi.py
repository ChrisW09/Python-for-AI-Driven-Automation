"""WSGI entry point — what gunicorn/uWSGI talk to in production."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "churnscope.settings")
application = get_wsgi_application()
