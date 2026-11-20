#!/usr/bin/env python3
"""Build the animated, self-contained SVG assets for the GitHub profile README.

GitHub renders README SVGs through <img>, which blocks external resources, so
fonts (woff2) and tech icons are embedded inline. Animations use CSS + SMIL only.

Usage:
    python3 scripts/build_assets.py <cache_dir>

<cache_dir> must contain:
    fonts/orbitron.woff2, fonts/sharetech.woff2      (Google Fonts, OFL)
    icons/<id>.svg                                   (https://skillicons.dev/icons?i=<id>)
    icons/si-linkedin.svg, icons/si-github.svg       (simple-icons@9.0.0)
Outputs go to ./assets/.
"""
import base64
import math
import os
import random
import re
import sys
from xml.sax.saxutils import escape

CACHE = sys.argv[1]
OUT = "assets"
random.seed(7)

# ───────────────────────────── palette ─────────────────────────────
BG0, BG1 = "#04050E", "#0A0F2A"
CYAN, MAGENTA, VIOLET, AMBER = "#00F0FF", "#FF2BD6", "#8B5CF6", "#FFB547"
TEXT, MUTED, LINE = "#E6F1FF", "#7F8CC0", "#1E2A5A"

ORB = "'Orbitron',sans-serif"
MONO = "'ShareTech',ui-monospace,Menlo,monospace"


def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


FONT_CSS = (
    "@font-face{font-family:'Orbitron';font-weight:400 900;"
    f"src:url(data:font/woff2;base64,{b64(os.path.join(CACHE, 'fonts/orbitron.woff2'))}) format('woff2');}}"
    "@font-face{font-family:'ShareTech';"
    f"src:url(data:font/woff2;base64,{b64(os.path.join(CACHE, 'fonts/sharetech.woff2'))}) format('woff2');}}"
)


def svg(w, h, body, css="", label="", defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}">\n'
            f'<style>{FONT_CSS}{css}</style>\n<defs>{defs}</defs>\n{body}\n</svg>\n')


def write(name, content):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(content)
    print(f"  {name:28s} {len(content) / 1024:6.1f} KB")


