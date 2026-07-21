# The ecosystem — beyond `docker`

You now know the format (OCI images), the machinery (namespaces, cgroups, overlay mounts), and the craft (data-science Dockerfiles, mounts, networks). This closing chapter zooms out to the landscape: the other tools that speak the same standards, an honest one-page sizing of Kubernetes, the dev-container workflow that may quietly become your daily driver, and the case — dear to this course — for containers as the backbone of **reproducible research**. A glossary closes the module.

The through-line is the punchline of [why-containers.md §2](why-containers.md): since 2015, "container" names an **open standard, not a product**. Everything below interoperates because everything implements the same three OCI (Open Container Initiative) specs — image, runtime, distribution.

---

## 1. The cast of characters

[Container-internals §2](container-internals.md) showed Docker decomposing into a chain: CLI → `dockerd` → `containerd` → `runc`. The ecosystem is largely *that chain, re-assembled by different vendors for different hosts*:

| Tool | What it is | When you'll meet it |
|---|---|---|
| **Docker (Engine/Desktop)** | The full developer-experience stack: CLI, daemon, builder, Compose, Desktop VM | Your laptop; small servers (all of Module 14) |
| **containerd** | The lifecycle core (pull, store, run via runc) — Docker minus the developer porcelain | Inside Docker; as the runtime on most Kubernetes nodes; behind cloud container services |
| **runc** | The reference OCI runtime — creates the namespaced/cgrouped process, then exits | The bottom of every stack above (swap-ins: gVisor, Kata, Firecracker-based runtimes for harder isolation) |
| **Podman** | A daemonless, rootless-first Docker-CLI clone | Red Hat-family Linux; security-conscious shops; HPC-adjacent settings |
| **CRI-O** | A minimal runtime implementing exactly Kubernetes's CRI (Container Runtime Interface), nothing else | Kubernetes nodes (OpenShift especially); you operate it only if you operate clusters |
| **Buildah / kaniko / BuildKit** | Image *builders* decoupled from any daemon | CI systems building images without privileged Docker daemons |
| **Singularity/Apptainer** | Container runtime for HPC (high-performance computing) clusters — unprivileged by design, images as single files | University clusters and supercomputers, where Docker daemons are forbidden; it runs converted OCI images |

