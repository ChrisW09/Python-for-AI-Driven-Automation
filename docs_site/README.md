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

Three things `generate.py` does that are worth knowing when you edit a module:

- **Chapter order follows the README.** A mini-book module's sidebar lists its
  chapters in the order the module README first links to them, not
  alphabetically. Reorder the README's table of contents and the sidebar
  follows; add a chapter the README never links to and it still appears, at
  the end.
- **Links are rewritten by target.** Notebooks, scripts and other repo files
  become GitHub URLs; links to another module's directory or README become
  that module's page on this site; `../README.md` ("🏠 Course home") becomes
  this site's home page.
- **The sidebar is grouped by hand, and checked.** `index.md` sorts the twenty
  modules into themed `{toctree}` blocks ("Python foundations", "Machine
  learning & applications", …) rather than one 20-entry `:glob:`, because a flat
  list of twenty is a wall rather than a table of contents. The cost is that a
  new module could be left out — so `generate.py` compares the tree against
  `index.md` first and aborts with the offending module's name if they differ.

Beyond the module guides the site also publishes the course-wide pages
(fast track, quizzes, datasets) and [`MAINTENANCE.md`](../MAINTENANCE.md) as
*For maintainers* — the same quarterly-currency checklist and verification
gates contributors run locally. Add another by putting it in `EXTRAS` in
`generate.py` and giving it a `{toctree}` entry in `index.md`.

`docs_site/root_files/` is copied verbatim to the site root (`html_extra_path`).
It holds `404.html`, which GitHub Pages serves for any unknown path: it is
deliberately a standalone file with absolute URLs and inline CSS, because a
themed page served from `/a/b/c/` cannot resolve its assets by relative path.

`make html` builds with `-W`, so an unresolved cross-reference fails the build
rather than shipping a dead link. `make linkcheck` additionally verifies that
external URLs still resolve — with localhost URLs and GitHub *anchor*
checks excluded in `conf.py`, since both report working links as broken.
It is not part of CI (external sites go down for reasons that are not your
bug), so run it before a release and read what it says.

## Publishing

The site is deployed automatically: the [Docs workflow](../.github/workflows/docs.yml)
builds it on every push to `main` and publishes `_build/html` to GitHub Pages at
<https://chrisw09.github.io/Python-for-AI-Driven-Automation/>. Pull requests that
touch markdown or `docs_site/` run the same build without publishing, so a broken
link fails the PR instead of the deployment. The build output is a plain static
site, so it would also work on Read the Docs or any static host.
