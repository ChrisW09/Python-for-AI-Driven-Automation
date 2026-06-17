# Exercises — The Capstone Bank

> 💡 **Intuition:** Each chapter in this module ends with a few small drills.
> This file is the **consolidated, graded bank** — the gym where you put it all
> together on the *canonical example app*. Work top to bottom, or jump to the
> section matching the chapter you just read.

Every exercise targets the **same app** you build in [tutorial.md](tutorial.md):
backend (`:8000`), frontend (`:80`), `nginx` (publishes `:80`/`:443`), Postgres
`db`, network `appnet`, volume `db_data`, images
`ghcr.io/chrisw09/example-app-{backend,frontend,nginx}`, domain `example.com`,
server `203.0.113.10`, deploy path `/opt/example-app`. Keep these names exactly —
consistency is the point.

**Difficulty tiers** (look for the badge on each task):

- 🟢 **Beginner** — one tool, guided, a few minutes.
- 🟡 **Intermediate** — combine ideas, light problem-solving.
- 🔴 **Advanced** — design decisions, edge cases, production thinking.

Each exercise states a concrete **deliverable**. Full answer keys are in
collapsible `<details>` blocks — try first, then check.

**Sections:** [Docker](#1-docker) · [Compose](#2-compose) ·
[Actions](#3-github-actions) · [Registries](#4-registries) · [DNS](#5-dns) ·
[Reverse proxies](#6-reverse-proxies) · [HTTPS](#7-https) ·
[Deployment](#8-deployment) · [Monitoring](#9-monitoring) ·
[Troubleshooting](#10-troubleshooting) · [Capstone challenges](#11-capstone-challenges)

---

## 1. Docker

> Concepts: images (*recipes*), containers (*cooked meals*), layers (*recipe
> steps*), volumes (*pantry*). Chapter: [docker.md](docker.md).

### 1.1 🟢 Build and run the backend image

**Deliverable:** a screenshot or pasted terminal output showing
`curl http://localhost:8000/api/health` returning `{"status":"ok"}` from a
container you built.

Build the backend image tagged `example-app-backend:dev`, run it with the right
port published, and hit `/api/health`.

<details>
<summary>Answer key</summary>

```bash
cd example-app/backend
docker build -t example-app-backend:dev .
docker run --rm -p 8000:8000 example-app-backend:dev
# in another terminal:
curl http://localhost:8000/api/health   # {"status":"ok"}
```

The `-p 8000:8000` maps host port → container port. Without it the container runs
but is unreachable.
</details>

### 1.2 🟡 Prove layer caching saves time

**Deliverable:** two build timings showing the second build is near-instant after
an app-only code change, and a one-sentence explanation.

Build the image once. Then add a blank line to `app/main.py` (a code change, not
a dependency change) and rebuild. Time both builds and explain why the second is
faster.

<details>
<summary>Answer key</summary>

```bash
time docker build -t example-app-backend:dev .   # full build
echo "" >> app/main.py
time docker build -t example-app-backend:dev .   # much faster
```

Because the Dockerfile copies `requirements.txt` and runs `pip install` *before*
`COPY app ./app`, the expensive pip layer is cached. Only the `COPY app` layer
and everything after it re-run when application code changes. Reordering those
COPYs would bust the cache on every code edit.
</details>

### 1.3 🔴 Shrink and harden the image

**Deliverable:** a short report comparing image size and listing two security
improvements already present in the canonical Dockerfile (§5.6), plus one you'd
add.

Inspect the built image's size and layers, identify the non-root user and
healthcheck, and propose one further hardening step.

<details>
<summary>Answer key</summary>

```bash
docker images example-app-backend:dev          # ~210MB on python:3.12-slim
docker history example-app-backend:dev         # see per-layer sizes
```

Already present: (1) `python:3.12-slim` base keeps size down; (2) `USER appuser`
runs as non-root; (3) `--no-cache-dir` on pip avoids a cache layer; (4) a
`HEALTHCHECK`. One more step: a **multi-stage build** that installs into a venv in
a builder stage and copies only the venv into a slim runtime stage, or pinning to
a digest (`python:3.12-slim@sha256:...`) for reproducibility. The `.dockerignore`
(§5.7) also keeps `tests/`, `.venv/`, and caches out of the build context.
</details>

**Next / Related:** [docker.md](docker.md) · [tutorial.md](tutorial.md) Phase 1.

---

## 2. Compose

> Concepts: multi-service orchestration, `appnet` network, service-name DNS,
> `depends_on` health conditions, the `db_data` volume. Chapter:
> [docker-compose.md](docker-compose.md).

### 2.1 🟢 Bring up the full stack and read its state

**Deliverable:** output of `docker compose ps` showing all four services up, with
`db` and `backend` healthy.

<details>
<summary>Answer key</summary>

```bash
cd example-app
docker compose up --build -d
docker compose ps
```

You should see `example-app-{backend,db,frontend,nginx}-1`. Only `nginx` shows a
published port (`0.0.0.0:80->80/tcp`); the others are internal to `appnet`.
</details>

### 2.2 🟡 Explain and test service discovery

**Deliverable:** a command that proves the backend can reach Postgres by the
hostname `db`, and one sentence on why that hostname works.

<details>
<summary>Answer key</summary>

```bash
docker compose exec backend python -c \
  "import psycopg,os; print(psycopg.connect(os.environ['DATABASE_URL']).execute('select 1').fetchone())"
# (1,)
```

It works because all services join the `appnet` network, and Docker's embedded
DNS resolves each **service name** (`db`, `backend`, `frontend`) to that
container's IP. That's why `DATABASE_URL` uses `@db:5432` rather than an IP.
</details>

### 2.3 🔴 Add a one-off override without editing the canonical file

**Deliverable:** a `docker-compose.override.yml` that publishes the backend on
`8000` for local debugging, applied automatically, with the canonical
`docker-compose.yml` left untouched.

<details>
<summary>Answer key</summary>

Create `example-app/docker-compose.override.yml`:

```yaml
services:
  backend:
    ports:
      - "8000:8000"
```

```bash
docker compose up -d        # override is merged automatically
curl http://localhost:8000/api/health   # {"status":"ok"}
```

Compose auto-merges `docker-compose.override.yml` on top of the base file. This
keeps the production template (§5.12) clean — in production the backend stays
unpublished behind Nginx. Don't commit the override into the deploy bundle.
</details>

**Next / Related:** [docker-compose.md](docker-compose.md) ·
[tutorial.md](tutorial.md) Phases 2–3.

---

## 3. GitHub Actions

> Concepts: CI (*quality-control line*), CD (*delivery truck*), jobs, `needs`,
> the repo-root workflow requirement. Chapter:
> [github-actions.md](github-actions.md).

### 3.1 🟢 Run the test job locally before pushing

**Deliverable:** `pytest -q` output showing `2 passed`.

<details>
<summary>Answer key</summary>

```bash
cd example-app/backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q          # 2 passed
```

This mirrors exactly what the `test` job does, so you catch failures before the
factory does.
</details>

### 3.2 🟡 Relocate the workflow so it actually runs

**Deliverable:** the workflow living at the repo-root `.github/workflows/ci-cd.yml`
and a green Actions run.

<details>
<summary>Answer key</summary>

```bash
mkdir -p .github/workflows
cp 12_cicd/example-app/.github/workflows/ci-cd.yml \
   .github/workflows/ci-cd.yml
git add .github/workflows/ci-cd.yml
git commit -m "Enable CI/CD workflow"
git push origin main
```

GitHub only runs workflows under the **repository root** `.github/workflows/`.
The module co-locates the file for teaching; the `APP_DIR` env var already points
at the module path, so no edits are needed after the copy.
</details>

### 3.3 🔴 Add a lint gate that blocks the build

**Deliverable:** a new step (or job) running `ruff check` that the
`build-and-push` job `needs`, so a lint failure stops image builds.

<details>
<summary>Answer key</summary>

Add `ruff==0.8.4` to `requirements.txt` (or install in the step), then add to the
`test` job:

```yaml
      - name: Lint
        working-directory: ${{ env.APP_DIR }}/backend
        run: ruff check .
```

Because `build-and-push` already declares `needs: test`, any failing step in
`test` (including lint) blocks the build and deploy jobs. Alternatively make lint
its own job and add it to `build-and-push`'s `needs: [test, lint]`.
</details>

**Next / Related:** [github-actions.md](github-actions.md) ·
[tutorial.md](tutorial.md) Phase 4.

---

## 4. Registries

> Concepts: GHCR as the *warehouse*, image tags (`:latest`, `:<sha>`), pulling
> with auth. Chapter: [registries.md](registries.md).

### 4.1 🟢 Pull a published image

**Deliverable:** terminal output of a successful `docker pull` of the backend
image from GHCR.

<details>
<summary>Answer key</summary>

```bash
echo "$GHCR_TOKEN" | docker login ghcr.io -u chrisw09 --password-stdin
docker pull ghcr.io/chrisw09/example-app-backend:latest
```

The owner is lowercased (`ChrisW09` → `chrisw09`) because GHCR requires lowercase
namespaces.
</details>

### 4.2 🟡 Tag and push a manual build to GHCR

**Deliverable:** the frontend image pushed under both `:latest` and a custom tag.

<details>
<summary>Answer key</summary>

```bash
cd example-app/frontend
docker build -t ghcr.io/chrisw09/example-app-frontend:latest \
             -t ghcr.io/chrisw09/example-app-frontend:manual-1 .
docker push ghcr.io/chrisw09/example-app-frontend:latest
docker push ghcr.io/chrisw09/example-app-frontend:manual-1
```

In CI we tag with both `:latest` and `${{ github.sha }}` so every build is
traceable to a commit while `:latest` always points at the newest main build.
</details>

### 4.3 🔴 Explain `:latest` risk and pin a deploy

**Deliverable:** a short note on why deploying `:latest` is risky, plus a Compose
snippet pinning images to an immutable SHA tag.

<details>
<summary>Answer key</summary>

`:latest` is a moving pointer — two `docker compose pull` runs can fetch different
bits, so you can't reproduce or cleanly roll back a deploy. Pin to the commit SHA
tag CI already pushes:

```yaml
  backend:
    image: ghcr.io/chrisw09/example-app-backend:9f3c1ab
```

Roll back by changing the tag to a previous SHA and re-running `docker compose up
-d`. Keep `:latest` for convenience locally; pin SHAs (or use digests) in
production.
</details>

**Next / Related:** [registries.md](registries.md) ·
[github-actions.md](github-actions.md).

---

## 5. DNS

> Concepts: DNS as the *internet phone book*, A records, propagation. Chapter:
> [dns.md](dns.md).

### 5.1 🟢 Resolve the domain

**Deliverable:** `dig +short example.com` returning `203.0.113.10`.

<details>
<summary>Answer key</summary>

```bash
dig +short example.com        # 203.0.113.10
dig +short www.example.com    # 203.0.113.10
```

Both names resolve because we created two A records pointing at the server IP.
</details>

### 5.2 🟡 Design the record set

**Deliverable:** a table of DNS records to serve both `example.com` and
`www.example.com` from `203.0.113.10`.

<details>
<summary>Answer key</summary>

| Type | Name  | Value          | TTL  |
|------|-------|----------------|------|
| A    | `@`   | `203.0.113.10` | 3600 |
| A    | `www` | `203.0.113.10` | 3600 |

`@` is the apex (`example.com`). A `CNAME www → example.com` is an alternative for
`www`, but you cannot CNAME the apex itself, so an A record there is the safe
choice.
</details>

### 5.3 🔴 Diagnose a stale record

**Deliverable:** the commands to confirm whether a wrong IP is cached locally vs.
served by the authoritative nameserver, and the fix.

<details>
<summary>Answer key</summary>

```bash
dig example.com              # check the ANSWER + TTL your resolver returns
dig @1.1.1.1 example.com     # bypass local cache, ask a public resolver
dig +trace example.com       # follow the delegation to the authoritative NS
```

If the authoritative answer is already correct but a resolver still serves the old
IP, it's a **TTL/caching** issue — wait out the TTL or flush the local cache.
Lowering TTL *before* a planned change reduces this window.
</details>

**Next / Related:** [dns.md](dns.md) · [tutorial.md](tutorial.md) Phase 5.4.

---

## 6. Reverse proxies

> Concepts: Nginx as the *receptionist*, path-based routing `/` vs `/api/`,
> upstreams, proxy headers. Chapter: [reverse-proxies.md](reverse-proxies.md).

### 6.1 🟢 Trace a request through the proxy

**Deliverable:** explain, in two or three sentences, the path of a browser request
to `http://localhost/api/message` through the running stack.

<details>
<summary>Answer key</summary>

The browser hits Nginx on port 80. Nginx matches the `location /api/` block and
proxies the request to `http://backend_upstream` (the `backend` service on
`:8000`). The backend returns `{"message":"Hello from FastAPI"}`, which Nginx
relays back. A request to `/` instead matches `location /` and goes to the
`frontend` upstream.
</details>

### 6.2 🟡 Add a `/healthz` proxy passthrough

**Deliverable:** an Nginx `location` that maps `/healthz` to the backend's
`/api/health`, plus a `curl` proving it.

<details>
<summary>Answer key</summary>

In `nginx/default.conf`, add inside the `server` block:

```nginx
    location = /healthz {
        proxy_pass http://backend_upstream/api/health;
    }
```

```bash
docker compose up --build -d
curl http://localhost/healthz     # {"status":"ok"}
```

The `=` makes it an exact match, and the URI on `proxy_pass` rewrites the path
sent upstream.
</details>

### 6.3 🔴 Add caching headers and gzip for the frontend

**Deliverable:** an Nginx config change that gzips text responses and sets a
cache header for static assets, with a note on why you'd *not* cache `/api/`.

<details>
<summary>Answer key</summary>

```nginx
    gzip on;
    gzip_types text/plain text/css application/javascript application/json;

    location / {
        proxy_pass http://frontend_upstream;
        add_header Cache-Control "public, max-age=300";
        # ...existing proxy_set_header lines...
    }
```

Don't cache `/api/` responses: `/api/visits` mutates state and returns a changing
counter, and `/api/message` should reflect the latest backend. Caching dynamic
API responses would serve stale data. Static frontend assets are safe to cache.
</details>

**Next / Related:** [reverse-proxies.md](reverse-proxies.md) ·
[https.md](https.md).

---

## 7. HTTPS

> Concepts: TLS certificate as a *tamper-proof ID card*, Let's Encrypt/Certbot,
> auto-renewal, HTTP→HTTPS redirect. Chapter: [https.md](https.md).

### 7.1 🟢 Inspect a site's certificate

**Deliverable:** the issuer and expiry of `example.com`'s certificate via CLI.

<details>
<summary>Answer key</summary>

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -noout -issuer -dates
```

Shows `issuer=...Let's Encrypt...`, `notBefore`, and `notAfter`. Let's Encrypt
certs last 90 days, which is why renewal must be automated.
</details>

### 7.2 🟡 Obtain a certificate and force HTTPS

**Deliverable:** a certbot command for `example.com` + `www.example.com` and an
Nginx redirect from port 80 to 443.

<details>
<summary>Answer key</summary>

```bash
sudo certbot certonly --standalone -d example.com -d www.example.com
```

Then in Nginx, redirect HTTP to HTTPS:

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    return 301 https://$host$request_uri;
}
```

The 443 server block then references the certs under
`/etc/letsencrypt/live/example.com/`. DNS must resolve and port 80 be open
*before* requesting the cert, since Let's Encrypt validates by connecting back.
</details>

### 7.3 🔴 Make renewal automatic and verify it

**Deliverable:** the renewal mechanism and a dry-run command proving it works.

<details>
<summary>Answer key</summary>

```bash
sudo certbot renew --dry-run
systemctl list-timers | grep certbot   # the certbot.timer runs renew twice daily
```

Certbot installs a systemd timer (or cron job) that runs `certbot renew`; it only
renews certs within 30 days of expiry. A **deploy hook** should reload Nginx after
renewal: `--deploy-hook "docker compose -f /opt/example-app/docker-compose.yml exec nginx nginx -s reload"`
(or restart the nginx service) so the new cert is picked up.
</details>

**Next / Related:** [https.md](https.md) · [dns.md](dns.md) ·
[reverse-proxies.md](reverse-proxies.md).

---

## 8. Deployment

> Concepts: the Ubuntu server as the *restaurant kitchen*, `/opt/example-app`,
> pulling images, `docker compose up -d`, rollbacks. Chapter:
> [deployment.md](deployment.md).

### 8.1 🟢 Deploy by pulling prebuilt images

**Deliverable:** the server running the stack from GHCR images (no local build).

<details>
<summary>Answer key</summary>

```bash
ssh deploy@203.0.113.10
cd /opt/example-app
docker compose pull
docker compose up -d
docker compose ps           # all four Up; nginx publishes :80
curl -s http://localhost/api/health   # {"status":"ok"}
```
</details>

### 8.2 🟡 Roll back to the previous image

**Deliverable:** steps to roll the backend back one version after a bad deploy.

<details>
<summary>Answer key</summary>

```bash
# pin the backend to the previous good SHA in docker-compose.yml:
#   image: ghcr.io/chrisw09/example-app-backend:<previous-sha>
docker compose pull backend
docker compose up -d backend
docker compose logs -f backend
```

Because CI tags every image with its commit SHA, rolling back is just selecting an
older immutable tag and re-upping that one service. This is why SHA tags matter
(see Exercise 4.3).
</details>

### 8.3 🔴 Zero-downtime config reload

**Deliverable:** reload an Nginx config change without dropping live connections,
and explain why a full `down`/`up` is worse.

<details>
<summary>Answer key</summary>

```bash
docker compose exec nginx nginx -t          # validate config first
docker compose exec nginx nginx -s reload   # graceful reload, no dropped conns
```

`nginx -s reload` re-reads config and spins up new worker processes while old
workers finish in-flight requests — no downtime. A `docker compose down && up`
stops the container entirely, dropping every active connection and briefly taking
the site offline. Always `nginx -t` before reloading to avoid loading a broken
config.
</details>

**Next / Related:** [deployment.md](deployment.md) ·
[github-actions.md](github-actions.md) (the `deploy` job) ·
[tutorial.md](tutorial.md) Phase 5.

---

## 9. Monitoring

> Concepts: healthchecks, logs, metrics, dashboards & alerts. Chapter:
> [monitoring.md](monitoring.md).

### 9.1 🟢 Read container health and logs

**Deliverable:** show the `db` and `backend` health status and the last 50 lines
of backend logs.

<details>
<summary>Answer key</summary>

```bash
docker compose ps                       # STATUS column shows (healthy)
docker inspect --format '{{.State.Health.Status}}' example-app-backend-1
docker compose logs --tail=50 backend
```

The backend's `(healthy)` comes from the `HEALTHCHECK` in its Dockerfile (§5.6),
which polls `/api/health`; the db's comes from the `pg_isready` healthcheck in the
Compose file (§5.12).
</details>

### 9.2 🟡 Add a uptime probe against /api/health

**Deliverable:** a small script (cron or loop) that polls `https://example.com/api/health`
and logs failures.

<details>
<summary>Answer key</summary>

```bash
#!/usr/bin/env bash
# uptime-probe.sh
url="https://example.com/api/health"
if ! curl -fsS --max-time 5 "$url" | grep -q '"status":"ok"'; then
  echo "$(date -Is) DOWN $url" >> /var/log/example-app-uptime.log
fi
```

Schedule with `*/1 * * * * /opt/example-app/uptime-probe.sh` in cron. `-f` makes
curl fail on non-2xx, `--max-time` bounds a hung request.
</details>

### 9.3 🔴 Wire up Prometheus + Grafana

**Deliverable:** a Compose addition for Prometheus scraping a metrics endpoint and
Grafana visualizing it, with one alert rule described.

<details>
<summary>Answer key</summary>

Add a metrics endpoint to the backend (e.g. `prometheus-fastapi-instrumentator`
exposing `/metrics`), then add to Compose:

```yaml
  prometheus:
    image: prom/prometheus
    volumes: [./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml]
    networks: [appnet]
  grafana:
    image: grafana/grafana
    ports: ["3000:3000"]
    networks: [appnet]
```

`prometheus.yml` scrapes `backend:8000/metrics`. In Grafana, add Prometheus as a
data source and chart request rate/latency. An alert rule: fire when
`up{job="backend"} == 0` for 2 minutes, or when 5xx rate exceeds a threshold —
delivered to email/Slack. See [monitoring.md](monitoring.md) for the full setup.
</details>

**Next / Related:** [monitoring.md](monitoring.md) ·
[troubleshooting.md](troubleshooting.md).

---

## 10. Troubleshooting

> Concepts: systematic diagnosis — is it the network, the container, the proxy, or
> the db? Chapter: [troubleshooting.md](troubleshooting.md).

### 10.1 🟢 Diagnose a container that exits immediately

**Deliverable:** the commands to find *why* a just-started container is not
running.

<details>
<summary>Answer key</summary>

```bash
docker compose ps -a          # see Exited status and exit code
docker compose logs backend   # the actual error/traceback
```

A non-zero exit code plus the logs almost always reveal the cause (bad import,
missing env var, port conflict). Start from the logs, not from guessing.
</details>

### 10.2 🟡 Fix "Error contacting backend" on the page

**Deliverable:** the diagnosis steps and the most likely root cause when
http://localhost loads but shows the backend error.

<details>
<summary>Answer key</summary>

```bash
docker compose ps                       # is backend healthy?
docker compose logs nginx backend       # nginx 502? backend traceback?
docker compose exec nginx wget -qO- http://backend:8000/api/message
```

The frontend HTML loaded (so Nginx → frontend works), but the `/api/` proxy
failed. Common causes: backend crashed/unhealthy, or the upstream name in
`default.conf` doesn't match the `backend` service. A 502 in nginx logs points at
the backend being down.
</details>

### 10.3 🔴 Resolve a port 80 conflict on the host

**Deliverable:** identify what's holding port 80 and two ways to resolve it
without breaking the canonical Compose file.

<details>
<summary>Answer key</summary>

```bash
sudo lsof -i :80                    # what's listening (often Apache/another nginx)
# Option A: stop the conflicting service
sudo systemctl stop apache2
# Option B: remap only locally via override (don't edit the canonical file):
#   docker-compose.override.yml:
#     services: { nginx: { ports: ["8080:80"] } }
```

On the production server, port 80 must stay free for our Nginx (and 443 for TLS).
Locally, an override mapping to `8080:80` lets you run alongside another web
server while keeping `docker-compose.yml` unchanged.
</details>

**Next / Related:** [troubleshooting.md](troubleshooting.md) ·
[monitoring.md](monitoring.md).

---

## 11. Capstone challenges

These are end-to-end and graded as a whole. Treat them like real tickets: design,
implement, test, ship.

### 11.A 🟡→🔴 Ship a new `/api/time` endpoint end-to-end

**Deliverable:** a new `GET /api/time` endpoint returning the current UTC time,
covered by a test, surfaced in the frontend, and deployed through CI to the
server.

<details>
<summary>Answer key</summary>

1. **Backend** — add to `app/main.py`:

   ```python
   from datetime import datetime, timezone

   @app.get("/api/time")
   def current_time():
       return {"time": datetime.now(timezone.utc).isoformat()}
   ```

2. **Test** — add to `tests/test_main.py`:

   ```python
   def test_time():
       res = client.get("/api/time")
       assert res.status_code == 200
       assert "time" in res.json()
   ```

3. **Frontend** — add a button + fetch to `/api/time` in `index.html`, mirroring
   the existing `load()` pattern (same-origin call through Nginx).

4. **Ship it** — `git push origin main`. CI runs `pytest` (now 3 tests), builds &
   pushes images, and the `deploy` job pulls and restarts on the server.

5. **Verify** — `curl https://example.com/api/time`.

No Nginx change is needed: `/api/time` already matches the existing `location
/api/` rule.
</details>

### 11.B 🔴 Scale the backend to two replicas behind Nginx

**Deliverable:** two backend replicas load-balanced by Nginx, with evidence both
handle traffic, while the db stays a single instance.

<details>
<summary>Answer key</summary>

Run two replicas:

```bash
docker compose up -d --scale backend=2
```

Docker's DNS returns multiple IPs for the `backend` service; Nginx's
`upstream backend_upstream { server backend:8000; }` will balance across them
(round-robin by default once it resolves multiple addresses; for explicit control
use a `resolver` directive or list replicas). Prove it by adding a hostname to the
response, e.g. include `socket.gethostname()` in `/api/health`, then:

```bash
for i in $(seq 6); do curl -s http://localhost/api/health; echo; done
# alternating container hostnames
```

Keep `db` single (stateful) — only the stateless backend scales. `restart:
unless-stopped` keeps replicas healthy. Note: `--scale` and a hardcoded single
upstream is fine for teaching; production would use a service mesh or Nginx
`resolver` for dynamic replica discovery.
</details>

### 11.C 🔴 Add Grafana alerting for the live app

**Deliverable:** Prometheus + Grafana running alongside the app, a dashboard for
request rate and error rate, and an alert that fires when the backend is down.

<details>
<summary>Answer key</summary>

1. Instrument the backend to expose `/metrics` (e.g.
   `prometheus-fastapi-instrumentator`).
2. Add `prometheus` and `grafana` services to Compose on `appnet` (see Exercise
   9.3). Prometheus scrapes `backend:8000/metrics`.
3. In Grafana, add Prometheus as a data source; build panels for
   `rate(http_requests_total[5m])` and the 5xx ratio.
4. Create a **Grafana alert rule**: condition `up{job="backend"} == 0` for 2m →
   notify via a contact point (email/Slack webhook). Optionally also alert when
   `/api/visits` error rate climbs (db unavailable path in `main.py`).
5. Verify by stopping the backend (`docker compose stop backend`) and confirming
   the alert fires, then restart it and confirm it resolves.

Full configuration and screenshots live in [monitoring.md](monitoring.md).
</details>

---

## Next / Related

- [tutorial.md](tutorial.md) — the guided end-to-end build these exercises drill.
- [troubleshooting.md](troubleshooting.md) — when an exercise misbehaves.
- [README.md](README.md) — the module map and recommended chapter order.
- Per-topic depth: [docker.md](docker.md) · [docker-compose.md](docker-compose.md)
  · [github-actions.md](github-actions.md) · [registries.md](registries.md) ·
  [dns.md](dns.md) · [reverse-proxies.md](reverse-proxies.md) ·
  [https.md](https.md) · [deployment.md](deployment.md) ·
  [monitoring.md](monitoring.md).
