"""Original dark illustrations for the Source from Sri Lanka section: one per export category plus the exporter
services. Same style and palette as art.py and art_more.py, written to assets/art/."""
from art import W, C, S, M, node, person
from art_more import doc, bubble, coin, globe, check

T = "rgba(73,198,245,.16)"   # cyan tint fill
G = "rgba(247,166,0,.22)"    # saffron tint fill


def leaf(x, y, s=1.0, rot=0, col=C, fill=T):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M0 0C40-60 120-70 170-50 140 0 80 40 0 0z" fill="{fill}" stroke="{col}" stroke-width="{6 / s:.1f}"/>'
            f'<path d="M0 0C50-18 100-34 170-50" stroke="{col}" stroke-width="{4 / s:.1f}"/></g>')


def tyre(x, y, r=150, col=W):
    treads = "".join(f'<path d="M{x} {y - r}l0 {r * .16}" stroke="{M}" stroke-width="10" transform="rotate({a} {x} {y})"/>' for a in range(0, 360, 20))
    return (f'<circle cx="{x}" cy="{y}" r="{r}" stroke="{col}" stroke-width="8"/>{treads}<circle cx="{x}" cy="{y}" r="{r * .62}" stroke="{C}" stroke-width="7"/>'
            f'<circle cx="{x}" cy="{y}" r="{r * .3}" fill="{G}" stroke="{S}" stroke-width="6"/>' + "".join(node(x + r * .46 * dx, y + r * .46 * dy, 8, S) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]))


def fish(x, y, s=1.0, col=W, fill="none"):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-160 0C-100-70 40-80 120-20l70-50v140l-70-50C40 80-100 70-160 0z" fill="{fill}" stroke="{col}" stroke-width="{7 / s:.1f}"/>'
            f'<circle cx="-100" cy="-12" r="9" fill="{col}" stroke="none"/><path d="M-60-40q20 40 0 80" stroke="{col}" stroke-width="{5 / s:.1f}"/></g>')


def gem(x, y, s=1.0, col=C, fill=T):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-120-60h240l60 70-180 190-180-190z" fill="{fill}" stroke="{col}" stroke-width="{7 / s:.1f}"/>'
            f'<path d="M-180 10h360M-120-60l40 70 80-70 80 70 40-70M-80 10l80 190 80-190" stroke="{col}" stroke-width="{5 / s:.1f}"/></g>')


def gear(x, y, r=110, col=W, teeth=10):
    t = "".join(f'<rect x="{x - 18}" y="{y - r - 26}" width="36" height="40" rx="6" stroke="{col}" stroke-width="6" transform="rotate({i * 360 / teeth} {x} {y})"/>' for i in range(teeth))
    return f'{t}<circle cx="{x}" cy="{y}" r="{r}" fill="#082a66" stroke="{col}" stroke-width="7"/><circle cx="{x}" cy="{y}" r="{r * .36}" stroke="{S}" stroke-width="7"/>'


def box3d(x, y, w=260, h=180, d=90, col=W):
    return (f'<path d="M{x} {y}h{w}v{h}h-{w}z" stroke="{col}" stroke-width="7"/><path d="M{x} {y}l{d} -{d * .6}h{w}l-{d} {d * .6}M{x + w} {y + h}l{d} -{d * .6}v-{h}" stroke="{col}" stroke-width="7"/>'
            f'<path d="M{x + w * .38} {y}l{d} -{d * .6}h{w * .24}l-{d} {d * .6}z" fill="{S}" stroke="none"/>')


def waves(y, x0=200, x1=1000, col=C, n=6):
    step = (x1 - x0) / n
    d = f"M{x0} {y}" + "".join(f"q{step / 4} -22 {step / 2} 0t{step / 2} 0" for _ in range(n))
    return f'<path d="{d}" stroke="{col}" stroke-width="6"/>'


