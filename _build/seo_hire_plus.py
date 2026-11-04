"""Deep role pages: forward deployed engineers and IFS consultants in Sri Lanka, plus redirects for retired URLs."""
import html

import seo_pages as SP
from seo_pages import a

e = html.escape
REVIEWED = "4 November 2026"
FX = SP.FX

# Sources
FT_800 = "https://www.pymnts.com/?p=3546498"
EWEEK = "https://www.eweek.com/news/openai-anthropic-cohere-ai-hiring/"
PARAFORM = "https://www.paraform.com/insights/forward-deployed-ai-engineer"
IFS_25 = "https://www.ifs.com/en/insights/news/ifs-marks-25th-anniversary-of-the-inception-of-its-operations-in-sri-lanka"
IFS_1000 = "https://www.ft.lk/top-story/Software-giant-IFS-to-hire-1-000-more-in-Sri-Lanka/26-759485"
GD_SENIOR = "https://www.glassdoor.com/Salaries/colombo-sri-lanka-senior-software-engineer-salary-SRCH_IL.0,17_IM1025_KO18,42.htm"
GD_LEAD = "https://www.glassdoor.com/Salaries/colombo-associate-technical-lead-salary-SRCH_IL.0,7_IM1025_KO8,32.htm"
GD_ARCH = "https://www.glassdoor.com/Salaries/colombo-software-architect-salary-SRCH_IL.0,7_IM1025_KO8,26.htm"
GD_ERP = "https://www.glassdoor.com/Salaries/colombo-erp-consultant-salary-SRCH_IL.0,7_IM1025_KO8,22.htm"
GD_SAP = "https://www.glassdoor.com/Salaries/colombo-sap-consultant-salary-SRCH_IL.0,7_IM1025_KO8,22.htm"

# Retired URLs that still get search traffic -> where they should go now
REDIRECTS = {"startups/": "solutions/sri-lanka-for-startups/"}

# Extra doors for the /hire/ hub
HUB_DOORS = [
    ("forward-deployed-engineers", "Forward deployed engineers", "Customer facing engineers who ship AI and integrations inside client systems."),
    ("ifs-consultants", "IFS consultants", "Functional, technical and support consultants from the largest IFS talent pool outside Sweden."),
]


def usd_m(k):
    return f"{round(k * 1000 / FX / 5) * 5:,}"


def usd_y(k):
    return f"{round(k * 1000 * 12 * 1.15 / FX / 100) * 100:,}"


def pay_rows(rows):
    return "".join(f"<tr><td>{a(l, u)}</td><td>{k},000</td><td>{usd_m(k)}</td><td>{usd_y(k)}</td></tr>" for l, k, u in rows)


