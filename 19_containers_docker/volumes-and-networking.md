# Volumes & networking — where data lives and how containers talk

Two chapters ago you learned that a container's filesystem is an overlay whose writable top layer **dies with the container** ([images-and-layers.md §3](images-and-layers.md)), and that each container gets a **private network stack** in its own namespace ([container-internals.md §3](container-internals.md)). Both facts are features — disposability and isolation — until the day they delete your notebooks or hide your API. This chapter is about the two escape hatches, done properly: **mounts** (data that outlives containers) and **networks** (traffic that crosses the walls on purpose).

[Module 14](../14_cicd/docker.md) covers both topics to the depth its example app needs (§7–8 there). Here we build the complete model, with the data-science-specific patterns — datasets, model caches, notebook survival, GPU-box etiquette — that a web-app module has no reason to cover. At the end, a short bridge hands you to [Docker Compose](../14_cicd/docker-compose.md), which declares everything in this chapter in YAML.

---

## 1. Why external storage exists (60-second recap)

Writes in a container land in its private writable layer. Three separate problems:

1. **Lifetime** — `docker rm` deletes the layer. Notebook edits, trained checkpoints, database rows: gone.
2. **Performance** — the overlay's copy-on-write is wrong for write-heavy data (modify one byte of a lower-layer file → the whole file copies up first; [images-and-layers.md §3](images-and-layers.md)). Databases and checkpoint writers deserve a real filesystem.
3. **Sharing** — the layer belongs to *one* container. Your training container and your Jupyter container can't both see it.

A **mount** solves all three at once: a directory from *outside* the overlay is grafted into the container's filesystem tree at a chosen path. Reads and writes there bypass copy-on-write entirely and touch the real location — which survives, performs natively, and can be mounted into ten containers at once.

> 💡 **Intuition:** [Module 14](../14_cicd/docker.md) calls a volume the **pantry** — the meal (container) is cleared away, the pantry stays stocked. The refinement this chapter adds: there are two *kinds* of pantry, and choosing wrong is a classic source of pain.

---

## 2. The two kinds of mount

```bash
# Named volume: Docker-managed storage, referred to by name
docker run -v experiment-data:/data my-training-image

# Bind mount: an exact host directory, referred to by path
docker run -v "$PWD/notebooks":/home/jovyan/work quay.io/jupyter/scipy-notebook
```

