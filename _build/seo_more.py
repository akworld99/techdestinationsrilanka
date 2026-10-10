"""Role pages (/hire/...), the featured badge page and the privacy page."""
import html

import seo_pages as SP

e = html.escape

# (slug, plural role, h1 keyword, [(label, median LKR thousands)], proof [(story, text)], extra sentence)
ROLES = [
    dict(slug="software-engineers", role="software engineers", short="Software engineers",
         pay=[("Associate software engineer", 93), ("Software engineer", 177), ("Senior software engineer", 260), ("Associate technical lead", 365), ("Software architect", 661)],
         proof=[("sysco-labs", "Full stack engineers on the same codebase as Sysco's US teams."), ("wso2", "780 engineers building API, integration and identity products."),
                ("virtusa", "3,000+ engineers serving Fortune 500 clients from Colombo."), ("creative-software", "Dedicated product teams for Scandinavian software companies."),
                ("gapstars", "Engineers embedded in European scaleups."), ("tiqri", "150 developers with client relationships of ten years and more.")],
         note="Java, .NET, JavaScript and TypeScript, Python and mobile stacks are all widely used at the companies below."),
    dict(slug="qa-engineers", role="QA and test automation engineers", short="QA engineers",
         pay=[("QA engineer", 101), ("Senior QA engineer", 205)],
         proof=[("xeynergy", "QA and test automation as part of full lifecycle delivery for US clients."), ("tiqri", "QA within dedicated long term product teams."),
                ("dijital-team", "QA specialists in a 200 person team built in two years."), ("sysco-labs", "Quality engineering as a core discipline.")],
         note="Test automation is the norm at export companies, alongside manual and exploratory testing."),
    dict(slug="devops-engineers", role="DevOps and cloud engineers", short="DevOps and cloud engineers",
         pay=[("DevOps engineer", 202), ("Senior DevOps engineer", 333)],
         proof=[("superloop", "Cloud, infrastructure and 24x7 network operations for an Australian carrier."), ("sysco-labs", "Cloud infrastructure for a Fortune 500 distributor."),
                ("xeynergy", "DevOps and support across the technology lifecycle."), ("dijital-team", "Network engineers and infrastructure specialists.")],
         note="Because Colombo's day covers the European morning and the Australian afternoon, teams here are often used for round the clock operations."),
    dict(slug="data-ai-engineers", role="data and AI engineers", short="Data and AI engineers",
         pay=[("Data engineer", 215), ("Senior data engineer", 364), ("Data scientist", 217), ("Machine learning engineer", 233)],
         proof=[("roar-global", "Built an AI gateway to 200+ models and runs an applied AI research lab."), ("xeynergy", "Ships its own agentic AI products."),
                ("rootcode", "AI platforms for the Estonian government."), ("sysco-labs", "Data, analytics and machine learning for pricing and supply chain.")],
         note="See also our page on why AI companies build in Sri Lanka."),
    dict(slug="erp-consultants", role="ERP consultants", short="ERP and IFS consultants",
         pay=[("ERP consultant", 169), ("SAP consultant", 219)],
         proof=[("why-global-companies-choose-sri-lanka", "IFS runs 75% of its global R&D and 80% of product support from Colombo."), ("creative-software", "IFS ERP consulting alongside product engineering."),
                ("inivos", "Founded by engineers who came up through IFS."), ("igt1-lanka", "Set up by the owners of IFS to supply software talent."), ("infomate", "Finance teams working daily on SAP, Oracle, NetSuite and Dynamics.")],
         note="IFS has operated in Sri Lanka for 27 years, which makes Colombo one of the deepest IFS talent pools anywhere. No public salary data exists for IFS consultants specifically."),
    dict(slug="cybersecurity-engineers", role="cybersecurity engineers", short="Cybersecurity engineers",
         pay=[("Cyber security engineer", 205)],
         proof=[("superloop", "Cybersecurity for a national telecom network."), ("surge-global", "Cybersecurity and engineering teams deployed as far as Papua New Guinea."),
                ("dijital-team", "Cybersecurity experts within dedicated client teams."), ("healthrecon-connect", "Operations run under HITRUST and SOC 1 controls.")],
         note="Reported pay for security roles varies more than for any other role, from about LKR 108,000 to LKR 1.3 million a month."),
    dict(slug="designers-product-managers", role="designers and product managers", short="Designers and product managers",
         pay=[("UX designer", 156), ("Senior UX designer", 244), ("Business analyst", 108), ("Product manager", 233), ("Senior product manager", 325)],
         proof=[("rootcode", "Rootcode Studio is a dedicated design division."), ("xeynergy", "Product management as part of delivery for US clients."),
                ("surge-global", "Creative, branding and product teams for international clients."), ("sysco-labs", "UI and UX as a core engineering discipline.")],
         note="Product roles usually sit with the client at first and move to Colombo as the team matures."),
    dict(slug="accountants", role="accountants and finance professionals", short="Accountants and finance staff",
         pay=[("Assistant accountant", 81), ("Financial analyst", 79), ("Finance manager", 267)],
         proof=[("infomate", "600+ finance professionals serving 150+ clients in 10+ countries."), ("wns", "Finance and accounting services from Colombo since 2004."),
                ("ey-gds", "500+ staff supporting EY member firms worldwide."), ("healthrecon-connect", "Revenue cycle specialists for US healthcare.")],
         note="Sri Lanka has one of the largest pools of CIMA, ACCA and CA qualified accountants outside the UK."),
]


