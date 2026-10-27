"""Industry pages, country pages, guides, Tech 50, Tech Tour and the files that help search and AI assistants read the site."""
import html
import json
import re

import extra
from seo_data import MARKETS, VERTICALS

e = html.escape
REVIEWED = "10 October 2026"
FX = 331  # LKR per USD, market rate on 8 October 2026


# ------------------------------------------------------------------ helpers
def mention(stories, slug, label=""):
    """Plain text for a story reference: a neutral description for featured service companies, the name otherwise."""
    import capability
    if slug in capability.ANON:
        return capability.ANON[slug]
    by = {s["slug"]: s for s in stories}
    return label or by[slug].get("company") or by[slug]["title"]


def _mentions(stories, text):
    def rep(m):
        slug, _, label = m.group(1).partition("|")
        out = mention(stories, slug, label)
        start = m.start() == 0 or text[:m.start()].rstrip().endswith((".", "?", ":"))
        return out[0].upper() + out[1:] if start else out
    return re.sub(r"\[\[([^\]]+)\]\]", rep, text)


def linked(B, stories, text, prefix):
    return e(_mentions(stories, text))


def plain_names(stories, text):
    return _mentions(stories, text)


def ld(obj):
    return f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>'


def crumbs_ld(B, trail):
    return ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{B.SITE_URL}/{p}"} for i, (n, p) in enumerate(trail)]})


def faq_block(stories, faqs, heading="Common questions"):
    items = "".join(f"<details><summary>{e(q)}</summary><p>{e(plain_names(stories, a))}</p></details>" for q, a in faqs)
    schema = ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain_names(stories, a)}} for q, a in faqs]})
    return f'<section class="faq"><h2>{e(heading)}</h2>{items}</section>', schema


def crumb_html(trail):
    return '<p class="crumb">' + ' <span aria-hidden="true">/</span> '.join(f'<a href="{href}">{e(n)}</a>' for n, href in trail) + "</p>"


def proof_list(B, stories, proof, prefix):
    items = "".join(f"<li>{e(t if isinstance(t, str) else t[1])}</li>" for t in proof)
    return f'<ul class="ticks built">{items}</ul><p class="cap">Sourced detail on this work is in our <a href="{prefix}stories/">stories</a>.</p>'


def stats_strip(stats):
    return '<dl class="facts">' + "".join(f"<div><dt>{e(v)}</dt><dd>{e(l)}</dd></div>" for v, l in stats) + "</dl>"


def chip_links(items):
    return '<ul class="names">' + "".join(f'<li><a href="{href}">{e(label)}</a></li>' for label, href in items) + "</ul>"


ICONS = {
    "healthtech": '<path d="M3 12h4l2-5 4 10 2-5h6"/><path d="M12 21C6 17 3 13.5 3 9.5A4.5 4.5 0 0 1 12 7a4.5 4.5 0 0 1 9 2.5c0 1-.2 1.9-.6 2.8"/>',
    "automotive": '<path d="M4 16V12l2-5h12l2 5v4"/><path d="M2 16h20v2H2z"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/><path d="M5 12h14"/>',
    "fintech": '<path d="M3 20h18"/><path d="M6 20v-6M11 20V9M16 20v-9"/><path d="M4 9l6-5 5 4 6-5"/><path d="M17 3h4v4"/>',
    "ai": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/><path d="M5 3l.6 1.6L7 5l-1.4.6L5 7l-.6-1.4L3 5l1.4-.4z"/>',
    "enterprise-software": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 12l9 5 9-5"/><path d="M3 16l9 5 9-5"/>',
    "semiconductors-embedded": '<rect x="7" y="7" width="10" height="10" rx="1.5"/><rect x="10" y="10" width="4" height="4"/><path d="M10 7V3M14 7V3M10 21v-4M14 21v-4M7 10H3M7 14H3M21 10h-4M21 14h-4"/>',
    "logistics-travel": '<path d="M2 7h11v10H2z"/><path d="M13 10h4l4 4v3h-8z"/><circle cx="6.5" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "govtech": '<path d="M3 9l9-6 9 6z"/><path d="M5 9v9M9.5 9v9M14.5 9v9M19 9v9"/><path d="M2 21h20M3 18h18"/>',
    "finance-accounting": '<rect x="5" y="2.5" width="14" height="19" rx="2"/><path d="M8 7h8"/><path d="M8.5 11.5h.01M12 11.5h.01M15.5 11.5h.01M8.5 15h.01M12 15h.01M15.5 15h.01M8.5 18h.01M12 18h3.5"/>',
}


def _flag(inner):
    return f'<svg class="flag" viewBox="0 0 30 20" width="30" height="20" aria-hidden="true"><clipPath id="fc"><rect width="30" height="20" rx="3"/></clipPath><g clip-path="url(#fc)">{inner}</g><rect x=".5" y=".5" width="29" height="19" rx="2.5" fill="none" stroke="rgba(15,27,51,.18)"/></svg>'


_NO = '<rect width="30" height="20" fill="#ba0c2f"/><path d="M0 10h30M11 0v20" stroke="#fff" stroke-width="5"/><path d="M0 10h30M11 0v20" stroke="#00205b" stroke-width="2.4"/>'
_SE = '<rect width="30" height="20" fill="#006aa7"/><path d="M0 10h30M11 0v20" stroke="#fecc02" stroke-width="3.6"/>'
_DK = '<rect width="30" height="20" fill="#c8102e"/><path d="M0 10h30M11 0v20" stroke="#fff" stroke-width="3.2"/>'
_AE = '<rect width="30" height="6.67" fill="#00732f"/><rect y="6.67" width="30" height="6.67" fill="#fff"/><rect y="13.33" width="30" height="6.67"/><rect width="8" height="20" fill="#e4002b"/>'
_UK = '<rect width="30" height="20" fill="#012169"/><path d="M0 0l30 20M30 0L0 20" stroke="#fff" stroke-width="4"/><path d="M0 0l30 20M30 0L0 20" stroke="#c8102e" stroke-width="1.6"/><path d="M15 0v20M0 10h30" stroke="#fff" stroke-width="6.4"/><path d="M15 0v20M0 10h30" stroke="#c8102e" stroke-width="3.6"/>'
FLAGS = {
    "usa": '<rect width="30" height="20" fill="#fff"/>' + "".join(f'<rect y="{y}" width="30" height="1.54" fill="#b22234"/>' for y in (0, 3.08, 6.15, 9.23, 12.31, 15.38, 18.46)) + '<rect width="13" height="10.8" fill="#3c3b6e"/>',
    "uk": _UK,
    "nordics": None,
    "norway": _NO,
    "sweden": _SE,
    "netherlands": '<rect width="30" height="6.67" fill="#ae1c28"/><rect y="6.67" width="30" height="6.67" fill="#fff"/><rect y="13.33" width="30" height="6.67" fill="#21468b"/>',
    "germany": '<rect width="30" height="6.67"/><rect y="6.67" width="30" height="6.67" fill="#dd0000"/><rect y="13.33" width="30" height="6.67" fill="#ffce00"/>',
    "australia": '<rect width="30" height="20" fill="#012169"/><g transform="scale(.5)">' + _UK.replace('<rect width="30" height="20" fill="#012169"/>', '') + '</g><g fill="#fff"><circle cx="7.5" cy="15" r="1.6"/><circle cx="22" cy="4" r="1"/><circle cx="26" cy="9" r="1"/><circle cx="22" cy="16" r="1"/><circle cx="18.5" cy="10" r="1"/></g>',
    "uae-gulf": _AE,
}
# shared working hours on a 9 to 6 day: (label, where the shared block sits in their day, share of their day)
OVERLAP = {
    "usa": ("Later shift, 2 to 3 hours", 0.0, 0.0),
    "uk": ("3.5 to 4.5 shared hours", 0.0, 0.5),
    "nordics": ("4.5 to 5.5 shared hours", 0.0, 0.61),
    "norway": ("4.5 to 5.5 shared hours", 0.0, 0.61),
    "sweden": ("4.5 to 5.5 shared hours", 0.0, 0.61),
    "netherlands": ("4.5 to 5.5 shared hours", 0.0, 0.61),
    "germany": ("4.5 to 5.5 shared hours", 0.0, 0.61),
    "australia": ("3.5 to 4.5 shared hours", 0.5, 0.5),
    "uae-gulf": ("6.5 to 7.5 shared hours", 0.0, 0.83),
}


VIMG = {"healthtech": "creative-software", "automotive": "inivos", "fintech": "millenniumit", "ai": "roar-global", "enterprise-software": "wso2",
        "semiconductors-embedded": "synopsys", "logistics-travel": "codegen", "govtech": "rootcode", "finance-accounting": "infomate"}
DEMONYM = {"usa": "US", "uk": "UK", "nordics": "Nordic", "norway": "Norwegian", "sweden": "Swedish", "netherlands": "Dutch", "germany": "German", "australia": "Australian", "uae-gulf": "Gulf"}


def _names(by, proof, n=3):
    out = []
    for slug, _ in proof:
        s = by.get(slug)
        name = (s.get("company") if s else None) or ("IFS" if slug == "why-global-companies-choose-sri-lanka" else None)
        if name and name not in out:
            out.append(name)
    return out


