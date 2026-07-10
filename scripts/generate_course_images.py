#!/usr/bin/env python3
"""Regenerate the structural course infographics in slides/images/.

These four PNGs encode the module structure, so they go stale whenever the
course is renumbered. Rerun this script (repo venv, needs matplotlib only)
after any structural change:

    .venv/bin/python scripts/generate_course_images.py

Produces: 00_course_roadmap.png, 01_dependency_graph.png,
          02_learning_paths.png, 03_weekly_timeline.png
(04_study_loop / 05_what_youll_build / 06_three_circles are structure-free
and are not regenerated here.)
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parent.parent / "slides" / "images"

# ---------------------------------------------------------------------------
# Ground truth: the current module structure. Edit HERE after a renumber.
# ---------------------------------------------------------------------------
MODULES = [
    # (num, name, nb-range label, color, optional?)
    (0,  "Onboarding",           "NB 0, 0b, 0c", "#8C8C8C", False),
    (1,  "Foundations",          "NB 1–6",       "#4C72B0", False),
    (2,  "Data Science",         "NB 7–11",      "#55A868", False),
    (3,  "Real-world I/O",       "NB 12–13",     "#64B5CD", False),
    (4,  "Machine Learning",     "NB 14–16",     "#CCB974", False),
    (5,  "Industry Apps",        "NB 17–20",     "#8A9A5B", False),
    (6,  "AI Engineering",       "NB 21–26",     "#C44E52", False),
    (7,  "Building AI POCs",     "NB 27–30",     "#937860", False),
    (8,  "Agents, Tools & MCP",  "NB 31–34",     "#8172B2", False),
    (9,  "NLP",                  "NB 35–37",     "#DA8BC3", True),
    (10, "DeepTab",              "NB 38",        "#B07AA1", True),
    (11, "Production",           "NB 39–40",     "#7A68A6", False),
    (12, "CI/CD & Deployment",   "mini-book",    "#6B8E9F", True),
    (13, "Capstones",            "NB 41–42",     "#3A3A3A", False),
    (14, "Business AI",          "NB 43–46",     "#4C9E9E", False),
    (15, "Django",               "mini-book",    "#A66E4A", True),
    (16, "Web Scraping",         "NB 47–49",     "#5F7F5F", False),
    (17, "PyTorch",              "NB 50–52",     "#B0603B", False),
]
MOD = {m[0]: m for m in MODULES}

TITLE_KW = dict(fontsize=22, fontweight="bold", color="#2b2b2b")
FOOT_KW = dict(fontsize=12.5, style="italic", color="#8a8a8a", ha="center")


def _box(ax, x, y, w, h, color, lines, optional=False):
    face = color if not optional else color + "55"  # soften optional modules
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.004,rounding_size=0.012",
                                facecolor=face, edgecolor="#2b2b2b", linewidth=1.4))
    n = len(lines)
    for i, (txt, kw) in enumerate(lines):
        kw = dict(kw)
        if optional and kw.get("color") == "white":
            kw["color"] = "#3a3a3a"   # white on a pale box is unreadable
        ax.text(x + w / 2, y + h * (n - i - 0.5) / n, txt,
                ha="center", va="center", **kw)


def roadmap():
    fig, ax = plt.subplots(figsize=(12.6, 7.1), dpi=100)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.5, 0.965, "Python for AI-Driven Automation and Business Data Science",
            ha="center", va="top", fontsize=19, fontweight="bold", color="#2b2b2b")
    ax.text(0.5, 0.905, "52 lessons + 5 labs + 13 appendices  ·  modules 0–17  ·  self-paced — spiral order",
            ha="center", va="top", fontsize=12, style="italic", color="#8a8a8a")

    order = list(range(18))
    per_row = 9
    w, h, gx = 0.0935, 0.175, 0.0125
    x0 = (1 - per_row * w - (per_row - 1) * gx) / 2
    rows = [0.60, 0.30]
    for i, mnum in enumerate(order):
        num, name, nbs, color, opt = MOD[mnum]
        r, c = divmod(i, per_row)
        x, y = x0 + c * (w + gx), rows[r]
        WRAP = {"Machine Learning": "Machine\nLearning", "Real-world I/O": "Real-world\nI/O",
                "AI Engineering": "AI\nEngineering", "Building AI POCs": "Building\nAI POCs",
                "Agents, Tools & MCP": "Agents, Tools\n& MCP", "CI/CD & Deployment": "CI/CD &\nDeployment",
                "Industry Apps": "Industry\nApps", "Data Science": "Data\nScience",
                "Web Scraping": "Web\nScraping"}
        white = dict(color="white", fontsize=12.5, fontweight="bold")
        small = dict(color="white", fontsize=8.2)
        label = WRAP.get(name, name) + (" *" if opt else "")
        _box(ax, x, y, w, h, color,
             [(str(num), white), (label, dict(color="white", fontsize=8.0, fontweight="bold")), (nbs, small)],
             optional=opt)
        if c < per_row - 1:  # arrow to the next box in the row
            ax.add_patch(FancyArrowPatch((x + w, y + h / 2), (x + w + gx, y + h / 2),
                                         arrowstyle="-|>", mutation_scale=11, color="#555"))
    # row-1 → row-2 connector
    ax.add_patch(FancyArrowPatch((x0 + per_row * w + (per_row - 1) * gx - w / 2, rows[0] - 0.005),
                                 (x0 + w / 2, rows[1] + h + 0.005),
                                 arrowstyle="-|>", mutation_scale=12, color="#555",
                                 connectionstyle="arc3,rad=0.0"))
    ax.text(0.5, 0.175, "* optional — NLP, DeepTab, CI/CD and Django can be skipped or read as reference",
            fontsize=10.5, color="#8a8a8a", ha="center")
    ax.text(0.5, 0.10, "— runs entirely offline · every exercise has a worked solution · "
                       "every notebook executes end-to-end —", **FOOT_KW)
    ax.text(0.5, 0.045, "Foundations of every page: read prose → run code → tweak → predict → re-run",
            fontsize=12, fontweight="bold", color="#555", ha="center")
    fig.savefig(OUT / "00_course_roadmap.png", bbox_inches="tight")
    plt.close(fig)


DEPS = [  # (upstream, downstream)
    (0, 1), (1, 2), (2, 3), (2, 4), (4, 5), (3, 6), (4, 6), (6, 7), (7, 8),
    (6, 9), (4, 17), (17, 10), (7, 11), (11, 12), (5, 13), (8, 13), (11, 13),
    (6, 14), (12, 15), (3, 16),
]


def dependency_graph():
    fig, ax = plt.subplots(figsize=(10.4, 9.6), dpi=100)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.5, 0.975, "Module dependency graph — what depends on what",
            ha="center", va="top", **TITLE_KW)
    pos = {  # 5 columns × 5 rows, spine flows top-left → bottom-right
        0: (0.015, 0.815), 1: (0.215, 0.815), 2: (0.415, 0.815), 3: (0.615, 0.815), 16: (0.815, 0.815),
        5: (0.015, 0.635), 4: (0.215, 0.635), 6: (0.415, 0.635), 7: (0.615, 0.635),
        17: (0.015, 0.455), 9: (0.215, 0.455), 11: (0.415, 0.455), 8: (0.615, 0.455),
        10: (0.015, 0.275), 14: (0.215, 0.275), 12: (0.415, 0.275), 13: (0.615, 0.275),
        15: (0.415, 0.095),
    }
    w, h = 0.17, 0.115
    for num, (x, y) in pos.items():
        _, name, _, color, opt = MOD[num]
        WRAP = {"Agents, Tools & MCP": "Agents, Tools\n& MCP", "CI/CD & Deployment": "CI/CD &\nDeployment"}
        _box(ax, x, y, w, h, color,
             [(str(num), dict(color="white", fontsize=12, fontweight="bold")),
              (WRAP.get(name, name), dict(color="white", fontsize=9.2, fontweight="bold"))],
             optional=opt)
    for a, b in DEPS:
        xa, ya = pos[a][0] + w / 2, pos[a][1]
        xb, yb = pos[b][0] + w / 2, pos[b][1]
        start = (xa, ya) if pos[a][1] > pos[b][1] else (xa, ya + h)
        end = (xb, yb + h) if pos[a][1] > pos[b][1] else (xb, yb)
        rad = 0.12
        if pos[a][1] == pos[b][1]:  # same row
            adjacent = abs(pos[a][0] - pos[b][0]) < 0.3
            if adjacent:            # connect the near sides
                lr = pos[a][0] < pos[b][0]
                start = (pos[a][0] + (w if lr else 0), ya + h / 2)
                end = (pos[b][0] + (0 if lr else w), yb + h / 2)
            else:                   # bow underneath so we don't cross boxes between
                start, end = (xa, ya), (xb, yb)
                rad = 0.3 if pos[a][0] < pos[b][0] else -0.3
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=12,
                                     color="#444", lw=1.3, alpha=0.85,
                                     connectionstyle=f"arc3,rad={rad}", zorder=1))
    ax.text(0.5, 0.025, "Edges flow downstream. Module N is safe to start once every "
                        "upstream module is comfortable.", **FOOT_KW)
    fig.savefig(OUT / "01_dependency_graph.png", bbox_inches="tight")
    plt.close(fig)


PATHS = [  # (label, color, hours, set of module numbers touched)
    ("Complete beginner", "#4C72B0", "~123 h", {0, 1, 2, 3, 4, 5, 6, 7, 8, 11, 13, 14, 16, 17}),
    ("Analyst (Excel + SQL)", "#64B5CD", "~47 h", {0, 2, 3, 4, 5, 13, 16}),
    ("Developer (knows Python)", "#55A868", "~55 h", {0, 2, 3, 4, 6, 11, 13}),
    ("ML practitioner", "#DD8452", "~38 h", {0, 6, 8, 11, 13, 17}),
    ("Manager (curious)", "#8172B2", "~10 h", {0, 13}),
]
SHORT = {0: "Onbd", 1: "Fnd", 2: "DS", 3: "I/O", 4: "ML", 5: "Ind", 6: "AI", 7: "POC",
         8: "MCP", 9: "NLP", 10: "DT", 11: "Prod", 12: "CI", 13: "Cap", 14: "Biz", 15: "Djg",
         16: "Scr", 17: "PyT"}


def learning_paths():
    fig, ax = plt.subplots(figsize=(13.2, 9.6), dpi=100)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.5, 0.97, "Pick the learning path that fits you", ha="center", va="top", **TITLE_KW)
    xs = [0.315 + i * 0.036 for i in range(18)]
    yhdr = 0.80
    ax.text(0.03, yhdr, "Path", fontsize=14, fontweight="bold", color="#2b2b2b", va="center")
    for i, x in enumerate(xs):
        ax.add_patch(FancyBboxPatch((x - 0.016, yhdr - 0.028), 0.032, 0.056,
                                    boxstyle="round,pad=0.002,rounding_size=0.006",
                                    facecolor="#f2f2f2", edgecolor="#999", lw=1))
        ax.text(x, yhdr + 0.011, str(i), ha="center", va="center", fontsize=8.6, fontweight="bold")
        ax.text(x, yhdr - 0.013, SHORT[i], ha="center", va="center", fontsize=7.6)
    ax.text(xs[-1] + 0.038, yhdr, "Time", fontsize=14, fontweight="bold", va="center")
    for r, (label, color, hours, touched) in enumerate(PATHS):
        y = 0.665 - r * 0.125
        ax.text(0.03, y, label, fontsize=14.5, fontweight="bold", color=color, va="center")
        ax.plot([xs[0], xs[-1]], [y, y], color=color, lw=2.4, alpha=0.45, zorder=1)
        for i, x in enumerate(xs):
            if i in touched:
                ax.scatter([x], [y], s=300, color=color, edgecolor="#222", lw=1.6, zorder=3)
            else:
                ax.scatter([x], [y], s=55, color="#d9d9d9", zorder=2)
        ax.text(xs[-1] + 0.038, y, hours, fontsize=14, fontweight="bold", va="center")
    ax.text(0.5, 0.055, "Each dot is one module. Solid line = modules you'd touch on that path. "
                        "Optional modules (9, 10, 12, 15) join any path;\n"
                        "16 (Web Scraping) slots in after Module 3 and 17 (PyTorch) after Module 4.", **FOOT_KW)
    fig.savefig(OUT / "02_learning_paths.png", bbox_inches="tight")
    plt.close(fig)


WEEKS = [  # (title, focus, nb-label, hours)
    ("Week 1", "Onboarding +\nPython I", "NB 0–3", "~8 h focus"),
    ("Week 2", "Python II +\nGit & Copilot", "NB 4–6, 45", "~10 h focus"),
    ("Week 3", "Data science I", "NB 7–9", "~8 h focus"),
    ("Week 4", "Data science II\n+ real-world I/O", "NB 10–13", "~10 h focus"),
    ("Week 5", "Machine\nlearning", "NB 14–16", "~9 h focus"),
    ("Week 6", "Deep learning\n(PyTorch)", "NB 50–52", "~9 h focus"),
    ("Week 7", "Industry\napplications", "NB 17–20", "~11 h focus"),
    ("Week 8", "AI engineering I", "NB 21–23", "~9 h focus"),
    ("Week 9", "AI engineering II\n+ production", "NB 24–26, 39–40", "~12 h focus"),
    ("Week 10", "Business AI +\nLLM theory", "NB 43–46, 21", "~9 h focus"),
    ("Week 11", "Build the POCs\n+ agents & MCP", "NB 27–34", "~15 h focus"),
    ("Week 12", "Web scraping\n+ capstones", "NB 47–49, 41–42", "~12 h focus"),
]
WEEK_COLORS = ["#4C72B0", "#4C72B0", "#55A868", "#64B5CD", "#CCB974", "#B0603B",
               "#8A9A5B", "#C44E52", "#7A68A6", "#4C9E9E", "#937860", "#3A3A3A"]


def weekly_timeline():
    fig, ax = plt.subplots(figsize=(12.6, 7.1), dpi=100)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.5, 0.965, "A self-paced 12-week schedule", ha="center", va="top", **TITLE_KW)
    w, h, gx = 0.145, 0.27, 0.0165
    x0 = (1 - 6 * w - 5 * gx) / 2
    for i, ((title, focus, nbs, hrs), color) in enumerate(zip(WEEKS, WEEK_COLORS)):
        r, c = divmod(i, 6)
        x = x0 + c * (w + gx)                       # two full rows of six
        y = 0.55 if r == 0 else 0.17
        _box(ax, x, y, w, h, color, [
            (title, dict(color="white", fontsize=13.5, fontweight="bold")),
            (focus, dict(color="white", fontsize=9.3)),
            (nbs, dict(color="white", fontsize=8.6, style="italic")),
            (hrs, dict(color="white", fontsize=9.2, fontweight="bold")),
        ])
    ax.text(0.5, 0.055, "≈ 8–15 hours of focused study per week  ·  more time → faster, "
                        "less time → split a week in two", **FOOT_KW)
    fig.savefig(OUT / "03_weekly_timeline.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    for fn in (roadmap, dependency_graph, learning_paths, weekly_timeline):
        fn()
        print("wrote", fn.__name__)
    print("done →", OUT)
