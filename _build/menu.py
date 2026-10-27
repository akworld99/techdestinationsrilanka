"""Master menu: the site's main navigation as a mega menu. Each top item opens a panel that lists everything in that
section; on phones the panels become an accordion. Rendered into every page by build.page()."""
import html

e = html.escape
LATEST = None   # newest story, set by build.main() so the Stories panel can feature it


def _groups():
    import seo_data
    import seo_more
    import seo_offshoring
    import seo_offshoring_plus as OX
    import seo_compare
    import solutions
    import source_data as D
    import source_markets as MK

    sol_desc = {"software-outsourcing-sri-lanka": "A Sri Lankan partner builds it for you",
                "dedicated-development-team-sri-lanka": "Engineers who work only on your product",
                "staff-augmentation-sri-lanka": "Add people to your own team",
                "offshore-development-center-sri-lanka": "Your own centre in Colombo",
                "sri-lanka-for-startups": "First hires and first teams"}
    roles = [(f"hire/{r['slug']}/", r["short"], None) for r in seo_more.ROLES]
    caps = [(f"offshoring/{c['slug']}/", c["label"], None) for c in seo_offshoring.CAPS]
    ox_label = {"from-uk": "From the UK", "from-usa": "From the USA", "from-australia": "From Australia", "from-uae": "From the UAE and Gulf"}
    return [
        dict(key="hire", label="Hire and build", lede="Hire engineers in Sri Lanka or have a Sri Lankan team build for you.",
             cols=[
                 ("Ways to build", [(f"solutions/{x['slug']}/", x["label"], sol_desc.get(x["slug"])) for x in solutions.SOLUTIONS]
                  + [("solutions/", "Compare the ways to build", None)]),
                 ("Hire by role", roles + [("hire/", "All roles and salaries", None)]),
                 ("Get started", [("talent/find/", "Find talent", "Tell us the roles, we introduce people"),
                                  ("services/", "All services", "What we do for companies"),
                                  ("guides/how-to-hire-in-sri-lanka/", "How hiring works", "Four routes and the rules"),
                                  ("talent/top-talent/", "Be featured as Top Talent", "For Sri Lankan professionals")]),
             ],
             feature=("tools/team-cost-calculator/", "Team cost calculator", "Price a team by role and size, direct or through a partner.", "assets/art/g-calculator.svg")),
        dict(key="outsourcing", label="Outsourcing", lede="Business services delivered from Sri Lanka, beyond software.",
             cols=[
                 ("Business services", caps, 2),
                 ("By your market", [(f"offshoring/{m['slug']}/", ox_label.get(m["slug"], m["slug"]), None) for m in OX.MARKET_PAGES]
                  + [("offshoring/bpo-companies-sri-lanka/", "BPO companies in Sri Lanka", "Who delivers what, with sources"),
                     ("offshoring/", "Outsourcing overview", None)]),
             ],
             feature=("offshoring/", "Outsourcing to Sri Lanka", "Accounting, research, medical billing, support, legal, BIM and more.", "assets/art/g-offshoring.svg")),
        dict(key="source", label="Source", lede="Buy products direct from Sri Lankan exporters, or win tenders if you export.",
             cols=[
                 ("Products", [(f"source/{c['slug']}/", c["label"], None) for c in D.CATS], 3),
                 ("Buy from Sri Lanka", [("source/request-a-quote/", "Request a quote", "Matched exporters in two working days"),
                                         ("source/how-to-import-from-sri-lanka/", "How to import", "Duties, documents, shipping"),
                                         ("source/sri-lanka-export-statistics/", "Export statistics", "By product and country"),
                                         ("source/", "All products", None)]),
                 ("By market", [(f"source/{m['slug']}/", f"Import to {m['short']}", None) for m in MK.MARKETS]),
                 ("For exporters", [("source/tender-radar/", "Tender Radar", "Tender alerts on WhatsApp"),
                                    ("source/bid-support/", "Bid support", "Win international tenders"),
                                    ("source/for-exporters/", "Exporter services", None)]),
             ]),
        dict(key="why", label="Why Sri Lanka", lede="The evidence, by industry and by the country you hire from.",
             cols=[
                 ("By industry", [(f"why-sri-lanka/{v['slug']}/", v["label"], None) for v in seo_data.VERTICALS] + [("why-sri-lanka/", "Why Sri Lanka overview", None)]),
                 ("By your country", [(f"hire-from/{m['slug']}/", m["label"], None) for m in seo_data.MARKETS] + [("hire-from/", "All countries", None)]),
                 ("Compare", [(f"compare/{o['slug']}/", "Sri Lanka vs " + (o["name"] if o["name"].startswith("the ") else o["name"][0].upper() + o["name"][1:]), None) for o in seo_compare.OTHERS]
                  + [("compare/", "All comparisons", None)]),
             ],
             feature=("guides/sri-lanka-tech-industry-facts/", "Industry facts", "Exports, workforce, graduates, rankings and exits, each sourced.", "assets/art/g-facts.svg")),
        dict(key="guides", label="Guides", lede="Practical, sourced guides for building a team in Sri Lanka.",
             cols=[
                 ("Guides", [("guides/sri-lanka-tech-salaries/", "Salary and cost guide 2026", None),
                             ("guides/how-to-hire-in-sri-lanka/", "How to hire", None),
                             ("guides/employer-of-record-sri-lanka/", "Employer of record", None),
                             ("guides/pay-employees-and-contractors-in-sri-lanka/", "Pay employees and contractors", None),
                             ("guides/set-up-a-company-in-sri-lanka/", "Set up a company", None),
                             ("guides/sri-lanka-startup-ecosystem/", "Startup ecosystem", None),
                             ("guides/", "All guides", None)]),
                 ("Tools and data", [("tools/team-cost-calculator/", "Team cost calculator", None),
                                     ("answers/", "Answers", "Short, sourced answers"),
                                     ("source/sri-lanka-export-statistics/", "Export statistics", None),
                                     ("data/sri-lanka-tech-salaries-2026.csv", "Salary data (CSV)", None)]),
             ],
             feature=("playbook/", "The 2026 playbook", "Salaries, hiring routes, setup, tax and industry numbers in one PDF.", "assets/art/g-playbook.svg")),
        dict(key="stories", label="Stories", lede="What Sri Lankan talent has built, and the companies behind it.",
             cols=[
                 ("Read", [("stories/", "All stories", "Products built in Sri Lanka"),
                           ("companies/", "Companies", "Directory of featured companies"),
                           ("tech-50/", "Sri Lanka Tech 50", None)]),
                 ("Take part", [("get-featured/", "Get your company featured", None),
                                ("featured-badge/", "Featured badge", None),
                                ("tech-tour/", "Sri Lanka Tech Tour", "Three days in Colombo")]),
             ],
             feature="latest"),
    ]


