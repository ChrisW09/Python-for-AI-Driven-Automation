# Python for AI-Driven Automation & Business Data Science

From your first line of Python to shipping a real AI-driven automation — a hands-on curriculum (self-paced *or* instructor-led) across Python fluency, business data science, machine learning, deep learning, AI engineering, and production.

<figure class="course-arc">
  <img src="_static/arc.png" alt="The arc of the course, from Foundations through Data Science, Machine Learning, Deep Learning, AI Engineering and Agents &amp; MCP, to Production.">
</figure>

<ul class="course-stats">
  <li><b>134</b> runnable notebooks</li>
  <li><b>20</b> modules</li>
  <li><b>300+</b> exercises</li>
  <li><b>389</b> in-lesson checkpoints</li>
  <li><b>100%</b> offline</li>
</ul>

This site is the reference documentation for the course: one section per module (the module guides, plus the full mini-book chapters for CI/CD, Django, and Containers & Docker), together with the fast track, quizzes, and dataset guides. The notebooks themselves live in the [GitHub repository](https://github.com/ChrisW09/Python-for-AI-Driven-Automation) — every notebook link on this site takes you straight to it, and each one can be opened in Google Colab with one click.

## Where to start

- **New to the course?** Start with the [onboarding module](modules/00_onboarding/index.md), or get a taste in 5 minutes with the [*See it work* notebook](https://github.com/ChrisW09/Python-for-AI-Driven-Automation/blob/main/00_onboarding/00c_see_it_work.ipynb) — an offline demo of the finished shapes, before any Python.
- **Short on time?** The [fast track](extras/fast_track.md) condenses the whole course into 22 notebooks (~26.5 h).
- **Here for one topic?** The sidebar is grouped by theme — jump straight to the module you need; each one names its prerequisites at the top.
- **Checking what stuck?** Every content module has a short [quiz](extras/quizzes.md).

## The shape of the course

The twenty modules fall into six stretches, and the sidebar groups them the same way.

**Python foundations** (modules 1–4) build the language itself, then the data stack — pandas, NumPy, plotting, statistics and time series — and finally how data actually arrives: HTTP APIs, SQL, validation, and web scraping.

**Machine learning & applications** (5–7) covers scikit-learn and honest evaluation, deep learning with PyTorch, and then the module where the tools become the job: [Industry Applications](modules/07_industry_applications/index.md), whose four core notebooks and fourteen full-weight appendices all run the same spine — *model → money → decision*.

**AI engineering & agents** (8–10) layers LLMs on top of that: prompting, RAG, document processing, evaluation and observability, three proof-of-concept builds, then agent architectures and the Model Context Protocol.

**Production & delivery** (13–14) turns notebooks into projects, schedules them, and ships them — Docker, GitHub Actions, registries, HTTPS and a real deployment.

**Capstones & business** (15–16) proves the whole thing end to end, then steps back to digital transformation, architecture patterns and AI governance.

**Optional tracks** run alongside: text analytics and deep tabular learning (11–12), and three closers — Django, compound-AI evaluation, and containers (17–19). All are fully offline, like everything else.

## How to read a module page

Each module page is that module's own guide: what you'll learn, the notebooks
in order with time estimates and difficulty, the exercises, and how it connects
to the modules on either side. Notebook names link straight to GitHub, where the
Colab badge at the top of every notebook opens it in a browser — nothing to
install. The three mini-book modules ([CI/CD](modules/14_cicd/index.md),
[Django](modules/17_django/index.md), and
[Containers & Docker](modules/19_containers_docker/index.md)) additionally have
their full prose chapters here, listed in the sidebar in reading order.

Every lesson is built the same way: short teaching sections broken up by **✋ quick-exercise
checkpoints** with collapsible solutions, then graded practice, stretch problems and a bonus
mini-project. All 389 checkpoint solutions are executed in a fresh kernel before release, so
the code on these pages is code that runs.

## Browse the course

```{toctree}
:caption: Start here
:maxdepth: 1

modules/00_onboarding/index
```

```{toctree}
:caption: Python foundations
:maxdepth: 1

modules/01_foundations/index
modules/02_data_science/index
modules/03_real_world_io/index
modules/04_webscraping/index
```

```{toctree}
:caption: Machine learning & applications
:maxdepth: 1

modules/05_machine_learning/index
modules/06_pytorch/index
modules/07_industry_applications/index
```

```{toctree}
:caption: AI engineering & agents
:maxdepth: 1

modules/08_ai_engineering/index
modules/09_building_ai_pocs/index
modules/10_agents_tools_mcp/index
```

```{toctree}
:caption: Optional: text & tabular
:maxdepth: 1

modules/11_nlp/index
modules/12_deeptab/index
```

```{toctree}
:caption: Production & delivery
:maxdepth: 1

modules/13_production/index
modules/14_cicd/index
```

```{toctree}
:caption: Capstones & business
:maxdepth: 1

modules/15_capstones/index
modules/16_business_ai/index
```

```{toctree}
:caption: Optional closers
:maxdepth: 1

modules/17_django/index
modules/18_compound_ai_evaluation/index
modules/19_containers_docker/index
```

```{toctree}
:caption: Course-wide
:maxdepth: 1

extras/fast_track
extras/quizzes
extras/datasets
```

```{toctree}
:caption: For maintainers
:maxdepth: 1

extras/maintenance
```
