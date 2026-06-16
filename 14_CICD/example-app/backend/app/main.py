"""Minimal FastAPI service for the CI/CD & deployment module.

Exposes three endpoints:
- GET /api/health   liveness probe used by Docker/monitoring
- GET /api/message  a hello-world payload the frontend renders
- GET /api/visits   a visit counter backed by Postgres (graceful if DB is down)
"""
import os
from contextlib import asynccontextmanager

import psycopg
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

DATABASE_URL = os.getenv("DATABASE_URL", "")


def _init_db() -> None:
    """Create the visits table if a database is configured and reachable."""
    if not DATABASE_URL:
        return
    with psycopg.connect(DATABASE_URL, connect_timeout=5) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS visits (id serial PRIMARY KEY, ts timestamptz DEFAULT now())"
        )


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs once on startup. We swallow DB errors so the API still serves
    # /health and /message even when Postgres is not ready yet.
    try:
        _init_db()
    except Exception as exc:  # pragma: no cover - depends on runtime env
        print(f"[startup] DB init skipped: {exc}")
    yield


app = FastAPI(title="Example API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/message")
def message():
    return {"message": "Hello from FastAPI"}


@app.get("/api/visits")
def visits():
    if not DATABASE_URL:
        return {"visits": None, "detail": "no database configured"}
    try:
        with psycopg.connect(DATABASE_URL, connect_timeout=5) as conn:
            conn.execute("INSERT INTO visits DEFAULT VALUES")
            row = conn.execute("SELECT count(*) FROM visits").fetchone()
        return {"visits": row[0]}
    except Exception as exc:
        return {"visits": None, "detail": f"database unavailable: {exc}"}