def panel(w, h, rid="pb"):
    """Dark rounded panel with a gradient border + HUD corner brackets."""
    defs = (f'<linearGradient id="{rid}" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{CYAN}"/><stop offset=".5" stop-color="{VIOLET}"/>'
            f'<stop offset="1" stop-color="{MAGENTA}"/></linearGradient>'
            f'<radialGradient id="{rid}g" cx=".5" cy="0" r="1">'
            f'<stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG0}"/></radialGradient>')
    body = (f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="16" fill="url(#{rid}g)"/>'
            f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="16" fill="none" stroke="url(#{rid})" stroke-opacity=".55"/>')
    L = 18
    for cx, cy, sx, sy in ((10, 10, 1, 1), (w - 10, 10, -1, 1), (10, h - 10, 1, -1), (w - 10, h - 10, -1, -1)):
        body += (f'<path d="M{cx} {cy + sy * L}V{cy}H{cx + sx * L}" fill="none" stroke="{CYAN}" '
                 f'stroke-width="2" class="brk"/>')
    return defs, body


BASE_CSS = (".brk{animation:brk 3s ease-in-out infinite}"
            "@keyframes brk{0%,100%{opacity:.9}50%{opacity:.3}}")


# ───────────────────────────── icons ─────────────────────────────
def icon_symbol(name, sid):
    """Turn a skillicons SVG into a <symbol>, namespacing its internal ids."""
    raw = open(os.path.join(CACHE, "icons", f"{name}.svg")).read()
    m = re.search(r'<svg[^>]*width="256"[^>]*>(.*?)</svg>', raw, re.S)
    inner = m.group(1)
    for old in set(re.findall(r'id="([^"]+)"', inner)):
        inner = re.sub(rf'(?<=["#(]){re.escape(old)}(?=["\)])', f"{sid}-{old}", inner)
    return f'<symbol id="{sid}" viewBox="0 0 256 256">{inner}</symbol>'


def ballerina_symbol(sid):
    raw = open(os.path.join(OUT, "ballerina.svg")).read()
    inner = re.search(r"<svg[^>]*>(.*)</svg>", raw, re.S).group(1)
    return f'<symbol id="{sid}" viewBox="0 0 256 256">{inner}</symbol>'


def simple_icon_path(name):
    raw = open(os.path.join(CACHE, "icons", f"si-{name}.svg")).read()
    return re.search(r'<path d="([^"]+)"', raw).group(1)


# ═════════════════════════════ HERO ═════════════════════════════
def build_hero():
    W, H, HZ = 880, 380, 262
    defs, body = panel(W, H, "hb")
    css = BASE_CSS + (
        ".tw{animation:tw 3.2s ease-in-out infinite}"
        "@keyframes tw{0%,100%{opacity:.15}50%{opacity:1}}"
        ".gl{animation:gl 5s steps(1) infinite}.gl.b{animation-name:gl2}"
        "@keyframes gl{0%,86%,100%{opacity:0;transform:translate(0,0)}87%{opacity:.85;transform:translate(-5px,1px)}"
        "89%{opacity:.85;transform:translate(4px,-2px)}91%{opacity:0}95%{opacity:.7;transform:translate(-2px,0)}96%{opacity:0}}"
        "@keyframes gl2{0%,86%,100%{opacity:0;transform:translate(0,0)}87%{opacity:.85;transform:translate(5px,-1px)}"
        "89%{opacity:.85;transform:translate(-4px,2px)}91%{opacity:0}95%{opacity:.7;transform:translate(3px,0)}96%{opacity:0}}"
        ".main{animation:jit 5s steps(1) infinite}"
        "@keyframes jit{0%,86%,100%{transform:translate(0,0)}87%{transform:translate(2px,0) skewX(-6deg)}"
        "89%{transform:translate(-2px,0)}91%{transform:none}}"
        ".blink{animation:bl 1.1s steps(1) infinite}@keyframes bl{0%{opacity:1}50%{opacity:0}}"
        ".spin{transform-box:view-box;transform-origin:735px 150px;animation:sp 24s linear infinite}"
        ".spin.r{animation-duration:16s;animation-direction:reverse}.spin.s{animation-duration:9s}"
        "@keyframes sp{to{transform:rotate(360deg)}}"
        ".pulse{transform-box:fill-box;transform-origin:center;animation:pu 2.6s ease-in-out infinite}"
        "@keyframes pu{0%,100%{transform:scale(1);opacity:.9}50%{transform:scale(1.08);opacity:.55}}"
        ".scan{animation:sc 6s linear infinite}@keyframes sc{from{transform:translateY(-60px)}to{transform:translateY(400px)}}"
    )
    defs += (
        f'<linearGradient id="ng" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="520" y2="0" spreadMethod="repeat">'
        f'<stop offset="0" stop-color="{CYAN}"/><stop offset=".35" stop-color="{VIOLET}"/>'
        f'<stop offset=".65" stop-color="{MAGENTA}"/><stop offset="1" stop-color="{CYAN}"/>'
        f'<animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="520 0" dur="7s" repeatCount="indefinite"/>'
        f'</linearGradient>'
        f'<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BG0}"/>'
        f'<stop offset="1" stop-color="{BG0}" stop-opacity="0"/></linearGradient>'
        f'<linearGradient id="hz" x1="0" x2="1"><stop offset="0" stop-color="{MAGENTA}" stop-opacity="0"/>'
        f'<stop offset=".5" stop-color="{MAGENTA}"/><stop offset="1" stop-color="{MAGENTA}" stop-opacity="0"/></linearGradient>'
        f'<linearGradient id="scg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/>'
        f'<stop offset=".5" stop-color="{CYAN}" stop-opacity=".10"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></linearGradient>'
        f'<radialGradient id="sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{VIOLET}" stop-opacity=".55"/>'
        f'<stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>'
        f'<clipPath id="card"><rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="15"/></clipPath>'
        f'<clipPath id="floor"><rect x="0" y="{HZ}" width="{W}" height="{H - HZ}"/></clipPath>'
        f'<filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3" result="b"/>'
        f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
    )
    g = ['<g clip-path="url(#card)">']
    # stars
    for _ in range(80):
        x, y = random.uniform(10, W - 10), random.uniform(10, HZ - 10)
        r = random.choice([0.6, 0.8, 1, 1.3])
        c = random.choice([TEXT, TEXT, CYAN, MAGENTA])
        g.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{c}" class="tw" '
                 f'style="animation-delay:-{random.uniform(0, 3.2):.2f}s"/>')
    # glow behind emblem
    g.append(f'<circle cx="735" cy="150" r="150" fill="url(#sun)"/>')
    # synthwave floor
    g.append('<g clip-path="url(#floor)">')
    vp = 440
    for j in range(-14, 15):
        g.append(f'<line x1="{vp}" y1="{HZ}" x2="{vp + j * 80}" y2="{H + 40}" stroke="{MAGENTA}" stroke-opacity=".45"/>')
    N, P, ZF, ZN = 9, 3.2, 9.0, 0.9
    for i in range(N):
        vals = []
        for s in range(25):
            u = s / 24
            z = ZF - (ZF - ZN) * u
            vals.append(f"{HZ + (H - HZ + 10) / z:.1f}")
        v = ";".join(vals)
        g.append(f'<line x1="0" x2="{W}" y1="{HZ}" y2="{HZ}" stroke="{MAGENTA}" stroke-opacity=".6">'
                 f'<animate attributeName="y1" values="{v}" dur="{P}s" begin="-{P * i / N:.2f}s" repeatCount="indefinite"/>'
                 f'<animate attributeName="y2" values="{v}" dur="{P}s" begin="-{P * i / N:.2f}s" repeatCount="indefinite"/></line>')
    g.append(f'<rect x="0" y="{HZ}" width="{W}" height="46" fill="url(#fade)"/></g>')
    g.append(f'<rect x="0" y="{HZ - 1}" width="{W}" height="2" fill="url(#hz)" filter="url(#glow)"/>')

    # emblem (HUD reticle)
    cx, cy = 735, 150
    em = [f'<g class="spin"><circle cx="{cx}" cy="{cy}" r="104" fill="none" stroke="{CYAN}" stroke-opacity=".35" stroke-dasharray="2 7"/>']
    for a in range(0, 360, 30):
        x1, y1 = cx + 96 * math.cos(math.radians(a)), cy + 96 * math.sin(math.radians(a))
        x2, y2 = cx + 104 * math.cos(math.radians(a)), cy + 104 * math.sin(math.radians(a))
        em.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{CYAN}" stroke-width="2"/>')
    em.append("</g>")
    r2 = 84
    arc = lambda a0, a1, r: (f"M{cx + r * math.cos(math.radians(a0)):.1f} {cy + r * math.sin(math.radians(a0)):.1f}"
                             f"A{r} {r} 0 0 1 {cx + r * math.cos(math.radians(a1)):.1f} {cy + r * math.sin(math.radians(a1)):.1f}")
    em.append(f'<g class="spin r" filter="url(#glow)">' + "".join(
        f'<path d="{arc(a, a + 70, r2)}" fill="none" stroke="{MAGENTA}" stroke-width="3" stroke-linecap="round"/>'
        for a in (0, 120, 240)) + "</g>")
    em.append(f'<g class="spin s">' + "".join(
        f'<path d="{arc(a, a + 25, 66)}" fill="none" stroke="{AMBER}" stroke-width="2"/>' for a in (0, 90, 180, 270)) + "</g>")
    hexp = " ".join(f"{cx + 50 * math.cos(math.radians(a + 30)):.1f},{cy + 50 * math.sin(math.radians(a + 30)):.1f}"
                    for a in range(0, 360, 60))
    em.append(f'<polygon points="{hexp}" fill="{BG1}" fill-opacity=".85" stroke="{CYAN}" stroke-width="1.5" class="pulse"/>')
    em.append(f'<text x="{cx}" y="{cy + 13}" text-anchor="middle" font-family="{ORB}" font-weight="900" font-size="36" '
              f'fill="url(#ng)" filter="url(#glow)">PF</text>')
    em.append(f'<path d="M{cx - 128} {cy}h18M{cx + 110} {cy}h18M{cx} {cy - 128}v18M{cx} {cy + 110}v18" stroke="{CYAN}" stroke-opacity=".6"/>')
    em.append(f'<circle r="4" fill="{AMBER}" filter="url(#glow)"><animateMotion dur="5s" repeatCount="indefinite" '
              f'path="M{cx + 120} {cy}a120 120 0 1 1 -240 0a120 120 0 1 1 240 0"/></circle>')
    g += em

    # left text block
    x0 = 48
    g.append(f'<text x="{x0}" y="64" font-family="{MONO}" font-size="14" fill="{CYAN}" letter-spacing="2">'
             f'<tspan class="blink">▌</tspan> IDENTITY // VERIFIED</text>')
    for word, y in (("PASINDU", 126), ("FERNANDO", 184)):
        common = f'x="{x0}" y="{y}" font-family="{ORB}" font-weight="900" font-size="50" letter-spacing="3"'
        g.append(f'<text {common} fill="{CYAN}" class="gl">{word}</text>')
        g.append(f'<text {common} fill="{MAGENTA}" class="gl b">{word}</text>')
        g.append(f'<text {common} fill="url(#ng)" class="main" filter="url(#glow)">{word}</text>')

    # rotating, typed role line
    roles = ["Software Engineer @ Choreo Labs",
             "Building the Ballerina Language Server",
             "Researching live VM migration · KVM/QEMU",
             "Backend systems · Developer tooling"]
    T, slot, cps, CW, ry = 16.0, 4.0, 24, 9.18, 226   # CW: measured ShareTech advance at 17px
    px = x0 + 2 * CW
    g.append(f'<text x="{x0}" y="{ry}" font-family="{MONO}" font-size="17" fill="{AMBER}">&gt;</text>')
    for i, role in enumerate(roles):
        n = len(role)
        t0 = i * slot
        ks, ws = ["0"], ["0"]
        for c in range(n + 1):
            ks.append(f"{(t0 + 0.15 + c / cps) / T:.4f}")
            ws.append(f"{c * CW:.1f}")
        ks.append(f"{(t0 + slot - 0.25) / T:.4f}")
        ws.append("0")
        kt, wv = ";".join(ks), ";".join(ws)
        cid = f"rc{i}"
        defs += (f'<clipPath id="{cid}"><rect x="{px}" y="{ry - 17}" width="0" height="24">'
                 f'<animate attributeName="width" values="{wv}" keyTimes="{kt}" calcMode="discrete" dur="{T}s" repeatCount="indefinite"/>'
                 f'</rect></clipPath>')
        # textLength pins the rendered width to n*CW so the clip/cursor stay in sync in every browser
        g.append(f'<text x="{px}" y="{ry}" font-family="{MONO}" font-size="17" fill="{TEXT}" clip-path="url(#{cid})" '
                 f'textLength="{n * CW:.1f}" lengthAdjust="spacingAndGlyphs">{escape(role)}</text>')
        xs = ";".join(f"{px + float(w) + 2:.1f}" for w in ws)
        op = ";".join(["0"] + ["1"] * (n + 1) + ["0"])
        g.append(f'<rect x="{px}" y="{ry - 15}" width="9" height="19" fill="{CYAN}" opacity="0">'
                 f'<animate attributeName="x" values="{xs}" keyTimes="{kt}" calcMode="discrete" dur="{T}s" repeatCount="indefinite"/>'
                 f'<animate attributeName="opacity" values="{op}" keyTimes="{kt}" calcMode="discrete" dur="{T}s" repeatCount="indefinite"/></rect>')

    # chips
    cxp = x0
    for txt, col in (("UCSC · BSc (Hons) CS", CYAN), ("GPA 3.98 / 4.00", AMBER), ("STATUS: BUILDING", MAGENTA)):
        w = len(txt) * 7.2 + 34
        dot = f'<circle cx="{cxp + 13}" cy="{H - 50}" r="3.5" fill="{col}" class="blink"/>' if "STATUS" in txt else \
              f'<rect x="{cxp + 10}" y="{H - 53.5}" width="7" height="7" fill="{col}" transform="rotate(45 {cxp + 13.5} {H - 50})"/>'
        g.append(f'<rect x="{cxp}" y="{H - 64}" width="{w:.0f}" height="28" rx="6" fill="{BG0}" fill-opacity=".85" '
                 f'stroke="{col}" stroke-opacity=".7"/>{dot}'
                 f'<text x="{cxp + 25}" y="{H - 45}" font-family="{MONO}" font-size="13" fill="{TEXT}" letter-spacing=".5">{escape(txt)}</text>')
        cxp += w + 10

    # scanline + crt texture
    g.append(f'<rect class="scan" x="0" y="0" width="{W}" height="60" fill="url(#scg)"/>')
    defs += (f'<pattern id="crt" width="4" height="4" patternUnits="userSpaceOnUse">'
             f'<rect width="4" height="1" fill="#fff" fill-opacity=".025"/></pattern>')
    g.append(f'<rect width="{W}" height="{H}" fill="url(#crt)"/>')
    g.append("</g>")
    write("hero.svg", svg(W, H, body + "".join(g), css,
                          "Pasindu Fernando — Software Engineer at Choreo Labs", defs))


