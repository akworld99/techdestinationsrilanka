#!/usr/bin/env python3
"""Tech Destination Sri Lanka: static site generator.

Run from the repo root:   python3 _build/build.py
Stories live in _build/content/*.txt (several stories per file, split by a line of =====).
Everything outside _build/ is generated output that GitHub Pages serves as is.
"""
import hashlib
import html
import json
import os
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import seo_data  # noqa: E402

# ---------------------------------------------------------------- settings
SITE_URL = "https://techdestinationsrilanka.lk"  # change when a custom domain is connected
SITE_NAME = "Tech Destination Sri Lanka"
TAGLINE = "Connecting the world to Sri Lanka's technology ecosystem"
LINKEDIN = "https://www.linkedin.com/company/tech-destination-sri-lanka/"
INSTAGRAM = "https://www.instagram.com/techdestination_srilanka/"
GA_ID = "G-X888MY82H5"   # Google Analytics measurement ID
INDEXNOW_KEY = "7c1e5a9d3b8f4e62a0d7c4b19f3e8a56"
FOLLOWERS = "7,800+"     # LinkedIn followers, shown on the services and talent pages
BOOKING_URL = ""          # Cal.com or Calendly link. Leave empty to hide the booking button.
FORM_ENDPOINT = "https://formspree.io/f/maeqjjvw"        # Formspree endpoint, e.g. https://formspree.io/f/abcdwxyz. Leave empty to hide the form.

SEO_TITLES = {'creative-software': "Creative Software: Sri Lankan engineers behind Norway's health records", 'roar-global': "Roar Global: Sri Lanka's first AI gateway, built in Colombo", 'xeynergy': 'Xeynergy: bootstrapped Sri Lankan AI software company', 'frontwalker': "Frontwalker Sri Lanka: a Swedish group's global tech center", 'superloop': 'Superloop Sri Lanka: 24x7 network operations from Colombo', 'igt1-lanka': "IGT1 Lanka: IFS owners' new tech company in Port City Colombo", 'synopsys': 'Synopsys Sri Lanka: chip design software R&D in Colombo', 'michelin': 'Michelin Sri Lanka: IT hub for Asia at Orion City, Colombo', 'tiqri': 'Tiqri: Norwegian software company engineering from Colombo', 'healthrecon-connect': 'HealthRecon Connect: US healthcare operations run from Sri Lanka', 'zebra-technologies': 'Zebra Technologies Lanka: software R&D center in Colombo', 'gapstars': 'Gapstars: Dutch founded engineering teams built in Sri Lanka', 'simcentric': 'SimCentric: simulation software engineered in Colombo', 'rootcode': "Rootcode: Sri Lankan company building Estonia's AI platforms", 'infomate': 'Infomate: finance and accounting services from Sri Lanka', 'wealthos': 'WealthOS: Sri Lankan founded platform acquired by JPMorganChase', 'startup-genome-2026': "Sri Lanka in Startup Genome's 2026 ecosystem rankings", 'orion-city': "Orion City: Sri Lanka's IT park with 85+ tech companies", 'dijital-team': 'Dijital Team: Australian company with 200 people in Colombo', 'codegen': 'CodeGen: travelbox, Vega supercar and ChargeNET from Colombo', 'inivos': 'Inivos: Sri Lankan engineers on European automotive software', 'surge-global': 'Surge Global: Colombo company with a Qatar government contract', 'oceans': 'Oceans: Sri Lankan talent for 600+ US startups', 'ey-gds': 'EY Global Delivery Services in Sri Lanka: 500+ staff', 'virtusa': 'Virtusa: from Colombo to Nasdaq and a $2 billion acquisition', 'wns': 'WNS Sri Lanka: 20 years of delivery from Colombo', 'sysco-labs': "Sysco LABS Sri Lanka: Sysco's core software built in Colombo", 'wso2': 'WSO2: Colombo built software company sold for $600 million', 'why-global-companies-choose-sri-lanka': 'Why IFS, HCLTech, EY and Sysco build in Sri Lanka', 'universities': "Universities behind Sri Lanka's software engineering talent", 'it-bpm-exports-2025': 'Sri Lanka IT and BPM exports: $1.645 billion in 2025', 'millenniumit': 'MillenniumIT: the Colombo company behind the LSE trading platform'}

CATEGORIES = {
    "built": ("Built by Sri Lankans", "Companies founded or led by Sri Lankan talent that compete globally."),
    "global": ("Global companies in Sri Lanka", "International companies that run engineering and operations from Sri Lanka."),
    "ecosystem": ("Ecosystem and data", "Rankings, export numbers and the talent pipeline."),
}

e = html.escape


# ---------------------------------------------------------------- content
def parse_stories():
    stories = []
    for f in sorted((HERE / "content").glob("*.txt")):
        for block in re.split(r"^=====\s*$", f.read_text(encoding="utf-8"), flags=re.M):
            block = block.strip()
            if not block:
                continue
            head, body = block.split("\n---\n", 1)
            s = {}
            for line in head.splitlines():
                k, v = line.split(":", 1)
                s[k.strip()] = v.strip()
            s["facts"] = [tuple(p.strip() for p in x.split("::")) for x in s.get("facts", "").split("||") if x.strip()]
            s["sources"] = [tuple(p.strip() for p in x.split("=>")) for x in s.get("sources", "").split("||") if x.strip()]
            s["date"] = date.fromisoformat(s["date"])
            s["body"] = body.strip()
            s["catname"] = CATEGORIES[s["category"]][0]
            stories.append(s)
    stories.sort(key=lambda s: s["date"], reverse=True)
    slugs = [s["slug"] for s in stories]
    assert len(slugs) == len(set(slugs)), "duplicate slug"
    return stories


def render_body(text):
    out = []
    for para in re.split(r"\n\s*\n", text):
        para = para.strip()
        if not para:
            continue
        if para.startswith("## "):
            out.append(f"<h2>{e(para[3:])}</h2>")
        elif para.startswith("> "):
            lines = [l[2:].strip() for l in para.splitlines()]
            cite = f"<cite>{e(lines[1])}</cite>" if len(lines) > 1 else ""
            out.append(f"<blockquote><p>{e(lines[0])}</p>{cite}</blockquote>")
        else:
            out.append(f"<p>{e(para)}</p>")
    return "\n".join(out)


