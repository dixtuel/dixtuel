#!/usr/bin/env python3
"""Generates dark.svg / light.svg — a terminal-style identity card, structurally
matching the reference card (titlebar, VISUAL.MAP image panel, SYSTEM.INFO typed
panel, scan sweep, reveal animation) but themed red/black and filled with real,
verified facts about dixtuel. VISUAL.MAP embeds the real GitHub avatar (base64,
self-contained) as a red/black duotone, with an animated scan bar sweeping over it."""
import base64
import pathlib

W, H = 1180, 610
MONO = "'Courier New', Consolas, monospace"

ASSET_DIR = pathlib.Path(__file__).resolve().parent / "assets"
AVATAR_B64 = base64.b64encode((ASSET_DIR / "avatar.png").read_bytes()).decode()

IMX, IMY, IMW, IMH = 48, 50, 420, 420

INFO_LINES = [
    ("head", None, "dixtuel@vds"),
    ("kv", "Subject", "dixtuel"),
    ("kv", "Role", "Full-Stack & AI Systems Developer"),
    ("kv", "Origin", "Turkiye"),
    ("kv", "Status", "Building - Shipping - Self-hosting"),
    ("kv", "ToolChain", "Docker, Git, Caddy, systemd"),
    ("blank", None, None),
    ("kv2", "Core.Lang", "Python, TypeScript, JavaScript, Bash"),
    ("kv2", "Core.Frontend", "Next.js, React, Tailwind CSS"),
    ("kv2", "Core.Backend", "FastAPI, Flask, Node.js/Express"),
    ("kv2", "Core.Database", "PostgreSQL, Redis, SQLite, Prisma"),
    ("kv2", "Core.Infra", "Docker, Caddy, Cloudflare, Linux"),
    ("blank", None, None),
    ("accent", None, "- Contact"),
    ("kv2", "Grid.Mail", "asrinklcc@dxtl.com.tr"),
    ("kv2", "Grid.Portfolio", "dxtl.com.tr"),
    ("kv2", "Grid.Github", "dixtuel"),
    ("blank", None, None),
    ("accent", None, "- Focus"),
    ("kv", "Now", "PulseRoute, Commit Gunlugu, Mikoshi AI"),
]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(theme):
    dark = theme == "dark"
    bg0 = "#05050a" if dark else "#faf6f5"
    bg1 = "#180506" if dark else "#f3e3e3"
    titlebar_bg = "#0f0a0a" if dark else "#efe4e4"
    panel_bg = "#0f0a0a" if dark else "#ffffff"
    panel_op = "0.45" if dark else "0.6"
    ascii_dim = "#5a2a2a" if dark else "#c7a3a3"
    key_col = "#C23B3B"
    value_col = "#f0d9d9" if dark else "#241414"
    cc_col = "#6b4a4a" if dark else "#b98f8f"
    head_col = "#ff6b5b"
    accent_col = "#D9A441"
    term_label = "#8a6a6a"
    scan_label = "#ff6b5b"
    panel_title = "#c97a7a"
    scanline_col = "#ff9d8a"

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    parts.append("<defs>")
    parts.append(
        '<filter id="duotone" color-interpolation-filters="sRGB">'
        '<feColorMatrix type="matrix" values="0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0  0.33 0.33 0.33 0 0  0 0 0 1 0"/>'
        '<feComponentTransfer>'
        '<feFuncR type="table" tableValues="0.04 1.0"/>'
        '<feFuncG type="table" tableValues="0.04 0.42"/>'
        '<feFuncB type="table" tableValues="0.06 0.36"/>'
        "</feComponentTransfer>"
        "</filter>"
    )
    parts.append(f'<clipPath id="imgClip"><rect x="{IMX}" y="{IMY}" width="{IMW}" height="{IMH}" rx="12"/></clipPath>')
    parts.append(
        '<linearGradient id="scanGrad2" x1="0%" y1="0%" x2="0%" y2="100%">'
        '<stop offset="0%" stop-color="#ffd9d0" stop-opacity="0"/>'
        '<stop offset="45%" stop-color="#ffd9d0" stop-opacity="0.1"/>'
        '<stop offset="50%" stop-color="#fff0ec" stop-opacity="0.9"/>'
        '<stop offset="55%" stop-color="#ffd9d0" stop-opacity="0.1"/>'
        '<stop offset="100%" stop-color="#ff6b5b" stop-opacity="0"/>'
        "</linearGradient>"
    )
    parts.append(
        '<linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">'
        '<stop offset="0%" stop-color="#8B0000"/><stop offset="50%" stop-color="#C23B3B"/><stop offset="100%" stop-color="#3d0a0a"/>'
        "</linearGradient>"
    )
    parts.append(f'<radialGradient id="bgGlow" cx="30%" cy="20%" r="80%"><stop offset="0%" stop-color="{bg1}"/><stop offset="100%" stop-color="{bg0}"/></radialGradient>')
    parts.append(
        '<linearGradient id="scanGrad" x1="0%" y1="0%" x2="0%" y2="100%">'
        f'<stop offset="0%" stop-color="{scanline_col}" stop-opacity="0"/>'
        f'<stop offset="45%" stop-color="{scanline_col}" stop-opacity="0.05"/>'
        f'<stop offset="50%" stop-color="#ffd9d0" stop-opacity="0.55"/>'
        f'<stop offset="55%" stop-color="{scanline_col}" stop-opacity="0.05"/>'
        f'<stop offset="100%" stop-color="#8B0000" stop-opacity="0"/>'
        "</linearGradient>"
    )
    parts.append(f'<pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="{scanline_col}" opacity="0.045"/></pattern>')
    parts.append(f'<mask id="revealMask" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H+10}">'
                 f'<rect x="0" y="0" width="{W}" height="0" fill="#fff">'
                 f'<animate attributeName="height" from="0" to="560" dur="2.6s" begin="0.2s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>'
                 "</rect></mask>")

    clip_defs = []
    begin = 0.75
    for i in range(len(INFO_LINES)):
        y = 26.0 + i * 22
        clip_defs.append(
            f'<clipPath id="lc{i}"><rect x="500" y="{y:.2f}" width="0" height="24">'
            f'<animate attributeName="width" from="0" to="640" dur="0.38s" begin="{begin:.2f}s" fill="freeze"/>'
            "</rect></clipPath>"
        )
        begin += 0.115
    parts.append("".join(clip_defs))

    parts.append(
        f"""<style>
    .key    {{ font-family: {MONO}; font-size: 14px; fill: {key_col}; font-weight: bold; }}
    .value  {{ font-family: {MONO}; font-size: 14px; fill: {value_col}; }}
    .cc     {{ font-family: {MONO}; font-size: 14px; fill: {cc_col}; }}
    .head   {{ font-family: {MONO}; font-size: 16px; fill: {head_col}; font-weight: bold; }}
    .accent {{ font-family: {MONO}; font-size: 14px; fill: {accent_col}; font-weight: bold; }}
    text, tspan {{ white-space: pre; }}
    .term-label {{ font-family: {MONO}; font-size: 12px; fill: {term_label}; letter-spacing: 0.5px; }}
    .scan-label {{ font-family: {MONO}; font-size: 10px; fill: {scan_label}; letter-spacing: 1px; }}
    .panel-title {{ font-family: {MONO}; font-size: 11px; fill: {panel_title}; letter-spacing: 2px; opacity: 0.7; }}
    .cursor-blink {{ fill: {head_col}; }}
  </style>
</defs>
"""
    )

    parts.append(f'<rect width="{W}" height="{H}" rx="18" fill="url(#bgGlow)"/>')
    parts.append(f'<rect width="{W}" height="{H}" rx="18" fill="url(#scanlines)"/>')

    parts.append('<g id="titlebar">')
    parts.append(f'<rect x="3" y="3" width="{W-6}" height="34" rx="16" fill="{titlebar_bg}" fill-opacity="0.85"/>')
    parts.append('<circle cx="24" cy="20" r="5" fill="#EF4444"><animate attributeName="opacity" values="1;0.55;1" dur="4s" repeatCount="indefinite"/></circle>')
    parts.append('<circle cx="42" cy="20" r="5" fill="#F59E0B"><animate attributeName="opacity" values="1;0.55;1" dur="4s" begin="0.3s" repeatCount="indefinite"/></circle>')
    parts.append('<circle cx="60" cy="20" r="5" fill="#10B981"><animate attributeName="opacity" values="1;0.55;1" dur="4s" begin="0.6s" repeatCount="indefinite"/></circle>')
    parts.append(f'<text x="{W//2}" y="25" text-anchor="middle" class="term-label">dixtuel@vds ~ % ./profile.sh --live</text>')
    parts.append(f'<circle cx="{W-58}" cy="20" r="4" fill="{scan_label}"><animate attributeName="opacity" values="1;0.15;1" dur="1.1s" repeatCount="indefinite"/></circle>')
    parts.append(f'<text x="{W-48}" y="24" class="scan-label">SCANNING</text>')
    parts.append("</g>")

    parts.append('<g transform="translate(0,38)">')
    parts.append(f'<rect x="14" y="26" width="488" height="468" rx="14" fill="{panel_bg}" fill-opacity="{panel_op}" stroke="url(#borderGrad)" stroke-width="1" opacity="0.35"/>')
    parts.append(f'<rect x="508" y="10" width="655" height="500" rx="14" fill="{panel_bg}" fill-opacity="{panel_op}" stroke="url(#borderGrad)" stroke-width="1" opacity="0.35"/>')
    parts.append('<text x="30" y="24" class="panel-title">VISUAL.MAP</text>')
    parts.append('<text x="524" y="24" class="panel-title">SYSTEM.INFO</text>')

    parts.append('<g mask="url(#revealMask)">')
    parts.append(
        f'<image href="data:image/png;base64,{AVATAR_B64}" x="{IMX}" y="{IMY}" width="{IMW}" height="{IMH}" '
        f'clip-path="url(#imgClip)" filter="url(#duotone)" preserveAspectRatio="xMidYMid slice"/>'
    )
    parts.append(f'<rect x="{IMX}" y="{IMY}" width="{IMW}" height="{IMH}" rx="12" fill="none" stroke="url(#borderGrad)" stroke-width="1.5" opacity="0.55"/>')
    parts.append(
        f'<rect x="{IMX}" y="{IMY-60}" width="{IMW}" height="60" fill="url(#scanGrad2)" clip-path="url(#imgClip)" style="mix-blend-mode:screen">'
        f'<animateTransform attributeName="transform" type="translate" from="0 0" to="0 {IMH+60}" dur="2.6s" repeatCount="indefinite"/>'
        "</rect>"
    )
    parts.append("</g>")

    for i, (kind, key, val) in enumerate(INFO_LINES):
        y = 42.0 + i * 22
        seg = [f'<g clip-path="url(#lc{i})"><text x="520" y="0" fill="{value_col}">']
        if kind == "head":
            seg.append(f'<tspan x="520" y="{y:.2f}" class="head">{esc(val)}</tspan>')
            seg.append('<tspan class="cc"> -&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-&#8212;-</tspan>')
        elif kind == "kv":
            dots = "." * max(3, 26 - len(key))
            seg.append(f'<tspan x="520" y="{y:.2f}" class="cc">. </tspan><tspan class="key">{esc(key)}</tspan><tspan class="cc">: {dots} </tspan><tspan class="value">{esc(val)}</tspan>')
        elif kind == "kv2":
            k1, k2 = key.split(".", 1)
            dots = "." * max(3, 22 - len(k2))
            seg.append(f'<tspan x="520" y="{y:.2f}" class="cc">. </tspan><tspan class="key">{k1}</tspan><tspan class="cc">.</tspan><tspan class="key">{k2}</tspan><tspan class="cc">: {dots} </tspan><tspan class="value">{esc(val)}</tspan>')
        elif kind == "accent":
            seg.append(f'<tspan x="520" y="{y:.2f}" class="accent">{esc(val)}</tspan>')
            seg.append('<tspan class="cc"> -&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-&#8212;-</tspan>')
        else:
            seg.append(f'<tspan x="520" y="{y:.2f}" class="cc">. </tspan>')
        seg.append("</text></g>")
        parts.append("".join(seg))

    cursor_y = 42.0 + (len(INFO_LINES) - 1) * 22 - 15
    parts.append(f'<rect x="522" y="{cursor_y:.1f}" width="9" height="16" class="cursor-blink" opacity="0">')
    parts.append(f'<animate attributeName="opacity" values="0;0;1;0;1;0;1;0" keyTimes="0;0.01;0.02;0.3;0.5;0.7;0.85;1" dur="1.4s" begin="{begin+0.5:.2f}s" repeatCount="indefinite"/>')
    parts.append("</rect>")

    parts.append("</g>")

    parts.append(f'<rect x="0" y="-70" width="{W}" height="70" fill="url(#scanGrad)" opacity="0.6" style="mix-blend-mode:screen">')
    parts.append(f'<animateTransform attributeName="transform" type="translate" from="0 -70" to="0 {H+70}" dur="4.2s" repeatCount="indefinite"/>')
    parts.append("</rect>")

    parts.append(f'<rect x="3" y="3" width="{W-6}" height="{H-6}" rx="16" fill="none" stroke="url(#borderGrad)" stroke-width="2" opacity="0.8">')
    parts.append('<animate attributeName="opacity" values="0.5;0.95;0.5" dur="3.2s" repeatCount="indefinite"/>')
    parts.append("</rect>")

    parts.append("</svg>")
    return "\n".join(parts)


if __name__ == "__main__":
    out = pathlib.Path(__file__).resolve().parent.parent
    (out / "dark.svg").write_text(build("dark"), encoding="utf-8")
    (out / "light.svg").write_text(build("light"), encoding="utf-8")
    print("wrote dark.svg / light.svg")
