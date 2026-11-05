"""Generate every figure of the dissertation as a scalable SVG.

Run:  python -I scripts/figures/build_figures.py
Writes figures/fig-NN-slug.svg (600 units wide = 6 in at the text width) and figures/FIGURES.md,
a manifest of number, title, chapter placement and file.

Every figure is computed: curves from the formulas of Chapter 3, Chapter 4 and Appendix A, diagrams
from the definitions. Illustrative parameters are stated in the figure's note in the manuscript.
"""
from __future__ import annotations

import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from svg import (SVG, Axes, ACCENT, ACCENT_PALE, BLACK, DARK, INK, LIGHT, MID, PALE, WARN, W, fmt)  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "figures")
FIGURES: list[tuple[int, str, str, str]] = []   # (number, file, title, placement)

# Figure numbers follow the order of first mention in the manuscript (APA 7), which is not the order in
# which the figures were written below. place_figures.py uses the same table.
NUMBERS = {
    "one-architecture-two-terms": 1, "framework-architecture": 2, "disagreement-payoff-vs-exit-option": 3,
    "conditions-and-dependencies": 4, "dependence-and-divided-commons": 5, "impatience-and-bargaining-weight": 6,
    "floor-additive-and-substitution": 7, "informational-shadow": 8, "scope-of-claims": 9, "typology-of-regimes": 10,
    "capacity-unit-claim": 11, "share-vs-fixed-quantity": 12, "survival-share-binding-minimum": 13,
    "demurrage-dynamics": 14, "information-gain-pricing": 15, "channels-of-accumulation": 16, "three-paths": 17,
    "credentials-uniqueness-without-substrate": 18, "blind-convention": 19, "ostrom-principles-mapped": 20,
    "convergent-remediation": 21, "strain-trigger-window": 22, "convergence-two-sides": 23,
}


def filename(slug: str) -> str:
    return f"fig-{NUMBERS[slug]:02d}-{slug}.svg"


def register(n, slug, title, placement):
    def deco(fn):
        FIGURES.append((NUMBERS[slug], filename(slug), title, placement))
        fn._meta = (NUMBERS[slug], slug)
        return fn
    return deco


def save(svg: SVG, n: int, slug: str):
    os.makedirs(OUT, exist_ok=True)
    for old in os.listdir(OUT):   # a renumbered figure leaves no stale copy behind
        if old.endswith(f"-{slug}.svg") and old != filename(slug):
            os.remove(os.path.join(OUT, old))
    svg.save(os.path.join(OUT, filename(slug)))


# ─────────────────────────────────────────────────────────────────────────────
# Figure 1. One architecture, two sets of terms (Section 1.1)
# ─────────────────────────────────────────────────────────────────────────────
@register(1, "one-architecture-two-terms", "One Architecture, Two Sets of Terms", "Section 1.1, after the two scenarios")
def fig01():
    s = SVG(W, 300, "One architecture, two sets of terms",
            "Two panels show the same exchange between a person and a synthetic system: data flows from the "
            "person to the system and services flow back. In the first scenario consent, reciprocal value and "
            "real exit all hold; in the second all three fail, and the failures are linked: exit fails first, "
            "then consent, then reciprocity.")
    def panel(x0, title, holds):
        px, py, pw, ph = x0, 36, 280, 240
        s.rect(px, py, pw, ph, fill="none", stroke=LIGHT, width=1)
        s.text(px + pw / 2, py + 16, title, size=11, anchor="middle", weight="bold")
        # parties
        s.box(px + 14, py + 60, 72, 48, ["Person"], size=10)
        s.box(px + pw - 86, py + 60, 72, 48, ["Synthetic", "system"], size=10)
        # flows
        ax1, ax2 = px + 86, px + pw - 86
        s.arrow(ax1 + 4, py + 74, ax2 - 4, py + 74, stroke=INK, width=1.4)
        s.text((ax1 + ax2) / 2, py + 66, "data, attention", size=8.5, anchor="middle")
        s.arrow(ax2 - 4, py + 96, ax1 + 4, py + 96, stroke=INK, width=1.4)
        s.text((ax1 + ax2) / 2, py + 110, "services, care", size=8.5, anchor="middle")
        # condition rows
        names = ["Real exit", "Consent", "Reciprocal value"]
        notes_hold = ["floor secured; can switch; records portable",
                      "account of flows; can refuse; can revoke",
                      "both gain; gains legible; division fair"]
        notes_fail = ["cannot leave: survival runs through the system",
                      "cannot refuse what it cannot leave",
                      "nothing obliges value to flow back"]
        for i, nm in enumerate(names):
            y = py + 140 + i * 30
            ok = holds
            mark = "holds" if ok else "fails"
            col = ACCENT if ok else WARN
            s.circle(px + 26, y, 5, fill=col)
            s.text(px + 38, y, f"{nm}: {mark}", size=9.5, baseline="middle", weight="bold")
            s.text(px + 38, y + 12, (notes_hold if ok else notes_fail)[i], size=8.2, baseline="middle", fill=DARK)
        if not holds:
            # dependency arrows down the failure chain
            s.arrow(px + 26, py + 147, px + 26, py + 163, stroke=WARN, width=1.0, head="arrow-warn")
            s.arrow(px + 26, py + 177, px + 26, py + 193, stroke=WARN, width=1.0, head="arrow-warn")
            s.text(px + pw - 10, py + 230, "each failure entails the next", size=8.2, anchor="end", style="italic", fill=WARN)
    panel(16, "Scenario 1: terms hold", True)
    panel(304, "Scenario 2: terms fail", False)
    s.text(W / 2, 20, "Same flows, same technology, different terms", size=10, anchor="middle", style="italic", fill=DARK)
    s.height = 296
    save(s, 1, "one-architecture-two-terms")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 2. The three conditions, their clauses and the dependencies (Section 3.4)
# ─────────────────────────────────────────────────────────────────────────────
@register(2, "conditions-and-dependencies", "The Three Conditions, Their Nine Clauses, and the Dependencies Among Them", "Section 3.4, after Proposition 3")
def fig02():
    s = SVG(W, 330, "The three conditions, their nine clauses, and the clause-level dependencies",
            "Three columns list the clauses of real exit, consent and reciprocal value. Arrows show the four "
            "dependencies the chapter establishes: a failure of E(i) entails a failure of C(ii) and, where the "
            "sub-floor position determines the division, of R(iii); a failure of E(iii) entails a failure of "
            "C(iii) where destroyed assets exceed value received; and a complete failure of C(i) entails a failure "
            "of R(ii). Exit is prior; consent and reciprocity are not ordered with respect to each other.")
    s.height = 322
    cols = [
        ("Condition E: Real exit", [("E(i)", "disagreement payoff at or above the floor"),
                                     ("E(ii)", "an exit option not drastically worse"),
                                     ("E(iii)", "leaving destroys no accumulated assets")]),
        ("Condition C: Consent", [("C(i)", "accurate account of the flows and their shadows"),
                                  ("C(ii)", "can refuse, entering no other, above the floor"),
                                  ("C(iii)", "can revoke at a bounded cost")]),
        ("Condition R: Reciprocal value", [("R(i)", "each party's net gain is positive"),
                                           ("R(ii)", "gains are legible to both"),
                                           ("R(iii)", "division not set solely by an unchosen asymmetry")]),
    ]
    cx = [12, 210, 408]
    cw = 180
    rows_y = [100, 160, 220]
    bh = 48
    for k, (title, clauses) in enumerate(cols):
        x = cx[k]
        s.rect(x, 40, cw, 244, fill=PALE if k == 0 else "#ffffff", stroke=LIGHT, width=1, rx=4)
        s.text(x + cw / 2, 60, title, size=9.5, anchor="middle", weight="bold")
        for j, (code, rest) in enumerate(clauses):
            y = rows_y[j]
            s.rect(x + 8, y - 20, cw - 16, bh, fill="#ffffff", stroke=MID, width=0.8, rx=3)
            s.text(x + 14, y - 6, code, size=9, weight="bold")
            for i, line in enumerate(s.wrap(rest, 7.5, cw - 28)[:2]):
                s.text(x + 14, y + 7 + i * 11, line, size=7.5, fill=DARK)
    # dependency arrows (from failing clause to entailed failure)
    def dep(k1, j1, k2, j2, label, dash=None, bend=-16, ly=None):
        x1 = cx[k1] + cw - 8; y1 = rows_y[j1] + 4
        x2 = cx[k2] + 8; y2 = rows_y[j2] + 4
        s.curve_arrow(x1, y1, (x1 + x2) / 2, (y1 + y2) / 2 + bend, x2, y2, stroke=ACCENT, width=1.4, dash=dash, head="arrow-accent")
        s.text((x1 + x2) / 2, ly if ly is not None else (y1 + y2) / 2 + bend - 4, label, size=7.5, anchor="middle", fill=ACCENT)
    dep(0, 0, 1, 1, "Prop. 1", ly=rows_y[0] - 26)                                   # E(i) -> C(ii)
    dep(0, 2, 1, 2, "if assets lost exceed value", dash="3 2", bend=18, ly=rows_y[2] + 44)   # E(iii) -> C(iii)
    dep(1, 0, 2, 1, "if complete", dash="3 2", ly=rows_y[0] - 26)                   # C(i) -> R(ii)
    # E(i) -> R(iii): long arrow beneath the boxes
    s.path(f"M {fmt(cx[0]+40)} {fmt(rows_y[0]+28)} L {fmt(cx[0]+40)} 296 L {fmt(cx[2]+40)} 296 L {fmt(cx[2]+40)} {fmt(rows_y[2]+30)}",
           stroke=ACCENT, width=1.4, dash="3 2", marker="arrow-accent")
    s.text(W / 2, 310, "E(i) fails and the sub-floor position alone sets the division: R(iii) fails (Prop. 3)", size=8, anchor="middle", fill=ACCENT)
    save(s, 2, "conditions-and-dependencies")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 3. Disagreement payoff versus exit option in the bargaining set (Section 3.3, A.3, A.3.4)
# ─────────────────────────────────────────────────────────────────────────────
def nash_frontier(V):
    return lambda uh: V - uh


