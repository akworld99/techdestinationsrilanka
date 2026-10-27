"""Source from Sri Lanka: a buyer hub for Sri Lankan exports with one page per export category, a request for quote page,
an import guide, and services for Sri Lankan exporters (Tender Radar alerts on WhatsApp, bid support and export consultancy).
Facts, figures and keywords live in source_data.py."""
import html
from urllib.parse import quote

import seo_pages as SP
from seo_pages import a
import source_data as D
from og_source import og_path
from source_cats import M

e = html.escape
REVIEWED = D.REVIEWED
WHATSAPP = "94716147945"   # Tender Radar and sourcing desk on WhatsApp


def wa(text):
    return f"https://wa.me/{WHATSAPP}?text={quote(text)}"


def lc(label):
    """The label inside a sentence: lower case unless it starts with a proper noun."""
    return label if label.split()[0] in ("Ceylon", "Ayurveda") else label[0].lower() + label[1:]


def _ev(items):
    return '<ul class="ticks">' + "".join(f"<li>{e(t)} {a(src, url)}</li>" for t, src, url in items) + "</ul>"


def _ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def _table(head, rows, slim=False):
    return (f'<div class="tbl{" slim" if slim else ""}"><table><thead><tr>' + "".join(f"<th>{e(h)}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")


def _glance(rows):
    return '<div class="tbl"><table><tbody>' + "".join(f'<tr><th scope="row">{e(k)}</th><td>{e(v)}</td></tr>' for k, v in rows) + "</tbody></table></div>"


def tiles(prefix_to_section, prefix_to_root, cats=None):
    cats = cats or D.CATS
    return '<div class="tile-grid five">' + "".join(
        f'<a class="tile" href="{prefix_to_section}{c["slug"]}/"><img src="{prefix_to_root}assets/art/{c["art"]}.svg" alt="{e(c["label"])} from Sri Lanka, illustration" loading="lazy" width="1200" height="900">'
        f'<span class="tile-body"><strong>{e(c["label"])}</strong><span>{e(c["short"])}</span></span></a>' for c in cats) + "</div>"


def _rfq_box(B, prefix, c=None):
    q = f"?product={c['slug']}" if c else ""
    what = lc(c["label"]) if c else "the product"
    msg = f"Hi, I want to source {what} from Sri Lanka."
    return f"""<div class="reach mt"><h2>Tell us what you need to source</h2>
  <p>Send the product, grade, quantity, destination and the certificates you need. We reply within two working days with Sri Lankan exporters who make it and already ship to markets like yours.</p>
  <div class="actions"><a class="btn" href="{prefix}source/request-a-quote/{q}">Request a quote</a><a class="btn btn-wa" href="{wa(msg)}" rel="noopener">WhatsApp us</a><a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a></div></div>"""


HOW_BUY = [
    ("Tell us the spec", "Product, grade, quantity, packing, destination port, the certificates you need and when you need the first shipment."),
    ("We shortlist exporters", "We match you with Sri Lankan exporters who make that product and already ship to markets like yours, and check them before we introduce them."),
    ("You deal direct", "Quotes and samples come from the exporters themselves and you choose. We stay on hand for the factory visit, the first order and the first shipment."),
]

CHECKS = [
    "The company is registered in Sri Lanka and listed as an exporter, through the Export Development Board directory or a chamber of commerce.",
    "The certificates you asked for exist, are current and cover the site that will make your order.",
    "It has shipped this product to your region before, and can show export documents or a buyer reference.",
    "It has the capacity for your volume and your delivery dates.",
    "A video call or a visit to the factory, on request, before you pay a deposit.",
]


ANSWERS = [  # (question, short answer, site path) for the site wide answers page
    ("What are Sri Lanka's main exports?", "Apparel and textiles (US$4.91 billion in 2025), tea (US$1.51 billion), coconut products (US$1.23 billion), rubber products (US$946 million), food and beverages, spices and essential oils, and electrical and electronic components.", "source/sri-lanka-export-statistics/"),
    ("How much did Sri Lanka export in 2025?", "US$17.25 billion of goods and services, up 5.6%: US$13.58 billion of goods and US$3.67 billion of services, according to the Export Development Board. January to September 2026 reached US$13.61 billion, up 5.04%.", "source/sri-lanka-export-statistics/"),
    ("Which countries buy the most from Sri Lanka?", "The United States, at about a fifth of goods exports, then India, the United Kingdom, Italy, Germany and the Netherlands.", "source/sri-lanka-export-statistics/"),
    ("Which Sri Lankan exports are growing fastest?", "Electrical and electronic components, up 61% in January to September 2026, spices and essential oils, up 30.5%, and food and beverages, up 20.9%.", "source/sri-lanka-export-statistics/"),
    ("How do I import from Sri Lanka?", "Agree the specification and terms with an exporter, check its registration and certificates, take samples, then ship from Colombo with a certificate of origin to claim any lower duty your country offers.", "source/how-to-import-from-sri-lanka/"),
    ("How do I find a supplier in Sri Lanka?", "Send us one request. Within two working days we come back with exporters who make your product, hold the certificates you need and already ship to markets like yours.", "source/request-a-quote/"),
    ("What is Tender Radar?", "A WhatsApp alert service for Sri Lankan exporters. It matches international tenders from UN agencies, development banks and utilities to what a company makes, with deadline reminders and a read on whether to bid.", "source/tender-radar/"),
]

def _steps(steps):
    return '<ol class="steps compact">' + "".join(f"<li><h3>{e(n)}</h3><p>{e(t)}</p></li>" for n, t in steps) + "</ol>"


def _promo(prefix, c):
    return f"""<aside class="promo"><img src="{prefix}assets/art/s-radar.svg" alt="" loading="lazy" width="1200" height="900"><div>
  <h2>Exporting {e(lc(c['label']))}? Get matched tenders on WhatsApp.</h2>
  <p>{e(c['tender'])}</p>
  <a class="door-go" href="{prefix}source/tender-radar/">See Tender Radar</a></div></aside>"""


# ------------------------------------------------------------------ category pages
def build_category(B, stories, c):
    prefix = "../../"
    path = f"source/{c['slug']}/"
    faq, faq_ld = SP.faq_block(stories, c["faqs"])
    products = _table(["Product", "HS code"], [(e(n), e(h)) for n, h in c["products"]])
    others = SP.chip_links([(x["label"], f"../{x['slug']}/") for x in D.CATS if x is not c])
    names = f'<p class="body-l">Also traded as: {e(", ".join(c["names"]))}.</p>' if c.get("names") else ""
    certs = _ticks([f"<strong>{e(n)}</strong> {e(t)}" for n, t in c["certs"]])
    caveats = _ev(c["caveats"]) if c.get("caveats") else ""
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Source from Sri Lanka", "../")])}
  <h1>{e(c['h1'])}</h1>
  <p class="answer">{e(c['answer'])}</p>
  <p class="reviewed">Last reviewed {REVIEWED}. Sources are linked next to each fact. We do not name buyers.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <img class="story-cover art" src="{prefix}assets/art/{c['art']}.svg" alt="{e(c['label'])} from Sri Lanka, illustration" width="1200" height="900">
  {SP.stats_strip(c['stats'])}
  <p class="cap">{c['stats_src']}</p>
  <h2 class="h-sub mt">{e(c['label'])} from Sri Lanka at a glance</h2>
  {_glance(c['glance'])}
  <h2 class="h-sub mt">What Sri Lankan exporters supply</h2>
  {products}
  <p class="cap">HS codes at heading or six digit level. Confirm the national tariff line in your market with your customs broker.</p>
  {names}
  <h2 class="h-sub mt">Why buyers source {e(lc(c['label']))} from Sri Lanka</h2>
  {_ev(c['evidence'])}
  <h2 class="h-sub mt">Certifications and standards to ask for</h2>
  {certs}
  {f'<h2 class="h-sub mt">Know this before you buy</h2>{caveats}' if caveats else ''}
  <h2 class="h-sub mt">Questions to ask a Sri Lankan {e(c['seller'])}</h2>
  {_ticks([e(q) for q in c['ask']])}
  <h2 class="h-sub mt">How we help you source {e(lc(c['label']))}</h2>
  {_steps(HOW_BUY)}
  {_rfq_box(B, prefix, c)}
  {_promo(prefix, c) if c.get('tender') else ''}
  {faq}
  <h2 class="h-sub mt">Other products from Sri Lanka</h2>
  {others}
  <p class="body-l mt">See also: <a href="../">All Sri Lankan export categories</a> · <a href="../how-to-import-from-sri-lanka/">How to import from Sri Lanka</a> · <a href="../request-a-quote/">Request a quote</a> · <a href="../for-exporters/">For Sri Lankan exporters</a></p>
</div></section>
"""
    url = f"{B.SITE_URL}/{path}"
    org = {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"}
    art = {"@context": "https://schema.org", "@type": "Article", "headline": c["h1"], "description": c["desc"], "datePublished": D.PUBLISHED, "dateModified": D.PUBLISHED,
           "author": org, "publisher": org, "mainEntityOfPage": url, "image": f"{B.SITE_URL}/" + (og_path(c["slug"]) or f"assets/art/{c['art']}.svg"), "inLanguage": "en", "about": [c["label"], "Sri Lanka", "Export"]}
    svc = {"@context": "https://schema.org", "@type": "Service", "name": f"Sourcing {lc(c['label'])} from Sri Lanka", "serviceType": "Supplier sourcing", "url": url,
           "provider": org, "areaServed": "Worldwide", "availableChannel": {"@type": "ServiceChannel", "serviceUrl": f"{B.SITE_URL}/source/request-a-quote/"}}
    head = faq_ld + SP.ld(art) + SP.ld(svc) + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), (c["label"], path)])
    B.write(path + "index.html", B.page(c["h1"], c["desc"], body, prefix, path, image=og_path(c["slug"]), extra_head=head, active="source", seo_title=c["title"]))
    return path


# ------------------------------------------------------------------ hub
def _bars():
    top = max(v for _, _, v, _, _ in D.SECTORS)
    rows = []
    for label, href, v, ytd, note in D.SECTORS:
        cls = "up" if ytd.startswith("+") else ("down" if ytd.startswith("\u2212") else "")
        name = f'<a href="{href}"><strong>{e(label)}</strong></a>' if href else f"<strong>{e(label)}</strong>"
        rows.append(f'<tr><td>{name}<br><span class="cap">{e(note)}</span></td><td class="bcell"><strong>{v:,.0f}</strong><span class="b" style="width:{max(v / top * 100, 1):.1f}%"></span></td><td class="{cls}">{e(ytd)}</td></tr>')
    return ('<div class="tbl bars"><table><colgroup><col style="width:44%"><col style="width:34%"><col style="width:22%"></colgroup><thead><tr><th>Category</th><th>2025 exports, US$ million</th><th>Jan to Sep 2026, change on a year earlier</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")


def build_hub(B, stories):
    prefix = "../"
    faq, faq_ld = SP.faq_block(stories, D.HUB_FAQS)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  <h1>Source from Sri Lanka: export products, exporters and how to buy</h1>
  <p class="answer">{e(D.HUB_ANSWER)}</p>
  <p class="reviewed">Last reviewed {REVIEWED}. Figures are from the Export Development Board, with sources linked. We do not name buyers.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  {SP.stats_strip(D.HUB_STATS)}
  <p class="cap">{D.HUB_STATS_SRC}</p>
  <h2 class="h-sub mt">How we help you buy from Sri Lanka</h2>
  {_steps(HOW_BUY)}
  <div class="actions"><a class="btn" href="request-a-quote/">Request a quote</a><a class="btn btn-wa" href="{wa("Hi, I want to source a product from Sri Lanka.")}" rel="noopener">WhatsApp us</a><a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a></div>
  <h2 class="h-sub mt">What Sri Lanka exports, by category</h2>
  {_bars()}
  <p class="cap">{D.BARS_SRC}</p>
  <p class="body-l">Full tables by product line and by country, with a CSV: <a href="sri-lanka-export-statistics/">Sri Lanka export statistics 2025 and 2026</a>.</p>
  <h2 class="h-sub mt">Buying for a specific market</h2>
  <p class="body-l">What each market buys from Sri Lanka, the duty it pays and the import rules to check:</p>
  {market_chips("")}
</div>
<div class="wrap"><h2 class="h-sub mt">Browse by product</h2>{tiles("", prefix)}</div>
<div class="wrap narrow">
  <h2 class="h-sub mt">What we check before we introduce an exporter</h2>
  {_ticks([e(x) for x in CHECKS])}
  <h2 class="h-sub mt">Trade access in one view</h2>
  {_ev(D.TRADE_SHORT)}
  <p class="body-l">Documents, shipping, payment and the steps to a first order are in our guide: <a href="how-to-import-from-sri-lanka/">how to import from Sri Lanka</a>.</p>
  <h2 class="h-sub mt">For Sri Lankan exporters</h2>
  <div class="offer2">
    <a class="offer offer-buy" href="tender-radar/"><h3>Tender Radar</h3><p>International tenders matched to what you make, sent to your WhatsApp, with a read on whether to bid.</p><span class="door-go">See Tender Radar</span></a>
    <a class="offer offer-sell" href="bid-support/"><h3>Bid support and export consultancy</h3><p>Decoding the tender, the compliance matrix, technical and commercial submissions, and the market entry work around them.</p><span class="door-go">See bid support</span></a>
  </div>
  {faq}
</div></section>
"""
    art = SP.ld({"@context": "https://schema.org", "@type": "CollectionPage", "name": "Source from Sri Lanka: exporters, products and how to buy", "url": f"{B.SITE_URL}/source/",
                 "description": D.HUB_DESC, "inLanguage": "en", "dateModified": D.PUBLISHED, "about": {"@type": "Country", "name": "Sri Lanka"},
                 "publisher": {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"},
                 "mainEntity": {"@type": "ItemList", "name": "Sri Lankan export product categories", "numberOfItems": len(D.CATS),
                                "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": c["label"], "url": f"{B.SITE_URL}/source/{c['slug']}/"} for i, c in enumerate(D.CATS)]}})
    head = faq_ld + art + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/")])
    B.write("source/index.html", B.page("Source from Sri Lanka: exporters, products and how to buy", D.HUB_DESC, body, prefix, "source/", image=og_path("hub"), extra_head=head, active="source", seo_title=D.HUB_TITLE))
    return "source/"