GROUP_BY_PATH = [("source/", "source"), ("offshoring/", "outsourcing"), ("solutions/", "hire"), ("hire/", "hire"), ("talent/", "hire"), ("services/", "hire"),
                 ("why-sri-lanka/", "why"), ("hire-from/", "why"), ("compare/", "why"), ("guides/", "guides"), ("tools/", "guides"), ("answers/", "guides"),
                 ("playbook/", "guides"), ("stories/", "stories"), ("companies/", "stories"), ("tech-50/", "stories"), ("tech-tour/", "stories"),
                 ("get-featured/", "stories"), ("featured-badge/", "stories"), ("about/", "about"), ("editorial-standards/", "about"), ("contact/", "about")]

_CACHE = {}


def _link(prefix, path, href, label, desc):
    cur = ' aria-current="page"' if href == path else ""
    d = f"<span>{e(desc)}</span>" if desc else ""
    return f'<li><a href="{prefix}{href}"{cur}><strong>{e(label)}</strong>{d}</a></li>'


def _feature(prefix, feat):
    if feat == "latest":
        s = LATEST
        if not s:
            return ""
        return (f'<a class="mm-feat" href="{prefix}stories/{s["slug"]}/"><img src="{prefix}assets/covers/{s["slug"]}.jpg" alt="" loading="lazy" width="1200" height="630">'
                f'<span class="mm-feat-k">Latest story</span><strong>{e(s["title"])}</strong></a>')
    href, title, text, img = feat
    return (f'<a class="mm-feat" href="{prefix}{href}"><img src="{prefix}{img}" alt="" loading="lazy" width="1200" height="900">'
            f'<strong>{e(title)}</strong><span>{e(text)}</span></a>')


def render(prefix, path):
    if "groups" not in _CACHE:
        _CACHE["groups"] = _groups()
    current = next((g for p, g in GROUP_BY_PATH if path.startswith(p)), "")
    items = []
    for g in _CACHE["groups"]:
        cols = []
        for col in g["cols"]:
            head, links = col[0], col[1]
            n = col[2] if len(col) > 2 else 1
            cols.append(f'<div class="mm-col{" wide" if n > 1 else ""}" style="--span:{n}"><p class="mm-h">{e(head)}</p><ul class="mm-list" style="--n:{n}">'
                        + "".join(_link(prefix, path, h, l, d) for h, l, d in links) + "</ul></div>")
        feat = _feature(prefix, g["feature"]) if g.get("feature") else ""
        pid = f"mm-{g['key']}"
        cur = " is-current" if g["key"] == current else ""
        items.append(f'<li class="mm-item{cur}"><button class="mm-top" type="button" aria-expanded="false" aria-controls="{pid}">{e(g["label"])}<span class="mm-chev" aria-hidden="true"></span></button>'
                     f'<div class="mm-panel" id="{pid}"><div class="wrap mm-in"><p class="mm-lede">{e(g["lede"])}</p><div class="mm-grid">{"".join(cols)}{feat}</div></div></div></li>')
    about_cur = " is-current" if current == "about" else ""
    items.append(f'<li class="mm-item mm-plain{about_cur}"><a class="mm-top" href="{prefix}about/"{" aria-current=\"page\"" if path == "about/" else ""}>About</a></li>')
    return f'<ul class="mm">{"".join(items)}</ul>'
