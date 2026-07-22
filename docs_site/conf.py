# Sphinx configuration for the course documentation site.
# Build with:  make html   (from docs_site/) — runs generate.py first.

project = "Python for AI-Driven Automation & Business Data Science"
author = "Christoph Weisser"
copyright = "2026, Christoph Weisser"

extensions = ["myst_parser", "sphinxcontrib.mermaid"]

# Only the curated tree built by generate.py is part of the docs.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md"]

source_suffix = {".md": "markdown", ".rst": "restructuredtext"}

# Generate #anchors for headings so chapter cross-links like
# images-and-layers.md#7-build-cache resolve.
myst_heading_anchors = 4
myst_enable_extensions = ["colon_fence"]
# Render ```mermaid fences as diagrams (via sphinxcontrib-mermaid)
myst_fence_as_directive = ["mermaid"]

# A few chapters use lexer hints Pygments doesn't know (dockerignore, jsonc);
# the blocks still render as literal text, so don't warn about them.
suppress_warnings = ["misc.highlighting_failure", "myst.header"]

# Module READMEs legitimately link to repo files that are rewritten to
# GitHub URLs by generate.py; anything left unresolved is a real breakage,
# so keep xref warnings visible.

html_theme = "furo"
html_title = "Python for AI-Driven Automation<br>& Business Data Science"
html_theme_options = {
    "source_repository": "https://github.com/ChrisW09/Python-for-AI-Driven-Automation",
    "source_branch": "main",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/ChrisW09/Python-for-AI-Driven-Automation",
            "html": "",
            "class": "fa-brands fa-github",
        },
    ],
}