def plain(text, limit=None):
    t = re.sub(r"^(## |> )", "", text, flags=re.M)
    t = re.sub(r"\s+", " ", t).strip()
    return t if not limit or len(t) <= limit else t[:limit].rsplit(" ", 1)[0] + "…"


def fdate(d):
    return f"{d.day} {d.strftime('%B %Y')}"


def read_minutes(s):
    return max(1, round(len(s["body"].split()) / 220))


# ---------------------------------------------------------------- covers
PALETTES = {
    "built": dict(bg=(11, 60, 145), facets=[(247, 166, 0), (233, 78, 27), (21, 151, 110), (30, 178, 230), (141, 27, 61)], text=(255, 255, 255), sub=(255, 205, 110)),
    "global": dict(bg=(7, 36, 92), facets=[(30, 178, 230), (21, 151, 110), (247, 166, 0), (233, 78, 27), (11, 96, 190)], text=(255, 255, 255), sub=(150, 214, 245)),
    "ecosystem": dict(bg=(247, 166, 0), facets=[(11, 60, 145), (141, 27, 61), (233, 78, 27), (21, 151, 110), (7, 36, 92)], text=(7, 36, 92), sub=(96, 44, 10)),
}


def make_cover(s, path):
    from PIL import Image, ImageDraw, ImageFont
    W, H = 1200, 630
    p = PALETTES[s["category"]]
    im = Image.new("RGB", (W, H), p["bg"])
    d = ImageDraw.Draw(im)
    h = int(hashlib.md5(s["slug"].encode()).hexdigest(), 16)
    f = p["facets"][h % 5:] + p["facets"][:h % 5]
    # tangram block echoing the logo mark: a square split along its diagonal into facets
    x0, y0, u = 70, 95, 220
    A, B, C, D_ = (x0, y0), (x0 + 2 * u, y0), (x0, y0 + 2 * u), (x0 + 2 * u, y0 + 2 * u)
    M = (x0 + u, y0 + u)
    g = 9  # gap between facets

    def poly(pts, col):
        cx = sum(q[0] for q in pts) / len(pts)
        cy = sum(q[1] for q in pts) / len(pts)
        pts = [(q[0] + (cx - q[0]) * g / 110, q[1] + (cy - q[1]) * g / 110) for q in pts]
        d.polygon(pts, fill=col)

    layouts = [
        [([A, B, M], 0), ([B, D_, M], 1), ([A, M, (x0, y0 + u)], 2), ([(x0, y0 + u), M, C], 3), ([C, M, D_], 4)],
        [([A, (x0 + u, y0), M], 0), ([(x0 + u, y0), B, M], 1), ([B, D_, M], 2), ([A, M, C], 3), ([C, M, D_], 4)],
        [([A, B, M], 0), ([B, (x0 + 2 * u, y0 + u), M], 1), ([(x0 + 2 * u, y0 + u), D_, M], 2), ([A, M, C], 3), ([C, M, D_], 4)],
    ]
    for pts, ci in layouts[(h >> 4) % 3]:
        poly(pts, f[ci])

    def font(size, weight):
        ft = ImageFont.truetype(str(HERE / "fonts" / "Manrope.ttf"), size)
        ft.set_variation_by_axes([weight])
        return ft

    big = s.get("cover") or s.get("company") or s["facts"][0][0]
    small = s["sector"] if s.get("company") else s["facts"][0][1]
    tx, maxw = 580, W - 580 - 70
    size = 104
    while True:
        ft = font(size, 800)
        words, lines, cur = big.split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if d.textlength(t, font=ft) <= maxw or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
        if (len(lines) <= 3 and all(d.textlength(l, font=ft) <= maxw for l in lines)) or size <= 54:
            break
        size -= 6
    lh = int(size * 1.08)
    sf = font(34, 600)
    total = lh * len(lines) + 26 + 44
    y = (H - total) // 2 - 6
    for l in lines:
        d.text((tx, y), l, font=ft, fill=p["text"])
        y += lh
    y += 26
    # wrap the small line
    words, cur, sl = small.split(), "", []
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=sf) <= maxw or not cur:
            cur = t
        else:
            sl.append(cur)
            cur = w
    sl.append(cur)
    for l in sl[:2]:
        d.text((tx, y), l, font=sf, fill=p["sub"])
        y += 44
    d.text((70, H - 62), SITE_NAME, font=font(24, 700), fill=p["text"])
    im.save(path, "JPEG", quality=84, optimize=True, progressive=True)


