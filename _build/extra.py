"""Services, talent, why Sri Lanka and get featured pages, plus the shared form builder."""
import html

import seo_pages

e = html.escape


def form(B, kind, title, intro, fields, submit, done):
    """fields: (type, name, label, required, options_or_placeholder)"""
    rows = []
    for typ, name, label, req, opt in fields:
        r = " required" if req else ""
        star = "" if req else ' <span class="opt">optional</span>'
        if typ == "select":
            ops = "".join(f"<option>{e(o)}</option>" for o in opt)
            ctl = f'<select name="{name}"{r}>{ops}</select>'
        elif typ == "textarea":
            ctl = f'<textarea name="{name}" rows="4" placeholder="{e(opt or "")}"{r}></textarea>'
        elif typ == "checks":
            boxes = "".join(f'<label class="check"><input type="checkbox" name="{name}" value="{e(o)}"> {e(o)}</label>' for o in opt)
            rows.append(f'<fieldset class="wide"><legend>{e(label)}{star}</legend><div class="checks">{boxes}</div></fieldset>')
            continue
        elif typ == "consent":
            rows.append(f'<label class="check wide"><input type="checkbox" name="{name}" value="yes" required> {e(label)}</label>')
            continue
        else:
            ctl = f'<input type="{typ}" name="{name}" placeholder="{e(opt or "")}"{r}>'
        wide = " wide" if typ == "textarea" else ""
        rows.append(f'<label class="{wide.strip()}"><span>{e(label)}{star}</span>{ctl}</label>')
    return f"""
<form class="form" id="{kind}-form" data-form="{kind}" data-done="{e(done)}" action="{e(B.FORM_ENDPOINT)}" method="POST">
  <h2>{e(title)}</h2>
  {f'<p class="form-intro">{e(intro)}</p>' if intro else ''}
  <div class="fields">
    {''.join(rows)}
  </div>
  <input type="hidden" name="form" value="{kind}">
  <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" class="sr" aria-hidden="true">
  <button class="btn" type="submit">{e(submit)}</button>
  <p class="form-status" role="status"></p>
</form>"""


def story_link(B, stories, slug, prefix, label=None):
    """Plain mention, no link: capability pages do not promote featured companies."""
    return e(seo_pages.mention(stories, slug, label or ""))


