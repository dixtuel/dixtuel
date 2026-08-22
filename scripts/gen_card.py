#!/usr/bin/env python3
import random

W, H = 1000, 640
MONO = "'Fira Code','Courier New',monospace"

random.seed(42)
NOISE_LINES = ["".join(random.choice("01") for _ in range(70)) for _ in range(30)]

ROWS = [
    ("ORIGIN", "Turkiye"),
    ("STATUS", "Building - Shipping - Self-hosting"),
    ("STACK.LANG", "Python, TypeScript, JavaScript, Bash"),
    ("STACK.FRONTEND", "Next.js, React, Tailwind CSS"),
    ("STACK.BACKEND", "FastAPI, Flask, Node.js/Express"),
    ("STACK.DATABASE", "PostgreSQL, Redis, SQLite, Prisma"),
    ("STACK.INFRA", "Docker, Caddy, Cloudflare, Linux"),
]

CONTACT = [
    ("GitHub", "github.com/dixtuel"),
    ("Mail", "asrinklcc@dxtl.com.tr"),
    ("Portfolio", "dxtl.com.tr"),
]


def build(theme):
    dark = theme == "dark"
    bg0 = "#05050a" if dark else "#faf6f5"
    bg1 = "#150506" if dark else "#f3e6e6"
    panel = "#0a0a0f" if dark else "#ffffff"
    border_op = "0.35" if dark else "0.25"
    text_main = "#f0d9d9" if dark else "#1a1010"
    text_dim = "#8a6a6a" if dark else "#8a6a6a"
    label_col = "#C23B3B"
    accent = "#8B0000"
    noise_op = "0.05" if dark else "0.035"
    dot_col = "#3d1010" if dark else "#e5cfcf"

    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    parts.append("<defs>")
    parts.append(
        f'<linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">'
        f'<stop offset="0%" stop-color="{accent}"><animate attributeName="stop-color" values="{accent};#C23B3B;#3d0a0a;{accent}" dur="8s" repeatCount="indefinite"/></stop>'
        f'<stop offset="50%" stop-color="#C23B3B"><animate attributeName="stop-color" values="#C23B3B;#3d0a0a;{accent};#C23B3B" dur="8s" repeatCount="indefinite"/></stop>'
        f'<stop offset="100%" stop-color="#3d0a0a"><animate attributeName="stop-color" values="#3d0a0a;{accent};#C23B3B;#3d0a0a" dur="8s" repeatCount="indefinite"/></stop>'
        f"</linearGradient>"
    )
    parts.append(
        f'<radialGradient id="bgGlow" cx="25%" cy="15%" r="85%">'
        f'<stop offset="0%" stop-color="{bg1}"/><stop offset="100%" stop-color="{bg0}"/>'
        f"</radialGradient>"
    )
    parts.append(f'<clipPath id="cardClip"><rect x="8" y="8" width="{W-16}" height="{H-16}" rx="14"/></clipPath>')
    parts.append(
        '<mask id="reveal" maskUnits="userSpaceOnUse" x="0" y="0" width="%d" height="%d">'
        '<rect x="0" y="0" width="%d" height="0" fill="#fff">'
        '<animate attributeName="height" from="0" to="%d" dur="1.4s" begin="0.1s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>'
        "</rect></mask>" % (W, H, W, H)
    )
    parts.append("</defs>")

    parts.append(f'<rect width="{W}" height="{H}" rx="18" fill="{panel}"/>')
    parts.append(f'<rect x="8" y="8" width="{W-16}" height="{H-16}" rx="14" fill="url(#bgGlow)"/>')

    parts.append(f'<g clip-path="url(#cardClip)" opacity="{noise_op}" font-family="{MONO}" font-size="9" fill="{accent}">')
    for i, line in enumerate(NOISE_LINES):
        parts.append(f'<text x="16" y="{34 + i * 18}">{line}</text>')
    parts.append("</g>")

    parts.append(f'<g mask="url(#reveal)">')

    parts.append(f'<rect x="8" y="8" width="{W-16}" height="{H-16}" rx="14" fill="none" stroke="url(#borderGrad)" stroke-width="1.5" opacity="{border_op}"/>')

    parts.append(f'<circle cx="34" cy="34" r="5" fill="{dot_col}"/>')
    parts.append(f'<circle cx="52" cy="34" r="5" fill="{dot_col}"/>')
    parts.append(f'<circle cx="70" cy="34" r="5" fill="{dot_col}"/>')
    parts.append(f'<text x="94" y="38" font-family="{MONO}" font-size="12" fill="{text_dim}">dixtuel@vds &#8212; profile.sh</text>')

    parts.append(f'<line x1="32" y1="54" x2="{W-32}" y2="54" stroke="{accent}" stroke-opacity="0.2"/>')

    parts.append(
        f'<text x="32" y="86" font-family="{MONO}" font-size="15" fill="{label_col}">dixtuel@vds ~ % ./whoami.sh --live'
        f'<tspan fill="{text_main}">&#9608;</tspan>'
        f'<animate attributeName="opacity" values="1;1;0;0;1" keyTimes="0;0.4;0.5;0.9;1" dur="1.2s" repeatCount="indefinite"/>'
        f"</text>"
    )

    parts.append(f'<text x="32" y="134" font-family="{MONO}" font-size="34" font-weight="700" fill="{text_main}">Asrin Kilic</text>')
    parts.append(f'<text x="32" y="160" font-family="{MONO}" font-size="15" fill="{label_col}">Full-Stack &amp; AI Systems Developer</text>')

    parts.append(f'<line x1="32" y1="182" x2="{W-32}" y2="182" stroke="{accent}" stroke-opacity="0.2"/>')

    y = 216
    for label, value in ROWS:
        parts.append(f'<text x="32" y="{y}" font-family="{MONO}" font-size="13" fill="{label_col}">{label}</text>')
        parts.append(f'<text x="272" y="{y}" font-family="{MONO}" font-size="13" fill="{text_main}">{value}</text>')
        y += 30

    parts.append(f'<line x1="32" y1="{y+2}" x2="{W-32}" y2="{y+2}" stroke="{accent}" stroke-opacity="0.2"/>')
    y += 36

    parts.append(f'<text x="32" y="{y}" font-family="{MONO}" font-size="13" fill="{label_col}">CONTACT</text>')
    y += 28
    for label, value in CONTACT:
        parts.append(f'<text x="52" y="{y}" font-family="{MONO}" font-size="13" fill="{text_dim}">{label}</text>')
        parts.append(f'<text x="272" y="{y}" font-family="{MONO}" font-size="13" fill="{text_main}">{value}</text>')
        y += 28

    parts.append(f'<text x="32" y="{H-30}" font-family="{MONO}" font-size="12" fill="{text_dim}"># tek basina kurup, tek basina idame ettiriyor.</text>')

    parts.append("</g>")
    parts.append("</svg>")
    return "\n".join(parts)


if __name__ == "__main__":
    import pathlib

    out = pathlib.Path(__file__).resolve().parent.parent
    (out / "dark.svg").write_text(build("dark"), encoding="utf-8")
    (out / "light.svg").write_text(build("light"), encoding="utf-8")
    print("wrote dark.svg / light.svg")
