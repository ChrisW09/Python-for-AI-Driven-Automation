# Containers & Docker — from first principles

> 🧭  [◀ Compound AI Evaluation](../18_compound_ai_evaluation/)  ·  [🏠 Course home](../README.md)

Welcome. This module answers a question that [Module 14 (CI/CD, Docker & Deployment)](../14_cicd/) deliberately postpones: **what *is* a container, actually?**

Module 14 treats Docker as a tool in a pipeline — you write a `Dockerfile`, CI builds it, a server runs it, users are happy. That is the right altitude for shipping software. But the moment something goes wrong — an image is mysteriously 8 GB, a rebuild takes ten minutes, a GPU isn't visible inside the container, a "deleted" file is still bloating your image, your notebook's data vanishes on restart — you need the level *below* the tool. You need to know what an image really is on disk, what the kernel actually does when a container starts, and why the whole thing works at all.

That is this module. No pipelines, no servers, no domains — just containers, opened up like a watch: images and layers, the overlay filesystem, namespaces and cgroups, and the Dockerfile patterns that matter specifically for **Python, data-science, and AI workloads** (which are heavier, weirder, and more GPU-shaped than the average web app).

> 💡 **Intuition:** Module 14 teaches you to *drive the car* — accelerate, brake, follow the road to production. This module opens the hood: engine, transmission, and why the dashboard lights mean what they mean. You can drive without it. You cannot *fix* anything without it.

Although this module is numbered 19, it pairs naturally with Module 14 and has **no dependency on modules 15–18**. You can read it *before* Module 14 (fundamentals first, then the pipeline) or *after* (pipeline first, then the deep-dive). Both orders work; the cross-links go both ways.

---

## What you'll learn

By the end of this module you will be able to:

- Explain **why containers exist** — the isolation and reproducibility problem — and where they came from (`chroot` → jails → LXC → Docker → the **OCI**, the Open Container Initiative).
- Say precisely how a **container differs from a virtual machine**, and name the situations where a container is the *wrong* tool.
- Describe an **OCI image** as it really is: content-addressed layers, a manifest, and a config — and read all three with `docker image inspect`.
- Explain **copy-on-write** and **OverlayFS** (the union filesystem Docker uses), and predict which layer a file read or write actually touches.
- Predict **build-cache** hits and misses, and explain why deleting a file in a later layer does *not* shrink an image.
- Narrate what happens on **`docker run`**: the client → daemon → `containerd` → `runc` chain, the six Linux **namespaces**, **cgroups v2** resource limits, and (in one paragraph each) capabilities and seccomp.
- Explain why *"containers share the host kernel"* and its consequences — including why Docker Desktop on macOS/Windows secretly runs a Linux virtual machine.
- Write **production-quality Dockerfiles for data-science and AI workloads**: slim vs full base images, layer ordering, multi-stage builds, non-root users, `pip`/`uv` cache mounts, GPU (CUDA) images, Jupyter in a container, and keeping multi-gigabyte model files out of your images.
- Persist data with **bind mounts and named volumes**, publish ports, and wire containers together over **container networks** with built-in DNS (Domain Name System) between them.
- Place Docker in its **ecosystem**: Podman, `containerd`, CRI-O, an honest one-page look at Kubernetes (and when you do *not* need it), dev containers, and Docker for reproducible research.

---

## Table of contents (read in this order)

Each chapter builds on the previous one. Read top to bottom.

| # | Chapter | What it covers |
|---|---|---|
| 1 | **README** (this file) | The map, the vocabulary, and how this module relates to Module 14 |
| 2 | [Why containers](why-containers.md) | The isolation/reproducibility problem, a short history, containers vs VMs in depth, and when a container is the wrong tool |
| 3 | [Images & layers](images-and-layers.md) | The OCI image format: layers, copy-on-write, OverlayFS, digests vs tags, manifests, and build-cache mechanics |
| 4 | [Container internals](container-internals.md) | What `docker run` actually does: namespaces, cgroups v2, the daemon → containerd → runc chain, and the shared kernel |
| 5 | [Dockerfiles for data science](dockerfiles-for-data-science.md) | Base images, pinning, cache mounts, multi-stage builds, GPU images, Jupyter, and model files — the Python/AI-specific playbook |
| 6 | [Volumes & networking](volumes-and-networking.md) | Bind mounts vs named volumes, persisting notebooks/models/databases, ports, and container-to-container DNS |
| 7 | [Ecosystem](ecosystem.md) | Podman, containerd, CRI-O, an honest look at Kubernetes, dev containers, reproducible research, and a glossary |
| 8 | [Exercises](exercises.md) | Hands-on challenges, easy → hard, with answer keys |

