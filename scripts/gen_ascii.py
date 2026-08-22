#!/usr/bin/env python3
"""Procedural ASCII-art monogram (no personal photo) — thick-stroke 'AK' letterforms
rendered via signed-distance-to-segment sampling, same density-ramp technique used by
ascii-art profile cards."""
import math
import random

RAMP = " .:-=+*%#"


def seg_dist(px, py, ax, ay, bx, by):
    abx, aby = bx - ax, by - ay
    apx, apy = px - ax, py - ay
    ab2 = abx * abx + aby * aby
    t = 0.0 if ab2 == 0 else max(0.0, min(1.0, (apx * abx + apy * aby) / ab2))
    cx, cy = ax + t * abx, ay + t * aby
    return math.hypot(px - cx, py - cy)

STROKES = [
    # letter A (apex ~ (35,8), base-left (10,110), base-right (60,110), crossbar y=70)
    (35, 8, 10, 110),
    (35, 8, 60, 110),
    (20, 70, 50, 70),
    # letter K (vertical bar x=110, diagonals from mid (110,62) )
    (110, 8, 110, 110),
    (110, 62, 160, 8),
    (110, 62, 160, 110),
]

THICK = 6.0

BOX_W, BOX_H = 200, 120


def coverage(px, py, samples=3):
    hits = 0
    total = 0
    step = 1.0 / samples
    for sy in range(samples):
        for sx in range(samples):
            qx = px + (sx + 0.5) * step
            qy = py + (sy + 0.5) * step
            total += 1
            d = min(seg_dist(qx, qy, *s) for s in STROKES)
            if d < THICK / 2:
                hits += 1
    return hits / total


def render(cols=96, rows=48, seed=7):
    random.seed(seed)
    lines = []
    for row in range(rows):
        line = []
        py = (row / rows) * BOX_H
        for col in range(cols):
            px = (col / cols) * BOX_W
            cov = coverage(px, py)
            if cov > 0:
                idx = min(len(RAMP) - 1, int(cov * (len(RAMP) - 1)) + 2)
                ch = RAMP[idx]
            else:
                # faint ambient noise, denser near the glyph bounding area
                near = min(seg_dist(px, py, *s) for s in STROKES)
                if near < 30 and random.random() < 0.55:
                    ch = random.choice(" .:")
                elif random.random() < 0.12:
                    ch = "."
                else:
                    ch = " "
            line.append(ch)
        lines.append("".join(line))
    return lines


if __name__ == "__main__":
    for l in render():
        print(l)
