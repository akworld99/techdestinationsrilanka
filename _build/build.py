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

# ---------------------------------------------------------------- settings
SITE_URL = "https://akworld99.github.io/techdestinationsrilanka"  # change when a custom domain is connected
SITE_NAME = "Tech Destination Sri Lanka"
TAGLINE = "Connecting the world to Sri Lanka's technology ecosystem"
LINKEDIN = "https://www.linkedin.com/company/tech-destination-sri-lanka/"
INSTAGRAM = "https://www.instagram.com/techdestination_srilanka/"
BOOKING_URL = ""          # Cal.com or Calendly link. Leave empty to hide the booking button.
FORM_ENDPOINT = ""        # Formspree endpoint, e.g. https://formspree.io/f/abcdwxyz. Leave empty to hide the form.

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


def page(title, desc, body, prefix, path, image=None, extra_head="", article=False, active=""):
    url = f"{SITE_URL}/{path}".rstrip("/") + ("/" if not path.endswith(".html") else "")
    if path == "":
        url = SITE_URL + "/"
    img = f"{SITE_URL}/{image or 'assets/share.jpg'}"
    full_title = title if title == SITE_NAME else f"{title} | {SITE_NAME}"

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
      {nav('about/', 'About', 'about')}
      <a class="btn btn-small" href="{prefix}contact/">Work with Sri Lankan talent</a>
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
      <a href="{prefix}stories/">All stories</a>
      <a href="{prefix}stories/?type=built">Built by Sri Lankans</a>
      <a href="{prefix}stories/?type=global">Global companies in Sri Lanka</a>
      <a href="{prefix}stories/?type=ecosystem">Ecosystem and data</a>
    </div>
    <div>
      <p class="foot-h">Work with us</p>
      <a href="{prefix}contact/?need=hire">Hire</a>
      <a href="{prefix}contact/?need=setup">Set up</a>
      <a href="{prefix}contact/?need=recruit">Recruit at scale</a>
      <a href="{prefix}about/#feature">Suggest a company</a>
    </div>
    <div>
      <p class="foot-h">Follow</p>
      <a href="{LINKEDIN}" rel="noopener">LinkedIn</a>
      <a href="{INSTAGRAM}" rel="noopener">Instagram</a>
      <a href="{prefix}feed.xml">RSS feed</a>
    </div>
  </div>
  <div class="wrap legal">© {date.today().year} {SITE_NAME}. Company names and trademarks belong to their owners.</div>
</footer>
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


