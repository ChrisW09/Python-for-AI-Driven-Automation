#!/usr/bin/env python
"""Generate the README hero banner (docs/images/hero.png).

A clean, modern title banner — dark gradient, a smooth upward "journey" curve,
the course title + tagline, and a row of thematic stages (no counts).

    python scripts/generate_hero_banner.py
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "images", "hero.png")

TITLE = "Python for AI-Driven Automation & Business Data Science"
TAGLINE = "From your first line of Python to shipping AI in production"
STAGES = ["Foundations", "Data Science", "Machine Learning", "Deep Learning",
          "AI Engineering", "Agents & MCP", "Production"]

INK = "#f8fafc"
MUTE = "#9fb3c8"
ACCENT = LinearSegmentedColormap.from_list(
    "accent", ["#38bdf8", "#818cf8", "#c084fc", "#f472b6"])

fig = plt.figure(figsize=(13.0, 4.3), dpi=200)
ax = fig.add_axes([0, 0, 1, 1])  # full-bleed: gradient covers the whole image
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# --- background: subtle dark vignette gradient ---
bg = LinearSegmentedColormap.from_list("bg", ["#0a1020", "#13203b", "#0a1020"])
grad = np.linspace(0, 1, 256).reshape(-1, 1)
ax.imshow(grad, extent=[0, 1, 0, 1], aspect="auto", cmap=bg, origin="lower", zorder=-20)
# faint dotted "data" texture, low alpha
rng = np.random.default_rng(7)
ax.scatter(rng.uniform(0, 1, 90), rng.uniform(0, 0.55, 90),
           s=rng.uniform(1, 7, 90), color="#3b82f6", alpha=0.07, zorder=-15)

# --- the journey curve (smootherstep, low-left to high-right) ---
x = np.linspace(0.04, 0.96, 300)
t = (x - x.min()) / (x.max() - x.min())
y = 0.20 + 0.34 * (6 * t**5 - 15 * t**4 + 10 * t**3)  # eased rise
pts = np.array([x, y]).T.reshape(-1, 1, 2)
segs = np.concatenate([pts[:-1], pts[1:]], axis=1)
# soft glow underlays
for lw, a in [(16, 0.06), (9, 0.10)]:
    ax.plot(x, y, color="#7c83ff", lw=lw, alpha=a, solid_capstyle="round", zorder=1)
lc = LineCollection(segs, cmap=ACCENT, linewidth=3.4, zorder=2)
lc.set_array(t)
ax.add_collection(lc)

# stage nodes along the curve
node_x = np.linspace(0.08, 0.92, len(STAGES))
node_y = np.interp(node_x, x, y)
ax.scatter(node_x, node_y, s=70, color="#0a1020", edgecolors="#e2e8f0",
           linewidths=1.6, zorder=3)
ax.scatter(node_x, node_y, s=16, color="#e2e8f0", zorder=4)

# stage labels under each node
for nx, ny, label in zip(node_x, node_y, STAGES):
    ax.text(nx, ny - 0.085, label, ha="center", va="top",
            fontsize=8.6, color=MUTE, zorder=5)

# --- title + tagline ---
ax.text(0.5, 0.85, TITLE, ha="center", va="center",
        fontsize=19.5, fontweight="bold", color=INK, zorder=6)
ax.text(0.5, 0.70, TAGLINE, ha="center", va="center",
        fontsize=12.5, color=MUTE, style="italic", zorder=6)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
fig.savefig(OUT, facecolor="#0a1020")
print("wrote", os.path.normpath(OUT))