def build_roles(B, stories):
    paths = []
    for r in ROLES:
        prefix = "../../"
        main = r["pay"][1] if len(r["pay"]) > 1 and r["slug"] in ("software-engineers",) else r["pay"][0]
        senior = next((p for p in r["pay"] if p[0].lower().startswith("senior")), None)
        yearly = round(main[1] * 1000 * 12 * 1.15 / SP.FX / 100) * 100
        answer = (f"You can hire {r['role']} in Sri Lanka directly, through an employer of record, or as a dedicated team from a Sri Lankan company. "
                  f"A {main[0].lower()} in Colombo earns a median of about LKR {main[1]},000 a month (about USD {SP.usd(main[1])})"
                  + (f", and a {senior[0].lower()} about LKR {senior[1]},000" if senior and senior is not main else "")
                  + f", according to self reported Glassdoor data for 2026. With statutory employer contributions that is roughly USD {yearly:,} a year at the median. Strong people at export companies earn more.")
        rows = "".join(f"<tr><td>{e(l)}</td><td>{m},000</td><td>{SP.usd(m)}</td><td>{round(m * 1000 * 12 * 1.15 / SP.FX / 100) * 100:,}</td></tr>" for l, m in r["pay"])
        faqs = [
            (f"How much do {r['role']} earn in Sri Lanka?", f"Self reported Glassdoor data for Colombo in 2026 shows a median of about LKR {main[1]},000 a month (about USD {SP.usd(main[1])}) for a {main[0].lower()}. Export focused employers pay above the median."),
            (f"Which companies employ {r['role']} in Sri Lanka?", "Published examples include " + ", ".join(next(s for s in stories if s["slug"] == p[0]).get("company") or "IFS" for p in r["proof"][:4]) + "."),
            (f"Do I need a local company to hire {r['role']} in Sri Lanka?", "No. You can hire through an employer of record, contract individuals, or take a dedicated team from a Sri Lankan company. Your own entity makes sense once the team passes a few dozen people."),
        ]
        faq, faq_ld = SP.faq_block(stories, faqs)
        others = SP.chip_links([(x["short"], f"../{x['slug']}/") for x in ROLES if x is not r])
        body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Hire in Sri Lanka", "../")])}
  <h1>Hire {e(r['role'])} in Sri Lanka</h1>
  <p class="answer">{e(answer)}</p>
  <p class="reviewed">Last reviewed {SP.REVIEWED}. Dollar figures use LKR {SP.FX} per dollar.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <h2 class="h-sub">What they earn</h2>
  <p class="cap">Median monthly pay in Colombo. Source: Glassdoor, 2026, self reported. Employer cost adds 15% statutory contributions. Full method and caveats in the <a href="{prefix}guides/sri-lanka-tech-salaries/">salary guide</a>.</p>
  <div class="tbl"><table><thead><tr><th>Role</th><th>Median LKR a month</th><th>Median USD a month</th><th>Employer cost, USD a year</th></tr></thead><tbody>{rows}</tbody></table></div>
  <p class="body-l mt-s">{e(r['note'])}</p>
  <h2 class="h-sub mt">Where {e(r['role'])} in Sri Lanka work today</h2>
  {SP.proof_list(B, stories, r['proof'], prefix)}
  <h2 class="h-sub mt">How to hire them</h2>
  <ol class="steps compact">
    <li><h3>One to ten people</h3><p>Use an employer of record or contractors. <a href="{prefix}guides/how-to-hire-in-sri-lanka/">How it works</a></p></li>
    <li><h3>A dedicated team</h3><p>A Sri Lankan company hires and runs the team for you. <a href="{prefix}companies/">See companies</a></p></li>
    <li><h3>Your own centre</h3><p>Register a company and hire directly. <a href="{prefix}guides/set-up-a-company-in-sri-lanka/">Setup guide</a></p></li>
  </ol>
  <div class="reach"><h2>Get a shortlist</h2><p>Tell us the seniority and stack. We introduce {e(r['role'])} or partner teams who fit.</p>
  <div class="actions"><a class="btn" href="{prefix}talent/find/?role={r['slug']}">Find {e(r['short'].lower())}</a><a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ghost" href="{prefix}hire-from/">Guides by country</a></div></div>
  {faq}
  <h2 class="h-sub mt">Other roles</h2>
  {others}