TAGLINE = {"healthtech": "Regulated health platforms and operations", "automotive": "Embedded, electric vehicle and connected car software", "fintech": "Trading, banking and wealth platforms",
           "ai": "AI products, agents and data platforms", "enterprise-software": "ERP, integration and large product codebases", "semiconductors-embedded": "Chip design tools and device software",
           "logistics-travel": "Booking, warehouse and supply chain systems", "govtech": "Public sector platforms and secure delivery", "finance-accounting": "Accounting, finance operations and shared services"}
PITCH = {"usa": "Core engineering and R&D for Fortune 500 companies", "uk": "Trading, wealth and simulation platforms", "nordics": "Product partnerships that have lasted decades",
         "norway": "National health and warehouse automation software", "sweden": "Enterprise software R&D at scale", "netherlands": "Embedded engineering teams for scaleups",
         "germany": "Automotive and chip design software", "australia": "Live network operations and dedicated teams", "uae-gulf": "The closest deep engineering market to the Gulf"}


def hub_blocks(prefix, stories=None):
    """Industry tiles and country cards, reused on the home page, the why page and the hire hub. No company names or logos here by design."""
    ind = "".join(
        f'<a class="tile" href="{prefix}why-sri-lanka/{x["slug"]}/"><img src="{prefix}assets/art/{x["slug"]}.svg" alt="{e(x["label"])} in Sri Lanka, illustration" loading="lazy" width="1200" height="900">'
        f'<span class="tile-body"><strong>{e(x["label"])}</strong><span>{e(TAGLINE[x["slug"]])}</span></span></a>' for x in VERTICALS)
    ctry = []
    for m in MARKETS:
        if m["slug"] == "nordics":
            flag = '<span class="flags">' + _flag(_SE) + _flag(_NO) + _flag(_DK) + "</span>"
        elif m["slug"] == "uae-gulf":
            om = '<rect width="30" height="6.67" fill="#fff"/><rect y="6.67" width="30" height="6.67" fill="#db161b"/><rect y="13.33" width="30" height="6.67" fill="#008000"/><rect width="8" height="20" fill="#db161b"/>'
            flag = '<span class="flags">' + _flag(_AE) + _flag(om) + "</span>"
        else:
            flag = _flag(FLAGS[m["slug"]])
        n = len(m["proof"])
        ctry.append(f'<a class="ctry" href="{prefix}hire-from/{m["slug"]}/"><span class="ctry-top">{flag}<span class="ctry-n"><b>{n}</b> companies building here</span></span><strong>{e(m["label"])}</strong>'
                    f'<span class="ctry-ov">{e(PITCH[m["slug"]])}</span></a>')
    return f'<div class="tile-grid">{ind}</div>', f'<div class="ctry-grid">{"".join(ctry)}</div>'


def related_for(slug):
    """Industry and country pages that cite a given story."""
    out = [(f"Why Sri Lanka for {x['name']}", f"why-sri-lanka/{x['slug']}/") for x in VERTICALS if slug in x.get("cites", [])]
    out += [(f"Hiring from {x['name']}", f"hire-from/{x['slug']}/") for x in MARKETS if slug in x.get("cites", [])]
    return out


def cta(prefix, heading, text, q=""):
    return f"""<section class="cta"><div class="wrap cta-in"><h2>{e(heading)}</h2><p>{e(text)}</p>
<div class="actions"><a class="btn btn-saffron" href="{prefix}talent/find/{q}">Find talent</a><a class="btn btn-ondark" href="https://calendly.com/digisavvyteams/30min" rel="noopener">Schedule a call</a><a class="btn btn-ondark" href="{prefix}guides/sri-lanka-tech-salaries/">See salary guide</a></div></div></section>"""


# ------------------------------------------------------------------ industry pages
MADE_HERE = {  # industry slug -> (heading, sentence, link text, path) for physical goods made in Sri Lanka
    "semiconductors-embedded": ("The hardware is made here too", "Sri Lankan exports of electrical and electronic components rose 61% to US$508.86 million in January to September 2026, led by cables, transformers and switchgear.", "Transformer, cable and switchgear manufacturers in Sri Lanka", "source/electrical-cables-transformers/"),
    "automotive": ("Tyres and rubber parts are made here too", "Sri Lankan makers supply about a quarter of world demand for solid tyres, by Export Development Board estimate, along with pneumatic tyres, seals and gaskets.", "Solid tyre manufacturers in Sri Lanka", "source/industrial-tyres/"),
    "healthtech": ("Medical consumables are made here too", "Sri Lanka exported US$293 million of industrial and surgical gloves in 2025, from manufacturers using local natural rubber.", "Rubber glove manufacturers in Sri Lanka", "source/rubber-gloves/"),
    "logistics-travel": ("Moving goods out of Sri Lanka", "Sri Lanka exported US$13.58 billion of goods in 2025, and its logistics and transport services earned US$1.85 billion.", "How to import from Sri Lanka", "source/how-to-import-from-sri-lanka/"),
}


def _made_here(slug, prefix):
    if slug not in MADE_HERE:
        return ""
    h, t, lt, p = MADE_HERE[slug]
    return f'<aside class="promo"><img src="{prefix}assets/art/{"s-electrical" if "electrical" in p else "s-tyres" if "tyres" in p else "s-gloves" if "gloves" in p else "s-import"}.svg" alt="" loading="lazy" width="1200" height="900"><div><h2>{e(h)}</h2><p>{e(t)}</p><a class="door-go" href="{prefix}{p}">{e(lt)}</a></div></aside>'


def build_verticals(B, stories):
    paths = []
    for v in VERTICALS:
        prefix = "../../"
        faq, faq_ld = faq_block(stories, v["faqs"])
        others = chip_links([(x["label"], f"../{x['slug']}/") for x in VERTICALS if x is not v])
        markets = chip_links([(x["label"], f"{prefix}hire-from/{x['slug']}/") for x in MARKETS])
        body = f"""
<section class="page-head">
  <div class="wrap narrow">
    {crumb_html([("Why Sri Lanka", "../")])}
    <h1>{e(v['h1'])}</h1>
    <p class="answer">{linked(B, stories, v['answer'], prefix)}</p>
  </div>
</section>
<section class="section top-0">
  <div class="wrap narrow">
    <img class="story-cover art" src="{prefix}assets/art/{v['slug']}.svg" alt="{e(v['h1'])}, illustration" width="1200" height="900">
    {stats_strip(v['stats'])}
    <h2 class="h-sub mt">What is already built in Sri Lanka</h2>
    {proof_list(B, stories, v['proof'], prefix)}
    <h2 class="h-sub mt">Roles you can hire</h2>
    <ul class="names roles">{''.join(f'<li><span>{e(r)}</span></li>' for r in v['roles'])}</ul>
    <div class="prose tight">{''.join(f'<h2>{e(h)}</h2><p>{linked(B, stories, t, prefix)}</p>' for h, t in v['sections'])}</div>
    {_made_here(v['slug'], prefix)}
    <div class="reach mt">
      <h2>Start with a shortlist</h2>
      <p>Tell us the roles and the stack. We introduce engineers or partner teams with {e(v['name'])} experience, and you take it from there.</p>
      <div class="actions"><a class="btn" href="{prefix}talent/find/?industry={v['slug']}">Find {e(v['name'])} talent</a>{('<a class="btn btn-ghost" href="' + prefix + 'offshoring/accounting-bookkeeping-outsourcing-sri-lanka/">Accounting outsourcing</a>') if v['slug'] == "finance-accounting" else ""}<a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ghost" href="{prefix}guides/how-to-hire-in-sri-lanka/">How hiring works</a></div>
    </div>
    {faq}
    <h2 class="h-sub mt">Other industries</h2>
    {others}
    <h2 class="h-sub mt">Hiring from your country</h2>
    {markets}
  </div>
</section>
{cta(prefix, "Building in " + v['label'].lower() + "?", "Get introduced to Sri Lankan engineers and teams who have done this work before.", "?industry=" + v['slug'])}
"""
        head = faq_ld + crumbs_ld(B, [("Why Sri Lanka", "why-sri-lanka/"), (v["label"], f"why-sri-lanka/{v['slug']}/")])
        path = f"why-sri-lanka/{v['slug']}/"
        B.write(path + "index.html", B.page(v["title"], v["desc"], body, prefix, path, extra_head=head, active="why"))
        paths.append(path)
    return paths


