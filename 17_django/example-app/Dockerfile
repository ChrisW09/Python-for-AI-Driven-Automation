# syntax=docker/dockerfile:1

# ---- Base image: small, official Python (same pattern as Module 14) ----
FROM python:3.12-slim

# Sensible Python defaults inside containers
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# All later paths are relative to /app
WORKDIR /app

# Copy ONLY requirements first so the pip layer is cached until deps change
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the application code
COPY manage.py .
COPY churnscope ./churnscope
COPY scoring ./scoring

# Run as a non-root user (never run containers as root in production).
# appuser must own /app so SQLite can create db.sqlite3 there.
RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

# Document the port the app listens on
EXPOSE 8000

# Container-level liveness check — stdlib only, since slim images have no curl.
# It hits the form page. With DJANGO_DEBUG=0 you must include 'localhost' in
# DJANGO_ALLOWED_HOSTS or the check 400s (see the run example in deployment.md).
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:8000/').status==200 else 1)"

# Migrate, then serve with gunicorn (the WSGI server; runserver is dev-only).
# Migrating at container start is fine for this single-container SQLite demo;
# in real life run migrations as a separate release step so several replicas
# don't race to migrate the same database. `exec` makes gunicorn PID 1 so it
# receives Docker's stop signals directly.
CMD ["sh", "-c", "python manage.py migrate --noinput && exec gunicorn churnscope.wsgi --bind 0.0.0.0:8000"]