---

## Hands-on lab notebook

The chapters explain the machinery; the **lab notebook** lets you build a working model of it in pure Python — no Docker installation, no internet, 100% offline.

| Notebook | ⏱ Time | Companion chapters | What you do |
|---|---|---|---|
| [`lab01_container_anatomy.ipynb`](lab01_container_anatomy.ipynb) | ~60 min | [Images & layers](images-and-layers.md), [Container internals](container-internals.md) | Build content-addressed image layers with `hashlib`, implement copy-on-write reads, simulate an OverlayFS lookup (upper/lower dirs, whiteouts), replay build-cache invalidation, and model PID-namespace isolation with plain Python objects |

Every simulation is grounded in the real command it mirrors — you'll see the actual `docker` command next to the toy version, so when you later run the real thing you already know what it's doing underneath. The lab uses the same scaffolding as the rest of the course: ✋ checkpoints, 🧪 practice exercises, a 🎁 mini-project, and 🧠 key takeaways.

---

## How this module relates to Module 14

The two modules are complements, not alternatives. Module 14 is **breadth across the pipeline**; this module is **depth on one box of that pipeline**. Here is the explicit map of which topics live where:

| Topic | Lives in **Module 14** | Lives in **Module 19** (here) |
|---|---|---|
| Why containers exist (the "works on my machine" problem) | [docker.md §1](../14_cicd/docker.md) — the short version | [why-containers.md](why-containers.md) — the full story, with history and honest limits |
| Containers vs virtual machines | [docker.md §2](../14_cicd/docker.md) — one section | [why-containers.md](why-containers.md) — in depth, including performance and security trade-offs |
| Writing a `Dockerfile`, line by line | [docker.md §10](../14_cicd/docker.md) — the canonical FastAPI tutorial | [dockerfiles-for-data-science.md](dockerfiles-for-data-science.md) — assumes that tutorial; adds the data-science/GPU-specific patterns |
| Layers and the build cache | [docker.md §5](../14_cicd/docker.md) — the ordering rule | [images-and-layers.md](images-and-layers.md) — the mechanism: content addressing, OverlayFS, whiteouts, digests |
| What happens at `docker run` | — (treated as a black box) | [container-internals.md](container-internals.md) — namespaces, cgroups, runc |
| Volumes & container networking | [docker.md §7–8](../14_cicd/docker.md) — enough to run the example app | [volumes-and-networking.md](volumes-and-networking.md) — the full model, plus data-science persistence patterns |
| Docker Compose | [docker-compose.md](../14_cicd/docker-compose.md) — full chapter | Only bridged to, at the end of [volumes-and-networking.md](volumes-and-networking.md) |
| Registries (push/pull, GHCR) | [registries.md](../14_cicd/registries.md) — full chapter | Only the *storage format* side (digests, manifests) in [images-and-layers.md](images-and-layers.md) |
| CI/CD, GitHub Actions, DNS, HTTPS, deployment, monitoring | Modules 14's remaining chapters | **Not here** — follow the links to Module 14 |
| Kubernetes, Podman, dev containers, reproducible research | — | [ecosystem.md](ecosystem.md) |

**Reading-order advice:**

