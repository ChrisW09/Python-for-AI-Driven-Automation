"""Generate the matplotlib figures for the Chapter 0 refresher deck.

All figures are computed from the bundled course datasets (or from clearly
labelled simulations); nothing is sketched by hand. Run from anywhere:

    python Chapters/chapter_00/make_figures.py

Output: Chapters/chapter_00/images/ch00_*.png at 150 dpi, matching the
figure size and resolution used by the other decks.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

HERE = Path(__file__).parent
ROOT = HERE.parents[1]
DATA = ROOT / "ALL CSV FILES - 2nd Edition"
OUT = HERE / "images"
OUT.mkdir(parents=True, exist_ok=True)

ACCENT = "#26468C"   # matches \definecolor{accent}{RGB}{38,70,140}
ORANGE = "#C8641E"
GREY = "#7A7A7A"
# Each simulated figure builds its own generator from this seed, so regenerating
# one panel on its own -- or reordering the calls in __main__ -- cannot change
# what the others draw. A single module-level generator shared by three figures
# made the shipped slides depend on call order.
SEED = 0

plt.rcParams.update(
    {
        "figure.dpi": 150,
        "savefig.dpi": 150,
        "font.size": 9,
        "axes.titlesize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linewidth": 0.6,
    }
)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)


# Wage.csv has no index column; Advertising.csv, Boston.csv and Credit.csv do.
wage = pd.read_csv(DATA / "Wage.csv")
adv = pd.read_csv(DATA / "Advertising.csv", index_col=0)
boston = pd.read_csv(DATA / "Boston.csv", index_col=0)
credit = pd.read_csv(DATA / "Credit.csv")


# 1 -- Centre and spread on a skewed variable ---------------------------------
def fig_center_spread():
    x = wage["wage"].to_numpy()
    fig, (ax1, ax2) = plt.subplots(
        2, 1, figsize=(6.8, 4.0), sharex=True, gridspec_kw={"height_ratios": [3, 1]}
    )

    ax1.hist(x, bins=40, color=ACCENT, alpha=0.75, edgecolor="white", linewidth=0.4)
    ax1.axvline(x.mean(), color=ORANGE, lw=2, label=f"mean = {x.mean():.1f}")
    ax1.axvline(
        np.median(x), color="black", lw=2, ls="--", label=f"median = {np.median(x):.1f}"
    )
    ax1.set_ylabel("frequency")
    ax1.set_title("Wage (n = 3000): a right-skewed distribution")
    ax1.legend(frameon=False)

    ax2.boxplot(
        x,
        vert=False,
        widths=0.5,
        patch_artist=True,
        boxprops={"facecolor": ACCENT, "alpha": 0.35},
        medianprops={"color": "black", "lw": 2},
        flierprops={"marker": "o", "ms": 3, "mfc": "none", "mec": GREY},
    )
    ax2.set_yticks([])
    ax2.set_xlabel("wage (thousands of dollars)")
    ax2.grid(axis="y", visible=False)
    save(fig, "ch00_center_spread.png")


# 2 -- Anatomy of a boxplot ---------------------------------------------------
def fig_boxplot_anatomy():
    x = wage["wage"].to_numpy()
    q1, med, q3 = np.percentile(x, [25, 50, 75])
    iqr = q3 - q1
    lo = x[x >= q1 - 1.5 * iqr].min()
    hi = x[x <= q3 + 1.5 * iqr].max()

    fig, ax = plt.subplots(figsize=(6.8, 2.9))
    ax.boxplot(
        x,
        vert=False,
        widths=0.35,
        patch_artist=True,
        boxprops={"facecolor": ACCENT, "alpha": 0.30},
        medianprops={"color": "black", "lw": 2},
        flierprops={"marker": "o", "ms": 3.5, "mfc": "none", "mec": ORANGE},
    )

    # Labels sit above the box on two staggered rows so nothing collides.
    #
    # The whisker is drawn at the most extreme observation still *inside* the
    # fence, not at the fence itself, so the label has to say so: on Wage the
    # lower fence is 20.4 while the whisker sits at 20.9. Labelling the whisker
    # "$Q_1 - 1.5$ IQR" made the slide contradict its own formula for any
    # student who worked the fence out by hand.
    ann = [
        (lo, f"lower whisker\nlast point above $Q_1 - 1.5\\,\\mathrm{{IQR}}$ = {lo:.0f}", 1.42),
        (q1, f"$Q_1$ = {q1:.0f}", 1.24),
        (med, f"median = {med:.0f}", 1.42),
        (q3, f"$Q_3$ = {q3:.0f}", 1.24),
        (hi, f"upper whisker\nlast point below $Q_3 + 1.5\\,\\mathrm{{IQR}}$ = {hi:.0f}", 1.42),
    ]
    for xv, label, ytext in ann:
        ax.annotate(
            label,
            xy=(xv, 1.10),
            xytext=(xv, ytext),
            ha="center",
            va="bottom",
            fontsize=8,
            arrowprops={"arrowstyle": "-", "color": GREY, "lw": 0.8},
        )

    ax.annotate(
        "",
        xy=(q1, 0.80),
        xytext=(q3, 0.80),
        arrowprops={"arrowstyle": "<->", "color": ACCENT, "lw": 1.2},
    )
    ax.text(
        (q1 + q3) / 2, 0.72, f"IQR = {iqr:.0f}", ha="center", fontsize=8, color=ACCENT
    )
    ax.annotate(
        "outliers: beyond the whiskers",
        xy=(x.max() * 0.97, 1.0),
        xytext=(x.max() * 0.97, 0.70),
        ha="right",
        fontsize=8,
        color=ORANGE,
        arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 0.8},
    )

    ax.set_ylim(0.60, 1.68)
    ax.set_yticks([])
    ax.set_xlabel("wage (thousands of dollars)")
    ax.set_title("The five-number summary, read off a boxplot")
    ax.grid(axis="y", visible=False)
    save(fig, "ch00_boxplot_anatomy.png")


# 3 -- What the correlation coefficient does and does not capture -------------
def fig_correlation():
    fig, axes = plt.subplots(1, 4, figsize=(9.2, 2.6))

    panels = [
        (adv["TV"], adv["sales"], "TV budget vs. sales", "TV"),
        (adv["radio"], adv["sales"], "radio budget vs. sales", "radio"),
        (adv["newspaper"], adv["sales"], "newspaper budget vs. sales", "newspaper"),
    ]
    for ax, (xv, yv, title, xlabel) in zip(axes, panels):
        r = np.corrcoef(xv, yv)[0, 1]
        ax.scatter(xv, yv, s=8, color=ACCENT, alpha=0.6, edgecolors="none")
        b, a = np.polyfit(xv, yv, 1)
        xs = np.linspace(xv.min(), xv.max(), 50)
        ax.plot(xs, a + b * xs, color=ORANGE, lw=1.6)
        ax.set_title(f"{title}\n$r = {r:.2f}$", fontsize=9)
        ax.set_xlabel(xlabel)
        ax.set_ylabel("sales" if ax is axes[0] else "")

    # A strong but non-linear relationship that r cannot see.
    rng = np.random.default_rng(SEED)
    xq = rng.uniform(-3, 3, 200)
    yq = xq**2 + rng.normal(0, 0.8, 200)
    r = np.corrcoef(xq, yq)[0, 1]
    axes[3].scatter(xq, yq, s=8, color=GREY, alpha=0.7, edgecolors="none")
    axes[3].axhline(yq.mean(), color=ORANGE, lw=1.6)
    axes[3].set_title(f"simulated: $y = x^2 + \\varepsilon$\n$r = {r:.2f}$", fontsize=9)
    axes[3].set_xlabel("x")

    save(fig, "ch00_correlation.png")


# 4 -- The central limit theorem in action ------------------------------------
def fig_clt():
    pop = wage["wage"].to_numpy()
    mu = pop.mean()
    fig, axes = plt.subplots(1, 4, figsize=(9.2, 2.5), sharey=False)

    axes[0].hist(pop, bins=40, color=GREY, alpha=0.75, edgecolor="white", linewidth=0.3)
    axes[0].axvline(mu, color=ORANGE, lw=1.8)
    axes[0].set_title(f"population\n(Wage, $\\mu$ = {mu:.0f})", fontsize=9)
    axes[0].set_ylabel("frequency")

    rng = np.random.default_rng(SEED)
    for ax, n in zip(axes[1:], (2, 10, 50)):
        means = rng.choice(pop, size=(4000, n), replace=True).mean(axis=1)
        ax.hist(means, bins=40, color=ACCENT, alpha=0.8, edgecolor="white", linewidth=0.3)
        ax.axvline(mu, color=ORANGE, lw=1.8)
        ax.set_title(
            f"means of samples, $n = {n}$\nSD = {means.std(ddof=1):.1f}", fontsize=9
        )
        ax.set_xlim(20, 220)

    fig.suptitle(
        "Whatever the population looks like, the sample mean becomes normal — and narrower",
        fontsize=9.5,
    )
    save(fig, "ch00_clt.png")


# 5 -- The four reference distributions of this course ------------------------
def fig_reference_dists():
    fig, axes = plt.subplots(1, 3, figsize=(9.2, 2.6))

    z = np.linspace(-4, 4, 400)
    axes[0].plot(z, stats.norm.pdf(z), color=ACCENT, lw=1.8, label="$N(0,1)$")
    axes[0].plot(z, stats.t.pdf(z, 3), color=ORANGE, lw=1.6, ls="--", label="$t_{3}$")
    axes[0].plot(z, stats.t.pdf(z, 30), color=GREY, lw=1.4, ls=":", label="$t_{30}$")
    axes[0].set_title("normal vs. $t$: heavier tails,\nsmaller df", fontsize=9)
    axes[0].legend(frameon=False, fontsize=8)

    c = np.linspace(0.01, 20, 400)
    for df, ls in ((2, "-"), (5, "--"), (10, ":")):
        axes[1].plot(c, stats.chi2.pdf(c, df), lw=1.6, ls=ls, label=f"$\\chi^2_{{{df}}}$")
    axes[1].set_title("$\\chi^2$: sums of squares\n(variance, LR tests)", fontsize=9)
    axes[1].legend(frameon=False, fontsize=8)

    f = np.linspace(0.01, 5, 400)
    for d1, d2, ls in ((2, 20, "-"), (5, 20, "--"), (10, 20, ":")):
        axes[2].plot(
            f, stats.f.pdf(f, d1, d2), lw=1.6, ls=ls, label=f"$F_{{{d1},{d2}}}$"
        )
    axes[2].set_title("$F$: ratios of variances\n(the $F$-test in Ch. 3)", fontsize=9)
    axes[2].legend(frameon=False, fontsize=8)

    save(fig, "ch00_reference_dists.png")


# 6 -- What "95% confidence" actually means -----------------------------------
def fig_ci_coverage():
    pop = wage["wage"].to_numpy()
    mu = pop.mean()
    n, reps = 40, 25
    # Own seed: this draw happens to miss twice in 25, which is the point of
    # the slide — "95%" is a property of the procedure, not of one interval.
    rng = np.random.default_rng(3)

    fig, ax = plt.subplots(figsize=(6.8, 3.4))
    n_miss = 0
    for i in range(reps):
        s = rng.choice(pop, size=n, replace=True)
        half = stats.t.ppf(0.975, n - 1) * s.std(ddof=1) / np.sqrt(n)
        lo, hi = s.mean() - half, s.mean() + half
        covers = lo <= mu <= hi
        n_miss += not covers
        ax.plot(
            [lo, hi], [i, i], color=ACCENT if covers else ORANGE, lw=1.8, alpha=0.85
        )
        ax.plot(s.mean(), i, "o", ms=3, color=ACCENT if covers else ORANGE)

    ax.axvline(mu, color="black", lw=1.6, ls="--", label=f"true $\\mu$ = {mu:.0f}")
    ax.set_yticks([])
    ax.set_xlabel("wage (thousands of dollars)")
    ax.set_title(
        f"{reps} samples of $n$ = {n}, one 95% CI each — {n_miss} miss $\\mu$",
        fontsize=10,
    )
    ax.legend(frameon=False, loc="lower right")
    ax.grid(axis="y", visible=False)
    save(fig, "ch00_ci_coverage.png")


# 7 -- Simple linear regression: fit and residuals ----------------------------
def fig_slr():
    x = adv["TV"].to_numpy()
    y = adv["sales"].to_numpy()
    b1, b0 = np.polyfit(x, y, 1)
    fitted = b0 + b1 * x
    resid = y - fitted
    r2 = 1 - (resid**2).sum() / ((y - y.mean()) ** 2).sum()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.2))

    ax1.scatter(x, y, s=10, color=ACCENT, alpha=0.65, edgecolors="none")
    for xi, yi, fi in zip(x[::6], y[::6], fitted[::6]):
        ax1.plot([xi, xi], [yi, fi], color=GREY, lw=0.7, alpha=0.8)
    xs = np.linspace(x.min(), x.max(), 50)
    ax1.plot(xs, b0 + b1 * xs, color=ORANGE, lw=2)
    ax1.set_xlabel("TV budget (thousands of dollars)")
    ax1.set_ylabel("sales (thousands of units)")
    ax1.set_title(
        f"$\\hat y = {b0:.2f} + {b1:.4f}\\,x$   ($R^2 = {r2:.2f}$)", fontsize=9.5
    )

    ax2.scatter(fitted, resid, s=10, color=ACCENT, alpha=0.65, edgecolors="none")
    ax2.axhline(0, color=ORANGE, lw=1.6)
    ax2.set_xlabel("fitted value $\\hat y$")
    ax2.set_ylabel("residual $y - \\hat y$")
    ax2.set_title("residuals vs. fitted: a pattern means trouble", fontsize=9.5)

    save(fig, "ch00_slr.png")


# ---------------------------------------------------------------------------
# Added figures: shape, association, inference and optimisation
# ---------------------------------------------------------------------------


# 8 -- A gallery of shapes, all from the course data ---------------------------
def fig_shape_gallery():
    panels = [
        (boston["rm"], "Boston: rooms per dwelling", "roughly symmetric"),
        (wage["wage"], "Wage: wages", "right-skewed"),
        (credit["Balance"], "Credit: card balance", "a spike at zero"),
        (boston["tax"], "Boston: property-tax rate", "bimodal"),
    ]
    fig, axes = plt.subplots(1, 4, figsize=(9.4, 2.7))
    for ax, (x, title, shape) in zip(axes, panels):
        ax.hist(x, bins=30, color=ACCENT, alpha=0.75, edgecolor="white", linewidth=0.3)
        ax.axvline(x.mean(), color=ORANGE, lw=1.8)
        ax.axvline(x.median(), color="black", lw=1.8, ls="--")
        ax.set_title(f"{title}\n{shape}", fontsize=8.5)
        ax.set_yticks([])
        ax.tick_params(labelsize=7.5)
    axes[0].set_ylabel("frequency")
    fig.suptitle(
        "Solid orange = mean, dashed black = median. The gap between them is the skew.",
        fontsize=8.5,
    )
    save(fig, "ch00_shape_gallery.png")


# 9 -- A log transform tames a skewed variable --------------------------------
def fig_log_transform():
    x = wage["wage"].to_numpy()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.6, 2.8))
    for ax, v, title in (
        (ax1, x, "wage"),
        (ax2, np.log(x), "log(wage)"),
    ):
        ax.hist(v, bins=40, color=ACCENT, alpha=0.75, edgecolor="white", linewidth=0.3)
        ax.axvline(v.mean(), color=ORANGE, lw=1.8, label="mean")
        ax.axvline(np.median(v), color="black", lw=1.8, ls="--", label="median")
        sk = stats.skew(v)
        ax.set_title(f"{title}   (skewness {sk:+.2f})", fontsize=9.5)
        ax.set_xlabel(title)
    ax1.set_ylabel("frequency")
    ax1.legend(frameon=False, fontsize=8)
    save(fig, "ch00_log_transform.png")


# 10 -- Anscombe's quartet ----------------------------------------------------
def fig_anscombe():
    x1 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5], float)
    x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8], float)
    sets = [
        (x1, [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68],
         "I: a linear fit is fine"),
        (x1, [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74],
         "II: the truth is a curve"),
        (x1, [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73],
         "III: one outlier tilts the line"),
        (x4, [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89],
         "IV: one point decides everything"),
    ]
    fig, axes = plt.subplots(1, 4, figsize=(9.4, 2.6), sharex=True, sharey=True)
    for ax, (x, y, title) in zip(axes, sets):
        y = np.asarray(y, float)
        b1, b0 = np.polyfit(x, y, 1)
        r = np.corrcoef(x, y)[0, 1]
        ax.scatter(x, y, s=16, color=ACCENT, alpha=0.85, edgecolors="none")
        xs = np.linspace(3, 20, 20)
        ax.plot(xs, b0 + b1 * xs, color=ORANGE, lw=1.5)
        ax.set_title(f"{title}\n$\\bar x$={x.mean():.1f}, $\\bar y$={y.mean():.2f}, "
                     f"$r$={r:.2f}", fontsize=8)
        ax.set_xlim(2, 20)
        ax.tick_params(labelsize=7.5)
    fig.suptitle(
        "Anscombe's quartet: identical means, SDs, correlation and regression line",
        fontsize=9,
    )
    save(fig, "ch00_anscombe.png")


# 11 -- Simpson's paradox -----------------------------------------------------
def fig_simpson():
    rng = np.random.default_rng(7)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.0, 3.1), sharey=True)
    colours = [ACCENT, ORANGE, "#2E7D5B"]
    xs_all, ys_all = [], []
    for k, (base_x, base_y, c) in enumerate(
        zip((2.0, 4.5, 7.0), (4.0, 6.0, 8.0), colours)
    ):
        x = base_x + rng.normal(0, 0.6, 40)
        y = base_y - 0.5 * (x - base_x) + rng.normal(0, 0.35, 40)
        xs_all.append(x)
        ys_all.append(y)
        for ax in (ax1, ax2):
            ax.scatter(x, y, s=12, color=c if ax is ax2 else GREY, alpha=0.75,
                       edgecolors="none")
        b1, b0 = np.polyfit(x, y, 1)
        xx = np.linspace(x.min(), x.max(), 20)
        ax2.plot(xx, b0 + b1 * xx, color=c, lw=1.8)

    X = np.concatenate(xs_all)
    Y = np.concatenate(ys_all)
    b1, b0 = np.polyfit(X, Y, 1)
    xx = np.linspace(X.min(), X.max(), 20)
    ax1.plot(xx, b0 + b1 * xx, color="black", lw=2)
    ax1.set_title(f"Ignoring the group: slope $= {b1:+.2f}$", fontsize=9.5)
    ax2.set_title("Within each group: slope $< 0$", fontsize=9.5)
    for ax in (ax1, ax2):
        ax.set_xlabel("hours of exercise per week")
    ax1.set_ylabel("cholesterol")
    fig.suptitle("Simpson's paradox: the aggregate reverses every subgroup", fontsize=9.5)
    save(fig, "ch00_simpson.png")


# 12 -- The 68-95-99.7 rule ---------------------------------------------------
def fig_normal_rule():
    z = np.linspace(-4, 4, 600)
    d = stats.norm.pdf(z)
    fig, ax = plt.subplots(figsize=(6.6, 2.9))
    ax.plot(z, d, color=ACCENT, lw=1.8)
    bands = [(1, 0.30, "68%"), (2, 0.18, "95%"), (3, 0.10, "99.7%")]
    for k, alpha, label in bands:
        m = (z >= -k) & (z <= k)
        ax.fill_between(z[m], d[m], color=ACCENT, alpha=alpha)
        ax.annotate(
            f"$\\pm{k}\\sigma$: {label}",
            xy=(k, stats.norm.pdf(k)),
            xytext=(k + 0.25, 0.36 - 0.09 * k),
            fontsize=8.5,
            arrowprops={"arrowstyle": "->", "color": GREY, "lw": 0.8},
        )
    ax.set_xticks(range(-4, 5))
    ax.set_xticklabels([f"${v:+d}\\sigma$".replace("+0σ", "\\mu") if v else "$\\mu$"
                        for v in range(-4, 5)], fontsize=8)
    ax.set_yticks([])
    ax.set_title("The 68\u201395\u201399.7 rule (and why $1.96$ is worth memorising)")
    save(fig, "ch00_normal_rule.png")


# 13 -- What a p-value is, as an area -----------------------------------------
def fig_pvalue():
    df = 99
    tobs = 2.0
    t = np.linspace(-4, 4, 600)
    d = stats.t.pdf(t, df)
    p = 2 * stats.t.sf(tobs, df)
    fig, ax = plt.subplots(figsize=(6.6, 2.9))
    ax.plot(t, d, color=ACCENT, lw=1.8)
    for side in (1, -1):
        m = (t * side) >= tobs
        ax.fill_between(t[m], d[m], color=ORANGE, alpha=0.75)
    ax.axvline(tobs, color=ORANGE, lw=1.4, ls="--")
    ax.axvline(-tobs, color=ORANGE, lw=1.4, ls="--")
    ax.annotate(
        f"observed $t = {tobs}$",
        xy=(tobs, stats.t.pdf(tobs, df)),
        xytext=(2.5, 0.28),
        fontsize=8.5,
        arrowprops={"arrowstyle": "->", "color": GREY, "lw": 0.8},
    )
    ax.annotate(
        f"the two shaded tails\nare the $p$-value: {p:.3f}",
        xy=(-2.6, 0.012),
        xytext=(-3.97, 0.20),
        fontsize=8,
        color=ORANGE,
        ha="left",
        arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 0.8},
    )
    ax.set_yticks([])
    ax.set_xlabel("value of the test statistic if $H_0$ were true  ($t_{99}$)")
    ax.set_title("A $p$-value is an area under the null distribution")
    save(fig, "ch00_pvalue.png")


# 14 -- Type I, Type II and power ---------------------------------------------
def fig_power():
    z = np.linspace(-4, 7, 800)
    shift = 2.8
    crit = 1.96
    h0 = stats.norm.pdf(z)
    h1 = stats.norm.pdf(z, shift)
    power = 1 - stats.norm.cdf(crit, shift)

    fig, ax = plt.subplots(figsize=(7.4, 3.0))
    ax.plot(z, h0, color=ACCENT, lw=1.8, label="if $H_0$ true")
    ax.plot(z, h1, color="#2E7D5B", lw=1.8, label="if $H_1$ true")
    m = z >= crit
    ax.fill_between(z[m], h0[m], color=ORANGE, alpha=0.85,
                    label=r"Type I error ($\alpha/2$)")
    m2 = z <= crit
    ax.fill_between(z[m2], h1[m2], color="#2E7D5B", alpha=0.28,
                    label=r"Type II error ($\beta$)")
    ax.axvline(crit, color="black", lw=1.2, ls="--")
    ax.annotate("reject $H_0$ to the right\nof the critical value",
                xy=(crit, 0.30), xytext=(3.4, 0.34), fontsize=8.5,
                arrowprops={"arrowstyle": "->", "color": GREY, "lw": 0.8})
    ax.set_yticks([])
    ax.set_xlabel("test statistic")
    ax.set_title(f"Power $= 1-\\beta = {power:.2f}$ for this effect size and $n$")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    save(fig, "ch00_power.png")


# 15 -- Law of large numbers, and the 1/sqrt(n) law ---------------------------
def fig_lln():
    pop = wage["wage"].to_numpy()
    mu = pop.mean()
    rng = np.random.default_rng(11)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.0))
    ns = np.arange(1, 501)
    for k in range(6):
        draws = rng.choice(pop, size=500, replace=True)
        ax1.plot(ns, np.cumsum(draws) / ns, lw=0.9, alpha=0.8)
    ax1.axhline(mu, color="black", lw=1.6, ls="--", label=f"$\\mu$ = {mu:.0f}")
    ax1.set_xlabel("observations so far, $n$")
    ax1.set_ylabel("running mean")
    ax1.set_title("Law of large numbers: six samples", fontsize=9.5)
    ax1.legend(frameon=False, fontsize=8)

    sizes = np.array([2, 5, 10, 25, 50, 100, 200, 400])
    emp = [rng.choice(pop, size=(2000, n), replace=True).mean(axis=1).std(ddof=1)
           for n in sizes]
    ax2.plot(sizes, emp, "o", color=ACCENT, ms=5, label="simulated SD of $\\bar x$")
    grid = np.linspace(2, 400, 200)
    ax2.plot(grid, pop.std(ddof=1) / np.sqrt(grid), color=ORANGE, lw=1.8,
             label=r"$\sigma/\sqrt{n}$")
    ax2.set_xlabel("sample size $n$")
    ax2.set_ylabel("spread of the sample mean")
    ax2.set_title("Precision improves only like $1/\\sqrt{n}$", fontsize=9.5)
    ax2.legend(frameon=False, fontsize=8)
    save(fig, "ch00_lln.png")


# 16 -- One point can move a least-squares line -------------------------------
def fig_outlier_influence():
    rng = np.random.default_rng(3)
    x = np.linspace(1, 10, 20)
    y = 2 + 0.8 * x + rng.normal(0, 0.7, 20)

    cases = [
        (5.5, 14.0, "an outlier in $y$, at a typical $x$"),
        (22.0, 5.0, "a high-leverage point, far out in $x$"),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.1))
    for ax, (xo, yo, title) in zip(axes, cases):
        xa = np.append(x, xo)
        ya = np.append(y, yo)
        b1, b0 = np.polyfit(x, y, 1)
        c1, c0 = np.polyfit(xa, ya, 1)
        xs = np.linspace(0, max(11, xo + 1), 50)
        ax.scatter(x, y, s=16, color=ACCENT, alpha=0.8, edgecolors="none")
        ax.scatter([xo], [yo], s=55, facecolors="none", edgecolors=ORANGE, lw=1.8)
        ax.plot(xs, b0 + b1 * xs, color=GREY, lw=1.6, ls="--",
                label=f"without: slope {b1:.2f}")
        ax.plot(xs, c0 + c1 * xs, color=ORANGE, lw=1.9,
                label=f"with: slope {c1:.2f}")
        ax.set_title(title, fontsize=9.5)
        ax.set_xlabel("x")
        ax.legend(frameon=False, fontsize=8, loc="upper left")
    axes[0].set_ylabel("y")
    save(fig, "ch00_outlier_influence.png")


# 17 -- Why distances need standardised variables -----------------------------
def fig_standardisation():
    d = credit[["Income", "Limit"]].to_numpy()[:120]
    q = np.array([50.0, 5000.0])          # the query customer

    def nearest(mat, point):
        return int(np.argmin(((mat - point) ** 2).sum(axis=1)))

    raw_nb = nearest(d, q)
    mu, sd = d.mean(axis=0), d.std(axis=0, ddof=1)
    z = (d - mu) / sd
    zq = (q - mu) / sd
    std_nb = nearest(z, zq)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.3))
    GREEN = "#2E7D5B"

    # Both candidate neighbours are marked in both panels, so the switch is visible.
    for ax, pts, query, xlab, ylab, title in (
        (ax1, d, q, "Income (thousands of \\$)", "Limit (\\$)",
         "Raw units: 'Limit' dwarfs 'Income', so it decides"),
        (ax2, z, zq, "Income ($z$-score)", "Limit ($z$-score)",
         "Standardised: both variables now count equally"),
    ):
        ax.scatter(pts[:, 0], pts[:, 1], s=14, color=ACCENT, alpha=0.5,
                   edgecolors="none")
        ax.scatter(*query, marker="*", s=170, color="black", zorder=6,
                   label="the customer we ask about")
        ax.plot([query[0], pts[raw_nb, 0]], [query[1], pts[raw_nb, 1]],
                color=ORANGE, lw=1.6, zorder=4)
        ax.plot([query[0], pts[std_nb, 0]], [query[1], pts[std_nb, 1]],
                color=GREEN, lw=1.6, ls="--", zorder=4)
        ax.scatter(*pts[raw_nb], s=90, facecolors="none", edgecolors=ORANGE, lw=2,
                   zorder=5, label="nearest in raw units")
        ax.scatter(*pts[std_nb], s=90, facecolors="none", edgecolors=GREEN, lw=2,
                   zorder=5, label="nearest after standardising")
        ax.set_title(title, fontsize=9)
        ax.set_xlabel(xlab)
        ax.set_ylabel(ylab)
    ax1.legend(frameon=False, fontsize=7.5, loc="upper left")
    save(fig, "ch00_standardisation.png")
    print(f"    (nearest neighbour: row {raw_nb} raw vs row {std_nb} standardised)")


# 18 -- Gradient descent on a real loss surface -------------------------------
def fig_gradient_descent():
    X = np.array([[1.0, 1.0], [1.0, 2.0], [1.0, 3.0]])
    y = np.array([2.0, 3.0, 5.0])
    beta_hat = np.linalg.solve(X.T @ X, X.T @ y)

    def loss(b0, b1):
        return sum((yi - b0 - b1 * xi) ** 2 for xi, yi in zip(X[:, 1], y))

    def path(alpha, steps):
        b = np.zeros(2)
        out = [b.copy()]
        for _ in range(steps):
            b = b + 2 * alpha * X.T @ (y - X @ b)
            out.append(b.copy())
        return np.array(out)

    fig, axes = plt.subplots(1, 2, figsize=(8.8, 3.3))
    settings = [
        (0.01, 60, "$\\alpha = 0.01$: converges \u2014 but slowly",
         (-1.5, 2.5), (-0.6, 3.0)),
        (0.07, 6, "$\\alpha = 0.07$: overshoots, and every step is worse",
         (-4.0, 5.5), (-8.0, 9.0)),
    ]
    for ax, (alpha, steps, title, xlim, ylim) in zip(axes, settings):
        g0, g1 = np.meshgrid(np.linspace(*xlim, 220), np.linspace(*ylim, 220))
        Z = loss(g0, g1)
        ax.contour(g0, g1, Z, levels=np.geomspace(0.3, Z.max(), 16), colors=[GREY],
                   linewidths=0.6, alpha=0.7)
        pth = path(alpha, steps)
        ax.plot(pth[:, 0], pth[:, 1], "-o", color=ORANGE, ms=3, lw=1.2)
        ax.plot(*beta_hat, "*", color="black", ms=14, zorder=5)
        ax.annotate("start", xy=(0, 0), xytext=(0.12, 0.06), fontsize=8,
                    xycoords="data", textcoords="axes fraction",
                    arrowprops={"arrowstyle": "->", "color": GREY, "lw": 0.8})
        ax.set_title(title, fontsize=9.5)
        ax.set_xlabel(r"$\beta_0$")
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
    axes[0].set_ylabel(r"$\beta_1$")
    axes[0].annotate("least-squares\nsolution", xy=tuple(beta_hat), xytext=(-1.25, 2.4),
                     fontsize=8,
                     arrowprops={"arrowstyle": "->", "color": GREY, "lw": 0.8})
    save(fig, "ch00_gradient_descent.png")




def fig_se_shrinks():
    """The square-root law: SE of the mean vs n, theory and simulation.

    Complements fig_lln (which tracks one running mean): here each dot is the
    *standard deviation of 4,000 sample means* at that n, against sigma/sqrt(n).
    """
    sigma = 10.0
    n_grid = np.unique(np.round(np.logspace(np.log10(2), 3, 50)).astype(int))
    theory = sigma / np.sqrt(n_grid)

    n_sim = np.array([2, 5, 10, 25, 60, 150, 400, 1000])
    rng = np.random.default_rng(SEED)
    sim = [rng.normal(50, sigma, size=(4000, n)).mean(axis=1).std(ddof=1)
           for n in n_sim]

    fig, ax = plt.subplots(figsize=(6.2, 3.3))
    ax.plot(n_grid, theory, color=ACCENT, lw=2, zorder=3)
    ax.plot(n_sim, sim, "o", color=ORANGE, ms=5, mec="white", mew=0.8, zorder=4)
    ax.text(6.4, 5.6, r"theory: $\mathrm{SE} = \sigma/\sqrt{n}$", color=ACCENT, fontsize=9.5)
    ax.text(150, 1.15, "simulation: SD of 4,000\nsample means at each $n$",
            color=ORANGE, fontsize=8.5)

    for n0 in (25, 100):
        se = sigma / np.sqrt(n0)
        ax.plot([n0, n0], [0, se], color=GREY, lw=0.9, ls=":", zorder=1)
        ax.plot([2, n0], [se, se], color=GREY, lw=0.9, ls=":", zorder=1)
    ax.annotate("quadruple $n$ (25 $\\to$ 100)\nto halve the SE (2 $\\to$ 1)",
                xy=(100, 1.0), xytext=(28, 3.4), fontsize=8.5, color="#333333",
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))

    ax.set_xscale("log")
    ax.set_xlabel("sample size $n$")
    ax.set_ylabel(r"standard error of $\bar{x}$  ($\sigma = 10$)")
    ax.set_xlim(1.8, 1100); ax.set_ylim(0, 7.5)
    ax.set_xticks([2, 5, 10, 25, 100, 1000])
    ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())
    save(fig, "ch00_se_shrinks.png")
    print("ch00_se_shrinks: SE(25) =", round(sigma/5, 2), " SE(100) =", round(sigma/10, 2))


if __name__ == "__main__":
    fig_center_spread()
    fig_boxplot_anatomy()
    fig_correlation()
    fig_clt()
    fig_reference_dists()
    fig_ci_coverage()
    fig_slr()
    fig_shape_gallery()
    fig_log_transform()
    fig_anscombe()
    fig_simpson()
    fig_normal_rule()
    fig_pvalue()
    fig_power()
    fig_lln()
    fig_outlier_influence()
    fig_standardisation()
    fig_gradient_descent()
    fig_se_shrinks()