# ------------------------------------------------------------------ country pages
def build_markets(B, stories):
    paths = []
    for m in MARKETS:
        prefix = "../../"
        faq, faq_ld = faq_block(stories, m["faqs"])
        others = chip_links([(x["label"], f"../{x['slug']}/") for x in MARKETS if x is not m])
        verts = chip_links([(x["label"], f"{prefix}why-sri-lanka/{x['slug']}/") for x in VERTICALS])
        verts_top = hub_blocks(prefix, stories)[0]
        body = f"""
<section class="page-head">
  <div class="wrap narrow">
    {crumb_html([("Why Sri Lanka", prefix + "why-sri-lanka/"), ("By country", "../")])}
    <h1>Why Sri Lanka is an ideal tech destination for {DEMONYM[m['slug']]} companies</h1>
    <p class="answer">{linked(B, stories, m['answer'], prefix)}</p>
  </div>
</section>
<section class="section top-0">
  <div class="wrap narrow">
    {stats_strip(m['stats'])}
    <h2 class="h-sub mt">Work already done from Sri Lanka for {e(m['name'])}</h2>
    {proof_list(B, stories, m['proof'], prefix)}
    <h2 class="h-sub mt">Working hours and time zones</h2>
    <p class="body-l">{e(m['overlap'])}</p>
    <h2 class="h-sub mt">What {DEMONYM[m['slug']]} companies source from Sri Lanka</h2>
    {verts_top}
    <h2 class="h-sub mt">Three ways to start</h2>
    <ol class="steps compact">
      <li><h3>Hire a few people</h3><p>Use an employer of record or contractors. No local company needed. <a href="{prefix}guides/how-to-hire-in-sri-lanka/">How it works</a></p></li>
      <li><h3>Take a dedicated team</h3><p>A Sri Lankan company runs a team that works only for you. <a href="{prefix}companies/">See companies</a></p></li>
      <li><h3>Open your own centre</h3><p>Register a company and hire directly. <a href="{prefix}guides/set-up-a-company-in-sri-lanka/">Setup guide</a></p></li>
    </ol>
    <div class="reach">
      <h2>Tell us who you need</h2>
      <p>We introduce Sri Lankan engineers, specialists or partner teams who have worked with companies from {e(m['name'])}.</p>
      <div class="actions"><a class="btn" href="{prefix}talent/find/?from={m['slug']}">Find talent</a>{('<a class="btn btn-ghost" href="' + prefix + 'offshoring/' + {"uk": "from-uk", "australia": "from-australia", "usa": "from-usa", "uae-gulf": "from-uae"}[m['slug']] + '/">Business services</a>') if m['slug'] in ("uk", "australia", "usa", "uae-gulf") else ""}<a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ghost" href="{prefix}guides/sri-lanka-tech-salaries/">Salary and cost guide</a></div>
    </div>
    {faq}
    <h2 class="h-sub mt">Other countries</h2>
    {others}
  </div>
</section>
"""
        head = faq_ld + crumbs_ld(B, [("Why Sri Lanka", "why-sri-lanka/"), ("By country", "hire-from/"), (m["label"], f"hire-from/{m['slug']}/")])
        path = f"hire-from/{m['slug']}/"
        seo_t = f"Why Sri Lanka for {DEMONYM[m['slug']]} companies: tech talent and teams"
        B.write(path + "index.html", B.page(seo_t, m["desc"], body, prefix, path, extra_head=head, active="why"))
        paths.append(path)

    cards = hub_blocks("../", stories)[1]
    body = f"""
<section class="page-head"><div class="wrap">
  {crumb_html([("Why Sri Lanka", "../why-sri-lanka/")])}
  <h1>Why Sri Lanka, for your country</h1>
  <p class="lede">Which companies from your market already build in Sri Lanka, what they build there, and how to start.</p>
</div></section>
<section class="section top-0"><div class="wrap">{cards}</div></section>
"""
    B.write("hire-from/index.html", B.page("Why Sri Lanka for your country: who already builds there", "Guides for companies in the USA, UK, Nordics, Netherlands, Germany, Australia and the Gulf hiring tech talent in Sri Lanka.", body, "../", "hire-from/",
                                           extra_head=crumbs_ld(B, [("Why Sri Lanka", "why-sri-lanka/"), ("By country", "hire-from/")]), active="why"))
    return paths + ["hire-from/"]


# ------------------------------------------------------------------ guides
def a(label, url):
    return f'<a href="{e(url)}" rel="noopener nofollow">{e(label)}</a>'


def usd(lkr):
    return f"{round(lkr * 1000 / FX / 5) * 5:,}"


GLASSDOOR = [
    ("Software engineering", [
        ("Associate software engineer", 93, "53 to 175", "https://www.glassdoor.com/Salaries/colombo-associate-software-engineer-salary-SRCH_IL.0,7_IM1025_KO8,35.htm"),
        ("Software engineer", 177, "118 to 243", "https://www.glassdoor.com/Salaries/colombo-software-engineer-salary-SRCH_IL.0,7_IM1025_KO8,25.htm"),
        ("Senior software engineer", 260, "188 to 900", "https://www.glassdoor.com/Salaries/colombo-sri-lanka-senior-software-engineer-salary-SRCH_IL.0,17_IM1025_KO18,42.htm"),
        ("Associate technical lead", 365, "274 to 524", "https://www.glassdoor.com/Salaries/colombo-associate-technical-lead-salary-SRCH_IL.0,7_IM1025_KO8,32.htm"),
        ("Software architect", 661, "465 to 988", "https://www.glassdoor.com/Salaries/colombo-software-architect-salary-SRCH_IL.0,7_IM1025_KO8,26.htm"),
        ("Engineering manager", 390, "185 to 2,400", "https://www.glassdoor.com/Salaries/colombo-engineering-manager-salary-SRCH_IL.0,7_IM1025_KO8,27.htm"),
    ]),
    ("QA, DevOps and security", [
        ("QA engineer", 101, "62 to 194", "https://www.glassdoor.com/Salaries/colombo-qa-engineer-salary-SRCH_IL.0,7_IM1025_KO8,19.htm"),
        ("Senior QA engineer", 205, "153 to 300", "https://www.glassdoor.com/Salaries/colombo-senior-qa-engineer-salary-SRCH_IL.0,7_IM1025_KO8,26.htm"),
        ("DevOps engineer", 202, "128 to 456", "https://www.glassdoor.com/Salaries/colombo-devops-engineer-salary-SRCH_IL.0,7_IM1025_KO8,23.htm"),
        ("Senior DevOps engineer", 333, "238 to 550", "https://www.glassdoor.com/Salaries/colombo-senior-devops-engineer-salary-SRCH_IL.0,7_IM1025_KO8,30.htm"),
        ("Cyber security engineer", 205, "108 to 1,300", "https://www.glassdoor.com/Salaries/colombo-cyber-security-engineer-salary-SRCH_IL.0,7_IM1025_KO8,31.htm"),
    ]),
    ("Data and AI", [
        ("Data engineer", 215, "140 to 356", "https://www.glassdoor.com/Salaries/colombo-data-engineer-salary-SRCH_IL.0,7_IM1025_KO8,21.htm"),
        ("Senior data engineer", 364, "241 to 513", "https://www.glassdoor.com/Salaries/colombo-senior-data-engineer-salary-SRCH_IL.0,7_IM1025_KO8,28.htm"),
        ("Data scientist", 217, "142 to 279", "https://www.glassdoor.com/Salaries/colombo-data-scientist-salary-SRCH_IL.0,7_IM1025_KO8,22.htm"),
        ("Machine learning engineer", 233, "110 to 279", "https://www.glassdoor.com/Salaries/colombo-machine-learning-engineer-salary-SRCH_IL.0,7_IM1025_KO8,33.htm"),
    ]),
    ("Product, design and ERP", [
        ("UX designer", 156, "88 to 229", "https://www.glassdoor.com/Salaries/colombo-ux-designer-salary-SRCH_IL.0,7_IM1025_KO8,19.htm"),
        ("Senior UX designer", 244, "210 to 376", "https://www.glassdoor.com/Salaries/colombo-senior-ux-designer-salary-SRCH_IL.0,7_IM1025_KO8,26.htm"),
        ("Business analyst", 108, "74 to 167", "https://www.glassdoor.com/Salaries/colombo-business-analyst-salary-SRCH_IL.0,7_IM1025_KO8,24.htm"),
        ("Product manager", 233, "145 to 367", "https://www.glassdoor.com/Salaries/colombo-product-manager-salary-SRCH_IL.0,7_IM1025_KO8,23.htm"),
        ("Senior product manager", 325, "195 to 575", "https://www.glassdoor.com/Salaries/colombo-senior-product-manager-salary-SRCH_IL.0,7_IM1025_KO8,30.htm"),
        ("ERP consultant", 169, "103 to 249", "https://www.glassdoor.com/Salaries/colombo-erp-consultant-salary-SRCH_IL.0,7_IM1025_KO8,22.htm"),
        ("SAP consultant", 219, "133 to 415", "https://www.glassdoor.com/Salaries/colombo-sap-consultant-salary-SRCH_IL.0,7_IM1025_KO8,22.htm"),
    ]),
    ("Finance", [
        ("Assistant accountant", 81, "54 to 125", "https://www.glassdoor.com/Salaries/colombo-assistant-accountant-salary-SRCH_IL.0,7_IM1025_KO8,28.htm"),
        ("Financial analyst", 79, "53 to 129", "https://www.glassdoor.com/Salaries/colombo-financial-analyst-salary-SRCH_IL.0,7_IM1025_KO8,25.htm"),
        ("Finance manager", 267, "211 to 433", "https://www.glassdoor.com/Salaries/colombo-finance-manager-salary-SRCH_IL.0,7_IM1025_KO8,23.htm"),
    ]),
]
COMMUNITY = [("Associate software engineer", 115, 13, "50 to 225"), ("Software engineer", 280, 19, "38 to 1,496"), ("Senior software engineer", 447, 13, "120 to 1,978"),
             ("Associate tech lead", 605, 11, "392 to 900"), ("Tech lead and senior tech lead", 774, 6, "638 to 2,791")]


