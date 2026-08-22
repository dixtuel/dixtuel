#!/usr/bin/env python3
import json
import pathlib
import subprocess

MONO = "'Fira Code','Courier New',monospace"
CELL = 12
GAP = 3
LEFT_PAD = 40
TOP_PAD = 46

SCALE = ["#15151c", "#3d0a0a", "#6b1414", "#8B0000", "#C23B3B", "#ff6b5b"]

MONTHS_TR = ["Oca", "Sub", "Mar", "Nis", "May", "Haz", "Tem", "Agu", "Eyl", "Eki", "Kas", "Ara"]


def fetch():
    q = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks { contributionDays { date contributionCount } }
          }
        }
      }
    }
    """
    out = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={q}", "-f", "login=dixtuel"],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def color_for(count, maxc):
    if count == 0:
        return SCALE[0]
    if maxc <= 0:
        return SCALE[1]
    ratio = count / maxc
    idx = 1 + min(int(ratio * (len(SCALE) - 2)), len(SCALE) - 2)
    return SCALE[idx]


def build(cal, theme):
    dark = theme == "dark"
    bg = "#0a0a0f" if dark else "#faf6f5"
    text_main = "#e5c9c9" if dark else "#1a1010"
    text_dim = "#8a6a6a"

    weeks = cal["weeks"]
    n_weeks = len(weeks)
    maxc = max((d["contributionCount"] for w in weeks for d in w["contributionDays"]), default=0)

    width = LEFT_PAD + n_weeks * (CELL + GAP) + 20
    height = TOP_PAD + 7 * (CELL + GAP) + 30

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    parts.append(f'<rect width="{width}" height="{height}" rx="12" fill="{bg}"/>')
    parts.append(
        f'<text x="{LEFT_PAD}" y="24" font-family="{MONO}" font-size="13" fill="{text_main}">'
        f'dixtuel &#8212; contribution heatmap ({cal["totalContributions"]} son 12 ay)</text>'
    )

    last_month = None
    for wi, week in enumerate(weeks):
        x = LEFT_PAD + wi * (CELL + GAP)
        first_day = week["contributionDays"][0] if week["contributionDays"] else None
        if first_day:
            m = int(first_day["date"].split("-")[1]) - 1
            if m != last_month:
                parts.append(f'<text x="{x}" y="{TOP_PAD - 8}" font-family="{MONO}" font-size="9" fill="{text_dim}">{MONTHS_TR[m]}</text>')
                last_month = m
        for di, day in enumerate(week["contributionDays"]):
            y = TOP_PAD + di * (CELL + GAP)
            c = color_for(day["contributionCount"], maxc)
            parts.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{c}"><title>{day["date"]}: {day["contributionCount"]}</title></rect>')

    legend_x = width - 20 - 6 * (CELL + 4)
    legend_y = height - 18
    parts.append(f'<text x="{LEFT_PAD}" y="{height-10}" font-family="{MONO}" font-size="10" fill="{text_dim}">az</text>')
    for i, c in enumerate(SCALE):
        parts.append(f'<rect x="{legend_x + i*(CELL+4)}" y="{legend_y-10}" width="{CELL}" height="{CELL}" rx="2" fill="{c}"/>')
    parts.append(f'<text x="{legend_x + len(SCALE)*(CELL+4) + 4}" y="{height-10}" font-family="{MONO}" font-size="10" fill="{text_dim}">cok</text>')

    parts.append("</svg>")
    return "\n".join(parts)


if __name__ == "__main__":
    cal = fetch()
    out = pathlib.Path(__file__).resolve().parent.parent
    (out / "heatmap-dark.svg").write_text(build(cal, "dark"), encoding="utf-8")
    (out / "heatmap-light.svg").write_text(build(cal, "light"), encoding="utf-8")
    print("wrote heatmap-dark.svg / heatmap-light.svg, total:", cal["totalContributions"])
