"""Ways of working pages: outsourcing, dedicated teams, staff augmentation, offshore centres and startups."""
import html

import seo_pages as SP

e = html.escape

SOLUTIONS = [
    dict(
        slug="software-outsourcing-sri-lanka", label="Software outsourcing", img="why-global-companies-choose-sri-lanka",
        h1="Software outsourcing and offshore development in Sri Lanka",
        title="Software outsourcing to Sri Lanka: offshore development guide",
        desc="Is Sri Lanka a good offshore software development destination? The evidence, the costs, the companies, and an honest view of where it fits and where it does not.",
        short="Hand a product or project to a Sri Lankan engineering company.",
        answer="Sri Lanka is an established offshore software development destination with USD 1.645 billion in IT and business process exports in 2025 and well over 100,000 technology professionals. IFS runs 75% of its global R&D in Colombo, and Sysco, Synopsys and Zebra run engineering centres there. Companies outsource to Sri Lanka for product engineers who stay on a codebase for years, at a cost the Export Development Board puts at 40% to 65% below equivalent teams in the US or UK.",
        stats=[("$1.645B", "IT and BPM exports in 2025"), ("75%", "of IFS global R&D done in Colombo"), ("USD 25 to 40", "an hour, typical partner rates per the Export Development Board")],
        proof=[("creative-software", "25 years of dedicated product teams for Scandinavian software companies."), ("virtusa", "Digital engineering for Fortune 500 clients with 3,000+ engineers in Colombo."),
               ("tiqri", "250+ completed projects for clients from startups to Fortune 500 companies."), ("xeynergy", "Full lifecycle delivery for US clients, plus its own AI products."),
               ("rootcode", "Product engineering and AI for European governments."), ("surge-global", "Software, data and security work for clients including the government of Qatar."),
               ("frontwalker", "100+ engineers and 250+ projects for a Stockholm listed group."), ("inivos", "Enterprise and automotive software with teams in four countries.")],
        sections=[
            ("Where Sri Lanka fits best", "Long running product engineering, regulated domains such as health and finance, enterprise software and ERP, and teams that need to feel like part of your company. The companies in our stories keep clients for ten, fifteen and twenty five years."),
            ("Where it fits less well", "Very large ramp ups of thousands of people in a few months, since the talent pool is deep but not endless. Work that needs full day overlap with US time zones without a shifted schedule. And work bought purely on the lowest price: the strongest Sri Lankan firms compete on retention and quality."),
            ("How engagements are usually structured", "Fixed scope projects for well defined builds. Dedicated teams for ongoing product work, billed monthly per person. Staff augmentation when you want individuals inside your own team. An offshore development centre when you want your own entity. Each has its own page linked below."),
            ("What it costs", "The Export Development Board cites developer rates of about USD 25 to 40 an hour through Sri Lankan companies. If you employ people directly, a senior software engineer costs roughly USD 10,800 to 18,600 a year including statutory contributions, depending on whether you pay at the local median or at export company levels. The salary guide has the detail and the sources."),
        ],
        faqs=[
            ("Is Sri Lanka a good country for software outsourcing?", "Yes, for the right kind of work. It exported USD 1.645 billion of IT and business process services in 2025, hosts most of IFS's global R&D, and has produced companies such as WSO2 and Virtusa that were acquired for USD 600 million and USD 2 billion. It suits long term product engineering better than very large, very fast ramp ups."),
            ("How much does it cost to outsource software development to Sri Lanka?", "Partner company rates are typically about USD 25 to 40 an hour according to the Export Development Board, which also says operations cost 40% to 65% less than equivalent teams in the US or UK."),
            ("Which are the leading software outsourcing companies in Sri Lanka?", "Companies we have reported on include Virtusa, Creative Software, Tiqri, Gapstars, Xeynergy, Rootcode, Surge Global, Frontwalker and Inivos. Each has a sourced story on this site."),
            ("What are the risks of outsourcing to Sri Lanka?", "The main ones are a finite talent pool for very large teams, limited natural overlap with US working hours, and strict termination rules if you employ people directly. Choosing an established partner and starting with a small team reduces all three."),
        ],
    ),
    dict(
        slug="dedicated-development-team-sri-lanka", label="Dedicated teams", img="creative-software",
        h1="Dedicated development teams in Sri Lanka",
        title="Dedicated development team in Sri Lanka: how it works",
        desc="A Sri Lankan company hires and runs a team that works only for you. Who does it well, how long clients stay, what it costs and how to start.",
        short="A Sri Lankan company hires and runs a team that works only for you.",
        answer="A dedicated development team is a group of engineers employed and managed by a Sri Lankan company who work only on your product, as an extension of your own team. It is the most common way foreign companies start in Sri Lanka. [[creative-software]] has run such teams for Scandinavian clients for 25 years, [[tiqri]] has client relationships of more than a decade, and [[gapstars]] embeds its engineers directly into 75+ European companies.",
        stats=[("25 years", "Creative Software has run dedicated teams"), ("10+ years", "typical length of Tiqri's longest client relationships"), ("75+", "companies supported by Gapstars")],
        proof=[("creative-software", "A Colombo team that DIPS of Norway credits as a significant contributor to its health record platform."), ("tiqri", "A dedicated, long term team for each client instead of a rotating pool."),
               ("gapstars", "Teams that embed in the client's company and regularly travel to its headquarters."), ("dijital-team", "Dedicated IT teams for clients in Australia, the US, Europe and the UK."),
               ("frontwalker", "Agile team deployment from its global tech center in Colombo."), ("xeynergy", "Fewer clients and deeper partnerships by design.")],
        sections=[
            ("How it works", "You define the roles. The partner recruits, employs and houses the team, handles HR and retention, and bills you monthly per person. You manage the work day to day as you would your own staff. Some clients later take the team into their own entity."),
            ("Why companies choose it", "You get a working team in weeks without registering a company or learning local employment law. The partner carries the hiring risk. And because the engineers work only for you, knowledge stays with your product."),
            ("What to ask a partner", "How long do your client teams last? What is your annual attrition? Can I interview every engineer? Who owns the code and the laptops? What happens if I want to take the team in house? Good partners answer these without hesitation."),
        ],
        faqs=[
            ("What is a dedicated development team?", "A team of engineers employed by a partner company who work only on your product and are managed day to day by you, while the partner handles hiring, HR, office space and retention."),
            ("How long does it take to set up a dedicated team in Sri Lanka?", "It depends on the roles and the partner. Ask partners for their typical time to hire for your stack, and expect senior and niche roles to take longer."),
            ("Which companies offer dedicated development teams in Sri Lanka?", "Creative Software, Tiqri, Gapstars, Dijital Team, Frontwalker and Xeynergy all run dedicated teams for international clients."),
            ("Can I convert a dedicated team into my own company later?", "Often yes, and it is worth agreeing the terms at the start."),
        ],
    ),
    dict(
        slug="staff-augmentation-sri-lanka", label="Staff augmentation", img="oceans",
        h1="IT staff augmentation in Sri Lanka",
        title="IT staff augmentation in Sri Lanka: hire remote engineers",
        desc="Add Sri Lankan engineers and specialists to your own team through an employer of record, contractors or a talent partner. Costs, routes and who does it.",
        short="Add individual engineers and specialists to your own team.",
        answer="Staff augmentation means adding individual Sri Lankan professionals to your existing team, managed by you, without setting up a local company. You can do it through an employer of record, by contracting people directly, or through a talent partner. [[oceans]] has placed Sri Lankan professionals with 600+ US startups and agencies, and reports an 86% first match success rate.",
        stats=[("600+", "companies use Oceans talent"), ("86%", "first match success rate reported by Oceans"), ("15%", "statutory employer contributions on top of salary")],
        proof=[("oceans", "Executive assistants, marketing, finance and operations specialists placed with US startups such as Morning Brew and beehiiv."), ("gapstars", "Engineers embedded directly into European scaleups."),
               ("xeynergy", "Engineering, QA, DevOps and product people working inside US client teams."), ("superloop", "Pays its Colombo staff on an Australian dollar benchmark, with company stock.")],
        sections=[
            ("Three ways to do it", "An employer of record employs the person in Sri Lanka on your behalf: Deel, Remote, G-P and Multiplier all list the country. A contractor agreement suits short or part time work. A talent partner finds, vets and sometimes trains people for you."),
            ("What it costs", "On self reported 2026 Glassdoor data a software engineer in Colombo earns a median of about LKR 177,000 a month and a senior engineer about LKR 260,000, with export companies paying well above that. Add 15% for statutory contributions and the provider's fee."),
            ("Getting the best people", "The strongest engineers have options. Pay on an international benchmark, give them real ownership, and bring them to your headquarters when you can. That is what the companies with ten year retention do."),
        ],
        faqs=[
            ("Can I hire a Sri Lankan developer without a local company?", "Yes. An employer of record such as Deel, Remote, G-P or Multiplier can employ the person for you, or you can contract them directly."),
            ("How much does a remote developer in Sri Lanka cost?", "A median of about LKR 177,000 a month for a software engineer and LKR 260,000 for a senior engineer on self reported 2026 Glassdoor data, plus 15% statutory contributions. Export focused employers pay more."),
            ("Is staff augmentation or a dedicated team better?", "Staff augmentation suits one to ten people you manage directly. A dedicated team suits larger groups where you want a partner to handle hiring, HR and retention."),
        ],
    ),
    dict(
        slug="offshore-development-center-sri-lanka", label="Offshore centres", img="synopsys",
        h1="Offshore development centres and global capability centres in Sri Lanka",
        title="Offshore development center in Sri Lanka: ODC and GCC guide",
        desc="IFS, Sysco, Synopsys, Zebra and EY run their own centres in Sri Lanka. Who is there, the rules on ownership and tax, and how to set one up.",
        short="Open your own engineering or capability centre in Colombo.",
        answer="An offshore development centre or global capability centre is your own operation in Sri Lanka, staffed by your employees. IFS, Sysco, Synopsys, Zebra Technologies, Michelin and EY all run one. A foreign company can own 100% of a Sri Lankan technology company, register it in about two weeks, and pays 15% tax on exported services. In SLASSCOM's 2025 compensation survey, 52% of participating firms were global capability centres.",
        stats=[("2,200+", "IFS employees in Colombo"), ("100%", "foreign ownership allowed for IT companies"), ("52%", "of firms in SLASSCOM's 2025 pay survey were capability centres")],
        proof=[("why-global-companies-choose-sri-lanka", "IFS, HCLTech, EY, Sysco and HSBC all run scaled operations in Sri Lanka."), ("sysco-labs", "The engineering arm of the world's largest foodservice distributor."),
               ("synopsys", "Chip design software R&D since 2015."), ("zebra-technologies", "A wholly owned software R&D subsidiary."), ("ey-gds", "One of nine countries in EY's global delivery network."),
               ("michelin", "IT services for Asia and a shared service center."), ("superloop", "24x7 network operations for an Australian carrier."), ("igt1-lanka", "A new centre in Port City Colombo from the owners of IFS.")],
        sections=[
            ("When your own centre makes sense", "Usually once you are confident you will need 30 or more people for years. Below that, a dedicated team from a partner is faster and carries less risk. You can start with a partner and convert later."),
            ("The rules in brief", "Private companies need one director and one shareholder, and directors need not live in Sri Lanka. IT companies can be fully foreign owned and can repatriate profits. Exported services are taxed at 15% and are zero rated for VAT. The setup guide covers the Board of Investment, Port City Colombo, visas and employment law, with sources."),
            ("Where centres are located", "Orion City houses IFS, Virtusa, Synopsys and Michelin teams among 85+ companies. TRACE Expert City, the World Trade Center and Port City Colombo are the other main hubs."),
        ],
        faqs=[
            ("Which global companies have offshore development centres in Sri Lanka?", "IFS, Sysco (Sysco LABS), Synopsys, Zebra Technologies, Michelin, EY, HCLTech, HSBC and Superloop all run their own centres or delivery operations in Sri Lanka."),
            ("Can a foreign company fully own a centre in Sri Lanka?", "Yes. IT and software companies can be 100% foreign owned and can repatriate profits, according to the Board of Investment."),
            ("What tax does an offshore development centre pay in Sri Lanka?", "Income from services exported and paid for in foreign currency is taxed at 15% from 1 April 2025. The standard corporate rate is 30%."),
            ("How long does it take to set up?", "Company registration takes about 7 to 14 working days. Hiring, office space and banking take longer, which is why many companies start with a partner run team."),
        ],
    ),
    dict(
        slug="sri-lanka-for-startups", label="For startups", img="wealthos",
        h1="Sri Lanka for startups: build your engineering team",
        title="Sri Lanka for startups: hire engineers and extend your runway",
        desc="WealthOS built its platform with a Sri Lankan team and was acquired by JPMorganChase. How startups hire in Sri Lanka, what it costs and who can help.",
        short="Extend your runway with a senior team from day one.",
        answer="Startups use Sri Lanka to build a senior engineering team at a fraction of home market cost without lowering the bar. [[wealthos]] built its wealth platform with 50+ engineers in Sri Lanka and was acquired by JPMorganChase less than three years after its first client. [[oceans]] supplies Sri Lankan talent to 600+ US startups, and [[gapstars]] builds engineering teams for Dutch scaleups such as Otrium.",
        stats=[("< 3 years", "from first client to acquisition for WealthOS"), ("600+", "US startups and agencies use Oceans talent"), ("#3 in Asia", "for affordable tech talent, Startup Genome 2026")],
        proof=[("wealthos", "Founded by two Sri Lankans in 2019 and acquired by JPMorganChase in 2026."), ("oceans", "Clients save 50% to 80% compared with US hires, by its own figures."),
               ("gapstars", "Embedded teams for European scaleups."), ("xeynergy", "Bootstrapped from six engineers to 80+ people and its own AI products."),
               ("rootcode", "A Colombo startup that now builds for European governments."), ("startup-genome-2026", "Sri Lanka made the biggest jump in Startup Genome's 2026 emerging ecosystem rankings.")],
        sections=[
            ("What startups hire first", "Usually two to five engineers through an employer of record or a small partner team, alongside a founder or lead at home who owns the product. Operations, finance and support roles often follow."),
            ("What it does to your runway", "A senior software engineer costs roughly USD 10,800 to 18,600 a year in Sri Lanka including statutory contributions, depending on how far above the local median you pay. The salary guide shows the working."),
            ("Making it work", "Hire for seniority, overlap a few hours every day, and treat the team as founders treat early employees. Superloop, for one, gives every Colombo employee company stock."),
        ],
        faqs=[
            ("Can an early stage startup hire engineers in Sri Lanka?", "Yes. Most start with a few people through an employer of record or a small partner team, which needs no local company."),
            ("Which startups have built with Sri Lankan engineers?", "WealthOS, acquired by JPMorganChase in 2026, built its platform with a Sri Lankan team. Oceans places Sri Lankan talent with US startups such as Morning Brew and beehiiv, and Gapstars works with Dutch scaleups such as Otrium."),
            ("How much can a startup save by hiring in Sri Lanka?", "Oceans says its clients save 50% to 80% compared with US hires. The Export Development Board cites 40% to 65% for operations compared with the US or UK."),
        ],
    ),
]