def build_salary(B, stories):
    prefix = "../../"
    rows = ""
    for group, items in GLASSDOOR:
        rows += f'<tr class="grp"><th colspan="5">{e(group)}</th></tr>'
        for role, med, rng, url in items:
            yearly = round(med * 1000 * 12 * 1.15 / FX / 100) * 100
            rows += f"<tr><td>{a(role, url)}</td><td>{med},000</td><td>{rng}</td><td>{usd(med)}</td><td>{yearly:,}</td></tr>"
    csv = ["group,role,median_lkr_month,range_lkr_thousands_month,median_usd_month,employer_cost_usd_year,source,source_url"]
    for group, items in GLASSDOOR:
        for role, med, rng, url in items:
            csv.append(f'{group},{role},{med * 1000},"{rng}",{usd(med).replace(",", "")},{round(med * 1000 * 12 * 1.15 / FX / 100) * 100},Glassdoor 2026 self reported,"{url}"')
    for r, m, n, rng in COMMUNITY:
        csv.append(f'Export and dollar pegged employers,{r},{m * 1000},"{rng}",{usd(m).replace(",", "")},{round(m * 1000 * 12 * 1.15 / FX / 100) * 100},TechSalary community records 2025 to 2026 ({n} records),https://techsalary.tldr.lk/')
    B.write("data/sri-lanka-tech-salaries-2026.csv", "\n".join(csv) + "\n")
    cite = f'<div class="cite"><strong>Use this data.</strong> Free to quote, chart or republish with a link to this page. <a href="../../data/sri-lanka-tech-salaries-2026.csv" download>Download the CSV</a> or run the numbers in the <a href="../../tools/team-cost-calculator/">team cost calculator</a>.<br><span>Suggested credit: Tech Destination Sri Lanka, Sri Lanka tech salary and cost guide 2026, {B.SITE_URL}/guides/sri-lanka-tech-salaries/</span></div>'
    crow = "".join(f"<tr><td>{e(r)}</td><td>{m},000</td><td>{rng}</td><td>{usd(m)}</td><td>{n}</td></tr>" for r, m, n, rng in COMMUNITY)
    faqs = [
        ("What is the average software engineer salary in Sri Lanka?", f"Self reported Glassdoor data for Colombo in 2026 shows a median of about LKR 177,000 a month for a software engineer (about USD {usd(177)}) and LKR 260,000 for a senior software engineer (about USD {usd(260)}). Community reported figures that include dollar pegged roles are higher, at about LKR 280,000 and LKR 447,000."),
        ("What does an employer pay on top of salary in Sri Lanka?", "Employers contribute 12% of gross earnings to the Employees' Provident Fund and 3% to the Employees' Trust Fund, 15% in total. Gratuity of half a month's salary per year of service applies once an employee completes five years with an employer of 15 or more people."),
        ("How much cheaper is a Sri Lankan engineering team?", "The Sri Lanka Export Development Board says operations here typically cost 40% to 65% less than equivalent headcount in the US or UK, with developer rates through vendors of about USD 25 to 40 an hour. It does not cite an underlying study, so treat it as an indication."),
        ("Is there an official salary survey for Sri Lankan tech?", "The SLASSCOM Compensation and Benefits Report, run by Deloitte, is the main employer survey. It is sold to members and participants and its figures are not public."),
    ]
    faq, faq_ld = faq_block(stories, faqs)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {crumb_html([("Guides", "../")])}
  <h1>Sri Lanka tech salary and cost guide 2026</h1>
  <p class="answer">A software engineer in Colombo earns a median of about LKR 177,000 a month (about USD {usd(177)}) and a senior software engineer about LKR 260,000 (about USD {usd(260)}), according to self reported Glassdoor data for 2026. Engineers at export focused and dollar pegged employers earn well above that: community reported medians are LKR 280,000 and LKR 447,000. Employers add 15% in statutory contributions.</p>
  <p class="reviewed">Last reviewed {REVIEWED}. US dollar figures use LKR {FX} per dollar, the market rate on 8 October 2026.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <p class="note"><strong>Read this first.</strong> There is no free, public employer survey of Sri Lankan tech pay. The one that exists, the {a("SLASSCOM Compensation and Benefits Report", "https://www.ft.lk/front-page/SLASSCOM-Tech-pay-stabilising-as-firms-pivot-to-performance/44-785740")} run by Deloitte, is paid. Everything below is self reported by employees, and the sources disagree with each other. Use the figures as ranges, and expect to pay toward the top for strong people.</p>

  <h2 class="h-sub mt">Monthly pay by role, Colombo</h2>
  <p class="cap">Median total pay and range in thousands of rupees a month. Source: Glassdoor, 2026, self reported. Employer cost adds 15% statutory contributions and converts to dollars a year.</p>
  <div class="tbl"><table>
    <thead><tr><th>Role</th><th>Median LKR a month</th><th>Range, LKR thousands</th><th>Median USD a month</th><th>Employer cost, USD a year</th></tr></thead>
    <tbody>{rows}</tbody>
  </table></div>
  {cite}

  <h2 class="h-sub mt">What engineers at export and dollar pegged employers report</h2>
  <p class="cap">Medians we calculated from 2025 and 2026 records on {a("TechSalary", "https://techsalary.tldr.lk/")}, a community run Sri Lankan salary database. Small samples. Includes salaries pegged to foreign currency, so it skews high.</p>
  <div class="tbl"><table>
    <thead><tr><th>Role</th><th>Median LKR a month</th><th>Range, LKR thousands</th><th>Median USD a month</th><th>Records</th></tr></thead>
    <tbody>{crow}</tbody>
  </table></div>
  <p class="body-l">The gap between the two tables is the real story. Local median pay and what good export companies pay are different markets. A job board guide from {a("ITPro.lk", "https://itpro.lk/salary-sri-lanka-it-jobs/")} puts 2026 software engineering bands at LKR 120,000 to 180,000 for juniors, 180,000 to 320,000 at mid level and 320,000 to 450,000 and above for seniors, which sits between them.</p>

  <h2 class="h-sub mt">What an employee costs on top of salary</h2>
  <ul class="ticks">
    <li>Employees' Provident Fund: employer pays 12% of gross earnings, employee pays 8% ({a("Department of Labour", "https://labourdept.gov.lk/employees-provident-fund-division-static/")}).</li>
    <li>Employees' Trust Fund: employer pays 3% ({a("ETF Board", "https://www.etfb.lk/payment-of-contributions/")}, rate per {a("De Saram", "https://www.desaram.com/a-guide-on-sri-lanka-employment-law/")}).</li>
    <li>Gratuity: half a month's last salary for each completed year, payable when someone with five or more years leaves an employer of 15 or more people ({a("Payment of Gratuity Act", "https://labourdept.gov.lk/downloads/labour_code/55.pdf")}).</li>
    <li>Leave: 14 days annual leave from the third calendar year and 7 days casual leave, plus public holidays. The 2026 {a("government calendar", "https://documents.gov.lk/view/calander/2026/2026_E.pdf")} lists 26 public holidays, 8 of them mercantile holidays.</li>
    <li>Hours: a 45 hour week under the Shop and Office Employees Act.</li>
  </ul>
  <p class="body-l">Worked example: a senior software engineer at the Glassdoor median of LKR 260,000 a month costs about LKR 299,000 with EPF and ETF, or roughly USD {round(260 * 1000 * 12 * 1.15 / FX / 100) * 100:,} a year. At the community median of LKR 447,000 the same sum is roughly USD {round(447 * 1000 * 12 * 1.15 / FX / 100) * 100:,} a year. Benefits such as medical cover, equipment and office space come on top.</p>

  <h2 class="h-sub mt">Rates through a partner company</h2>
  <p class="body-l">If you take a dedicated team from a Sri Lankan company you pay a rate that includes salary, management, space and margin. The {a("Export Development Board", "https://www.srilankabusiness.com/blog/sri-lanka-ict-industry-growth-potential-and-future.html")} puts developer rates at about USD 25 to 40 an hour and says operations typically cost 40% to 65% less than equivalent headcount in the US or UK. The board promotes exports and cites no study, so treat this as an indication and ask partners for quotes.</p>

  <h2 class="h-sub mt">Pay rises</h2>
  <p class="body-l">The SLASSCOM chairman said in a {a("2023 interview", "https://echelon.lk/slasscom-chairman-on-unlocking-the-tech-potential/")} that normal annual wage growth is about 10% to 15%, and that most tech companies raised pay by 45% to 70% or pegged it to the dollar during the 2022 crisis. SLASSCOM's 2025 report says increment budgets have since stabilised. Budget for double digit annual rises for good engineers.</p>

  <h2 class="h-sub mt">Our advice</h2>
  <p class="body-l">Do not hire at the median. The companies in our stories that keep people for a decade pay on an international benchmark. One Australian employer pegs Colombo salaries to the Australian dollar and gives every employee stock. You will still pay far less than at home, and you will get the engineers everyone else is trying to hire.</p>

  <div class="reach mt"><h2>Want real quotes?</h2><p>Tell us the roles. We will introduce people or partner companies who can give you current numbers.</p>
  <div class="actions"><a class="btn" href="{prefix}talent/find/">Find talent</a><a class="btn btn-ghost" href="../how-to-hire-in-sri-lanka/">How to hire in Sri Lanka</a></div></div>
  {faq}