</div></section>
"""
        path = f"hire/{r['slug']}/"
        head = faq_ld + SP.crumbs_ld(B, [("Hire in Sri Lanka", "hire/"), (r["short"], path)])
        B.write(path + "index.html", B.page(f"Hire {r['short'].lower().replace('erp and ifs', 'ERP and IFS').replace('qa ', 'QA ').replace('devops', 'DevOps').replace(' ai ', ' AI ')} in Sri Lanka: pay and how", f"What {r['role']} earn in Sri Lanka in 2026, which companies employ them, and three ways to hire them from abroad.", body, prefix, path, extra_head=head, active="talent"))
        paths.append(path)

    cards = "".join(f'<a class="door" href="{r["slug"]}/"><h3>{e(r["short"])}</h3><p>Median about LKR {r["pay"][0][1] if r["slug"] != "software-engineers" else 177},000 a month for a {e((r["pay"][0][0] if r["slug"] != "software-engineers" else "software engineer").lower())}.</p><span class="door-go">Pay, companies and how to hire</span></a>' for r in ROLES)
    v, m = SP.hub_blocks("../", stories)
    faqs = [
        ("How do I hire developers in Sri Lanka?", "Choose one of four routes: an employer of record for a handful of direct hires, contractors for short projects, a dedicated team run by a Sri Lankan company, or your own registered company for a long term centre."),
        ("How much does a developer cost in Sri Lanka?", f"A software engineer in Colombo earns a median of about LKR 177,000 a month (about USD {SP.usd(177)}) and a senior engineer about LKR 260,000, on self reported Glassdoor data for 2026. Employers add 15% in statutory contributions. Partner company rates are around USD 25 to 40 an hour according to the Export Development Board."),
        ("Is Sri Lanka good for software outsourcing?", "The evidence says yes. IFS runs 75% of its global R&D in Colombo, Sysco, Synopsys and Zebra run engineering centres there, and Sri Lankan built companies such as WSO2 and Virtusa have been acquired for USD 600 million and USD 2 billion."),
        ("What time zone do Sri Lankan developers work in?", "UTC+5:30. That gives 4.5 to 5.5 shared working hours with Central Europe, 3.5 to 4.5 with the UK, 6.5 to 7.5 with the Gulf and 3.5 to 4.5 with eastern Australia. Teams serving the US usually work a later shift."),
    ]
    faq, faq_ld = SP.faq_block(stories, faqs)
    body = f"""
