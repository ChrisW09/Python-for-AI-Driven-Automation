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

## Publishing (optional)

The `_build/html` directory is a static site — it can be published as-is via
GitHub Pages (e.g. a workflow that runs `make html` and uploads
`docs_site/_build/html`), Read the Docs, or any static host.
