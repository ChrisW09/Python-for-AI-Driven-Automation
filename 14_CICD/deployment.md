# Production Deployment

This chapter is where everything in the module comes together. So far you have
learned how to package the app into [Docker](docker.md) images, how to wire the
services together with [Docker Compose](docker-compose.md), how to automate
builds with [GitHub Actions](github-actions.md), and how to store images in a
[registry](registries.md). Now we will take that same app — the canonical
[example app](example-app/docker-compose.yml) — and ship it to a real server on
the public internet so that anyone in the world can open `https://example.com`
and use it.

We will build this up from first principles. If you have never logged into a
server before, that is fine: we will go slowly and define every term the first
time it appears.

---

## 1. The big picture: what "deployment" actually means

> 💡 **Intuition:** Up to now you have been *cooking in your own kitchen* —
> running the app on your laptop with `docker compose up`. **Deployment** is the
> act of moving that exact, tested meal into a **restaurant kitchen** (an
> always-on Ubuntu server) so that paying customers can order it any time, even
> while you are asleep.

In our module's vocabulary:

- **CI (Continuous Integration)** is the *quality-control line*: every change is
  tested automatically before it is allowed through.
- **CD (Continuous Deployment/Delivery)** is the *delivery truck*: once a change
  passes quality control, it is automatically shipped to the customers.
- The **Ubuntu server** is the *restaurant kitchen* — a computer that is always
  powered on, has a public IP address, and runs your containers 24/7.

The goal of this chapter is a fully automated path from "I typed `git push`" to
"the new version is live at `https://example.com`" with **no manual steps** in
between. That path is the pipeline.

---

## 2. The canonical pipeline, step by step

Here is the end-to-end pipeline we are building. This is the same diagram you
saw in the [README](README.md) and [tutorial](tutorial.md) — it is the
backbone of the whole module.

```mermaid
flowchart LR
  A[Developer] --> B[git push to GitHub]
  B --> C[GitHub Actions]
  C --> D[Run tests]
  D --> E[Build Docker images]
  E --> F[Push to GHCR registry]
  F --> G[Ubuntu server]
  G --> H[docker compose pull and up -d]
  H --> I[Live application]
```

Let us walk through **every single arrow**, because understanding *why* each
step exists is what turns you from someone who copies commands into someone who
can debug them.

### Step 1 — Developer

This is you, on your laptop, editing `app/main.py` or `index.html`. Nothing is
live yet. The only thing that matters at this stage is that you commit your work
to Git, exactly as you already do in normal development.

### Step 2 — `git push` to GitHub

When you run `git push`, your local commits travel to the shared repository on
GitHub. This is the **trigger**: GitHub watches the repository, and a push to
the `main` branch is the event that starts the assembly line. (Look again at the
top of the workflow in §5.13: `on: push: branches: [main]`.)

> 💡 **Intuition:** Pushing to `main` is like placing a finished order on the
> conveyor belt of the **automated factory**. From here on, no human touches it.

### Step 3 — GitHub Actions

**GitHub Actions** is GitHub's built-in automation system — the *automated
factory / assembly line*. When the push arrives, GitHub spins up a fresh,
disposable virtual machine (called a **runner**) and executes the steps defined
in the workflow file. A clean machine every time means builds are reproducible:
nothing lingers from a previous run.

### Step 4 — Run tests (the quality-control line)

The very first job is `test`. It installs the backend's dependencies and runs
`pytest`. If a single test fails, the pipeline **stops here** and never builds or
deploys anything. This is the whole point of CI: a broken change can never reach
production because it is caught on the quality-control line first.

In our app, `test_main.py` checks `/api/health` and `/api/message`. If you
accidentally rename an endpoint, those tests go red and deployment is blocked.

### Step 5 — Build Docker images (freeze the recipes)

Once tests pass, the `build-and-push` job builds three Docker images — one each
for `backend`, `frontend`, and `nginx`.

> 💡 **Intuition:** A Docker **image** is a **recipe**: frozen, immutable
> instructions for producing a running program. Building the image is writing
> the recipe card down so it can be reproduced identically anywhere.