| | **Named volume** | **Bind mount** |
|---|---|---|
| What it is | A directory Docker creates and manages (under `/var/lib/docker/volumes/…`), addressed by name | An existing host directory/file you address by absolute path |
| Who owns the location | Docker | You |
| Visible in your file manager? | Not usefully (and on Docker Desktop it's *inside the VM*) | Yes — it's just your folder |
| Lifecycle | Independent object: `docker volume create/ls/inspect/rm`; survives any container | Whatever the host directory's life is |
| Performance on macOS/Windows | **Native** (lives inside the Linux VM) | **Slow for many small files** (every access crosses the VM file-sharing boundary — [container-internals.md §6](container-internals.md)) |
| Content at first mount | If empty, Docker *pre-populates* it from the image's directory at that path | Host directory **shadows** the image's directory — you see the host's content, period |
| Best for | Databases, model caches, anything only containers touch | Source code and notebooks you edit with host tools; datasets that already live on the host |

The decision rule that covers nearly everything:

> ✅ **Best practice:** **Bind-mount what you edit; volume what services own.** Code and notebooks — bind mount (you want your editor, Git, and backups touching the real files). Postgres data, pip/HF caches, artifacts only containers read/write — named volume (native speed, no host-path coupling, managed lifecycle). And mount read-only wherever writing isn't the point: `-v "$PWD/data":/data:ro` — a dataset that *can't* be modified by a buggy job is a dataset you don't have to re-download.

The data-science standard kit, assembled:

```bash
docker run --rm --gpus all --shm-size=2g \
  -v "$PWD":/workspace \                        # code + notebooks: bind, editable
  -v "$PWD/data":/data:ro \                     # dataset: bind, READ-ONLY
  -v hf-cache:/home/appuser/.cache/huggingface \ # model cache: named volume — survives,
  -v checkpoints:/checkpoints \                  # checkpoints: named volume    shared, fast
  my-training-image python train.py
```

That `hf-cache` line deserves a highlight: mounting the model-hub cache as a named volume means the 5 GB download happens **once**, not once per container — the runtime half of the model-delivery strategy from [dockerfiles-for-data-science.md §8](dockerfiles-for-data-science.md).

Two footnotes for completeness: `--mount type=bind,source=…,target=…` is the long-form, more explicit spelling of `-v` (same result; `--mount` errors on a missing host path where `-v` silently creates a directory — a surprisingly good reason to prefer it in scripts). And **tmpfs mounts** (`--tmpfs /scratch`) give you RAM-backed scratch space that never touches disk — occasionally right for sensitive intermediates or hot temp files.

> ⚠️ **Common mistake:** The vanished-notebook incident. You run Jupyter in a container *without* mounting your work directory, save notebooks all afternoon into `/home/jovyan/work` — which is just the writable layer — then `docker rm` the container. Everything is gone, unrecoverable. The `-v "$PWD":/home/jovyan/work` in every Jupyter example ([dockerfiles-for-data-science.md §7](dockerfiles-for-data-science.md)) is not decoration; it is the difference between a filesystem and a mirage. (Half-remembered variant of the same trap: `docker compose down -v` — the `-v` there deletes *named volumes*; see [Module 14's Compose chapter](../14_cicd/docker-compose.md).)

### Permissions: the UID collision

Mounts graft filesystems, but Linux permissions ride along as raw numeric UIDs (user IDs) — and the container's idea of user 1000 and the host's idea of user 1000 are just numbers that may or may not refer to the same human. The two symptoms: a container running as root writes into your bind mount and leaves **root-owned files** you can't edit or delete without `sudo`; or a container running as its own non-root user **can't write** into your mounted directory at all. The fixes, in order of preference: run the container as *your* UID (`docker run --user "$(id -u):$(id -g)" …` — works with most well-built images), use images whose default user is UID 1000 matching the typical first Linux user (Jupyter's `jovyan`, the `--uid 1000` in [our Dockerfile](dockerfiles-for-data-science.md)), or `chown` the directory to the container's UID once. On shared GPU servers this etiquette matters doubly — root-owned droppings in a shared dataset directory make no friends.

---

## 3. Publishing ports: crossing the wall from outside

Networking has exactly two directions to keep straight, and they use different machinery:

- **Host (or internet) → container**: requires **publishing** a port.
- **Container → container**: requires a **shared network**, no publishing at all (§4).

Each container's network namespace has its own interfaces and ports — that's why five containers can all bind `:8000` internally with no clash. Publishing pokes a deliberate hole: `-p HOST:CONTAINER` makes the Docker daemon forward the host's port over the container's virtual cable (the veth pair from [container-internals.md §3](container-internals.md)):

```bash
docker run -p 8888:8888 my-jupyter          # host's 8888 → container's 8888
docker run -p 9999:8888 my-jupyter          # any free host port works on the left
docker run -p 127.0.0.1:8888:8888 my-jupyter  # loopback-only: reachable ONLY from this machine
docker run -P my-jupyter                    # publish every EXPOSEd port on random host ports
docker port <container>                     # see what ended up where
```

Three rules of thumb:

- **`EXPOSE` in a Dockerfile publishes nothing** — it's documentation ([Module 14 §10](../14_cicd/docker.md)). Only `-p`/`-P` at run time opens the door.
- **The left side is a scarce resource; the right side isn't.** One process per host port — a clash gives `bind: address already in use`; remap the left side freely, never the app's own port.
- **On shared or internet-facing machines, bind loopback by default.** Plain `-p 8888:8888` listens on *all* host interfaces — on a lab server, that's your token-authenticated-if-you're-lucky Jupyter offered to the whole network (and Docker's port publishing famously bypasses simple host firewall configs). `-p 127.0.0.1:8888:8888` plus SSH (Secure Shell) port-forwarding is the sane default for remote DS boxes: `ssh -L 8888:localhost:8888 you@gpubox`, then browse `localhost:8888` at home.

---

## 4. Container networks: crossing the walls between containers

Now the inward-facing direction. Docker's model: **networks are named objects; containers attached to the same network can reach each other; DNS (Domain Name System) resolves container names to their current IPs.** The workflow:

```bash
docker network create mlnet                     # a user-defined bridge network

docker run -d --name db  --network mlnet -v pgdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=app postgres:16-alpine
docker run -d --name api --network mlnet -p 8000:8000 my-model-api
docker run --rm --network mlnet postgres:16-alpine psql -h db -U postgres  # name, not IP!

docker network ls / inspect mlnet               # who's attached, what IPs
docker network connect othernet api             # containers can join several networks
```

What's happening underneath: a **bridge network** is a virtual switch on the host; each attached container's namespace gets a veth cable plugged into it; and — the crucial service — Docker runs an **embedded DNS server** (at `127.0.0.11` inside each container) that resolves *container names on user-defined networks* to their current IPs. Names are stable; IPs are cattle. When `db` is recreated tomorrow with a new IP, `psql -h db` still lands correctly — which is precisely why [Module 14's app](../14_cicd/docker-compose.md) connects to `postgresql://…@db:5432/…` and never to an address.

Details that round out the model:

- **The default bridge is the legacy exception.** Containers run without `--network` land on the default `bridge` — which has **no name-DNS** (only deprecated `--link` hacks). Practical rule: *always* create a user-defined network for multi-container work (Compose does this automatically — the `appnet` in Module 14).
- **Networks isolate as well as connect.** Two containers on *different* networks can't reach each other at all. That's a design tool: in Module 14's stack, only `nginx` is published; `db` is reachable solely by containers on `appnet` — the database has no door to the internet whatsoever.
- **`localhost` is the recurring trap.** Inside a container, `localhost` is *that container's own* loopback — never a neighbor, never the host. Neighbors go by container name; the **host itself** goes by the special name `host.docker.internal` (built into Docker Desktop; add `--add-host=host.docker.internal:host-gateway` on Linux) — the name you need when a container must call, say, an LLM server or database running natively on your machine.
- **Two special modes:** `--network host` deletes the network wall entirely — the container shares the host's stack (no `-p` needed or possible; Linux only; occasionally justified for latency or port-range-heavy tools), and `--network none` gives no network at all — a surprisingly useful reproducibility trick: a container that *cannot* download anything is a container whose inputs are provably all mounted and pinned.

```mermaid
flowchart TD
  subgraph host["Host"]
    subgraph mlnet["user-defined bridge 'mlnet' + embedded DNS"]
      API["api :8000"] -->|"db:5432"| DB[("db :5432")]
      JUP["jupyter :8888"] -->|"api:8000"| API
    end
    P1(["-p 8000:8000"]) --> API
    P2(["-p 127.0.0.1:8888:8888"]) --> JUP
  end
  WORLD([Browser / network]) --> P1
  ME([This machine only]) --> P2
  DB -.->|"no published port — unreachable from outside"| X[ ]
  style X display:none
```

---

## 5. The bridge to Compose

Look at what §2–§4's `docker run` commands have become: names, networks, volumes, ports, environment — five flags deep, three containers wide, order-sensitive. This is exactly the cliff at which [Module 14's Docker Compose chapter](../14_cicd/docker-compose.md) picks up: everything in this chapter has a one-line YAML spelling —

```yaml
services:
  api:
    ports: ["8000:8000"]          # §3: publishing
    networks: [mlnet]             # §4: shared network + DNS by service name
  db:
    volumes:
      - pgdata:/var/lib/postgresql/data   # §2: named volume
    networks: [mlnet]
volumes:
  pgdata:
networks:
  mlnet:
```

— and `docker compose up` replays it all in dependency order. Nothing new happens underneath: Compose *is* this chapter, declared instead of typed. Read that chapter next if you haven't; it also covers the operational verbs (`up`/`down`/`logs`/`pull`) and the production workflow.

---

## 6. Exercises

Try each before opening the answer.

**Exercise 1.** For each item, choose bind mount, named volume, tmpfs, or "bake into image", and justify in a sentence: (a) the 20 GB training dataset on the lab server's disk; (b) the Hugging Face model cache; (c) your `notebooks/` directory; (d) the Postgres data directory of your experiment tracker; (e) a 3 MB scikit-learn model that must ship atomically with the serving code.

<details>
<summary>Answer</summary>

(a) **Bind mount, read-only** (`:ro`) — it already lives on the host, multiple jobs share it, and nothing should ever write to it. (b) **Named volume** — containers own it, it must survive and be shared across runs, and it avoids one 5 GB download per container. (c) **Bind mount** — you edit with host tools and it must be in Git and backups; losing it to a `docker rm` is unacceptable. (d) **Named volume** — the canonical case: service-owned, write-heavy (CoW-hostile), no reason for a host path. (e) **Bake into the image** as its own layer — tiny, and versioning it with the code digest is exactly the requirement ([dockerfiles-for-data-science.md §8](dockerfiles-for-data-science.md)'s table, row 3).
</details>

**Exercise 2.** After a containerized training run on a shared server, `ls -l outputs/` on the host shows every checkpoint owned by `root`, and your colleague's cleanup script now fails. Why did this happen, and give two preventions for next time.

<details>
<summary>Answer</summary>

The container's process ran as UID 0 (root — the Docker default when no `USER` is set), and bind mounts carry raw numeric ownership straight onto the host filesystem, so its writes landed root-owned. Preventions: run as yourself — `docker run --user "$(id -u):$(id -g)" …`; or use/build images with a non-root default user (UID 1000 `appuser`/`jovyan`) per [dockerfiles-for-data-science.md §5](dockerfiles-for-data-science.md). (Cleanup after the fact needs `sudo chown -R` — the reason this is an *etiquette* issue on shared boxes.)
</details>

**Exercise 3.** `docker run -d --name api -p 8000:8000 my-api` then `docker run --rm curlimages/curl http://localhost:8000/health` fails to connect — yet `curl http://localhost:8000/health` from the host works. Explain both results and give two correct ways for the second container to reach the API.

<details>
<summary>Answer</summary>

From the **host**, the published port forwards `localhost:8000` into the container — works. Inside the **curl container**, `localhost` is its *own* network namespace's loopback, where nothing listens — fails. Correct routes: (1) put both on a shared user-defined network and use the name — `docker network create net; docker network connect net api; docker run --rm --network net curlimages/curl http://api:8000/health`; (2) go through the host's published port via `http://host.docker.internal:8000` (Desktop; `--add-host=…:host-gateway` on Linux). Route 1 is the idiomatic one — it's what Compose automates.
</details>

**Exercise 4.** A teammate proposes publishing Postgres with `-p 5432:5432` on your internet-reachable GPU server "so the training containers can reach it." Explain why this is both unnecessary and dangerous, and what to do instead.

<details>
<summary>Answer</summary>

Unnecessary: containers reach each other over a shared user-defined network by name (`db:5432`) with **no published port** — publishing is only for *host/outside* → container traffic. Dangerous: `-p 5432:5432` binds all host interfaces, offering the database to the entire internet (and Docker's forwarding can sidestep naive host-firewall rules) — scanners find open Postgres ports in minutes. Instead: attach `db` and the training containers to one network and publish nothing; if *humans* need occasional access from laptops, bind loopback only (`-p 127.0.0.1:5432:5432`) and connect through SSH tunnels.
</details>

**Exercise 5.** Your bind-mounted repo makes `pip install -e .` and Git operations painfully slow inside a container on your MacBook, but the identical setup is instant on the Linux CI box. Why — and name two mitigations that don't abandon containers.

<details>
<summary>Answer</summary>

On macOS the containers live in Docker Desktop's Linux VM ([container-internals.md §6](container-internals.md)); a bind mount crosses the macOS↔VM file-sharing boundary on **every file operation**, and repos + `site-packages` are exactly the many-small-files workload that boundary hates. Linux has no boundary — bind mounts are native. Mitigations: keep the hot, container-private paths (venvs, caches, `node_modules`-alikes) on **named volumes** (VM-native speed) while bind-mounting only the source you edit; use Docker Desktop's newer file-sharing backends (VirtioFS) / enable its sync features; or develop inside the container filesystem itself with a dev-container workflow ([ecosystem.md](ecosystem.md)) and let the IDE, not the FS boundary, do the bridging.
</details>

---

## Next / Related

- **Next:** [Ecosystem](ecosystem.md) — Podman, Kubernetes honestly sized, dev containers, and reproducible research.
- [Module 14 — Docker Compose](../14_cicd/docker-compose.md) — this chapter's flags, declared in YAML and taken to production.
- [Container internals](container-internals.md) — the namespaces and veth plumbing under every network in §4.
- [Dockerfiles for data science](dockerfiles-for-data-science.md) — the images these mounts and networks bring to life.
