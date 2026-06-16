# Docker Compose

In [Docker](docker.md) you learned to build an image and run a single container
with `docker run`. Our example app, though, is **four** containers — a FastAPI
`backend`, a static `frontend`, a Postgres `db`, and an `nginx` reverse proxy —
that must start in the right order, share a network, persist data, and restart
on failure. Doing that by hand, with four long `docker run` commands and a hand-
created network and volume, is tedious and easy to get wrong. **Docker Compose**
is the tool that fixes this.

This chapter assumes you've read [Docker](docker.md). We'll reuse the same
analogies (image = recipe, container = meal, volume = pantry) and build up to the
exact [`docker-compose.yml`](example-app/docker-compose.yml) we ship.

---

## 1. Why Compose exists

> 💡 **Intuition:** Running containers one by one with `docker run` is like
> plating a four-course dinner by shouting separate instructions for each dish,
> in the right order, every single time. Compose is the **single menu card**: you
> write down all the dishes, their order, and how they share the kitchen *once*,
> then say "serve it" — and everything comes out together.

Without Compose, bringing up our app means something like:

```bash
docker network create appnet
docker volume create db_data
docker run -d --name db --network appnet -v db_data:/var/lib/postgresql/data \
  -e POSTGRES_USER=app -e POSTGRES_PASSWORD=app -e POSTGRES_DB=app postgres:16-alpine
docker run -d --name backend --network appnet \
  -e DATABASE_URL=postgresql://app:app@db:5432/app example-app-backend
docker run -d --name frontend --network appnet example-app-frontend
docker run -d --name nginx --network appnet -p 80:80 example-app-nginx
```

Five commands, in order, with flags you have to remember exactly — and you have
to *tear it all down* in reverse by hand too. **Docker Compose** lets you
describe that entire setup declaratively in one YAML file (`docker-compose.yml`)
and manage it with a handful of commands. You say *what* you want; Compose
figures out *how* to make it so.

> A note on naming: the modern command is **`docker compose`** (two words, a
> built-in subcommand of Docker). The old standalone tool was `docker-compose`
> (hyphen, v1). They're mostly compatible; throughout this module we use the
> modern `docker compose`.

---

## 2. The shape of a Compose file

A Compose file is YAML with a few **top-level keys**. The three you'll use are:

- `services:` — the containers that make up your app, each defined as a named
  block. This is the heart of the file.
- `volumes:` — named volumes Compose should create and manage (our `db_data`).
- `networks:` — networks Compose should create (our `appnet`).

Each service under `services:` is a name (e.g. `backend`) followed by **per-
service keys** that describe how to build/run that one container. We'll meet each
key by building the file up in three stages.

---

## 3. Stage 1 — a tiny one-service Compose file

Start as small as possible: just the backend.

```yaml
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
```

Line by line:

