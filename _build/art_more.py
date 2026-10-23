"""More original dark illustrations, for the guides and the business services (offshoring) tiles. Same style as art.py."""
from art import W, C, S, M, person, node


def doc(x, y, w=220, h=280, col=W, lines=5, lc=M):
    ls = "".join(f'<path d="M{x + 30} {y + 60 + i * 38}h{w - 60 - (40 if i % 3 == 2 else 0)}" stroke="{lc}" stroke-width="6"/>' for i in range(lines))
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" stroke="{col}" stroke-width="6"/>{ls}'


def bubble(x, y, w, h, col=W):
    return f'<path d="M{x} {y + 20}q0-20 20-20h{w - 40}q20 0 20 20v{h - 40}q0 20-20 20H{x + 60}l-40 40v-40h-0q-20 0-20-20z" stroke="{col}" stroke-width="6"/>'


def bars(x0, base, vals, w=46, gap=26, cols=(C, W)):
    return "".join(f'<rect x="{x0 + i * (w + gap)}" y="{base - v}" width="{w}" height="{v}" rx="6" fill="{cols[i % len(cols)]}" stroke="none" opacity=".9"/>' for i, v in enumerate(vals))


def coin(x, y, r=40, col=S):
    return f'<circle cx="{x}" cy="{y}" r="{r}" stroke="{col}" stroke-width="6"/><path d="M{x} {y - r * .55}v{r * 1.1}M{x - r * .3} {y - r * .25}c0-14 {r * .6}-14 {r * .6} 0s-{r * .6} 14-{r * .6} 28 {r * .6} 14 {r * .6} 0" stroke="{col}" stroke-width="4"/>'


def globe(x, y, r=150, col=W):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" stroke="{col}" stroke-width="6"/><ellipse cx="{x}" cy="{y}" rx="{r * .45}" ry="{r}" stroke="{M}" stroke-width="4"/>'
            f'<path d="M{x - r} {y}h{2 * r}M{x - r * .87} {y - r * .5}h{r * 1.74}M{x - r * .87} {y + r * .5}h{r * 1.74}" stroke="{M}" stroke-width="4"/>')


def check(x, y, s=1, col=C):
    return f'<path d="M{x - 22 * s} {y}l{16 * s} {16 * s} {30 * s}-{34 * s}" stroke="{col}" stroke-width="{8 * s}"/>'


def headset(x, y, col=W):
    return (f'<path d="M{x - 90} {y + 20}v-30a90 90 0 0 1 180 0v30" stroke="{col}" stroke-width="7"/>'
            f'<rect x="{x - 110}" y="{y + 10}" width="40" height="80" rx="16" fill="{C}" stroke="none"/><rect x="{x + 70}" y="{y + 10}" width="40" height="80" rx="16" fill="{C}" stroke="none"/>'
            f'<path d="M{x + 90} {y + 90}q0 50-60 50h-30" stroke="{col}" stroke-width="6"/>{node(x - 4, y + 140, 12, S)}')