# ------------------------------------------------------------------ forms
def _form(B, kind, title, intro, fields, submit, done):
    """fields: (type, name, label, required, options); select options may be (value, label) pairs."""
    rows = []
    for typ, name, label, req, opt in fields:
        r = " required" if req else ""
        star = "" if req else ' <span class="opt">optional</span>'
        if typ == "select":
            ops = "".join(f'<option value="{e(o[0])}">{e(o[1])}</option>' if isinstance(o, tuple) else f"<option>{e(o)}</option>" for o in opt)
            rows.append(f'<label><span>{e(label)}{star}</span><select name="{name}"{r}>{ops}</select></label>')
        elif typ == "textarea":
            rows.append(f'<label class="wide"><span>{e(label)}{star}</span><textarea name="{name}" rows="4" placeholder="{e(opt or "")}"{r}></textarea></label>')
        elif typ == "checks":
            boxes = "".join(f'<label class="check"><input type="checkbox" name="{name}" value="{e(o)}"> {e(o)}</label>' for o in opt)
            rows.append(f'<fieldset class="wide"><legend>{e(label)}{star}</legend><div class="checks">{boxes}</div></fieldset>')
        elif typ == "consent":
            rows.append(f'<label class="check wide"><input type="checkbox" name="{name}" value="yes" required> {e(label)}</label>')
        else:
            rows.append(f'<label><span>{e(label)}{star}</span><input type="{typ}" name="{name}" placeholder="{e(opt or "")}"{r}></label>')
    return f"""
<form class="form" id="{kind}-form" data-form="{kind}" data-done="{e(done)}" action="{e(B.FORM_ENDPOINT)}" method="POST">
  <h2>{e(title)}</h2>
  {f'<p class="form-intro">{e(intro)}</p>' if intro else ''}
  <div class="fields">{''.join(rows)}</div>
  <input type="hidden" name="form" value="{kind}">
  <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" class="sr" aria-hidden="true">
  <button class="btn" type="submit">{e(submit)}</button>
  <p class="form-status" role="status"></p>
</form>"""