def make_brand_assets():
    from PIL import Image, ImageDraw, ImageFont
    src = Image.open(HERE / "logo-source.png").convert("RGB")
    logo = src.crop((170, 200, 1335, 740))
    logo.resize((int(logo.width * 200 / logo.height), 200), Image.LANCZOS).save(ROOT / "assets" / "logo.png", optimize=True)
    mark = src.crop((185, 215, 540, 725))
    side = max(mark.size) + 40
    sq = Image.new("RGB", (side, side), (255, 255, 255))
    sq.paste(mark, ((side - mark.width) // 2, (side - mark.height) // 2))
    sq.resize((180, 180), Image.LANCZOS).save(ROOT / "assets" / "apple-touch-icon.png", optimize=True)
    sq.resize((48, 48), Image.LANCZOS).save(ROOT / "assets" / "favicon.png", optimize=True)
    # default share image
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), (255, 255, 255))
    lg = logo.resize((int(logo.width * 330 / logo.height), 330), Image.LANCZOS)
    im.paste(lg, ((W - lg.width) // 2, 110))
    d = ImageDraw.Draw(im)
    ft = ImageFont.truetype(str(HERE / "fonts" / "Manrope.ttf"), 34)
    ft.set_variation_by_axes([600])
    tw = d.textlength(TAGLINE, font=ft)
    d.text(((W - tw) / 2, 480), TAGLINE, font=ft, fill=(11, 60, 145))
    d.rectangle([0, H - 14, W, H], fill=(247, 166, 0))
    im.save(ROOT / "assets" / "share.jpg", "JPEG", quality=86, optimize=True)


# ---------------------------------------------------------------- templates
LANDMARKS = """<svg class="landmarks" viewBox="0 0 1200 300" role="img" aria-label="Line drawing of Sigiriya, the Colombo Lotus Tower and the Nine Arch Bridge" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
<path d="M0 262h1200" />
<path d="M60 262c24-10 40-34 58-72 8-18 14-58 34-74 12-10 40-14 96-14 54 0 86 2 100 14 18 16 22 52 32 74 16 36 34 60 62 72" />
<path d="M150 118c30 8 170 8 198 0M132 176c20 10 60 14 100 14M290 190c30-2 60-6 78-14M196 262v-30h24v30M226 232l10-22 10 22" />
<path d="M40 262c4-16 2-30-4-40M40 232c-10-8-22-8-30-2M40 232c10-10 22-10 32-4M40 236c-6-12-4-22 2-30" />
<path d="M470 262c4-18 2-34-6-48M468 222c-12-10-26-10-36-2M468 222c12-12 28-12 38-4M468 226c-8-14-6-26 2-36" />
<path d="M600 262V96M624 262V96M600 96h24M592 262h40" />
<path d="M612 96V70" />
<path d="M576 70c0-22 16-40 36-40s36 18 36 40c0 14-10 26-36 26s-36-12-36-26z" />
<path d="M588 50c8 6 40 6 48 0M582 66c12 8 48 8 60 0M612 30V8" />
<path d="M604 140h16M604 180h16M604 220h16" />
<path d="M700 262v-52h26v52M726 262v-84h30v84M756 262v-40h22v40M540 262v-36h24v36M516 262v-58h24v58" />
<path d="M820 150h380M820 150v112M820 164h380" />
<path d="M840 262v-52c0-20 12-34 30-34s30 14 30 34v52M920 262v-52c0-20 12-34 30-34s30 14 30 34v52M1000 262v-52c0-20 12-34 30-34s30 14 30 34v52M1080 262v-52c0-20 12-34 30-34s30 14 30 34v52M1160 262v-52c0-20 12-34 30-34" />
<path d="M900 150v-14h70v14M916 136v-8h38v8M980 150v-12h60v12M1050 150v-12h60v12" />
<path d="M790 262c-2-30 6-60 30-84M1196 100c-30 6-50 22-60 50" />
</svg>"""


def page(title, desc, body, prefix, path, image=None, extra_head="", article=False, active="", seo_title=None):
    url = f"{SITE_URL}/{path}".rstrip("/") + ("/" if not path.endswith(".html") else "")
    if path == "":
        url = SITE_URL + "/"
    img = f"{SITE_URL}/{image or 'assets/share.jpg'}"
    title_tag = seo_title or title
    full_title = title_tag if (title_tag == SITE_NAME or len(title_tag) > 42) else f"{title_tag} | {SITE_NAME}"

    def nav(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{prefix}{href}"{cur}>{label}</a>'

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:type" content="{'article' if article else 'website'}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('consent','default',{{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'granted'}});
gtag('consent','default',{{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',region:['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE','IS','LI','NO','GB','CH'],wait_for_update:500}});
try{{var c=localStorage.getItem('tdsl-consent');if(c)gtag('consent','update',{{analytics_storage:c}});}}catch(e){{}}
gtag('js',new Date());gtag('config','{GA_ID}');</script>
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<link rel="icon" type="image/png" href="{prefix}assets/favicon.png">
<link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">
<link rel="alternate" type="application/rss+xml" title="{SITE_NAME} stories" href="{SITE_URL}/feed.xml">
<link rel="preload" href="{prefix}assets/fonts/manrope.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{prefix}assets/styles.css">
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="{prefix}index.html" aria-label="{SITE_NAME} home"><img src="{prefix}assets/logo.png" alt="{SITE_NAME}" width="431" height="200"></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav id="nav" class="nav" aria-label="Main">
      {nav('stories/', 'Stories', 'stories')}
      {nav('companies/', 'Companies', 'companies')}
      {nav('why-sri-lanka/', 'Why Sri Lanka', 'why')}
      {nav('talent/', 'Talent', 'talent')}
      {nav('services/', 'Services', 'services')}
      {nav('guides/', 'Guides', 'guides')}
      {nav('about/', 'About', 'about')}
      <a class="btn btn-small" href="{prefix}talent/find/">Find talent</a>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap foot">
    <div class="foot-brand">
      <p class="foot-name">{SITE_NAME}</p>
      <p>{TAGLINE}.</p>
      <p class="fine">We are an independent media platform. We are not a government body and we do not speak for one.</p>
    </div>
    <div>
      <p class="foot-h">Read</p>
      <a href="{prefix}stories/">Stories</a>
      <a href="{prefix}companies/">Companies</a>
      <a href="{prefix}why-sri-lanka/">Why Sri Lanka</a>
      <a href="{prefix}guides/sri-lanka-tech-industry-facts/">Industry facts</a>
      <a href="{prefix}tech-50/">Sri Lanka Tech 50</a>
      <a href="{prefix}about/">About</a>
    </div>
    <div>
      <p class="foot-h">For companies</p>
      <a href="{prefix}talent/find/">Find talent</a>
      <a href="{prefix}hire/">Hire by role</a>
      <a href="{prefix}solutions/">Ways to build</a>
      <a href="{prefix}services/">Services</a>
      <a href="{prefix}guides/sri-lanka-tech-salaries/">Salary guide</a>
      <a href="{prefix}guides/how-to-hire-in-sri-lanka/">How to hire</a>
      <a href="{prefix}guides/set-up-a-company-in-sri-lanka/">Set up a company</a>
      <a href="{prefix}tech-tour/">Tech Tour</a>
      <a href="{prefix}get-featured/">Get featured</a>
    </div>
    <div>
      <p class="foot-h">For professionals</p>
      <a href="{prefix}talent/top-talent/">Be featured as Top Talent</a>
      <a href="{LINKEDIN}" rel="noopener">LinkedIn</a>
      <a href="{INSTAGRAM}" rel="noopener">Instagram</a>
      <a href="{prefix}featured-badge/">Featured badge</a>
      <a href="{prefix}contact/">Contact</a>
      <a href="{prefix}privacy/">Privacy</a>
    </div>
  </div>
  <div class="wrap foot-hubs">
    <p><strong>By industry</strong> {' '.join(f'<a href="{prefix}why-sri-lanka/{v["slug"]}/">{v["label"]}</a>' for v in seo_data.VERTICALS)}</p>
    <p><strong>Ways to build</strong> {' '.join(f'<a href="{prefix}solutions/{x["slug"]}/">{x["label"]}</a>' for x in solutions.SOLUTIONS)}</p>
    <p><strong>By country</strong> {' '.join(f'<a href="{prefix}hire-from/{m["slug"]}/">{m["label"]}</a>' for m in seo_data.MARKETS)}</p>
  </div>
  <div class="wrap news">
    <form class="newsletter" data-form="newsletter" data-done="You are on the list." action="{e(FORM_ENDPOINT)}" method="POST">
      <label for="nl-email"><strong>New stories by email.</strong> One short email when we publish. No spam.</label>
      <div class="nl-row"><input id="nl-email" type="email" name="email" placeholder="you@company.com" required><input type="hidden" name="form" value="newsletter"><button class="btn btn-saffron" type="submit">Subscribe</button></div>
      <p class="form-status" role="status"></p>
    </form>
  </div>
  <div class="wrap legal">© {date.today().year} {SITE_NAME}. Company names and trademarks belong to their owners.</div>
</footer>
<div class="consent" id="consent" hidden><p>We use analytics cookies to see which pages are read. <a href="{prefix}privacy/">Privacy</a></p><div><button class="btn btn-small" data-consent="granted">Accept</button><button class="btn btn-small btn-ghost" data-consent="denied">Decline</button></div></div>
<script src="{prefix}assets/app.js" defer></script>
</body>
</html>
"""


def card(s, prefix, size=""):
    return f"""<article class="card {size}" data-type="{s['category']}" data-text="{e((s['title'] + ' ' + s.get('company', '') + ' ' + s['sector']).lower())}">
  <a class="card-cover" href="{prefix}stories/{s['slug']}/" tabindex="-1" aria-hidden="true"><img src="{prefix}assets/covers/{s['slug']}.jpg" alt="" width="1200" height="630" loading="lazy"></a>
  <div class="card-body">
    <p class="meta"><span class="tag tag-{s['category']}">{e(s['catname'])}</span><time datetime="{s['date'].isoformat()}">{fdate(s['date'])}</time></p>
    <h3><a href="{prefix}stories/{s['slug']}/">{e(s['title'])}</a></h3>
    {f'<p class="dek">{e(s["dek"])}</p>' if size else ''}
  </div>
</article>"""


def logo(s, prefix, cls="logo"):
    """Company logo if _build/logos/<slug>.png exists, otherwise nothing."""
    if (HERE / "logos" / f"{s['slug']}.png").exists():
        return f'<img class="{cls}" src="{prefix}assets/logos/{s['slug']}.png" alt="" width="96" height="96" loading="lazy">'
    return ""


def doors(prefix):
    items = [
        ("hire", "Hire", "Add Sri Lankan engineers to your own team. We point you to people and partners who have done it before."),
        ("setup", "Set up", "Open your own engineering centre in Colombo. Entity, Board of Investment and Port City options, explained by people on the ground."),
        ("recruit", "Recruit at scale", "Build a team of 20 or 200. We connect you with recruiters and employers of record who do this every week."),
    ]
    return "".join(
        f'<a class="door" href="{prefix}{"talent/find/" if k == "hire" else "contact/?need=" + k}" data-need="{k}"><h3>{t}</h3><p>{d}</p><span class="door-go">{"Find talent" if k == "hire" else "Start a conversation"}</span></a>' for k, t, d in items
    )


def build_home(stories):
    lead, rest = stories[0], stories[1:7]
    companies = sorted({s["company"] for s in stories if s.get("company")}, key=str.lower)
    numbers = [
        ("$1.645B", "IT and BPM export revenue in 2025", "it-bpm-exports-2025"),
        ("120,000+", "IT professionals", "it-bpm-exports-2025"),
        ("#3 in Asia", "for affordable tech talent, Startup Genome 2026", "startup-genome-2026"),
        ("12,000+", "ICT graduates every year", "startup-genome-2026"),
    ]
    svc = [
        ("hire", "Hire talent", "Engineers, specialists and finance professionals added to your own team, as employees or contractors.", "talent/find/", "Find talent"),
        ("partner", "Find a delivery partner", "A Sri Lankan company that has built your kind of product before, matched from the ones we have reported on.", "solutions/software-outsourcing-sri-lanka/", "How outsourcing works"),
        ("setup", "Set up your own centre", "Company registration, Board of Investment and Port City options, with introductions to advisers on the ground.", "solutions/offshore-development-center-sri-lanka/", "Plan a centre"),
        ("recruit", "Recruit at scale", "Twenty people or two hundred, through recruiters and campus pipelines that hire for global tech companies.", "contact/?need=recruit", "Start recruiting"),
    ]
    ICN = {'hire': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.6-3.6 3.2-5.5 6.5-5.5s5.9 1.9 6.5 5.5"/><path d="M18 8v6M15 11h6"/>', 'partner': '<path d="M3 8l4-3 5 3 5-3 4 3v8l-4 3-5-3-5 3-4-3z"/><path d="M12 8v8"/>', 'setup': '<path d="M4 21V6l8-3 8 3v15"/><path d="M9 21v-5h6v5M8 9h2M14 9h2M8 12.5h2M14 12.5h2"/>', 'recruit': '<circle cx="8" cy="9" r="3"/><circle cx="17" cy="10" r="2.4"/><path d="M2 20c.5-3.3 2.8-5 6-5s5.5 1.7 6 5"/><path d="M15.5 15.2c3.2-.4 5.6 1.2 6.2 4.3"/>'}
    ind_tiles, ctry_cards = seo_pages.hub_blocks("", stories)
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <h1>Sri Lanka. The underdog tech economy powering global software.</h1>
      <p class="lede">We help companies abroad hire Sri Lankan engineers, find delivery partners and set up their own teams. Our newsroom shows you the proof first: {len(stories)} sourced stories about what this talent has already built.</p>
      <div class="actions">
        <a class="btn" href="talent/find/">Find talent</a>
        <a class="btn btn-ghost" href="services/">See what we do</a>
      </div>
      <p class="hero-trust"><span><b>{len(companies)}</b> companies featured</span><span><b>{FOLLOWERS}</b> LinkedIn followers</span><span><b>{len(seo_pages.MARKETS)}</b> markets covered</span></p>
    </div>
    <div class="hero-lead">
      {card(lead, "", "lead")}
    </div>
  </div>
  <div class="wrap">{LANDMARKS}</div>
</section>

<section class="section svc-home">
  <div class="wrap">
    <div class="section-head"><h2>What we do for companies building in Sri Lanka</h2><a class="more" href="services/">All services</a></div>
    <div class="svc4">
      {''.join(f'<a class="svc-card" href="{h}"><span class="ind-ic"><svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICN[k]}</svg></span><h3>{t_}</h3><p>{d}</p><span class="door-go">{c}</span></a>' for k, t_, d, h, c in svc)}
    </div>
    <ol class="flow"><li><b>Tell us what you need</b> Roles, team size and timeline.</li><li><b>We match you</b> People, partners or advisers from the ecosystem we report on.</li><li><b>You decide</b> You talk to them directly and choose.</li></ol>
  </div>
</section>

<section class="band">
  <div class="wrap numbers">
    {''.join(f'<a class="num" href="stories/{slug}/"><strong>{e(v)}</strong><span>{e(l)}</span></a>' for v, l, slug in numbers)}
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head"><h2>Who already builds in Sri Lanka</h2><a class="more" href="why-sri-lanka/">The full case</a></div>
    <p class="hub-l">By industry</p>
    {ind_tiles}
    <p class="hub-l mt">By country</p>
    {ctry_cards}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Five ways to build your team</h2><a class="more" href="solutions/">Compare them</a></div>
    {solutions.tiles("")}
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head"><h2>The proof, in stories</h2><a class="more" href="stories/">All {len(stories)} stories</a></div>
    <div class="grid">
      {''.join(card(s, "") for s in rest)}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="duo">
      <a class="duo-card duo-blue" href="talent/find/">
        <p class="duo-for">For companies</p>
        <h2>Find talent from Sri Lanka</h2>
        <p>Tell us the role. We introduce engineers, specialists or whole teams who have already delivered for global companies.</p>
        <span class="btn btn-saffron">Find talent</span>
      </a>
      <a class="duo-card duo-saffron" href="talent/top-talent/">
        <p class="duo-for">For professionals</p>
        <h2>Be featured as Sri Lankan Top Talent</h2>
        <p>Want to be hired by a global company? Apply for a featured profile and get seen by the founders and hiring managers who follow us.</p>
        <span class="btn">Apply to be featured</span>
      </a>
    </div>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head"><h2>Numbers before you decide</h2><a class="more" href="guides/">All guides</a></div>
    <div class="doors wrap3">
      <a class="door" href="guides/sri-lanka-tech-salaries/"><h3>Salary and cost guide</h3><p>What engineers earn in Colombo in 2026 and what an employee costs on top, with sources.</p><span class="door-go">See the numbers</span></a>
      <a class="door" href="guides/how-to-hire-in-sri-lanka/"><h3>How to hire</h3><p>Employer of record, contractors, a partner team or your own company, compared.</p><span class="door-go">Compare routes</span></a>
      <a class="door" href="guides/set-up-a-company-in-sri-lanka/"><h3>Set up a company</h3><p>Registration, ownership, tax, the Board of Investment and Port City Colombo.</p><span class="door-go">Read the guide</span></a>
      <a class="door" href="tech-tour/"><h3>Sri Lanka Tech Tour</h3><p>Three days in Colombo meeting the companies and people in our stories.</p><span class="door-go">Register interest</span></a>
      <a class="door" href="tech-50/"><h3>Sri Lanka Tech 50</h3><p>Our annual fact checked list. Nominations for the first edition are open.</p><span class="door-go">Nominate a company</span></a>
      <a class="door" href="guides/sri-lanka-tech-industry-facts/"><h3>Industry facts</h3><p>Exports, workforce, graduates, rankings and exits, each with its source.</p><span class="door-go">Check the facts</span></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>{len(companies)} companies featured so far</h2><a class="more" href="companies/">Open the directory</a></div>
    <ul class="names">
      {''.join(f'<li><a href="stories/{s["slug"]}/">{logo(s, "")}{e(s["company"])}</a></li>' for s in sorted([s for s in stories if s.get("company")], key=lambda s: s["company"].lower()))}
    </ul>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head"><h2>Live from our LinkedIn</h2><a class="more" href="{LINKEDIN}" rel="noopener">Follow {FOLLOWERS} others</a></div>
    <div class="li-row">
      {''.join(f'<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:{s["linkedin"]}?collapsed=1" height="600" frameborder="0" allowfullscreen loading="lazy" title="LinkedIn post: {e(s["title"])}"></iframe>' for s in stories[:3])}
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap cta-in">
    <h2>Ready to build in Sri Lanka?</h2>
    <p>Tell us the roles, the team size and the timeline. We will introduce the people, partners or advisers who fit.</p>
    <div class="actions"><a class="btn btn-saffron" href="talent/find/">Find talent</a><a class="btn btn-ondark" href="contact/">Talk to us</a><a class="btn btn-ondark" href="get-featured/">Get your company featured</a></div>
  </div>
</section>
"""
    ld = [{"@context": "https://schema.org", "@type": "NewsMediaOrganization", "name": SITE_NAME, "url": SITE_URL + "/", "logo": f"{SITE_URL}/assets/logo.png", "sameAs": [LINKEDIN, INSTAGRAM], "description": TAGLINE,
           "areaServed": ["LK", "US", "GB", "SE", "NO", "DK", "FI", "NL", "DE", "AU", "AE", "OM", "SA", "QA"], "knowsAbout": ["Sri Lanka technology industry", "software engineering talent", "IT outsourcing", "global capability centres"]},
          {"@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME, "url": SITE_URL + "/"},
          {"@context": "https://schema.org", "@type": "Organization", "name": SITE_NAME, "url": SITE_URL + "/", "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
              {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": SITE_URL + "/" + u, "areaServed": "Worldwide"}} for n, u in [
                  ("Tech talent sourcing in Sri Lanka", "talent/find/"), ("Software outsourcing partner matching in Sri Lanka", "solutions/software-outsourcing-sri-lanka/"),
                  ("Dedicated development teams in Sri Lanka", "solutions/dedicated-development-team-sri-lanka/"), ("IT staff augmentation in Sri Lanka", "solutions/staff-augmentation-sri-lanka/"),
                  ("Offshore development centre setup in Sri Lanka", "solutions/offshore-development-center-sri-lanka/")]]}}]
    head = f'<script type="application/ld+json">{json.dumps(ld)}</script>'
    desc = "Hire Sri Lankan tech talent, find a software outsourcing partner or set up your own team. Backed by sourced stories on what Sri Lankan engineers have built."
    write("index.html", page(SITE_NAME, desc, body, "", "", extra_head=head, seo_title="Tech Destination Sri Lanka: hire tech talent and build teams"))


def build_stories_index(stories):
    filters = '<button class="chip is-on" data-filter="all">All</button>' + "".join(
        f'<button class="chip" data-filter="{k}">{v[0]}</button>' for k, v in CATEGORIES.items()
    )
    body = f"""
<section class="page-head">
  <div class="wrap">
    <h1>Stories</h1>
    <p class="lede">{len(stories)} sourced stories about what Sri Lankan tech talent has built, and who is building here.</p>
    <div class="filters" role="group" aria-label="Filter stories">
      {filters}
      <label class="search"><span class="sr">Search stories</span><input type="search" id="q" placeholder="Search by company or topic"></label>
    </div>
  </div>
</section>
<section class="section top-0">
  <div class="wrap">
    <div class="grid" id="list">
      {''.join(card(s, "../") for s in stories)}
    </div>
    <p class="empty" id="empty" hidden>No stories match that search. Try a company name, or clear the filter.</p>
  </div>
</section>
"""
    write("stories/index.html", page("Sri Lankan tech stories: companies, founders and data", f"All {len(stories)} stories from {SITE_NAME}: Sri Lankan built companies, global companies in Sri Lanka, and ecosystem data.", body, "../", "stories/", active="stories"))


def build_story(s, stories):
    i = stories.index(s)
    same = [x for x in stories if x is not s and x["category"] == s["category"]]
    related = (same[:3] if len(same) >= 3 else same + [x for x in stories if x is not s and x not in same][: 3 - len(same)])
    facts = "".join(f"<div><dt>{e(v)}</dt><dd>{e(l)}</dd></div>" for v, l in s["facts"])
    sources = "".join(f'<li><a href="{e(u)}" rel="noopener nofollow">{e(l)}</a></li>' for l, u in s["sources"])
    li = f"https://www.linkedin.com/feed/update/urn:li:activity:{s['linkedin']}/" if s.get("linkedin") else LINKEDIN
    post_fig = ""
    if s.get("linkedin"):
        post_fig = (f'<section class="li-live"><h2>Live on LinkedIn</h2><p class="cap">The original post, with current reactions and comments.</p>'
                    f'<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:activity:{s["linkedin"]}?collapsed=1" height="640" width="504" frameborder="0" allowfullscreen loading="lazy" title="LinkedIn post: {e(s["title"])}"></iframe>'
                    f'<p class="cap"><a href="{li}" rel="noopener">Open the post on LinkedIn</a></p></section>')
    note = f'<p class="note"><strong>Update.</strong> {e(s["note"])}</p>' if s.get("note") else ""
    body = f"""
<article class="story">
  <header class="story-head">
    <div class="wrap narrow">
      <p class="crumb"><a href="../">Stories</a> <span aria-hidden="true">/</span> <a href="../?type={s['category']}">{e(s['catname'])}</a></p>
      <h1>{e(s['title'])}</h1>
      <p class="lede">{e(s['dek'])}</p>
      <div class="byline">{logo(s, '../../', 'by-logo') if s.get('company') else ''}<p class="meta"><time datetime="{s['date'].isoformat()}">{fdate(s['date'])}</time><span>{read_minutes(s)} min read</span><span>{e(s['sector'])}</span></p></div>
    </div>
  </header>
  <div class="wrap narrow">
    <img class="story-cover" src="../../assets/covers/{s['slug']}.jpg" alt="" width="1200" height="630">
    <dl class="facts">{facts}</dl>
    {note}
    <div class="prose">
{render_body(s['body'])}
    </div>
    {f'<section class="sources"><h2>Sources</h2><ul>{sources}</ul></section>' if sources else ''}
    {post_fig}
    {('<p class="rel">Related: ' + ' '.join(f'<a href="../../{p}">{e(l)}</a>' for l, p in seo_pages.related_for(s['slug'])) + '</p>') if seo_pages.related_for(s['slug']) else ''}
    <div class="story-actions">
      <a class="btn btn-ghost" href="{li}" rel="noopener">Join the discussion on LinkedIn</a>
      <button class="btn btn-ghost" data-copy>Copy link</button>
    </div>
  </div>
</article>

<section class="section tint">
  <div class="wrap">
    <div class="section-head"><h2>Want a team like this one?</h2></div>
    <div class="doors">{doors("../../")}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Keep reading</h2><a class="more" href="../">All stories</a></div>
    <div class="grid">{''.join(card(x, "../../") for x in related)}</div>
  </div>
</section>
"""
    url = f"{SITE_URL}/stories/{s['slug']}/"
    ld = {
        "@context": "https://schema.org", "@type": "NewsArticle", "headline": s["title"][:110], "description": s["dek"],
        "datePublished": s["date"].isoformat(), "dateModified": date.today().isoformat() if s.get("note") else s["date"].isoformat(),
        "image": [f"{SITE_URL}/assets/covers/{s['slug']}.jpg"], "mainEntityOfPage": url,
        "author": {"@type": "Organization", "name": SITE_NAME, "url": SITE_URL + "/"},
        "publisher": {"@type": "Organization", "name": SITE_NAME, "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/assets/logo.png"}},
    }
    if s.get("company"):
        ld["about"] = {"@type": "Organization", "name": s["company"]}
    head = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n<meta property="article:published_time" content="{s["date"].isoformat()}">' + seo_pages.crumbs_ld(sys.modules[__name__], [("Stories", "stories/"), (s.get("company") or s["title"], f"stories/{s['slug']}/")])
    write(f"stories/{s['slug']}/index.html", page(s["title"], s["dek"], body, "../../", f"stories/{s['slug']}/", image=f"assets/covers/{s['slug']}.jpg", extra_head=head, article=True, active="stories", seo_title=SEO_TITLES.get(s["slug"])))


def build_companies(stories):
    cos = sorted([s for s in stories if s.get("company")], key=lambda s: s["company"].lower())
    rows = "".join(
        f"""<a class="co" href="../stories/{s['slug']}/" data-type="{s['category']}" data-text="{e((s['company'] + ' ' + s['sector'] + ' ' + s['blurb']).lower())}">
  {logo(s, '../', 'co-logo') or f'<span class="co-mark co-{s["category"]}" aria-hidden="true">' + e(''.join(w[0] for w in re.findall(r"[A-Za-z0-9]+", s['company'])[:2]).upper()) + '</span>'}
  <span class="co-main"><strong>{e(s['company'])}</strong><span>{e(s['blurb'])}</span></span>
  <span class="co-side"><span class="tag tag-{s['category']}">{'Sri Lankan built' if s['category'] == 'built' else 'Global company'}</span><span class="co-sector">{e(s['sector'])}</span></span>
</a>""" for s in cos
    )
    nb = sum(1 for s in cos if s["category"] == "built")
    body = f"""
<section class="page-head">
  <div class="wrap">
    <h1>Tech companies in Sri Lanka</h1>
    <p class="lede">Every company we have featured: {nb} built by Sri Lankans and {len(cos) - nb} global companies running engineering or operations from Sri Lanka. Each entry links to the full story and its sources.</p>
    <div class="filters" role="group" aria-label="Filter companies">
      <button class="chip is-on" data-filter="all">All {len(cos)}</button>
      <button class="chip" data-filter="built">Sri Lankan built</button>
      <button class="chip" data-filter="global">Global companies</button>
      <label class="search"><span class="sr">Search companies</span><input type="search" id="q" placeholder="Search by name or sector"></label>
    </div>
  </div>
</section>
<section class="section top-0">
  <div class="wrap">
    <div class="co-list" id="list">{rows}</div>
    <p class="empty" id="empty" hidden>No companies match that search. Try a different name or sector.</p>
  </div>
</section>
<section class="cta">
  <div class="wrap cta-in">
    <h2>Missing from this list?</h2>
    <p>If your company builds for global markets with Sri Lankan talent, we want to hear about it.</p>
    <a class="btn btn-saffron" href="../get-featured/">Get featured</a>
  </div>
</section>
"""
    write("companies/index.html", page("Tech companies in Sri Lanka: directory of featured companies", f"Directory of {len(cos)} technology companies in Sri Lanka featured by {SITE_NAME}: Sri Lankan built product companies and global firms with teams in Colombo.", body, "../", "companies/", active="companies"))


def build_about(stories):
    body = f"""
<section class="page-head">
  <div class="wrap narrow">
    <h1>About</h1>
    <p class="lede">Tech Destination Sri Lanka helps companies abroad hire talent and build teams in Sri Lanka. We lead with independent, sourced reporting, so founders, CTOs and investors can judge the talent on evidence before they talk to us.</p>
  </div>
</section>
<section class="section top-0">
  <div class="wrap narrow prose">
    <h2>What we do</h2>
    <p>Two things. We report on what Sri Lankan technology talent has built, with sources. And we help companies abroad act on it: <a href="../talent/find/">finding talent</a>, <a href="../solutions/software-outsourcing-sri-lanka/">matching delivery partners</a>, and <a href="../solutions/offshore-development-center-sri-lanka/">setting up their own teams</a>. The reporting is how most people find us. The <a href="../services/">services</a> are how we help once they do.</p>

    <h2>Why this exists</h2>
    <p>Sri Lankan engineers built the trading platform the London Stock Exchange bought. They write core R&D for IFS, Sysco and Synopsys. They founded WSO2 and Virtusa. Most of the world has never heard any of it.</p>
    <p>We started on LinkedIn in April 2026 to change that, one sourced story at a time. This site is the permanent home for those stories.</p>

    <h2>How we report</h2>
    <p>Credibility is the only asset a publication like this has. So we hold every story to the same rules.</p>
    <ul>
      <li>Every claim needs a source, and the sources are listed at the end of each story.</li>
      <li>We credit people. The story is what Sri Lankan engineers and founders did, never a slogan about a country.</li>
      <li>If we cannot verify a number, we ask the company or leave it out.</li>
      <li>One company, one story. No filler and no buzzwords.</li>
      <li>When facts change after publication, we update the story and say so.</li>
    </ul>

    <h2>Who it is for</h2>
    <p>Foreign founders, CTOs, hiring managers and investors who are deciding where to build their next team. If that is you, <a href="../contact/">tell us what you need</a> and we will point you to the right people.</p>

    <h2 id="feature">Get featured</h2>
    <p>We feature companies of every size as long as the story holds up, and we feature individual professionals through Sri Lankan Top Talent. <a href="../get-featured/">Suggest a company</a> or <a href="../talent/top-talent/">apply as a professional</a>. Partner spotlights are available for companies that want a dedicated feature. They follow the same sourcing rules and are labelled as partner content.</p>

    <h2>What we are not</h2>
    <p>We are not a government body, an industry association or an investment promotion agency, and we do not speak for any of them.</p>
  </div>
</section>
"""
    write("about/index.html", page("About", "Who runs Tech Destination Sri Lanka, how we source and check every story, and how to suggest a company.", body, "../", "about/", active="about"))


def build_contact():
    booking = f'<a class="btn" href="{e(BOOKING_URL)}" rel="noopener">Book a 20 minute call</a>' if BOOKING_URL else ""
    import extra
    form = extra.form(sys.modules[__name__], "contact", "Send a message", "", [
        ("select", "need", "I want to", True, ["Hire Sri Lankan talent", "Find a delivery partner", "Set up in Sri Lanka", "Recruit at scale", "Feature my company", "Employer branding", "Events and delegations", "Something else"]),
        ("text", "name", "Your name", True, ""),
        ("email", "email", "Work email", True, ""),
        ("text", "company", "Company", False, ""),
        ("textarea", "message", "What do you need?", True, "Roles, team size, timeline, or the question you have"),
    ], "Send message", "Message sent. We will reply by email.")
    body = f"""
<section class="page-head">
  <div class="wrap narrow">
    <h1 id="contact-title">Contact</h1>
    <p class="lede" id="contact-lede">Tell us what you are trying to do. We will point you to the people, partners and companies who have done it before.</p>
  </div>
</section>
<section class="section top-0">
  <div class="wrap narrow">
    <div class="doors stack" id="needs">{doors("../")}</div>
    <div class="reach">
      <h2>Reach us</h2>
      <p>The fastest way to reach the team is a message to our LinkedIn page. Say which of the three you need, and roughly how many people or what timeline you have in mind.</p>
      <div class="actions">
        {booking}
        <a class="btn{' btn-ghost' if booking else ''}" href="{LINKEDIN}" rel="noopener">Message us on LinkedIn</a>
        <a class="btn btn-ghost" href="{INSTAGRAM}" rel="noopener">Instagram</a>
      </div>
    </div>
    {form}
  </div>
</section>
"""
    write("contact/index.html", page("Contact", "Hire Sri Lankan talent, find a delivery partner, set up in Sri Lanka or get featured. Tell us what you need.", body, "../", "contact/"))


def build_meta(stories, extra_pages=()):
    now = datetime.now(timezone.utc)
    urls = [("", date.today())] + [(p, date.today()) for p in ("stories/", "companies/", "about/", "contact/") + tuple(extra_pages)] + [(f"stories/{s['slug']}/", s["date"]) for s in stories]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE_URL}/{p}</loc><lastmod>{d.isoformat()}</lastmod></url>\n" for p, d in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "PerplexityBot", "Google-Extended", "Applebot-Extended", "Bingbot", "CCBot"]
    write("robots.txt", "User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {SITE_URL}/sitemap.xml\n")
    items = "".join(
        f"<item><title>{e(s['title'])}</title><link>{SITE_URL}/stories/{s['slug']}/</link><guid>{SITE_URL}/stories/{s['slug']}/</guid>"
        f"<pubDate>{datetime(s['date'].year, s['date'].month, s['date'].day, 6, tzinfo=timezone.utc).strftime('%a, %d %b %Y %H:%M:%S +0000')}</pubDate>"
        f"<description>{e(s['dek'])}</description></item>\n" for s in stories)
    write("feed.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>{SITE_NAME}</title><link>{SITE_URL}/</link>'
          f"<description>{e(TAGLINE)}</description><language>en</language><lastBuildDate>{now.strftime('%a, %d %b %Y %H:%M:%S +0000')}</lastBuildDate>\n{items}</channel></rss>\n")
    base = SITE_URL + "/"
    nf = page("Page not found", "That page does not exist.", f"""
<section class="page-head"><div class="wrap narrow"><h1>Page not found</h1>
<p class="lede">That link does not lead anywhere. The stories are all still here.</p>
<div class="actions"><a class="btn" href="{base}stories/">Browse the stories</a><a class="btn btn-ghost" href="{base}">Go to the home page</a></div></div></section>""", base, "404.html")
    write("404.html", nf.replace(f'href="{base}index.html"', f'href="{base}"'))
    write(".nojekyll", "")
    write(f"{INDEXNOW_KEY}.txt", INDEXNOW_KEY)
    write("CNAME", SITE_URL.split("//")[1] + "\n")


def write(rel, content):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def main():
    global seo_pages, seo_more, solutions
    import seo_pages
    import seo_more
    import solutions
    stories = parse_stories()
    for d in ("covers", "posts", "logos"):
        (ROOT / "assets" / d).mkdir(parents=True, exist_ok=True)
    cf = HERE / "post-images" / "crops.json"   # per story [x, y, width] of the banner crop inside the 800x1000 post graphic
    crops = json.loads(cf.read_text()) if cf.exists() else {}
    if "--no-images" not in sys.argv:
        make_brand_assets()
        for s in stories:
            custom = HERE / "post-images" / f"{s['slug']}.jpg"   # the original 4:5 post graphic
            dest = ROOT / "assets" / "covers" / f"{s['slug']}.jpg"
            if custom.exists():
                from PIL import Image
                x, y, w = crops.get(s["slug"], [0, 0, 800])
                im = Image.open(custom).convert("RGB")
                h = round(w * 630 / 1200)
                im.crop((x, y, x + w, y + h)).resize((1200, 630), Image.LANCZOS).save(dest, "JPEG", quality=82, optimize=True, progressive=True)
                Image.open(custom).convert("RGB").save(ROOT / "assets" / "posts" / f"{s['slug']}.jpg", "JPEG", quality=80, optimize=True, progressive=True)
            else:
                make_cover(s, dest)
        for f in (HERE / "logos").glob("*.png"):
            (ROOT / "assets" / "logos" / f.name).write_bytes(f.read_bytes())
    build_home(stories)
    build_stories_index(stories)
    for s in stories:
        build_story(s, stories)
    build_companies(stories)
    build_about(stories)
    build_contact()
    import extra
    build_meta(stories, extra.build_all(sys.modules[__name__], stories) + seo_pages.build_all(sys.modules[__name__], stories) + seo_more.build_all(sys.modules[__name__], stories) + solutions.build_all(sys.modules[__name__], stories))
    print(f"Built {len(stories)} stories, {sum(1 for s in stories if s.get('company'))} companies")


if __name__ == "__main__":
    main()