</div></section>
"""
    path = "guides/sri-lanka-tech-salaries/"
    head = faq_ld + crumbs_ld(B, [("Guides", "guides/"), ("Salary and cost guide", path)])
    B.write(path + "index.html", B.page("Sri Lanka tech salary guide 2026: engineer pay and employer costs", "Sourced 2026 salary ranges for software engineers, QA, DevOps, data, product and finance roles in Sri Lanka, plus what an employee costs on top.", body, prefix, path, extra_head=head, active="guides"))
    return path


def build_hire_guide(B, stories):
    prefix = "../../"
    faqs = [
        ("Can I hire in Sri Lanka without setting up a company?", "Yes. An employer of record employs the person locally on your behalf. Deel, Remote, G-P and Multiplier all list Sri Lanka. You can also contract individuals directly or take a dedicated team from a Sri Lankan company."),
        ("What are the statutory employer contributions in Sri Lanka?", "12% of gross earnings to the Employees' Provident Fund and 3% to the Employees' Trust Fund. The employee contributes a further 8% to the provident fund from their salary."),
        ("How hard is it to terminate an employee in Sri Lanka?", "Harder than in most Western countries. For employers with 15 or more staff, ending the employment of someone with over 180 days of service for non disciplinary reasons needs the employee's written consent or approval from the Commissioner of Labour, with compensation set by a published formula."),
        ("How long is probation in Sri Lanka?", "Probation can run up to 180 days and can be extended once by the same period, according to law firm D. L. & F. De Saram."),
    ]
    faq, faq_ld = faq_block(stories, faqs)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {crumb_html([("Guides", "../")])}
  <h1>How to hire tech talent in Sri Lanka</h1>
  <p class="answer">There are four ways to hire in Sri Lanka: through an employer of record, as contractors, through a dedicated team run by a Sri Lankan company, or through your own local company. For fewer than ten people, an employer of record or a partner team is fastest and needs no local entity. Past a few dozen people, most companies register their own.</p>
  <p class="reviewed">Last reviewed {REVIEWED}. This is general information, not legal advice.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <h2 class="h-sub">The four routes compared</h2>
  <div class="tbl"><table>
    <thead><tr><th>Route</th><th>Best for</th><th>You need</th><th>Trade off</th></tr></thead>
    <tbody>
      <tr><td><strong>Employer of record</strong></td><td>1 to 10 people you manage directly</td><td>A contract with a provider. {a("Deel", "https://www.deel.com/hiring/employees/sri-lanka/")}, {a("Remote", "https://remote.com/country-explorer/sri-lanka")}, {a("G-P", "https://www.globalization-partners.com/globalpedia/sri-lanka-employer-of-record")} and {a("Multiplier", "https://www.usemultiplier.com/srilanka/employer-of-record")} list Sri Lanka</td><td>A monthly fee per person, and you do your own recruiting</td></tr>
      <tr><td><strong>Contractors</strong></td><td>Short projects and specialists</td><td>A services contract and a way to pay abroad. See <a href="../pay-employees-and-contractors-in-sri-lanka/">how to pay contractors</a></td><td>Less commitment on both sides. Check misclassification risk with an adviser</td></tr>
      <tr><td><strong>Dedicated team from a partner</strong></td><td>5 to 100 people, fast</td><td>A services agreement with a Sri Lankan company such as those in our <a href="{prefix}companies/">directory</a></td><td>You pay a margin. The partner handles hiring, HR, space and retention</td></tr>
      <tr><td><strong>Your own company</strong></td><td>Long term centres of 30 people or more</td><td>A registered company, a local secretary, payroll and an office. See the <a href="../set-up-a-company-in-sri-lanka/">setup guide</a></td><td>Most control and lowest unit cost, most work to start</td></tr>
    </tbody>
  </table></div>

  <h2 class="h-sub mt">Steps that work</h2>
  <ol class="steps compact">
    <li><h3>Define the roles</h3><p>Stack, seniority, hours of overlap you need and the budget range. The <a href="../sri-lanka-tech-salaries/">salary guide</a> gives current ranges.</p></li>
    <li><h3>Pick the route</h3><p>Small and direct, or a partner team. Decide before you interview, because it changes who employs the person.</p></li>
    <li><h3>Meet people</h3><p>Ask us for introductions, or talk to two or three partner companies and compare.</p></li>
  </ol>

  <h2 class="h-sub mt">Employment basics to know</h2>
  <ul class="ticks">
    <li>Working time: a 9 hour day including a one hour break, up to 45 hours a week, under the Shop and Office Employees Act ({a("De Saram employment law guide", "https://www.desaram.com/a-guide-on-sri-lanka-employment-law/")}).</li>
    <li>Leave: 14 days annual leave from the third calendar year and 7 days casual leave. Maternity leave is 84 paid working days.</li>
    <li>Probation: up to 180 days, extendable once.</li>
    <li>Notice: there is no statutory minimum. It is set in the contract.</li>
    <li>Contributions: employer EPF 12% and ETF 3%. Employee EPF 8%.</li>
    <li>Termination: for employers with 15 or more staff, non disciplinary termination of someone with over 180 days of service needs written consent or approval from the Commissioner of Labour ({a("Termination of Employment of Workmen Act", "https://lankalaw.net/wp-content/uploads/2025/03/Termination-of-Employment-of-Workmen-Consolidated-2024.pdf")}). Compensation follows a formula capped at LKR 2.5 million ({a("De Saram", "https://www.desaram.com/sri-lanka-employment-termination-redundancy-laws-2025/")}).</li>
    <li>Income tax: the first LKR 150,000 a month is tax free, then bands from 6% to 36% apply ({a("Inland Revenue notice, March 2025", "https://taxadvisor.lk/data/uploads/notice_to_taxpayers_26_03_2025_.pdf")}).</li>
  </ul>
  <p class="body-l">The termination rules are the part foreign employers most often miss. Hire carefully, use the probation period properly, and take local advice before ending a contract. For contracts, payroll and tax in detail, read <a href="../pay-employees-and-contractors-in-sri-lanka/">how to pay employees and contractors in Sri Lanka</a>.</p>

  <div class="reach mt"><h2>Skip the search</h2><p>Tell us the roles and we will introduce people or partner teams who fit.</p>
  <div class="actions"><a class="btn" href="{prefix}talent/find/">Find talent</a><a class="btn btn-ghost" href="{prefix}hire-from/">Guides by country</a></div></div>
  {faq}
</div></section>
"""
    path = "guides/how-to-hire-in-sri-lanka/"
    head = faq_ld + crumbs_ld(B, [("Guides", "guides/"), ("How to hire in Sri Lanka", path)])
    B.write(path + "index.html", B.page("How to hire developers in Sri Lanka: routes, costs and rules", "Employer of record, contractors, a partner team or your own company. How each route works in Sri Lanka, with the employment rules to know.", body, prefix, path, extra_head=head, active="guides"))
    return path