MARKET_CHOICES = ["Gulf and Middle East", "South Asia", "East Africa", "West and Southern Africa", "Southeast Asia", "Maldives and the Pacific", "Europe", "North America", "Australia and New Zealand"]


def build_rfq(B, stories):
    prefix = "../../"
    path = "source/request-a-quote/"
    products = [(c["slug"], c["label"]) for c in D.CATS] + [("other", "Something else")]
    form = _form(B, "rfq", "Request a quote", "Two minutes is enough. The more specific the spec, the better the match.", [
        ("select", "product", "Product category", True, products),
        ("textarea", "spec", "Product, grade or specification", True, "For example: Ceylon cinnamon quills, Alba grade, 10 kg cartons"),
        ("text", "quantity", "Quantity and how often", True, "For example: one 20 ft container a month"),
        ("text", "destination", "Destination country and port", True, "For example: Rotterdam, Netherlands"),
        ("select", "incoterms", "Delivery terms", False, ["Not sure yet", "FOB Colombo", "CFR or CIF to my port", "DAP or DDP to my door", "EXW, I arrange collection"]),
        ("checks", "certifications", "Certificates you need", False, ["Organic", "Fairtrade or Rainforest Alliance", "ISO 22000, FSSC 22000 or BRCGS", "Halal", "Kosher", "ISO 9001", "CE or UL", "Type tested to IEC", "Not sure"]),
        ("text", "timeline", "When you need the first shipment", False, "For example: March 2027"),
        ("text", "name", "Your name", True, ""),
        ("email", "email", "Work email", True, ""),
        ("text", "company", "Company", True, ""),
        ("text", "country", "Your country", True, ""),
        ("tel", "whatsapp", "WhatsApp number", False, "With country code"),
    ], "Send request", "Request received. We will reply by email within two working days.")
    faq, faq_ld = SP.faq_block(stories, D.RFQ_FAQS)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Source from Sri Lanka", "../")])}
  <h1>Request a quote from Sri Lankan exporters</h1>
  <p class="lede">Tell us what you are buying. We come back within two working days with exporters who make it, have the certificates you need and already ship to markets like yours. You deal with them directly.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  {form}
  <p class="cap mt-s">Prefer to talk? <a href="{wa("Hi, I want to source a product from Sri Lanka.")}" rel="noopener">WhatsApp us</a>, <a href="{B.BOOKING_URL}" rel="noopener">schedule a call</a> or email <a href="mailto:{B.EMAIL}">{B.EMAIL}</a>.</p>
  <h2 class="h-sub mt">What happens next</h2>
  {_steps(HOW_BUY)}
  <h2 class="h-sub mt">What we check before an introduction</h2>
  {_ticks([e(x) for x in CHECKS])}
  {faq}
  <p class="body-l mt">Browse first: <a href="../">all Sri Lankan export categories</a> · <a href="../how-to-import-from-sri-lanka/">how to import from Sri Lanka</a></p>
