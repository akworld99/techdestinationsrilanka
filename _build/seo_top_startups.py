"""Top startups in Sri Lanka: a sourced directory page with logos, links, categories and a client-side filter."""
import html
import json
import os
import re
from urllib.parse import urlparse

import seo_pages as SP
from seo_pages import a

e = html.escape
PATH = "startups/"
REVIEWED = "23 October 2026"
DATA = os.path.join(os.path.dirname(__file__), "content", "startups.json")

# Broad filter groups, mapped from the detailed category label
GROUPS = [
    ("Fintech", ("fintech", "payment", "bnpl", "wealthtech", "insurtech", "banking")),
    ("AI and deeptech", ("ai", "deeptech", "drone", "robot", "graphene", "ev ", "aiot", "web3", "blockchain", "medtech")),
    ("Healthtech", ("health", "med")),
    ("SaaS and enterprise", ("saas", "enterprise", "hr tech", "martech", "governance", "logistics", "supply chain", "construction")),
    ("Consumer and marketplaces", ("e-commerce", "consumer", "mobility", "travel", "proptech", "jobs", "fashion")),
    ("Agritech and climate", ("agri", "climate")),
    ("Edtech", ("edtech", "education")),
]


def group_of(cat):
    c = (cat or "").lower() + " "
    for g, keys in GROUPS:
        if any(k in c for k in keys):
            return g
    return "Other"


def domain(url):
    return urlparse(url).netloc.replace("www.", "") if url else ""


def load():
    items = json.load(open(DATA))
    return [s for s in items if s.get("include", True)]


FAQS = [
    ("What are the best startups in Sri Lanka?", "Among the best known are PickMe, the ride hailing and delivery app that listed on the Colombo Stock Exchange in 2024; WealthOS, the wealth management platform acquired by J.P. Morgan in 2026; and fintechs such as PayHere, Mintpay and Koko. WSO2, founded in Colombo, was acquired by EQT in 2024 in a deal reported at about USD 600 million. This page lists 50 with a sourced fact for each."),
    ("How many startups are there in Sri Lanka?", "Estimates vary with the definition. Our startup ecosystem guide brings together the published counts and rankings, including Startup Genome's 2025 and 2026 reports."),
    ("What are the top AI startups in Sri Lanka?", "Examples on this page include Logical, the desktop AI assistant founded by Sri Lankan engineers and backed by Y Combinator, Scouts, which builds AI drones for security and agriculture, and SenzMate, which applies AI and IoT to farming and industry."),
    ("What are the leading fintech startups in Sri Lanka?", "PayHere, Mintpay, Koko, DirectPay, PAYable, WEBXPAY, Onepay and InsureMe are among the most active. WealthOS, a wealth management platform, was acquired by J.P. Morgan in 2026."),
    ("Has Sri Lanka produced a unicorn?", "Not yet. Its largest technology exits are WSO2, acquired by EQT in 2024 in a deal reported at about USD 600 million, and Virtusa, which was founded with its main delivery base in Colombo and acquired by Baring Private Equity Asia in 2021 for about USD 2 billion."),
    ("How can I invest in or partner with Sri Lankan startups?", "Tell us what you are looking for, whether that is investment, a technology partner or an acquisition target, and we will make introductions."),
]


def card(s, prefix):
    url = s.get("website") or ""
    dom = domain(url)
    initials = "".join(w[0] for w in re.sub(r"\(.*?\)", "", s["name"]).split()[:2]).upper()
    logo = (f'<img src="https://www.google.com/s2/favicons?domain={e(dom)}&amp;sz=128" alt="{e(s["name"])} logo" width="48" height="48" loading="lazy" '
            f'onerror="this.replaceWith(Object.assign(document.createElement(\'span\'),{{className:\'mono\',textContent:\'{initials}\'}}))">') if dom else f'<span class="mono">{initials}</span>'
    founders = ", ".join(s.get("founders") or [])
    meta = " · ".join(x for x in [s.get("category", ""), f"Founded {s['founded']}" if s.get("founded") else "", founders] if x)
    status = f'<p class="st-status">{e(s["status_short"])}</p>' if s.get("status_short") else ""
    link = f'<a class="st-link" href="{e(url)}" rel="noopener" target="_blank">{e(dom)} ↗</a>' if url else ""
    return f"""<article class="st-card" data-group="{e(group_of(s.get('category')))}">
  <div class="st-top">{logo}<div><h3>{e(s['name'])}</h3><p class="st-meta">{e(meta)}</p></div></div>
  <p>{e(s['description'])}</p>
  <p class="st-proof"><strong>Proof:</strong> {e(s['proof_point'])} {a('Source', s['proof_source'])}</p>
  {status}{link}
</article>"""


CSS = """<style>
.st-filters{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0 20px}
.st-filters button{border:1px solid rgba(127,127,127,.35);background:transparent;border-radius:999px;padding:7px 14px;font:inherit;font-size:14px;cursor:pointer;color:inherit}
.st-filters button[aria-pressed=true]{background:#0b2a5b;color:#fff;border-color:#0b2a5b}
.st-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
.st-card{border:1px solid rgba(127,127,127,.22);border-radius:16px;padding:18px;display:flex;flex-direction:column;gap:8px}
.st-card p{margin:0;font-size:15px;line-height:1.5}
.st-top{display:flex;gap:12px;align-items:center}
.st-top img,.st-top .mono{width:48px;height:48px;border-radius:12px;flex:none;background:#fff;border:1px solid rgba(127,127,127,.2);object-fit:contain;padding:6px}
.st-top .mono{display:flex;align-items:center;justify-content:center;font-weight:800;color:#0b2a5b;padding:0}
.st-top h3{margin:0;font-size:18px}
.st-meta{font-size:13px!important;opacity:.75}
.st-proof{font-size:14px!important}
.st-status{font-size:13px!important;font-weight:600;color:#b45309}
.st-link{margin-top:auto;font-size:14px;font-weight:600}
</style>"""