def doors(prefix):
    items = [
        ("hire", "Hire", "Add Sri Lankan engineers to your own team. We point you to people and partners who have done it before."),
        ("setup", "Set up", "Open your own engineering centre in Colombo. Entity, Board of Investment and Port City options, explained by people on the ground."),
        ("recruit", "Recruit at scale", "Build a team of 20 or 200. We connect you with recruiters and employers of record who do this every week."),
    ]
    return "".join(
        f'<a class="door" href="{prefix}contact/?need={k}"><h3>{t}</h3><p>{d}</p><span class="door-go">Start a conversation</span></a>' for k, t, d in items
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
    body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <h1>Sri Lanka. The underdog tech economy powering global software.</h1>
      <p class="lede">Sri Lankan engineers build trading platforms for stock exchanges, health records for Norway and chip design software for Silicon Valley. We report the stories, with sources.</p>
      <div class="actions">
        <a class="btn" href="stories/">Read the stories</a>
        <a class="btn btn-ghost" href="contact/">Work with Sri Lankan talent</a>
      </div>
    </div>
    <div class="hero-lead">
      {card(lead, "", "lead")}
    </div>
  </div>
  <div class="wrap">{LANDMARKS}</div>
</section>

<section class="band">
  <div class="wrap numbers">
    {''.join(f'<a class="num" href="stories/{slug}/"><strong>{e(v)}</strong><span>{e(l)}</span></a>' for v, l, slug in numbers)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>Latest stories</h2><a class="more" href="stories/">All {len(stories)} stories</a></div>
    <div class="grid">
      {''.join(card(s, "") for s in rest)}
    </div>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head"><h2>Three ways to work with Sri Lankan talent</h2></div>
    <div class="doors">{doors("")}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>{len(companies)} companies featured so far</h2><a class="more" href="companies/">Open the directory</a></div>
    <ul class="names">
      {''.join(f'<li><a href="stories/{s["slug"]}/">{e(s["company"])}</a></li>' for s in sorted([s for s in stories if s.get("company")], key=lambda s: s["company"].lower()))}
    </ul>
  </div>
</section>

<section class="cta">
  <div class="wrap cta-in">
    <h2>Built something global from Sri Lanka?</h2>
    <p>We feature companies and founders with real numbers and sources behind them. Tell us yours.</p>
    <a class="btn btn-saffron" href="about/#feature">Suggest a company</a>
  </div>
</section>
"""
    ld = {"@context": "https://schema.org", "@type": "Organization", "name": SITE_NAME, "url": SITE_URL + "/", "logo": f"{SITE_URL}/assets/logo.png", "sameAs": [LINKEDIN, INSTAGRAM]}
    head = f'<script type="application/ld+json">{json.dumps(ld)}</script>'
    desc = "Sourced stories about the global software, products and companies built by Sri Lankan tech talent, for founders, CTOs and investors."
    write("index.html", page(SITE_NAME, desc, body, "", "", extra_head=head))


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
    write("stories/index.html", page("Stories", f"All {len(stories)} stories from {SITE_NAME}: Sri Lankan built companies, global companies in Sri Lanka, and ecosystem data.", body, "../", "stories/", active="stories"))


def build_story(s, stories):
    i = stories.index(s)
    same = [x for x in stories if x is not s and x["category"] == s["category"]]
    related = (same[:3] if len(same) >= 3 else same + [x for x in stories if x is not s and x not in same][: 3 - len(same)])
    facts = "".join(f"<div><dt>{e(v)}</dt><dd>{e(l)}</dd></div>" for v, l in s["facts"])
    sources = "".join(f'<li><a href="{e(u)}" rel="noopener nofollow">{e(l)}</a></li>' for l, u in s["sources"])
    li = f"https://www.linkedin.com/feed/update/urn:li:activity:{s['linkedin']}/" if s.get("linkedin") else LINKEDIN
    note = f'<p class="note"><strong>Update.</strong> {e(s["note"])}</p>' if s.get("note") else ""
    body = f"""
<article class="story">
  <header class="story-head">
    <div class="wrap narrow">
      <p class="crumb"><a href="../">Stories</a> <span aria-hidden="true">/</span> <a href="../?type={s['category']}">{e(s['catname'])}</a></p>
      <h1>{e(s['title'])}</h1>
      <p class="lede">{e(s['dek'])}</p>
      <p class="meta"><time datetime="{s['date'].isoformat()}">{fdate(s['date'])}</time><span>{read_minutes(s)} min read</span><span>{e(s['sector'])}</span></p>
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
    head = f'<script type="application/ld+json">{json.dumps(ld)}</script>\n<meta property="article:published_time" content="{s["date"].isoformat()}">'
    write(f"stories/{s['slug']}/index.html", page(s["title"], s["dek"], body, "../../", f"stories/{s['slug']}/", image=f"assets/covers/{s['slug']}.jpg", extra_head=head, article=True, active="stories"))


def build_companies(stories):
    cos = sorted([s for s in stories if s.get("company")], key=lambda s: s["company"].lower())
    rows = "".join(
        f"""<a class="co" href="../stories/{s['slug']}/" data-type="{s['category']}" data-text="{e((s['company'] + ' ' + s['sector'] + ' ' + s['blurb']).lower())}">
  <span class="co-mark co-{s['category']}" aria-hidden="true">{e(''.join(w[0] for w in re.findall(r"[A-Za-z0-9]+", s['company'])[:2]).upper())}</span>
  <span class="co-main"><strong>{e(s['company'])}</strong><span>{e(s['blurb'])}</span></span>
  <span class="co-side"><span class="tag tag-{s['category']}">{'Sri Lankan built' if s['category'] == 'built' else 'Global company'}</span><span class="co-sector">{e(s['sector'])}</span></span>
</a>""" for s in cos
    )
    nb = sum(1 for s in cos if s["category"] == "built")
    body = f"""
<section class="page-head">
  <div class="wrap">
    <h1>Companies</h1>
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
    <a class="btn btn-saffron" href="../about/#feature">Suggest a company</a>
  </div>
</section>
"""
    write("companies/index.html", page("Companies", f"Directory of the {len(cos)} companies featured by {SITE_NAME}, from Sri Lankan built product companies to global firms with teams in Colombo.", body, "../", "companies/", active="companies"))


def build_about(stories):
    body = f"""
<section class="page-head">
  <div class="wrap narrow">
    <h1>About</h1>
    <p class="lede">Tech Destination Sri Lanka is an independent media platform. We document what Sri Lankan tech talent has built for the world, so founders, CTOs and investors can judge it on evidence.</p>
  </div>
</section>
<section class="section top-0">
  <div class="wrap narrow prose">
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

    <h2 id="feature">Suggest a company</h2>
    <p>We feature companies of every size as long as the story holds up. To suggest one, send us:</p>
    <ul>
      <li>What was built, and who uses it outside Sri Lanka</li>
      <li>The people behind it</li>
      <li>Numbers you can back with a public source or documents</li>
    </ul>
    <p>Message us on <a href="{LINKEDIN}" rel="noopener">LinkedIn</a> or use the <a href="../contact/?need=feature">contact page</a>. Partner spotlights are available for companies that want a dedicated feature. They follow the same sourcing rules and are labelled as partner content.</p>

    <h2>What we are not</h2>
    <p>We are not a government body, an industry association or an investment promotion agency, and we do not speak for any of them.</p>
  </div>
</section>
"""
    write("about/index.html", page("About", "Who runs Tech Destination Sri Lanka, how we source and check every story, and how to suggest a company.", body, "../", "about/", active="about"))


def build_contact():
    booking = f'<a class="btn" href="{e(BOOKING_URL)}" rel="noopener">Book a 20 minute call</a>' if BOOKING_URL else ""
    form = ""
    if FORM_ENDPOINT:
        form = f"""
    <form class="form" action="{e(FORM_ENDPOINT)}" method="POST" id="contact-form">
      <h2>Send a message</h2>
      <label>I want to
        <select name="need" id="need">
          <option value="hire">Hire Sri Lankan talent</option>
          <option value="setup">Set up in Sri Lanka</option>
          <option value="recruit">Recruit at scale</option>
          <option value="feature">Suggest a company to feature</option>
          <option value="other">Something else</option>
        </select>
      </label>
      <label>Your name <input type="text" name="name" autocomplete="name" required></label>
      <label>Work email <input type="email" name="email" autocomplete="email" required></label>
      <label>Company <input type="text" name="company" autocomplete="organization"></label>
      <label>What do you need? <textarea name="message" rows="5" required></textarea></label>
      <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" class="sr" aria-hidden="true">
      <button class="btn" type="submit">Send message</button>
      <p class="form-status" id="form-status" role="status"></p>
    </form>"""
    body = f"""
<section class="page-head">
  <div class="wrap narrow">
    <h1 id="contact-title">Work with Sri Lankan talent</h1>
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
    write("contact/index.html", page("Work with Sri Lankan talent", "Hire Sri Lankan engineers, set up in Sri Lanka or recruit a team at scale. Tell us what you need.", body, "../", "contact/"))


def build_meta(stories):
    now = datetime.now(timezone.utc)
    urls = [("", date.today())] + [(p, date.today()) for p in ("stories/", "companies/", "about/", "contact/")] + [(f"stories/{s['slug']}/", s["date"]) for s in stories]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE_URL}/{p}</loc><lastmod>{d.isoformat()}</lastmod></url>\n" for p, d in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
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


def write(rel, content):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def main():
    stories = parse_stories()
    (ROOT / "assets" / "covers").mkdir(parents=True, exist_ok=True)
    if "--no-images" not in sys.argv:
        make_brand_assets()
        for s in stories:
            custom = HERE / "post-images" / f"{s['slug']}.jpg"   # drop the real post graphic here to replace the generated cover
            dest = ROOT / "assets" / "covers" / f"{s['slug']}.jpg"
            if custom.exists():
                from PIL import Image
                im = Image.open(custom).convert("RGB")
                im.thumbnail((1200, 1200))
                im.save(dest, "JPEG", quality=84, optimize=True, progressive=True)
            else:
                make_cover(s, dest)
    build_home(stories)
    build_stories_index(stories)
    for s in stories:
        build_story(s, stories)
    build_companies(stories)
    build_about(stories)
    build_contact()
    build_meta(stories)
    print(f"Built {len(stories)} stories, {sum(1 for s in stories if s.get('company'))} companies")


if __name__ == "__main__":
    main()