def tiles(prefix):
    return '<div class="tile-grid five">' + "".join(
        f'<a class="tile" href="{prefix}solutions/{s["slug"]}/"><img src="{prefix}assets/art/{s["slug"]}.svg" alt="" loading="lazy" width="1200" height="900"><span class="tile-body"><strong>{e(s["label"])}</strong><span>{e(s["short"])}</span></span></a>'
        for s in SOLUTIONS) + "</div>"


def build_all(B, stories):
    paths = []
    for s in SOLUTIONS:
        prefix = "../../"
        faq, faq_ld = SP.faq_block(stories, s["faqs"])
        others = SP.chip_links([(x["label"], f"../{x['slug']}/") for x in SOLUTIONS if x is not s])
        ind, ctry = SP.hub_blocks(prefix, stories)
        body = f"""
<section class="page-head has-img"><div class="wrap narrow">
  {SP.crumb_html([("Ways to build", "../")])}
  <h1>{e(s['h1'])}</h1>
  <p class="answer">{SP.linked(B, stories, s['answer'], prefix)}</p>
  <p class="reviewed">Last reviewed {SP.REVIEWED}.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <img class="story-cover art" src="{prefix}assets/art/{s['slug']}.svg" alt="" width="1200" height="900">
  {SP.stats_strip(s['stats'])}
  <div class="prose tight">{''.join(f'<h2>{e(h)}</h2><p>{SP.linked(B, stories, t, prefix)}</p>' for h, t in s['sections'])}</div>
  <h2 class="h-sub mt">Who does this in Sri Lanka</h2>
  {SP.proof_list(B, stories, s['proof'], prefix)}
  <div class="reach mt"><h2>Talk to us first</h2><p>Tell us what you are building and how big the team needs to be. We will suggest the route and introduce the right people or partners.</p>
  <div class="actions"><a class="btn" href="{prefix}talent/find/?route={s['slug']}">Find talent</a><a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ghost" href="{prefix}guides/sri-lanka-tech-salaries/">Salary and cost guide</a><a class="btn btn-ghost" href="{prefix}guides/set-up-a-company-in-sri-lanka/">Setup guide</a></div></div>
  {faq}
  <h2 class="h-sub mt">Other ways to build</h2>
  {others}
</div>
<div class="wrap"><h2 class="h-sub mt">By industry</h2>{ind}</div>
</section>
"""
        path = f"solutions/{s['slug']}/"
        head = faq_ld + SP.crumbs_ld(B, [("Ways to build", "solutions/"), (s["label"], path)])
        B.write(path + "index.html", B.page(s["title"], s["desc"], body, prefix, path, extra_head=head, active="services"))
        paths.append(path)
    body = f"""
<section class="page-head"><div class="wrap">
  <h1>Ways to build a tech team in Sri Lanka</h1>
  <p class="lede">Five routes, from handing over a project to opening your own centre. Each page has the evidence, the costs and the companies that do it.</p>
</div></section>
<section class="section top-0"><div class="wrap">{tiles("../")}
  <div class="reach mt"><h2>Not sure which fits?</h2><p>Tell us the team size and timeline and we will point you the right way.</p>
  <div class="actions"><a class="btn" href="../talent/find/">Find talent</a><a class="btn btn-ghost" href="../services/">Our services</a></div></div>
</div></section>
"""
    B.write("solutions/index.html", B.page("Ways to build a tech team in Sri Lanka", "Software outsourcing, dedicated teams, staff augmentation, offshore development centres and startup teams in Sri Lanka, each explained with evidence and costs.", body, "../", "solutions/", active="services"))
    return paths + ["solutions/"]