Crucially, the image is built **once**, in the factory. The exact same bytes
that were tested are the bytes that will run in production. You never rebuild on
the server — that would risk producing a *different* meal from the one you
approved.

### Step 6 — Push to GHCR (store the recipe in the warehouse)

The freshly built images are pushed to **GHCR (GitHub Container Registry)** — a
*warehouse / app store* for recipes. Our images are named:

```
ghcr.io/chrisw09/example-app-backend
ghcr.io/chrisw09/example-app-frontend
ghcr.io/chrisw09/example-app-nginx
```

> Note the lowercase `chrisw09`. GHCR requires the owner segment to be
> lowercase, even though the GitHub account is `ChrisW09`. In generic examples
> the form is `ghcr.io/<owner>/example-app-backend`.

Each image is pushed with **two tags**: `:latest` (a moving pointer to the newest
build) and `:${{ github.sha }}` (the exact Git commit hash). The commit-hash tag
is your time machine — it lets you roll back to any previous build precisely. We
will use it in §9.

### Step 7 — Ubuntu server

The server is a rented Linux computer (from any cloud provider) that is always
on and reachable at the public IP `203.0.113.10`. It is the *restaurant kitchen*.
It does **not** build anything. Its only job is to pull the prebuilt images from
the warehouse and run them.

### Step 8 — `docker compose pull` and `up -d`

The pipeline connects to the server over **SSH (Secure Shell** — an encrypted
remote login**)** and runs two commands in `/opt/example-app`:

- `docker compose pull` — download the newest images from GHCR.
- `docker compose up -d` — (re)start the containers in the background
  (**`-d`** = *detached*), replacing only the containers whose image changed.

### Step 9 — Live application

The containers are running, Nginx is listening on ports 80/443, and visitors at
`https://example.com` see the new version. The loop is closed.

---

## 3. Why "build once, pull everywhere" matters

A beginner's instinct is often: "Why not just `git pull` on the server and run
`docker compose up --build`?" It would work — and it is a classic trap.

> ⚠️ **Common mistake:** Building images on the production server. The build
> would (a) consume CPU/RAM that should serve users, (b) pull build-time
> dependencies onto the production box, and (c) potentially produce a *different*
> image than the one your tests validated, because the server's environment
> differs from the CI runner. The image you ship must be the image you tested,
> byte-for-byte.

> ✅ **Best practice:** Treat images as immutable artifacts. CI builds and tests
> them once; every environment (staging, production) *pulls* the identical image
> by tag. This is the foundation of reliable, reproducible deployments.

---

## 4. Ubuntu 24.04 server setup runbook

Before any automation can connect, the server has to exist and be hardened. This
section is a complete, copy-along runbook for a fresh Ubuntu 24.04 LTS box at
`203.0.113.10`. Do this **once**, by hand, the first time you provision the
machine.

> 💡 **Intuition:** We are setting up the *restaurant kitchen* before opening
> day: hiring a trusted manager (a non-root user), giving them a key instead of a
> password, locking the back door (firewall), and installing the cooking
> equipment (Docker).

### 4.1 First login as root

Your cloud provider gives you initial access — usually as the `root` user (the
all-powerful administrator) via either a password or a pre-installed SSH key.
From your laptop:

```bash
ssh root@203.0.113.10
```

- `ssh` — the Secure Shell client.
- `root@203.0.113.10` — log in as user `root` on the host at that IP.

You are now inside the server. Everything below runs *on the server* unless we
say otherwise.

### 4.2 Create a non-root sudo user

Running everything as `root` is dangerous: one typo can wipe the machine, and
any compromised process has total control. We create a normal user who can
*elevate* to admin only when needed via `sudo`.

```bash
adduser deploy
usermod -aG sudo deploy
```

- `adduser deploy` — creates a user named `deploy` and prompts for a password and
  some optional details. (You may pick any name; we use `deploy` and will reuse
  it as `SERVER_USER` later.)
- `usermod -aG sudo deploy` — **a**ppends (`-a`) the user to the **g**roup (`-G`)
  `sudo`, granting the ability to run admin commands by prefixing them with
  `sudo`.