<section class="page-head"><div class="wrap">
  <h1>Hire developers and tech talent in Sri Lanka</h1>
  <p class="answer">Sri Lanka has well over 100,000 technology professionals, and global companies including IFS, Sysco, Synopsys and Virtusa run core engineering there. You can hire one person through an employer of record, take a dedicated team from a Sri Lankan company, or open your own centre. Pick a role below for pay, the companies that employ those people today, and how to start.</p>
</div></section>
<section class="section top-0"><div class="wrap">
  <div class="doors wrap3">{cards}</div>
  <div class="reach mt"><h2>Not sure where to start?</h2><p>Tell us what you are building. We will suggest the roles and the route, and introduce people who fit.</p>
  <div class="actions"><a class="btn" href="../talent/find/">Find talent</a><a class="btn btn-ghost" href="../guides/how-to-hire-in-sri-lanka/">How hiring works</a><a class="btn btn-ghost" href="../guides/sri-lanka-tech-salaries/">Salary guide</a></div></div>
  <h2 class="h-sub mt">By your industry</h2>{v}
  <h2 class="h-sub mt">By your country</h2>{m}
  <div class="narrow-in">{faq}</div>
</div></section>
"""
    B.write("hire/index.html", B.page("Hire developers in Sri Lanka: roles, salaries and how to start", "Hire software engineers, QA, DevOps, data, ERP and finance talent in Sri Lanka. Pay by role, the companies already there, and three ways to start.", body, "../", "hire/",
                                      extra_head=faq_ld + SP.crumbs_ld(B, [("Hire in Sri Lanka", "hire/")]), active="talent"))
    return paths + ["hire/"]


def build_badge(B, stories):
    cos = sorted([s for s in stories if s.get("company")], key=lambda s: s["company"].lower())
    opts = "".join(f'<option value="{s["slug"]}">{e(s["company"])}</option>' for s in cos)
    for name, bg, fg, sub in (("featured-light", "#ffffff", "#0b3c91", "#b46f00"), ("featured-dark", "#07245c", "#ffffff", "#f7a600")):
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="440" height="120" viewBox="0 0 440 120" role="img" aria-label="Featured on Tech Destination Sri Lanka">
<rect x="1.5" y="1.5" width="437" height="117" rx="14" fill="{bg}" stroke="#0b3c91" stroke-width="3"/>
<g transform="translate(22 24)"><path d="M0 0h36L0 36z" fill="#e94e1b"/><path d="M36 0h36v36z" fill="#f7a600"/><path d="M0 36l36 36H0z" fill="#0f7d5c"/><path d="M36 36l36 36V36z" fill="#1eb2e6"/><path d="M36 0L72 36H36z" fill="#8d1b3d"/></g>
<text x="116" y="46" font-family="Manrope, Arial, Helvetica, sans-serif" font-size="17" font-weight="700" fill="{sub}">Featured on</text>
<text x="116" y="74" font-family="Manrope, Arial, Helvetica, sans-serif" font-size="23" font-weight="800" fill="{fg}">Tech Destination</text>
<text x="116" y="100" font-family="Manrope, Arial, Helvetica, sans-serif" font-size="23" font-weight="800" fill="{fg}">Sri Lanka</text>
</svg>
"""
        B.write(f"assets/badge/{name}.svg", svg)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  <h1>Featured badge</h1>
  <p class="lede">If we have featured your company, you can show this badge on your website. It links to your story, so visitors can read it and check the sources.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <div class="badge-row"><img src="../assets/badge/featured-light.svg" alt="Featured on Tech Destination Sri Lanka badge, light" width="220" height="60"><span class="badge-dark"><img src="../assets/badge/featured-dark.svg" alt="Featured on Tech Destination Sri Lanka badge, dark" width="220" height="60"></span></div>
  <div class="form badge-form">
    <h2>Get the code for your company</h2>
    <div class="fields">
      <label><span>Company</span><select id="badge-co">{opts}</select></label>
      <label><span>Style</span><select id="badge-style"><option value="featured-light">Light</option><option value="featured-dark">Dark</option></select></label>
      <label class="wide"><span>Paste this into your website</span><textarea id="badge-code" rows="4" readonly></textarea></label>
    </div>
    <button class="btn" type="button" id="badge-copy">Copy code</button>
  </div>
  <p class="aside">Not featured yet? <a href="../get-featured/">Tell us about your company</a>.</p>