@register(3, "disagreement-payoff-vs-exit-option", "A Disagreement Payoff Moves the Bargained Share; an Exit Option Only Bounds It", "Section 3.3, after the definition of the exit option")
def fig03():
    s = SVG(W, 330, "A disagreement payoff moves the bargained share; an exit option only bounds it",
            "Two panels plot the human party's payoff on the horizontal axis and the synthetic party's on the "
            "vertical axis, with the feasible frontier u_h + u_s = V. Left: raising the human party's "
            "disagreement payoff from d to d' moves the Nash solution along the frontier toward the human party. "
            "Right: an outside option o_h leaves the solution unchanged unless it exceeds the Nash payoff, in which "
            "case the human party receives exactly o_h and no more.")
    V = 10.0
    def panel(x0, title):
        ax = Axes(s, x0 + 46, 40, 210, 200, 0, 12, 0, 12)
        ax.frame(xticks=(), yticks=(), size=9,
                 xlabel_runs=[("u", "i"), ("h", "isub"), ("  (human party)", "")],
                 ylabel_runs=[("u", "i"), ("s", "isub"), ("  (synthetic party)", "")])
        s.text(x0 + 46 + 105, 28, title, size=10.5, anchor="middle", weight="bold")
        ax.curve(nash_frontier(V), xmin=0, xmax=V, stroke=INK, width=1.6)
        s.rich(ax.X(V) - 2, ax.Y(0.6), [("u", "i"), ("h", "isub"), (" + ", ""), ("u", "i"), ("s", "isub"), (" = ", ""), ("V", "i")], size=9, anchor="end")
        return ax
    # left: disagreement payoff shift
    ax = panel(10, "Disagreement payoff")
    d = (2.0, 2.0); d2 = (5.0, 2.0)
    for (dh, ds), lab, col in [(d, "d", MID), (d2, "d′", ACCENT)]:
        surplus = V - dh - ds
        uh = dh + surplus / 2; us = ds + surplus / 2
        ax.point(dh, ds, fill=col)
        ax.label(dh, ds, lab, dx=5, dy=12, style="italic", fill=col)
        ax.svg.line(ax.X(dh), ax.Y(ds), ax.X(uh), ax.Y(us), stroke=col, width=1.0, dash="2 2")
        ax.point(uh, us, fill=col)
        ax.svg.line(ax.X(uh), ax.Y(us), ax.X(uh), ax.Y(0), stroke=col, width=0.8, dash="1 2")
    ax.svg.rich(ax.X(4) + 3, ax.Y(0) + 13, [("u", "i"), ("h", "isub"), ("*", "")], size=9, anchor="middle", fill=MID)
    ax.svg.rich(ax.X(6.5) + 3, ax.Y(0) + 13, [("u", "i"), ("h", "isub"), ("*′", "")], size=9, anchor="middle", fill=ACCENT)
    s.arrow(ax.X(2.3), ax.Y(2.0) + 1, ax.X(4.7), ax.Y(2.0) + 1, stroke=ACCENT, width=1.2, head="arrow-accent")
    s.text(ax.X(3.5), ax.Y(2.0) + 24, "floor raises d", size=8.5, anchor="middle", fill=ACCENT, style="italic")
    s.text(ax.X(0.3), ax.Y(11.3), "The split moves with d: each party", size=8, fill=DARK)
    s.text(ax.X(0.3), ax.Y(10.6), "gets its d plus half the surplus", size=8, fill=DARK)
    s.text(ax.X(0.3), ax.Y(9.9), "(Nash, 1950).", size=8, fill=DARK)
    # right: outside option
    ax = panel(310, "Exit option")
    dh, ds = 2.0, 2.0
    surplus = V - dh - ds
    uh = dh + surplus / 2; us = ds + surplus / 2
    ax.point(dh, ds, fill=MID); ax.label(dh, ds, "d", dx=5, dy=12, style="italic", fill=MID)
    ax.svg.line(ax.X(dh), ax.Y(ds), ax.X(uh), ax.Y(us), stroke=MID, width=1.0, dash="2 2")
    ax.point(uh, us, fill=MID)
    # non-binding option
    ax.vline(4.0, 0, V - 4.0, stroke=DARK, width=1.0, dash="4 2")
    ax.svg.rich(ax.X(4.0), ax.Y(0) + 13, [("o", "i"), ("h", "isub"), (" < ", ""), ("u", "i"), ("h", "isub"), ("*", "")], size=8.5, anchor="middle", fill=DARK)
    s.text(ax.X(4.0) - 4, ax.Y(2.4), "does not bind:", size=8, fill=DARK, anchor="end")
    s.text(ax.X(4.0) - 4, ax.Y(1.7), "no effect", size=8, fill=DARK, anchor="end")
    # binding option
    ax.vline(7.5, 0, V - 7.5, stroke=ACCENT, width=1.4, dash="4 2")
    ax.point(7.5, V - 7.5, fill=ACCENT)
    ax.svg.rich(ax.X(7.5), ax.Y(0) + 13, [("o", "i"), ("h", "isub"), (" > ", ""), ("u", "i"), ("h", "isub"), ("*", "")], size=8.5, anchor="middle", fill=ACCENT)
    s.text(ax.X(7.5) + 4, ax.Y(4.2), "binds: party", size=8, fill=ACCENT)
    s.rich(ax.X(7.5) + 4, ax.Y(3.5), [("gets exactly ", ""), ("o", "i"), ("h", "isub")], size=8, fill=ACCENT)
    s.text(ax.X(0.3), ax.Y(11.3), "An option matters only when it exceeds", size=8, fill=DARK)
    s.text(ax.X(0.3), ax.Y(10.6), "the bargained payoff, and then only", size=8, fill=DARK)
    s.text(ax.X(0.3), ax.Y(9.9), "up to its own value.", size=8, fill=DARK)
    s.height = 300
    save(s, 3, "disagreement-payoff-vs-exit-option")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 4. Additive and substitution cases of the floor (Section 3.6, A.3.1)
# ─────────────────────────────────────────────────────────────────────────────
@register(4, "floor-additive-and-substitution", "What an Unconditional Floor Does to the Division of Surplus: The Additive and Substitution Cases", "Section 3.6, after the paragraph on the division of surplus")
def fig04():
    s = SVG(W, 330, "What an unconditional floor does to the division of surplus",
            "Left panel, additive case: the floor of value Delta raises the human party's disagreement payoff and "
            "the joint value of agreement by the same amount, so the frontier shifts out by Delta and the human "
            "party's payoff rises by exactly Delta while the surplus and its division are unchanged. Right panel, "
            "substitution case: the floor replaces floor goods the provider used to supply at cost c_s, so the "
            "frontier shifts out only by c_s; the surplus shrinks by Delta minus c_s, the human party gains "
            "between Delta over two and Delta, and the provider's payoff falls by at most Delta over two.")
    V, dh, ds, D, cs = 10.0, 2.0, 2.0, 3.0, 1.0
    def panel(x0, title):
        ax = Axes(s, x0 + 46, 40, 210, 200, 0, 15, 0, 15)
        ax.frame(size=9, xlabel_runs=[("u", "i"), ("h", "isub")], ylabel_runs=[("u", "i"), ("s", "isub")])
        s.text(x0 + 46 + 105, 28, title, size=10.5, anchor="middle", weight="bold")
        ax.curve(nash_frontier(V), xmin=0, xmax=V, stroke=MID, width=1.4)
        return ax
    def nash(ax, dh_, ds_, V_, col, lab):
        sur = V_ - dh_ - ds_
        uh = dh_ + sur / 2; us = ds_ + sur / 2
        ax.point(dh_, ds_, fill=col); ax.svg.line(ax.X(dh_), ax.Y(ds_), ax.X(uh), ax.Y(us), stroke=col, width=1.0, dash="2 2")
        ax.point(uh, us, fill=col)
        ax.svg.line(ax.X(uh), ax.Y(us), ax.X(uh), ax.Y(0), stroke=col, width=0.8, dash="1 2")
        return uh, us
    # additive
    ax = panel(10, "Additive case")
    ax.curve(nash_frontier(V + D), xmin=0, xmax=V + D, stroke=ACCENT, width=1.6)
    u0, _ = nash(ax, dh, ds, V, MID, "d")
    u1, _ = nash(ax, dh + D, ds, V + D, ACCENT, "d′")
    s.text(ax.X(u0), ax.Y(0) + 13, "u*", size=8.5, anchor="middle", fill=MID, style="italic")
    s.text(ax.X(u1) + 8, ax.Y(0) + 13, "u* + Δ", size=8.5, anchor="middle", fill=ACCENT, style="italic")
    s.rich(ax.X(V + D) + 2, ax.Y(1.2), [("V", "i"), (" + Δ", "")], size=9, anchor="start", fill=ACCENT)
    s.rich(ax.X(V) + 2, ax.Y(1.2), [("V", "i")], size=9, anchor="start", fill=MID)
    s.text(ax.X(0.3), ax.Y(14.3), "Surplus and division unchanged;", size=8, fill=DARK)
    s.text(ax.X(0.3), ax.Y(13.5), "human party better off by exactly Δ.", size=8, fill=DARK)
    # substitution
    ax = panel(310, "Substitution case")
    ax.curve(nash_frontier(V + cs), xmin=0, xmax=V + cs, stroke=ACCENT, width=1.6)
    u0, s0 = nash(ax, dh, ds, V, MID, "d")
    u1, s1 = nash(ax, dh + D, ds, V + cs, ACCENT, "d′")
    s.text(ax.X(u0) - 6, ax.Y(0) + 13, "u*", size=8.5, anchor="middle", fill=MID, style="italic")
    s.text(ax.X(u1) + 22, ax.Y(0) + 13, "u* + (Δ + c)/2", size=8.5, anchor="middle", fill=ACCENT, style="italic")
    s.rich(ax.X(V + cs) + 2, ax.Y(1.2), [("V", "i"), (" + c", ""), ("s", "isub")], size=9, anchor="start", fill=ACCENT)
    # provider loss bracket
    ax.svg.line(ax.X(0) - 2, ax.Y(s0), ax.X(u0), ax.Y(s0), stroke=MID, width=0.8, dash="1 2")
    ax.svg.line(ax.X(0) - 2, ax.Y(s1), ax.X(u1), ax.Y(s1), stroke=ACCENT, width=0.8, dash="1 2")
    s.text(ax.X(0.3), ax.Y(14.3), "Surplus shrinks by Δ − c; human gain", size=8, fill=DARK)
    s.text(ax.X(0.3), ax.Y(13.5), "between Δ/2 and Δ; provider loses at", size=8, fill=DARK)
    s.text(ax.X(0.3), ax.Y(12.7), "most Δ/2 (equal patience).", size=8, fill=DARK)
    s.height = 300
    save(s, 4, "floor-additive-and-substitution")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 5. Impatience and the bargaining weight (A.3.2)