SCENES = {
    # ---------------- plantation and spice
    "s-tea": f'<path d="M330 360h420v60c0 130-90 230-210 230S330 550 330 420z" fill="{T}" stroke="{W}" stroke-width="8"/><path d="M750 400h50a60 60 0 0 1 0 120h-62" stroke="{W}" stroke-width="8"/>'
    + f'<path d="M260 680h560" stroke="{M}" stroke-width="6"/><path d="M450 300q-30-50 0-90t0-90M540 300q-30-50 0-90t0-90M630 300q-30-50 0-90t0-90" stroke="{M}" stroke-width="5"/>'
    + leaf(820, 300, 1.1, -30, S, G) + leaf(860, 330, .8, 20),
    "s-cinnamon": "".join(f'<g transform="rotate(-12 600 450)"><rect x="300" y="{y}" width="600" height="56" rx="28" fill="{f}" stroke="{c}" stroke-width="6"/><path d="M330 {y + 12}q-14 16 0 32" stroke="{c}" stroke-width="5"/></g>'
                          for y, f, c in [(300, G, S), (370, T, C), (440, G, S), (510, T, C), (580, G, S)])
    + f'<path d="M560 250v420M640 250v420" stroke="{W}" stroke-width="8" transform="rotate(-12 600 450)"/>' + leaf(840, 220, .8, -20),
    "s-spices": f'<path d="M420 300h260v320q0 40-40 40H460q-40 0-40-40z" stroke="{W}" stroke-width="7"/><rect x="400" y="250" width="300" height="56" rx="12" fill="{S}" stroke="none"/>'
    + f'<path d="M440 460h220" stroke="{M}" stroke-width="5"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}" stroke="{c}" stroke-width="5"/>' for x, y, r, f, c in [(780, 560, 30, "#082a66", W), (840, 600, 26, "#082a66", M), (800, 630, 22, "#082a66", W), (880, 540, 24, "#082a66", M), (300, 600, 26, "#082a66", W), (250, 560, 20, "#082a66", M)])
    + f'<path d="M860 300l24 60 64 6-48 42 14 62-54-32-54 32 14-62-48-42 64-6z" fill="{G}" stroke="{S}" stroke-width="6"/>',
    "s-herbal": f'<path d="M340 420h520c0 140-110 230-260 230S340 560 340 420z" fill="{T}" stroke="{W}" stroke-width="8"/><path d="M500 650l-30 50h260l-30-50" stroke="{W}" stroke-width="7"/>'
    + f'<path d="M720 160l-150 300" stroke="{S}" stroke-width="22"/>' + leaf(380, 380, 1, -40) + leaf(560, 380, .9, -150, S, G) + leaf(300, 300, .7, -70),
    # ---------------- coconut
    "s-coconut": f'<circle cx="480" cy="450" r="190" fill="#3b2a1a" stroke="{W}" stroke-width="8"/><circle cx="480" cy="450" r="150" fill="#f6f1e6" stroke="none"/><circle cx="480" cy="450" r="150" stroke="{M}" stroke-width="4"/>'
    + f'<path d="M700 520h300c0 80-60 130-150 130S700 600 700 520z" fill="{T}" stroke="{C}" stroke-width="7"/><path d="M760 480q30-40 0-80M850 480q30-40 0-80M940 480q30-40 0-80" stroke="{M}" stroke-width="5"/>',
    "s-cocopeat": f'<path d="M260 380l200-110 260 70-200 120z" fill="{G}" stroke="{S}" stroke-width="7"/><path d="M260 380v190l260 90V460M720 340v190L520 660" stroke="{S}" stroke-width="7"/>'
    + "".join(f'<path d="M{x} {y}l{60} 20" stroke="#c98a2b" stroke-width="5"/>' for x, y in [(300, 450), (340, 520), (420, 480), (380, 580), (450, 600)])
    + f'<rect x="780" y="430" width="200" height="230" rx="24" stroke="{W}" stroke-width="7"/><path d="M880 430V300" stroke="{C}" stroke-width="7"/>' + leaf(880, 330, .7, -40) + leaf(880, 360, .7, -140, C, T),
    "s-carbon": "".join(f'<path d="M{x} {y}l40-23 40 23v46l-40 23-40-23z" fill="{"#0a1a3a" if (i + j) % 3 else G}" stroke="{C if (i + j) % 3 else S}" stroke-width="5"/>' for i, x in enumerate(range(240, 640, 80)) for j, y in enumerate(range(260 + (i % 2) * 46, 660, 92)))
    + f'<rect x="760" y="230" width="190" height="420" rx="40" stroke="{W}" stroke-width="8"/><path d="M760 330h190M760 550h190" stroke="{M}" stroke-width="6"/><path d="M855 180v50M855 650v50" stroke="{C}" stroke-width="8"/>'
    + "".join(node(820 + (k % 3) * 34, 380 + (k // 3) * 40, 9, S) for k in range(12)),
    # ---------------- fresh produce and plants
    "s-fruit": f'<path d="M420 360c-90 0-130 90-130 170s60 160 130 160 130-80 130-160-40-170-130-170z" fill="{G}" stroke="{S}" stroke-width="8"/>'
    + "".join(f'<path d="M{330 + i * 40} 420l60 60M{390 + i * 40} 420l-60 60" stroke="#c98a2b" stroke-width="4"/>' for i in range(4))
    + f'<path d="M420 360l-60-120 50 70 10-110 30 110 50-70-60 120" fill="{T}" stroke="{C}" stroke-width="6"/>'
    + f'<path d="M640 300c140 40 230 160 250 320-80-140-170-200-280-230z" fill="{G}" stroke="{S}" stroke-width="7"/><path d="M700 330c120 50 190 150 210 290" stroke="{S}" stroke-width="5"/><path d="M630 280l-20-40" stroke="{W}" stroke-width="8"/>',
    "s-flora": f'<path d="M600 680V320" stroke="{C}" stroke-width="8"/>' + leaf(600, 600, 1.1, -30) + leaf(600, 520, 1.1, -150, C, T) + leaf(600, 450, .9, -40)
    + "".join(f'<ellipse cx="600" cy="250" rx="34" ry="80" fill="{G}" stroke="{S}" stroke-width="6" transform="rotate({a} 600 300)"/>' for a in range(0, 360, 60)) + node(600, 300, 26, S)
    + f'<path d="M420 680h360l-30-60H450z" stroke="{W}" stroke-width="7"/>',
    # ---------------- rubber, apparel, leather
    "s-tyres": tyre(470, 440, 200) + f'<path d="M760 640V330h120l60 140h80v170" stroke="{W}" stroke-width="7"/><path d="M760 380l-60-180M730 300h-60" stroke="{S}" stroke-width="8"/>' + tyre(830, 640, 46, W) + tyre(1000, 640, 46, W),
    "s-gloves": f'<path d="M430 690V470l-60-180q-10-40 25-48t50 30l45 130V200q0-36 36-36t36 36v190V160q0-36 36-36t36 36v230V190q0-36 36-36t36 36v210V260q0-36 36-36t36 36v300q0 130-130 130z" fill="{T}" stroke="{C}" stroke-width="8"/>'
    + f'<path d="M430 690h270v40H430z" fill="{S}" stroke="none"/><path d="M820 300l40 40 80-90" stroke="{S}" stroke-width="10"/>',
    "s-apparel": f'<path d="M600 210v-40a36 36 0 1 1 36 36" stroke="{W}" stroke-width="7"/><path d="M600 210L320 330h560z" stroke="{W}" stroke-width="7"/>'
    + f'<path d="M470 330l-130 70 50 100 70-30v220h280V470l70 30 50-100-130-70c-20 40-60 60-130 60s-110-20-130-60z" fill="{T}" stroke="{C}" stroke-width="8"/>'
    + f'<path d="M600 390v300" stroke="{M}" stroke-width="4" stroke-dasharray="4 14"/><rect x="660" y="520" width="70" height="44" rx="6" fill="{S}" stroke="none"/>',
    "s-leather": f'<path d="M250 560c0-60 30-110 90-120l140-20 120 70 200 30c50 8 70 40 70 80v40H250z" fill="{G}" stroke="{S}" stroke-width="8"/><path d="M250 640h620" stroke="{W}" stroke-width="10"/><path d="M480 420l40 80M540 450l30 60" stroke="{S}" stroke-width="5"/>'
    + f'<rect x="760" y="250" width="230" height="170" rx="20" stroke="{W}" stroke-width="7"/><path d="M820 250v-40h110v40" stroke="{W}" stroke-width="7"/><path d="M760 310h230" stroke="{C}" stroke-width="5"/>',
    # ---------------- industrial
    "s-electrical": f'<circle cx="400" cy="430" r="190" stroke="{W}" stroke-width="8"/><circle cx="400" cy="430" r="60" fill="{G}" stroke="{S}" stroke-width="7"/>'
    + "".join(f'<circle cx="400" cy="430" r="{r}" stroke="{C}" stroke-width="5" opacity=".8"/>' for r in (90, 115, 140, 165))
    + f'<path d="M590 430c80 0 60 180 160 180h80" stroke="{C}" stroke-width="10"/>'
    + f'<rect x="760" y="250" width="240" height="300" rx="16" stroke="{W}" stroke-width="7"/>' + "".join(f'<path d="M{x} 250v-60" stroke="{W}" stroke-width="7"/><circle cx="{x}" cy="180" r="16" fill="{S}" stroke="none"/>' for x in (810, 880, 950))
    + "".join(f'<path d="M790 {y}h180" stroke="{M}" stroke-width="5"/>' for y in (300, 340, 380, 420, 460, 500)) + f'<path d="M880 590l-30 60h50l-30 60" stroke="{S}" stroke-width="8"/>',
    "s-engineering": gear(470, 440, 140) + gear(760, 330, 80, C, 8)
    + f'<path d="M700 520h240v150H700z" stroke="{W}" stroke-width="7"/><path d="M940 560h80v70h-80M760 520v-40h120v40" stroke="{W}" stroke-width="7"/><circle cx="820" cy="595" r="40" stroke="{S}" stroke-width="7"/>',
    "s-boats": f'<path d="M260 520h680l-90 140H380z" fill="{T}" stroke="{W}" stroke-width="8"/><path d="M420 520V360h260l80 160" stroke="{W}" stroke-width="7"/><path d="M470 410h70v50h-70zM580 410h70v50h-70z" fill="{S}" stroke="none"/>'
    + f'<path d="M560 360V220" stroke="{C}" stroke-width="7"/>' + waves(700, 180, 1020) + waves(750, 260, 940, M),
    "s-packaging": box3d(300, 380, 300, 230, 100) + f'<rect x="740" y="250" width="200" height="300" rx="16" stroke="{C}" stroke-width="7"/><path d="M780 320h120M780 360h120M780 400h80" stroke="{M}" stroke-width="5"/>'
    + "".join(f'<path d="M{780 + i * 12} 460v50" stroke="{W}" stroke-width="{3 + (i % 3)}"/>' for i in range(10)),
    "s-ceramics": f'<ellipse cx="480" cy="520" rx="250" ry="70" stroke="{W}" stroke-width="8"/><ellipse cx="480" cy="510" rx="170" ry="44" stroke="{C}" stroke-width="5"/><ellipse cx="480" cy="505" rx="100" ry="24" fill="{T}" stroke="none"/>'
    + f'<path d="M720 300h220l-20 260q-4 40-44 40H784q-40 0-44-40z" fill="{T}" stroke="{W}" stroke-width="8"/><path d="M940 360h30a50 50 0 0 1 0 100h-40" stroke="{W}" stroke-width="7"/><path d="M760 380h160" stroke="{S}" stroke-width="10"/>',
    "s-wood": f'<path d="M390 250V680M620 250V680" stroke="{W}" stroke-width="10"/><path d="M390 290h230M390 350h230M390 410h230" stroke="{W}" stroke-width="7"/><path d="M350 470h310" stroke="{S}" stroke-width="18"/><path d="M370 480v200M640 480v200" stroke="{W}" stroke-width="8"/>'
    + f'<rect x="760" y="300" width="240" height="380" rx="14" fill="{G}" stroke="{S}" stroke-width="7"/>' + "".join(f'<path d="M{790 + i * 44} 320q-20 170 0 340" stroke="#c98a2b" stroke-width="4"/>' for i in range(5)),
    # ---------------- sea and earth
    "s-seafood": fish(560, 420, 1.6, W, T) + waves(680, 200, 1000) + waves(730, 300, 900, M) + node(880, 260, 10, S) + node(930, 300, 7, S),
    "s-aquarium": f'<rect x="270" y="240" width="660" height="420" rx="28" stroke="{W}" stroke-width="8"/><path d="M270 330h660" stroke="{C}" stroke-width="4" stroke-dasharray="6 12"/>'
    + fish(520, 470, .55, S, G) + fish(720, 400, .45, C, T) + leaf(330, 640, .9, -80, C, T) + leaf(880, 640, .8, -110, C, T)
    + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" stroke="{M}" stroke-width="4"/>' for x, y, r in [(800, 300, 12), (820, 260, 8), (790, 230, 6)]),
    "s-food": f'<path d="M330 320h120v40l30 50v260H300V410l30-50z" fill="{T}" stroke="{W}" stroke-width="7"/><rect x="320" y="470" width="140" height="110" fill="{S}" stroke="none"/>'
    + f'<path d="M560 420h200v260H560z" stroke="{W}" stroke-width="7"/><rect x="550" y="380" width="220" height="50" rx="10" fill="{C}" stroke="none"/><path d="M590 500h140M590 540h100" stroke="{M}" stroke-width="5"/>'
    + f'<circle cx="900" cy="560" r="110" fill="{G}" stroke="{S}" stroke-width="7"/>' + "".join(node(900 + dx, 560 + dy, 8, "#082a66") for dx, dy in [(-40, -30), (20, -50), (40, 10), (-20, 30), (0, 70), (-60, 40)]),
    "s-gems": gem(520, 380, 1.3) + f'<circle cx="860" cy="520" r="110" stroke="{S}" stroke-width="10"/>' + gem(860, 380, .45, S, G)
    + "".join(f'<path d="M{x} {y}l0-34M{x - 17} {y - 17}h34" stroke="{W}" stroke-width="5"/>' for x, y in [(260, 230), (980, 230), (300, 640)]),
    "s-minerals": f'<path d="M300 660l60-260 90-80 70 120-30 220z" fill="{T}" stroke="{C}" stroke-width="7"/><path d="M490 660l40-330 80-90 70 150-40 270z" fill="{T}" stroke="{W}" stroke-width="7"/>'
    + f'<path d="M660 660l70-200 100-40 60 120-50 120z" fill="#0a1a3a" stroke="{M}" stroke-width="7"/><path d="M760 470l40 80M800 440l50 90" stroke="{M}" stroke-width="4"/><path d="M250 660h700" stroke="{S}" stroke-width="7"/>',
    # ---------------- services for exporters and buyers
    "s-radar": "".join(f'<circle cx="460" cy="460" r="{r}" stroke="{C}" stroke-width="5" opacity="{o}"/>' for r, o in [(70, 1), (140, .8), (210, .6)])
    + f'<path d="M460 460L460 250A210 210 0 0 1 642 355z" fill="{T}" stroke="none"/><path d="M460 460l182-105" stroke="{C}" stroke-width="6"/>'
    + node(560, 330, 14, S) + node(380, 560, 10, W) + node(600, 520, 9, W) + node(330, 380, 8, M)
    + bubble(760, 260, 260, 180, S) + f'<path d="M800 310h170M800 350h120M800 390h150" stroke="{W}" stroke-width="6"/>',
    "s-bid": doc(320, 180, 330, 470, W, 8) + check(400, 600, 1, S)
    + f'<circle cx="820" cy="420" r="120" fill="{G}" stroke="{S}" stroke-width="8"/><circle cx="820" cy="420" r="80" stroke="{S}" stroke-width="5"/>'
    + f'<path d="M760 520l-40 150 60-30 40 60 20-170M880 520l40 150-60-30-40 60" stroke="{S}" stroke-width="7"/>' + check(820, 420, 1.1, W),
    "s-import": globe(780, 380, 160) + f'<path d="M220 600h500l-60 90H290z" fill="{T}" stroke="{W}" stroke-width="8"/>'
    + "".join(f'<rect x="{x}" y="{y}" width="80" height="50" rx="4" fill="{f}" stroke="none"/>' for x, y, f in [(300, 545, S), (390, 545, C), (480, 545, S), (345, 490, C), (435, 490, S)])
    + f'<path d="M560 540q120-160 220-150" stroke="{S}" stroke-width="5" stroke-dasharray="3 14"/>' + node(780, 390, 14, S),
    "s-exporters": f'<path d="M240 670V420l140-80v80l140-80v80l140-80v330z" stroke="{W}" stroke-width="7"/><path d="M640 670V260h70v150" stroke="{W}" stroke-width="7"/><path d="M200 670h560" stroke="{M}" stroke-width="6"/>'
    + "".join(f'<rect x="{x}" y="540" width="50" height="50" rx="6" fill="{S if x == 420 else "none"}" stroke="{C}" stroke-width="5"/>' for x in (290, 420, 550))
    + globe(900, 380, 120) + f'<path d="M680 230q120-110 220 30" stroke="{S}" stroke-width="6"/><path d="M890 240l12 26 22-20" stroke="{S}" stroke-width="6"/>',
    "s-rfq": doc(330, 190, 320, 460, W, 7) + f'<circle cx="790" cy="410" r="120" stroke="{C}" stroke-width="9"/><path d="M875 495l120 120" stroke="{C}" stroke-width="18"/>'
    + person(790, 430, .9, S) + f'<rect x="380" y="560" width="180" height="50" rx="10" fill="{S}" stroke="none"/>',
    "s-stats": f'<path d="M230 690h740" stroke="{W}" stroke-width="7"/><path d="M230 690V200" stroke="{W}" stroke-width="7"/>'
    + "".join(f'<rect x="{x}" y="{690 - h}" width="78" height="{h}" rx="8" fill="{f}" stroke="{c}" stroke-width="6"/>'
              for x, h, f, c in [(290, 170, T, C), (400, 230, T, C), (510, 205, T, C), (620, 300, G, S), (730, 360, T, C), (840, 440, G, S)])
    + f'<path d="M300 470L440 400L550 430L660 330L770 290L880 190" stroke="{S}" stroke-width="7" stroke-dasharray="2 16" stroke-linecap="round"/>'
    + node(880, 190, 16, S),
}


def write_all(root):
    from art import svg as base_svg
    import art
    art.SCENES.update(SCENES)
    out = root / "assets" / "art"
    out.mkdir(parents=True, exist_ok=True)
    for k in SCENES:
        (out / f"{k}.svg").write_text(base_svg(k), encoding="utf-8")