> ⚠️ **Common mistake:** Forgetting the `-a` in `usermod -aG`. Without it,
> `usermod -G sudo deploy` *replaces* all of the user's groups with just `sudo`,
> silently removing them from other groups. Always include `-a`.

### 4.3 Set up SSH key login for the new user

A **password** can be guessed or brute-forced. An **SSH key pair** cannot
practically be — it is a private key you keep secret and a public key you place
on the server. Generate a key **on your laptop** (not the server) if you do not
already have one:

```bash
# On your LAPTOP:
ssh-keygen -t ed25519 -C "deploy@example.com"
```

- `-t ed25519` — use the modern, fast, secure Ed25519 key type.
- `-C "…"` — a comment to help you recognize the key later.

This creates `~/.ssh/id_ed25519` (private — never share) and
`~/.ssh/id_ed25519.pub` (public — safe to distribute). Copy the public key to
the server's `deploy` user:

```bash
# On your LAPTOP:
ssh-copy-id deploy@203.0.113.10
```

`ssh-copy-id` appends your public key to `/home/deploy/.ssh/authorized_keys` on
the server. Now test it — you should log in **without a password**:

```bash
ssh deploy@203.0.113.10
```

If that works, you have key-based login. Keep this terminal open while you do the
next step, so you do not lock yourself out.

### 4.4 Harden the SSH daemon

The **SSH daemon** (`sshd`) is the program on the server that accepts logins. We
now forbid password logins and root logins entirely, so only key-holders can get
in. Edit the config:

```bash
sudo nano /etc/ssh/sshd_config
```

Ensure these three lines are set (uncomment and edit as needed):

```text
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
```

- `PermitRootLogin no` — nobody can SSH in directly as `root`.
- `PasswordAuthentication no` — passwords are rejected; keys only.
- `PubkeyAuthentication yes` — key-based login is allowed.

Apply the change by restarting the daemon:

```bash
sudo systemctl restart ssh
```

> ⚠️ **Common mistake:** Disabling password auth *before* confirming your key
> works. If your key is misconfigured and passwords are off, you are locked out
> permanently. Always keep one working session open and test a *second* login in
> a new terminal before closing the first.

### 4.5 Configure the firewall with `ufw`

A **firewall** controls which network ports accept connections. **`ufw`
(Uncomplicated Firewall)** is Ubuntu's friendly front-end. We open only the
three ports we need:

```bash
sudo ufw allow 22/tcp     # SSH (so we don't lock ourselves out)
sudo ufw allow 80/tcp     # HTTP
sudo ufw allow 443/tcp    # HTTPS
sudo ufw enable
```

- Port **22** — SSH remote login. Open it *first* and *before enabling* the
  firewall, or you lock yourself out.
- Port **80** — HTTP. Nginx listens here; also needed for Let's Encrypt
  certificate issuance (see [https.md](https.md)).
- Port **443** — HTTPS, the encrypted web port.
- `sudo ufw enable` — turns the firewall on. Confirm with `sudo ufw status`.

Postgres (5432) is deliberately **not** opened — the database is only ever
reached *inside* the Docker `appnet` network, never from the public internet.

### 4.6 Install Docker Engine and the Compose plugin

We install Docker from Docker's **official apt repository** (not Ubuntu's older
packaged version), so we get current releases and the v2 `compose` plugin.

```bash
# 1. Remove any old/conflicting packages
sudo apt-get remove -y docker docker-engine docker.io containerd runc 2>/dev/null

# 2. Install prerequisites and add Docker's GPG key
sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# 3. Add the Docker apt repository for Ubuntu 24.04
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 4. Install Docker Engine + CLI + Compose plugin
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io \
  docker-buildx-plugin docker-compose-plugin
```

Line notes:

- The **GPG key** lets apt verify that packages genuinely come from Docker.
- `$(. /etc/os-release && echo "$VERSION_CODENAME")` resolves to `noble`, the
  codename for Ubuntu 24.04 — the repo line is built dynamically so it is
  correct on any release.
- `docker-compose-plugin` gives you the modern **`docker compose`** (v2, a
  space), not the legacy `docker-compose` (a hyphen).