# ------------------------------------------------------------------ services
def build_services(B, stories):
    def block(anchor, title, text, points, cta, href):
        return f"""<article class="svc" id="{anchor}">
  <h3>{title}</h3>
  <p>{text}</p>
  <ul class="ticks">{''.join(f'<li>{p}</li>' for p in points)}</ul>
  <a class="door-go" href="{href}">{cta}</a>
</article>"""

    global_co = [
        block("hire", "Hire", "Add Sri Lankan engineers, designers, data people or finance professionals to your own team.",
              ["A shortlist matched to your role and stack", "Direct hire, contractor or employer of record, whichever fits", "Introductions to people who have built for global companies"],
              "Find talent", "../talent/find/"),
        block("partner", "Find a delivery partner", "Have a product or project to build? We match you with a Sri Lankan company that has done that kind of work before.",
              ["Matched from companies we have reported on and checked", "Dedicated team, project or build and transfer models", "References you can call"],
              "Describe your project", "../contact/?need=partner"),
        block("setup", "Set up", "Open your own engineering centre in Sri Lanka, the way IFS, Sysco and Synopsys did.",
              ["Company registration and Board of Investment routes explained", "Port City Colombo and tech park options", "Introductions to legal, tax and payroll advisers on the ground"],
              "Plan your setup", "../contact/?need=setup"),
        block("recruit", "Recruit at scale", "Build a team of 20 or 200 on a deadline.",
              ["Recruitment partners who hire for global tech companies every week", "Campus pipelines from the leading universities", "Employer branding so the right people apply to you"],
              "Start recruiting", "../contact/?need=recruit"),
    ]
    local_co = [
        block("spotlight", "Partner spotlight", f"A dedicated feature on your company, written to our editorial standard and published to our LinkedIn audience of {B.FOLLOWERS} followers and on this site.",
              ["Researched, sourced and written by our editors", "A permanent story page and directory listing here", "Fact checked and sourced like every story"],
              "Ask about a spotlight", "../get-featured/"),
        block("employer", "Employer branding", "Show engineers why they should build their career with you.",
              ["Team and culture stories", "Hiring campaigns to a Sri Lankan tech audience", "Founder and leadership profiles"],
              "Talk to us", "../contact/?need=employer"),
        block("events", "Events and delegations", "Heading to GITEX, Web Summit or London Tech Week? Show up as part of one Sri Lankan delegation, with content before, during and after.",
              ["Shared delegation identity and materials", "Event coverage for the companies attending", "Introductions to foreign buyers who follow us"],
              "Join a delegation", "../contact/?need=events"),
    ]
    body = f"""
<section class="page-head">
  <div class="wrap">
    <h1>Services</h1>
    <p class="lede">The stories show what Sri Lankan talent can do. These services help you act on it, whether you are a company abroad, a company in Sri Lanka or a professional looking for global work.</p>
    <p class="jump">Go to: <a href="#global">For global companies</a> <a href="#local">For Sri Lankan companies</a> <a href="#people">For professionals</a></p>
  </div>
</section>

<section class="section top-0" id="global">
  <div class="wrap">
    <div class="section-head"><h2>For global companies</h2></div>
    <div class="svc-grid">{''.join(global_co)}</div>
  </div>
</section>

<section class="section top-0">
  <div class="wrap">
    <div class="section-head"><h2>Five ways to build your team</h2><a class="more" href="../solutions/">Compare them</a></div>
    {__import__("solutions").tiles("../")}
  </div>
</section>

<section class="section tint" id="local">
  <div class="wrap">
    <div class="section-head"><h2>For Sri Lankan companies</h2></div>
    <div class="svc-grid three">{''.join(local_co)}</div>
  </div>
</section>

<section class="section" id="people">
  <div class="wrap">
    <div class="section-head"><h2>For professionals</h2></div>
    <div class="svc-grid one">
      {block("top-talent", "Sri Lankan Top Talent", "Get your profile in front of founders and hiring managers abroad. Free for the people we select.",
             ["A published profile built around work you can show", "Shared with employers who ask us for talent", "Your contact details stay private"],
             "Apply to be featured", "../talent/top-talent/")}
    </div>
  </div>
</section>

<section class="section tint">
  <div class="wrap">
    <div class="section-head"><h2>How it works</h2></div>
    <ol class="steps">
      <li><h3>Tell us what you need</h3><p>Use the form for your situation or message us on LinkedIn. A few lines are enough to start.</p></li>
      <li><h3>We match you</h3><p>We introduce the people, companies or advisers who fit, drawn from the ecosystem we report on every week.</p></li>
      <li><h3>You decide</h3><p>You talk to them directly and choose. We stay available if you need another option.</p></li>
    </ol>
  </div>
</section>

<section class="cta">
  <div class="wrap cta-in">
    <h2>Not sure which one fits?</h2>
    <p>Tell us what you are trying to do in two lines and we will point you the right way.</p>
    <div class="actions"><a class="btn btn-saffron" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ondark" href="../contact/">Contact us</a></div>
  </div>
</section>
"""
    B.write("services/index.html", B.page("Services", "Hire Sri Lankan talent, find a delivery partner, set up in Sri Lanka, recruit at scale, or get your company and people featured.", body, "../", "services/", active="services"))


# ------------------------------------------------------------------ talent
ROLES = ["Software engineering", "QA and test automation", "Data and AI", "DevOps and cloud", "Product and design", "ERP and enterprise apps", "Cybersecurity", "Finance and accounting", "Marketing and operations"]


