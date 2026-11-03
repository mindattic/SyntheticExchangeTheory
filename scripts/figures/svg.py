"""Minimal, dependency-free SVG drawing helpers for the dissertation's figures.

Every figure is generated from numbers and text, never from bitmaps, so it scales to any size.
Coordinates are in "units" where the figure's viewBox width is 600 units = 6 inches at the
document's text width; font sizes are therefore in points when the figure is printed at 6 inches.

Conventions (APA 7 figures; see docs in build_figures.py):
- sans-serif text, 9-12 pt; no decorative color; grayscale-safe with one muted accent;
- direct labels rather than legends where the geometry allows;
- every SVG carries <title> and <desc> for accessibility.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from xml.sax.saxutils import escape

FONT = "Arial, Helvetica, 'Liberation Sans', sans-serif"
BLACK = "#000000"
INK = "#1a1a1a"
DARK = "#4d4d4d"
MID = "#8c8c8c"
LIGHT = "#cfcfcf"
PALE = "#ececec"
ACCENT = "#2b5d8c"      # one muted blue, used sparingly for the thing a figure is about
ACCENT_PALE = "#dbe6f0"
WARN = "#a0522d"        # one muted red-brown for failure/withdrawal states

W = 600.0               # figure width in units (6 in): 100 units per inch
FONT_SCALE = 1.4        # nominal size n in the figure code prints as n points at 6 in (n * 1.4 units)


def fmt(x: float) -> str:
    """Compact numeric formatting for SVG attributes."""
    if abs(x - round(x)) < 1e-6:
        return str(int(round(x)))
    return f"{x:.2f}".rstrip("0").rstrip(".")


@dataclass
class SVG:
    width: float
    height: float
    title: str
    desc: str
    parts: list[str] = field(default_factory=list)

    # ── primitives ──────────────────────────────────────────────────────────
    def raw(self, s: str) -> None:
        self.parts.append(s)

    def line(self, x1, y1, x2, y2, stroke=INK, width=1.2, dash=None, cap="butt", marker=None, opacity=None):
        a = f'<line x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}" stroke="{stroke}" stroke-width="{fmt(width)}" stroke-linecap="{cap}"'
        if dash:
            a += f' stroke-dasharray="{dash}"'
        if marker:
            a += f' marker-end="url(#{marker})"'
        if opacity is not None:
            a += f' opacity="{opacity}"'
        self.raw(a + "/>")

    def rect(self, x, y, w, h, fill="none", stroke=INK, width=1.0, rx=0, dash=None, opacity=None):
        a = f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" fill="{fill}" stroke="{stroke}" stroke-width="{fmt(width)}"'
        if rx:
            a += f' rx="{fmt(rx)}"'
        if dash:
            a += f' stroke-dasharray="{dash}"'
        if opacity is not None:
            a += f' opacity="{opacity}"'
        self.raw(a + "/>")

    def circle(self, cx, cy, r, fill=INK, stroke="none", width=1.0, opacity=None):
        a = f'<circle cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{fmt(width)}"'
        if opacity is not None:
            a += f' opacity="{opacity}"'
        self.raw(a + "/>")

    def ellipse(self, cx, cy, rx, ry, fill="none", stroke=INK, width=1.0, dash=None, opacity=None):
        a = f'<ellipse cx="{fmt(cx)}" cy="{fmt(cy)}" rx="{fmt(rx)}" ry="{fmt(ry)}" fill="{fill}" stroke="{stroke}" stroke-width="{fmt(width)}"'
        if dash:
            a += f' stroke-dasharray="{dash}"'
        if opacity is not None:
            a += f' opacity="{opacity}"'
        self.raw(a + "/>")

    def path(self, d: str, fill="none", stroke=INK, width=1.2, dash=None, marker=None, opacity=None, join="round"):
        a = f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{fmt(width)}" stroke-linejoin="{join}" stroke-linecap="round"'
        if dash:
            a += f' stroke-dasharray="{dash}"'
        if marker:
            a += f' marker-end="url(#{marker})"'
        if opacity is not None:
            a += f' opacity="{opacity}"'
        self.raw(a + "/>")

    def polyline(self, pts, **kw):
        d = "M " + " L ".join(f"{fmt(x)} {fmt(y)}" for x, y in pts)
        self.path(d, **kw)

    def polygon(self, pts, fill=PALE, stroke=INK, width=1.0, opacity=None):
        d = "M " + " L ".join(f"{fmt(x)} {fmt(y)}" for x, y in pts) + " Z"
        self.path(d, fill=fill, stroke=stroke, width=width, opacity=opacity)

    def text(self, x, y, s, size=10, anchor="start", weight="normal", style="normal", fill=INK,
             baseline="auto", rotate=None, family=FONT, letter=None):
        size = size * FONT_SCALE
        a = (f'<text x="{fmt(x)}" y="{fmt(y)}" font-family="{family}" font-size="{fmt(size)}" '
             f'text-anchor="{anchor}" font-weight="{weight}" font-style="{style}" fill="{fill}" '
             f'dominant-baseline="{baseline}"')
        if rotate is not None:
            a += f' transform="rotate({fmt(rotate)} {fmt(x)} {fmt(y)})"'
        if letter:
            a += f' letter-spacing="{letter}"'
        self.raw(a + f">{escape(s)}</text>")

    def rich(self, x, y, runs, size=10, anchor="start", fill=INK, baseline="auto"):
        """Text with mixed italic/sub/superscript runs: runs = [(text, style)] where style in
        {"", "i", "b", "sub", "sup"}."""
        size = size * FONT_SCALE
        a = (f'<text x="{fmt(x)}" y="{fmt(y)}" font-family="{FONT}" font-size="{fmt(size)}" '
             f'text-anchor="{anchor}" fill="{fill}" dominant-baseline="{baseline}">')
        for s, st in runs:
            if st == "i":
                a += f'<tspan font-style="italic">{escape(s)}</tspan>'
            elif st == "b":
                a += f'<tspan font-weight="bold">{escape(s)}</tspan>'
            elif st == "sub":
                a += f'<tspan baseline-shift="sub" font-size="{fmt(size*0.72)}">{escape(s)}</tspan>'
            elif st == "sup":
                a += f'<tspan baseline-shift="super" font-size="{fmt(size*0.72)}">{escape(s)}</tspan>'
            elif st == "isub":
                a += f'<tspan font-style="italic" baseline-shift="sub" font-size="{fmt(size*0.72)}">{escape(s)}</tspan>'
            else:
                a += escape(s)
        self.raw(a + "</text>")

    def lines(self, x, y, strings, size=10, anchor="start", leading=1.25, weight="normal", style="normal", fill=INK):
        for i, s in enumerate(strings):
            self.text(x, y + i * size * FONT_SCALE * leading, s, size=size, anchor=anchor, weight=weight, style=style, fill=fill)

    def wrap(self, s: str, size: float, max_width: float) -> list[str]:
        """Greedy word wrap using an average glyph width of 0.5 em for the sans face."""
        em = size * FONT_SCALE
        limit = max(1, int(max_width / (0.5 * em)))
        words, lines, cur = s.split(), [], ""
        for w in words:
            cand = (cur + " " + w).strip()
            if len(cand) > limit and cur:
                lines.append(cur)
                cur = w
            else:
                cur = cand
        if cur:
            lines.append(cur)
        return lines

    def note(self, y, s, size=8, max_width=None, anchor="middle", x=None, style="italic", fill=DARK, leading=1.3):
        """A wrapped caption-like note; returns the y just below the last line."""
        max_width = (self.width - 40) if max_width is None else max_width
        x = (self.width / 2 if anchor == "middle" else 20) if x is None else x
        for i, line in enumerate(self.wrap(s, size, max_width)):
            self.text(x, y + i * size * FONT_SCALE * leading, line, size=size, anchor=anchor, style=style, fill=fill)
            last = y + i * size * FONT_SCALE * leading
        return last + size * FONT_SCALE * leading

    # ── compound shapes ─────────────────────────────────────────────────────
    def box(self, x, y, w, h, label_lines, size=10, fill="#ffffff", stroke=INK, width=1.0, rx=3,
            weight="normal", style="normal", tcolor=INK, leading=1.25):
        self.rect(x, y, w, h, fill=fill, stroke=stroke, width=width, rx=rx)
        n = len(label_lines)
        step = size * FONT_SCALE * leading
        total = (n - 1) * step
        y0 = y + h / 2 - total / 2
        for i, s in enumerate(label_lines):
            self.text(x + w / 2, y0 + i * step, s, size=size, anchor="middle",
                      weight=weight, style=style, fill=tcolor, baseline="middle")

    def arrow(self, x1, y1, x2, y2, stroke=INK, width=1.2, dash=None, head="arrow"):
        self.line(x1, y1, x2, y2, stroke=stroke, width=width, dash=dash, marker=head)

    def curve_arrow(self, x1, y1, cx, cy, x2, y2, stroke=INK, width=1.2, dash=None, head="arrow"):
        self.path(f"M {fmt(x1)} {fmt(y1)} Q {fmt(cx)} {fmt(cy)} {fmt(x2)} {fmt(y2)}", stroke=stroke,
                  width=width, dash=dash, marker=head)

    def brace_h(self, x1, x2, y, depth=6, stroke=INK):
        """A simple horizontal brace from x1 to x2 at height y, opening downward."""
        m = (x1 + x2) / 2
        d = (f"M {fmt(x1)} {fmt(y)} Q {fmt(x1)} {fmt(y-depth)} {fmt(x1+depth)} {fmt(y-depth)} "
             f"L {fmt(m-depth)} {fmt(y-depth)} Q {fmt(m)} {fmt(y-depth)} {fmt(m)} {fmt(y-2*depth)} "
             f"Q {fmt(m)} {fmt(y-depth)} {fmt(m+depth)} {fmt(y-depth)} "
             f"L {fmt(x2-depth)} {fmt(y-depth)} Q {fmt(x2)} {fmt(y-depth)} {fmt(x2)} {fmt(y)}")
        self.path(d, stroke=stroke, width=1.0)

    # ── output ──────────────────────────────────────────────────────────────
    def render(self) -> str:
        defs = (
            '<defs>'
            '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{INK}"/></marker>'
            '<marker id="arrow-accent" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{ACCENT}"/></marker>'
            '<marker id="arrow-warn" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{WARN}"/></marker>'
            '<marker id="arrow-mid" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{MID}"/></marker>'
            '<marker id="dot" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5">'
            f'<circle cx="5" cy="5" r="4" fill="{INK}"/></marker>'
            '<pattern id="hatch" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(45)">'
            f'<line x1="0" y1="0" x2="0" y2="6" stroke="{MID}" stroke-width="1"/></pattern>'
            '<pattern id="hatch-accent" patternUnits="userSpaceOnUse" width="6" height="6" patternTransform="rotate(45)">'
            f'<line x1="0" y1="0" x2="0" y2="6" stroke="{ACCENT}" stroke-width="1"/></pattern>'
            '</defs>'
        )
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{fmt(self.width / 100)}in" height="{fmt(self.height / 100)}in" '
                f'viewBox="0 0 {fmt(self.width)} {fmt(self.height)}" role="img" aria-labelledby="t d">\n'
                f'<title id="t">{escape(self.title)}</title>\n<desc id="d">{escape(self.desc)}</desc>\n'
                f'{defs}\n<rect x="0" y="0" width="{fmt(self.width)}" height="{fmt(self.height)}" fill="#ffffff"/>\n')
        return head + "\n".join(self.parts) + "\n</svg>\n"

    def save(self, path: str) -> None:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(self.render())


# ── axes helper for mathematical plots ──────────────────────────────────────
@dataclass
class Axes:
    """Maps data coordinates to figure coordinates inside a plotting rectangle."""
    svg: SVG
    x0: float; y0: float; w: float; h: float          # plot rectangle (y0 is top)
    xmin: float; xmax: float; ymin: float; ymax: float

    def X(self, x: float) -> float:
        return self.x0 + (x - self.xmin) / (self.xmax - self.xmin) * self.w

    def Y(self, y: float) -> float:
        return self.y0 + self.h - (y - self.ymin) / (self.ymax - self.ymin) * self.h

    def frame(self, xlabel="", ylabel="", xticks=(), yticks=(), xtick_labels=None, ytick_labels=None,
              size=9.5, arrows=True, grid=False, xlabel_runs=None, ylabel_runs=None):
        s = self.svg
        bx, by = self.X(self.xmin), self.Y(self.ymin)
        # axes
        s.line(bx, by, self.X(self.xmax) + (10 if arrows else 0), by, width=1.2, marker="arrow" if arrows else None)
        s.line(bx, by, bx, self.Y(self.ymax) - (10 if arrows else 0), width=1.2, marker="arrow" if arrows else None)
        for i, t in enumerate(xticks):
            x = self.X(t)
            if grid:
                s.line(x, by, x, self.Y(self.ymax), stroke=PALE, width=0.8)
            s.line(x, by, x, by + 4, width=1.0)
            lab = xtick_labels[i] if xtick_labels else fmt(t)
            s.text(x, by + 14, lab, size=size, anchor="middle")
        for i, t in enumerate(yticks):
            y = self.Y(t)
            if grid:
                s.line(bx, y, self.X(self.xmax), y, stroke=PALE, width=0.8)
            s.line(bx - 4, y, bx, y, width=1.0)
            lab = ytick_labels[i] if ytick_labels else fmt(t)
            s.text(bx - 7, y, lab, size=size, anchor="end", baseline="middle")
        if xlabel_runs:
            s.rich(self.X(self.xmax) + 10, by + 30, xlabel_runs, size=size + 1, anchor="end")
        elif xlabel:
            s.text(self.X(self.xmax) + 10, by + 30, xlabel, size=size + 1, anchor="end")
        off = 46 if yticks else 24
        if ylabel_runs:
            s.raw(f'<g transform="translate({fmt(bx - off)} {fmt(self.Y(self.ymax) - 6)}) rotate(-90)">')
            s.rich(0, 0, ylabel_runs, size=size + 1, anchor="end")
            s.raw("</g>")
        elif ylabel:
            s.text(bx - off, self.Y(self.ymax) - 6, ylabel, size=size + 1, anchor="end", rotate=-90)

    def curve(self, fn, n=200, xmin=None, xmax=None, **kw):
        a = self.xmin if xmin is None else xmin
        b = self.xmax if xmax is None else xmax
        pts = []
        for i in range(n + 1):
            x = a + (b - a) * i / n
            y = fn(x)
            if y is None or math.isnan(y) or math.isinf(y) or y < self.ymin or y > self.ymax:
                if len(pts) > 1:
                    self.svg.polyline(pts, **kw)
                pts = []
                continue
            pts.append((self.X(x), self.Y(y)))
        if len(pts) > 1:
            self.svg.polyline(pts, **kw)

    def point(self, x, y, r=3.2, fill=INK, stroke="#ffffff", width=1.0):
        self.svg.circle(self.X(x), self.Y(y), r, fill=fill, stroke=stroke, width=width)

    def label(self, x, y, s, dx=6, dy=-6, size=9.5, anchor="start", style="normal", fill=INK, runs=None):
        if runs:
            self.svg.rich(self.X(x) + dx, self.Y(y) + dy, runs, size=size, anchor=anchor, fill=fill)
        else:
            self.svg.text(self.X(x) + dx, self.Y(y) + dy, s, size=size, anchor=anchor, style=style, fill=fill)

    def hline(self, y, x1=None, x2=None, **kw):
        a = self.xmin if x1 is None else x1
        b = self.xmax if x2 is None else x2
        self.svg.line(self.X(a), self.Y(y), self.X(b), self.Y(y), **kw)

    def vline(self, x, y1=None, y2=None, **kw):
        a = self.ymin if y1 is None else y1
        b = self.ymax if y2 is None else y2
        self.svg.line(self.X(x), self.Y(a), self.X(x), self.Y(b), **kw)

    def fill_between(self, fn_lo, fn_hi, xa, xb, n=120, fill=PALE, opacity=None):
        top = [(self.X(xa + (xb - xa) * i / n), self.Y(fn_hi(xa + (xb - xa) * i / n))) for i in range(n + 1)]
        bot = [(self.X(xa + (xb - xa) * i / n), self.Y(fn_lo(xa + (xb - xa) * i / n))) for i in range(n, -1, -1)]
        self.svg.polygon(top + bot, fill=fill, stroke="none", opacity=opacity)
