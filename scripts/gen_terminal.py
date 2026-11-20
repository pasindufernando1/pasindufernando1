"""Generate an animated 'neofetch' terminal SVG for the GitHub profile header.

Pure SMIL animation (works inside <img> on GitHub); loops every T seconds.
Usage: python3 gen_terminal.py <out.svg> [freeze_at_seconds]
"""
import sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]
FREEZE = float(sys.argv[2]) if len(sys.argv) > 2 else None  # static frame for previews

W, H = 880, 470
T = 20.0                      # loop length (s)
HIDE_AT, GONE_AT = 0.955, 0.985
FS, CW, LH = 15, 9.03, 23     # font size, mono char width, line height

BG, BAR, BORDER = "#0D1117", "#161B22", "#30363D"
TEAL, AMBER, TXT, MUTED, PINK, BLUE = "#46C0BC", "#F0A23B", "#C9D1D9", "#8B949E", "#F778BA", "#79C0FF"
FONT = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

out = []
uid = [0]


def k(t):
    return max(0.0, min(1.0, t / T))


def appear(t):
    """SMIL opacity animation: hidden until t, visible until loop end."""
    if FREEZE is not None:
        return "" if FREEZE >= t else None
    a = k(t)
    return (f'<animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" calcMode="discrete" '
            f'values="0;1;0" keyTimes="0;{a:.4f};{GONE_AT}"/>')


def group(t, body):
    anim = appear(t)
    if anim is None:
        return ""
    op = "1" if FREEZE is not None else "0"
    return f'<g opacity="{op}">{anim}{body}</g>'


def typed(x, y, text, t0, cps=14, color=TXT):
    """Text revealed character-by-character via an animated clip rect."""
    uid[0] += 1
    cid = f"c{uid[0]}"
    n = len(text)
    if FREEZE is not None:
        shown = max(0, min(n, int((FREEZE - t0) * cps))) if FREEZE >= t0 else 0
        rect = f'<rect x="{x}" y="{y - FS}" width="{shown * CW:.1f}" height="{LH}"/>'
    else:
        vals, keys = ["0"], ["0"]
        for i in range(n + 1):
            vals.append(f"{i * CW:.1f}")
            keys.append(f"{k(t0 + i / cps):.4f}")
        vals.append("0")
        keys.append(f"{GONE_AT}")
        rect = (f'<rect x="{x}" y="{y - FS}" width="0" height="{LH}">'
                f'<animate attributeName="width" dur="{T}s" repeatCount="indefinite" calcMode="discrete" '
                f'values="{";".join(vals)}" keyTimes="{";".join(keys)}"/></rect>')
    out.append(f'<clipPath id="{cid}">{rect}</clipPath>')
    out.append(f'<text x="{x}" y="{y}" fill="{color}" clip-path="url(#{cid})">{escape(text)}</text>')
    return t0 + n / cps


def prompt(y, t):
    body = (f'<text x="28" y="{y}"><tspan fill="{TEAL}" font-weight="700">pasindu</tspan>'
            f'<tspan fill="{MUTED}">@</tspan><tspan fill="{AMBER}" font-weight="700">choreo-labs</tspan>'
            f'<tspan fill="{MUTED}">:</tspan><tspan fill="{BLUE}">~</tspan><tspan fill="{TXT}">$</tspan></text>')
    out.append(group(t, body))
    return 28 + len("pasindu@choreo-labs:~$ ") * CW