def build_talent(B, stories):
    sl = lambda slug, label=None, p="../": story_link(B, stories, slug, p, label)
    hub = f"""
<section class="page-head">
  <div class="wrap">
    <h1>Talent</h1>
    <p class="lede">Two ways in. Companies come here to find Sri Lankan talent. Professionals come here to be found.</p>
  </div>
</section>
<section class="section top-0">
  <div class="wrap">
    <div class="duo">
      <a class="duo-card duo-blue" href="find/">
        <p class="duo-for">For companies</p>
        <h2>Find talent from Sri Lanka</h2>
        <p>Tell us the role. We introduce engineers, specialists or whole teams who have already delivered for global companies.</p>
        <span class="btn btn-saffron">Find talent</span>
      </a>
      <a class="duo-card duo-saffron" href="top-talent/">
        <p class="duo-for">For professionals</p>
        <h2>Be featured as Sri Lankan Top Talent</h2>
        <p>Want to be hired by a global company? Apply for a featured profile and get seen by the founders and hiring managers who follow us.</p>
        <span class="btn">Apply to be featured</span>
      </a>
    </div>
  </div>
</section>
<section class="section top-0">
  <div class="wrap">
    <div class="section-head"><h2>Hire by role</h2><a class="more" href="../hire/">All roles and pay</a></div>
    {seo_pages.chip_links([(r["short"], "../hire/" + r["slug"] + "/") for r in __import__("seo_more").ROLES])}
  </div>
</section>
<section class="section tint">
  <div class="wrap">
    <div class="section-head"><h2>What Sri Lankan talent is trusted with</h2><a class="more" href="../stories/">Read the stories</a></div>
    <div class="proof">
      <div><strong>Core product R&D</strong><p>Chip design software at Synopsys, enterprise platforms at IFS and Sysco, and device software at Zebra Technologies.</p></div>
      <div><strong>National systems</strong><p>Engineering on Norway's leading health record platform and on Estonia's government AI.</p></div>
      <div><strong>Financial infrastructure</strong><p>The London Stock Exchange's trading platform, and a wealth platform bought by JPMorganChase.</p></div>
      <div><strong>Embedded teams</strong><p>Dedicated teams that have worked inside European and US companies for ten years and more.</p></div>
    </div>
  </div>
</section>
"""
    B.write("talent/index.html", B.page("Talent", "Find talent from Sri Lanka, or apply to be featured as Sri Lankan Top Talent and get seen by global employers.", hub, "../", "talent/", active="talent"))

    find_form = form(B, "find-talent", "Tell us who you need", "A few lines are enough. We reply by email with next steps.", [
        ("text", "name", "Your name", True, ""),
        ("email", "email", "Work email", True, ""),
        ("text", "company", "Company", True, ""),
        ("text", "country", "Country", False, ""),
        ("checks", "roles", "Roles you need", False, ROLES),
        ("select", "team_size", "How many people", True, ["1 to 2", "3 to 10", "11 to 50", "More than 50"]),
        ("select", "model", "How you want to work", True, ["Hire directly", "Contractors or employer of record", "A dedicated team from a partner company", "Not sure yet"]),
        ("select", "timeline", "When", True, ["As soon as possible", "Within 3 months", "Later this year", "Exploring"]),
        ("textarea", "message", "Anything else", False, "Stack, seniority, time zone overlap, budget range"),
    ], "Send request", "Request sent. We will reply by email.")
    find_faq, find_ld = seo_pages.faq_block(stories, [
        ("Do I need a company in Sri Lanka to hire there?", "No. You can hire through an employer of record, contract individuals, or take a dedicated team from a Sri Lankan company."),
        ("What roles can I hire in Sri Lanka?", "Software engineers, QA, DevOps and cloud, data and AI, designers and product managers, ERP consultants, cybersecurity engineers, and finance and accounting professionals."),
        ("What does a Sri Lankan software engineer cost?", "A median of about LKR 177,000 a month, roughly USD 535, on self reported 2026 Glassdoor data, plus 15% statutory employer contributions. Strong engineers at export companies earn more."),
    ])
    find = f"""
<section class="page-head">
  <div class="wrap narrow">
    <p class="crumb"><a href="../">Talent</a></p>
    <h1>Find talent from Sri Lanka</h1>
    <p class="lede">Engineers, specialists and finance professionals who already work for global companies. Tell us the role and we will introduce people or teams who fit.</p>
  </div>
</section>
<section class="section top-0">
  <div class="wrap narrow">
    <ul class="names roles">{''.join(f'<li><span>{e(r)}</span></li>' for r in ROLES)}</ul>
    <div class="proof two">
      <div><strong>People you hire directly</strong><p>Individuals from our Top Talent pool and network, hired by you as employees or contractors.</p></div>
      <div><strong>Teams from a partner company</strong><p>A dedicated team run by a Sri Lankan company we have reported on, working as an extension of yours.</p></div>
    </div>
    {find_form}
    {find_faq}
    <p class="aside">Prefer to talk it through? <a href="{B.BOOKING_URL}" rel="noopener">Schedule a 30 minute call</a> or email <a href="mailto:{B.EMAIL}">{B.EMAIL}</a>.</p>
    <p class="aside">Planning a team of 20 or more, or your own entity? See <a href="../../services/#setup">Set up</a> and <a href="../../services/#recruit">Recruit at scale</a>.</p>
  </div>
</section>
"""
    B.write("talent/find/index.html", B.page("Find talent from Sri Lanka", "Tell us the role you need. We introduce Sri Lankan engineers, specialists or dedicated teams who have delivered for global companies.", find, "../../", "talent/find/", active="talent", extra_head=find_ld))

    tt_form = form(B, "top-talent", "Apply to be featured", "It takes about five minutes. We review every application.", [
        ("text", "name", "Full name", True, ""),
        ("email", "email", "Email", True, ""),
        ("url", "linkedin", "LinkedIn profile", True, "https://www.linkedin.com/in/"),
        ("text", "role", "What you do", True, "Senior backend engineer"),
        ("select", "experience", "Years of experience", True, ["Under 2", "2 to 5", "6 to 10", "More than 10"]),
        ("text", "location", "Where you are based", True, "Colombo"),
        ("text", "skills", "Main skills", True, "Java, AWS, Kubernetes"),
        ("url", "portfolio", "Portfolio, GitHub or website", False, "https://"),
        ("textarea", "proof", "The work you are proudest of", True, "What you built, who used it, and any numbers you can share"),
        ("checks", "open_to", "Open to", False, ["Remote full time", "Contract or freelance", "Relocation", "Roles with companies in Sri Lanka"]),
        ("consent", "consent", "I agree that Tech Destination Sri Lanka may publish a profile based on this information and share it with employers. My email is never published.", True, None),
    ], "Send application", "Application sent. We will email you after we review it.")
    tt_faq, tt_ld = seo_pages.faq_block(stories, [
        ("Is it free to be featured as Sri Lankan Top Talent?", "Yes. There is no charge for professionals we select."),
        ("Who can apply?", "Engineers, designers, data, product, ERP, security and finance professionals from Sri Lanka, at any career stage, who can show their work."),
        ("Will my contact details be published?", "No. Your email and phone number are never published. Employers reach you through us."),
    ])
    tt = f"""
<section class="page-head">
  <div class="wrap narrow">
    <p class="crumb"><a href="../">Talent</a></p>
    <h1>Be featured as Sri Lankan Top Talent</h1>
    <p class="lede">You do global grade work. We put it in front of the founders, CTOs and hiring managers who read us to decide where to hire next.</p>
  </div>
</section>
<section class="section top-0">
  <div class="wrap narrow">
    <div class="proof two">
      <div><strong>What you get</strong><p>A published profile on this site built around your work, a feature to our {B.FOLLOWERS} LinkedIn followers, and introductions when an employer asks us for someone like you. It is free.</p></div>
      <div><strong>Who we feature</strong><p>Engineers, designers, data, product, ERP, security and finance professionals from Sri Lanka, at any career stage, with work they can show.</p></div>
    </div>
    <h2 class="h-sub">How we choose</h2>
    <ul class="ticks">
      <li>Proof over titles. Products shipped, clients served, open source, awards or results with numbers.</li>
      <li>We check what we publish, the same way we check company stories.</li>
      <li>Your email and phone are never published. Employers reach you through us.</li>
    </ul>
    <ol class="steps compact">
      <li><h3>Apply</h3><p>Send the form below with your LinkedIn and your best work.</p></li>
      <li><h3>Review</h3><p>We read every application and may ask a few questions.</p></li>
      <li><h3>Get featured</h3><p>We write your profile, you approve it, and we publish.</p></li>
    </ol>
    {tt_form}
    {tt_faq}
  </div>
</section>
"""
    B.write("talent/top-talent/index.html", B.page("Be featured as Sri Lankan Top Talent", "Apply for a featured profile and get seen by global founders and hiring managers looking for Sri Lankan talent.", tt, "../../", "talent/top-talent/", active="talent", extra_head=tt_ld))