# ═════════════════════════════ DIVIDER ═════════════════════════════
def build_divider(num, title, fname):
    W, H = 880, 58
    css = (".blink{animation:bl 1.1s steps(1) infinite}@keyframes bl{0%{opacity:1}50%{opacity:0}}")
    lx = 78 + len(title) * 17.5 + 24   # Orbitron 18px + 3px tracking
    defs = (f'<linearGradient id="ln" gradientUnits="userSpaceOnUse" x1="{lx}" y1="0" x2="{W - 60}" y2="0"><stop offset="0" stop-color="{CYAN}"/>'
            f'<stop offset="1" stop-color="{MAGENTA}" stop-opacity="0"/></linearGradient>'
            f'<filter id="glow" x="-50%" y="-200%" width="200%" height="500%"><feGaussianBlur stdDeviation="2.5" result="b"/>'
            f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    body = (f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="12" fill="{BG0}" stroke="{LINE}"/>'
            f'<text x="24" y="37" font-family="{MONO}" font-size="16" fill="{MAGENTA}">{num}</text>'
            f'<text x="52" y="37" font-family="{MONO}" font-size="16" fill="{MUTED}">//</text>'
            f'<text x="78" y="37" font-family="{ORB}" font-weight="700" font-size="18" letter-spacing="3" fill="{TEXT}" filter="url(#glow)">{escape(title)}</text>'
            f'<line x1="{lx}" y1="30" x2="{W - 60}" y2="30" stroke="url(#ln)" stroke-opacity=".6"/>'
            f'<rect x="{lx}" y="28" width="70" height="4" rx="2" fill="{CYAN}" filter="url(#glow)">'
            f'<animate attributeName="x" values="{lx};{W - 130}" dur="3.2s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.8;1" dur="3.2s" repeatCount="indefinite"/></rect>'
            f'<rect x="{W - 44}" y="22" width="16" height="16" fill="none" stroke="{CYAN}" transform="rotate(45 {W - 36} 30)"/>'
            f'<rect x="{W - 40}" y="26" width="8" height="8" fill="{MAGENTA}" class="blink" transform="rotate(45 {W - 36} 30)"/>')
    write(fname, svg(W, H, body, css, f"{num} {title}", defs))


# ═════════════════════════════ TIMELINE ═════════════════════════════
def build_timeline():
    W, H = 880, 300
    defs, body = panel(W, H, "tb")
    css = BASE_CSS + (
        ".ring{transform-box:fill-box;transform-origin:center;animation:rg 2.4s ease-out infinite}"
        "@keyframes rg{0%{transform:scale(.6);opacity:.9}100%{transform:scale(1.7);opacity:0}}"
        ".blink{animation:bl 1.1s steps(1) infinite}@keyframes bl{0%{opacity:1}50%{opacity:0}}"
        ".hexs{transform-box:fill-box;transform-origin:center;animation:sp 12s linear infinite}"
        "@keyframes sp{to{transform:rotate(360deg)}}"
        ".in{opacity:0;animation:in 1s ease-out forwards}"
        "@keyframes in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}"
    )
    defs += (f'<linearGradient id="tl" gradientUnits="userSpaceOnUse" x1="150" y1="0" x2="730" y2="0"><stop offset="0" stop-color="{CYAN}"/>'
             f'<stop offset=".5" stop-color="{VIOLET}"/><stop offset="1" stop-color="{MAGENTA}"/></linearGradient>'
             f'<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/>'
             f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    nodes = [
        (150, CYAN, "01", "UCSC", ["BSc (Hons) Computer Science", "GPA 3.98 / 4.00 · Top of batch"]),
        (440, VIOLET, "02", "RESEARCH", ["Fault-tolerant live VM migration", "KVM · QEMU · Checkpointing"]),
        (730, MAGENTA, "03", "CHOREO LABS", ["Software Engineer", "Ballerina LS · VS Code extension"]),
    ]
    y = 96
    g = [f'<text x="40" y="44" font-family="{MONO}" font-size="13" fill="{MUTED}" letter-spacing="2">MISSION LOG · TRAJECTORY</text>',
         f'<line x1="150" y1="{y}" x2="730" y2="{y}" stroke="url(#tl)" stroke-width="2" stroke-opacity=".7"/>']
    for k in range(3):
        g.append(f'<circle r="4.5" fill="#fff" filter="url(#glow)"><animateMotion dur="3s" begin="{k}s" repeatCount="indefinite" '
                 f'path="M150 {y}H730"/><animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.9;1" dur="3s" begin="{k}s" repeatCount="indefinite"/></circle>')
    for i, (x, col, num, title, lines) in enumerate(nodes):
        hexp = lambda r: " ".join(f"{x + r * math.cos(math.radians(a)):.1f},{y + r * math.sin(math.radians(a)):.1f}" for a in range(0, 360, 60))
        g.append(f'<circle cx="{x}" cy="{y}" r="22" fill="none" stroke="{col}" stroke-width="2" class="ring" style="animation-delay:{i * .8}s"/>')
        g.append(f'<polygon points="{hexp(30)}" fill="none" stroke="{col}" stroke-opacity=".5" stroke-dasharray="4 4" class="hexs"/>')
        g.append(f'<polygon points="{hexp(21)}" fill="{BG0}" stroke="{col}" stroke-width="2" filter="url(#glow)"/>')
        g.append(f'<text x="{x}" y="{y + 6}" text-anchor="middle" font-family="{ORB}" font-weight="700" font-size="15" fill="{TEXT}">{num}</text>')
        d = f"animation-delay:{0.3 + i * 0.45:.2f}s"
        blk = [f'<text x="{x}" y="{y + 66}" text-anchor="middle" font-family="{ORB}" font-weight="700" font-size="17" '
               f'letter-spacing="2" fill="{col}" filter="url(#glow)">{title}</text>']
        for j, ln in enumerate(lines):
            blk.append(f'<text x="{x}" y="{y + 96 + j * 22}" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{TEXT if j == 0 else MUTED}">{escape(ln)}</text>')
        g.append(f'<g class="in" style="{d}">{"".join(blk)}</g>')
    # NOW tag on last node
    g.append(f'<g><rect x="760" y="{y - 40}" width="52" height="20" rx="4" fill="{MAGENTA}" fill-opacity=".15" stroke="{MAGENTA}"/>'
             f'<circle cx="771" cy="{y - 30}" r="3" fill="{MAGENTA}" class="blink"/>'
             f'<text x="780" y="{y - 25.5}" font-family="{MONO}" font-size="12" fill="{MAGENTA}">NOW</text></g>')
    g.append(f'<line x1="40" y1="{H - 52}" x2="{W - 40}" y2="{H - 52}" stroke="{LINE}"/>')
    g.append(f'<text x="{W / 2}" y="{H - 24}" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{MUTED}" letter-spacing="1">'
             f'<tspan fill="{AMBER}">OFF-DUTY ▸</tspan> Tennis · Carrom · Volunteering <tspan class="blink" fill="{CYAN}">_</tspan></text>')
    write("timeline.svg", svg(W, H, body + "".join(g), css,
                              "Mission log: UCSC BSc (Hons) CS, GPA 3.98; research on fault-tolerant live VM migration with KVM/QEMU; now Software Engineer at Choreo Labs", defs))


# ═════════════════════════════ ORBIT ═════════════════════════════
def build_orbit():
    W, H = 880, 600
    CX, CY = 440, 306
    defs, body = panel(W, H, "ob")
    css = BASE_CSS + (
        ".core{transform-box:fill-box;transform-origin:center;animation:pu 2.8s ease-in-out infinite}"
        "@keyframes pu{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.12);opacity:.7}}"
        ".dash{animation:da 20s linear infinite}@keyframes da{to{stroke-dashoffset:-400}}"
    )
    defs += (f'<radialGradient id="cg" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{CYAN}" stop-opacity=".9"/>'
             f'<stop offset=".35" stop-color="{VIOLET}" stop-opacity=".45"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>'
             f'<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/>'
             f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    rings = [
        (100, 30, 1, 50, CYAN, ["java", "ballerina", "c", "go"]),
        (172, 55, -1, 42, VIOLET, ["ts", "js", "kotlin", "python", "cpp", "php", "scala", "r"]),
        (244, 90, 1, 38, MAGENTA, ["spring", "nodejs", "express", "react", "tailwind", "docker",
                                   "postgres", "mysql", "mongodb", "git", "linux", "figma", "gradle"]),
    ]
    syms = {}
    for *_, ids in rings:
        for i in ids:
            if i not in syms:
                syms[i] = ballerina_symbol("i-ballerina") if i == "ballerina" else icon_symbol(i, f"i-{i}")
    defs += "".join(syms.values())
    g = []
    # background grid of dots
    for gx in range(40, W, 40):
        for gy in range(40, H, 40):
            if math.hypot(gx - CX, gy - CY) > 280:
                g.append(f'<circle cx="{gx}" cy="{gy}" r="1" fill="{LINE}"/>')
    # core
    g.append(f'<circle cx="{CX}" cy="{CY}" r="64" fill="url(#cg)" class="core"/>')
    hexp = " ".join(f"{CX + 34 * math.cos(math.radians(a + 30)):.1f},{CY + 34 * math.sin(math.radians(a + 30)):.1f}" for a in range(0, 360, 60))
    g.append(f'<polygon points="{hexp}" fill="{BG0}" stroke="{CYAN}" stroke-width="2" filter="url(#glow)">'
             f'<animateTransform attributeName="transform" type="rotate" from="0 {CX} {CY}" to="360 {CX} {CY}" dur="14s" repeatCount="indefinite"/></polygon>')
    g.append(f'<text x="{CX}" y="{CY - 1}" text-anchor="middle" font-family="{ORB}" font-weight="900" font-size="14" fill="{TEXT}">CORE</text>'
             f'<text x="{CX}" y="{CY + 14}" text-anchor="middle" font-family="{MONO}" font-size="10" fill="{CYAN}" letter-spacing="1">STACK</text>')
    for r, dur, direction, size, col, ids in rings:
        g.append(f'<circle cx="{CX}" cy="{CY}" r="{r}" fill="none" stroke="{col}" stroke-opacity=".35" stroke-dasharray="3 9" class="dash"/>')
        frm, to = (0, 360) if direction > 0 else (360, 0)
        items = []
        n = len(ids)
        for k, i in enumerate(ids):
            a = 2 * math.pi * k / n - math.pi / 2
            x, y = CX + r * math.cos(a), CY + r * math.sin(a)
            items.append(f'<g transform="translate({x:.1f} {y:.1f})"><g>'
                         f'<animateTransform attributeName="transform" type="rotate" from="{-frm}" to="{-to}" dur="{dur}s" repeatCount="indefinite"/>'
                         f'<circle r="{size / 2 + 5}" fill="{BG0}" stroke="{col}" stroke-opacity=".6"/>'
                         f'<use href="#i-{i}" xlink:href="#i-{i}" x="{-size / 2}" y="{-size / 2}" width="{size}" height="{size}"/></g></g>')
        g.append(f'<g><animateTransform attributeName="transform" type="rotate" from="{frm} {CX} {CY}" to="{to} {CX} {CY}" '
                 f'dur="{dur}s" repeatCount="indefinite"/>{"".join(items)}</g>')
    # legend
    leg = [("INNER", "Primary — Java · Ballerina · C · Go", CYAN),
           ("MID", "Languages", VIOLET),
           ("OUTER", "Frameworks · Data · Tools", MAGENTA)]
    for k, (a, b, col) in enumerate(leg):
        yy = 40 + k * 20
        g.append(f'<rect x="30" y="{yy - 9}" width="8" height="8" fill="{col}"/>'
                 f'<text x="46" y="{yy}" font-family="{MONO}" font-size="12" fill="{MUTED}"><tspan fill="{TEXT}">{a}</tspan>  {escape(b)}</text>')
    g.append(f'<text x="{W - 30}" y="40" text-anchor="end" font-family="{MONO}" font-size="12" fill="{MUTED}" letter-spacing="2">TECH ARSENAL · '
             f'{sum(len(r[-1]) for r in rings)} MODULES ONLINE</text>')
    write("orbit.svg", svg(W, H, body + "".join(g), css,
                           "Tech stack orbit. Primary: Java, Ballerina, C, Go. Languages: TypeScript, JavaScript, Kotlin, Python, C++, PHP, Scala, R. "
                           "Frameworks and tools: Spring, Node.js, Express, React, Tailwind, Docker, PostgreSQL, MySQL, MongoDB, Git, Linux, Figma, Gradle.", defs))


# ═════════════════════════════ DATA STREAM ═════════════════════════════
def build_stream():
    W, H = 880, 64
    items = ["Spring Cloud", "Gin", "Socket.io", "OpenAPI", "Language Server Protocol", "VS Code Extensions",
             "KVM", "QEMU", "Jetpack Compose", "Android Studio", "Maven", "Oracle", "Bootstrap", "Material UI",
             "jQuery", "Three.js", "HTML", "CSS", "Choreo", "Asgardeo", "Photoshop", "Canva", "GitHub", "VS Code"]
    cols = [CYAN, MAGENTA, VIOLET, AMBER]
    CW, PAD, GAP = 7.8, 30, 12
    chips, x = [], 0
    for k, t in enumerate(items):
        w = len(t) * CW + PAD
        c = cols[k % 4]
        chips.append(f'<rect x="{x:.1f}" y="18" width="{w:.1f}" height="28" rx="14" fill="{BG1}" stroke="{c}" stroke-opacity=".7"/>'
                     f'<circle cx="{x + 13:.1f}" cy="32" r="3" fill="{c}"/>'
                     f'<text x="{x + 22:.1f}" y="37" font-family="{MONO}" font-size="13" fill="{TEXT}">{escape(t)}</text>')
        x += w + GAP
    total = x
    css = (f".mq{{animation:mq {total / 40:.1f}s linear infinite}}@keyframes mq{{to{{transform:translateX(-{total:.1f}px)}}}}")
    defs = (f'<linearGradient id="ef" x1="0" x2="1"><stop offset="0" stop-color="{BG0}"/><stop offset=".07" stop-color="{BG0}" stop-opacity="0"/>'
            f'<stop offset=".93" stop-color="{BG0}" stop-opacity="0"/><stop offset="1" stop-color="{BG0}"/></linearGradient>'
            f'<clipPath id="cl"><rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="11"/></clipPath>')
    strip = "".join(chips)
    body = (f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="12" fill="{BG0}" stroke="{LINE}"/>'
            f'<g clip-path="url(#cl)"><g class="mq">{strip}<g transform="translate({total:.1f} 0)">{strip}</g></g>'
            f'<rect width="{W}" height="{H}" fill="url(#ef)"/></g>')
    write("stream.svg", svg(W, H, body, css, "Also using: " + ", ".join(items), defs))


# ═════════════════════════════ BUTTONS ═════════════════════════════
def build_button(name, label, sub, color, fname):
    W, H = 280, 64
    path = simple_icon_path(name)
    css = (".run{animation:run 3s linear infinite}@keyframes run{to{stroke-dashoffset:-688}}"
           ".hb{animation:hb 2.4s ease-in-out infinite}@keyframes hb{0%,100%{opacity:.35}50%{opacity:.9}}")
    defs = (f'<linearGradient id="bg2" x1="0" x2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{MAGENTA}"/></linearGradient>'
            f'<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="2.5" result="b"/>'
            f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    per = 2 * (W - 4 + H - 4)
    body = (f'<rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12" fill="{BG0}" stroke="{LINE}"/>'
            f'<rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12" fill="none" stroke="url(#bg2)" stroke-width="1.5" class="hb"/>'
            f'<rect x="2" y="2" width="{W - 4}" height="{H - 4}" rx="12" fill="none" stroke="{CYAN}" stroke-width="2.5" '
            f'stroke-dasharray="90 {per - 90}" class="run" filter="url(#glow)"/>'
            f'<g transform="translate(22 18) scale(1.15)"><path d="{path}" fill="{color}"/></g>'
            f'<text x="66" y="30" font-family="{ORB}" font-weight="700" font-size="15" letter-spacing="2" fill="{TEXT}">{label}</text>'
            f'<text x="66" y="48" font-family="{MONO}" font-size="12" fill="{MUTED}">{escape(sub)}</text>'
            f'<path d="M{W - 34} 26l8 6-8 6" fill="none" stroke="{CYAN}" stroke-width="2" class="hb"/>')
    body = body.replace("-688", f"-{per}")
    css = css.replace("-688", f"-{per}")
    write(fname, svg(W, H, body, css, f"{label} — {sub}", defs))


# ═════════════════════════════ FOOTER ═════════════════════════════
def build_footer():
    W, H = 880, 130
    css = (".bar{transform-box:fill-box;transform-origin:center;animation:eq 1.4s ease-in-out infinite}"
           "@keyframes eq{0%,100%{transform:scaleY(.25)}50%{transform:scaleY(1)}}"
           ".blink{animation:bl 1.1s steps(1) infinite}@keyframes bl{0%{opacity:1}50%{opacity:0}}")
    defs = (f'<linearGradient id="eqg" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{MAGENTA}"/></linearGradient>'
            f'<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="2" result="b"/>'
            f'<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    bars = []
    n = 64
    for i in range(n):
        x = 40 + i * (W - 80) / n
        h = 10 + 26 * abs(math.sin(i * 0.45)) * (0.4 + 0.6 * math.sin(math.pi * i / n))
        bars.append(f'<rect x="{x:.1f}" y="{40 - h / 2:.1f}" width="6" height="{h:.1f}" rx="3" fill="url(#eqg)" class="bar" '
                    f'style="animation-delay:-{(i * 0.09) % 1.4:.2f}s;opacity:.85"/>')
    body = (f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="{BG0}" stroke="{LINE}"/>'
            f'<g filter="url(#glow)">{"".join(bars)}</g>'
            f'<text x="{W / 2}" y="92" text-anchor="middle" font-family="{ORB}" font-weight="700" font-size="16" letter-spacing="5" fill="{TEXT}">'
            f'END OF TRANSMISSION</text>'
            f'<text x="{W / 2}" y="114" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{MUTED}">'
            f'thanks for visiting · see you in the next build <tspan fill="{CYAN}" class="blink">█</tspan></text>')
    write("footer.svg", svg(W, H, body, css, "End of transmission — thanks for visiting", defs))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    build_hero()
    build_divider("01", "IDENTITY", "div-identity.svg")
    build_divider("02", "TECH ARSENAL", "div-arsenal.svg")
    build_divider("03", "UPLINK", "div-uplink.svg")
    build_timeline()
    build_orbit()
    build_stream()
    build_button("linkedin", "LINKEDIN", "/in/pasindufdo", "#0A66C2", "btn-linkedin.svg")
    build_button("github", "GITHUB", "@pasindufernando1", "#FFFFFF", "btn-github.svg")
    build_footer()
