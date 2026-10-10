"""Original dark illustrations for the industry tiles and the ways to build tiles. Pure SVG, written to assets/art/."""

W, C, S, M = "#ffffff", "#49c6f5", "#f7a600", "#8fa6d6"


def person(x, y, s=1.0, col=W, sw=6):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="{col}" stroke-width="{sw / s:.1f}" fill="none">'
            f'<circle cx="0" cy="-34" r="20"/><path d="M-38 44c2-30 18-44 38-44s36 14 38 44"/></g>')


def node(x, y, r=9, col=C):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}" stroke="none"/>'


SCENES = {
    # ---------------- industries
    "healthtech": f'''
<path d="M70 360h250l40-90 60 200 55-150 35 40h160" stroke="{C}" stroke-width="7"/>
<rect x="690" y="150" width="300" height="380" rx="26" stroke="{W}" stroke-width="6"/>
<path d="M840 215v90M795 260h90" stroke="{S}" stroke-width="12"/>
<path d="M735 370h210M735 415h210M735 460h130" stroke="{M}" stroke-width="6"/>
<path d="M690 360h-20" stroke="{C}" stroke-width="7"/>
<circle cx="1060" cy="190" r="34" stroke="{C}" stroke-width="5"/><path d="M1045 190l11 11 20-22" stroke="{C}" stroke-width="5"/>''',
    "automotive": f'''
<path d="M170 420l50-120c8-18 22-28 42-28h330c22 0 40 8 54 24l92 104 130 22c26 5 40 22 40 46v32H150v-50c0-14 6-24 20-30z" stroke="{W}" stroke-width="6"/>
<path d="M262 400l34-84h150v84zM480 316h110l74 84H480z" stroke="{M}" stroke-width="5"/>
<circle cx="320" cy="500" r="56" stroke="{C}" stroke-width="7"/><circle cx="320" cy="500" r="18" fill="{C}" stroke="none"/>
<circle cx="760" cy="500" r="56" stroke="{C}" stroke-width="7"/><circle cx="760" cy="500" r="18" fill="{C}" stroke="none"/>
<path d="M560 272v-70h160v-50M720 152h150M400 272v-110h-110" stroke="{S}" stroke-width="5" stroke-dasharray="2 14"/>
{node(870, 152, 11, S)}{node(290, 162, 11, S)}
<rect x="930" y="230" width="130" height="64" rx="10" stroke="{S}" stroke-width="5"/><path d="M1060 250h16v24h-16M952 262h40M972 244v36" stroke="{S}" stroke-width="5"/>''',
    "fintech": f'''
<path d="M120 560h960" stroke="{M}" stroke-width="4"/>
''' + "".join(f'<path d="M{x} {t}v{b - t}" stroke="{M}" stroke-width="4"/><rect x="{x - 22}" y="{o}" width="44" height="{h}" rx="5" fill="{col}" stroke="none"/>'
              for x, t, b, o, h, col in [(200, 380, 540, 410, 100, C), (310, 330, 520, 370, 90, W), (420, 360, 540, 400, 110, C), (530, 280, 470, 310, 110, W), (640, 300, 480, 330, 90, C), (750, 220, 420, 250, 120, W), (860, 180, 360, 210, 100, C)]) + f'''
<path d="M150 470l160-90 110 40 110-110 110 30 110-100 110-50 130-60" stroke="{S}" stroke-width="7"/>
<path d="M1000 110h70v70" stroke="{S}" stroke-width="7"/>
<circle cx="1010" cy="430" r="62" stroke="{W}" stroke-width="6"/><path d="M1010 396v68M990 414c0-12 40-12 40 0s-40 12-40 26 40 14 40 0" stroke="{W}" stroke-width="5"/>''',
    "ai": "".join(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{M}" stroke-width="2.5" opacity=".7"/>'
                  for x1, ys1, x2, ys2 in [(250, (170, 300, 430, 560), 520, (230, 365, 500)), (520, (230, 365, 500), 790, (170, 300, 430, 560)), (790, (170, 300, 430, 560), 1010, (300, 430))]
                  for y1 in ys1 for y2 in ys2) + "".join(node(250, y, 16, C) for y in (170, 300, 430, 560)) + "".join(node(520, y, 20, W) for y in (230, 365, 500))
          + "".join(node(790, y, 16, C) for y in (170, 300, 430, 560)) + "".join(node(1010, y, 22, S) for y in (300, 430))
          + f'<path d="M520 120l12 34 34 12-34 12-12 34-12-34-34-12 34-12z" fill="{S}" stroke="none"/>',
    "enterprise-software": f'''
<path d="M600 130l330 150-330 150-330-150z" stroke="{W}" stroke-width="6" fill="rgba(73,198,245,.10)"/>
<path d="M270 370l330 150 330-150" stroke="{C}" stroke-width="6"/>
<path d="M270 460l330 150 330-150" stroke="{S}" stroke-width="6"/>
<path d="M480 250l120 55 120-55M600 305v60" stroke="{M}" stroke-width="4"/>
<rect x="90" y="150" width="110" height="80" rx="12" stroke="{C}" stroke-width="5"/><path d="M200 190h80" stroke="{C}" stroke-width="4" stroke-dasharray="2 12"/>
<rect x="1000" y="150" width="110" height="80" rx="12" stroke="{C}" stroke-width="5"/><path d="M1000 190h-80" stroke="{C}" stroke-width="4" stroke-dasharray="2 12"/>
<path d="M118 180h54M118 202h34M1028 180h54M1028 202h34" stroke="{M}" stroke-width="5"/>''',
    "semiconductors-embedded": f'''
<rect x="420" y="170" width="360" height="360" rx="30" stroke="{W}" stroke-width="7"/>
<rect x="500" y="250" width="200" height="200" rx="14" stroke="{C}" stroke-width="6" fill="rgba(73,198,245,.12)"/>
<path d="M560 310h80v80h-80z" fill="{S}" stroke="none"/>
''' + "".join(f'<path d="M{x} 170V{y1}h{dx}M{x} 530v{600 - 530 + (0 if i % 2 else 30)}h{-dx}" stroke="{C}" stroke-width="5"/>' for i, (x, y1, dx) in enumerate([(480, 110, -150), (560, 80, -120), (640, 80, 130), (720, 110, 160)]))
    + "".join(f'<path d="M420 {y}H{x1}M780 {y}H{x2}" stroke="{C}" stroke-width="5"/>{node(x1, y, 10, S)}{node(x2, y, 10, S)}' for y, x1, x2 in [(230, 220, 980), (310, 150, 1050), (390, 150, 1050), (470, 220, 980)])
    + node(330, 110, 10, S) + node(440, 80, 10, S) + node(770, 80, 10, S) + node(880, 110, 10, S),
    "logistics-travel": f'''
<path d="M150 520C330 520 300 260 520 260s220 220 420 170 130-230 130-230" stroke="{C}" stroke-width="6" stroke-dasharray="4 20"/>
<path d="M150 440c-32 0-56 24-56 54 0 40 56 92 56 92s56-52 56-92c0-30-24-54-56-54z" stroke="{W}" stroke-width="6"/><circle cx="150" cy="494" r="18" fill="{S}" stroke="none"/>
<path d="M1070 110c-32 0-56 24-56 54 0 40 56 92 56 92s56-52 56-92c0-30-24-54-56-54z" stroke="{S}" stroke-width="6"/><circle cx="1070" cy="164" r="18" fill="{W}" stroke="none"/>
<g transform="translate(520 228) rotate(-18)"><path d="M-70 0l60-12 46-62h22l-24 62 50-10 16-22h16l-10 32 10 32h-16l-16-22-50-10 24 62h-22l-46-62-60-12z" fill="{W}" stroke="none"/></g>
<rect x="700" y="440" width="150" height="120" rx="10" stroke="{W}" stroke-width="6"/><path d="M700 480h150M760 440v40M790 440v40" stroke="{M}" stroke-width="5"/>
<rect x="866" y="490" width="100" height="70" rx="8" stroke="{C}" stroke-width="5"/><path d="M866 516h100" stroke="{C}" stroke-width="4"/>''',
    "govtech": f'''
<path d="M250 300l350-170 350 170z" stroke="{W}" stroke-width="7" fill="rgba(73,198,245,.10)"/>
<path d="M290 300h620M270 540h660M230 590h740" stroke="{W}" stroke-width="7"/>
''' + "".join(f'<path d="M{x} 330v190" stroke="{C}" stroke-width="16"/>' for x in (350, 475, 600, 725, 850)) + f'''
<circle cx="600" cy="232" r="30" stroke="{S}" stroke-width="6"/><path d="M586 232l10 10 18-20" stroke="{S}" stroke-width="5"/>
<path d="M1000 150c30 14 54 16 76 12v70c0 44-34 70-76 86-42-16-76-42-76-86v-70c22 4 46 2 76-12z" stroke="{S}" stroke-width="5"/>
<path d="M90 420h110M90 460h80M90 500h110" stroke="{M}" stroke-width="5"/>''',
    "finance-accounting": f'''
<rect x="160" y="130" width="380" height="470" rx="24" stroke="{W}" stroke-width="6"/>
<path d="M210 210h280" stroke="{S}" stroke-width="8"/>
''' + "".join(f'<path d="M210 {y}h150M410 {y}h80" stroke="{M}" stroke-width="6"/>' for y in (280, 335, 390, 445, 500)) + f'''
<path d="M210 550h280" stroke="{W}" stroke-width="5"/>
<path d="M660 600V430M770 600V330M880 600V380M990 600V230" stroke="{C}" stroke-width="54"/>
<path d="M620 600h430" stroke="{W}" stroke-width="5"/>
<path d="M640 330l120-90 110 50 140-130" stroke="{S}" stroke-width="6"/>{node(1010, 160, 12, S)}''',
    # ---------------- ways to build
    "software-outsourcing-sri-lanka": f'''
<circle cx="400" cy="360" r="220" stroke="{W}" stroke-width="6"/>
<path d="M180 360h440M400 140c-110 110-110 330 0 440M400 140c110 110 110 330 0 440M216 250h368M216 470h368" stroke="{M}" stroke-width="4"/>
<path d="M520 300C640 120 860 120 960 250" stroke="{S}" stroke-width="6" stroke-dasharray="4 18"/>
<path d="M520 420C660 600 860 590 960 470" stroke="{C}" stroke-width="6" stroke-dasharray="4 18"/>
{node(520, 300, 14, S)}{node(520, 420, 14, C)}
<rect x="840" y="250" width="270" height="220" rx="20" stroke="{W}" stroke-width="6"/>
<path d="M930 320l-44 40 44 40M1020 320l44 40-44 40M990 300l-30 120" stroke="{C}" stroke-width="7"/>''',
    "dedicated-development-team-sri-lanka": f'''
<rect x="150" y="120" width="900" height="480" rx="36" stroke="{M}" stroke-width="4" stroke-dasharray="6 16"/>
{person(330, 400, 1.5, C)}{person(600, 360, 1.9, W, 7)}{person(870, 400, 1.5, C)}
<path d="M400 250h400" stroke="{S}" stroke-width="5"/>
<path d="M600 150l14 30 32 4-24 22 6 32-28-16-28 16 6-32-24-22 32-4z" fill="{S}" stroke="none"/>''',
    "staff-augmentation-sri-lanka": f'''
{person(220, 420, 1.4, M, 5)}{person(430, 420, 1.4, M, 5)}{person(640, 420, 1.4, M, 5)}
<circle cx="880" cy="390" r="150" stroke="{S}" stroke-width="5" stroke-dasharray="6 16"/>
{person(880, 420, 1.7, S, 7)}
<path d="M1060 200v90M1015 245h90" stroke="{W}" stroke-width="10"/>
<path d="M150 560h560" stroke="{C}" stroke-width="5"/><path d="M710 560h320" stroke="{S}" stroke-width="5"/>''',
    "offshore-development-center-sri-lanka": f'''
<path d="M90 600h1020" stroke="{W}" stroke-width="5"/>
<path d="M190 600V310h170v290M400 600V190h220v410M660 600V370h160v230" stroke="{W}" stroke-width="6"/>
''' + "".join(f'<rect x="{x}" y="{y}" width="34" height="34" rx="5" fill="{col}" stroke="none"/>' for x, y, col in
              [(222, 350, C), (294, 350, M), (222, 420, M), (294, 420, C), (222, 490, C), (294, 490, M),
               (440, 230, S), (520, 230, C), (440, 300, C), (520, 300, C), (440, 370, C), (520, 370, S), (440, 440, M), (520, 440, C), (440, 510, C), (520, 510, M),
               (690, 410, C), (750, 410, M), (690, 480, M), (750, 480, C)]) + f'''
<path d="M960 600V330M936 330h48M948 330v-60h24v60" stroke="{C}" stroke-width="6"/>
<ellipse cx="960" cy="232" rx="42" ry="46" stroke="{S}" stroke-width="6"/><path d="M930 215c16 10 44 10 60 0M960 186v-40" stroke="{S}" stroke-width="5"/>
<path d="M510 190v-70h70l-16 22 16 22h-70" stroke="{S}" stroke-width="5" fill="rgba(247,166,0,.35)"/>''',
    "sri-lanka-for-startups": f'''
<path d="M120 600C260 520 420 420 560 300" stroke="{C}" stroke-width="6" stroke-dasharray="4 18"/>
<g transform="translate(700 250) rotate(38)">
<path d="M0-170c56 50 80 120 80 200v70h-160v-70c0-80 24-150 80-200z" stroke="{W}" stroke-width="7" fill="rgba(73,198,245,.12)"/>
<circle cx="0" cy="-30" r="30" stroke="{S}" stroke-width="7"/>
<path d="M-80 60l-56 70 56-10M80 60l56 70-56-10" stroke="{W}" stroke-width="7"/>
<path d="M-34 110c0 50 34 90 34 90s34-40 34-90" stroke="{S}" stroke-width="7" fill="rgba(247,166,0,.4)"/>
</g>
''' + "".join(f'<path d="M{x} {y - r}v{2 * r}M{x - r} {y}h{2 * r}" stroke="{col}" stroke-width="4"/>' for x, y, r, col in [(220, 200, 16, W), (980, 480, 18, S), (1040, 160, 12, C), (330, 420, 10, C), (880, 580, 10, W)]),
}


def svg(key):
    h = sum(ord(c) for c in key)
    tri = [("#f7a600", "M1200 0H980l220 220z"), ("#1eb2e6", "M0 900h200L0 700z"), ("#0f7d5c", "M1200 900V760l-140 140z"), ("#8d1b3d", "M0 0h150L0 150z")]
    facets = "".join(f'<path d="{d}" fill="{c}" opacity=".9"/>' for c, d in (tri[h % 4:] + tri[:h % 4])[:2])
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#ffffff" opacity=".10"/>' for x in range(60, 1200, 60) for y in range(60, 900, 60))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" width="1200" height="900">
<defs><radialGradient id="g" cx="50%" cy="38%" r="75%"><stop offset="0" stop-color="#12449f"/><stop offset=".55" stop-color="#082a66"/><stop offset="1" stop-color="#041532"/></radialGradient>
<filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="9" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
<rect width="1200" height="900" fill="url(#g)"/>{dots}{facets}
<g fill="none" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)">{SCENES[key]}</g>
</svg>
'''


def write_all(root):
    out = root / "assets" / "art"
    out.mkdir(parents=True, exist_ok=True)
    for k in SCENES:
        (out / f"{k}.svg").write_text(svg(k), encoding="utf-8")