</div></section>
"""
    head = faq_ld + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), ("Request a quote", path)])
    B.write(path + "index.html", B.page("Request a quote from Sri Lankan exporters", "Send one request and get matched with Sri Lankan exporters who make your product, hold your certificates and ship to your market. Reply in two working days.",
                                        body, prefix, path, image=og_path("request-a-quote"), extra_head=head, active="source", seo_title="Request a quote from Sri Lankan exporters and suppliers"))
    return path


# ------------------------------------------------------------------ tender radar
def _alert():
    rows = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in D.SAMPLE_ALERT)
    return f"""<figure class="wa" aria-label="Sample Tender Radar alert on WhatsApp">
  <div class="wa-top"><span class="wa-av">TR</span><div><strong>Tender Radar</strong><span>Tech Destination Sri Lanka</span></div></div>
  <div class="wa-msg"><p class="wa-h">New tender match</p><dl>{rows}</dl>
    <p class="wa-read"><strong>Our read:</strong> {e(D.SAMPLE_READ)}</p><span class="wa-time">09:14</span></div>
  <figcaption>Sample alert. The details are illustrative. Real alerts name the buyer and link to the tender notice.</figcaption>
</figure>"""


def _plans(prefix):
    out = []
    for i, (name, who, items, cta, href) in enumerate(D.PLANS):
        out.append(f'<div class="plan{" is-main" if i == 1 else ""}"><h3>{e(name)}</h3><p class="for">{e(who)}</p>{_ticks([e(x) for x in items])}<a class="door-go" href="{href}">{e(cta)}</a></div>')
    return '<div class="plans">' + "".join(out) + "</div>"


def build_radar(B, stories):
    prefix = "../../"
    path = "source/tender-radar/"
    form = _form(B, "tender-radar", "Set up your Tender Radar", "Tell us what you make and where you can deliver. We send matched tenders to your WhatsApp.", [
        ("text", "company", "Company", True, ""),
        ("text", "name", "Your name", True, ""),
        ("email", "email", "Work email", True, ""),
        ("tel", "whatsapp", "WhatsApp number for alerts", True, "With country code"),
        ("textarea", "products", "What you make", True, "Products, ratings or sizes. For example: distribution transformers 25 to 1,000 kVA, 11 and 33 kV"),
        ("checks", "markets", "Where you can deliver", True, MARKET_CHOICES),
        ("textarea", "certifications", "Certificates and type tests you hold", False, "For example: ISO 9001, IEC 60076 type tests at an accredited lab"),
        ("select", "experience", "Overseas tender experience", True, ["We have not bid overseas yet", "We have bid a few times", "We bid regularly"]),
        ("consent", "consent", "I agree to receive tender alerts on WhatsApp and can stop them at any time by replying STOP.", True, ""),
    ], "Start my radar", "Received. We will message you on WhatsApp to confirm your profile.")
    faq, faq_ld = SP.faq_block(stories, D.RADAR_FAQS)
    cover = _table(["Sector", "Tenders we track"], [(f"<strong>{e(s)}</strong>", e(t)) for s, t in D.RADAR_SECTORS])
    body = f"""
<section class="page-head"><div class="wrap split">
  <div>
    {SP.crumb_html([("Source from Sri Lanka", "../"), ("For exporters", "../for-exporters/")])}
    <h1>Tender Radar: international tender alerts on WhatsApp</h1>
    <p class="lede">{e(D.RADAR_LEDE)}</p>
    <div class="actions"><a class="btn btn-wa" href="{wa("Hi, I want Tender Radar alerts for my products.")}" rel="noopener">Start on WhatsApp</a><a class="btn btn-ghost" href="#tender-radar-form">Set up with the form</a></div>
  </div>
  {_alert()}
</div></section>
<section class="section"><div class="wrap narrow">
  <h2 class="h-sub">Why exporters miss tenders they could win</h2>
  {_ticks([e(x) for x in D.RADAR_WHY])}
  <h2 class="h-sub mt">How it works</h2>
  {_steps(D.RADAR_STEPS)}
  <h2 class="h-sub mt">What Tender Radar covers</h2>
  {cover}
  <h2 class="h-sub mt">Where the tenders come from</h2>
  {_ev(D.RADAR_SOURCES)}
  <h2 class="h-sub mt">What a tender will ask you for</h2>
  {_ev(D.TENDER_REQS)}
  <p class="body-l">Gaps here are what sink first bids. Our <a href="../bid-support/">bid support</a> starts by checking your documents against the tender before you spend time on the price.</p>
