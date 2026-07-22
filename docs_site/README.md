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
(`modules/`, `extras/`, `_static/`) from the repository's markdown and rewrites
relative links so they resolve in the built site. Those directories and
`_build/` are generated — edit the module READMEs in the repository instead,
then rebuild.

Two things `generate.py` does that are worth knowing when you edit a module:

- **Chapter order follows the README.** A mini-book module's sidebar lists its
  chapters in the order the module README first links to them, not
  alphabetically. Reorder the README's table of contents and the sidebar
  follows; add a chapter the README never links to and it still appears, at
  the end.
- **Links are rewritten by target.** Notebooks, scripts and other repo files
  become GitHub URLs; links to another module's directory or README become
  that module's page on this site; `../README.md` ("🏠 Course home") becomes
  this site's home page.

`make html` builds with `-W`, so an unresolved cross-reference fails the build
rather than shipping a dead link. `make linkcheck` additionally verifies that
external URLs still resolve.

## Publishing

The site is deployed automatically: the [Docs workflow](../.github/workflows/docs.yml)
builds it on every push to `main` and publishes `_build/html` to GitHub Pages at
<https://chrisw09.github.io/Python-for-AI-Driven-Automation/>. Pull requests that
touch markdown or `docs_site/` run the same build without publishing, so a broken
link fails the PR instead of the deployment. The build output is a plain static
site, so it would also work on Read the Docs or any static host.