def build_setup_guide(B, stories):
    prefix = "../../"
    faqs = [
        ("Can a foreigner own 100% of a software company in Sri Lanka?", "Yes. IT and software are not on the lists of sectors closed or capped for foreign investors, and the Board of Investment states that 100% foreign ownership and full repatriation of profits are allowed."),
        ("What is the corporate tax rate for IT companies in Sri Lanka?", "The standard corporate rate is 30%. Since 1 April 2025, income from services exported and paid for in foreign currency through a bank is taxed at 15%. The earlier full exemption for service exports has ended."),
        ("How long does it take to register a company in Sri Lanka?", "About 7 to 14 working days overall, according to the Chambers Doing Business In 2026 guide: 3 to 5 working days for name reservation and 5 to 12 days for the certificate."),
        ("Does Port City Colombo give a tax holiday to software companies?", "Not automatically. A licence as an Authorised Person lets you operate there in foreign currency. Tax incentives depend on being designated a Business of Strategic Importance. Under the 2025 regulations, secondary businesses so designated pay 7.5% corporate tax for four years."),
    ]
    faq, faq_ld = faq_block(stories, faqs)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {crumb_html([("Guides", "../")])}
  <h1>How to set up a tech company in Sri Lanka</h1>
  <p class="answer">A foreign company can own 100% of a Sri Lankan software company, register it in about two weeks, and repatriate profits. Export service income is taxed at 15%. The main choices are whether to register with the Board of Investment, and whether to locate in Port City Colombo or a regular tech park such as Orion City.</p>
  <p class="reviewed">Last reviewed {REVIEWED}. Rules changed several times in 2025 and 2026. This is general information, not legal or tax advice. Confirm with the bodies linked below or a local adviser.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow prose tight">
  <h2>Registering the company</h2>
  <ul>
    <li>Law: Companies Act No. 7 of 2007. A private company needs at least one director and one shareholder.</li>
    <li>Directors do not have to live in Sri Lanka. A company secretary is required and must be resident ({a("De Saram", "https://www.desaram.com/incorporate-a-company-in-sri-lanka/")}).</li>
    <li>Timeline: name reservation on the registrar's online portal takes 3 to 5 working days and the certificate 5 to 12 days ({a("Chambers Doing Business In 2026", "https://gpg-pdf.chambers.com/Doing-Business-In-2026/1005/")}).</li>
    <li>Since 30 March 2026 you must file beneficial ownership details before incorporation is complete. From June 2026, new companies must register with Inland Revenue within 30 days.</li>
    <li>A branch office of a foreign company needs a minimum inward remittance of USD 200,000.</li>
  </ul>

  <h2>Ownership and money</h2>
  <ul>
    <li>100% foreign ownership and 100% repatriation of profits are allowed for IT companies, through an Inward Investment Account ({a("Board of Investment guide, December 2025", "https://investsrilanka.com/wp-content/uploads/2025/12/BOI-Inv-Guide-Leaflet-2025.12.29.pdf")}).</li>
    <li>Withholding tax on dividends is 15%, subject to tax treaties.</li>
  </ul>

  <h2>Board of Investment registration</h2>
  <p>You can run a company without the Board of Investment (BOI). Registering gives you approval as a foreign investor, help with visas and a single point of contact. The BOI's December 2025 guide lists a minimum investment of USD 150,000 for IT and business process companies and USD 250,000 as the general minimum for foreign investment. Ask the BOI which applies to you. Larger projects of USD 3 million and above can negotiate further concessions ({a("BOI: setting up in Sri Lanka", "https://investsrilanka.com/?p=11127")}).</p>

  <h2>Tax</h2>
  <ul>
    <li>Corporate income tax: 30% standard rate.</li>
    <li>Exported services: 15%, where the service is used outside Sri Lanka and paid in foreign currency through a bank. This applies from 1 April 2025, when the previous exemption ended ({a("Inland Revenue notice", "https://taxadvisor.lk/data/uploads/notice_to_taxpayers_26_03_2025_.pdf")}).</li>
    <li>VAT: 18% standard rate. Exports of services are zero rated ({a("Inland Revenue Department", "https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Value%20Added%20Tax%20(VAT).aspx?menuid=1202")}).</li>
    <li>Payroll: employer EPF 12% and ETF 3%. See the <a href="../sri-lanka-tech-salaries/">salary and cost guide</a>.</li>
  </ul>

  <h2>Port City Colombo</h2>
  <p>Port City is a special economic zone beside Colombo's business district. The first global IT firms moved in during 2025.</p>
  <ul>
    <li>You operate there as an Authorised Person, licensed by the {a("Colombo Port City Economic Commission", "https://www.portcitycolombo.gov.lk/application-process")}. The licence runs 12 months and is renewable. Until space is ready you can work from an approved location outside the zone.</li>
    <li>Business is done in foreign currency and must serve overseas clients unless the commission authorises local dealings.</li>
    <li>Tax incentives are not automatic. They apply to companies designated as Businesses of Strategic Importance. Under regulations gazetted in September 2025, secondary businesses with that status pay 7.5% corporate tax for four years, then normal rates ({a("KPMG", "https://kpmg.com/us/en/taxnewsflash/news/2025/09/sri-lanka-guidance-tax-exemptions-incentives-colombo-port-city.html")}, {a("De Saram", "https://www.desaram.com/sri-lanka-port-city-regulations-2025-tax-investment-rules/")}).</li>
    <li>The income tax exemption for employees was removed in January 2026 for newly registered companies ({a("KPMG", "https://assets.kpmg.com/content/dam/kpmg/lk/pdf/kpmg-tax-news/2026/january/Tax_Flash_News_the_Colombo_Port_City_Economic_Commission_Act.pdf")}).</li>
  </ul>
  <p>Older guides that promise 25 year tax holidays and tax free salaries are out of date.</p>

  <h2>Where tech companies locate</h2>
  <ul>
    <li>Orion City, Colombo 09: a 16 acre IT park that is home to IFS, Virtusa, Synopsys and Michelin teams.</li>
    <li>TRACE Expert City, Colombo 10: a tech campus whose tenants include CodeGen.</li>
    <li>World Trade Center, Colombo 01: twin towers in the business district, home to the BOI and Dijital Team.</li>
    <li>Port City Colombo: the special economic zone described above.</li>
  </ul>

  <h2>Visas</h2>
  <ul>
    <li>Staff of BOI companies get residence visas on the BOI's recommendation, for one year at a time. The BOI offers investors a five year residence visa.</li>
    <li>An investor visa is available for USD 100,000 (5 years) or USD 200,000 (10 years) ({a("Department of Immigration and Emigration", "https://www.immigration.gov.lk/pages_e.php?id=18")}).</li>
    <li>A digital nomad visa is in force for remote workers earning at least USD 2,000 a month from abroad. It does not allow local employment.</li>
  </ul>

  <h2>Who to contact</h2>
  <ul>
    <li>{a("Board of Investment of Sri Lanka", "https://investsrilanka.com/")}: Investor Facilitation Centre, World Trade Center, Colombo 01.</li>
    <li>{a("Colombo Port City Economic Commission", "https://www.portcitycolombo.gov.lk/")}</li>
    <li>{a("SLASSCOM", "https://slasscom.lk/")}, the IT and business process industry chamber.</li>
    <li>{a("Export Development Board", "https://www.srilankabusiness.com/ict-services/")}</li>
  </ul>
</div>
<div class="wrap narrow">
  <div class="reach mt"><h2>Planning a centre?</h2><p>Tell us the team size and timeline. We will introduce advisers and companies who have done it.</p>
  <div class="actions"><a class="btn" href="{prefix}contact/?need=setup">Plan your setup</a><a class="btn btn-ghost" href="../how-to-hire-in-sri-lanka/">Start smaller first</a></div></div>
  {faq}
</div></section>
"""
    path = "guides/set-up-a-company-in-sri-lanka/"
    head = faq_ld + crumbs_ld(B, [("Guides", "guides/"), ("Set up a company in Sri Lanka", path)])
    B.write(path + "index.html", B.page("How to set up a tech company in Sri Lanka: tax, BOI, Port City", "Company registration, foreign ownership, the 15% tax on service exports, Board of Investment and Port City rules, verified October 2026.", body, prefix, path, extra_head=head, active="guides"))
    return path


FACTS = [
    ("How big are Sri Lanka's IT and BPM exports?", "USD 1.645 billion in 2025, up 8.8% on the year, according to the Export Development Board. The Central Bank's narrower balance of payments measure records about USD 0.8 billion, and the industry estimates about USD 2 billion, because revenue booked abroad and freelance income are not fully captured.", [("Export Development Board via Daily FT", "https://www.ft.lk/top-story/Export-earnings-up-5-6-to-17-2-b-in-2025/26-787471"), ("EconomyNext", "https://economynext.com/sri-lankas-it-bpo-export-revenue-lower-than-reality-after-crisis-expert-260080/")]),
    ("How many people work in tech in Sri Lanka?", "The Export Development Board cites 146,000 people employed in the sector. Press reports of industry estimates in 2026 put it at about 175,000. The last full official survey counted 124,873 ICT workers in 2018.", [("Export Development Board", "https://www.srilankabusiness.com/ict-services/"), ("National IT and BPM Workforce Survey 2019", "https://www.icta.lk/icta-assets/uploads/2023/02/NATIONAL-IT-BPM-WORKFORCE-SURVEY-2019-1-1.pdf")]),
    ("How many ICT graduates does Sri Lanka produce each year?", "Startup Genome's 2026 report says 12,000+. Industry estimates reported in the press in 2026 say about 17,000 enter the sector each year.", [("Our story on the 2026 report", "stories/startup-genome-2026/")]),
    ("How does Sri Lanka rank for tech talent?", "Third in Asia for affordable tech talent in Startup Genome's Global Startup Ecosystem Report 2026, which also recorded Sri Lanka climbing more than 65 places in its emerging ecosystem rankings, the biggest jump that year.", [("Our story", "stories/startup-genome-2026/")]),
    ("What are the biggest Sri Lankan tech exits?", "Virtusa, cofounded by a Sri Lankan, was acquired for USD 2 billion in 2021. WSO2 was acquired by EQT for USD 600 million in 2024. The London Stock Exchange bought MillenniumIT after choosing its trading platform. JPMorganChase acquired WealthOS in 2026.", [("Virtusa", "stories/virtusa/"), ("WSO2", "stories/wso2/"), ("MillenniumIT", "stories/millenniumit/"), ("WealthOS", "stories/wealthos/")]),
    ("Which global companies run R&D in Sri Lanka?", "IFS does about 60% of its global product development in Colombo. Sysco, Synopsys and Zebra Technologies run engineering or R&D centres there. HCLTech, EY, HSBC and WNS run delivery operations.", [("Our roundup", "stories/why-global-companies-choose-sri-lanka/"), ("Companies directory", "companies/")]),
    ("Who are the largest tech employers in Sri Lanka?", "Virtusa has 3,000+ engineers in Colombo and IFS has 2,200+ employees there.", [("Virtusa", "stories/virtusa/"), ("Our roundup", "stories/why-global-companies-choose-sri-lanka/")]),
    ("What time zone is Sri Lanka in?", "UTC+5:30 all year, with no daylight saving. That is 1.5 hours ahead of the UAE, 3.5 to 4.5 hours ahead of Central Europe, 4.5 to 5.5 hours ahead of the UK and 9.5 to 10.5 hours ahead of US Eastern time.", [("Guides by country", "hire-from/")]),
    ("What does a software engineer earn in Sri Lanka?", f"A median of about LKR 177,000 a month (about USD {usd(177)}) according to self reported Glassdoor data for 2026, and about LKR 260,000 for a senior engineer. Export focused employers pay more.", [("Salary and cost guide", "guides/sri-lanka-tech-salaries/")]),
    ("What tax do IT exporters pay in Sri Lanka?", "15% on income from services exported and paid for in foreign currency, from 1 April 2025. The standard corporate rate is 30%.", [("Setup guide", "guides/set-up-a-company-in-sri-lanka/")]),
    ("Can foreigners fully own a tech company in Sri Lanka?", "Yes. IT and software companies can be 100% foreign owned and can repatriate profits, according to the Board of Investment.", [("Setup guide", "guides/set-up-a-company-in-sri-lanka/")]),
    ("Which universities feed the tech industry?", "The University of Moratuwa, a top contributor to Google Summer of Code since 2004, and SLIIT, the largest private tech university with 25,000+ students, are the best known. Peradeniya and Ruhuna teach chip design with a curriculum built with Synopsys.", [("Universities", "stories/universities/"), ("Synopsys", "stories/synopsys/")]),
    ("Where are the main tech parks in Colombo?", "Orion City in Colombo 09 houses 85+ technology companies. TRACE Expert City in Colombo 10, the World Trade Center in Colombo 01 and Port City Colombo are the other main hubs.", [("Orion City", "stories/orion-city/")]),
    ("Is there an AI industry in Sri Lanka?", "Yes. Roar Global runs the country's first AI gateway, Xeynergy builds its own AI products and Rootcode builds AI platforms for the Estonian government.", [("Why Sri Lanka for AI", "why-sri-lanka/ai/")]),
]


def build_facts(B, stories):
    prefix = "../../"
    items = ""
    for q, ans, srcs in FACTS:
        links = ", ".join(a(l, u) if u.startswith("http") else f'<a href="{prefix}{u}">{e(l)}</a>' for l, u in srcs)
        items += f'<div class="fact"><h2>{e(q)}</h2><p>{e(ans)}</p><p class="srcs">Sources: {links}</p></div>'
    faq_ld = ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans, _ in FACTS]})
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {crumb_html([("Guides", "../")])}
  <h1>Sri Lanka tech industry facts and statistics</h1>
  <p class="answer">Sri Lanka's IT and business process sector exported USD 1.645 billion of services in 2025 and employs roughly 150,000 people. It is home to about 60% of IFS's global product development, to engineering centres for Sysco, Synopsys and Zebra, and to exits worth up to USD 2 billion. The key numbers are below, each with its source.</p>
  <p class="reviewed">Last reviewed {REVIEWED}. Where sources disagree we show the range and say who reported what.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">{items}
  <div class="cite"><strong>Use these numbers.</strong> Free to quote or republish with a link to this page. Each one names its original source, so cite that as well.<br><span>Suggested credit: Tech Destination Sri Lanka, Sri Lanka tech industry facts 2026, {B.SITE_URL}/guides/sri-lanka-tech-industry-facts/</span></div>
  <p class="body-l">For goods exports by product and by country, from tea and apparel to cables and spices, see <a href="{prefix}source/sri-lanka-export-statistics/">Sri Lanka export statistics</a>.</p>
  <div class="reach mt"><h2>Need a number we do not have?</h2><p>Ask us. If we can source it, we will add it here.</p><div class="actions"><a class="btn" href="{prefix}contact/">Contact us</a><a class="btn btn-ghost" href="{prefix}stories/">Read the stories</a></div></div>
</div></section>
"""
    path = "guides/sri-lanka-tech-industry-facts/"
    head = faq_ld + crumbs_ld(B, [("Guides", "guides/"), ("Industry facts", path)])
    B.write(path + "index.html", B.page("Sri Lanka tech industry facts and statistics 2026", "Sourced answers on Sri Lanka's IT exports, workforce, graduates, rankings, exits, salaries, tax and time zone, updated October 2026.", body, prefix, path, extra_head=head, active="guides"))
    return path