</div>
<div class="wrap"><h2 class="h-sub mt">Plans</h2>{_plans(prefix)}</div>
<div class="wrap narrow">
  {form}
  {faq}
  <p class="body-l mt">See also: <a href="../bid-support/">Bid support and export consultancy</a> · <a href="../for-exporters/">All services for exporters</a> · <a href="../electrical-cables-transformers/">Electrical exports from Sri Lanka</a></p>
</div></section>
"""
    svc = SP.ld({"@context": "https://schema.org", "@type": "Service", "name": "Tender Radar: international tender alerts on WhatsApp", "serviceType": "Tender alert service",
                 "description": D.RADAR_DESC, "url": f"{B.SITE_URL}/{path}", "provider": {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"},
                 "areaServed": {"@type": "Country", "name": "Sri Lanka"}, "availableChannel": {"@type": "ServiceChannel", "serviceUrl": wa("Tender Radar")}})
    head = faq_ld + svc + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), ("For exporters", "source/for-exporters/"), ("Tender Radar", path)])
    B.write(path + "index.html", B.page("Tender Radar: international tender alerts on WhatsApp", D.RADAR_DESC, body, prefix, path, image=og_path("tender-radar"), extra_head=head, active="source", seo_title=D.RADAR_TITLE))
    return path


# ------------------------------------------------------------------ bid support and consultancy
def build_bid(B, stories):
    prefix = "../../"
    path = "source/bid-support/"
    form = _form(B, "bid-review", "Book a bid review", "Send the tender you are looking at. We read it and tell you what it will take to bid, and whether we think you should.", [
        ("text", "tender", "Tender link or reference", True, ""),
        ("date", "deadline", "Submission deadline", False, ""),
        ("text", "product", "What is being bought", True, ""),
        ("text", "company", "Company", True, ""),
        ("text", "name", "Your name", True, ""),
        ("email", "email", "Work email", True, ""),
        ("tel", "whatsapp", "WhatsApp number", False, "With country code"),
        ("select", "help", "What you need", True, ["A go or no go review", "Help preparing the whole bid", "Help with one part: technical, commercial or documents", "Export consultancy, not a specific tender"]),
    ], "Request review", "Received. We will reply within one working day.")
    faq, faq_ld = SP.faq_block(stories, D.BID_FAQS)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Source from Sri Lanka", "../"), ("For exporters", "../for-exporters/")])}
  <h1>Tender bid support and export consultancy for Sri Lankan manufacturers</h1>
  <p class="answer">{e(D.BID_ANSWER)}</p>
  <div class="actions"><a class="btn" href="#bid-review-form">Book a bid review</a><a class="btn btn-wa" href="{wa("Hi, I need help with a tender.")}" rel="noopener">WhatsApp us</a><a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a></div>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <img class="story-cover art" src="{prefix}assets/art/s-bid.svg" alt="Tender bid support, illustration" width="1200" height="900">
  <h2 class="h-sub mt">What we do on a bid</h2>
  {_steps(D.BID_STEPS)}
  <h2 class="h-sub mt">Export consultancy around the bid</h2>
  {_ticks([f"<strong>{e(n)}</strong> {e(t)}" for n, t in D.CONSULT])}
  <h2 class="h-sub mt">How we work with you</h2>
  {_ticks([e(x) for x in D.BID_PRINCIPLES])}
  <h2 class="h-sub mt">Who you work with</h2>
  <p class="body-l">{e(D.BID_TEAM)}</p>
  {form}
  {faq}
  <p class="body-l mt">See also: <a href="../tender-radar/">Tender Radar alerts on WhatsApp</a> · <a href="../for-exporters/">All services for exporters</a></p>
</div></section>
"""
    svc = SP.ld({"@context": "https://schema.org", "@type": "Service", "name": "Tender bid support and export consultancy", "serviceType": "Bid writing and tender consultancy",
                 "description": D.BID_DESC, "url": f"{B.SITE_URL}/{path}", "provider": {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"}, "areaServed": {"@type": "Country", "name": "Sri Lanka"}})
    how = SP.ld({"@context": "https://schema.org", "@type": "HowTo", "name": "How to prepare an international tender bid", "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate(D.BID_STEPS)]})
    head = faq_ld + svc + how + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), ("For exporters", "source/for-exporters/"), ("Bid support", path)])
    B.write(path + "index.html", B.page("Tender bid support and export consultancy for Sri Lankan manufacturers", D.BID_DESC, body, prefix, path, image=og_path("bid-support"), extra_head=head, active="source", seo_title=D.BID_TITLE))
    return path


# ------------------------------------------------------------------ for exporters
def build_exporters(B, stories):
    prefix = "../../"
    path = "source/for-exporters/"
    form = _form(B, "exporter", "Join the exporter network", "Tell us what you make. We use it to match you with buyer requests and tenders.", [
        ("text", "company", "Company", True, ""),
        ("text", "website", "Website", False, ""),
        ("select", "category", "Main category", True, [(c["slug"], c["label"]) for c in D.CATS] + [("other", "Something else")]),
        ("textarea", "products", "Products and HS codes", True, "For example: solid tyres for forklifts, HS 4012.90"),
        ("textarea", "certifications", "Certificates you hold", False, "For example: ISO 9001, BRCGS, organic EU"),
        ("checks", "markets", "Markets you already ship to", False, MARKET_CHOICES),
        ("text", "capacity", "Monthly capacity", False, "For example: 8 containers a month"),
        ("text", "name", "Your name", True, ""),
        ("email", "email", "Work email", True, ""),
        ("tel", "whatsapp", "WhatsApp number", True, "With country code"),
    ], "Join", "Received. We will message you on WhatsApp to confirm your profile.")
    faq, faq_ld = SP.faq_block(stories, D.EXP_FAQS)
    svcs = "".join(f'<a class="door has-art" href="{h}"><img class="door-art" src="{prefix}assets/art/{art}.svg" alt="" loading="lazy" width="1200" height="900"><h3>{e(t)}</h3><p>{e(d)}</p><span class="door-go">{e(c)}</span></a>' for art, t, d, h, c in D.EXP_SERVICES)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Source from Sri Lanka", "../")])}
  <h1>Win overseas buyers and tenders: services for Sri Lankan exporters</h1>
  <p class="answer">{e(D.EXP_ANSWER)}</p>
</div></section>
<section class="section top-0"><div class="wrap">
  <div class="doors wrap3">{svcs}</div>
</div>
<div class="wrap narrow">
  <h2 class="h-sub mt">How buyers find you through us</h2>
  {_ticks([e(x) for x in D.EXP_HOW])}
  {form}
  {faq}
</div></section>
"""
    head = faq_ld + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), ("For exporters", path)])
    B.write(path + "index.html", B.page("Services for Sri Lankan exporters: buyers, tenders and bids", D.EXP_DESC, body, prefix, path, image=og_path("for-exporters"), extra_head=head, active="source", seo_title=D.EXP_TITLE))
    return path


# ------------------------------------------------------------------ import guide
def build_guide(B, stories):
    prefix = "../../"
    path = "source/how-to-import-from-sri-lanka/"
    faq, faq_ld = SP.faq_block(stories, D.GUIDE_FAQS)
    sections = "".join(f'<h2 class="h-sub mt" id="{sid}">{e(h)}</h2>' + (f'<p class="body-l">{e(intro)}</p>' if intro else "") + _ev(items) for sid, h, intro, items in D.GUIDE_SECTIONS)
    toc = '<nav class="toc" aria-label="On this page"><strong>On this page</strong><ol>' + "".join(f'<li><a href="#{sid}">{e(h)}</a></li>' for sid, h, _, _ in D.GUIDE_SECTIONS) + "</ol></nav>"
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Source from Sri Lanka", "../")])}
  <h1>How to import from Sri Lanka: trade deals, documents, shipping and payment</h1>
  <p class="answer">{e(D.GUIDE_ANSWER)}</p>
  <p class="reviewed">Last reviewed {REVIEWED}. General information with sources linked, not legal or customs advice.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <img class="story-cover art" src="{prefix}assets/art/s-import.svg" alt="Importing from Sri Lanka, illustration" width="1200" height="900">
  {toc}
  <h2 class="h-sub mt" id="steps">Your first order from Sri Lanka, step by step</h2>
  {_steps(D.GUIDE_STEPS)}
  {sections}
  <h2 class="h-sub mt" id="by-market">Guides by market</h2>
  {market_chips("../")}
  {_rfq_box(B, prefix)}
  {faq}
  <p class="body-l mt">Browse products: <a href="../">all Sri Lankan export categories</a></p>
</div></section>
"""
    art = SP.ld({"@context": "https://schema.org", "@type": "Article", "headline": "How to import from Sri Lanka", "description": D.GUIDE_DESC, "datePublished": D.PUBLISHED, "dateModified": D.PUBLISHED,
                 "author": {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"}, "publisher": {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"},
                 "mainEntityOfPage": f"{B.SITE_URL}/{path}", "image": f"{B.SITE_URL}/assets/art/s-import.svg"})
    how = SP.ld({"@context": "https://schema.org", "@type": "HowTo", "name": "How to import from Sri Lanka", "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate(D.GUIDE_STEPS)]})
    head = faq_ld + art + how + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), ("How to import from Sri Lanka", path)])
    B.write(path + "index.html", B.page("How to import from Sri Lanka", D.GUIDE_DESC, body, prefix, path, image=og_path("how-to-import-from-sri-lanka"), extra_head=head, active="source", seo_title=D.GUIDE_TITLE))
    return path


# ------------------------------------------------------------------ export statistics
def _usd(v):
    return "–" if v is None else f"{v:,.2f}"


def _chg(c):
    if not c:
        return "–"
    return f'<span class="{"down" if c.startswith(M) else "up"}">{e(c)}</span>'


def _lnk(label, href, prefix):
    """Link from a page one level inside /source/: category slugs and ../root paths both gain one ../"""
    return f'<a href="{prefix}{href}">{e(label)}</a>' if href else e(label)


def build_stats(B, stories):
    import source_stats as X
    prefix = "../"
    path = "source/sri-lanka-export-statistics/"
    faq, faq_ld = SP.faq_block(stories, X.FAQS)
    rows = [[f"<strong>{e(l)}</strong>", _usd(v1), _chg(c1), _usd(v2), _chg(c2)] for l, v1, c1, v2, c2 in X.TOTALS]
    head5 = ["", "2025, US$ million", "Change", "Jan to Sep 2026, US$ million", "Change"]
    sect = [[_lnk(l, h, prefix), _usd(v1), _chg(c1), _usd(v2), _chg(c2)] for l, h, v1, c1, v2, c2 in X.SECTORS]
    serv = [[_lnk(l, h, prefix), _usd(v1), _chg(c1), _usd(v2), _chg(c2)] for l, h, v1, c1, v2, c2 in X.SERVICES]
    lines = [[_lnk(l, h, prefix), _usd(v), _chg(c)] for l, h, v, c in X.LINES]
    mkts = [[e(l), _usd(v1), _chg(c1), _usd(v2), _chg(c2)] for l, v1, c1, v2, c2 in X.MARKETS]
    products = "".join(f'<li><a href="../{c["slug"]}/">{e(c["label"])}</a></li>' for c in D.CATS)
    csv_name = "sri-lanka-exports-2025-2026.csv"
    B.write("data/" + csv_name, "\n".join(",".join(f'"{x}"' if "," in x else x for x in r) for r in X.csv_rows()) + "\n")
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Source from Sri Lanka", "../")])}
  <h1>{e(X.H1)}</h1>
  <p class="answer">{e(X.ANSWER)}</p>
  <p class="reviewed">Last reviewed {REVIEWED}. Figures from the Export Development Board, linked below each table.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  {SP.stats_strip(X.STATS)}
  <nav class="toc" aria-label="On this page"><strong>On this page</strong><ol>
    <li><a href="#totals">Total exports</a></li><li><a href="#by-product">Exports by product</a></li><li><a href="#lines">Fastest growing product lines</a></li>
    <li><a href="#by-country">Exports by country</a></li><li><a href="#changes">What changed in 2026</a></li><li><a href="#list">Main export products list</a></li></ol></nav>
  <h2 class="h-sub mt" id="totals">Sri Lanka's total exports, 2025 and 2026</h2>
  {_table(head5, rows)}
  <h2 class="h-sub mt" id="by-product">Sri Lanka exports by product</h2>
  <p class="body-l">Goods by sector, largest first, with services below. Each product links to our buyer's guide for it.</p>
  {_table(head5, sect + [[f"<strong>Services</strong>", "", "", "", ""]] + serv)}
  <p class="cap">{X.SRC}</p>
  <h2 class="h-sub mt" id="lines">Fastest growing product lines, January to September 2026</h2>
  {_table(["Product line", "Jan to Sep 2026, US$ million", "Change on Jan to Sep 2025"], lines, slim=True)}
  <p class="cap">Source: Export Development Board, <a href="{X.EDB9M_EDB}" rel="noopener">January to September 2026</a>. A dash means the release gave the growth rate but not the value.</p>
  <h2 class="h-sub mt" id="by-country">Sri Lanka exports by country</h2>
  <p class="body-l">Goods exports to the largest markets. The United States takes about a fifth of Sri Lanka's goods exports.</p>
  {_table(["Market", "2025, US$ million", "Change", "Jan to Sep 2026, US$ million", "Change"], mkts)}
  <p class="cap">{X.SRC}</p>
  <p class="body-l">What each market buys, its duty access and import rules:</p>
  {market_chips("../")}
  <h2 class="h-sub mt" id="changes">What changed in 2026</h2>
  {_ev(X.SHIFTS)}
  <h2 class="h-sub mt" id="list">Sri Lanka's main export products list</h2>
  <p class="body-l">Every category we cover, with products, HS codes, certificates, markets and how to buy:</p>
  <ul class="names roles">{products}</ul>
  <div class="cite"><strong>Use this data.</strong> Free to quote, chart or republish with a link to this page. <a href="../../data/{csv_name}" download>Download the CSV</a>.<br><span>Suggested credit: Tech Destination Sri Lanka, Sri Lanka export statistics 2025 and 2026, from Export Development Board data, {B.SITE_URL}/{path}</span></div>
  {_rfq_box(B, "../../")}
  {faq}
</div></section>
"""
    org = {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"}
    ds = SP.ld({"@context": "https://schema.org", "@type": "Dataset", "name": "Sri Lanka export statistics 2025 and January to September 2026",
                "description": "Sri Lanka goods and services exports in US$ million for 2025 and January to September 2026, by sector, product line and market, compiled from Export Development Board releases.",
                "url": f"{B.SITE_URL}/{path}", "creator": org, "publisher": org, "license": "https://creativecommons.org/licenses/by/4.0/", "isAccessibleForFree": True,
                "isBasedOn": [X.EDB25, X.EDB9M_EDB], "temporalCoverage": "2025-01-01/2026-09-30", "spatialCoverage": {"@type": "Place", "name": "Sri Lanka"},
                "dateModified": D.PUBLISHED, "keywords": ["Sri Lanka exports", "Sri Lanka export statistics", "Sri Lanka exports by country", "Sri Lanka export products", "Sri Lanka export income"],
                "variableMeasured": ["Export value (US$ million)", "Year on year change (%)"],
                "distribution": [{"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": f"{B.SITE_URL}/data/{csv_name}"}]})
    art = SP.ld({"@context": "https://schema.org", "@type": "Article", "headline": X.H1, "description": X.DESC, "datePublished": D.PUBLISHED, "dateModified": D.PUBLISHED,
                 "author": org, "publisher": org, "mainEntityOfPage": f"{B.SITE_URL}/{path}", "image": f"{B.SITE_URL}/" + (og_path("sri-lanka-export-statistics") or "assets/share.jpg")})
    head = faq_ld + ds + art + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), ("Export statistics", path)])
    B.write(path + "index.html", B.page("Sri Lanka export statistics", X.DESC, body, "../../", path, image=og_path("sri-lanka-export-statistics"), extra_head=head, active="source", seo_title=X.TITLE))
    return path


# ------------------------------------------------------------------ buyer market pages
def market_chips(prefix):
    import source_markets as MK
    return '<ul class="names roles">' + "".join(f'<li><a href="{prefix}{m["slug"]}/">{e("Import to " + m["short"])}</a></li>' for m in MK.MARKETS) + "</ul>"


def build_market(B, stories, m):
    import source_markets as MK
    prefix = "../../"
    path = f"source/{m['slug']}/"
    faq, faq_ld = SP.faq_block(stories, m["faqs"])
    by_slug = {c["slug"]: c for c in D.CATS}
    rows = [[(f'<a href="../{cs}/">{e(p)}</a>' if cs else (f"<strong>{e(p)}</strong>" if p == "All goods" else e(p)))] + [(f"<strong>{_usd(v)}</strong>" if p == "All goods" else _usd(v)) for v in vals]
            for p, vals, cs in m["top"]["rows"]]
    cats = [by_slug[x] for x in m["cats"] if x in by_slug]
    others = "".join(f'<li><a href="../{x["slug"]}/">{e("Import to " + x["short"])}</a></li>' for x in MK.MARKETS if x is not m)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Source from Sri Lanka", "../")])}
  <h1>{e(m['h1'])}</h1>
  <p class="answer">{e(m['answer'])}</p>
  <p class="reviewed">Last reviewed {REVIEWED}. General information with sources linked, not legal or customs advice. We do not name buyers.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  {SP.stats_strip(m['stats'])}
  <h2 class="h-sub mt">What {e(m['the'])} buys from Sri Lanka</h2>
  {_table(m["top"]["head"], rows, slim=len(m["top"]["head"]) <= 3)}
  <p class="cap">{m['top']['src']}</p>
  <h2 class="h-sub mt">Duty and trade access</h2>
  {_ev(m['duty'])}
  <h2 class="h-sub mt">Import rules to check in {e(m['the'])}</h2>
  {_ev(m['rules'])}
  <p class="body-l">Documents, shipping from Colombo and payment terms are in the full guide: <a href="../how-to-import-from-sri-lanka/">how to import from Sri Lanka</a>. Figures for every market: <a href="../sri-lanka-export-statistics/">Sri Lanka export statistics</a>.</p>
</div>
<div class="wrap"><h2 class="h-sub mt">Products buyers in {e(m['the'])} source from Sri Lanka</h2>{tiles("../", prefix, cats)}</div>
<div class="wrap narrow">
  <h2 class="h-sub mt">How we help you buy</h2>
  {_steps(HOW_BUY)}
  <div class="reach mt"><h2>Sourcing for {e(m['the'])}?</h2>
  <p>Send the product, grade, quantity and the certificates {e(m['the'])} requires. We reply within two working days with Sri Lankan exporters who make it and already ship to {e(m['the'])} or markets like it.</p>
  <div class="actions"><a class="btn" href="../request-a-quote/?to={quote(m['to'])}">Request a quote</a><a class="btn btn-wa" href="{wa("Hi, I want to source from Sri Lanka for " + m["the"] + ".")}" rel="noopener">WhatsApp us</a><a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a></div></div>
  {faq}
  <h2 class="h-sub mt">Other markets</h2>
  <ul class="names roles">{others}</ul>
</div></section>
"""
    org = {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"}
    art = SP.ld({"@context": "https://schema.org", "@type": "Article", "headline": m["h1"], "description": m["desc"], "datePublished": D.PUBLISHED, "dateModified": D.PUBLISHED,
                 "author": org, "publisher": org, "mainEntityOfPage": f"{B.SITE_URL}/{path}", "inLanguage": "en",
                 "image": f"{B.SITE_URL}/" + (og_path(m["slug"]) or "assets/share.jpg"), "about": ["Sri Lanka", m["label"], "Import", "Export"],
                 "spatialCoverage": [{"@type": "Country", "name": "Sri Lanka"}, {"@type": "Place", "name": m["label"]}]})
    head = faq_ld + art + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), (f"Import to {m['short']}", path)])
    B.write(path + "index.html", B.page(m["h1"], m["desc"], body, prefix, path, image=og_path(m["slug"]), extra_head=head, active="source", seo_title=m["title"]))
    return path


