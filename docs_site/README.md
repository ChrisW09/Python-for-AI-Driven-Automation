# Course documentation site (Sphinx)

A browsable documentation site generated from the course's own markdown:
every module guide, the full mini-book chapters (CI/CD, Django, Containers &
Docker), and the fast-track / quiz / dataset guides — with every notebook
link pointing at GitHub (one click from there into Colab).

## Build

```bash
pip install -r docs_site/requirements.txt
cd docs_site
make html
open _build/html/index.html        # Windows: start _build\html\index.html
```

`make html` first runs `generate.py`, which assembles the Sphinx source tree
(`modules/`, `extras/`) from the repository's markdown and rewrites relative
links so they resolve in the built site. Those two directories and `_build/`
are generated — edit the module READMEs in the repository instead, then
rebuild.

## Publishing

The site is deployed automatically: the [Docs workflow](../.github/workflows/docs.yml)
builds it on every push to `main` and publishes `_build/html` to GitHub Pages at
<https://chrisw09.github.io/Python-for-AI-Driven-Automation/>. The build output
is a plain static site, so it would also work on Read the Docs or any static host.