def build_guides_hub(B):
    items = [
        ("sri-lanka-tech-salaries/", "Salary and cost guide 2026", "What engineers, designers, data and finance people earn in Colombo, and what an employee costs on top."),
        ("how-to-hire-in-sri-lanka/", "How to hire in Sri Lanka", "Employer of record, contractors, partner teams or your own company, with the employment rules to know."),
        ("set-up-a-company-in-sri-lanka/", "How to set up a tech company", "Registration, ownership, the 15% export tax, the Board of Investment and Port City Colombo."),
        ("sri-lanka-tech-industry-facts/", "Industry facts and statistics", "Exports, workforce, graduates, rankings and exits, each with its source."),
        ("sri-lanka-startup-ecosystem/", "The startup ecosystem", "How many startups, how the country ranks, the exits, the investors and the weak points."),
        ("pay-employees-and-contractors-in-sri-lanka/", "How to pay employees and contractors", "Contracts, currency, the 15% tax cap, EPF and ETF, payroll deadlines and the laws that apply."),
        ("employer-of-record-sri-lanka/", "Employer of record in Sri Lanka", "Hire without a local company: who covers Sri Lanka, what you pay and the rules to know."),
        ("../tools/team-cost-calculator/", "Team cost calculator", "Pick roles and team size to see monthly and yearly cost, direct or through a partner."),
        ("../offshoring/", "Outsourcing beyond tech", "Accounting, research, medical billing, support, legal, BIM, marketing and virtual assistants from Sri Lanka."),
        ("../compare/", "Sri Lanka compared", "Side by side with Vietnam, the Philippines, Poland, Ukraine, Romania and Latin America."),
        ("../answers/", "Answers", "Short, sourced answers to the questions founders and CTOs ask most."),
        ("../playbook/", "The 2026 playbook (PDF)", "Salaries, hiring routes, setup, tax and industry numbers in one download."),
        ("../why-sri-lanka/", "Why Sri Lanka, by industry", "Evidence pages for healthtech, automotive, fintech, AI and more."),
        ("../hire-from/", "Hiring by country", "Time zones and proof for the USA, UK, Nordics, Netherlands, Germany, Australia and the Gulf."),
        ("../source/how-to-import-from-sri-lanka/", "How to import from Sri Lanka", "Duty access for the UK, EU and US, export documents, shipping from Colombo and payment terms."),
        ("../source/sri-lanka-export-statistics/", "Sri Lanka export statistics", "Exports by product and by country for 2025 and 2026, with a CSV download."),
    ]
    art = {"sri-lanka-tech-salaries/": "g-salaries", "how-to-hire-in-sri-lanka/": "g-hire", "set-up-a-company-in-sri-lanka/": "g-setup", "sri-lanka-tech-industry-facts/": "g-facts",
           "sri-lanka-startup-ecosystem/": "g-ecosystem", "employer-of-record-sri-lanka/": "g-eor", "pay-employees-and-contractors-in-sri-lanka/": "g-pay", "../offshoring/": "g-offshoring",
           "../tools/team-cost-calculator/": "g-calculator", "../compare/": "g-compare", "../answers/": "g-answers", "../playbook/": "g-playbook", "../why-sri-lanka/": "g-why", "../hire-from/": "g-countries",
           "../source/how-to-import-from-sri-lanka/": "s-import", "../source/sri-lanka-export-statistics/": "s-stats"}
    cards = "".join(f'<a class="door has-art" href="{h}"><img class="door-art" src="../assets/art/{art.get(h, "g-why")}.svg" alt="{e(t)}, illustration" loading="lazy" width="1200" height="900"><h3>{e(t)}</h3><p>{e(d)}</p><span class="door-go">Open</span></a>' for h, t, d in items)
    body = f"""
<section class="page-head"><div class="wrap">
  <h1>Guides</h1>
  <p class="lede">Practical, sourced answers for companies deciding whether and how to build in Sri Lanka.</p>
</div></section>
<section class="section top-0"><div class="wrap"><div class="doors wrap3">{cards}</div></div></section>
"""
    B.write("guides/index.html", B.page("Guides to hiring and building tech teams in Sri Lanka", "Salary guide, hiring guide, company setup guide and industry statistics for technology companies looking at Sri Lanka.", body, "../", "guides/", active="guides"))
    return "guides/"


# ------------------------------------------------------------------ Tech 50 and Tech Tour
def build_tech50(B, stories):
    f = extra.form(B, "tech-50", "Nominate a company", "You can nominate your own company or someone else's.", [
        ("text", "name", "Your name", True, ""), ("email", "email", "Email", True, ""),
        ("text", "company", "Company you are nominating", True, ""), ("url", "website", "Company website", False, "https://"),
        ("select", "category", "Category", True, ["Product company", "Engineering services", "Global company in Sri Lanka", "Startup under five years old", "AI", "Finance and shared services"]),
        ("textarea", "why", "Why it belongs on the list", True, "What it built, who uses it abroad, and numbers we can verify"),
        ("select", "sponsor", "Interested in sponsoring the list?", False, ["No", "Yes, send me details"]),
    ], "Send nomination", "Nomination received. Thank you.")
    body = f"""
<section class="page-head"><div class="wrap narrow">
  <h1>Sri Lanka Tech 50</h1>
  <p class="answer">The Sri Lanka Tech 50 is our annual list of the fifty companies doing the most to put Sri Lankan technology talent on the world map. Nominations for the first edition are open.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <div class="proof two">
    <div><strong>What gets a company on the list</strong><p>Work delivered for customers outside Sri Lanka, growth in people and revenue, and recognition that can be checked. Every entry is fact checked to the same standard as our <a href="../stories/">stories</a>.</p></div>
    <div><strong>Who it is for</strong><p>Product companies, engineering services firms, global companies with centres here and startups under five years old.</p></div>
  </div>
  <h2 class="h-sub">How it works</h2>
  <ol class="steps compact">
    <li><h3>Nominate</h3><p>Anyone can nominate a company using the form below.</p></li>
    <li><h3>We verify</h3><p>We check the claims against public sources and ask companies for evidence.</p></li>
    <li><h3>We publish</h3><p>The fifty are published here and on LinkedIn, each with a short profile and sources.</p></li>
  </ol>
  <h2 class="h-sub">Categories</h2>
  <ul class="names roles"><li><span>Product companies</span></li><li><span>Engineering services</span></li><li><span>Global companies in Sri Lanka</span></li><li><span>Startups under five years old</span></li><li><span>AI</span></li><li><span>Finance and shared services</span></li></ul>
  {f}
  <p class="aside">Want to sponsor the first edition? Choose yes in the form or <a href="../contact/?need=feature">contact us</a>.</p>
</div></section>
"""
    B.write("tech-50/index.html", B.page("Sri Lanka Tech 50: nominate a company", "Nominations are open for the Sri Lanka Tech 50, an annual fact checked list of the companies putting Sri Lankan technology talent on the world map.", body, "../", "tech-50/"))
    return "tech-50/"