Let the `deploy` user run Docker without `sudo`:

```bash
sudo usermod -aG docker deploy
```

Log out and back in for the group change to take effect, then verify:

```bash
docker --version
docker compose version
docker run --rm hello-world
```

> ✅ **Best practice:** Enable Docker on boot so containers come back after a
> server reboot: `sudo systemctl enable docker`. Our compose services also use
> `restart: unless-stopped`, which restarts containers automatically unless you
> explicitly stopped them.

### 4.7 Create the deployment directory

By module convention, the app lives in `/opt/example-app` on the server. `/opt`
is the standard Linux location for self-contained, optional application
software.

```bash
sudo mkdir -p /opt/example-app
sudo chown deploy:deploy /opt/example-app
```

We `chown` it to `deploy` so the deployment can write there without `sudo`.

---

## 5. The production `docker-compose.yml` (pull, don't build)

Locally, our [example-app/docker-compose.yml](example-app/docker-compose.yml)
has both `build:` and `image:` keys so `docker compose up --build` can build from
source. On the **server**, we never build — so we use a **production variant**
that drops every `build:` line and keeps only the `image:` tags. The server pulls
exactly those tags from GHCR.

Create `/opt/example-app/docker-compose.yml` on the server with this content:

```yaml
# Production compose file for /opt/example-app on 203.0.113.10.
# No `build:` keys — the server ONLY pulls prebuilt images from GHCR.

services:
  backend:
    image: ghcr.io/chrisw09/example-app-backend:latest
    environment:
      DATABASE_URL: postgresql://app:app@db:5432/app
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
    networks: [appnet]

  frontend:
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

What changed versus the local file:

- **Every `build: ./…` line is gone.** With no build context, `docker compose
  pull` and `up -d` resolve services purely by their `image:` tag.
- **Everything else is identical** — same service names (`backend`, `frontend`,
  `db`, `nginx`), same ports, same `appnet` network, same `db_data` volume, same
  db creds (`app`/`app`/`app`), same `DATABASE_URL`, same Postgres healthcheck.
  Consistency between local and prod is exactly what makes "it works on my
  machine" become "it works in production."

> ⚠️ **Common mistake:** Leaving `build:` keys in the production file. If the
> server has no source code (it should not!), `docker compose up` will fail
> trying to build, or — worse — silently build a stale local image instead of
> pulling the tested one.

> ✅ **Best practice:** Pin to a specific commit tag in production
> (`…-backend:${SHA}`) rather than `:latest`, so a deploy is an explicit,
> auditable change. We will see the rollback payoff of this in §9. For a first
> deployment, `:latest` is fine to keep things simple.

---

## 6. Log in to GHCR on the server and pull

Our GHCR images are **private by default**, so the server must authenticate
before it can pull them. On the server, log in once:

```bash
echo "$GHCR_TOKEN" | docker login ghcr.io -u chrisw09 --password-stdin
```

- `GHCR_TOKEN` is a **Personal Access Token (PAT)** created on GitHub with the
  `read:packages` scope. Generate it under GitHub → Settings → Developer settings
  → Personal access tokens. (The CI pipeline uses the automatic `GITHUB_TOKEN`
  instead — see §8 — but a human/server login needs a PAT.)
- `--password-stdin` reads the token from standard input instead of the command
  line, so the secret never lands in your shell history.

Docker stores the credentials in `~/.docker/config.json`, so future pulls just
work. Now do the first manual deploy to prove the whole stack runs:

```bash
cd /opt/example-app
docker compose pull
docker compose up -d
docker compose ps
```

`docker compose ps` should show all four services `running`, with `db` and
`backend` reporting `healthy` once their health checks pass. Open
`http://203.0.113.10/` in a browser — you should see the Example App page, and
clicking **Refresh** should show "Hello from FastAPI" fetched through Nginx.

> ✅ **Best practice:** Make the server's GHCR images **public** if they contain
> no secrets, which removes the need for server-side login entirely. For private
> images, prefer a token with the *minimum* scope (`read:packages`) and rotate it
> periodically.