SCENES = {
    # ---------------- guides
    "g-salaries": bars(260, 600, [140, 200, 260, 330, 400]) + coin(860, 260, 70) + coin(960, 380, 50, C) + coin(800, 440, 44, W)
    + f'<path d="M230 600h470" stroke="{M}" stroke-width="5"/><path d="M250 470l110-70 100 40 120-110 110-60" stroke="{S}" stroke-width="7"/>',
    "g-hire": person(380, 420, 1.5) + person(600, 380, 1.8, C) + person(820, 420, 1.5)
    + f'<circle cx="600" cy="560" r="0"/><rect x="460" y="540" width="280" height="90" rx="20" stroke="{S}" stroke-width="6"/>' + check(600, 585, 1.2, S),
    "g-setup": f'<path d="M330 640V330l270-130 270 130v310" stroke="{W}" stroke-width="7"/><path d="M270 640h660" stroke="{M}" stroke-width="6"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="70" height="70" rx="8" stroke="{C}" stroke-width="5"/>' for x in (400, 565, 730) for y in (380, 500))
    + f'<path d="M600 200V90" stroke="{W}" stroke-width="6"/><path d="M600 90h110l-25 30 25 30H600" fill="{S}" stroke="none"/>',
    "g-facts": f'<circle cx="420" cy="420" r="170" stroke="{W}" stroke-width="7"/><path d="M420 420V250a170 170 0 0 1 160 230z" fill="{C}" stroke="none" opacity=".9"/><path d="M420 420l160 60" stroke="{S}" stroke-width="6"/>'
    + bars(700, 600, [150, 240, 320, 210], 50, 30, (S, W)) + f'<path d="M680 600h330" stroke="{M}" stroke-width="5"/>',
    "g-ecosystem": f'<path d="M600 140c90 70 120 190 80 330H520c-40-140-10-260 80-330z" stroke="{W}" stroke-width="7"/><circle cx="600" cy="300" r="36" stroke="{C}" stroke-width="6"/>'
    + f'<path d="M520 470l-70 80 90-20M680 470l70 80-90-20" stroke="{W}" stroke-width="7"/><path d="M560 540c0 60 40 110 40 110s40-50 40-110" fill="rgba(247,166,0,.45)" stroke="{S}" stroke-width="6"/>'
    + "".join(node(x, y, r, col) for x, y, r, col in [(260, 200, 10, C), (950, 220, 12, S), (300, 560, 8, W), (920, 600, 10, C), (840, 120, 7, W), (360, 360, 7, S)]),
    "g-eor": person(470, 450, 2.2) + f'<path d="M760 220l140 50v120c0 110-70 180-140 210-70-30-140-100-140-210V270z" stroke="{C}" stroke-width="7" fill="rgba(73,198,245,.12)"/>' + check(760, 400, 1.4, S),
    "g-pay": f'<rect x="230" y="260" width="400" height="250" rx="26" stroke="{W}" stroke-width="7"/><path d="M230 330h400" stroke="{C}" stroke-width="22"/><path d="M280 440h120M280 470h70" stroke="{M}" stroke-width="6"/>'
    + coin(880, 300, 60) + coin(880, 500, 60, C) + f'<path d="M660 360h130M790 360l-26-22M790 360l-26 22M790 460H660M660 460l26-22M660 460l26 22" stroke="{S}" stroke-width="6"/>',
    "g-calculator": f'<rect x="420" y="160" width="360" height="520" rx="36" stroke="{W}" stroke-width="7"/><rect x="470" y="215" width="260" height="100" rx="14" fill="rgba(73,198,245,.18)" stroke="{C}" stroke-width="5"/>'
    + "".join(f'<rect x="{470 + i * 92}" y="{360 + j * 92}" width="70" height="70" rx="14" fill="{S if (i == 2 and j == 2) else "none"}" stroke="{S if (i == 2 and j == 2) else M}" stroke-width="5"/>' for i in range(3) for j in range(3))
    + f'<path d="M560 270h140" stroke="{W}" stroke-width="8"/>',
    "g-compare": f'<path d="M600 150v470M440 640h320M360 250h480" stroke="{W}" stroke-width="7"/><circle cx="600" cy="150" r="20" fill="{S}" stroke="none"/>'
    + f'<path d="M360 250l-90 190h180zM840 250l-90 190h180z" stroke="{C}" stroke-width="6"/><path d="M270 440a90 40 0 0 0 180 0M750 440a90 40 0 0 0 180 0" fill="rgba(73,198,245,.25)" stroke="{C}" stroke-width="6"/>',
    "g-answers": bubble(240, 200, 420, 220) + bubble(560, 420, 400, 190, C)
    + f'<path d="M420 260q30-40 70-10t-30 60v30" stroke="{S}" stroke-width="10"/>{node(460, 380, 9, S)}<path d="M640 490h240M640 530h170" stroke="{W}" stroke-width="6"/>',
    "g-playbook": doc(380, 170, 300, 420, W, 7) + f'<rect x="560" y="250" width="280" height="400" rx="18" fill="#082a66" stroke="{C}" stroke-width="6"/>'
    + f'<path d="M610 330h180M610 380h180M610 430h120" stroke="{M}" stroke-width="6"/><path d="M700 520v90M660 570l40 40 40-40" stroke="{S}" stroke-width="8"/>',
    "g-why": globe(600, 430, 190) + f'<path d="M700 300c0-40 30-70 66-70s66 30 66 70c0 56-66 120-66 120s-66-64-66-120z" fill="{S}" stroke="none"/><circle cx="766" cy="300" r="22" fill="#082a66"/>',
    "g-countries": globe(600, 450, 170) + "".join(f'<path d="M600 450Q{(600 + x) / 2} {min(450, y) - 160} {x} {y}" stroke="{S}" stroke-width="5" stroke-dasharray="3 14"/>{node(x, y, 14, C)}' for x, y in [(220, 260), (300, 640), (980, 240), (1000, 600), (760, 140)]) + node(600, 450, 16, S),
    "g-offshoring": f'<rect x="300" y="300" width="380" height="270" rx="28" stroke="{W}" stroke-width="7"/><path d="M420 300v-50q0-20 20-20h100q20 0 20 20v50M300 400h380" stroke="{W}" stroke-width="7"/><rect x="460" y="380" width="60" height="40" rx="8" fill="{S}" stroke="none"/>'
    + globe(840, 330, 120) + f'<path d="M700 480q100 60 160-30" stroke="{C}" stroke-width="6" stroke-dasharray="3 14"/>',
    # ---------------- business services
    "o-accounting": doc(300, 180, 330, 440, W, 8) + f'<rect x="680" y="300" width="230" height="320" rx="26" stroke="{C}" stroke-width="7"/><rect x="715" y="340" width="160" height="60" rx="8" fill="rgba(73,198,245,.2)" stroke="{C}" stroke-width="4"/>'
    + "".join(f'<circle cx="{745 + i * 50}" cy="{450 + j * 55}" r="14" fill="{S if i == 2 and j == 2 else M}" stroke="none"/>' for i in range(3) for j in range(3)) + check(470, 580, 1, S),
    "o-research": bars(250, 620, [120, 190, 160, 260, 230, 330], 44, 24, (M, C)) + f'<circle cx="760" cy="330" r="120" stroke="{W}" stroke-width="8"/><path d="M845 415l130 130" stroke="{W}" stroke-width="16"/>'
    + f'<path d="M690 360l50-50 40 30 60-70" stroke="{S}" stroke-width="7"/>',
    "o-va": person(420, 470, 2.2) + headset(420, 320, W) + f'<rect x="680" y="230" width="300" height="300" rx="22" stroke="{C}" stroke-width="6"/><path d="M680 300h300M750 200v60M910 200v60" stroke="{C}" stroke-width="6"/>'
    + "".join(f'<rect x="{710 + i * 62}" y="{330 + j * 62}" width="44" height="40" rx="6" fill="{S if (i, j) in [(1, 0), (3, 1), (0, 2)] else "none"}" stroke="{M}" stroke-width="3"/>' for i in range(4) for j in range(3)),
    "o-marketing": f'<path d="M260 360v140l90 10 30 110h60l-20-104 380 104V250L350 350z" stroke="{W}" stroke-width="7"/><path d="M840 250v370" stroke="{W}" stroke-width="7"/>'
    + f'<path d="M900 330q50 0 50 50t-50 50M920 270q110 0 110 110t-110 110" stroke="{C}" stroke-width="6"/>' + bars(300, 200, [60, 100, 140], 40, 20, (S,)),
    "o-support": headset(600, 300, W) + bubble(220, 180, 240, 140, C) + bubble(760, 420, 260, 150, S) + f'<path d="M820 480h140M820 515h90" stroke="{W}" stroke-width="5"/><path d="M270 230h140M270 265h90" stroke="{W}" stroke-width="5"/>',
    "o-medical": doc(330, 170, 320, 440, W, 6) + f'<path d="M490 210v0" />' + f'<rect x="700" y="230" width="220" height="220" rx="30" fill="rgba(247,166,0,.15)" stroke="{S}" stroke-width="7"/><path d="M810 280v120M750 340h120" stroke="{S}" stroke-width="16"/>'
    + coin(810, 560, 54, C) + check(490, 560, 1, C),
    "o-legal": f'<path d="M600 160v460M470 640h260M330 260h540" stroke="{W}" stroke-width="7"/>'
    + f'<path d="M360 260l-80 170h160zM840 260l-80 170h160z" stroke="{C}" stroke-width="6"/><path d="M280 430a80 36 0 0 0 160 0M760 430a80 36 0 0 0 160 0" fill="rgba(73,198,245,.25)" stroke="{C}" stroke-width="6"/>'
    + f'<rect x="555" y="120" width="90" height="60" rx="10" fill="{S}" stroke="none"/>',
    "o-bim": f'<path d="M400 640V300l200-110 200 110v340" stroke="{W}" stroke-width="6"/><path d="M400 300l200 110 200-110M600 410v230" stroke="{C}" stroke-width="5"/>'
    + "".join(f'<path d="M400 {y}l200 110 200-110" stroke="{M}" stroke-width="3" opacity=".8"/>' for y in (400, 500, 600))
    + f'<path d="M220 680h760" stroke="{M}" stroke-width="5"/><path d="M880 220h120v120" stroke="{S}" stroke-width="6" stroke-dasharray="4 14"/><path d="M200 300l60-60 60 60" stroke="{S}" stroke-width="6"/>',
    "o-annotation": f'<rect x="230" y="190" width="740" height="480" rx="24" stroke="{W}" stroke-width="6"/>'
    + f'<circle cx="430" cy="380" r="90" fill="rgba(73,198,245,.18)" stroke="none"/><rect x="330" y="280" width="200" height="200" stroke="{C}" stroke-width="6" stroke-dasharray="16 10"/><rect x="330" y="250" width="110" height="30" fill="{C}" stroke="none"/>'
    + f'<path d="M640 560l90-150 80 110 50-60 70 100z" fill="rgba(247,166,0,.25)" stroke="none"/><rect x="620" y="380" width="320" height="200" stroke="{S}" stroke-width="6" stroke-dasharray="16 10"/><rect x="620" y="350" width="120" height="30" fill="{S}" stroke="none"/>',
    "o-insurance": f'<path d="M330 380a270 200 0 0 1 540 0z" fill="rgba(73,198,245,.15)" stroke="{C}" stroke-width="7"/><path d="M600 180v-30M600 380v200q0 50 50 50" stroke="{W}" stroke-width="7"/>'
    + person(400, 560, 1.1) + person(800, 560, 1.1) + f'<path d="M380 380q40-30 70 0 40-30 70 0M680 380q40-30 70 0 40-30 70 0" stroke="{C}" stroke-width="5"/>',
}


def write_all(root):
    from art import svg as base_svg
    import art
    art.SCENES.update(SCENES)
    out = root / "assets" / "art"
    out.mkdir(parents=True, exist_ok=True)
    for k in SCENES:
        (out / f"{k}.svg").write_text(base_svg(k), encoding="utf-8")