**Podman deserves its own paragraph**, because it's the one you might actually *choose*. Its two architectural differences from Docker: **no daemon** — `podman run` forks the container directly (your shell → conmon → runc → process), so there's no root background service and no all-powerful socket ([container-internals.md §2](container-internals.md)'s warning about `docker.sock` simply has no referent); and **rootless by default** — using user namespaces ([container-internals.md §3](container-internals.md)) so an unprivileged user runs full containers, with "root" inside mapped to their own UID outside. The CLI is deliberately compatible (`alias docker=podman` mostly works, images are the same OCI images, Dockerfiles build unchanged, `podman compose` runs Compose files), so your knowledge transfers ~1:1. Trade-offs: Docker Desktop's polish and ecosystem integrations still lead on Mac/Windows, and some tooling assumes the Docker socket exists. Takeaway: you learned the *format and the model* in this module — the brand of client is a detail.

---

## 2. Kubernetes — the honest one-pager

**What it is.** **Kubernetes** ("K8s") is a **container orchestrator**: software that runs containers across a *fleet* of machines and continuously reconciles reality against a declared desired state. You submit YAML saying "eight replicas of `ghcr.io/…/model-api:9f3c1ab`, each needs 2 CPU + 4 GB + 1 GPU, spread across failure zones, roll updates gradually, restart what dies" — and the control plane schedules **pods** (groups of containers) onto **nodes** (machines running containerd/CRI-O; note: not Docker), watches them, and repairs drift forever. Around that core: **Services** (stable virtual IPs/DNS load-balancing across pod replicas — [volumes-and-networking.md §4](volumes-and-networking.md)'s name-based wiring, generalized to a cluster), **Ingress** (the cluster-wide reverse proxy — Module 14's Nginx receptionist, as an API object), autoscaling, secrets/config objects, and persistent-volume plumbing. It is genuinely excellent engineering, it won the orchestration war completely, and for ML platforms at scale (Kubeflow, Ray-on-K8s, every cloud's GPU clusters) it is the substrate.

**What it costs.** A steep learning curve (a dozen new object kinds before "hello world"), meaningful operational burden even on managed clouds (upgrades, networking add-ons, observability, RBAC — role-based access control), and an ecosystem whose complexity compounds (Helm charts, operators, service meshes). Kubernetes solves *coordination across many machines under change* — if you don't have that problem, you're paying its costs to solve a problem you don't have.

**When you do NOT need it** — which, for this course's audience, is *most of the time*:

- **One server can hold your workload.** A modern box (or one rented GPU machine) plus [Docker Compose with `restart: unless-stopped`](../14_cicd/docker-compose.md), shipped by [Module 14's CI pipeline](../14_cicd/github-actions.md), gives you self-healing, ordered startup, and one-command deploys — the honest 80% of orchestration value at 5% of the complexity. That is precisely why Module 14 teaches that stack.
- **Your "scaling" is batch jobs, not always-on traffic.** Nightly retrains and backfills want a job scheduler (cron, Airflow, cloud batch/serverless-container services), not a standing cluster.
- **You'd be a cluster of one admin.** Kubernetes assumes an operator; a data scientist alone is better served spending that attention on the model.
- Honest **upgrade triggers**: multiple machines that must act as one pool; real elasticity needs (traffic or GPU-job queues that outgrow any single box); many teams sharing infrastructure with quotas and isolation; availability requirements that survive a machine dying at 3 a.m. When several of those arrive, reach for a *managed* offering (EKS/GKE/AKS) — and notice that everything in this module transfers: same images, same registries, same layer/caching discipline, same volumes-and-DNS mental model, bigger YAML.

> 💡 **Intuition:** Compose is a **thermostat** — one device, declared target, simple feedback loop, fits on one wall. Kubernetes is a **building-management system** — hundreds of devices, zones, failover chillers, a control room, and a staff. Magnificent for an airport; a very silly way to heat an apartment.

---

## 3. Dev containers — the environment as part of the repo

A **dev container** flips this module's artifact around: instead of packaging the app *for running elsewhere*, you package the **development environment itself**, and your editor moves *inside* it. VS Code (and GitHub Codespaces, JetBrains, and the open `devcontainer` CLI — it's a published spec) reads a `.devcontainer/devcontainer.json` in the repo, builds/starts the container, mounts your source into it, and reconnects the editor's backend inside — terminal, debugger, extensions, kernels all run in the container, while the UI stays native.

```jsonc
// .devcontainer/devcontainer.json
{
  "name": "course-ds-env",
  "build": { "dockerfile": "Dockerfile" },        // or "image": "ghcr.io/org/ds-env:digest…"
  "runArgs": ["--gpus", "all", "--shm-size=2g"],  // the flags from dockerfiles-for-data-science.md
  "mounts": [
    "source=hf-cache,target=/home/vscode/.cache/huggingface,type=volume"
  ],
  "customizations": {
    "vscode": { "extensions": ["ms-python.python", "ms-toolsai.jupyter"] }
  },
  "forwardPorts": [8888],
  "postCreateCommand": "uv sync --frozen",
  "remoteUser": "vscode"                          // non-root, UID-1000 — §5 of volumes-and-networking
}
```

Why this lands especially well for data science: **onboarding** becomes "clone, reopen in container" — the new teammate gets CUDA, the pinned lockfile environment, and the right Python in minutes, on any OS; **"works on my machine" dies at development time**, not just deploy time, because everyone (and CI, and Codespaces) shares one pinned image; and it's the cleanest answer to [volumes-and-networking.md §6 Exercise 5](volumes-and-networking.md)'s macOS bind-mount slowness — the heavy filesystem traffic happens *inside* the container while the editor bridges in. Note the composability: every line of that JSON is a concept you already own — a Dockerfile, run flags, mounts, ports, a non-root user. Dev containers are this module's material with an editor attached.

---

## 4. Containers for reproducible research

This course keeps insisting that an analysis is a *claim*, and claims need to be checkable. Here is where the whole module cashes out for science. The reproducibility tower from [why-containers.md §1](why-containers.md) — OS, native libs, interpreter, packages, config — is exactly what peer reviewers, future-you, and your Module 18-style evaluation runs cannot otherwise reconstruct. The container discipline for a checkable computational claim:

1. **A `Dockerfile` in the repo**, base image **pinned by digest** ([images-and-layers.md §4](images-and-layers.md)).
2. **A lockfile** driving every install ([dockerfiles-for-data-science.md §2](dockerfiles-for-data-science.md)) — the Dockerfile contains *no* unpinned `pip install`/`apt-get install` of moving targets.
3. **Data and outputs outside the image**: read-only input mounts, versioned/checksummed datasets, outputs to a mounted directory ([volumes-and-networking.md §2](volumes-and-networking.md)) — the image is *code+environment*, not a data warehouse.
4. **Run offline where feasible**: `docker run --network none …` turns "no hidden downloads" from a hope into an enforced property — if it runs air-gapped, its inputs are provably pinned.
5. **Archive the built image itself** for the paper/report: push to a registry **and record the digest** in the README/citation; for long-horizon archiving, `docker save image | gzip > env.tar.gz` deposited with the data (e.g., Zenodo) — registries and tags rot on decade timescales; a tarball plus its digest doesn't.
6. **One command reproduces it**: `docker run --rm -v "$PWD/data":/data:ro -v "$PWD/out":/out ghcr.io/…@sha256:… python analysis.py` — pasteable into a paper's appendix.

The scientific ecosystem has standardized around exactly this stack: **Binder / `repo2docker`** turn a Git repo into a live containerized Jupyter environment for readers; workflow engines (**Nextflow, Snakemake**) run every pipeline step in a per-step container; **Apptainer** carries the same images onto HPC clusters; journals increasingly accept or request container images alongside code. And you've already met the pain this tames inside this course: [Module 18's CAFE setup](../18_compound_ai_evaluation/) needs Python ≥ 3.11 *plus* an R installation — a two-runtime tower that a single pinned image reduces to `docker run`.

> ⚠️ **Common mistake:** "It's in Docker, so it's reproducible." A Dockerfile full of `FROM python:latest` and unpinned installs is **irreproducibility, containerized** — it freezes nothing; it just relocates the drift into the build. The *image* (a digest) is reproducible by construction; a *Dockerfile* is only as reproducible as its pins. Ship both: the Dockerfile for transparency, the digest for certainty.

---

## 5. Glossary

Quick-reference definitions for every load-bearing term in this module (chapter of first serious treatment in parentheses):

| Term | Definition |
|---|---|
| **OCI** | Open Container Initiative — the standards body for the image, runtime, and distribution specs ([why-containers](why-containers.md)) |
| **Image** | Immutable, layered filesystem bundle + config, addressed by digest ([images-and-layers](images-and-layers.md)) |
| **Container** | A process (tree) with private namespaces, a cgroup, and an overlay-mounted image as its root ([container-internals](container-internals.md)) |
| **Layer** | One tar archive of filesystem changes (adds/modifies/whiteouts) against the layers below ([images-and-layers](images-and-layers.md)) |
| **Whiteout** | Marker entry in a layer that hides a lower layer's file — deletions never reclaim space ([images-and-layers](images-and-layers.md)) |
| **Copy-on-write (CoW)** | Reads search down the stack; modifying a lower file first copies it, in full, into the writable layer ([images-and-layers](images-and-layers.md)) |
| **OverlayFS** | The Linux union filesystem (lowerdir/upperdir/merged) that composes layers at mount time ([images-and-layers](images-and-layers.md)) |
| **Digest** | SHA-256 hash of an artifact's bytes — content-addressed, immutable identity (vs. **tag**: a mutable name) ([images-and-layers](images-and-layers.md)) |
| **Manifest** | The JSON listing an image's config + layer digests; a **manifest list/index** maps platforms to manifests ([images-and-layers](images-and-layers.md)) |
| **Build cache** | Per-instruction layer reuse, keyed on parent + instruction text + copied-file content ([images-and-layers](images-and-layers.md)) |
| **Cache mount** | BuildKit's build-time-only persistent directory (`RUN --mount=type=cache`) — speeds rebuilds, adds no layer weight ([dockerfiles-for-data-science](dockerfiles-for-data-science.md)) |
| **Multi-stage build** | Several `FROM` stages in one Dockerfile; only what's `COPY --from`ed survives into the final image ([dockerfiles-for-data-science](dockerfiles-for-data-science.md)) |
| **Namespace** | Kernel-provided private view of one machine aspect — pid, net, mnt, uts, ipc, user ([container-internals](container-internals.md)) |
| **cgroup** | Kernel resource accounting/limiting for a process group — memory kills (exit 137), CPU throttles ([container-internals](container-internals.md)) |
| **Capabilities / seccomp** | Root's powers split into grantable pieces / a syscall allowlist — the default in-container hardening ([container-internals](container-internals.md)) |
| **runc / containerd / shim** | OCI runtime that creates the process / the lifecycle manager above it / the per-container babysitter between them ([container-internals](container-internals.md)) |
| **Bind mount / named volume / tmpfs** | Host path grafted in / Docker-managed persistent directory / RAM-backed scratch ([volumes-and-networking](volumes-and-networking.md)) |
| **Bridge network / veth** | Virtual switch joining containers / the virtual cable pair attaching each namespace to it ([volumes-and-networking](volumes-and-networking.md)) |
| **Port publishing** | Host-port → container-port forwarding (`-p`); `EXPOSE` merely documents ([volumes-and-networking](volumes-and-networking.md)) |
| **Registry** | HTTP service storing images by digest under tags — the warehouse ([Module 14 registries](../14_cicd/registries.md)) |
| **Podman** | Daemonless, rootless-first, Docker-compatible engine ([this chapter](#1-the-cast-of-characters)) |
| **Kubernetes** | Multi-machine container orchestrator: declared desired state, continuously reconciled ([this chapter](#2-kubernetes--the-honest-one-pager)) |
| **Dev container** | A repo-declared containerized development environment your editor attaches into ([this chapter](#3-dev-containers--the-environment-as-part-of-the-repo)) |

---

## 6. Exercises

**Exercise 1.** Your university's HPC cluster forbids Docker ("no root daemons on shared nodes") but offers Apptainer; your workstation uses Docker. A colleague concludes you must maintain two separate environment definitions. Correct them, citing the standards involved.

<details>
<summary>Answer</summary>

One definition suffices: the Dockerfile builds an **OCI image**, and OCI images are the lingua franca — Apptainer converts/pulls OCI images directly (`apptainer pull docker://ghcr.io/org/env@sha256:…`), and Podman (daemonless, rootless — often permitted where Docker isn't) runs them unchanged. The cluster's objection is to Docker's *architecture* (root daemon, socket), not to the *format*. Build once, pin the digest, run under whichever OCI-speaking runtime each machine allows.
</details>

**Exercise 2.** A three-person team serves one internal model API (steady ~5 requests/second) from a single GPU server, deployed via Module 14's Compose + GitHub Actions pipeline. Their new lead proposes migrating to Kubernetes "for scalability and self-healing." Which claimed benefits do they *already have*, and what would be the honest triggers to revisit?

<details>
<summary>Answer</summary>

Already covered: **self-healing** (`restart: unless-stopped` restarts crashes and survives reboots), **automated repeatable deploys** (the CI pipeline), **health-gated startup** (Compose healthchecks), and capacity — 5 req/s doesn't stress one box, and K8s adds no GPUs. The migration would add cluster operations, RBAC, networking add-ons, and a learning curve, for coordination-across-machines value they don't need. Honest revisit triggers: workload outgrowing the single box (sustained load or queued GPU jobs), a real availability requirement beyond one machine's uptime, multiple teams needing quota'd shared infrastructure — and then via a managed cluster, reusing the same images and registry discipline unchanged.
</details>

**Exercise 3.** Design the reproducibility appendix for a results-bearing analysis (a paper or an important business report): list the artifacts you'd publish and the one-line run command, and state what each artifact pins.

<details>
<summary>Answer</summary>

Publish: (1) the **repo at a tagged commit** — code; (2) the **Dockerfile** with base pinned by digest — environment recipe, transparent; (3) the **lockfile** — every Python package, exact versions/hashes; (4) the **built image's digest** (pushed to a registry) plus, for long-horizon archiving, a `docker save` tarball deposited alongside the data — environment as bytes, certain; (5) **checksummed input data** (or its versioned DOI). Run command: `docker run --rm --network none -v "$PWD/data":/data:ro -v "$PWD/out":/out ghcr.io/org/paper-env@sha256:… python -m analysis` — `--network none` proving no hidden downloads, `:ro` protecting inputs, outputs landing outside the container. Together: same code + same environment + same data + no network = same numbers, checkable by a stranger in one command.
</details>

---

## Next / Related

- [Exercises](exercises.md) — the module's consolidated exercise bank, easy → hard.
- [`lab01_container_anatomy.ipynb`](lab01_container_anatomy.ipynb) — if you haven't run the lab yet, this is the moment.
- [Module 14 — CI/CD, Docker & Deployment](../14_cicd/) — take these fundamentals to a live, shipping system.