</div></section>
<script>
(function () {{
  var co = document.getElementById('badge-co'), st = document.getElementById('badge-style'), out = document.getElementById('badge-code'), btn = document.getElementById('badge-copy');
  function upd() {{
    out.value = '<a href="{B.SITE_URL}/stories/' + co.value + '/"><img src="{B.SITE_URL}/assets/badge/' + st.value + '.svg" alt="Featured on Tech Destination Sri Lanka" width="220" height="60"></a>';
  }}
  co.addEventListener('change', upd); st.addEventListener('change', upd); upd();
  btn.addEventListener('click', function () {{ out.select(); if (navigator.clipboard) navigator.clipboard.writeText(out.value); btn.textContent = 'Code copied'; setTimeout(function () {{ btn.textContent = 'Copy code'; }}, 2000); }});
}})();
</script>
"""
    B.write("featured-badge/index.html", B.page("Featured on Tech Destination Sri Lanka badge", "Companies featured by Tech Destination Sri Lanka can add this badge to their website. It links to the company's story and sources.", body, "../", "featured-badge/"))
    return "featured-badge/"


def build_privacy(B):
    body = f"""
<section class="page-head"><div class="wrap narrow"><h1>Privacy</h1>
<p class="lede">What we collect on this site, why, and how to have it removed.</p>
<p class="reviewed">Last updated {SP.REVIEWED}.</p></div></section>
<section class="section top-0"><div class="wrap narrow prose tight">
  <h2>Forms</h2>
  <p>When you send a form on this site we receive what you typed: usually your name, email, company and message. Forms are delivered to us by Formspree, a form handling service. We use the information to reply to you and to make the introductions you asked for. We do not sell it.</p>
  <h2>Top Talent applications</h2>
  <p>If you apply to be featured as Sri Lankan Top Talent, we use your application to assess and, with your agreement, write and publish a profile. You see the profile before it is published. We do not publish your email or phone number. You can ask us to remove a published profile at any time.</p>
  <h2>Newsletter</h2>
  <p>If you subscribe, we use your email only to send you new stories. Every email will let you unsubscribe.</p>
  <h2>Analytics</h2>
  <p>We use Google Analytics to understand which pages are read. For visitors in the European Economic Area, the United Kingdom and Switzerland, analytics cookies stay off unless you accept them in the banner. You can change your choice by clearing this site's data in your browser.</p>
  <h2>Embedded LinkedIn posts</h2>
  <p>Some pages show posts from our LinkedIn page inside a LinkedIn frame. LinkedIn may set its own cookies when those load. Their use is covered by LinkedIn's privacy policy.</p>
  <h2>Your requests</h2>
  <p>To see, correct or delete information we hold about you, email <a href="mailto:{B.EMAIL}">{B.EMAIL}</a> or use the <a href="../contact/">contact page</a>.</p>
</div></section>
"""
    B.write("privacy/index.html", B.page("Privacy", "What Tech Destination Sri Lanka collects through its forms and analytics, why, and how to have it removed.", body, "../", "privacy/"))
    return "privacy/"


def build_all(B, stories):
    return build_roles(B, stories) + [build_badge(B, stories), build_privacy(B)]