JS = """<script>
document.querySelectorAll('.st-filters button').forEach(b=>b.addEventListener('click',()=>{
 document.querySelectorAll('.st-filters button').forEach(x=>x.setAttribute('aria-pressed',x===b));
 const g=b.dataset.g; document.querySelectorAll('.st-card').forEach(c=>c.hidden=!(g==='all'||c.dataset.group===g));
}));
</script>"""


def build(B, stories):
    items = load()
    prefix = "../"
    groups = sorted({group_of(s.get("category")) for s in items}, key=lambda g: [x for x, _ in GROUPS].index(g) if g in [x for x, _ in GROUPS] else 99)
    counts = {g: sum(1 for s in items if group_of(s.get("category")) == g) for g in groups}
    filters = '<div class="st-filters" role="group" aria-label="Filter by sector"><button data-g="all" aria-pressed="true">All ' + str(len(items)) + "</button>" + "".join(
        f'<button data-g="{e(g)}" aria-pressed="false">{e(g)} {counts[g]}</button>' for g in groups) + "</div>"
    cards = "".join(card(s, prefix) for s in items)
    faq, faq_ld = SP.faq_block(stories, FAQS)
    n = len(items)
    itemlist = SP.ld({"@context": "https://schema.org", "@type": "ItemList", "name": f"Top {n} startups in Sri Lanka (2026)",
                      "numberOfItems": n, "itemListElement": [
                          {"@type": "ListItem", "position": i + 1, "item": {"@type": "Organization", "name": s["name"], **({"url": s["website"]} if s.get("website") else {}),
                                                                           "description": s["description"], **({"foundingDate": str(s["founded"])} if s.get("founded") else {})}}
                          for i, s in enumerate(items)]})
    fin = counts.get("Fintech", 0)
    body = f"""{CSS}
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Guides", prefix + "guides/")])}
  <h1>Top {n} startups in Sri Lanka (2026)</h1>
  <p class="answer">Sri Lanka's best known startups include PickMe, the ride hailing app that listed in Colombo in 2024, WealthOS, acquired by J.P. Morgan in 2026, and a wave of fintechs led by PayHere, Mintpay and Koko. Alongside them are AI and deeptech companies such as Logical, backed by Y Combinator, Scouts in drones and Ceylon Graphene Technologies in advanced materials. These {n} tech and tech enabled startups and scale ups were founded in Sri Lanka or by Sri Lankans who build there, and each comes with one sourced fact.</p>
  <p class="reviewed">Last reviewed {REVIEWED}. Not a ranking: companies are grouped by sector. Logos belong to their owners. Know a startup we should add? <a href="mailto:{B.EMAIL}">Tell us</a>.</p>
</div></section>
<section class="section top-0"><div class="wrap">
  {SP.stats_strip([(str(n), "startups and scale ups"), (str(fin), "in fintech"), ("$600M", "WSO2 exit to EQT, the largest so far")])}
  <h2 class="h-sub mt">Sri Lankan startups by sector</h2>
  {filters}
  <div class="st-grid">{cards}</div>
</div>
<div class="wrap narrow">
  <h2 class="h-sub mt">How we chose them</h2>
  <ul class="ticks">
    <li>Founded in Sri Lanka, or by Sri Lankans with their team or origin in Sri Lanka.</li>
    <li>A technology product or a business built on one. IT services and outsourcing firms are covered in our <a href="{prefix}companies/">company directory</a> instead.</li>
    <li>Active in 2025 or 2026, with at least one fact we could check: funding, users, an exit, a listing, an award or an accelerator.</li>
  </ul>
  <div class="reach mt"><h2>Looking to invest, partner or acquire?</h2><p>We introduce founders and teams to investors, corporate partners and companies looking for technology or talent in Sri Lanka.</p>
  <div class="actions"><a class="btn" href="{prefix}talent/find/?route=startups">Request an introduction</a><a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ghost" href="{prefix}guides/sri-lanka-startup-ecosystem/">Startup ecosystem guide</a></div></div>
  {faq}
  <p class="body-l mt">Related: <a href="{prefix}guides/sri-lanka-startup-ecosystem/">Sri Lanka's startup ecosystem</a> · <a href="{prefix}solutions/sri-lanka-for-startups/">Building a startup team in Sri Lanka</a> · <a href="{prefix}why-sri-lanka/ai/">AI in Sri Lanka</a> · <a href="{prefix}why-sri-lanka/fintech/">Fintech in Sri Lanka</a></p>
</div></section>
{JS}"""
    head = faq_ld + itemlist + SP.crumbs_ld(B, [("Guides", "guides/"), ("Top startups in Sri Lanka", PATH)])
    B.write(PATH + "index.html", B.page(f"Top {n} startups in Sri Lanka (2026)",
                                        f"The {n} Sri Lankan startups to know in 2026: tech, AI, fintech, healthtech and deeptech, with logos, founders, websites and a sourced fact for each.",
                                        body, prefix, PATH, extra_head=head, active="guides",
                                        seo_title=f"Top {n} startups in Sri Lanka (2026): tech, AI and fintech"))
    return [PATH]