# ─────────────────────────────────────────────────────────────────────────────
@register(5, "impatience-and-bargaining-weight", "Impatience Below the Floor Drives the Human Party's Share of the Surplus Toward Zero", "Section 3.6, after the paragraph on impatience")
def fig05():
    s = SVG(W, 300, "Impatience below the floor drives the human party's share of the surplus toward zero",
            "The human party's bargaining weight alpha equals r_s divided by r_h plus r_s, plotted against the "
            "human party's discount rate r_h for a fixed r_s. As r_h grows without bound, which the survival "
            "constraint implies for a party below its floor, alpha falls toward zero and the party receives only "
            "its disagreement payoff. A floor keeps r_h finite and so keeps alpha positive.")
    rs = 1.0
    ax = Axes(s, 70, 36, 440, 200, 0, 10, 0, 1.0)
    ax.frame(xticks=(0, 2, 4, 6, 8, 10), yticks=(0, 0.25, 0.5, 0.75, 1.0),
             xtick_labels=["0", "2", "4", "6", "8", "10"], ytick_labels=["0", "0.25", "0.50", "0.75", "1"],
             xlabel_runs=[("r", "i"), ("h", "isub"), ("  (human party's discount rate, in units of ", ""), ("r", "i"), ("s", "isub"), (")", "")],
             ylabel_runs=[("α = ", ""), ("r", "i"), ("s", "isub"), (" / (", ""), ("r", "i"), ("h", "isub"), (" + ", ""), ("r", "i"), ("s", "isub"), (")", "")], grid=True)
    ax.curve(lambda rh: rs / (rh + rs), xmin=0, xmax=10, stroke=INK, width=1.8)
    ax.hline(0.5, 0, 1, stroke=MID, width=0.8, dash="2 2")
    ax.vline(1, 0, 0.5, stroke=MID, width=0.8, dash="2 2")
    ax.point(1, 0.5, fill=INK)
    ax.label(1, 0.5, "", dx=8, dy=-8, runs=[("equal patience: α = ½", "")], size=9)
    # region below floor: large r_h
    ax.svg.rect(ax.X(5), ax.Y(1.0), ax.X(10) - ax.X(5), ax.Y(0) - ax.Y(1.0), fill="url(#hatch)", stroke="none", opacity=0.5)
    s.text(ax.X(7.5), ax.Y(0.9), "below the floor:", size=9, anchor="middle", fill=WARN)
    s.rich(ax.X(7.5), ax.Y(0.82), [("r", "i"), ("h", "isub"), (" → ∞, α → 0", "")], size=9, anchor="middle", fill=WARN)
    s.text(ax.X(7.5), ax.Y(0.74), "party receives d and none of the surplus", size=8, anchor="middle", fill=WARN)
    # floor arrow
    ax.svg.arrow(ax.X(7), ax.Y(0.14), ax.X(2.2), ax.Y(0.33), stroke=ACCENT, width=1.4, head="arrow-accent")
    s.rich(ax.X(5.2), ax.Y(0.40), [("a floor keeps ", ""), ("r", "i"), ("h", "isub"), (" finite", "")], size=9, anchor="middle", fill=ACCENT)
    s.text(ax.X(5.2), ax.Y(0.33), "and α positive", size=9, anchor="middle", fill=ACCENT)
    s.height = 272
    save(s, 5, "impatience-and-bargaining-weight")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 6. Power-dependence and the divided commons (Section 3.5, A.5)
# ─────────────────────────────────────────────────────────────────────────────
@register(6, "dependence-and-divided-commons", "Dependence Rises With Value and Falls With Availability; Divided Among Many Parties, It Loses Its Restraining Force", "Section 3.5, after Proposition 4")
def fig06():
    s = SVG(W, 320, "Dependence rises with value and falls with availability; divided among many parties it loses its restraining force",
            "Left panel: contours of dependence D = v divided by lambda in the plane of motivational investment v "
            "(horizontal) and availability of alternatives lambda (vertical); dependence is high where v is high "
            "and lambda low. Right panel: the private cost of a degrading action borne by one of M synthetic "
            "parties is gamma over M; it falls below the private benefit b once M exceeds gamma over b, after "
            "which the action is individually rational though collectively destructive.")
    # left: D = v / lambda contours
    ax = Axes(s, 60, 40, 210, 200, 0, 10, 0, 10)
    ax.frame(size=9, xlabel_runs=[("v", "i"), ("  motivational investment", "")],
             ylabel_runs=[("λ", "i"), ("  availability elsewhere", "")])
    s.text(165, 28, "Dependence D = g(v, λ)", size=10.5, anchor="middle", weight="bold")
    ax.svg.rect(ax.X(6), ax.Y(3), ax.X(10) - ax.X(6), ax.Y(0) - ax.Y(3), fill=ACCENT_PALE, stroke="none", opacity=0.8)
    for k, col, lx, ly in [(0.5, LIGHT, 4.6, 9.6), (1.0, MID, 8.4, 9.0), (2.0, DARK, 9.2, 5.1), (4.0, INK, 9.2, 2.9)]:
        ax.curve(lambda v, k=k: v / k, xmin=0.2, xmax=10, stroke=col, width=1.2)   # λ = v / D
        ax.label(lx, ly, f"D = {fmt(k)}", dx=0, dy=0, anchor="middle", size=8, fill=col if col != LIGHT else MID)
    s.text(ax.X(8), ax.Y(1.9), "high dependence:", size=8, anchor="middle", fill=ACCENT)
    s.text(ax.X(8), ax.Y(1.1), "high v, low λ", size=8, anchor="middle", fill=ACCENT)
    s.text(ax.X(0.6), ax.Y(8.0), "low dependence:", size=8, fill=DARK)
    s.text(ax.X(0.6), ax.Y(7.2), "alternatives abound", size=8, fill=DARK)
    # right: commons dilution
    gamma, b = 8.0, 2.0
    ax2 = Axes(s, 350, 40, 210, 200, 1, 10, 0, 9)
    ax2.frame(xticks=(1, 2, 4, 6, 8, 10), yticks=(0, 2, 4, 6, 8), size=9,
              xlabel_runs=[("M", "i"), ("  synthetic parties on one population", "")],
              ylabel="cost or benefit to one party")
    s.text(455, 28, "Dilution of restraint", size=10.5, anchor="middle", weight="bold")
    ax2.curve(lambda M: gamma / M, xmin=1, xmax=10, stroke=INK, width=1.8)
    ax2.hline(b, 1, 10, stroke=ACCENT, width=1.4, dash="4 2")
    ax2.svg.rich(ax2.X(9.8), ax2.Y(b) - 6, [("private benefit ", ""), ("b", "i")], size=8.5, anchor="end", fill=ACCENT)
    ax2.svg.rich(ax2.X(2.2), ax2.Y(gamma / 2.2) - 8, [("share of cost ", ""), ("γ", "i"), (" / ", ""), ("M", "i")], size=8.5, fill=INK)
    Mstar = gamma / b
    ax2.vline(Mstar, 0, b, stroke=MID, width=0.8, dash="2 2")
    ax2.point(Mstar, b, fill=WARN)
    ax2.svg.rect(ax2.X(Mstar), ax2.Y(9), ax2.X(10) - ax2.X(Mstar), ax2.Y(0) - ax2.Y(9), fill="url(#hatch)", stroke="none", opacity=0.45)
    s.rich(ax2.X(Mstar) + 6, ax2.Y(7.2), [("M", "i"), (" > ", ""), ("γ", "i"), ("/", ""), ("b", "i"), (": degrading the", "")], size=8.5, fill=WARN)
    s.text(ax2.X(Mstar) + 6, ax2.Y(6.4), "population pays privately", size=8.5, fill=WARN)
    s.text(ax2.X(Mstar) + 6, ax2.Y(5.6), "though it costs all together", size=8.5, fill=WARN)
    s.height = 284
    save(s, 6, "dependence-and-divided-commons")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 7. The informational shadow and level matching (Section 3.7, A.6)
# ─────────────────────────────────────────────────────────────────────────────
@register(7, "informational-shadow", "The Informational Shadow of a Flow and the Level at Which Consent Must Be Given", "Section 3.7, after Proposition 5")
def fig07():
    s = SVG(W, 300, "The informational shadow of a flow and the level at which consent must be given",
            "Left: a single source i sends a flow to a recipient; the flow licenses inferences about a set of "
            "parties, its shadow, that includes i and others who did not consent. Right: the collective shadow of "
            "a population is the union of its members' shadows; Proposition 5 requires the three conditions at "
            "the level of that union, above a materiality threshold the governance layer sets.")
    # left
    s.text(150, 28, "One flow, one shadow", size=10.5, anchor="middle", weight="bold")
    s.box(30, 110, 70, 40, ["source i"], size=10, fill="#ffffff")
    s.box(220, 110, 80, 40, ["recipient", "(model)"], size=10, fill="#ffffff")
    s.arrow(100, 130, 218, 130, width=1.6)
    s.text(159, 122, "flow", size=9, anchor="middle", style="italic")
    # shadow ellipse around i and others
    s.ellipse(110, 215, 100, 46, fill=ACCENT_PALE, stroke=ACCENT, width=1.2, dash="4 2")
    s.text(110, 180, "shadow Σ", size=9.5, anchor="middle", fill=ACCENT, style="italic")
    s.rich(135, 183, [("i", "isub")], size=9.5, fill=ACCENT)
    pts = [(55, 215), (85, 205), (110, 225), (140, 205), (165, 215)]
    for k, (x, y) in enumerate(pts):
        s.circle(x, y, 5, fill=ACCENT if k == 2 else "#ffffff", stroke=ACCENT, width=1.2)
    s.text(110, 240, "i", size=9, anchor="middle", style="italic", fill=ACCENT)
    s.note(272, "the others the flow licenses inferences about consented to nothing (Viljoen, 2021)", size=8, x=110, max_width=200, style="normal")
    # dashed line linking flow to shadow
    s.line(160, 136, 130, 170, stroke=ACCENT, width=0.9, dash="2 2")
    # right
    s.text(450, 28, "Population and collective shadow", size=10.5, anchor="middle", weight="bold")
    cx, cy = 450, 165
    s.ellipse(cx, cy, 130, 95, fill="none", stroke=INK, width=1.4)
    s.rich(cx - 118, cy - 100, [("Σ", ""), ("P", "isub"), (" = ∪ Σ", ""), ("i", "isub"), ("  (collective shadow)", "")], size=9.5)
    # member shadows
    for (ex, ey, rx, ry) in [(410, 150, 50, 30), (470, 140, 55, 32), (440, 190, 60, 30), (500, 185, 45, 28)]:
        s.ellipse(ex, ey, rx, ry, fill=ACCENT_PALE, stroke=ACCENT, width=1.0, dash="3 2", opacity=0.85)
    for (x, y) in [(395, 150), (450, 135), (430, 195), (505, 180), (475, 165)]:
        s.circle(x, y, 4, fill=ACCENT, stroke="#ffffff", width=0.8)
    s.note(cy + 112, "population P, everyone the shadows cover: consent, exit and reciprocity must hold at this level (Proposition 5)", size=8, x=cx, max_width=280, style="normal")
    s.height = 312
    save(s, 7, "informational-shadow")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 8. Typology of exchange regimes (Section 3.9)