def build_markets(B, stories):
    try:
        import source_markets as MK
    except ImportError:
        return []
    return [build_market(B, stories, m) for m in MK.MARKETS]


# ------------------------------------------------------------------ homepage band
def home_section(B):
    feat = [c for c in D.CATS if c["slug"] in D.HOME_TILES]
    feat.sort(key=lambda c: D.HOME_TILES.index(c["slug"]))
    stats = "".join(f"<li><strong>{e(v)}</strong><span>{e(l)}</span></li>" for v, l in D.HOME_STATS)
    return f"""<section class="section src">
  <div class="wrap">
    <div class="src-head">
      <div>
        <p class="eyebrow">Source from Sri Lanka</p>
        <h2>Buy direct from Sri Lankan exporters</h2>
        <p class="src-lede">{e(D.HOME_LEDE)}</p>
        <div class="actions"><a class="btn" href="source/request-a-quote/">Request a quote</a><a class="btn btn-ghost" href="source/">Browse all products</a></div>
      </div>
      <ul class="src-stats">{stats}</ul>
    </div>
    {tiles("source/", "", feat)}
    <div class="offer2">
      <a class="offer offer-buy" href="source/request-a-quote/"><h3>Buying from Sri Lanka?</h3><p>Send one request. We come back within two working days with exporters who make it, hold your certificates and ship to your market.</p><span class="door-go">Request a quote</span></a>
      <a class="offer offer-sell" href="source/tender-radar/"><h3>Exporting from Sri Lanka?</h3><p>Tender Radar sends international tenders matched to what you make to your WhatsApp, and our bid desk helps you win them.</p><span class="door-go">See Tender Radar</span></a>
    </div>
  </div>
</section>"""