Here is the server-side pull/up sequence as a diagram:

```mermaid
sequenceDiagram
    participant CI as GitHub Actions (deploy job)
    participant S as Ubuntu server /opt/example-app
    participant R as GHCR registry
    participant C as Containers
    CI->>S: SSH in, run script
    S->>R: docker compose pull (auth via stored creds)
    R-->>S: backend / frontend / nginx images
    S->>C: docker compose up -d
    C->>C: recreate only changed containers
    S->>S: docker image prune -f
    Note over C: nginx serves :80/:443 → app is live
```

---

## 7. Automating the deploy: how the GitHub Actions `deploy` job works

Now we automate everything in §6 so a `git push` does it for us. Recall the
`deploy` job from the workflow (§5.13):

```yaml
  deploy:
    needs: build-and-push
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy over SSH
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          script: |
            cd /opt/example-app
            docker compose pull
            docker compose up -d
            docker image prune -f
```

Line by line:

- `needs: build-and-push` — this job runs **only after** images are built and
  pushed. The dependency chain is `test → build-and-push → deploy`; a failure
  anywhere upstream cancels the deploy.
- `if: github.ref == 'refs/heads/main'` — only deploy on pushes to `main`, never
  on pull-request builds. You do not want every PR redeploying production.
- `appleboy/ssh-action@v1` — a community action that opens an SSH connection and
  runs a script on the remote host. It is the *delivery truck* arriving at the
  kitchen door.
- `host`, `username`, `key` — pulled from **GitHub Secrets** (never hard-coded).
- `script:` — the exact commands run on the server: pull the new images, restart
  changed containers, and prune dangling old images to reclaim disk.

### 7.1 The three secrets you must set

In your GitHub repository, go to **Settings → Secrets and variables → Actions →
New repository secret**, and create exactly these three:

