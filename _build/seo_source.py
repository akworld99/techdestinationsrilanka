"""Source from Sri Lanka: a buyer hub for Sri Lankan exports with one page per export category, a request for quote page,
an import guide, and services for Sri Lankan exporters (Tender Radar alerts on WhatsApp, bid support and export consultancy).
Facts, figures and keywords live in source_data.py."""
import html
from urllib.parse import quote

import seo_pages as SP
from seo_pages import a
import source_data as D

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


def _table(head, rows):
    return ('<div class="tbl"><table><thead><tr>' + "".join(f"<th>{e(h)}</th>" for h in head) + "</tr></thead><tbody>"
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
           "author": org, "publisher": org, "mainEntityOfPage": url, "image": f"{B.SITE_URL}/assets/art/{c['art']}.svg", "inLanguage": "en", "about": [c["label"], "Sri Lanka", "Export"]}
    svc = {"@context": "https://schema.org", "@type": "Service", "name": f"Sourcing {lc(c['label'])} from Sri Lanka", "serviceType": "Supplier sourcing", "url": url,
           "provider": org, "areaServed": "Worldwide", "availableChannel": {"@type": "ServiceChannel", "serviceUrl": f"{B.SITE_URL}/source/request-a-quote/"}}
    head = faq_ld + SP.ld(art) + SP.ld(svc) + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/"), (c["label"], path)])
    B.write(path + "index.html", B.page(c["h1"], c["desc"], body, prefix, path, extra_head=head, active="source", seo_title=c["title"]))
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
                 "description": D.HUB_DESC, "hasPart": [{"@type": "WebPage", "name": c["h1"], "url": f"{B.SITE_URL}/source/{c['slug']}/"} for c in D.CATS]})
    head = faq_ld + art + SP.crumbs_ld(B, [("Source from Sri Lanka", "source/")])
    B.write("source/index.html", B.page("Source from Sri Lanka: exporters, products and how to buy", D.HUB_DESC, body, prefix, "source/", extra_head=head, active="source", seo_title=D.HUB_TITLE))
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
    B.write(path + "index.html", B.page("Request a quote from Sri Lankan exporters", "Send one request and get matched with Sri Lankan exporters who make your product, hold the certificates you need and ship to your market. Reply within two working days.",
                                        body, prefix, path, extra_head=head, active="source", seo_title="Request a quote from Sri Lankan exporters and suppliers"))
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
    B.write(path + "index.html", B.page("Tender Radar: international tender alerts on WhatsApp", D.RADAR_DESC, body, prefix, path, extra_head=head, active="source", seo_title=D.RADAR_TITLE))
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
    B.write(path + "index.html", B.page("Tender bid support and export consultancy for Sri Lankan manufacturers", D.BID_DESC, body, prefix, path, extra_head=head, active="source", seo_title=D.BID_TITLE))
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
    B.write(path + "index.html", B.page("Services for Sri Lankan exporters: buyers, tenders and bids", D.EXP_DESC, body, prefix, path, extra_head=head, active="source", seo_title=D.EXP_TITLE))
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
    B.write(path + "index.html", B.page("How to import from Sri Lanka", D.GUIDE_DESC, body, prefix, path, extra_head=head, active="source", seo_title=D.GUIDE_TITLE))
    return path


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
    paths += [build_hub(B, stories), build_rfq(B, stories), build_radar(B, stories), build_bid(B, stories), build_exporters(B, stories), build_guide(B, stories)]
    return paths


def llms_lines(B):
    lines = ["", "## Source products from Sri Lanka", f"- [Source from Sri Lanka: exporters, products and how to buy]({B.SITE_URL}/source/): {D.HUB_ANSWER}"]
    lines += [f"- [{c['h1']}]({B.SITE_URL}/source/{c['slug']}/): {c['answer']}" for c in D.CATS]
    lines += [f"- [How to import from Sri Lanka]({B.SITE_URL}/source/how-to-import-from-sri-lanka/): {D.GUIDE_ANSWER}",
              f"- [Request a quote from Sri Lankan exporters]({B.SITE_URL}/source/request-a-quote/)",
              "", "## Services for Sri Lankan exporters",
              f"- [Tender Radar: international tender alerts on WhatsApp]({B.SITE_URL}/source/tender-radar/): {D.RADAR_DESC}",
              f"- [Tender bid support and export consultancy]({B.SITE_URL}/source/bid-support/): {D.BID_DESC}",
              f"- [Services for Sri Lankan exporters]({B.SITE_URL}/source/for-exporters/): {D.EXP_DESC}"]
    return lines