# ─────────────────────────────────────────────────────────────────────────────
@register(8, "typology-of-regimes", "Five Prototypes of Exchange Regime by Clause Pattern", "Section 3.9, after the typology table")
def fig08():
    s = SVG(W, 300, "Five prototypes of exchange regime by clause pattern",
            "A matrix with the nine clauses as columns and the five prototypes as rows, from partnership, where "
            "every clause holds, through patronage, the marketplace of the desperate and the company town, to "
            "enclosure, where every clause fails. Filled cells mark clauses that hold, open cells clauses that fail, "
            "and half-filled cells clauses that fail conditionally. The present data economy is marked between the "
            "marketplace of the desperate and the company town.")
    clauses = ["E(i)", "E(ii)", "E(iii)", "C(i)", "C(ii)", "C(iii)", "R(i)", "R(ii)", "R(iii)"]
    # 1 holds, 0 fails, 0.5 conditional, None = cannot be assessed
    rows = [
        ("Partnership", [1, 1, 1, 1, 1, 1, 1, 1, 1]),
        ("Patronage", [1, 1, 1, 0, 1, 1, 1, 1, 1]),
        ("Marketplace of the desperate", [0, 1, 1, 1, 0, 1, 1, 1, 0]),
        ("Company town", [0.5, 0, 1, 0, 0.5, 1, None, 0, 0.5]),
        ("Enclosure", [0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ]
    x0, y0 = 150, 60
    cw, rh = 40, 36
    # column headers grouped
    for g, (lab, span) in enumerate([("Real exit", 3), ("Consent", 3), ("Reciprocal value", 3)]):
        gx = x0 + g * 3 * cw
        s.rect(gx, y0 - 34, 3 * cw, 16, fill=PALE, stroke="none")
        s.text(gx + 1.5 * cw, y0 - 23, lab, size=9, anchor="middle", weight="bold")
    for j, c in enumerate(clauses):
        s.text(x0 + j * cw + cw / 2, y0 - 6, c, size=8.5, anchor="middle")
    for i, (name, pat) in enumerate(rows):
        y = y0 + i * rh
        if " of the " in name:
            a, b = name.split(" of the ")
            s.text(x0 - 10, y + rh / 2 - 6, a, size=9, anchor="end", baseline="middle")
            s.text(x0 - 10, y + rh / 2 + 7, "of the " + b, size=9, anchor="end", baseline="middle")
        else:
            s.text(x0 - 10, y + rh / 2, name, size=9.5, anchor="end", baseline="middle", weight="bold" if i in (0, 4) else "normal")
        for j, v in enumerate(pat):
            cx = x0 + j * cw + cw / 2; cy = y + rh / 2
            s.rect(x0 + j * cw, y, cw, rh, fill="none", stroke=LIGHT, width=0.6)
            if v == 1:
                s.circle(cx, cy, 8, fill=ACCENT)
            elif v == 0:
                s.circle(cx, cy, 8, fill="#ffffff", stroke=WARN, width=1.4)
            elif v == 0.5:
                s.circle(cx, cy, 8, fill="#ffffff", stroke=ACCENT, width=1.2)
                s.path(f"M {fmt(cx)} {fmt(cy-8)} A 8 8 0 0 1 {fmt(cx)} {fmt(cy+8)} Z", fill=ACCENT, stroke="none")
            else:
                s.text(cx, cy, "n/a", size=7.5, anchor="middle", baseline="middle", fill=MID)
    # continuum arrow at left
    s.arrow(40, y0 + 6, 40, y0 + 5 * rh - 6, stroke=MID, width=1.2, head="arrow-mid")
    s.text(28, y0 + 2.5 * rh, "direction of travel", size=8.5, anchor="middle", rotate=-90, fill=DARK)
    # present data economy marker
    ym = y0 + 3 * rh
    s.line(x0 - 4, ym, x0 + 9 * cw + 4, ym, stroke=DARK, width=1.0, dash="3 2")
    s.text(x0 + 9 * cw + 8, ym - 6, "present data", size=7.5, baseline="middle", fill=DARK)
    s.text(x0 + 9 * cw + 8, ym + 6, "economy (3.9)", size=7.5, baseline="middle", fill=DARK)
    # legend
    ly = y0 + 5 * rh + 24
    s.circle(x0, ly, 6, fill=ACCENT); s.text(x0 + 12, ly, "holds", size=8.5, baseline="middle")
    s.circle(x0 + 70, ly, 6, fill="#ffffff", stroke=WARN, width=1.4); s.text(x0 + 82, ly, "fails", size=8.5, baseline="middle")
    s.circle(x0 + 130, ly, 6, fill="#ffffff", stroke=ACCENT, width=1.2)
    s.path(f"M {fmt(x0+130)} {fmt(ly-6)} A 6 6 0 0 1 {fmt(x0+130)} {fmt(ly+6)} Z", fill=ACCENT, stroke="none")
    s.text(x0 + 142, ly, "fails conditionally (often, or where another clause fails)", size=8.5, baseline="middle")
    s.height = 318
    s.note(ly + 20, "n/a: cannot be assessed because R(ii) fails. The prototypes are points on a continuum, not a partition (Section 3.9).", size=8, anchor="start", x=x0)
    save(s, 8, "typology-of-regimes")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 9. Capacity, unit and claim: issuance, redemption and retirement (Section 4.4)
# ─────────────────────────────────────────────────────────────────────────────
@register(9, "capacity-unit-claim", "Capacity, Unit and Claim: How the Compute Dividend Is Issued, Redeemed and Retired", "Section 4.4, after the issuance paragraph")
def fig09():
    s = SVG(W, 330, "Capacity, unit and claim: how the compute dividend is issued, redeemed and retired",
            "A flow diagram. Measured capacity C(t) in reference-workload units is the base; a share theta of it is "
            "credited equally to N persons as claims on a settlement ledger; claims are redeemed at par for the "
            "reference workload with owners of capacity up to the obligated share, with a rationing rule beyond it; "
            "demurrage retires idle claims, and the next period's dividend is computed from capacity, not from the "
            "stock of claims.")
    # capacity box
    s.box(20, 60, 150, 70, ["Capacity C(t)", "physical, perishable;", "measured in units"], size=9.5, fill=PALE)
    s.box(225, 60, 150, 70, ["Issuance", "θ · C(t) / N(t)", "to each person"], size=9.5, fill="#ffffff")
    s.box(430, 60, 150, 70, ["Claims", "ledger balances", "denominated in units"], size=9.5, fill="#ffffff")
    s.arrow(170, 95, 223, 95, width=1.6); s.text(197, 88, "share θ", size=8.5, anchor="middle", style="italic")
    s.arrow(375, 95, 428, 95, width=1.6); s.text(402, 88, "credit", size=8.5, anchor="middle", style="italic")
    # redemption
    s.box(430, 190, 150, 70, ["Redemption", "at par for the reference", "workload, up to the", "obligated share"], size=9, fill=ACCENT_PALE, stroke=ACCENT)
    s.arrow(505, 130, 505, 188, width=1.6)
    s.text(512, 160, "spend", size=8.5, style="italic")
    s.box(225, 190, 150, 70, ["Owners of capacity", "deliver workload", "(redemption obligation)"], size=9, fill="#ffffff")
    s.arrow(428, 225, 377, 225, width=1.6)
    # beyond the share
    s.box(430, 280, 150, 36, ["beyond the share: queue,", "lot, or price above par"], size=8.5, fill="#ffffff", stroke=MID)
    s.arrow(505, 260, 505, 278, stroke=MID, width=1.2, head="arrow-mid")
    # demurrage retirement loop
    s.box(225, 280, 150, 36, ["Demurrage retires", "idle claims"], size=9, fill="#ffffff", stroke=MID)
    s.path(f"M 450 125 Q 300 150 300 278", stroke=MID, width=1.2, dash="4 2", marker="arrow-mid")
    s.text(330, 165, "idle balance", size=8.5, fill=DARK, style="italic")
    # next period from capacity
    s.path("M 95 130 Q 95 300 215 300", stroke=INK, width=1.0, dash="1 3")
    s.text(60, 220, "next period's", size=8.5, fill=DARK, style="italic")
    s.text(60, 232, "dividend is computed", size=8.5, fill=DARK, style="italic")
    s.text(60, 244, "from capacity, not", size=8.5, fill=DARK, style="italic")
    s.text(60, 256, "from claims", size=8.5, fill=DARK, style="italic")
    s.text(20, 40, "Three things the word compute names are kept apart: capacity, unit, claim.", size=9, style="italic", fill=DARK)
    s.height = 324
    save(s, 9, "capacity-unit-claim")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 10. Share versus fixed quantity (Section 4.4, A.2)
# ─────────────────────────────────────────────────────────────────────────────
@register(10, "share-vs-fixed-quantity", "A Fixed Quantity of Compute Loses Real Value as Compute Grows Abundant; a Share Tracks the Real Purchasing Power of All Compute", "Section 4.4, after the indexing paragraph")
def fig10():
    s = SVG(W, 310, "A fixed quantity of compute loses real value as compute grows abundant; a share tracks the real purchasing power of all compute",
            "Real value of the allocation over time under illustrative growth: capacity C doubles every two years "
            "and the goods price of a unit of compute falls 20 percent a year (p, the price of goods in compute, rises 25 percent) while population is flat. A fixed "
            "quantity's real value falls with 1 over p; a fixed share's real value tracks C over p, which rises "
            "while capacity grows faster than its relative price falls.")
    g_C = math.log(2) / 2.0      # capacity doubles every two years
    g_p = math.log(1 / 0.8)      # the goods price of a unit of compute falls 20%/yr, so p rises 25%/yr
    ax = Axes(s, 70, 36, 440, 210, 0, 10, 0, 4)
    ax.frame(xticks=(0, 2, 4, 6, 8, 10), yticks=(0, 1, 2, 3, 4), size=9,
             xlabel="years", ylabel="real value of the allocation (year 0 = 1)", grid=True)
    # real value of a fixed quantity = q / p(t), where p is the price of goods in compute units;
    # p RISES as compute becomes abundant (goods cost more compute). Model p(t) = e^{g_p t}: value = e^{-g_p t}.
    ax.curve(lambda t: math.exp(-g_p * t), xmin=0, xmax=10, stroke=WARN, width=1.8)
    ax.curve(lambda t: math.exp((g_C - g_p) * t), xmin=0, xmax=10, stroke=ACCENT, width=1.8)
    ax.hline(1, 0, 10, stroke=MID, width=0.8, dash="2 2")
    ax.label(10, math.exp((g_C - g_p) * 10), "", dx=-4, dy=16, anchor="end", fill=ACCENT,
             runs=[("share θ: real value ∝ ", ""), ("C", "i"), ("/", ""), ("p", "i")])
    ax.label(10, math.exp(-g_p * 10), "", dx=-4, dy=-8, anchor="end", fill=WARN,
             runs=[("fixed quantity: real value ∝ 1/", ""), ("p", "i")])
    s.text(ax.X(0.3), ax.Y(3.8), "Illustrative: capacity doubles every two years;", size=8, fill=DARK)
    s.text(ax.X(0.3), ax.Y(3.5), "the goods price of a unit of compute falls 20 percent a year;", size=8, fill=DARK)
    s.text(ax.X(0.3), ax.Y(3.2), "population constant.", size=8, fill=DARK)
    s.height = 282
    save(s, 10, "share-vs-fixed-quantity")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 11. The survival share with a binding minimum (Section 4.5, A.2)
# ─────────────────────────────────────────────────────────────────────────────
@register(11, "survival-share-binding-minimum", "The Survival Share Is a Percentage With a Binding Physical Minimum", "Section 4.5, after the first bold feature")
def fig11():
    s = SVG(W, 310, "The survival share is a percentage with a binding physical minimum",
            "The survival share sigma, plotted against the per-person allocation a, equals the floor bundle's "
            "value divided by a when that exceeds the ordinary share sigma-zero, is capped at one, and equals "
            "sigma-zero otherwise. Three regions: where the whole allocation falls short of the floor the share "
            "is one and the floor cannot be met without raising theta; where the allocation is modest the share "
            "rises to cover the floor; where the allocation is ample the ordinary share applies.")
    sigma0, fbar = 0.3, 3.0
    ax = Axes(s, 70, 36, 440, 210, 0, 15, 0, 1.1)
    ax.frame(xticks=(0, 3, 5, 10, 15), yticks=(0, 0.3, 0.5, 1.0), size=9,
             xtick_labels=["0", "f̄", "5", "f̄/σ₀", "15"], ytick_labels=["0", "σ₀", "0.5", "1"],
             xlabel_runs=[("a", "i"), ("  per-person allocation (units)", "")],
             ylabel_runs=[("σ", "i"), ("  survival share of the allocation", "")], grid=True)
    f = lambda a: min(1.0, max(sigma0, fbar / a)) if a > 0 else 1.0
    ax.curve(f, xmin=0.01, xmax=15, stroke=INK, width=2.0, n=600)
    # regions
    ax.svg.rect(ax.X(0), ax.Y(1.1), ax.X(fbar) - ax.X(0), ax.Y(0) - ax.Y(1.1), fill="url(#hatch)", stroke="none", opacity=0.5)
    ax.svg.rect(ax.X(fbar), ax.Y(1.1), ax.X(fbar / sigma0) - ax.X(fbar), ax.Y(0) - ax.Y(1.1), fill=ACCENT_PALE, stroke="none", opacity=0.6)
    s.text(ax.X(1.5), ax.Y(0.75), "a < f̄:", size=8.5, anchor="middle", fill=WARN, weight="bold")
    s.text(ax.X(1.5), ax.Y(0.68), "σ = 1, floor", size=8, anchor="middle", fill=WARN)
    s.text(ax.X(1.5), ax.Y(0.61), "not met; θ", size=8, anchor="middle", fill=WARN)
    s.text(ax.X(1.5), ax.Y(0.54), "must rise", size=8, anchor="middle", fill=WARN)
    s.text(ax.X(6.5), ax.Y(0.95), "minimum binds: σ = f̄ / a", size=8.5, anchor="middle", fill=ACCENT, weight="bold")
    s.text(ax.X(6.5), ax.Y(0.88), "the tier delivers exactly the floor", size=8, anchor="middle", fill=ACCENT)
    s.text(ax.X(12.5), ax.Y(0.45), "ordinary share σ₀", size=8.5, anchor="middle", fill=INK, weight="bold")
    s.text(ax.X(12.5), ax.Y(0.38), "tier exceeds the floor;", size=8, anchor="middle", fill=DARK)
    s.text(ax.X(12.5), ax.Y(0.31), "remainder is discretionary", size=8, anchor="middle", fill=DARK)
    s.height = 282
    save(s, 11, "survival-share-binding-minimum")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 12. Balance dynamics under interest and under demurrage (Section 4.6, A.4)
# ─────────────────────────────────────────────────────────────────────────────
@register(12, "demurrage-dynamics", "Idle Balances Compound Under Interest and Converge Under Demurrage", "Section 4.6, after the distributive case")
def fig12():
    s = SVG(W, 320, "Idle balances compound under interest and converge under demurrage",
            "Two parties with the same constant net inflow k but different starting balances. Left: under a "
            "positive return r their balances grow without bound and diverge exponentially. Right: under a "
            "demurrage rate delta both converge to the same steady state k over delta, the difference in starting "
            "wealth decaying with half-life ln 2 over delta.")
    k, r, delta = 1.0, 0.05, 0.10
    W0a, W0b = 2.0, 12.0
    def left_fn(W0): return lambda t: (W0 + k / r) * math.exp(r * t) - k / r
    def right_fn(W0): return lambda t: k / delta + (W0 - k / delta) * math.exp(-delta * t)
    ax = Axes(s, 60, 40, 220, 200, 0, 40, 0, 120)
    ax.frame(xticks=(0, 10, 20, 30, 40), yticks=(0, 40, 80, 120), size=9, xlabel="periods", ylabel="balance W(t)", grid=True)
    s.text(170, 28, "Interest-bearing regime (r > 0)", size=10.5, anchor="middle", weight="bold")
    ax.curve(left_fn(W0b), xmin=0, xmax=40, stroke=INK, width=1.8)
    ax.curve(left_fn(W0a), xmin=0, xmax=40, stroke=MID, width=1.8)
    ax.label(0, W0b, "W(0) = 12", dx=6, dy=-8, size=8.5)
    ax.label(0, W0a, "W(0) = 2", dx=40, dy=-2, size=8.5, fill=MID)
    s.text(ax.X(1.5), ax.Y(112), "gap grows at rate r; no bound", size=8.5, fill=WARN)
    ax2 = Axes(s, 350, 40, 220, 200, 0, 40, 0, 15)
    ax2.frame(xticks=(0, 10, 20, 30, 40), yticks=(0, 5, 10, 15), size=9, xlabel="periods", ylabel="balance W(t)", grid=True)
    s.text(460, 28, "Demurrage regime (δ > 0)", size=10.5, anchor="middle", weight="bold")
    ax2.curve(right_fn(W0b), xmin=0, xmax=40, stroke=INK, width=1.8)
    ax2.curve(right_fn(W0a), xmin=0, xmax=40, stroke=MID, width=1.8)
    ax2.hline(k / delta, 0, 40, stroke=ACCENT, width=1.0, dash="4 2")
    ax2.svg.rich(ax2.X(39), ax2.Y(k / delta) - 6, [("steady state ", ""), ("k", "i"), ("/", ""), ("δ", "i")], size=8.5, anchor="end", fill=ACCENT)
    ax2.label(0, W0b, "W(0) = 12", dx=6, dy=-6, size=8.5)
    ax2.label(0, W0a, "W(0) = 2", dx=16, dy=4, size=8.5, fill=MID)
    hl = math.log(2) / delta
    ax2.vline(hl, 0, right_fn(W0b)(hl), stroke=MID, width=0.8, dash="2 2")
    s.text(ax2.X(hl) + 3, ax2.Y(0.6), "half-life ln 2/δ", size=8, fill=DARK)
    s.text(ax2.X(2), ax2.Y(14.3), "endowments forgotten; stocks track flows", size=8.5, fill=ACCENT)
    s.height = 286
    save(s, 12, "demurrage-dynamics")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 13. Three channels of accumulation and the instrument that acts on each (Sections 4.6, 4.8)
# ─────────────────────────────────────────────────────────────────────────────
@register(13, "channels-of-accumulation", "Three Channels of Accumulation and the Instrument That Acts on Each", "Section 4.8, after the three candidate rules")
def fig13():
    s = SVG(W, 300, "Three channels of accumulation and the instrument that acts on each",
            "Discretionary income can be held as idle balances, lent as loan claims, or converted into "
            "compute-generating capacity. Demurrage bounds the first and lowers the lender's net return on the "
            "second without closing it; only a rule on capacity acts on the third, and that rule is left to the "
            "convention. Demurrage therefore has no distributive effect of its own without the capacity rule.")
    s.box(20, 110, 120, 60, ["Discretionary", "income"], size=10, fill=PALE)
    chans = [("Idle balances", "ρ = −δ: bounded at k/δ", "Demurrage", ACCENT, "bounds the balance"),
             ("Loan claims", "net return r − δ; open if r ≥ δ", "Demurrage on claims", MID, "lowers; does not close"),
             ("Capacity: hardware, equity,", "land; compounds at π", "Capacity rule", WARN, "the only instrument; left to the convention")]
    ys = [40, 120, 200]
    for (t1, t2, inst, col, verdict), y in zip(chans, ys):
        s.arrow(140, 140, 208, y + 30, width=1.4)
        s.box(210, y, 170, 60, [t1, t2], size=8.5, fill="#ffffff")
        s.arrow(380, y + 30, 408, y + 30, stroke=col, width=1.4, head="arrow-accent" if col == ACCENT else ("arrow-warn" if col == WARN else "arrow-mid"))
        s.box(410, y + 6, 172, 48, [inst] + s.wrap(verdict, 8, 160), size=8, fill="#ffffff", stroke=col, tcolor=col)
    s.height = 272
    save(s, 13, "channels-of-accumulation")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 14. Information gain declines with each similar contributor (Section 4.7)
# ─────────────────────────────────────────────────────────────────────────────
@register(14, "information-gain-pricing", "Under Information-Gain Pricing the Price of Each Further Similar Datum Falls", "Section 4.7, after the qualifications")
def fig14():
    s = SVG(W, 300, "Under information-gain pricing the price of each further similar datum falls",
            "For a model estimating a parameter with prior variance one and observation noise variance one, the "
            "information the n-th similar datum adds is one half of the log of one plus one over n, which falls "
            "toward zero, while a novel datum, one that bears on a parameter the model has not seen, adds the full "
            "first-observation gain. The price therefore follows novelty to the model, not status among people.")
    def gain(n):  # nats, Gaussian: 1/2 ln((tau+n)/(tau+n-1)) with prior precision tau=1, noise precision 1
        return 0.5 * math.log((1 + n) / n)
    ax = Axes(s, 70, 36, 440, 200, 0, 11, 0, 0.4)
    ax.frame(xticks=tuple(range(1, 11)), yticks=(0, 0.1, 0.2, 0.3, 0.4), size=9,
             xtick_labels=[str(i) for i in range(1, 11)], ytick_labels=["0", "0.1", "0.2", "0.3", "0.4"],
             xlabel="n-th contributor of similar data", ylabel="information gain of the datum (nats)", grid=True)
    for n in range(1, 11):
        g = gain(n)
        ax.svg.rect(ax.X(n) - 12, ax.Y(g), 24, ax.Y(0) - ax.Y(g), fill=ACCENT_PALE, stroke=ACCENT, width=1.0)
        ax.svg.text(ax.X(n), ax.Y(g) - 4, f"{g:.2f}", size=7.5, anchor="middle", fill=DARK)
    # novel datum marker
    ax.svg.rect(ax.X(10.9) - 10, ax.Y(gain(1)), 20, ax.Y(0) - ax.Y(gain(1)), fill="url(#hatch-accent)", stroke=ACCENT, width=1.0)
    s.text(ax.X(10.9), ax.Y(gain(1)) - 4, "novel", size=7.5, anchor="middle", fill=ACCENT)
    s.text(ax.X(2.4), ax.Y(0.385), "gain of the n-th datum = ½ ln(1 + 1/n), Gaussian prior and noise", size=8, fill=DARK)
    s.text(ax.X(2.4), ax.Y(0.36), "of unit variance (Lindley, 1956)", size=8, fill=DARK)
    s.height = 272
    save(s, 14, "information-gain-pricing")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 15. The blind convention: what lies behind the veil and what is decided before it (Chapter 5)
# ─────────────────────────────────────────────────────────────────────────────
@register(15, "blind-convention", "The Blind Convention: What Is Decided Before the Veil and What Lies Behind It", "Section 5.6, after the third pre-veil decision")
def fig15():
    s = SVG(W, 340, "The blind convention: what is decided before the veil and what lies behind it",
            "Nested regions. Outermost: the genesis rules and four pre-veil decisions, the eligibility criterion, "
            "the aggregation rule, the partition of credential issuers and the monitor's accountability, which "
            "are visible and revisable. Inside: weak blindness, under which participants do not know their "
            "counterparties' kind, and strong blindness, under which they also do not know how the rules will "
            "classify them. At the center the convention chooses general formulas for the share, the floor "
            "standard, the workload, the demurrage rate and the capacity rules.")
    # outer
    s.rect(20, 30, 560, 290, fill="#ffffff", stroke=INK, width=1.2, rx=6)
    s.text(32, 48, "Decided before the veil (visible, revisable):", size=10, weight="bold")
    pre = ["1  eligibility: one seat per unique accountable principal",
           "2  aggregation rule (open)",
           "3  partition of the population among credential issuers",
           "4  accountability of the monitor of the convention's blindness"]
    for i, t in enumerate(pre):
        s.text(32, 66 + i * 14, t, size=8.8, fill=DARK)
    # weak blindness
    s.rect(40, 130, 520, 178, fill=PALE, stroke=DARK, width=1.0, rx=6)
    s.text(52, 148, "Weak blindness: counterparties' kind concealed", size=10, weight="bold")
    s.text(52, 162, "prevents coalitions and vote trading by substrate; each participant still knows its own kind", size=8.5, fill=DARK)
    # strong blindness
    s.rect(60, 172, 480, 124, fill=ACCENT_PALE, stroke=ACCENT, width=1.0, rx=6)
    s.text(72, 190, "Strong blindness: how the rules will classify oneself concealed", size=10, weight="bold", fill=ACCENT)
    s.text(72, 204, "force in proportion to the share of borderline participants; none for present principals", size=8.5, fill=ACCENT)
    # center
    s.rect(90, 216, 420, 68, fill="#ffffff", stroke=ACCENT, width=1.2, rx=4)
    s.text(300, 234, "The convention chooses general formulas, not figures:", size=9.5, anchor="middle", weight="bold")
    s.text(300, 250, "share θ · floor standard · workload · demurrage δ · capacity rule · data governance", size=8.5, anchor="middle", fill=DARK)
    s.text(300, 266, "aim: Rawlsian impartiality by public-choice means (Brennan & Buchanan, 1985)", size=8.5, anchor="middle", fill=DARK, style="italic")
    s.height = 332
    save(s, 15, "blind-convention")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 16. Credentials: uniqueness without substrate (Section 5.6)
# ─────────────────────────────────────────────────────────────────────────────
@register(16, "credentials-uniqueness-without-substrate", "Credentials Attest Uniqueness Without Disclosing Substrate: The Issuer Partition and Its Two Gaps", "Section 5.6, after the credential-pooling paragraph")
def fig16():
    s = SVG(W, 320, "Credentials attest uniqueness without disclosing substrate: the issuer partition and its two gaps",
            "Three issuers each certify a disjoint population; each principal receives one credential that attests "
            "it is one bearer of obligations without saying whether it is a person or a system; the credentials "
            "enter a blinded pool that seats one participant per credential. Two gaps are marked: a principal "
            "certified by several issuers could hold several credentials unless the partition is kept disjoint, "
            "and an operator controlling several legal persons could hold several seats.")
    xs = [60, 240, 420]
    for k, x in enumerate(xs):
        s.rect(x, 40, 120, 110, fill=PALE, stroke=LIGHT, width=1, rx=4)
        s.text(x + 60, 56, f"Issuer {k+1}", size=10, anchor="middle", weight="bold")
        s.text(x + 60, 70, "disjoint population", size=8.5, anchor="middle", fill=DARK)
        for j in range(4):
            px = x + 22 + j * 26
            kind = (k * 4 + j) % 3
            if kind == 0:
                s.circle(px, 100, 7, fill="#ffffff", stroke=INK, width=1.2)     # person
            elif kind == 1:
                s.rect(px - 6, 94, 12, 12, fill="#ffffff", stroke=INK, width=1.2)  # system/principal
            else:
                s.path(f"M {px} 93 L {px+7} 106 L {px-7} 106 Z", fill="#ffffff", stroke=INK, width=1.2)  # hybrid
        s.text(x + 60, 128, "one credential each:", size=8.5, anchor="middle", fill=DARK)
        s.text(x + 60, 140, "\"one bearer of obligations\"", size=8.5, anchor="middle", fill=DARK, style="italic")
        s.arrow(x + 60, 152, x + 60, 196, width=1.4)
    # pool
    s.rect(60, 198, 480, 56, fill=ACCENT_PALE, stroke=ACCENT, width=1.2, rx=6)
    s.text(300, 218, "Blinded pool: one seat per credential; substrate not disclosed", size=10, anchor="middle", weight="bold", fill=ACCENT)
    for j in range(12):
        s.circle(90 + j * 38, 240, 6, fill="#ffffff", stroke=ACCENT, width=1.2)
    # legend
    s.circle(66, 282, 6, fill="#ffffff", stroke=INK, width=1.2); s.text(78, 282, "person", size=8.5, baseline="middle")
    s.rect(132, 276, 12, 12, fill="#ffffff", stroke=INK, width=1.2); s.text(150, 282, "system via its principal", size=8.5, baseline="middle")
    s.path("M 282 275 L 289 288 L 275 288 Z", fill="#ffffff", stroke=INK, width=1.2); s.text(296, 282, "hybrid (seated as a person)", size=8.5, baseline="middle")
    s.height = 368
    y = s.note(304, "Gap 1: a principal certified by two issuers holds two credentials unless the partition is disjoint, a pre-veil decision.", size=8, anchor="start", x=60, fill=WARN, style="normal")
    s.note(y + 2, "Gap 2: an operator controlling several legal persons could hold several seats; the criterion resists copying models, not companies (Section 5.6).", size=8, anchor="start", x=60, fill=WARN, style="normal")
    save(s, 16, "credentials-uniqueness-without-substrate")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 17. Ostrom's eight principles mapped onto the framework (Section 5.9)
# ─────────────────────────────────────────────────────────────────────────────
@register(17, "ostrom-principles-mapped", "Ostrom's Eight Design Principles Mapped Onto the Framework, With the Strength of Each Mapping", "Section 5.9, after the eighth principle")
def fig17():
    s = SVG(W, 330, "Ostrom's eight design principles mapped onto the framework, with the strength of each mapping",
            "Eight rows pair each of Ostrom's design principles with the element of the framework it maps onto and "
            "a three-level indicator of how well the mapping holds: supports, partial, or weak. Boundaries are a "
            "constraint rather than a support, collective choice maps only partly onto the blind convention, "
            "monitoring rests on a trusted authority, and nested enterprises has the weakest evidence of the eight.")
    rows = [
        ("1 Clearly defined boundaries", "the identity problem of 5.6: a constraint, not a support", 1),
        ("2 Congruence and proportionality", "two tiers; data pricing; demurrage with capacity rules", 2),
        ("3 Collective-choice arrangements", "the blind convention, which corresponds only partly", 1),
        ("4 Monitoring", "a monitor who is a trusted authority (pre-veil decision 4)", 1),
        ("5 Graduated sanctions", "publicity, then suspension from transacting in the unit", 2),
        ("6 Conflict-resolution mechanisms", "a partial answer to enforcement without a sovereign", 2),
        ("7 Recognition of rights to organize", "states must tolerate a self-governed compute commons", 2),
        ("8 Nested enterprises", "nested systems under a shared unit; weakest evidence", 0),
    ]
    y0 = 52
    s.text(20, 36, "Ostrom's principle", size=9.5, weight="bold")
    s.text(225, 36, "Framework element", size=9.5, weight="bold")
    s.text(580, 36, "Mapping", size=9.5, weight="bold", anchor="end")
    for i, (p, el, strength) in enumerate(rows):
        y = y0 + i * 32
        s.line(20, y - 12, 580, y - 12, stroke=PALE, width=0.8)
        s.text(20, y + 4, p, size=8.8)
        s.text(225, y + 4, el, size=8, fill=DARK)
        # three-dot indicator
        for d in range(3):
            filled = d < (3 if strength == 2 else 2 if strength == 1 else 1)
            s.circle(548 + d * 12, y, 4.5, fill=(ACCENT if strength == 2 else MID if strength == 1 else WARN) if filled else "#ffffff",
                     stroke=(ACCENT if strength == 2 else MID if strength == 1 else WARN), width=1.0)
    ly = y0 + 8 * 32 + 2
    for d, (lab, col, n) in enumerate([("supports", ACCENT, 3), ("partial", MID, 2), ("weak", WARN, 1)]):
        x = 20 + d * 110
        for k in range(3):
            s.circle(x + k * 12, ly, 4.5, fill=col if k < n else "#ffffff", stroke=col, width=1.0)
        s.text(x + 44, ly, lab, size=8.5, baseline="middle")
    s.height = ly + 16
    save(s, 17, "ostrom-principles-mapped")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 18. Convergent remediation (Section 6.3)
# ─────────────────────────────────────────────────────────────────────────────
@register(18, "convergent-remediation", "Convergent Remediation: Many Organizations, Few Models, One Shared Exposure", "Section 6.3, after the condition on the workflow")
def fig18():
    s = SVG(W, 330, "Convergent remediation: many organizations, few models, one shared exposure",
            "Left: before, many organizations fix the same class of flaw independently, so their fixes differ and "
            "a defect in one fix exposes one organization. Right: after, the same few models propose and check the "
            "fixes for all of them, so the fixes converge, a shared defect in the fix is reproduced across all, and "
            "what would have been partly correlated failures become one exposure. The number of dependent systems "
            "is unchanged; only the diversity of their fixes falls.")
    def orgs(x, label):
        s.text(x + 60, 30, label, size=10.5, anchor="middle", weight="bold")
        for i in range(8):
            y = 60 + i * 26
            s.rect(x, y - 8, 120, 18, fill="#ffffff", stroke=INK, width=0.9, rx=2)
            s.text(x + 60, y + 1, f"organization {i+1}", size=8, anchor="middle", baseline="middle")
    # before
    orgs(20, "Before")
    for i in range(8):
        y = 60 + i * 26
        # distinct fixes: differing small glyphs
        s.rect(150, y - 6, 14, 14, fill=[PALE, LIGHT, "#ffffff", ACCENT_PALE][i % 4], stroke=INK, width=0.8, rx=[0, 3, 7, 1][i % 4])
    s.text(157, 282, "fixes differ", size=8.5, anchor="middle", fill=DARK)
    s.text(157, 294, "defect exposes one", size=8.5, anchor="middle", fill=DARK)
    # after
    orgs(300, "After")
    s.box(470, 120, 100, 60, ["same few", "models propose", "and check fixes"], size=8.8, fill=ACCENT_PALE, stroke=ACCENT)
    for i in range(8):
        y = 60 + i * 26
        s.line(420, y, 468, 150, stroke=ACCENT, width=0.8)
        s.line(468, 150, 420, y, stroke="none")
        s.rect(430, y - 6, 14, 14, fill=ACCENT_PALE, stroke=ACCENT, width=0.8, rx=2)
    s.text(437, 282, "fixes converge", size=8.5, anchor="middle", fill=WARN)
    s.text(437, 294, "one shared exposure", size=8.5, anchor="middle", fill=WARN)
    # premise chain
    s.height = 308
    save(s, 18, "convergent-remediation")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 19. Strain, trigger, window and the two branches (Sections 6.1, 6.4, 6.5)
# ─────────────────────────────────────────────────────────────────────────────
@register(19, "strain-trigger-window", "Slow Strain, a Discrete Trigger, and a Window That Opens Onto Two Branches", "Section 6.4, after the layered model")
def fig19():
    s = SVG(W, 300, "Slow strain, a discrete trigger, and a window that opens onto two branches",
            "A timeline. Three slow pressures, labor displacement, energy and physical resources, and strategic "
            "competition, accumulate beneath a threshold; a discrete trigger, the correlated-patch catastrophe, "
            "opens a policy window; the window closes onto either a fair founding, available only if the design "
            "was prepared in advance, or an authoritarian consolidation of control over compute.")
    ax = Axes(s, 40, 50, 320, 170, 0, 10, 0, 10)
    s.line(ax.X(0), ax.Y(0), ax.X(10) + 8, ax.Y(0), width=1.2, marker="arrow")
    s.text(ax.X(10) + 8, ax.Y(0) + 16, "time", size=9.5, anchor="end")
    # strain curve: slow accumulation
    ax.curve(lambda t: 1.2 + 0.55 * t if t < 7 else 1.2 + 0.55 * 7, xmin=0, xmax=7, stroke=INK, width=1.8)
    ax.hline(5.5, 0, 10, stroke=MID, width=0.8, dash="3 2")
    s.text(ax.X(0.2), ax.Y(5.5) - 5, "threshold (Pierson, 2004)", size=8, fill=DARK)
    s.text(ax.X(2.8), ax.Y(1.5), "slow strain: labor, resources,", size=8.5, fill=DARK)
    s.text(ax.X(2.8), ax.Y(0.8), "competition (Section 6.2)", size=8.5, fill=DARK)
    # trigger
    ax.vline(7, 0, 9.4, stroke=WARN, width=1.6)
    s.text(ax.X(7), ax.Y(9.7), "trigger: correlated-patch catastrophe", size=8.5, anchor="middle", fill=WARN, weight="bold")
    # window
    ax.svg.rect(ax.X(7), ax.Y(9.2), ax.X(8.6) - ax.X(7), ax.Y(0) - ax.Y(9.2), fill=ACCENT_PALE, stroke="none", opacity=0.7)
    s.text(ax.X(7.8), ax.Y(0.5), "window", size=8.5, anchor="middle", fill=ACCENT, style="italic")
    s.text(ax.X(7.8), ax.Y(8.6), "(Kingdon, 1984/2003)", size=7.5, anchor="middle", fill=ACCENT)
    # branches
    s.arrow(ax.X(8.6), ax.Y(5.3), ax.X(10) + 60, ax.Y(8.2), stroke=ACCENT, width=1.6, head="arrow-accent")
    s.arrow(ax.X(8.6), ax.Y(5.3), ax.X(10) + 60, ax.Y(2.2), stroke=WARN, width=1.6, head="arrow-warn")
    s.text(ax.X(10) + 66, ax.Y(8.4), "fair founding: only if the", size=8.5, fill=ACCENT)
    s.text(ax.X(10) + 66, ax.Y(7.7), "design was prepared", size=8.5, fill=ACCENT)
    s.text(ax.X(10) + 66, ax.Y(7.0), "(any design that distributes", size=8, fill=DARK)
    s.text(ax.X(10) + 66, ax.Y(6.3), "control would fit; 6.7)", size=8, fill=DARK)
    s.text(ax.X(10) + 66, ax.Y(2.4), "authoritarian branch:", size=8.5, fill=WARN)
    s.text(ax.X(10) + 66, ax.Y(1.7), "consolidation of control", size=8.5, fill=WARN)
    s.text(ax.X(10) + 66, ax.Y(1.0), "over compute (6.5)", size=8.5, fill=WARN)
    s.height = 274
    save(s, 19, "strain-trigger-window")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 20. The scope of the theory's claims (Section 3.8, 7.6)
# ─────────────────────────────────────────────────────────────────────────────
@register(20, "scope-of-claims", "The Scope of the Theory's Claims: Where the Necessary Condition Holds and Where the Sufficiency Conjecture Is Offered", "Section 3.8, after the three theses")
def fig20():
    s = SVG(W, 320, "The scope of the theory's claims",
            "Nested regions of synthetic parties. Outermost: any party, for which the theory claims only that the "
            "floor clause of exit is necessary for a party that cannot leave. Inside: parties with designed and "
            "stable objectives. Innermost: parties that also have an accountable principal, the designed-incentive "
            "regime, in which fair terms, once enforced, are conjectured sufficient. Emergent, unstable or concealed "
            "objectives, and systems beyond the reach of enforcement, lie outside; tissue-based parties in their "
            "own right are not yet reached by the definitions.")
    s.rect(30, 40, 540, 230, fill="#ffffff", stroke=INK, width=1.2, rx=8)
    s.text(42, 58, "Any synthetic party", size=10, weight="bold")
    s.text(42, 72, "claim: E(i) is necessary, for a party that cannot leave, to non-domination (Insufficiency thesis)", size=8.5, fill=DARK)
    s.rect(60, 86, 480, 170, fill=PALE, stroke=DARK, width=1.0, rx=8)
    s.text(72, 104, "Designed and stable objective", size=10, weight="bold")
    s.text(72, 118, "the regime criterion: provenance and stability of the objective, not capability", size=8.5, fill=DARK)
    s.rect(90, 132, 420, 122, fill=ACCENT_PALE, stroke=ACCENT, width=1.2, rx=8)
    s.text(102, 150, "Designed-incentive regime", size=10, weight="bold", fill=ACCENT)
    s.text(102, 164, "a designed, stable objective held by an accountable principal", size=8.5, fill=ACCENT)
    s.text(102, 182, "claim: fair terms, satisfied at every level the data concerns, are sufficient", size=8.5, fill=ACCENT)
    s.text(102, 196, "once enforced (Sufficiency conjecture); open premise: the terms can be made to bind", size=8.5, fill=ACCENT)
    s.text(102, 218, "a superintelligence with such an objective and principal falls here;", size=8.5, fill=DARK)
    s.text(102, 232, "a narrow system with an emergent objective does not (Section 1.2)", size=8.5, fill=DARK)
    # outside markers
    s.height = 345
    s.note(290, "Outside the regime: emergent, unstable or concealed objectives (Scope thesis); parties beyond the reach of enforcement with dependence near zero (Section 7.6); tissue-based parties in their own right, which the definitions do not yet reach (Section 8.5). For these the framework claims only the necessary condition.", size=8, anchor="start", x=42, fill=WARN, style="normal")
    save(s, 20, "scope-of-claims")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 21. Convergence from two sides (Chapter 8)
# ─────────────────────────────────────────────────────────────────────────────
@register(21, "convergence-two-sides", "Convergence From Two Sides: The Question Changes From How Parties Exchange to Who Counts as a Party", "Section 8.5, at its opening")
def fig21():
    s = SVG(W, 300, "Convergence from two sides",
            "Two axes meet. Along the horizontal axis people incorporate machines: records, implants, speech "
            "neuroprostheses with personal voice models. Along the vertical axis machines become biological: "
            "neuromorphic hardware, organoid reservoirs, sentience candidates. Cases from Chapter 8 are placed on "
            "each axis, and the corner where they meet is marked as the point at which the theory's question "
            "changes from how parties should exchange to who counts as a party.")
    ox, oy = 90, 240
    s.line(ox, oy, 560, oy, width=1.4, marker="arrow")
    s.line(ox, oy, ox, 50, width=1.4, marker="arrow")
    s.text(560, oy + 18, "people incorporating machines (8.1)", size=9.5, anchor="end")
    s.text(ox - 14, 50, "machines becoming biological (8.2)", size=9.5, anchor="end", rotate=-90)
    hcases = [("medical records", 160, 1), ("implanted device", 290, 2), ("speech neuroprosthesis", 430, 1)]
    for lab, x, lines in hcases:
        s.circle(x, oy, 4.5, fill=INK)
        s.text(x, oy - 10 - (12 if lines == 2 else 0), lab, size=8.5, anchor="middle")
    s.text(290, oy - 10, "", size=8.5, anchor="middle")
    s.text(430, oy - 22, "with a personal voice model", size=8, anchor="middle", fill=DARK)
    s.text(430, oy - 34, "(Card et al., 2024)", size=8, anchor="middle", fill=DARK)
    vcases = [("neuromorphic hardware", 190), ("organoid reservoir", 130), ("sentience candidate", 80)]
    for lab, y in vcases:
        s.circle(ox, y, 4.5, fill=INK)
        s.text(ox + 10, y + 3, lab, size=8.5)
    # convergence corner
    s.path(f"M 430 {oy-40} Q 440 120 {ox+20} 80", stroke=ACCENT, width=1.2, dash="4 3")
    s.circle(480, 110, 36, fill=ACCENT_PALE, stroke=ACCENT, width=1.2)
    s.text(480, 104, "who counts", size=8.8, anchor="middle", fill=ACCENT, weight="bold")
    s.text(480, 116, "as a party?", size=8.8, anchor="middle", fill=ACCENT, weight="bold")
    s.text(330, 90, "conditions stay substrate-neutral;", size=8.2, anchor="middle", fill=DARK)
    s.text(330, 102, "their content and sufficiency change (8.5)", size=8.2, anchor="middle", fill=DARK)
    s.height = 272
    save(s, 21, "convergence-two-sides")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 22. Three paths: control, control reversed, synthesis (Foreword, Section 5.2)
# ─────────────────────────────────────────────────────────────────────────────
@register(22, "three-paths", "Three Paths: Control in Either Direction Is One Relation With the Roles Exchanged; Synthesis Is a Different Relation", "Section 5.2, after the rejection of permanent sovereignty")
def fig22():
    s = SVG(W, 280, "Three paths: control in either direction is one relation with the roles exchanged; synthesis is a different relation",
            "Three small diagrams. In the first, people hold power over synthetic systems and the systems depend on "
            "them; in the second the roles are exchanged; both are the same relation, in which the dependent party's "
            "outcome rests on the ruler's continuing benevolence and capability. In the third, each party has a "
            "floor it cannot be forced to bargain away and can leave, and the terms are set behind a veil, so "
            "neither depends on the other's goodwill.")
    def pair(x, top, bottom, mode):
        t1, t2 = {"a": ("Path 1:", "people control systems"), "b": ("Path 2:", "systems control people"), "c": ("Path 3:", "synthesis")}[mode]
        s.text(x + 90, 30, t1, size=9.5, anchor="middle", weight="bold")
        s.text(x + 90, 44, t2, size=9.5, anchor="middle", weight="bold")
        if mode in ("a", "b"):
            s.box(x + 40, 60, 100, 36, [top], size=9.5, fill=PALE)
            s.box(x + 40, 150, 100, 36, [bottom], size=9.5, fill="#ffffff")
            s.arrow(x + 90, 96, x + 90, 148, stroke=WARN, width=1.6, head="arrow-warn")
            s.text(x + 98, 118, "rules", size=8.5, fill=WARN)
            s.text(x + 98, 130, "depends", size=8.5, fill=WARN)
            s.text(x + 90, 206, "stable only while the ruler", size=8, anchor="middle", fill=DARK)
            s.text(x + 90, 218, "stays benevolent and strong", size=8, anchor="middle", fill=DARK)
        else:
            s.box(x + 10, 100, 70, 36, ["people"], size=9.5, fill=ACCENT_PALE, stroke=ACCENT)
            s.box(x + 110, 100, 70, 36, ["systems"], size=9.5, fill=ACCENT_PALE, stroke=ACCENT)
            s.arrow(x + 80, 112, x + 108, 112, stroke=ACCENT, width=1.4, head="arrow-accent")
            s.arrow(x + 108, 124, x + 80, 124, stroke=ACCENT, width=1.4, head="arrow-accent")
            s.text(x + 90, 92, "terms: consent, value, exit", size=8, anchor="middle", fill=ACCENT)
            s.rect(x + 20, 150, 140, 40, fill="#ffffff", stroke=ACCENT, width=1.0, rx=4, dash="4 2")
            s.text(x + 90, 166, "floor no one can bargain away;", size=8, anchor="middle", fill=DARK)
            s.text(x + 90, 178, "rules written behind a veil", size=8, anchor="middle", fill=DARK)
            s.text(x + 90, 206, "does not need goodwill in order", size=8, anchor="middle", fill=DARK)
            s.text(x + 90, 218, "to persist (the body's claim)", size=8, anchor="middle", fill=DARK)
    pair(10, "people", "systems", "a")
    pair(205, "systems", "people", "b")
    pair(400, "", "", "c")
    s.brace_h(60, 335, 236, depth=6, stroke=DARK)
    s.height = 290
    s.note(258, "the same relation with the roles exchanged (a stipulation of Section 3.8)", size=8.5, x=197, max_width=330)
    save(s, 22, "three-paths")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 23. The architecture of the framework (Section 1.9 / 9.1)
# ─────────────────────────────────────────────────────────────────────────────
@register(23, "framework-architecture", "The Architecture of the Framework: Conditions, Layers and Presuppositions", "Section 1.9, after the chapter plan")
def fig23():
    s = SVG(W, 340, "The architecture of the framework: conditions, layers and presuppositions",
            "A layered diagram. At the top, the three conditions of fair exchange, with exit prior. Beneath them "
            "the economic layer, a compute-denominated basic income with a survival tier, demurrage and capacity "
            "rules, which secures the floor and prices the flows, and the governance layer, a blind convention "
            "with commons institutions, which sets every power-allocating parameter. At the base, the two premises "
            "everything rests on: the grounding assumption and the enforcement presupposition. The transition "
            "chapter sits beside the layers as the account of how they could come into being.")
    s.rect(60, 30, 480, 52, fill=ACCENT_PALE, stroke=ACCENT, width=1.2, rx=6)
    s.text(300, 48, "Three conditions: real exit (prior) · consent · reciprocal value", size=10.5, anchor="middle", weight="bold", fill=ACCENT)
    s.text(300, 66, "Chapter 3: Propositions 1 to 5, the typology, the three theses", size=8.5, anchor="middle", fill=DARK)
    s.arrow(300, 82, 300, 100, width=1.4)
    s.rect(60, 102, 230, 86, fill="#ffffff", stroke=INK, width=1.0, rx=6)
    s.text(175, 120, "Economic layer (Chapter 4)", size=10, anchor="middle", weight="bold")
    s.lines(72, 136, ["compute unit; share θ of capacity;", "survival tier with binding minimum;", "demurrage; capacity rule; data pricing"], size=8.5, fill=DARK)
    s.rect(310, 102, 230, 86, fill="#ffffff", stroke=INK, width=1.0, rx=6)
    s.text(425, 120, "Governance layer (Chapter 5)", size=10, anchor="middle", weight="bold")
    s.lines(322, 136, ["blind convention; credentials;", "four pre-veil decisions; Ostrom's", "principles; graduated sanctions"], size=8.5, fill=DARK)
    s.arrow(290, 145, 308, 145, width=1.2); s.arrow(308, 160, 290, 160, width=1.2)
    s.text(300, 178, "sets θ, floor standard, workload, δ, capacity rule", size=7.6, anchor="middle", fill=DARK)
    s.arrow(300, 190, 300, 206, width=1.4)
    s.rect(60, 208, 480, 78, fill=PALE, stroke=DARK, width=1.0, rx=6)
    s.text(300, 226, "Premises", size=10, anchor="middle", weight="bold")
    s.text(300, 240, "grounding assumption: people are the only adequate source of input in domains", size=8, anchor="middle", fill=DARK)
    s.text(300, 251, "of meaning, preference, value and culture (Chapter 2, Section 7.1)", size=8, anchor="middle", fill=DARK)
    s.text(300, 266, "enforcement presupposition: an authority able to enforce redemption, acceptance", size=8, anchor="middle", fill=DARK)
    s.text(300, 277, "of the survival tier and the capacity rule (Chapter 4, Section 7.2)", size=8, anchor="middle", fill=DARK)
    s.rect(60, 296, 480, 50, fill="#ffffff", stroke=MID, width=1.0, rx=6, dash="4 2")
    s.text(300, 314, "Transition (Chapter 6): strain, trigger, window · Limitations (Chapter 7) · Convergence (Chapter 8)", size=8, anchor="middle", fill=DARK)
    s.text(300, 332, "The theory is untested; Sections 7.5 and 9.3 state what a test would require.", size=8.5, anchor="middle", fill=DARK, style="italic")
    s.height = 360
    save(s, 23, "framework-architecture")


# ─────────────────────────────────────────────────────────────────────────────
def main():
    fns = [v for k, v in sorted(globals().items()) if k.startswith("fig") and callable(v)]
    for fn in fns:
        fn()
    FIGURES.sort()
    with open(os.path.join(OUT, "FIGURES.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("# Figures\n\nGenerated by `python -I scripts/figures/build_figures.py`. Do not edit the SVGs by hand.\n\n")
        f.write("| No. | File | Title | Placement |\n|---|---|---|---|\n")
        for n, file, title, placement in FIGURES:
            f.write(f"| {n} | `{file}` | {title} | {placement} |\n")
    print(f"wrote {len(FIGURES)} figures to {OUT}")


if __name__ == "__main__":
    main()