# ------------------------------------------------------------------ why Sri Lanka
def build_why(B, stories):
    sl = lambda slug, label=None: story_link(B, stories, slug, "../", label)
    lk = lambda slug, label: f'<a href="../stories/{slug}/">{e(label)}</a>'
    rows = [
        ("The work is core product, and has been for decades",
         f"IFS does about 60% of its global product development in Colombo ({lk('why-global-companies-choose-sri-lanka', 'our analysis')}). Sysco's engineers here work on the same codebase as its teams in Texas. Synopsys engineers chip design software here, and Zebra Technologies builds product for its global platforms."),
        ("Sri Lankan founders build companies that get bought",
         "The London Stock Exchange bought the Colombo company that built its trading platform. EQT acquired WSO2 for $600 million. Virtusa listed on Nasdaq and sold for $2 billion. JPMorganChase acquired a Sri Lankan founded wealth platform in 2026."),
        ("European and Australian companies stay for the long run",
         "Colombo teams have worked with Scandinavian clients for 25 years. A Stockholm listed software group calls Colombo its global tech center. Dutch and Australian companies have built their engineering base here and kept growing it."),
        ("The talent pipeline is measured",
         f"12,000+ ICT graduates a year and third in Asia for affordable tech talent, according to {lk('startup-genome-2026', 'Startup Genome 2026')}. 120,000+ IT professionals and $1.645 billion in exports ({lk('it-bpm-exports-2025', 'export data')}). {lk('universities', 'Moratuwa and SLIIT')} feed it."),
        ("It is more than software engineers",
         "Sri Lanka's depth in certified accountants supports finance operations for clients in 10+ countries, and US healthcare revenue operations run from Colombo under HITRUST certification."),
        ("The working day overlaps with yours",
         f"GMT+5:30 gives four to six hours of real time overlap with Europe and three to four with the US East Coast, and a full day with the Middle East and much of Asia Pacific ({lk('why-global-companies-choose-sri-lanka', 'analysis')})."),
        ("The infrastructure is already built",
         "Purpose built technology campuses in Colombo house 85+ technology companies, and Port City Colombo's special economic zone has its first global tenants."),
        ("Startups are building products, beyond services",
         'Sri Lankan startups ship their own AI products, and one builds AI infrastructure for the Estonian government. The country has about 750 to 1,000 startups. <a href="../guides/sri-lanka-startup-ecosystem/">See the startup ecosystem</a>.'),
    ]
    body = f"""
<section class="page-head">
  <div class="wrap narrow">
    <h1>Why Sri Lanka</h1>
    <p class="lede">Eight reasons, each backed by a company you can look up. Every claim on this page links to a story with its sources.</p>
  </div>
</section>
<section class="section top-0">
  <div class="wrap narrow">
    <ol class="reasons">
      {''.join(f'<li><h2>{e(t)}</h2><p>{p}</p></li>' for t, p in rows)}
    </ol>
    <h2 class="h-sub">The case for your industry</h2>
    {seo_pages.hub_blocks("../", stories)[0]}
    <h2 class="h-sub mt">The case for your country</h2>
    {seo_pages.hub_blocks("../", stories)[1]}
    <div class="reach mt">
      <h2>Questions worth asking before you start</h2>
      <ul class="ticks">
        <li>Do you need a few people, a dedicated team from a partner, or your own entity?</li>
        <li>Which skills, and how senior? Niche skills take longer to hire anywhere.</li>
        <li>How many hours of overlap does your team need each day?</li>
      </ul>
      <div class="actions"><a class="btn" href="../talent/find/">Find talent</a><a class="btn btn-ghost" href="../guides/">Read the guides</a></div>
    </div>
  </div>
</section>
"""
    B.write("why-sri-lanka/index.html", B.page("Why Sri Lanka", "Eight evidence backed reasons global companies build technology teams in Sri Lanka, each linked to a sourced story.", body, "../", "why-sri-lanka/", active="why"))


