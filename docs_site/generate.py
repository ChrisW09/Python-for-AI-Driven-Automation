#!/usr/bin/env python3
"""Assemble the Sphinx source tree from the course's markdown documentation.

Copies every module README (as the module's index page) plus the mini-book
chapters (14_cicd, 17_django, 19_containers_docker, ...) into docs_site/,
rewriting links so they resolve in the built site:

  *.ipynb, *.py, *.cff, LICENSE, ...  ->  GitHub blob URLs
  ../NN_module/ (directory links)     ->  that module's index page
  chapter.md (same-directory links)   ->  kept (Sphinx resolves them)

Run from anywhere:  python3 docs_site/generate.py
The Makefile runs it automatically before every build.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
GITHUB_REPO = "https://github.com/ChrisW09/Python-for-AI-Driven-Automation"


def github_url(rel, is_dir: bool) -> str:
    """Repo path -> GitHub URL. Directories live under /tree/, files under
    /blob/ — get it wrong and every such link takes a redirect hop."""
    return f"{GITHUB_REPO}/{'tree' if is_dir else 'blob'}/main/{rel.as_posix()}"

MODULE_DIRS = sorted(
    d for d in ROOT.iterdir() if d.is_dir() and re.match(r"^\d{2}_", d.name)
)
EXTRAS = {
    "fast_track": ROOT / "fast_track" / "README.md",
    "quizzes": ROOT / "quizzes" / "README.md",
    "datasets": ROOT / "data" / "README.md",
}

LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)")


def rewrite_links(text: str, src_dir: Path, doc_dir: str) -> str:
    """Rewrite one file's relative links for its new home under docs_site/.

    src_dir: the directory the original file lives in (for resolving paths).
    doc_dir: the docs-tree directory of the copied file, relative to
             docs_site/ (e.g. "modules/14_cicd" or "extras").
    """

    def target_for(url: str) -> str | None:
        if url.startswith(("http://", "https://", "#", "mailto:")):
            return None
        path_part, _, anchor = url.partition("#")
        resolved = (src_dir / path_part).resolve()
        try:
            rel = resolved.relative_to(ROOT)
        except ValueError:
            return None  # points outside the repo — leave alone

        # Directory link or README link -> the page we copy it to (if any)
        if resolved.is_dir() or rel.name == "README.md":
            mod = rel.as_posix()
            if rel.name == "README.md":
                mod = mod.removesuffix("README.md").rstrip("/")
            prefix = "../" * (doc_dir.count("/") + 1)
            frag = f"#{anchor}" if anchor else ""
            if re.match(r"^\d{2}_[^/]+$", mod):
                return f"{prefix}modules/{mod}/index.md{frag}"
            slug = {"fast_track": "fast_track", "quizzes": "quizzes", "data": "datasets"}.get(mod)
            if slug:
                return f"{prefix}extras/{slug}.md{frag}"
            # The repository root README ("🏠 Course home") -> this site's home
            # page, so navigation stays on the site. An anchored link is the
            # exception: the site index is a short summary and won't have the
            # big README's headings, so send those to GitHub.
            if mod == "" and not anchor:
                return f"{prefix}index.md"
            return github_url(rel, resolved.is_dir()) + frag

        # Same-directory chapter .md links stay local (Sphinx resolves them)
        if rel.suffix == ".md" and resolved.parent == src_dir:
            return None

        # Chapter .md in another copied module -> that module's local page
        if rel.suffix == ".md" and re.match(r"^\d{2}_[^/]+/[^/]+\.md$", rel.as_posix()):
            prefix = "../" * (doc_dir.count("/") + 1)
            frag = f"#{anchor}" if anchor else ""
            return f"{prefix}modules/{rel.as_posix()}{frag}"

        # Everything else (.ipynb, .py, .csv, LICENSE, ...)
        return github_url(rel, resolved.is_dir()) + (f"#{anchor}" if anchor else "")

    def sub(m: re.Match) -> str:
        new = target_for(m.group(2))
        return m.group(0) if new is None else f"[{m.group(1)}]({new})"

    return LINK_RE.sub(sub, text)


def chapter_order(mod: Path, readme: str) -> list[str]:
    """Order a module's chapters the way its README introduces them.

    The mini-book modules are written to be read front to back, and their
    README's table of contents *is* that order. Sorting the files by name
    instead would put "Exercises" third and "Architecture" first — so take
    the order in which the README first links to each chapter, then append
    anything it never links to (alphabetically) so no page is lost.
    """
    files = {f.name for f in mod.glob("*.md")} - {"README.md"}
    ordered: list[str] = []
    for m in LINK_RE.finditer(readme):
        name = m.group(2).partition("#")[0]
        if name in files and name not in ordered:
            ordered.append(name)
    return ordered + sorted(files - set(ordered))


def main() -> None:
    for out in (HERE / "modules", HERE / "extras", HERE / "_static"):
        shutil.rmtree(out, ignore_errors=True)
        out.mkdir(parents=True)

    # The course hero image doubles as the site's social-preview card.
    shutil.copy(ROOT / "docs" / "images" / "hero.png", HERE / "_static" / "hero.png")

    module_pages = []
    for mod in MODULE_DIRS:
        readme = mod / "README.md"
        if not readme.exists():
            continue
        dest_dir = HERE / "modules" / mod.name
        dest_dir.mkdir(parents=True)
        doc_dir = f"modules/{mod.name}"

        raw_readme = readme.read_text()
        chapters = chapter_order(mod, raw_readme)
        body = rewrite_links(raw_readme, mod, doc_dir)
        if chapters:
            entries = "\n".join(c for c in chapters)
            body += (
                "\n\n```{toctree}\n:hidden:\n:maxdepth: 1\n\n"
                + entries
                + "\n```\n"
            )
        (dest_dir / "index.md").write_text(body)

        for ch in chapters:
            (dest_dir / ch).write_text(
                rewrite_links((mod / ch).read_text(), mod, doc_dir)
            )
        module_pages.append(f"modules/{mod.name}/index")

    for slug, src in EXTRAS.items():
        (HERE / "extras" / f"{slug}.md").write_text(
            rewrite_links(src.read_text(), src.parent, "extras")
        )

    print(f"generated {len(module_pages)} module sections + {len(EXTRAS)} extras")


if __name__ == "__main__":
    main()