def build_tour(B, stories):
    f = extra.form(B, "tech-tour", "Register your interest", "No commitment. We will send dates and details when the first group is confirmed.", [
        ("text", "name", "Your name", True, ""), ("email", "email", "Work email", True, ""),
        ("text", "company", "Company", True, ""), ("text", "country", "Country", True, ""),
        ("select", "goal", "What you want to explore", True, ["Hiring a few people", "A dedicated team with a partner", "Opening our own centre", "Investing", "Not sure yet"]),
        ("select", "size", "Team size you have in mind", False, ["Under 10", "10 to 50", "More than 50"]),
        ("textarea", "notes", "Anything you want to see", False, "Industries, companies or people you would like to meet"),
    ], "Register interest", "Thank you. We will be in touch with dates.")
    body = f"""
<section class="page-head"><div class="wrap narrow">
  <h1>Sri Lanka Tech Tour</h1>
  <p class="answer">The Sri Lanka Tech Tour is a three day visit to Colombo for founders, CTOs and investors who are deciding whether to build a team here. You meet the companies in our stories, see where they work and talk to the people who set them up. We are taking registrations of interest for the first group.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <h2 class="h-sub">What the three days cover</h2>
  <ol class="steps compact">
    <li><h3>See the work</h3><p>Visits to engineering centres of global companies and Sri Lankan product companies, including a tech park.</p></li>
    <li><h3>Meet the people</h3><p>Sessions with founders, engineering leaders and university faculty. Time with engineers, without a sales pitch.</p></li>
    <li><h3>Plan your route</h3><p>Briefings on hiring models, costs, company setup and Port City, and one to one time with advisers.</p></li>
  </ol>
  <div class="proof two">
    <div><strong>Who it is for</strong><p>Founders, CTOs, heads of engineering and investors from outside Sri Lanka who are weighing a team of five or more.</p></div>
    <div><strong>How it runs</strong><p>Small groups, so every visit is a conversation. Dates and cost are set once a group is confirmed, and you decide then whether to join.</p></div>
  </div>
  <p class="body-l">Want to prepare first? Read <a href="../why-sri-lanka/">why companies choose Sri Lanka</a>, the <a href="../guides/sri-lanka-tech-salaries/">salary guide</a> and the <a href="../guides/set-up-a-company-in-sri-lanka/">setup guide</a>.</p>
  {f}
</div></section>
"""
    B.write("tech-tour/index.html", B.page("Sri Lanka Tech Tour: three days for founders and CTOs", "A three day visit to Colombo to meet Sri Lanka's technology companies, engineers and advisers before you decide to build a team there. Register your interest.", body, "../", "tech-tour/"))
    return "tech-tour/"


# ------------------------------------------------------------------ machine readable summary
def build_llms(B, stories, pages):
    lines = [f"# {B.SITE_NAME}", "", f"> {B.SITE_NAME} helps companies abroad hire technology talent, find software outsourcing partners and set up teams in Sri Lanka. It publishes sourced reporting on the software, products and companies built by Sri Lankan technology talent. Through Source from Sri Lanka it also connects buyers abroad with Sri Lankan exporters of tea, cinnamon, coconut products, apparel, rubber products, electrical equipment and more, and runs Tender Radar, international tender alerts and bid support for Sri Lankan exporters.", "",
             "Sri Lanka is UTC+5:30. Colombo is the main technology hub. Every story lists its sources at the end.", "", "## Key facts"]
    lines += [f"- {q} {ans}" for q, ans, _ in FACTS]
    lines += ["", "## Guides"]
    lines += [f"- [{t}]({B.SITE_URL}/{p}): {d}" for p, t, d in [
        ("guides/sri-lanka-tech-salaries/", "Sri Lanka tech salary and cost guide 2026", "Role by role pay ranges and employer costs"),
        ("guides/how-to-hire-in-sri-lanka/", "How to hire tech talent in Sri Lanka", "Four hiring routes and employment rules"),
        ("guides/set-up-a-company-in-sri-lanka/", "How to set up a tech company in Sri Lanka", "Registration, tax, Board of Investment and Port City"),
        ("guides/sri-lanka-tech-industry-facts/", "Sri Lanka tech industry facts and statistics", "Sourced industry numbers"),
        ("why-sri-lanka/", "Why Sri Lanka", "Eight evidence backed reasons"),
        ("guides/employer-of-record-sri-lanka/", "Employer of record in Sri Lanka", "Providers, costs and rules for hiring without a local company"),
        ("offshoring/", "Outsourcing to Sri Lanka: business services beyond tech", "BPO and KPO capabilities with sources: accounting, research, medical billing, support, legal, BIM, marketing, virtual assistants"),
        ("guides/pay-employees-and-contractors-in-sri-lanka/", "How to pay employees and contractors in Sri Lanka", "Contracts, currency, contractor tax, EPF and ETF, payroll deadlines and the laws that apply"),
        ("tools/team-cost-calculator/", "Sri Lanka team cost calculator", "Cost of a team by role and size"),
        ("answers/", "Answers", "Short sourced answers on hiring, outsourcing and setup"),
        ("guides/sri-lanka-startup-ecosystem/", "Sri Lanka's startup ecosystem", "Size, rankings, exits, investors and weaknesses"),
        ("playbook/", "Sri Lanka tech team playbook 2026", "All guides in one PDF"),
        ("data/sri-lanka-tech-salaries-2026.csv", "Salary data 2026 (CSV)", "Open data, free to use with attribution"),
        ("data/sri-lanka-exports-2025-2026.csv", "Sri Lanka export statistics 2025 and 2026 (CSV)", "Exports by sector, product line and market from Export Development Board releases, free to use with attribution"),
    ]]
    import seo_offshoring, seo_offshoring_plus as OX
    lines += ["", "## Outsourcing business services to Sri Lanka"] + [f"- [{c['h1']}]({B.SITE_URL}/offshoring/{c['slug']}/): {c['answer']}" for c in seo_offshoring.CAPS]
    lines += [f"- [{m['h1']}]({B.SITE_URL}/offshoring/{m['slug']}/): {m['answer']}" for m in OX.MARKET_PAGES]
    lines += [f"- [BPO and outsourcing companies in Sri Lanka]({B.SITE_URL}/offshoring/bpo-companies-sri-lanka/): Organisations delivering business services from Sri Lanka, by service, with sources"]
    import seo_compare
    lines += ["", "## Sri Lanka compared with other offshore destinations"] + [f"- [Sri Lanka vs {o['name'][0].upper() + o['name'][1:]}]({B.SITE_URL}/compare/{o['slug']}/): {o['answer']}" for o in seo_compare.OTHERS]
    import solutions
    lines += ["", "## Ways to build a team in Sri Lanka"] + [f"- [{x['h1']}]({B.SITE_URL}/solutions/{x['slug']}/): {x['desc']}" for x in solutions.SOLUTIONS]
    lines += ["", "## Why Sri Lanka, by industry"] + [f"- [{v['h1']}]({B.SITE_URL}/why-sri-lanka/{v['slug']}/): {v['desc']}" for v in VERTICALS]
    lines += ["", "## Hiring from each country"] + [f"- [{m['h1']}]({B.SITE_URL}/hire-from/{m['slug']}/): {m['desc']}" for m in MARKETS]
    import seo_source
    lines += seo_source.llms_lines(B)
    lines += ["", "## Services", f"- [Find talent from Sri Lanka]({B.SITE_URL}/talent/find/)", f"- [Be featured as Sri Lankan Top Talent]({B.SITE_URL}/talent/top-talent/)", f"- [All services]({B.SITE_URL}/services/)",
              f"- [Sri Lanka Tech 50]({B.SITE_URL}/tech-50/)", f"- [Sri Lanka Tech Tour]({B.SITE_URL}/tech-tour/)", f"- [Companies directory]({B.SITE_URL}/companies/)", "", "## Contact", f"- Schedule a call: {B.BOOKING_URL}", f"- Email: {B.EMAIL}"]
    lines += ["", "## Stories"] + [f"- [{s['title']}]({B.SITE_URL}/stories/{s['slug']}/): {s['dek']}" for s in stories]
    B.write("llms.txt", "\n".join(lines) + "\n")


def build_all(B, stories):
    pages = build_verticals(B, stories) + build_markets(B, stories)
    pages += [build_salary(B, stories), build_hire_guide(B, stories), build_setup_guide(B, stories), build_facts(B, stories), build_guides_hub(B), build_tech50(B, stories), build_tour(B, stories)]
    build_llms(B, stories, pages)
    return pages