def article_ld(B, path, title, desc, about):
    return SP.ld({"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
                  "datePublished": "2026-11-04", "dateModified": "2026-11-04",
                  "author": {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"},
                  "publisher": {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"},
                  "mainEntityOfPage": f"{B.SITE_URL}/{path}", "inLanguage": "en", "about": about})


def howto_ld(name, steps):
    return SP.ld({"@context": "https://schema.org", "@type": "HowTo", "name": name,
                  "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate(steps)]})


def steps_html(steps):
    return '<ol class="steps compact">' + "".join(f"<li><h3>{e(n)}</h3><p>{e(t)}</p></li>" for n, t in steps) + "</ol>"


def reach(B, prefix, role_slug, heading, text, label):
    return (f'<div class="reach mt"><h2>{e(heading)}</h2><p>{e(text)}</p><div class="actions">'
            f'<a class="btn" href="{prefix}talent/find/?role={role_slug}">{e(label)}</a>'
            f'<a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a>'
            f'<a class="btn btn-ghost" href="{prefix}tools/team-cost-calculator/">Estimate team cost</a></div></div>')


# ------------------------------------------------------------------ forward deployed engineers
FDE_PATH = "hire/forward-deployed-engineers/"
FDE_FAQS = [
    ("What is a forward deployed engineer?",
     "A software engineer who works directly with a customer to get a product running inside that customer's systems: connecting data sources, building the integrations and workflows the customer needs, tuning AI models on their data and staying until it works in production. Palantir made the role known; AI companies such as OpenAI, Anthropic and Cohere now hire for it at scale."),
    ("Can forward deployed engineers work from Sri Lanka?",
     "Yes, for most of the job. Integration, data pipelines, evaluation and model tuning happen in code and can be done remotely. What needs presence is discovery, the first weeks with a new customer and building trust with their executives. Teams that work well put one engineer near the customer and run the rest of the deployment from Colombo, with travel for kickoffs."),
    ("How much does a forward deployed engineer cost in Sri Lanka?",
     f"There is no public salary data for the title in Sri Lanka. The closest benchmarks are associate technical leads (median about LKR 365,000 a month, about USD {usd_m(365)}) and software architects (about LKR 661,000, about USD {usd_m(661)}), on self reported Glassdoor data for Colombo in 2026. With 15% statutory contributions that is roughly USD {usd_y(365)} to {usd_y(661)} a year at the median. Strong people at export companies earn more."),
    ("What time zones do Sri Lankan engineers cover?",
     "Sri Lanka is UTC+5:30. The working day overlaps the UK and Europe in the afternoon, the Gulf for most of the day and Australia in the morning. For US customers, forward deployed engineers usually work a late shift to cover the US morning."),
    ("How is a forward deployed engineer different from a solutions engineer?",
     "A solutions engineer helps win the deal: demos, proofs of concept and technical answers during sales. A forward deployed engineer arrives after the deal and builds the production deployment, often writing code that goes back into the core product."),
    ("Where do forward deployed engineers in Sri Lanka come from?",
     "Mostly from enterprise software implementation and integration work. Sri Lanka has a large pool of engineers who have spent years deploying ERP, integration middleware and banking systems at customers abroad, which is the same mix of code, data and customer handling the role needs."),
]
FDE_STEPS = [
    ("Write down the deployment, not the job title", "List the systems you connect to, the data the engineer touches, the customers they face and the overlap hours you need."),
    ("Pick the model", "One or two people through an employer of record, a pod from a Sri Lankan engineering company, or your own centre once you pass a few dozen people."),
    ("Screen on a customer scenario", "Give candidates a messy real world brief: an unclear request, partial data and an API to integrate. Watch how they ask questions as closely as how they code."),
    ("Onboard next to your team", "Bring new engineers to your office or a customer site for the first two to four weeks. Plan visas early: Sri Lankan passport holders need visas for the US, UK and Schengen area."),
    ("Run deployments as a pod", "Pair a customer facing lead with Colombo engineers who own integrations, evaluation and fixes, with a fixed daily overlap window."),
]


def build_fde(B, stories):
    prefix = "../../"
    faq, faq_ld = SP.faq_block(stories, FDE_FAQS)
    answer = (f"You can hire forward deployed engineers in Sri Lanka directly through an employer of record or as a pod from a Sri Lankan engineering company. "
              f"The talent comes from years of enterprise software deployment: IFS alone does about 60% of its global product development and about 80% of its global product support in Colombo. "
              f"Experienced engineers at technical lead and architect level cost roughly USD {usd_y(365)} to {usd_y(661)} a year at the median, including statutory contributions.")
    pay = pay_rows([("Senior software engineer", 260, GD_SENIOR), ("Associate technical lead", 365, GD_LEAD), ("Software architect", 661, GD_ARCH)])
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Hire in Sri Lanka", "../")])}
  <h1>Hire forward deployed engineers in Sri Lanka</h1>
  <p class="answer">{e(answer)}</p>
  <p class="reviewed">Last reviewed {REVIEWED}. Dollar figures use LKR {FX} per dollar.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <nav class="toc" aria-label="On this page"><p><strong>On this page</strong></p><ol><li><a href="#role">The role</a></li><li><a href="#why">Why Sri Lanka</a></li><li><a href="#cost">Cost</a></li><li><a href="#model">What works remotely</a></li><li><a href="#skills">What to screen for</a></li><li><a href="#how">How to hire</a></li></ol></nav>

  <h2 class="h-sub" id="role">What a forward deployed engineer does</h2>
  <p class="body-l">A forward deployed engineer (FDE) takes a product into a customer's real environment and makes it work there. That means connecting the customer's data, building the integrations and workflows they need, tuning AI models on their data and handling problems in production. It is software engineering with a customer in the room.</p>
  <p class="body-l">The role has spread fast with AI. Monthly job listings for forward deployed engineers rose more than 800% between January and September 2025, according to Financial Times data reported by {a("PYMNTS", FT_800)}, with OpenAI, Anthropic and Cohere all expanding their teams ({a("eWeek", EWEEK)}). In the US, average total pay is about USD 238,000 a year according to Levels.fyi data cited by {a("Paraform", PARAFORM)}.</p>

  <h2 class="h-sub mt" id="why">Why companies look to Sri Lanka for this role</h2>
  <ul class="ticks">
    <li><strong>Deployment is already the core skill.</strong> IFS has run in Sri Lanka since 1997 and does about 60% of its global product development and about 80% of its global product support here ({a("IFS", IFS_25)}). Thousands of engineers have spent their careers getting enterprise software to work at customers abroad.</li>
    <li><strong>Integration depth.</strong> Middleware, API and identity platforms built in Colombo run inside banks, telcos and governments worldwide, so integration work is familiar ground.</li>
    <li><strong>Customer facing by habit.</strong> Engineers at export companies work in English with clients in the US, UK, Europe and Australia every day, often on the client's own systems.</li>
    <li><strong>Hours that cover three regions.</strong> UTC+5:30 overlaps the UK and Europe in the afternoon, the Gulf for most of the day and Australia in the morning.</li>
  </ul>
  <h3 class="mt-s">Where this kind of work happens in Colombo today</h3>
  {SP.proof_list(B, stories, [("why-global-companies-choose-sri-lanka", "IFS product development, support and consulting run from Colombo."), ("wso2", "Integration and identity products used by enterprises worldwide, built in Colombo."), ("sysco-labs", "Engineers on the same production systems as a Fortune 500 company's US teams."), ("virtusa", "Engineers delivering for Fortune 500 clients from Colombo for over two decades.")], prefix)}

  <h2 class="h-sub mt" id="cost">What it costs</h2>
  <p class="body-l">No public salary data exists for the forward deployed engineer title in Sri Lanka. These are the closest roles by seniority. Expect to pay above the median for people with customer facing and AI deployment experience.</p>
  <div class="tbl"><table><thead><tr><th>Benchmark role</th><th>Median LKR a month</th><th>Median USD a month</th><th>Employer cost, USD a year</th></tr></thead><tbody>{pay}</tbody></table></div>
  <p class="cap">Source: Glassdoor, Colombo, 2026, self reported. Employer cost adds 15% statutory contributions (EPF and ETF). More in the <a href="{prefix}guides/sri-lanka-tech-salaries/">salary guide</a>.</p>

  <h2 class="h-sub mt" id="model">What works remotely and what does not</h2>
  <div class="tbl"><table><thead><tr><th>Part of the job</th><th>From Colombo?</th></tr></thead><tbody>
    <tr><td>Data pipelines, integrations and API work</td><td>Yes</td></tr>
    <tr><td>Model tuning, evaluation sets, guardrails and monitoring</td><td>Yes</td></tr>
    <tr><td>Production support and fixes</td><td>Yes, and it covers hours your home team does not</td></tr>
    <tr><td>Discovery workshops and the first weeks with a new customer</td><td>Better in person. Plan travel or pair with a local lead</td></tr>
    <tr><td>Executive relationships at the customer</td><td>Usually owned by an onshore lead</td></tr>
  </tbody></table></div>
  <p class="body-l">The pattern that works: one customer facing lead near the customer, and a Colombo pod that owns integration, evaluation and production fixes. For customers in the UK, Europe, the Gulf and Australia, Sri Lankan engineers can often lead the whole deployment on shared hours.</p>

  <h2 class="h-sub mt" id="skills">What to screen for</h2>
  <ul class="ticks">
    <li><strong>Production code</strong> in Python or TypeScript, plus SQL.</li>
    <li><strong>Integration experience:</strong> REST and event APIs, identity, and at least one enterprise system such as an ERP, CRM or core banking platform.</li>
    <li><strong>AI deployment:</strong> retrieval pipelines, evaluation sets, prompt and agent design, and cost and latency control.</li>
    <li><strong>Cloud:</strong> AWS, Azure or GCP in a customer's account, not only your own.</li>
    <li><strong>Customer handling:</strong> turning a vague request into a scoped plan and explaining trade-offs to people who are not engineers.</li>
  </ul>

  <h2 class="h-sub mt" id="how">How to hire forward deployed engineers in Sri Lanka</h2>
  {steps_html(FDE_STEPS)}
  {reach(B, prefix, "forward-deployed-engineers", "Get a shortlist", "Tell us the product, the customers and the stack. We introduce engineers or partner teams who have done deployment work of that kind.", "Find forward deployed engineers")}
  {faq}
  <h2 class="h-sub mt">Related</h2>
  {SP.chip_links([("Data and AI engineers", "../data-ai-engineers/"), ("IFS consultants", "../ifs-consultants/"), ("Software engineers", "../software-engineers/"), ("Staff augmentation", "../../solutions/staff-augmentation-sri-lanka/"), ("Employer of record", "../../guides/employer-of-record-sri-lanka/"), ("Hire from the USA", "../../hire-from/usa/")])}
</div></section>
"""
    title = "Hire forward deployed engineers in Sri Lanka"
    desc = "Hire forward deployed engineers in Sri Lanka: what the role needs, why the talent is here, cost by seniority, what works remotely and how to hire. 2026 guide."
    head = (faq_ld + article_ld(B, FDE_PATH, title, desc, ["Forward deployed engineer", "Hiring in Sri Lanka", "AI deployment"])
            + howto_ld("How to hire forward deployed engineers in Sri Lanka", FDE_STEPS)
            + SP.crumbs_ld(B, [("Hire in Sri Lanka", "hire/"), ("Forward deployed engineers", FDE_PATH)]))
    B.write(FDE_PATH + "index.html", B.page(title, desc, body, prefix, FDE_PATH, extra_head=head, active="talent",
                                            seo_title="Hire forward deployed engineers in Sri Lanka (2026)"))
    return FDE_PATH


# ------------------------------------------------------------------ IFS consultants
IFS_PATH = "hire/ifs-consultants/"
IFS_FAQS = [
    ("Why hire IFS consultants from Sri Lanka?",
     "Because that is where much of IFS itself is built and supported. IFS has operated in Sri Lanka since 1997, has its largest R&D centre outside Sweden in Colombo, and does about 60% of its global product development and about 80% of its global product support there. That has produced the deepest pool of IFS trained people anywhere outside Sweden."),
    ("How many people does IFS employ in Sri Lanka?",
     "Over 2,500 in early 2024, with plans to reach about 3,500, according to IFS chief executive Mark Moffat speaking to the Daily FT. In 2023 IFS said its Sri Lankan team was about 40% of its global workforce."),
    ("How much does an IFS consultant cost in Sri Lanka?",
     f"There is no public salary data for IFS consultants specifically. ERP consultants in Colombo earn a median of about LKR 169,000 a month (about USD {usd_m(169)}) and SAP consultants about LKR 219,000 (about USD {usd_m(219)}), on self reported Glassdoor data for 2026. Senior and lead IFS consultants with IFS Cloud experience earn well above these medians."),
    ("Can Sri Lankan IFS consultants support customers in Europe and the US?",
     "Yes. IFS's own global support runs largely from Colombo. The working day overlaps Europe in the afternoon and the Nordics and UK for several hours. US coverage is usually handled with a later shift or a support rota."),
    ("What IFS work can be done from Sri Lanka?",
     "Most of it: configuration, development, integrations, reports, data migration, testing, upgrades to IFS Cloud and application managed support. Workshops with your process owners and go-live weeks are often done on site or with a local lead."),
    ("Should I hire IFS consultants directly or through a partner?",
     "For one or two long term people, hire directly through an employer of record. For a project or an upgrade, a Sri Lankan IFS delivery team brings ready made functional and technical cover. For ongoing support, an application managed services contract is usually cheaper than building your own bench."),
]
IFS_STEPS = [
    ("Map the modules and versions", "List your IFS version (IFS Applications 8, 9, 10 or IFS Cloud), the modules in use, your integrations and the customisations you carry."),
    ("Decide what you need", "Functional consultants for process and configuration, technical consultants for development and integrations, or a support team for day to day tickets."),
    ("Choose the model", "Direct hires through an employer of record, staff augmentation from an IFS delivery company, a fixed scope project team, or an application managed services contract."),
    ("Test on your own scenarios", "Ask candidates to walk through a real process from your business, such as a month end close or a work order, in the IFS module concerned."),
    ("Set the overlap and handover", "Agree shared hours with your team, a ticket process and documentation standards before the first sprint or support month starts."),
]
IFS_ROLES = [
    ("Functional consultants", "Finance, supply chain and procurement, manufacturing, projects, HR and payroll, maintenance (EAM) and field service (FSM and PSO scheduling)."),
    ("Technical consultants and developers", "IFS Cloud development, extensions, workflows, Aurena and Lobby pages, reports and custom objects."),
    ("Integration specialists", "IFS Connect, REST APIs and links to CRM, e-commerce, banking, logistics and shop floor systems."),
    ("Data migration and upgrade teams", "Moving from IFS Applications 8, 9 or 10 to IFS Cloud, data cleansing, testing and cutover."),
    ("Application managed services", "Level 1 to 3 support, monitoring, monthly updates and small changes under a service agreement."),
    ("Solution architects and project managers", "Design, governance and delivery leadership for implementations and upgrades."),
]


def build_ifs(B, stories):
    prefix = "../../"
    faq, faq_ld = SP.faq_block(stories, IFS_FAQS)
    answer = ("You can hire IFS consultants in Sri Lanka directly, through an IFS delivery company, or under a managed support contract. "
              "Colombo has the deepest IFS talent pool outside Sweden: IFS has operated there since 1997 and does about 60% of its global product development and about 80% of its global product support from Sri Lanka. "
              f"ERP consultants in Colombo earn a median of about USD {usd_m(169)} a month; experienced IFS Cloud consultants earn well above that.")
    pay = pay_rows([("ERP consultant", 169, GD_ERP), ("SAP consultant", 219, GD_SAP), ("Associate technical lead", 365, GD_LEAD)])
    roles = "".join(f"<tr><td><strong>{e(r)}</strong></td><td>{e(d)}</td></tr>" for r, d in IFS_ROLES)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Hire in Sri Lanka", "../")])}
  <h1>Hire IFS consultants in Sri Lanka</h1>
  <p class="answer">{e(answer)}</p>
  <p class="reviewed">Last reviewed {REVIEWED}. Dollar figures use LKR {FX} per dollar.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  {SP.stats_strip([("1997", "IFS in Sri Lanka since"), ("2,500+", "IFS staff in Sri Lanka, 2024"), ("~60%", "of IFS global product development"), ("~80%", "of IFS global product support")])}
  <p class="cap">Sources: {a("IFS, 2023", IFS_25)} and {a("Daily FT, 2024", IFS_1000)}.</p>
  <nav class="toc" aria-label="On this page"><p><strong>On this page</strong></p><ol><li><a href="#why">Why Sri Lanka</a></li><li><a href="#roles">Roles</a></li><li><a href="#cost">Cost</a></li><li><a href="#models">Ways to engage</a></li><li><a href="#how">How to hire</a></li></ol></nav>

  <h2 class="h-sub mt" id="why">Why Sri Lanka for IFS talent</h2>
  <ul class="ticks">
    <li><strong>IFS is built here.</strong> Colombo hosts IFS's largest R&D centre outside Sweden. In 2023 the Sri Lankan team was about 40% of IFS's global workforce, and it nearly tripled between 2017 and 2022 ({a("IFS", IFS_25)}).</li>
    <li><strong>Support and consulting too, not only code.</strong> IFS runs about 80% of its global product support from Sri Lanka, along with cloud operations and a consulting business unit ({a("IFS", IFS_25)}). Chief executive Mark Moffat has called Sri Lanka the company's "engine" ({a("Daily FT", IFS_1000)}).</li>
    <li><strong>An ecosystem around it.</strong> People trained at IFS now work at IFS partners and delivery companies in Colombo that implement and support IFS for customers in the Nordics, the UK, Europe, the US and Asia.</li>
    <li><strong>Hours that suit IFS markets.</strong> UTC+5:30 gives several shared hours with the Nordics, the UK and Central Europe every working day.</li>
  </ul>

  <h2 class="h-sub mt" id="roles">IFS roles you can hire in Sri Lanka</h2>
  <div class="tbl"><table><thead><tr><th>Role</th><th>What they cover</th></tr></thead><tbody>{roles}</tbody></table></div>

  <h2 class="h-sub mt" id="cost">What it costs</h2>
  <p class="body-l">No public salary data exists for IFS consultants specifically. These are the nearest benchmarks. Consultants with IFS Cloud, upgrade and customer facing experience earn well above the ERP median.</p>
  <div class="tbl"><table><thead><tr><th>Benchmark role</th><th>Median LKR a month</th><th>Median USD a month</th><th>Employer cost, USD a year</th></tr></thead><tbody>{pay}</tbody></table></div>
  <p class="cap">Source: Glassdoor, Colombo, 2026, self reported. Employer cost adds 15% statutory contributions. Partner day rates vary with seniority and contract length. More in the <a href="{prefix}guides/sri-lanka-tech-salaries/">salary guide</a>.</p>

  <h2 class="h-sub mt" id="models">Ways to engage IFS talent in Sri Lanka</h2>
  <div class="tbl"><table><thead><tr><th>Model</th><th>Best for</th><th>Watch out for</th></tr></thead><tbody>
    <tr><td>Direct hire through an employer of record</td><td>One to five long term people on your own team</td><td>You carry the management and the knowledge risk if someone leaves</td></tr>
    <tr><td>Staff augmentation from an IFS delivery company</td><td>Extra functional or technical capacity for a programme</td><td>Agree named people and a replacement policy in the contract</td></tr>
    <tr><td>Fixed scope project team</td><td>Implementations, IFS Cloud upgrades, rollouts to new sites</td><td>Scope creep; tie payments to milestones</td></tr>
    <tr><td>Application managed services</td><td>Day to day support, monthly updates and small changes</td><td>Define response times and what counts as a change</td></tr>
    <tr><td>Your own centre</td><td>Thirty or more IFS people over the long term</td><td>Setup time; see the <a href="{prefix}guides/set-up-a-company-in-sri-lanka/">setup guide</a></td></tr>
  </tbody></table></div>

  <h2 class="h-sub mt" id="how">How to hire IFS consultants in Sri Lanka</h2>
  {steps_html(IFS_STEPS)}
  {reach(B, prefix, "ifs-consultants", "Get IFS consultants or a delivery team", "Tell us your IFS version, modules and what you need. We introduce consultants or IFS delivery teams in Sri Lanka who fit.", "Find IFS consultants")}
  {faq}
  <h2 class="h-sub mt">Related</h2>
  {SP.chip_links([("ERP consultants", "../erp-consultants/"), ("Forward deployed engineers", "../forward-deployed-engineers/"), ("Enterprise software in Sri Lanka", "../../why-sri-lanka/enterprise-software/"), ("Staff augmentation", "../../solutions/staff-augmentation-sri-lanka/"), ("Hire from the Nordics", "../../hire-from/nordics/"), ("Hire from the UK", "../../hire-from/uk/")])}
</div></section>
"""
    title = "Hire IFS consultants in Sri Lanka"
    desc = "Hire IFS consultants in Sri Lanka, home to about 60% of IFS product development: functional, technical and support roles, costs and ways to engage. 2026."
    head = (faq_ld + article_ld(B, IFS_PATH, title, desc, ["IFS consultants", "IFS Cloud", "Hiring in Sri Lanka"])
            + howto_ld("How to hire IFS consultants in Sri Lanka", IFS_STEPS)
            + SP.crumbs_ld(B, [("Hire in Sri Lanka", "hire/"), ("IFS consultants", IFS_PATH)]))
    B.write(IFS_PATH + "index.html", B.page(title, desc, body, prefix, IFS_PATH, extra_head=head, active="talent",
                                            seo_title="Hire IFS consultants in Sri Lanka: roles, cost, how (2026)"))
    return IFS_PATH


def build_redirects(B):
    for old, new in REDIRECTS.items():
        url = f"{B.SITE_URL}/{new}"
        depth = "../" * old.count("/")
        B.write(old + "index.html", f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title>
<link rel="canonical" href="{url}"><meta name="robots" content="noindex,follow"><meta http-equiv="refresh" content="0; url={depth}{new}">
</head><body><p>This page has moved to <a href="{depth}{new}">{url}</a>.</p></body></html>""")


LLMS = [
    (FDE_PATH, "Hire forward deployed engineers in Sri Lanka", "What the role needs, why the talent is here, cost by seniority, what works remotely and how to hire"),
    (IFS_PATH, "Hire IFS consultants in Sri Lanka", "Functional, technical and support IFS roles, costs and ways to engage, from the largest IFS talent pool outside Sweden"),
]


def build(B, stories):
    build_redirects(B)
    return [build_fde(B, stories), build_ifs(B, stories)]