- `services:` — top-level key; everything indented under it is a container.
- `backend:` — the service name. It's also the container's DNS name on the
  network (we'll use that in Stage 2). Pick it deliberately.
- `build: ./backend` — instead of pulling a prebuilt image, **build** one from
  the Dockerfile in the `./backend` directory (the build context, exactly like
  the `.` argument to `docker build` in [Docker](docker.md) §9).
- `ports:` — publish ports, the Compose equivalent of `docker run -p`.
- `- "8000:8000"` — map `HOST:CONTAINER`. Host 8000 → container 8000.

Run it:

```bash
docker compose up -d
```

Compose builds the image, creates a default network, starts the container, and
returns. One command replaces the whole `docker run` incantation. `docker
compose down` tears it all back down.

---

## 4. Stage 2 — two services that talk to each other

Now add the database and connect the backend to it. This is where Compose starts
to earn its keep.

```yaml
services:
  backend:
    build: ./backend
    image: ghcr.io/chrisw09/example-app-backend:latest
    environment:
      DATABASE_URL: postgresql://app:app@db:5432/app
    depends_on:
      db:
        condition: service_healthy
    networks: [appnet]

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: app
      POSTGRES_DB: app
    volumes:
      - db_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks: [appnet]

volumes:
  db_data:

networks:
  appnet:
```

New keys, explained:

- `image: ghcr.io/chrisw09/example-app-backend:latest` — when used *alongside*
  `build`, this names the image Compose produces (and would push/pull). Locally
  Compose builds it and tags it with this name; in production we skip the build
  and just *pull* this exact image. See [Registries](registries.md).
- `environment:` — inject environment variables into the container (like `-e`).
  Here `DATABASE_URL` tells the backend how to reach Postgres. Look closely at
  the host portion: `@db:5432`. **`db` is the service name**, and Docker's
  internal DNS on `appnet` resolves it to the database container's IP. This is
  the "container DNS by service name" feature from [Docker](docker.md) §7 — it's
  why we never hard-code an IP.
- `depends_on:` — declare start-order dependencies. `backend` depends on `db`.
- `condition: service_healthy` — and crucially, don't just wait for `db` to
  *start*, wait for it to report **healthy** (per its `healthcheck`). Without
  this condition, `depends_on` only waits for the container to be *created*, not
  for Postgres to actually be ready to accept connections — a classic race.
- `db.healthcheck:` — how Compose decides the database is healthy:
  - `test: ["CMD-SHELL", "pg_isready -U app"]` — run `pg_isready` (Postgres's
    own "are you accepting connections?" probe) for user `app`. `CMD-SHELL`
    means "run this string in a shell."
  - `interval: 10s` — check every 10 seconds.
  - `timeout: 5s` — each check has 5 seconds to answer.
  - `retries: 5` — mark unhealthy only after 5 consecutive failures.
- `volumes: - db_data:/var/lib/postgresql/data` — mount the named volume
  `db_data` (the **pantry**) at Postgres's data directory so the data survives
  container restarts ([Docker](docker.md) §8).
- `networks: [appnet]` — attach the service to the `appnet` network. (`[appnet]`
  is YAML's inline-list shorthand for a one-item list.)
- `volumes: db_data:` (top level) — declare the named volume so Compose creates
  and manages it.
- `networks: appnet:` (top level) — declare the network so Compose creates it.

The start sequence Compose now enforces:

```mermaid
flowchart LR
  DB[(db starts)] --> HC{healthcheck<br/>pg_isready}
  HC -->|healthy| BE[backend starts]
  HC -.->|not yet| HC
```

The backend literally will not start until the database answers `pg_isready`.
That eliminates the most common startup crash in multi-container apps.

---

## 5. Stage 3 — the full four-service file we ship

Here is the complete, canonical
[`docker-compose.yml`](example-app/docker-compose.yml), quoted **verbatim**:

```yaml
# Compose file for local dev AND as the production template.
# Locally: `docker compose up --build`.
# In production we PULL prebuilt images (see deployment.md) — the `image:`
# tags below are what CI pushes and what the server pulls.

services:
  backend:
    build: ./backend
    image: ghcr.io/chrisw09/example-app-backend:latest
    environment:
      DATABASE_URL: postgresql://app:app@db:5432/app
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
    networks: [appnet]

  frontend:
    build: ./frontend
    image: ghcr.io/chrisw09/example-app-frontend:latest
    restart: unless-stopped
    networks: [appnet]

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: app
      POSTGRES_DB: app
    volumes:
      - db_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped
    networks: [appnet]

  nginx:
    build: ./nginx
    image: ghcr.io/chrisw09/example-app-nginx:latest
    ports:
      - "80:80"
    depends_on:
      - backend
      - frontend
    restart: unless-stopped
    networks: [appnet]

volumes:
  db_data:

networks:
  appnet:
```

The top comment is doing real work: this *one* file serves both **local
development** (`docker compose up --build` builds everything from source) and as
the **production template** (the server pulls the `image:` tags instead of
building). Same file, two modes.

We've met most keys in Stage 2. Here's what's new across the four services:

- **`backend`** — unchanged from Stage 2, plus `restart: unless-stopped`
  (explained below). Builds from `./backend`, tagged
  `ghcr.io/chrisw09/example-app-backend:latest`, gets `DATABASE_URL`, waits for
  `db` to be healthy.
- **`frontend`** — builds from `./frontend`, tagged `…-frontend:latest`. It's the
  static `index.html` served by a tiny Nginx ([Docker](docker.md)'s frontend
  Dockerfile). No `ports:` — it is **not** published to the host directly;
  visitors reach it *through* the `nginx` reverse proxy. It just sits on `appnet`
  listening on its internal port 80.
- **`db`** — identical to Stage 2: `postgres:16-alpine`, the three `POSTGRES_*`
  variables creating the `app` user/password/database, the `db_data` volume, and
  the `pg_isready` healthcheck that gates the backend.
- **`nginx`** — builds from `./nginx`, tagged `…-nginx:latest`. This is the one
  service with a **published port**: `ports: - "80:80"` maps host 80 to the
  container's 80, making it the single public entrance. Its `depends_on:` is the
  *list* form (`- backend` / `- frontend`) — note this waits only for those
  containers to *start*, not to be healthy (they have no compose-level
  healthcheck here), which is fine because Nginx tolerates a brief upstream
  hiccup and retries.

The one new per-service key, used on every service:

- `restart: unless-stopped` — Docker's **restart policy**. If the container
  crashes or the server reboots, Docker automatically restarts it — *unless* you
  explicitly stopped it yourself (`docker compose stop`). This is what keeps the
  app self-healing in production. Other values: `no` (default, never restart),
  `on-failure` (only on a non-zero exit), `always` (restart even after a manual
  stop, on daemon start).

> ⚠️ **Common mistake:** Publishing ports you don't need. Only `nginx` has
> `ports:`. If you also published the backend (`-p 8000:8000`) or Postgres
> (`-p 5432:5432`), you'd expose them to the whole internet, bypassing the proxy
> and exposing your database. Keep internal services internal — they reach each
> other over `appnet` without any published port.

---

## 6. How containers reach each other over `appnet`

All four services declare `networks: [appnet]`, so Compose puts them on one
user-defined bridge network and runs an internal DNS server for it. The result
is the **service name = hostname** rule:

```mermaid
flowchart TD
  subgraph appnet["appnet (internal bridge network)"]
    NGINX[nginx :80] -->|"/api/ → backend:8000"| BACKEND[backend :8000]
    NGINX -->|"/ → frontend:80"| FRONTEND[frontend :80]
    BACKEND -->|"db:5432"| DB[(db :5432)]
  end
  HOST([Host / Internet]) -->|"published :80"| NGINX
```

Trace a request:

1. A browser hits the host on port 80. Only `nginx` publishes a port, so the
   request lands there.
2. Nginx looks at the path. `/api/...` is proxied to `backend:8000`; everything
   else to `frontend:80`. It finds those hosts via Docker's DNS — `backend` and
   `frontend` resolve to the right container IPs on `appnet`.
3. The backend, needing data, connects to `db:5432` — again, `db` resolved by
   name to the Postgres container.

Nobody hard-codes an IP. If a container restarts and gets a new IP, the name
still resolves. This name-based wiring is exactly what the Nginx config relies on
(`upstream backend_upstream { server backend:8000; }`) — see
[Reverse proxies](reverse-proxies.md).

> ⚠️ **Common mistake:** Using `localhost` to reach another service. Inside the
> `backend` container, `localhost:5432` is the backend itself, not the database.
> The Postgres host is `db`. (Same trap as [Docker](docker.md) §7.)

---

## 7. The key Compose commands

All commands run from the directory containing `docker-compose.yml`.

### `docker compose up -d` — create and start everything

```bash
docker compose up -d
```

- `up` — create the network, volumes, and containers defined in the file, and
  start them in dependency order (`db` healthy → `backend`; `backend`/`frontend`
  started → `nginx`).
- `-d` — **detached**: run in the background and return your prompt (same meaning
  as `docker run -d`). Without it, Compose streams all containers' logs to your
  terminal and holds it.

### `docker compose up --build` — rebuild images first

```bash
docker compose up -d --build
```

- `--build` — force a rebuild of every service that has a `build:` key *before*
  starting. Use this in local development whenever you've changed source or a
  Dockerfile; otherwise Compose reuses the existing image and your changes won't
  appear.

### `docker compose down` — stop and remove everything

```bash
docker compose down          # remove containers + network (keeps named volumes)
docker compose down -v       # also remove named volumes (DELETES db_data!)
```

- `down` — the inverse of `up`: stop and remove the containers and the network.
  By default it **keeps** named volumes, so your database survives.
- `-v` — *also* delete named volumes. This wipes `db_data` — every row in
  Postgres is gone. Useful to reset a dev database; catastrophic in production.

### `docker compose logs -f` — view logs across services

```bash
docker compose logs -f
docker compose logs -f backend
```

- `logs` — show the combined, color-coded logs of all services (or just the one
  you name).
- `-f` — **follow** the stream live (like `docker logs -f`). Ctrl-C stops
  following without stopping the containers.

### `docker compose ps` — list this project's containers

```bash
docker compose ps
```

Shows the status of the containers Compose manages for *this* project — name,
state, health, and published ports. The Compose-scoped cousin of `docker ps`.

### `docker compose pull` — fetch prebuilt images

```bash
docker compose pull
```

Pulls the images named in each `image:` key from their registry — without
building. This is the **production** path: the server doesn't build from source;
CI already pushed the images to GHCR, and the server just pulls the latest tags.
This is the first half of our deploy step.

### `docker compose exec` — run a command in a running service

```bash
docker compose exec db psql -U app -d app
docker compose exec backend sh
```

- `exec` — run a command inside an already-running service container (like
  `docker exec`). Address it by **service name**, not container name. The first
  example opens a `psql` shell into the database; the second drops you into a
  shell in the backend. Add `-it`-style interactivity automatically for shells;
  Compose allocates a TTY when appropriate.

The production deploy (from the CI workflow) is literally just two of these,
preceded by a `cd` into the server's `/opt/example-app`:

```bash
docker compose pull      # get the freshly built images from GHCR
docker compose up -d     # recreate any containers whose image changed
```

Compose is smart enough to recreate only the services whose image actually
changed, leaving the rest running. See [Deployment](deployment.md) for the full
SSH-driven flow.

---

## 8. Best practices and common mistakes

> ✅ **Production best practices:**
> - **One file, two modes.** Keep `build:` *and* `image:` so the same file builds
>   locally and pulls in production. Build with `--build` in dev; `pull` + `up -d`
>   on the server.
> - **Gate dependents on health, not just start.** Use `depends_on` with
>   `condition: service_healthy` (plus a real `healthcheck`) for stateful
>   services like databases.
> - **Publish only what must be public.** Here, only `nginx`. Everything else
>   talks over `appnet` with no host port.
> - **Set `restart: unless-stopped`** on long-running services so they survive
>   crashes and reboots.
> - **Persist state on named volumes** (`db_data`) and never `down -v` in prod.

> ⚠️ **Common mistakes (consolidated):**
> - **Assuming `depends_on` waits for readiness.** Plain `depends_on` waits only
>   for the container to *start*. Postgres can be "started" but still
>   initializing; without `condition: service_healthy` the backend connects too
>   early and crashes. (The list-form `depends_on` under `nginx` has *no*
>   condition — it only orders startup.)
> - **Putting secrets in the Compose file.** Our demo hard-codes `app/app` for
>   teaching, but real passwords and API keys belong in environment files or a
>   secrets manager, never committed in `docker-compose.yml`.
> - **Port clashes.** Two services (or another program on the host) both binding
>   host port 80 fails with "address already in use." Only one thing can own a
>   host port at a time; change the host side (`"8080:80"`) or stop the
>   conflicting process.
> - **Forgetting `--build`.** You edit code, run `docker compose up -d`, and see
>   no change — because Compose reused the old image. Add `--build`.

> 🔧 **Troubleshooting:** `docker compose ps` shows the backend restarting in a
> loop? Run `docker compose logs backend`. If it's failing to connect to
> Postgres, confirm `db` is `healthy` (`docker compose ps` shows health) and that
> `DATABASE_URL` uses the host `db`, not `localhost`.

---

## 9. Exercises

**Exercise 1.** In the full file, why does `backend` use `depends_on` with
`condition: service_healthy` while `nginx` uses the plain list form
(`- backend`, `- frontend`)?

<details>
<summary>Answer</summary>

The backend *must not start querying Postgres until Postgres is truly ready to
accept connections* — "started" isn't enough, so it waits for the `db`
healthcheck (`pg_isready`) to pass. Nginx, by contrast, only needs its upstreams
to *exist*; it tolerates a brief moment where a backend isn't answering yet and
simply retries the request, so ordering (start `backend`/`frontend` first) is
sufficient and no health condition is required.
</details>

**Exercise 2.** A teammate runs `docker compose down -v` on the production server
to "restart cleanly." What just happened, and how should they have restarted?

<details>
<summary>Answer</summary>

`-v` deletes named volumes, so `db_data` was wiped — **the entire database is
gone**. To restart without data loss they should have used `docker compose
restart`, or `docker compose down` (no `-v`) followed by `docker compose up -d`.
Reserve `down -v` for throwaway dev environments.
</details>

**Exercise 3.** The backend logs show
`could not translate host name "localhost" to address`. The `DATABASE_URL` reads
`postgresql://app:app@localhost:5432/app`. What's wrong and what's the fix?

<details>
<summary>Answer</summary>

Inside the backend container, `localhost` means the backend itself, which isn't
running Postgres. The database is a *separate* container reachable by its service
name on `appnet`. Change the host to `db`:
`postgresql://app:app@db:5432/app` — which is exactly what the canonical file
uses.
</details>

**Exercise 4.** You're on the production server and CI just pushed new images to
GHCR. Which two Compose commands bring the new version live, and why is
`--build` *not* used?

<details>
<summary>Answer</summary>

```bash
docker compose pull
docker compose up -d
```

`pull` downloads the freshly built images CI pushed to GHCR; `up -d` recreates
only the containers whose image changed. `--build` is not used because the server
doesn't build from source — building already happened in CI. The server's job is
just to fetch and run the prebuilt images.
</details>

---

## Next / Related

- **[Docker](docker.md)** — the single-container fundamentals (images, layers,
  volumes, networking, `docker run`) this chapter builds on.
- **[Deployment](deployment.md)** — how `docker compose pull && up -d` runs on
  the Ubuntu server over SSH to ship a new release.
- **[Reverse proxies](reverse-proxies.md)** — how the `nginx` service routes
  `/api/` to `backend:8000` and `/` to `frontend:80` over `appnet`.
