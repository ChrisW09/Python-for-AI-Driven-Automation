# Exercises — Container Fundamentals Bank

> 💡 **Intuition:** Each chapter ends with a few embedded drills. This file is the **consolidated bank**, ordered easy → hard within each section — the gym where the module's ideas get load-bearing. Work top to bottom, or jump to the section matching the chapter you just read.

**Difficulty tiers** (look for the badge on each task):

- 🟢 **Beginner** — one concept, guided, a few minutes.
- 🟡 **Intermediate** — combine ideas, light problem-solving.
- 🔴 **Advanced** — design decisions, edge cases, production thinking.

**Equipment:** exercises marked **[paper]** need only your head; **[python]** need any Python interpreter (no Docker); **[docker]** need a working Docker installation (Docker Desktop or Engine) — they're optional if you're working fully offline, and each states its expected output so you can dry-run it mentally. Every exercise states a concrete **deliverable**; answer keys sit in collapsible `<details>` blocks — try first, then check.

**Sections:** [Concepts & history](#1-concepts--history) · [Images & layers](#2-images--layers) · [Internals](#3-internals) · [DS Dockerfiles](#4-ds-dockerfiles) · [Volumes & networking](#5-volumes--networking) · [Ecosystem](#6-ecosystem) · [Capstone challenges](#7-capstone-challenges)

---

## 1. Concepts & history

> Chapter: [why-containers.md](why-containers.md).

### 1.1 🟢 [paper] The elevator explanation

**Deliverable:** four sentences, written down: explain to a smart non-engineer (a) what problem containers solve, (b) how a container differs from a VM (virtual machine), (c) why containers start in milliseconds, (d) one situation where you'd still choose a VM.

<details>
<summary>Answer key</summary>

Model answer: (a) Software silently depends on its whole environment — OS libraries, language version, config — so it breaks when moved; a container packages the app *with* its environment into one portable, isolated unit. (b) A VM fakes an entire computer and boots its own operating-system kernel; a container is just an ordinary process that the host's kernel shows a private view of the machine. (c) Because "starting" a container is starting a process plus some kernel bookkeeping — nothing boots. (d) Running untrusted/hostile code, or needing a different OS/kernel (e.g. testing on Windows from Linux) — the shared kernel rules containers out.
</details>

### 1.2 🟢 [paper] Right tool, three scenarios

**Deliverable:** for each, name venv / container / VM and one-line justification: (a) reproducing a colleague's LightGBM + `libomp` analysis on your differently-configured laptop; (b) a quick pandas exploration of a CSV (comma-separated values) file; (c) a grading service that executes students' arbitrary submitted code.

<details>
<summary>Answer key</summary>

(a) **Container** — the pain is *native* dependencies + cross-machine drift, exactly what images freeze. (b) **venv** (or even none) — pure-Python, single machine; containerizing adds ceremony, no value. (c) **VM/micro-VM** — arbitrary hostile code must not share a kernel with the host; plain containers are the wrong sole boundary ([why-containers.md §4](why-containers.md)).
</details>

### 1.3 🟡 [paper] What did Docker actually invent?

**Deliverable:** a short paragraph answering: namespaces, cgroups, and LXC all predate Docker — so what, concretely, did Docker add in 2013, and what did the OCI change in 2015?

<details>
<summary>Answer key</summary>

Docker added the *logistics*, not the isolation: the **image** (a layered, immutable, shareable artifact), the **Dockerfile** (environments as reviewable, reproducible code), and the **registry** with `push`/`pull` (distribution like a package manager) — turning kernel machinery into a developer workflow. The OCI then took Docker's formats and made them **vendor-neutral standards** (image, runtime, distribution specs), so today any compliant tool — Podman, containerd, Kubernetes — builds/runs/serves the same images. You learned a format, not a product.
</details>

---

## 2. Images & layers

> Chapter: [images-and-layers.md](images-and-layers.md) · Lab: [`lab01_container_anatomy.ipynb`](lab01_container_anatomy.ipynb).

### 2.1 🟢 [docker] Read a real image's anatomy

**Deliverable:** for `python:3.12-slim` (or any local image): its config digest (`Id`), one `RepoDigest`, the number of filesystem layers, and its default `Cmd` — plus which chapter concept each field is.

<details>
<summary>Answer key</summary>

```bash
docker pull python:3.12-slim
docker image inspect python:3.12-slim   # Id, RepoDigests, Config.Cmd, RootFS.Layers
docker history python:3.12-slim         # layers with sizes; 0B rows are metadata-only
```

`Id` = digest of the **config blob**; `RepoDigests` = the pinnable **manifest digest** (what `FROM …@sha256:` uses); `RootFS.Layers` = the ordered **diff-ID stack** (typically ~5 layers for slim); `Config.Cmd` = `["python3"]`, living in the config, not in any filesystem layer.
</details>

### 2.2 🟢 [python] Digest ≠ tag, in eight lines

**Deliverable:** a tiny Python demo: hash two byte-strings with `hashlib.sha256`, show identical content ⟹ identical digest, then re-point a `tags = {"latest": …}` dict and state in one sentence which behavior mirrors tags and which mirrors digests.

<details>
<summary>Answer key</summary>

```python
import hashlib
h = lambda b: hashlib.sha256(b).hexdigest()[:12]
v1, v2 = b"model-api code v1", b"model-api code v2"
print(h(v1), h(v1) == h(b"model-api code v1"))   # same bytes -> same digest, always
tags = {"latest": h(v1)}
tags["latest"] = h(v2)                            # re-pointed silently
```

The dict is the **tag**: a mutable name → digest pointer anyone can re-aim. The hash is the **digest**: identity *derived from content*, impossible to re-point. Deploy-by-digest is deploy-by-mathematics; deploy-by-tag is deploy-by-trust.
</details>

### 2.3 🟡 [paper] The invalidation cascade, predicted

**Deliverable:** for the Dockerfile below, list which layers rebuild after each independent change: (a) edit `src/train.py`; (b) add one package to `requirements.txt`; (c) change `ENV LOG_LEVEL=debug` to `info`; (d) `touch requirements.txt` (timestamp only).

```dockerfile
FROM python:3.12-slim          # L1
ENV LOG_LEVEL=debug            # L2
WORKDIR /app                   # L3
COPY requirements.txt .        # L4
RUN pip install -r requirements.txt   # L5
COPY src/ ./src/               # L6
CMD ["python", "src/train.py"] # L7
```

<details>
<summary>Answer key</summary>

(a) **L6–L7** rebuild (L6's copied content changed; L7 follows because its parent changed — cheap). (b) **L4–L7** (L4's content hash changed; the expensive L5 re-runs — this is the edit that hurts). (c) **L2–L7** — instruction text changed near the top, so *everything below* rebuilds, including the pip install, even though no dependency changed; a reason to put volatile `ENV`s *below* the heavy layers when they don't affect them. (d) **Nothing** — `COPY`'s cache key hashes file *content*, not metadata ([images-and-layers.md §7](images-and-layers.md)).
</details>

### 2.4 🟡 [docker] Prove that deleting doesn't shrink

**Deliverable:** two image sizes demonstrating the whiteout effect: an image that creates a 50 MB file and `rm`s it in a *separate* instruction vs. in the *same* instruction, plus one sentence naming the mechanism.

<details>
<summary>Answer key</summary>

```dockerfile
# Dockerfile.two-layers                      # Dockerfile.one-layer
FROM debian:bookworm-slim                    FROM debian:bookworm-slim
RUN dd if=/dev/zero of=/big bs=1M count=50   RUN dd if=/dev/zero of=/big bs=1M count=50 \
RUN rm /big                                      && rm /big
```

```bash
docker build -f Dockerfile.two-layers -t demo:two . && docker build -f Dockerfile.one-layer -t demo:one .
docker images demo   # demo:two ≈ base + 50MB; demo:one ≈ base
```

Layers are immutable and additive: the second Dockerfile's `rm` in a *later* layer only adds a **whiteout** hiding `/big` — the 50 MB still ships in the earlier layer. Deleting within the same `RUN` means the file never exists when that single layer is snapshotted.
</details>

### 2.5 🔴 [python] Implement the overlay lookup

**Deliverable:** a function `read(path, upper, lowers, whiteouts)` implementing OverlayFS resolution — upper wins, then lowers top-down, whiteouts terminate the search — passing the four asserts below. (The lab notebook builds a fuller version; write this one from scratch, closed-book.)

```python
upper     = {"c.txt": "upper-c"}
lowers    = [{"b.txt": "l2-b", "c.txt": "l2-c"},        # l2 (higher)
             {"a.txt": "l1-a", "b.txt": "l1-b"}]        # l1 (lower)
whiteouts = {"a.txt"}

assert read("c.txt", upper, lowers, whiteouts) == "upper-c"
assert read("b.txt", upper, lowers, whiteouts) == "l2-b"
assert read("a.txt", upper, lowers, whiteouts) is None
assert read("zzz.txt", upper, lowers, whiteouts) is None
```

<details>
<summary>Answer key</summary>

```python
def read(path, upper, lowers, whiteouts):
    if path in whiteouts:          # whiteout in the writable layer hides everything below
        return None
    if path in upper:              # upper (container layer) wins
        return upper[path]
    for layer in lowers:           # then lowers, top-down; first hit wins
        if path in layer:
            return layer[path]
    return None                    # nowhere in the stack
```

Ten lines, and it *is* the [images-and-layers.md §5](images-and-layers.md) mount semantics: `merged/` is exactly "call `read` for every name." Extension if you're enjoying it: implement `write` (into `upper`) and `delete` (add to `whiteouts`) and you have copy-on-write.
</details>

---

## 3. Internals

> Chapter: [container-internals.md](container-internals.md).

### 3.1 🟢 [docker] Catalog the illusion

**Deliverable:** run five commands inside `docker run -it --rm python:3.12-slim bash` — `ps aux`, `hostname`, `whoami`, `ip addr` (or `cat /proc/net/dev`), `uname -r` — and label each output with the namespace responsible, plus the one output that is *not* namespaced and why.

<details>
<summary>Answer key</summary>

`ps aux` (2 processes, bash is PID 1) → **pid namespace**. `hostname` (random hex) → **uts namespace**. `ip addr` (own `eth0`, 172.17.x.x) → **net namespace**. The filesystem you're standing in → **mnt namespace** over the overlay mount. `whoami` = root → user identity (with reduced capabilities; remapped only if user namespaces are on). `uname -r` → the **host's kernel version** — the kernel is the one shared, un-namespaced thing; on macOS/Windows it's Docker Desktop's Linux VM kernel.
</details>

### 3.2 🟡 [paper] The chain of command, reconstructed

**Deliverable:** the sequence of actors between typing `docker run app` and your process executing — client, dockerd, containerd, shim, runc — with one clause on each actor's job, and answers to: which one *stays* running next to your container, and which exits immediately by design?

<details>
<summary>Answer key</summary>

**Client** parses flags and POSTs to the daemon's socket → **dockerd** resolves the image/volumes/network and delegates → **containerd** ensures image blobs and prepares the overlay snapshot → **containerd-shim** (stays!) holds stdio and exit status so daemons can restart without killing containers → **runc** makes the namespace/cgroup/pivot-root syscalls per the OCI bundle and **exits by design** — after which only your process (plus the shim) remains. There is no "container object" running anywhere: just a well-dressed process.
</details>

### 3.3 🟡 [docker] Watch a memory limit kill

**Deliverable:** a one-liner container that allocates past a 256 MB limit, its exit code, and the `docker inspect` field proving the OOM (out-of-memory) kill.

<details>
<summary>Answer key</summary>

```bash
docker run --name oomtest --memory=256m python:3.12-slim \
  python -c "x = bytearray(400 * 1024 * 1024)"
echo $?                                                    # 137  (128 + SIGKILL)
docker inspect --format '{{.State.OOMKilled}} {{.State.ExitCode}}' oomtest   # true 137
docker rm oomtest
```

The cgroup's `memory.max` was 268435456; the allocation crossed it; the kernel's OOM killer sent SIGKILL — no Python traceback possible. Exit 137 + `OOMKilled: true` is the fingerprint to check whenever a training container "vanishes overnight" ([container-internals.md §4](container-internals.md)).
</details>

### 3.4 🔴 [paper] Four errors, four mechanisms

**Deliverable:** match each symptom to the internal mechanism and give the fix: (a) `docker stop` takes exactly 10 s every time; (b) DataLoader workers die with `bus error`; (c) a "root" shell inside the container can't `mount` anything; (d) on your Mac, containers OOM at 8 GB while the host has 32 GB free.

<details>
<summary>Answer key</summary>

(a) The app runs as **PID 1**, which doesn't get default signal handlers — SIGTERM is ignored, and Docker SIGKILLs after the grace period; fix: `docker run --init`, or an exec-form entrypoint whose process handles SIGTERM. (b) `/dev/shm` (ipc namespace) capped at 64 MB; fix: `--shm-size=2g`. (c) Default **capability** set lacks `CAP_SYS_ADMIN` and **seccomp** blocks the `mount` syscall — "root" inside is deliberately depowered; fix: don't mount inside containers (use `-v`), or, knowingly, `--cap-add`. (d) Docker Desktop's **Linux VM** has a fixed memory allocation that caps all containers regardless of host RAM; fix: raise it in Desktop settings ([container-internals.md §6](container-internals.md)).
</details>

---

## 4. DS Dockerfiles

> Chapter: [dockerfiles-for-data-science.md](dockerfiles-for-data-science.md) · Generic tutorial: [Module 14 docker.md](../14_cicd/docker.md).

### 4.1 🟢 [paper] Base-image triage

**Deliverable:** the right `FROM` for each, with one line why: (a) pandas ETL (extract-transform-load) job, CPU; (b) GPU inference for a PyTorch model; (c) building `flash-attn` from source; (d) a pure-Python CLI (command-line interface) utility.

<details>
<summary>Answer key</summary>

(a) `python:3.12-slim` — glibc wheels install clean, ~120 MB. (b) `nvidia/cuda:12.x-runtime-…` + Python, or `pytorch/pytorch:…-runtime` — CUDA libs in the image, driver from the host. (c) `nvidia/cuda:12.x-devel-…` — needs `nvcc` and headers — **as the builder stage only**, shipping a `runtime` final stage. (d) `python:3.12-slim` still the default; `-alpine` is *acceptable* here (no scientific wheels involved) if you truly care about the last 70 MB.
</details>

### 4.2 🟡 [paper] Roast this Dockerfile

**Deliverable:** at least six concrete defects in the Dockerfile below, each with its fix and the chapter section that names it.

```dockerfile
FROM python:latest
COPY . .
RUN pip install torch transformers pandas
RUN rm -rf /root/.cache/pip
ENV HF_TOKEN=hf_abcdef123456
COPY model.pt /model.pt
CMD python serve.py
```

<details>
<summary>Answer key</summary>

1. **`python:latest`** — unpinned moving target; pin version + digest (§1–2). 2. **`COPY . .` first** — every source edit busts the install cache; copy lockfile → install → copy code (§3), and there's evidently **no `.dockerignore`** either (data/checkpoints/.git ride in — §5). 3. **Unpinned `pip install`** — no lockfile, different image every build (§2); also default torch wheel bundles CUDA — pick the right index for the target (§6). 4. **`RUN rm` in a separate layer** — reclaims nothing, adds whiteouts ([images-and-layers.md §2](images-and-layers.md)); use a cache mount or same-instruction cleanup. 5. **Secret in `ENV`** — baked into the config/layers forever; use runtime `-e` or BuildKit secret mounts (§5). 6. **5 GB `model.pt` baked in, before code even** — decouple model delivery (volume/startup download) or at minimum give it its own late layer (§8). 7. No **non-root `USER`** (§5). 8. Shell-form **`CMD`** — wraps in `/bin/sh`, which then owns PID 1 and eats signals; use exec form `["python","serve.py"]`.
</details>

### 4.3 🟡 [docker] Feel the cache mount

**Deliverable:** rough timings of three builds of a requirements-only Dockerfile — cold, warm (no changes), and after adding one small package — with and without `RUN --mount=type=cache,target=/root/.cache/pip`, plus one sentence on where the win comes from.

<details>
<summary>Answer key</summary>

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.12-slim
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
```

Expected shape: cold ≈ full download+install either way; warm = instant either way (pure layer cache hit); **add-one-package** is where they diverge — without the mount, the layer re-runs and re-downloads *every* wheel (`--no-cache-dir` or a discarded cache); with it, pip finds all previous wheels in the mounted cache and only fetches the newcomer: minutes → seconds. The cache lives outside all layers, so the image size is identical ([images-and-layers.md §7](images-and-layers.md), [dockerfiles-for-data-science.md §3](dockerfiles-for-data-science.md)).
</details>

### 4.4 🔴 [paper] Design a training image for the team GPU server

**Deliverable:** a complete Dockerfile sketch + the exact `docker run` line for: PyTorch training, CUDA 12.x, a compiled extension, weekly-changing deps, daily-changing code, checkpoints that must survive, dataset read from `/datasets` on the host, shared 4-GPU box (be a good citizen: memory cap, your own UID, specific GPUs).

<details>
<summary>Answer key</summary>

Dockerfile: `nvidia/cuda:12.4.1-devel` **builder** stage — venv, lockfile copy, cache-mounted `pip install` (extension compiles here) → `nvidia/cuda:12.4.1-runtime` **final** stage — system Python, `COPY --from=builder /opt/venv`, `useradd --uid 1000`, `COPY src/` last, exec-form `CMD`. Run line:

```bash
docker run --rm -d --name maria-train \
  --gpus '"device=2,3"' --memory=48g --shm-size=8g \
  --user "$(id -u):$(id -g)" \
  -v /datasets:/datasets:ro \
  -v maria-ckpts:/checkpoints \
  team-train:9f3c1ab python -m src.train --out /checkpoints
```

Every flag earns its place: specific GPUs + memory cap = shared-box citizenship; `--shm-size` for DataLoader workers; `:ro` dataset; named volume for checkpoints (survives `--rm`); your UID so outputs aren't root-owned; an immutable code tag, not `:latest`.
</details>

---

## 5. Volumes & networking

> Chapter: [volumes-and-networking.md](volumes-and-networking.md).

### 5.1 🟢 [docker] A volume outlives its containers

**Deliverable:** terminal output showing: container A writes a file into named volume `scratch`, is removed; container B reads the file from the same volume.

<details>
<summary>Answer key</summary>

```bash
docker run --rm -v scratch:/data alpine sh -c 'echo "survived" > /data/note.txt'
docker run --rm -v scratch:/data alpine cat /data/note.txt    # survived
docker volume inspect scratch    # Docker-managed Mountpoint, independent lifecycle
docker volume rm scratch         # cleanup — THIS is what deletes the data
```

The writable layer died with container A (`--rm`); the volume is a separate object that containers merely visit.
</details>

### 5.2 🟢 [paper] Mount-type triage

**Deliverable:** bind / named volume / tmpfs / bake-into-image for: (a) `notebooks/` you edit in VS Code; (b) the pip cache a CI (continuous-integration) runner reuses across builds; (c) decrypted credentials needed only while the process runs; (d) Postgres data on a Mac laptop (performance matters).

<details>
<summary>Answer key</summary>

(a) **Bind mount** — host tools (editor, Git) must see the real files. (b) Build-time **cache mount** (`RUN --mount=type=cache`) — the build-context cousin of volumes, no layer weight. (c) **tmpfs** — RAM-only, never persisted, gone at exit. (d) **Named volume** — on macOS it lives inside the Linux VM = native filesystem speed; a bind mount would drag every page across the VM file-sharing boundary.
</details>

### 5.3 🟡 [docker] Wire up name-based service discovery

**Deliverable:** commands creating network `mlnet`, a `redis` container on it, and a second container that reaches it as `redis` by name — plus one sentence on why the *default* bridge would have failed.

<details>
<summary>Answer key</summary>

```bash
docker network create mlnet
docker run -d --name redis --network mlnet redis:7-alpine
docker run --rm --network mlnet redis:7-alpine redis-cli -h redis ping   # PONG
```

Name resolution comes from Docker's embedded DNS (127.0.0.11), which serves **user-defined** networks only; on the legacy default `bridge`, `-h redis` would not resolve ([volumes-and-networking.md §4](volumes-and-networking.md)). Note also: no `-p` anywhere — container↔container traffic never needs published ports.
</details>

### 5.4 🔴 [paper] Remote-lab network design

**Deliverable:** a diagram-or-list design for a shared internet-reachable GPU server running: Jupyter (you only), an experiment-tracker web UI (whole team, VPN'd — virtual private network), Postgres (used by the tracker only). For each: network membership, publish decision (`-p` what, bound where), and the reasoning.

<details>
<summary>Answer key</summary>

One user-defined network `labnet` with all three attached. **Postgres:** no `-p` at all — reachable only as `db:5432` from `labnet`; the internet has no path to it. **Tracker UI:** `-p 127.0.0.1:5000:5000` if team members come via SSH tunnels, or bind the VPN interface's IP (`-p 10.8.0.5:5000:5000`) for direct VPN access — never `0.0.0.0` on a public box. **Jupyter:** `-p 127.0.0.1:8888:8888`, token auth on, reached via `ssh -L 8888:localhost:8888` — single-user tools get loopback + tunnel by default. Principle: publish nothing publicly; every service gets the *narrowest* interface that serves its real audience, and container-to-container traffic rides the network, not published ports.
</details>

---

## 6. Ecosystem

> Chapter: [ecosystem.md](ecosystem.md).

### 6.1 🟢 [paper] Who runs what

**Deliverable:** one line each: what would you use to (a) run OCI images on a Docker-less Kubernetes node; (b) run containers on an HPC cluster that forbids root daemons; (c) get Docker-compatible commands without a daemon on Fedora; (d) build images inside CI without privileged Docker?

<details>
<summary>Answer key</summary>

(a) **containerd** (or CRI-O) — the K8s-native lifecycle managers. (b) **Apptainer** (Singularity) — unprivileged HPC runtime that consumes OCI images. (c) **Podman** — daemonless, rootless, CLI-compatible. (d) **BuildKit / kaniko / Buildah** — daemonless builders. Common thread: one OCI image format throughout; only the runner changes.
</details>

### 6.2 🟡 [paper] The Kubernetes decision memo

**Deliverable:** a five-sentence memo for your team lead: current state = one GPU server, Compose, Module-14-style CI, one model API + nightly retrain. Recommend for/against Kubernetes now, list the two strongest reasons, and name the concrete trigger that should reopen the question.

<details>
<summary>Answer key</summary>

Model memo: *Recommend against, for now. (1) Everything K8s would give us at our scale — restart-on-crash, health-gated startup, one-command reproducible deploys — we already have via Compose `restart: unless-stopped` + CI; (2) the costs are real and permanent: cluster upgrades, RBAC, networking add-ons, and a team-wide learning curve, all to coordinate a fleet we don't have. The nightly retrain is a scheduled job, not an always-on scaling problem. Reopen when a trigger lands: sustained load or GPU-job queueing beyond this one box, a genuine multi-machine availability requirement, or multiple teams needing quota'd shared infra — and then evaluate a managed cluster first, reusing our images and registry unchanged.*
</details>

### 6.3 🔴 [python] Reproducibility audit

**Deliverable:** a checklist-based audit of any real repo you own (or a course module): score it ✅/❌ on — Dockerfile present; base pinned by digest; installs driven by a lockfile; data/outputs outside the image (mounts, `.dockerignore`); runnable with `--network none`; built-image digest recorded anywhere. Then write the *smallest* diff that would fix the worst ❌.

<details>
<summary>Answer key</summary>

Typical findings and their one-line fixes: base pinned to a tag only → append `@sha256:…` from `docker images --digests`; `pip install -r requirements.txt` where the file has loose pins → generate a lock (`uv lock` / `pip-compile`) and install `--frozen`/from the lock; `data/` not in `.dockerignore` → add it (and mount at runtime); network-dependent run (model downloads at import time) → pre-fetch into a cached volume and pin the revision, then test under `--network none`; no digest recorded → paste the image digest into the README's "reproduce" section next to the one-command `docker run`. The audit itself — six binary checks — is the deliverable worth keeping in your team's PR (pull-request) template ([ecosystem.md §4](ecosystem.md)).
</details>

---

## 7. Capstone challenges

End-to-end, spanning every chapter. Treat them like real tickets: design, implement (where you have Docker), verify.

### 7.A 🟡→🔴 Containerize a real analysis from this course

**Deliverable:** pick a notebook-based analysis from an earlier module (e.g., a Module 2 or Module 5 lesson) and produce: a pinned Dockerfile (slim base by digest, lockfile install, non-root user), a `.dockerignore`, and a documented pair of run commands — one launching Jupyter Lab with the work directory mounted, one executing the analysis headlessly (`jupyter nbconvert --to notebook --execute`) with inputs `:ro` and outputs to a mounted `out/`. Verify the headless run works with `--network none`.

<details>
<summary>Answer key</summary>

Skeleton:

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.12-slim@sha256:<digest>
RUN useradd --create-home --uid 1000 runner
WORKDIR /work
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt jupyterlab
USER runner
EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser"]
```

```bash
# interactive
docker run --rm -p 127.0.0.1:8888:8888 -v "$PWD":/work course-analysis
# headless, provably offline
docker run --rm --network none -v "$PWD":/work -v "$PWD/out":/out course-analysis \
  jupyter nbconvert --to notebook --execute lesson.ipynb --output /out/lesson-run.ipynb
```

Success criteria: rebuild after editing the notebook touches only the code layer (ordering!); the offline run passing proves no hidden downloads; outputs land host-side, owned by UID 1000 = you.
</details>

### 7.B 🔴 The image-diet ticket

**Deliverable:** a written optimization plan (target: < 1.5 GB and < 60 s warm rebuilds) for this inherited image, with each step tied to its mechanism: `FROM nvidia/cuda:12.4.1-devel-ubuntu22.04`, `COPY . .` (repo contains `data/` 12 GB, `.git/` 800 MB), unpinned `pip install torch transformers fastapi` (CPU-only service in production!), `RUN apt-get install` of build tools kept in the final image, `COPY weights/model.safetensors` (2.2 GB, retrained weekly), root user, `:latest` deploys.

<details>
<summary>Answer key</summary>

(1) **Base:** CPU service needs no CUDA at all → `python:3.12-slim` by digest (−7 GB; mechanism: base choice, §1 of the DS chapter). (2) **`.dockerignore`** for `data/`, `.git/`, checkpoints (−12.8 GB of context; §5). (3) **Lockfile + CPU wheel index** for torch (−~2.5 GB of bundled CUDA libs; §2, §6). (4) **Multi-stage**: build tools in a builder, `COPY --from` the venv (whiteout economics; [images-and-layers.md §2](images-and-layers.md)/§4). (5) **Model out of the image**: weekly weights → startup download pinned to a model version, cached on a volume (decoupled cadences; §8) — this alone removes 2.2 GB from every code deploy. (6) **Ordering + cache mount**: lockfile→install→code gives the <60 s warm rebuild ([images-and-layers.md §7](images-and-layers.md)). (7) **Hygiene:** non-root `USER`, exec-form CMD, deploy by SHA tag/digest not `:latest`. Landing zone: ~400–700 MB, seconds-scale rebuilds.
</details>

### 7.C 🔴 Teach-back: the whiteboard hour

**Deliverable:** you're giving next cohort's one-hour "containers from first principles" session, whiteboard only. Produce: (1) the three drawings you'd build the hour around; (2) the five vocabulary terms you'd insist every attendee can define cold; (3) the three live commands you'd run if a laptop with Docker appears; (4) the one question you'd close with.

<details>
<summary>Answer key</summary>

A strong version: **Drawings** — (i) VM-vs-container stacks (where the kernel line sits — [why-containers.md §3](why-containers.md)); (ii) the layer stack with a writable top, one copy-up arrow, one whiteout ([images-and-layers.md §3](images-and-layers.md)); (iii) the `docker run` chain client→dockerd→containerd→shim→runc→process with namespaces/cgroups annotated ([container-internals.md §2](container-internals.md)). **Terms** — image, layer, digest vs tag, namespace, cgroup. **Commands** — `docker history python:3.12-slim` (layers are visible, some 0B); `docker run -it --rm python:3.12-slim bash` + `ps aux` + `uname -r` (the illusion and its one crack); `docker run --rm --memory=64m python:3.12-slim python -c "bytearray(10**9)"` + `echo $?` (cgroups are real: 137). **Closing question** — "Your image deletes a 5 GB file in its last layer. How big is the download, and why?" — because answering it requires the whole model: layers, immutability, whiteouts, content addressing.
</details>

---

## Next / Related

- [`lab01_container_anatomy.ipynb`](lab01_container_anatomy.ipynb) — the guided, offline build-it-yourself companion to sections 2 and 3.
- [README.md](README.md) — the module map and reading order.
- Per-topic depth: [why-containers.md](why-containers.md) · [images-and-layers.md](images-and-layers.md) · [container-internals.md](container-internals.md) · [dockerfiles-for-data-science.md](dockerfiles-for-data-science.md) · [volumes-and-networking.md](volumes-and-networking.md) · [ecosystem.md](ecosystem.md).
- Ready to ship? [Module 14](../14_cicd/) turns these fundamentals into a live, auto-deploying system.