- **New to Docker entirely?** Read [why-containers.md](why-containers.md) and [images-and-layers.md](images-and-layers.md) here, then jump to [Module 14's docker.md](../14_cicd/docker.md) to learn the hands-on commands and Dockerfile writing, then come back for the rest.
- **Already through Module 14?** Read this module straight through — every chapter will snap concepts you've *used* into concepts you *understand*.

---

## Prerequisites

You should be comfortable with:

- **Python 3** — functions, dicts, classes (Module 1 level).
- Using a **terminal / command line** — running commands, navigating directories.
- **Git** basics — enough to know what a commit hash is (that intuition transfers directly to image digests).

You do **not** need:

- Docker installed — the lab notebook is pure Python, and every real command in the chapters is reference material you can run later. (To actually run the commands, install **Docker Desktop** on macOS/Windows or **Docker Engine** on Linux.)
- Module 14 — the two modules cross-link but neither strictly requires the other.
- A server, a domain, or any cloud account.

> 💡 **Intuition:** This module is deliberately the *cheapest* infrastructure module in the course: everything runs on your laptop or in your head. The expensive parts — servers, domains, pipelines — live in Module 14.

---

## Why this matters for data scientists specifically

You might wonder whether kernel namespaces are really your problem. They are, for three reasons:

1. **Reproducibility is your product.** A model score you cannot reproduce is a rumor. Containers are the strongest practical tool for freezing an analysis environment — Python version, BLAS (Basic Linear Algebra Subprograms) library, CUDA version, every transitive dependency — so that a result from March still computes in November. [ecosystem.md](ecosystem.md) treats this in depth.
2. **Data-science images are pathological.** PyTorch with CUDA support is multiple gigabytes *before* your code arrives. Naive Dockerfiles that are merely "slow" for a web app become unusable for ML work. The patterns in [dockerfiles-for-data-science.md](dockerfiles-for-data-science.md) — cache mounts, multi-stage builds, model-file discipline — exist precisely because of this.
3. **You will debug through abstractions.** "CUDA driver version is insufficient", "Killed" (the out-of-memory killer), "permission denied" on a mounted volume — every one of these errors is *only* explicable at the level of [container-internals.md](container-internals.md). Knowing the internals turns a lost afternoon into a five-minute fix.

---

## Estimated time

| Activity | Approx. time |
|---|---|
| Read README + Why containers (the mental model) | 45–60 min |
| Read Images & layers + Container internals (the deep core) | 2–3 hours |
| Read the data-science Dockerfile + volumes/networking chapters | 1.5–2 hours |
| Work through [`lab01_container_anatomy.ipynb`](lab01_container_anatomy.ipynb) | ~60 min |
| Read Ecosystem + complete the [Exercises](exercises.md) | 1.5–2 hours |
| **Total** | **roughly 7–9 hours**, comfortably spread over a few days |

---

## A quick self-check

Before moving on, see whether you can already answer these. If some feel shaky — good, that's the module doing its job. Answers are hidden below.

1. A container and a virtual machine both isolate software. What is the single biggest *structural* difference between them?
2. Two image tags, `myapp:latest` on your laptop and `myapp:latest` on a server, can point at different bytes. Why can two image *digests* never do that?
3. Your Dockerfile ends with `RUN rm -rf /var/cache/big-stuff`. Does the final image get smaller? Why or why not?
4. Why does Docker on macOS need a virtual machine at all, when Docker on Linux doesn't?

<details>
<summary>Show answers</summary>

1. A VM (virtual machine) boots its **own kernel** on simulated hardware; a container **shares the host's Linux kernel** and is isolated only by kernel features (namespaces, cgroups). Details in [why-containers.md](why-containers.md).
2. A **tag** is a mutable label anyone can re-point; a **digest** is the SHA-256 hash *of the image content itself* — same digest mathematically implies same bytes. Details in [images-and-layers.md](images-and-layers.md).
3. **No.** Layers are immutable and additive: the deleted files still exist in the earlier layer; the `RUN rm` merely adds a later layer that *hides* them (a whiteout). To actually shrink the image you must avoid adding the files in the first place, or use a multi-stage build. Details in [images-and-layers.md](images-and-layers.md) and [dockerfiles-for-data-science.md](dockerfiles-for-data-science.md).
4. Because containers are a **Linux-kernel** feature — namespaces and cgroups don't exist in the macOS (or Windows) kernel. Docker Desktop therefore runs a hidden Linux VM and your containers live inside it. Details in [container-internals.md](container-internals.md).

</details>

---

## Next / Related

- **Next:** [Why containers](why-containers.md) — the problem, the history, and the honest limits.
- [Images & layers](images-and-layers.md) — the single most useful chapter if you only read one.
- [Module 14 — CI/CD, Docker & Deployment](../14_cicd/) — the pipeline this module's fundamentals plug into.

---

📝 **Finished this module?** Test yourself with the [Module 19 quiz](../quizzes/quiz_19_containers_docker.ipynb) — five questions, ~10 minutes.
