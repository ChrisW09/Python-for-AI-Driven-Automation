# Sphinx configuration for the course documentation site.
# Build with:  make html   (from docs_site/) — runs generate.py first.

project = "Python for AI-Driven Automation & Business Data Science"
author = "Christoph Weisser"
copyright = "2026, Christoph Weisser"

extensions = [
    "myst_parser",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",  # copy button on every code block
    "sphinxext.opengraph",  # link previews when a page is shared
]

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

# Copy buttons: strip interactive prompts so a copied line pastes and runs.
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: "
copybutton_prompt_is_regex = True
copybutton_only_copy_prompt_lines = False

# Link previews (Open Graph / Twitter cards) when a page is shared.
html_baseurl = "https://chrisw09.github.io/Python-for-AI-Driven-Automation/"
ogp_site_url = html_baseurl
ogp_site_name = project
ogp_image = html_baseurl + "_static/hero.png"
ogp_enable_meta_description = True

# ── linkcheck ────────────────────────────────────────────────────────────────
# Two classes of false alarm would otherwise drown the real findings:
#   * localhost URLs are instructions to open your own dev server, not links.
#   * GitHub emits heading ids as `user-content-<slug>`, so anchor checking
#     reports links that work perfectly in a browser as broken.
# Ignoring both means a non-empty linkcheck report is worth reading.
linkcheck_ignore = [r"^https?://(127\.0\.0\.1|localhost)(:\d+)?(/|$)"]
linkcheck_anchors_ignore_for_url = [r"^https://github\.com/"]
linkcheck_retries = 2

html_theme = "furo"
html_title = "Python for AI-Driven Automation<br>& Business Data Science"
html_static_path = ["_static"]

# Furo does not bundle an icon font, so a footer icon has to supply its own
# markup — with an empty "html" the link renders as an invisible zero-width
# anchor. Inline the GitHub mark instead.
GITHUB_MARK = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="24" height="24"
     fill="currentColor" aria-hidden="true">
  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38
  0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01
  1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95
  0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.42 7.42 0 0 1 2-.27c.68 0
  1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0
  3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012
  8.012 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/>
</svg>
"""

html_theme_options = {
    "source_repository": "https://github.com/ChrisW09/Python-for-AI-Driven-Automation",
    "source_branch": "main",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/ChrisW09/Python-for-AI-Driven-Automation",
            "html": GITHUB_MARK,
            "class": "",
        },
    ],
}