| Secret name      | Value                                                          |
|------------------|----------------------------------------------------------------|
| `SERVER_HOST`    | `203.0.113.10` (the server's public IP or `example.com`)       |
| `SERVER_USER`    | `deploy` (the non-root sudo user you created in §4.2)          |
| `SERVER_SSH_KEY` | The **private** key whose public half is in the server's `authorized_keys` |

For `SERVER_SSH_KEY`, paste the *entire* private key file, including the
`-----BEGIN OPENSSH PRIVATE KEY-----` and `-----END …-----` lines. It is wise to
generate a **dedicated deploy key** for CI rather than reusing your personal one:

```bash
# On your laptop: a CI-only key, no passphrase (CI can't type one)
ssh-keygen -t ed25519 -f ci_deploy_key -C "github-actions-deploy"
ssh-copy-id -i ci_deploy_key.pub deploy@203.0.113.10
# Then paste the contents of ci_deploy_key (the private file) into SERVER_SSH_KEY
```

> ⚠️ **Common mistake:** Pasting the **public** key (`.pub`) into
> `SERVER_SSH_KEY`. The action needs the *private* key; the public half lives on
> the server. Also: a passphrase-protected key will hang CI, because the runner
> cannot type the passphrase — use a passphrase-less key dedicated to deployment.

> ✅ **Best practice:** Use a dedicated, passphrase-less deploy key per project,
> and remove it from the server's `authorized_keys` if the project is retired.
> Never commit private keys to the repository.

### 7.2 The repo-root workflow caveat

> ⚠️ **Important caveat:** GitHub only runs workflows located at the
> **repository root** in `.github/workflows/`. For teaching and co-location, this
> module keeps the workflow at
> `14_CICD/example-app/.github/workflows/ci-cd.yml`.
> GitHub will **not** discover it there. To actually run the pipeline, copy or
> move that file to the repo-root `.github/workflows/ci-cd.yml`. The workflow's
> `APP_DIR` environment variable already points at the module path
> (`14_CICD/example-app`), so all the build/test steps
> resolve correctly once the file is relocated.

---

## 8. CI authentication vs. server authentication

It is worth being precise about the two different logins to GHCR, because
beginners often conflate them:

- **In CI**, the `build-and-push` job logs in with `${{ secrets.GITHUB_TOKEN }}`
  — an automatic, short-lived token GitHub injects into every workflow run. The
  `permissions: packages: write` block grants it push access. You never create
  this token yourself.
- **On the server**, the `deploy` job's `docker compose pull` uses the
  credentials you stored with `docker login` in §6 (a `read:packages` PAT). The
  runner SSHes in *as the server user*, so it inherits the server's stored Docker
  credentials.

In short: CI **pushes** with `GITHUB_TOKEN`; the server **pulls** with a PAT it
remembers from a one-time `docker login`.

---

## 9. Rollbacks: deploying a previous `:sha` tag

Things break. The mark of a production-ready setup is not "never breaking" but
"recovering in seconds." Because CI tags every image with the commit hash
(`…-backend:${{ github.sha }}`), rolling back is just deploying an older tag.

Suppose commit `9f2c1a` is bad and the previous good commit was `1b7d4e`. On the
server (or by editing the compose file to pin tags):

```bash
cd /opt/example-app
export TAG=1b7d4e
docker compose pull
docker compose up -d
```

If your production compose pins images by variable, e.g.
`image: ghcr.io/chrisw09/example-app-backend:${TAG}`, then setting `TAG` and
re-running `up -d` instantly reverts to the known-good build. Because the old
image is still in GHCR (the warehouse keeps old recipes), no rebuild is needed —
the rollback takes only as long as a pull.

> ✅ **Best practice:** Never delete old `:sha` tags from the registry too
> eagerly — they are your rollback targets. Keep at least the last several
> builds. A retention policy that prunes images older than, say, 30 days is a
> sensible balance.

> ⚠️ **Common mistake:** Relying on `:latest` for rollbacks. `:latest` always
> points at the *newest* (broken) build, so re-pulling `:latest` just redeploys
> the bug. Roll back by pinning the previous commit tag.

---

## 10. Zero-downtime considerations

When `docker compose up -d` recreates a container, there is a brief moment where
the old container stops and the new one starts. For our small app this gap is
typically a second or two — usually acceptable. But here is how to think about
shrinking it:

- **`depends_on` + healthchecks** ensure the database is ready before the backend
  starts (our `backend` waits for `condition: service_healthy` on `db`), avoiding
  a flood of startup errors.
- **`restart: unless-stopped`** means a crashed container comes back on its own.
- **Stateless services restart fastest.** Our `backend`, `frontend`, and `nginx`
  hold no local state — all persistent data lives in the `db_data` volume — so
  they can be replaced freely without data loss.
- **For true zero-downtime**, you would run multiple replicas behind the proxy
  and roll them one at a time (a rolling update), or use a blue-green strategy
  (start the new stack alongside the old, then switch the proxy). Plain Compose
  on a single host does not do rolling updates automatically; that is where
  orchestrators like Kubernetes or Docker Swarm come in. For a single-server
  teaching app, the brief restart is fine.

> 💡 **Intuition:** Zero-downtime is like swapping the chef mid-service without
> the diners noticing: you bring the new chef fully up to speed *beside* the old
> one, then hand over in a single instant — you never leave the kitchen empty.

---

## 11. Handling `.env` files and secrets

Our example uses plain database credentials (`app`/`app`/`app`) for clarity. In a
real deployment you must **not** hard-code secrets in the compose file or commit
them to Git. Instead, use a `.env` file on the server.

Docker Compose automatically reads a file named `.env` sitting next to
`docker-compose.yml` and substitutes `${VAR}` references. On the server:

```bash
# /opt/example-app/.env  — readable only by the deploy user
POSTGRES_PASSWORD=a-long-random-secret
DATABASE_URL=postgresql://app:a-long-random-secret@db:5432/app
```

Lock it down so only the owner can read it:

```bash
chmod 600 /opt/example-app/.env
```

Then reference the variables in compose, e.g.
`POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}`.

> ⚠️ **Common mistake:** Committing `.env` to Git. Add it to `.gitignore`. A
> leaked database password in your repository history is very hard to fully
> scrub. Secrets belong on the server (or in GitHub Secrets for CI), never in the
> repo.

> ✅ **Best practice:** Keep secrets out of the image too — pass them at runtime
> via environment variables or Docker secrets, so the same immutable image is
> safe to use across environments.

---

## 12. Putting it all together

Here is the complete first-time-then-automated workflow:

1. **One time:** provision the server (§4), create the prod compose file (§5),
   `docker login ghcr.io` (§6), and do a manual `pull && up -d` to confirm it
   works.
2. **One time:** set the three GitHub Secrets (§7.1) and relocate the workflow to
   the repo root (§7.2).
3. **Forever after:** `git push` to `main`. CI tests, builds, pushes, SSHes in,
   pulls, and restarts — and `https://example.com` shows the new version, with no
   manual steps.

That is a real, production-grade continuous deployment pipeline. From here, the
[monitoring](monitoring.md) chapter teaches you how to *watch* it in production,
and [troubleshooting](troubleshooting.md) teaches you how to fix it when an arrow
in that pipeline breaks.

---

## Exercises

Try these on a real (or throwaway cloud) server if you can — there is no
substitute for the real thing.

**Exercise 1 — Build the production compose file.**
Starting from the local [example-app/docker-compose.yml](example-app/docker-compose.yml),
produce the production variant. Which exact lines do you remove, and which must
stay identical?

<details>
<summary>Answer</summary>

Remove the four `build: ./backend`, `build: ./frontend`, `build: ./nginx` lines
(the `db` service has no `build:`). Keep everything else **identical**: all four
service names, the `image:` tags, `ports: "80:80"`, the `DATABASE_URL`, the
Postgres healthcheck, `depends_on`, `restart: unless-stopped`, the `appnet`
network, and the `db_data` volume. The result is the file shown in §5.

</details>

**Exercise 2 — Harden a fresh server.**
List, in order, the commands to (a) create a sudo user `deploy`, (b) enable
key-only SSH, and (c) open only ports 22/80/443. What is the single most
dangerous ordering mistake?

<details>
<summary>Answer</summary>

```bash
adduser deploy
usermod -aG sudo deploy
ssh-copy-id deploy@203.0.113.10          # from your laptop, after creating a key
# edit /etc/ssh/sshd_config: PermitRootLogin no / PasswordAuthentication no
sudo systemctl restart ssh
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

The most dangerous mistake is disabling `PasswordAuthentication` (or enabling
`ufw` without allowing port 22) **before** confirming your SSH key works in a
second session — you can permanently lock yourself out.

</details>

**Exercise 3 — Wire up the deploy job.**
Name the three GitHub Secrets the `deploy` job reads, what each should contain,
and the classic error people make with `SERVER_SSH_KEY`.

<details>
<summary>Answer</summary>

`SERVER_HOST` = `203.0.113.10` (or `example.com`); `SERVER_USER` = `deploy`;
`SERVER_SSH_KEY` = the **private** key (full file, BEGIN/END lines included)
whose public half is in the server's `authorized_keys`. The classic error is
pasting the public `.pub` key instead of the private one, or using a
passphrase-protected key (which hangs CI).

</details>

**Exercise 4 — Roll back.**
A deploy of commit `9f2c1a` broke production; `1b7d4e` was the last good one. How
do you revert in seconds *without* rebuilding, and why does re-pulling `:latest`
not help?

<details>
<summary>Answer</summary>

Deploy the previous commit-hash image tag, e.g. set
`image: ghcr.io/chrisw09/example-app-backend:1b7d4e` (or `export TAG=1b7d4e`),
then `docker compose pull && docker compose up -d`. The old image is still in
GHCR, so no rebuild is needed — only a pull. Re-pulling `:latest` does not help
because `:latest` points at the newest (broken) `9f2c1a` build.

</details>

---

## Next / Related

- [github-actions.md](github-actions.md) — the CI/CD workflow whose `deploy` job
  drives this chapter.
- [registries.md](registries.md) — how images get into GHCR for the server to
  pull.
- [monitoring.md](monitoring.md) — watch the deployment once it is live.
- [troubleshooting.md](troubleshooting.md) — diagnose and fix a broken
  deployment.
