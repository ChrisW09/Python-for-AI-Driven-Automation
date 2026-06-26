#!/usr/bin/env python
"""Generate the README roadmap banner (docs/images/course_roadmap.png).

A clean module map of the current curriculum (modules 0-14). Re-run after any
curriculum change so the banner never drifts from the README.

    python scripts/generate_roadmap_banner.py
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "images", "course_roadmap.png")

# (number, name, notebook label, one-line focus, colour)
MODULES = [
    ("0",  "Onboarding",        "setup",     "start here",                 "#6b7280"),
    ("1",  "Foundations",       "NB 1–6",    "Python without friction",    "#4f6d9a"),
    ("2",  "Data Science",      "NB 7–11",   "pandas · NumPy · stats · TS", "#3f8f6b"),
    ("3",  "Real-world I/O",    "NB 12–13",  "HTTP · SQL · validation",    "#5aa6c0"),
    ("4",  "Machine Learning",  "NB 14–16",  "sklearn · eval · features",  "#c7a456"),
    ("5",  "Industry Apps",     "NB 17–20",  "churn · fraud · demand",     "#b5524e"),
    ("6",  "AI Engineering",    "NB 21–26",  "LLMs · RAG · agents · eval",  "#7c5cae"),
    ("7",  "Building AI POCs",  "NB 27–30",  "3 POCs · RAG · vector DBs",   "#a9763f"),
    ("8",  "Agents · MCP",      "NB 31–34",  "architectures · tools · MCP", "#3f8f8f"),
    ("9",  "NLP",               "NB 35–37",  "topics · sentiment",         "#8a9a4b"),
    ("10", "DeepTab (opt.)",    "NB 38",     "deep tabular learning",      "#496a8f"),
    ("11", "Production",        "NB 39–40",  "packaging · scheduling",     "#9a7bb0"),
    ("12", "CI/CD & Deploy",    "mini-book", "Docker → HTTPS",             "#566374"),
    ("13", "Capstones",         "NB 41–42",  "ship 2 projects",            "#3a3a3a"),
    ("14", "Business AI",       "NB 43–46",  "strategy · BPM · governance", "#4f8a8b"),
]

COLS = 5
COL_W, ROW_H = 2.7, 2.55
BOX_W, BOX_H = 2.35, 1.45
LEFT, Y_TOP = 0.5, 6.45            # left margin; centre-y of row 0
WIDTH = 2 * LEFT + (COLS - 1) * COL_W + BOX_W
MIDX = WIDTH / 2

fig, ax = plt.subplots(figsize=(12.6, 7.0), dpi=170)
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, 9.2)
ax.axis("off")

# Title + subtitle
ax.text(MIDX, 8.78, "Python for AI-Driven Automation & Business Data Science",
        ha="center", va="center", fontsize=19, fontweight="bold", color="#1f2937")
ax.text(MIDX, 8.18,
        "87 notebooks  ·  14 modules  ·  249 in-lesson checkpoints  ·  self-paced or instructor-led  ·  100% offline",
        ha="center", va="center", fontsize=11.5, style="italic", color="#6b7280")

for i, (num, name, nb, focus, colour) in enumerate(MODULES):
    r, c = divmod(i, COLS)
    cx = LEFT + c * COL_W + BOX_W / 2
    cy = Y_TOP - r * ROW_H
    # NB label above the box
    ax.text(cx, cy + BOX_H / 2 + 0.26, nb, ha="center", va="center",
            fontsize=8.5, style="italic", color="#9ca3af")
    # the box
    ax.add_patch(FancyBboxPatch(
        (cx - BOX_W / 2, cy - BOX_H / 2), BOX_W, BOX_H,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        linewidth=0, facecolor=colour))
    ax.text(cx, cy + 0.30, num, ha="center", va="center",
            fontsize=16, fontweight="bold", color="white")
    ax.text(cx, cy - 0.26, name, ha="center", va="center",
            fontsize=10.5, fontweight="bold", color="white")
    # focus caption below the box
    ax.text(cx, cy - BOX_H / 2 - 0.27, focus, ha="center", va="center",
            fontsize=7.8, color="#6b7280")

# Footer mantra
ax.text(MIDX, 0.30,
        "every notebook runs end-to-end offline  ·  every exercise has a worked solution  ·  "
        "a quick checkpoint to try every ~20 min",
        ha="center", va="center", fontsize=9.4, color="#374151")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT, bbox_inches="tight", pad_inches=0.25, facecolor="white")
print("wrote", os.path.normpath(OUT))