# ---------------------------------------------------------------- frame
out.append(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="12" fill="{BG}" stroke="{BORDER}"/>')
out.append(f'<path d="M1 13a12 12 0 0 1 12-12h{W - 26}a12 12 0 0 1 12 12v23H1z" fill="{BAR}"/>')
out.append(f'<line x1="1" y1="36" x2="{W - 1}" y2="36" stroke="{BORDER}"/>')
for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
    out.append(f'<circle cx="{22 + i * 20}" cy="18.5" r="6" fill="{c}"/>')
out.append(f'<text x="{W / 2}" y="23" text-anchor="middle" fill="{MUTED}" font-size="13">pasindu@choreo-labs: ~</text>')

# ---------------------------------------------------------------- neofetch
y = 70
x = prompt(y, 0.2)
t = typed(x, y, "neofetch", 0.7)
t_out = t + 0.35

# pixel monogram "PF" with gradient fill
P = ["11110", "10001", "10001", "11110", "10000", "10000", "10000"]
F = ["11111", "10000", "10000", "11110", "10000", "10000", "10000"]
cell, gx, gy = 17, 44, 118
rects = []
for r in range(7):
    for c in range(5):
        for off, glyph in ((0, P), (6, F)):
            if glyph[r][c] == "1":
                fill = TEAL if off == 0 else AMBER
                rects.append(f'<rect x="{gx + (c + off) * cell}" y="{gy + r * cell}" width="{cell - 3}" height="{cell - 3}" rx="3" fill="{fill}"/>')
mono = "".join(rects)
mono += (f'<text x="{gx + 5.5 * cell - 1.5}" y="{gy + 7 * cell + 34}" text-anchor="middle" fill="{MUTED}" '
         f'font-size="12" letter-spacing="3">HELLO, WORLD</text>')
out.append(group(t_out, mono))

ix, iy = 290, 102
info = [
    ("title", None),
    ("rule", None),
    ("Name", "Pasindu Fernando"),
    ("Role", "Software Engineer @ Choreo Labs"),
    ("Builds", "Ballerina Language Server · VS Code ext"),
    ("Focus", "Backend systems · Developer tooling"),
    ("Research", "Fault-tolerant live VM migration"),
    ("Stack", "Java · Ballerina · C · Go"),
    ("Education", "BSc (Hons) CS · UCSC · GPA 3.98/4.00"),
    ("Off-duty", "Tennis · Carrom · Volunteering"),
    ("colors", None),
]
for i, (key, val) in enumerate(info):
    ty = iy + i * LH
    tt = t_out + 0.07 * i
    if key == "title":
        body = (f'<text x="{ix}" y="{ty}" font-weight="700"><tspan fill="{TEAL}">pasindu</tspan>'
                f'<tspan fill="{MUTED}">@</tspan><tspan fill="{AMBER}">choreo-labs</tspan></text>')
    elif key == "rule":
        body = f'<text x="{ix}" y="{ty}" fill="{MUTED}">{"─" * 19}</text>'
    elif key == "colors":
        cols = ["#F85149", AMBER, "#3FB950", TEAL, BLUE, "#BC8CFF", PINK, TXT]
        body = "".join(f'<rect x="{ix + j * 26}" y="{ty - 13}" width="22" height="16" rx="3" fill="{c}"/>'
                       for j, c in enumerate(cols))
    else:
        body = (f'<text x="{ix}" y="{ty}"><tspan fill="{TEAL}" font-weight="700">{key}</tspan>'
                f'<tspan fill="{MUTED}">: </tspan><tspan fill="{TXT}">{escape(val)}</tspan></text>')
    out.append(group(tt, body))
t_info_end = t_out + 0.07 * len(info)

# ---------------------------------------------------------------- ls ~/projects
y2 = iy + len(info) * LH + 22
x = prompt(y2, t_info_end + 0.6)
t = typed(x, y2, "ls ~/projects", t_info_end + 1.1)
y3 = y2 + LH
projects = [("VentureVerse/", TEAL), ("Sri-Tel/", AMBER), ("LIFELINE/", PINK), ("c-webserver/", BLUE)]
px = 28
for j, (name, col) in enumerate(projects):
    out.append(group(t + 0.3 + j * 0.08, f'<text x="{px}" y="{y3}" fill="{col}" font-weight="700">{name}</text>'))
    px += (len(name) + 4) * CW

# ---------------------------------------------------------------- idle prompt + cursor
y4 = y3 + LH + 8
t_idle = t + 0.9
x = prompt(y4, t_idle)
if FREEZE is None:
    a = k(t_idle)
    cur = (f'<rect x="{x + 1}" y="{y4 - 14}" width="9" height="18" fill="{TEAL}" opacity="0">'
           f'<animate attributeName="opacity" dur="{T}s" repeatCount="indefinite" calcMode="discrete" '
           f'values="0;1;0" keyTimes="0;{a:.4f};{GONE_AT}"/></rect>')
    blink = (f'<rect x="{x}" y="{y4 - 15}" width="11" height="20" fill="{BG}" opacity="0">'
             f'<animate attributeName="opacity" dur="1.06s" repeatCount="indefinite" calcMode="discrete" '
             f'values="0;1" keyTimes="0;0.5"/></rect>')
    out.append(cur + group(t_idle, blink))
elif FREEZE >= t_idle:
    out.append(f'<rect x="{x + 1}" y="{y4 - 14}" width="9" height="18" fill="{TEAL}"/>')

assert y4 + 20 < H, (y4, H)
assert t_idle / T < HIDE_AT, "timeline too long for loop"

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Animated terminal running neofetch for Pasindu Fernando, Software Engineer at Choreo Labs">
<g font-family="{FONT}" font-size="{FS}" xml:space="preserve">
{chr(10).join(s for s in out if s)}
</g>
</svg>
'''
open(OUT, "w").write(svg)
print(f"wrote {OUT}  idle at {t_idle:.1f}s / loop {T}s")