# ------------------------------------------------------------------ get featured
def build_get_featured(B, stories):
    f = form(B, "get-featured", "Tell us about the company", "Suggesting someone else's company is welcome too.", [
        ("text", "name", "Your name", True, ""),
        ("email", "email", "Email", True, ""),
        ("text", "company", "Company", True, ""),
        ("url", "website", "Company website", False, "https://"),
        ("select", "interest", "I am interested in", True, ["An editorial feature", "A partner spotlight", "Employer branding", "Events and delegations", "Not sure yet"]),
        ("textarea", "story", "What was built, and who uses it outside Sri Lanka", True, "Product or service, clients or markets, team size"),
        ("textarea", "proof", "Where we can verify the numbers", False, "Links to press coverage, your website, awards or public filings"),
    ], "Send", "Thank you. We read every submission and will reply by email.")
    body = f"""
<section class="page-head">
  <div class="wrap narrow">
    <h1>Get featured</h1>
    <p class="lede">We have featured {sum(1 for s in stories if s.get('company'))} companies so far. If yours builds for global markets with Sri Lankan talent, we want to hear about it.</p>
  </div>
</section>
<section class="section top-0">
  <div class="wrap narrow">
    <div class="proof two">
      <div><strong>Editorial feature</strong><p>A sourced story on what your company built and who uses it abroad, published here and on LinkedIn.</p></div>
      <div><strong>Partner spotlight</strong><p>A dedicated feature with wider promotion to our audience. Ask us for the media kit.</p></div>
    </div>
    <h2 class="h-sub">What makes a story we can run</h2>
    <ul class="ticks">
      <li>Something built or delivered for customers outside Sri Lanka</li>
      <li>The people behind it, by name</li>
      <li>Numbers that a public source or your documents can back</li>
    </ul>
    {f}
  </div>
</section>
"""
    B.write("get-featured/index.html", B.page("Get featured", "Suggest a Sri Lankan built company for an editorial feature, or ask about partner spotlights, employer branding and delegations.", body, "../", "get-featured/"))


def build_all(B, stories):
    build_services(B, stories)
    build_talent(B, stories)
    build_why(B, stories)
    build_get_featured(B, stories)
    return ["services/", "talent/", "talent/find/", "talent/top-talent/", "why-sri-lanka/", "get-featured/"]