def build(B, stories):
    import art_source
    art_source.write_all(B.ROOT)
    paths = [build_category(B, stories, c) for c in D.CATS]
    paths += [build_hub(B, stories), build_rfq(B, stories), build_radar(B, stories), build_bid(B, stories), build_exporters(B, stories), build_guide(B, stories), build_stats(B, stories)]
    paths += build_markets(B, stories)
    return paths


def llms_lines(B):
    import source_stats as X
    lines = ["", "## Sri Lanka export facts"] + [f"- {q} {ans}" for q, ans in X.FAQS[:6]]
    lines += ["", "## Source products from Sri Lanka", f"- [Source from Sri Lanka: exporters, products and how to buy]({B.SITE_URL}/source/): {D.HUB_ANSWER}",
              f"- [{X.H1}]({B.SITE_URL}/source/sri-lanka-export-statistics/): {X.ANSWER} CSV: {B.SITE_URL}/data/sri-lanka-exports-2025-2026.csv"]
    lines += [f"- [{c['h1']}]({B.SITE_URL}/source/{c['slug']}/): {c['answer']}" for c in D.CATS]
    lines += [f"- [How to import from Sri Lanka]({B.SITE_URL}/source/how-to-import-from-sri-lanka/): {D.GUIDE_ANSWER}",
              f"- [Request a quote from Sri Lankan exporters]({B.SITE_URL}/source/request-a-quote/)"]
    import source_markets as MK
    lines += [f"- [{m['h1']}]({B.SITE_URL}/source/{m['slug']}/): {m['answer']}" for m in MK.MARKETS]
    lines += [
              "", "## Services for Sri Lankan exporters",
              f"- [Tender Radar: international tender alerts on WhatsApp]({B.SITE_URL}/source/tender-radar/): {D.RADAR_DESC}",
              f"- [Tender bid support and export consultancy]({B.SITE_URL}/source/bid-support/): {D.BID_DESC}",
              f"- [Services for Sri Lankan exporters]({B.SITE_URL}/source/for-exporters/): {D.EXP_DESC}"]
    return lines
