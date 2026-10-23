"""SEO and answer-engine extras for the offshoring section: per-service depth (definitions, at-a-glance, steps,
provider checklist, extra FAQs, Service/Article/HowTo schema), buyer-market landing pages and a sourced BPO company directory."""
import html

import seo_pages as SP
from seo_pages import a

e = html.escape

# ---------------------------------------------------------------- per service extras
EXTRA = {
    "accounting-bookkeeping-outsourcing-sri-lanka": dict(
        term="accounting outsourcing",
        define="Accounting outsourcing means handing day to day finance work, such as bookkeeping, accounts payable and receivable, reconciliations and month-end close, to an external team that works in your systems under your controls. Offshore accounting does the same with a team in another country, usually to reach qualified people at lower cost and to keep work moving overnight.",
        glance=[("Best for", "Accounting firms, CFOs and growing companies with steady, documented finance processes"), ("Main client markets", "UK, Australia, US, Nordics, Middle East"),
                ("Typical setup", "A dedicated accountant or a small team through a provider, working in your Xero, QuickBooks, MYOB, Sage or NetSuite"), ("AI exposure", "High for data entry, low for close, review and commentary"),
                ("Qualifications to ask for", "CA Sri Lanka, CIMA, ACCA, or part qualified students")],
        checklist=["Which accounting software and which country's rules has the team worked in?", "Are staff qualified or studying for CA, CIMA or ACCA, and who reviews their work?", "How do they access your systems, and what security certifications do they hold?", "How are month-end deadlines, quality checks and errors handled?", "Can you meet and choose the people who will work on your account?", "What does the price include, and what is the notice period?"],
        faqs=[("Which are the accounting outsourcing companies in Sri Lanka?", "They range from global banks and exchanges running their own finance operations, such as HSBC and the London Stock Exchange Group, to specialist providers serving accounting firms and companies abroad. Our directory of business process companies in Sri Lanka lists examples with sources."),
              ("Can I hire an offshore accountant in Sri Lanka for my Australian or UK firm?", "Yes. Providers employ the accountant in Sri Lanka and you direct the work, or you can use an employer of record. Ask for experience with BAS, GST and Xero for Australia, or VAT, Making Tax Digital and Sage or Xero for the UK."),
              ("Is my financial data safe with a Sri Lankan accounting team?", "It depends on the provider's controls, not the country. Ask for ISO 27001 or SOC 2, role based access, no local data storage and a data processing agreement. Sri Lanka's Personal Data Protection Act applies to processors from 1 January 2027.")]),
    "investment-research-kpo-sri-lanka": dict(
        term="investment research outsourcing",
        define="Investment research outsourcing, a form of knowledge process outsourcing (KPO), means using an external analyst team for financial modelling, company and credit research, data work and deal support, while your own analysts keep the client relationship and the final call.",
        glance=[("Best for", "Asset managers, banks, private equity, hedge funds and consultancies"), ("Main client markets", "US, UK and Europe, Australia"), ("Typical setup", "Dedicated analysts through a research provider, or your own team via an employer of record"),
                ("AI exposure", "Medium: data extraction automated, analysis and judgement are not"), ("Qualifications to ask for", "CFA candidates, CA or CIMA, finance or economics degrees")],
        checklist=["Which asset classes and sectors does the team already cover?", "How are compliance, information barriers and confidentiality handled?", "What data terminals and tools do analysts use?", "How is research quality reviewed before it reaches you?", "Can you start with a pilot on one coverage area?"],
        faqs=[("What is KPO?", "Knowledge process outsourcing: outsourcing work that needs specialist knowledge and judgement, such as research, analytics and financial modelling, rather than transactional processing."),
              ("Is investment research outsourced to Colombo?", "Yes. Acuity Knowledge Partners, which began in Colombo as Amba Research in 2003, serves more than 50 global financial institutions from its Sri Lankan team.")]),
    "virtual-assistants-sri-lanka": dict(
        term="hiring a virtual assistant",
        define="A virtual assistant is a remote employee or contractor who handles administrative and operational work, such as calendars, email, research, CRM updates and coordination, for a business or an executive. An offshore virtual assistant does this from another country, usually full time and dedicated to one client.",
        glance=[("Best for", "Founders, executives, small businesses and operations teams"), ("Main client markets", "Australia, UAE, UK, US"), ("Typical setup", "A dedicated full time assistant through a remote staffing provider"),
                ("AI exposure", "Very high for routine tasks, so hire for ownership of outcomes"), ("Hours", "Same day with the UAE, the Australian afternoon, the UK morning with an early shift")],
        checklist=["Is the assistant employed by the provider, with leave, equipment and backup covered?", "Can you interview and choose the person?", "What tools and AI assistants are they already using?", "What happens when they are sick or leave?", "Are there minimum terms or setup fees?"],
        faqs=[("How much does a virtual assistant from Sri Lanka cost?", "It depends on experience and whether you hire through a provider or directly. Ask two or three remote staffing providers for a monthly all-in price for the profile you need, and see our salary guide for local pay levels."),
              ("Can I find a virtual assistant in Sri Lanka for my business in Dubai?", "Yes. Sri Lanka is 1.5 hours ahead of the UAE, so an assistant works almost the same day, and several Sri Lankan providers already serve UAE clients.")]),
    "digital-marketing-outsourcing-sri-lanka": dict(
        term="digital marketing outsourcing",
        define="Digital marketing outsourcing means using an external agency or a dedicated remote team to run channels such as SEO, paid search and social, email and marketing operations, with your team owning strategy and brand.",
        glance=[("Best for", "Agencies needing white label capacity, and companies building an in-house style remote marketing team"), ("Main client markets", "Australia, Southeast Asia, Middle East, UK"),
                ("Typical setup", "Agency retainer, or dedicated marketers through a staffing provider"), ("AI exposure", "High for content volume, lower for paid media, analytics and operations"), ("Tools to ask about", "Google Ads, Meta, GA4, HubSpot, Salesforce, Semrush or Ahrefs")],
        checklist=["Which clients in your country and channel can they show results for?", "Who owns your ad accounts, data and content?", "How is performance reported, and against what targets?", "How do they use AI, and how is AI output checked?", "Can you meet the people who will run your account?"],
        faqs=[("Which are the top digital marketing companies in Sri Lanka?", "There is no reliable independent ranking. Judge agencies on results for clients in your market and channel. We can introduce agencies and specialists that fit your brief."),
              ("Can a Sri Lankan agency work as a white label partner?", "Yes. White label SEO, paid media and content delivery for overseas agencies is a common arrangement.")]),
    "customer-support-outsourcing-sri-lanka": dict(
        term="customer support outsourcing",
        define="Customer support outsourcing means an external team handles customer contact, by email, chat or phone, and related operations such as order, account or claims servicing, using your tools, scripts and quality standards.",
        glance=[("Best for", "Banking, insurance, travel and complex servicing; email and chat; UK, Gulf and Australian hours"), ("Main client markets", "UK, Australia, UAE, US, Nordics"),
                ("Typical setup", "A managed team through a business process provider, or a dedicated team"), ("AI exposure", "High for simple tier one queries, low for escalations and regulated cases"), ("Hours", "UK and Gulf day shifts natural; US needs night shifts")],
        checklist=["Which industries and channels does the provider already support?", "How are quality, call recording and customer data handled?", "What is the plan for shift cover, attrition and peaks?", "How will the team work alongside your AI chatbot?", "What are the service levels and the penalties for missing them?"],
        faqs=[("Are there call centers in Sri Lanka?", "Yes. Contact centres serve airlines, hospitality, retail and financial services, and global firms such as HSBC have run customer operations in Colombo since 2004. The sector is smaller than the largest call centre destinations."),
              ("Is Sri Lanka good for email and chat support?", "Yes, particularly for complex or regulated queries and for customers in the UK, the Gulf and Australia, where working hours overlap.")]),
    "medical-billing-outsourcing-sri-lanka": dict(
        term="medical billing outsourcing",
        define="Medical billing outsourcing means an external team runs part or all of a healthcare provider's revenue cycle: eligibility checks, coding, claim submission, payment posting, denials and accounts receivable follow-up, working in the provider's practice management and billing systems.",
        glance=[("Best for", "US physician practices, specialty groups, hospitals and billing companies"), ("Main client markets", "US, with some UK and Australia"), ("Typical setup", "A dedicated billing team through an RCM provider, priced per FTE or as a share of collections"),
                ("AI exposure", "High for transcription and data entry, low for denials and complex AR"), ("Compliance to ask about", "HIPAA business associate agreement, SOC 2, certified coders (CPC, CCS)")],
        checklist=["Which specialties, payers and billing systems does the team know?", "Will they sign a HIPAA business associate agreement?", "Are coders certified, and how are coding audits done?", "What are their denial and collection rates for similar clients?", "How is protected health information accessed and logged?"],
        faqs=[("Which medical billing companies operate in Sri Lanka?", "Several revenue cycle firms work from Colombo and Kandy for US clients, including one that opened a 300 seat Kandy centre in 2024. Our directory of business process companies in Sri Lanka lists examples with sources."),
              ("Can Sri Lankan teams work in US billing systems?", "Yes. Teams routinely work in US practice management, EHR and clearinghouse systems through secure remote access.")]),
    "legal-process-outsourcing-sri-lanka": dict(
        term="legal process outsourcing",
        define="Legal process outsourcing (LPO) means using an external team of lawyers and paralegals for legal support work, such as research, document and contract review, drafting under instruction, conveyancing and matter administration, supervised by your own qualified lawyers.",
        glance=[("Best for", "UK and Australian law firms, in-house legal teams, conveyancers"), ("Main client markets", "UK, Australia, Singapore, US"), ("Typical setup", "Dedicated paralegals or lawyers through an LPO provider"),
                ("AI exposure", "High for first pass review, low for supervised drafting and review of AI output"), ("Qualifications to ask for", "Attorneys-at-law of Sri Lanka, LLB holders, UK or Australian qualifications where relevant")],
        checklist=["Which jurisdictions and practice areas does the team already support?", "How are conflicts, confidentiality and privilege protected?", "Who supervises the work, and how is it reviewed?", "Which legal tech and AI tools do they use?", "What professional indemnity cover does the provider hold?"],
        faqs=[("Is LPO allowed for UK law firms?", "Yes. Regulated activities stay with your firm and its qualified lawyers, who supervise and take responsibility for the outsourced work. Check your regulator's guidance on outsourcing and confidentiality.")]),
    "engineering-design-bim-outsourcing-sri-lanka": dict(
        term="BIM and CAD outsourcing",
        define="BIM and CAD outsourcing means using an external team to produce building information models, drawings, detailing, quantity take off and estimates for your projects, to your standards and templates.",
        glance=[("Best for", "Architects, engineers, contractors and quantity surveyors"), ("Main client markets", "UK, Australia, Gulf"), ("Typical setup", "A dedicated modeller or estimator through a design firm"),
                ("AI exposure", "Lower than most back office work"), ("Software to ask about", "Revit, AutoCAD, Navisworks, Tekla, CostX")],
        checklist=["Which standards have they worked to, such as UK BIM, RIBA stages or NRM?", "Which software versions and templates can they use?", "How are model quality and clash checks reviewed?", "Can they show work on similar building types?", "How is your project data stored and shared?"],
        faqs=[("Can Sri Lankan teams do quantity surveying for Gulf projects?", "Yes. Sri Lanka has a strong quantity surveying profession with long experience in Gulf construction, and take off, BOQs and estimating are commonly outsourced.")]),
    "data-annotation-sri-lanka": dict(
        term="data annotation outsourcing",
        define="Data annotation outsourcing means using an external team to label, tag, convert or evaluate data, such as images, text, audio or AI model output, so it can be used to train or test machine learning systems.",
        glance=[("Best for", "AI companies, data vendors and teams needing expert or local language data"), ("Main client markets", "US and global AI companies"), ("Typical setup", "A managed project with an established data processing firm"),
                ("AI exposure", "Simple labelling automated; evaluation and expert work growing"), ("Specialities", "LLM evaluation, finance and legal domain labelling, Sinhala and Tamil data")],
        checklist=["What annotation tools and quality processes does the team use?", "How is accuracy measured and reported?", "How is training data secured and deleted?", "Can they provide domain experts or native Sinhala and Tamil speakers?"],
        faqs=[("Can Sri Lankan teams provide Sinhala and Tamil training data?", "Yes. Sri Lanka is the natural source of Sinhala data and a strong source of Tamil data, both low resource languages for AI.")]),
    "insurance-hr-payroll-outsourcing-sri-lanka": dict(
        term="insurance and HR back office outsourcing",
        define="Insurance and HR back office outsourcing means using an external team for administrative and operational work such as policy and claims administration, underwriting support, payroll processing, HR administration and recruitment support.",
        glance=[("Best for", "Insurers, MGAs, brokers, payroll bureaus and HR teams"), ("Main client markets", "UK, Australia, US and Europe"), ("Typical setup", "A managed team or a dedicated team through a provider"),
                ("AI exposure", "High for data entry and calculation, low for complex claims and compliance"), ("Ask about", "Systems experience, data security and regulated activity boundaries")],
        checklist=["Which policy, claims or payroll systems does the team know?", "Which activities stay with your licensed staff?", "How are data security and audits handled?", "What are the service levels and escalation routes?"],
        faqs=[("Can Sri Lankan teams handle Lloyd's market work?", "UK specialist insurer CFC opened a 200 seat global services hub in Colombo in 2025, which shows the market is being used for UK specialty insurance operations. Ask any provider for direct experience with your lines.")]),
}

STEPS = [
    ("Pick one process", "Choose a single, well documented process with clear volumes and quality measures, such as accounts payable or tier two support."),
    ("Decide the model", "A managed provider runs it for you; a dedicated team works only for you through a staffing provider or employer of record; your own centre comes later."),
    ("Shortlist two or three providers", "Ask each the questions below, check references in your country and meet the people who would do the work."),
    ("Run a paid pilot", "Four to eight weeks with clear targets, with your team reviewing output daily at first."),
    ("Agree the contract", "Service levels, data protection, IP and confidentiality, pricing, notice and exit terms."),
    ("Scale what works", "Add people or processes once quality is proven, and keep a named lead on both sides."),
]


def glance_html(c):
    x = EXTRA[c["slug"]]
    return '<div class="tbl"><table><tbody>' + "".join(f"<tr><th scope=\"row\">{e(k)}</th><td>{e(v)}</td></tr>" for k, v in x["glance"]) + "</tbody></table></div>"


def depth_html(c, prefix):
    """Definition, steps and provider checklist inserted into each service page."""
    x = EXTRA[c["slug"]]
    steps = "".join(f'<li><h3>{e(n)}</h3><p>{e(t)}</p></li>' for n, t in STEPS)
    checks = "".join(f"<li>{e(q)}</li>" for q in x["checklist"])
    return f"""
  <h2 class="h-sub mt">What is {e(x['term'])}?</h2>
  <p class="body-l">{e(x['define'])}</p>
  <h2 class="h-sub mt">How to outsource {e(c['label'].lower())} to Sri Lanka, step by step</h2>
  <ol class="steps compact">{steps}</ol>
  <h2 class="h-sub mt">Questions to ask a Sri Lankan provider</h2>
  <ul class="ticks">{checks}</ul>
  <p class="body-l">See which organisations already do this work in our <a href="../bpo-companies-sri-lanka/">directory of business process companies in Sri Lanka</a>.</p>"""


def schema(B, c, path):
    x = EXTRA[c["slug"]]
    url = f"{B.SITE_URL}/{path}"
    org = {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"}
    svc = {"@context": "https://schema.org", "@type": "Service", "name": c["h1"], "serviceType": c["label"] + " outsourcing", "description": c["desc"], "url": url,
           "provider": org, "areaServed": [{"@type": "Country", "name": n} for n in ("United States", "United Kingdom", "Australia", "United Arab Emirates")],
           "availableChannel": {"@type": "ServiceChannel", "serviceUrl": f"{B.SITE_URL}/talent/find/"}}
    art = {"@context": "https://schema.org", "@type": "Article", "headline": c["h1"], "description": c["desc"], "datePublished": "2026-10-23", "dateModified": "2026-10-23",
           "author": org, "publisher": org, "mainEntityOfPage": url, "image": f"{B.SITE_URL}/assets/art/{c['_art']}.svg", "inLanguage": "en", "about": [c["label"], "Sri Lanka", "Outsourcing"]}
    how = {"@context": "https://schema.org", "@type": "HowTo", "name": f"How to outsource {c['label'].lower()} to Sri Lanka",
           "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate(STEPS)]}
    return SP.ld(svc) + SP.ld(art) + SP.ld(how)


# ---------------------------------------------------------------- buyer market pages
MARKET_PAGES = [
    dict(slug="from-uk", name="the UK", short="UK", h1="Outsourcing to Sri Lanka from the UK",
         title="Outsourcing to Sri Lanka from the UK: BPO, accounting and offshore teams",
         desc="How UK companies, accounting firms, insurers and law firms outsource to Sri Lanka: time zone, the best fit services, data protection, examples and how to start.",
         answer="UK businesses have outsourced to Sri Lanka for more than 20 years. HSBC opened its Colombo operations in 2004, the London Stock Exchange Group employs more than 1,600 people there, and in 2025 the UK specialist insurer CFC opened a 200 seat hub in Colombo. Sri Lanka is 4.5 hours ahead of the UK in summer and 5.5 in winter, so a team starting early afternoon covers the full UK day, and work processed in the Sri Lankan morning is ready before London opens.",
         tz="4.5 hours ahead (BST) or 5.5 hours ahead (GMT)", best=["accounting-bookkeeping-outsourcing-sri-lanka", "insurance-hr-payroll-outsourcing-sri-lanka", "legal-process-outsourcing-sri-lanka", "engineering-design-bim-outsourcing-sri-lanka", "customer-support-outsourcing-sri-lanka"],
         law="Your UK GDPR obligations still apply when data is processed in Sri Lanka. Use a data processing agreement with international transfer terms, and expect Sri Lanka's own data protection law to apply to processors from 1 January 2027. If you engage individual contractors, take advice on how IR35 applies to your arrangement.",
         proof=[("HSBC has run operations in Colombo since 2004, serving 24 markets.", "HSBC Sri Lanka", "https://www.about.hsbc.lk/hsbc-in-sri-lanka/hsbc-electronic-data-processing"),
                ("LSEG's Colombo hubs employ more than 1,600 people.", "LSEG careers", "https://www.lseg.com/en/careers/where-we-work/colombo-sri-lanka"),
                ("UK specialist insurer CFC opened a 200 seat global services hub in Colombo in October 2025.", "Daily Mirror", "https://www.dailymirror.lk/business-news/Virtusa-partners-to-unveil-200-seat-digital-service-hub-in-Sri-Lanka/273-323084"),
                ("A UK managed BIM team delivers Revit, clash detection and RIBA work packages from Sri Lanka.", "Company website", "https://thesourcingcollective.co.uk/about-us-bim-manager-team/"),
                ("A Colombo legal process outsourcing firm serves UK clients among more than 14 jurisdictions.", "Daily FT", "https://www.ft.lk/HR/Women-led-LPO-services-firm-Velox-Partners-enters-new-office-space-in-Colombo/47-746421")],
         faqs=[("Do UK companies outsource to Sri Lanka?", "Yes. HSBC, the London Stock Exchange Group and the specialist insurer CFC all run operations in Colombo, and UK accounting, law and architecture firms use Sri Lankan teams."),
               ("What time difference is there between the UK and Sri Lanka?", "Sri Lanka is 4.5 hours ahead of the UK in British Summer Time and 5.5 hours ahead in winter. Sri Lanka has no daylight saving."),
               ("Is outsourcing to Sri Lanka GDPR compliant?", "It can be. Compliance depends on your contract and the provider's controls: a data processing agreement, approved transfer terms and appropriate security. Sri Lanka's Personal Data Protection Act also applies from 1 January 2027.")]),
    dict(slug="from-australia", name="Australia", short="Australia", h1="Outsourcing to Sri Lanka from Australia",
         title="Outsourcing to Sri Lanka from Australia: offshore staff, accounting and BPO",
         desc="How Australian businesses and accounting firms build offshore teams in Sri Lanka: time zone overlap, the best fit services, providers that serve Australia and how to start.",
         answer="Australian businesses are one of Sri Lanka's main outsourcing markets, especially accounting firms, professional services and growing companies hiring offshore staff. Sri Lanka is 4.5 to 5.5 hours behind Sydney and 2.5 hours behind Perth, so the Sri Lankan morning overlaps the Australian afternoon and overnight work is ready for the next morning. Remote staffing providers in Colombo employ staff locally for Australian clients, and Australian firms signed new contracts to build Sri Lankan teams in 2026.",
         tz="4.5 to 5.5 hours behind Sydney and Melbourne, 2.5 hours behind Perth", best=["accounting-bookkeeping-outsourcing-sri-lanka", "virtual-assistants-sri-lanka", "digital-marketing-outsourcing-sri-lanka", "insurance-hr-payroll-outsourcing-sri-lanka", "engineering-design-bim-outsourcing-sri-lanka"],
         law="The Australian Privacy Principles still apply to personal information you send offshore, so choose a provider with strong security and contract for it. Staff employed by a Sri Lankan provider are employed under Sri Lankan law, and Australian superannuation does not normally apply to them; confirm your position with an adviser.",
         proof=[("Sri Lankan staffing firms provide remote staff, employer of record, payroll and recruitment for Australian companies without a local entity.", "Outsource Accelerator", "https://www.outsourceaccelerator.com/articles/hire-remote-staff-sri-lanka-australia/"),
                ("Two Australian companies signed two year contracts in 2026 to build teams in Sri Lanka.", "Outsource Accelerator", "https://news.outsourceaccelerator.com/formix-australian-it-contracts/"),
                ("A global remote staffing firm opened its Colombo office in 2022 to serve Australian and other clients.", "EIN Presswire", "https://www.einpresswire.com/article/596646716/emapta-sri-lanka-celebrates-first-year-as-global-expansion-continues"),
                ("Australia, the UK, the Nordics and North America were named as the main markets of Sri Lanka's business process industry.", "Echelon", "https://echelon.lk/the-growing-influence-of-sri-lankas-bpm-industry")],
         faqs=[("Do Australian companies outsource to Sri Lanka?", "Yes. Australia is one of the main markets for Sri Lankan business process firms, particularly for accounting, administration, marketing and payroll teams."),
               ("What is the time difference between Australia and Sri Lanka?", "Sri Lanka is 4.5 hours behind Sydney and Melbourne in winter and 5.5 hours behind during Australian daylight saving, and 2.5 hours behind Perth."),
               ("Sri Lanka or the Philippines for Australian offshore staff?", "The Philippines is larger and closer in time. Sri Lanka suits Australian firms that want qualified accountants and finance staff, and teams with strong business backgrounds. See our comparison page.")]),
    dict(slug="from-usa", name="the USA", short="USA", h1="Outsourcing to Sri Lanka from the USA",
         title="Outsourcing to Sri Lanka from the USA: medical billing, research and back office",
         desc="How US companies use Sri Lanka for overnight back office, medical billing, investment research and finance operations. Time zones, best fit services and how to start.",
         answer="US companies use Sri Lanka mainly for work that benefits from an overnight turnaround: medical billing and revenue cycle management, investment research, finance operations and data work. Sri Lanka is 9.5 to 13.5 hours ahead of the US, so claims, reconciliations and research processed during the Sri Lankan day are ready when US offices open. Investment research firms in Colombo serve Wall Street institutions, and revenue cycle firms serve US hospitals and practices.",
         tz="9.5 to 10.5 hours ahead of New York, 12.5 to 13.5 hours ahead of California", best=["medical-billing-outsourcing-sri-lanka", "investment-research-kpo-sri-lanka", "accounting-bookkeeping-outsourcing-sri-lanka", "data-annotation-sri-lanka", "customer-support-outsourcing-sri-lanka"],
         law="For healthcare work, sign a HIPAA business associate agreement and check the provider's security controls. For other personal data, apply your state privacy obligations through your contract. Sri Lanka's data protection law applies to processors from 1 January 2027.",
         proof=[("Acuity Knowledge Partners' Sri Lankan team serves more than 50 global financial institutions.", "Acuity", "https://www.acuitykp.com/news/press-release/acuity-knowledge-partners-reaffirms-commitment-to-sri-lanka"),
                ("A 300 seat medical billing and coding centre opened in Kandy in 2024, serving the US, UK and Australia.", "Daily Mirror", "https://dailymirror.lk/print/business-news/HealthRecon-Connect-opens-new-Kandy-office/273-296315"),
                ("Medical transcription teams in Sri Lanka work around the clock for US hospital groups.", "EDB directory", "https://www.srilankabusiness.com/exporters-directory/company-profiles/medsource-pvt-ltd/"),
                ("A Colombo company runs a US revenue cycle team on its own billing software.", "Daily FT", "https://www.ft.lk/Healthcare/Medcube-releases-AI-driven-medical-billing-software/45-766387")],
         faqs=[("Do US companies outsource to Sri Lanka?", "Yes, especially for medical billing, investment research, finance operations and software. The time difference gives an overnight turnaround."),
               ("Can a Sri Lankan team work US hours?", "Yes, on night shifts, which is standard in US facing healthcare and support work. For back office work, most US clients prefer the overnight model.")]),
    dict(slug="from-uae", name="the UAE", short="UAE", h1="Outsourcing to Sri Lanka from the UAE and the Gulf",
         title="Outsourcing to Sri Lanka from Dubai and the UAE: back office and offshore teams",
         desc="How UAE and Gulf companies use Sri Lanka for finance, quantity surveying, marketing, support and virtual assistance, working almost the same day. Best fit services and how to start.",
         answer="For companies in Dubai, Abu Dhabi and the wider Gulf, Sri Lanka is one of the closest offshore options: 1.5 hours ahead of the UAE and a short flight from Colombo. Sri Lankan teams already work in Gulf construction, finance and hospitality, and providers serve UAE clients with accountants, quantity surveyors, marketers, support agents and virtual assistants who share almost the whole working day.",
         tz="1.5 hours ahead of the UAE, 2.5 hours ahead of Saudi Arabia", best=["accounting-bookkeeping-outsourcing-sri-lanka", "engineering-design-bim-outsourcing-sri-lanka", "digital-marketing-outsourcing-sri-lanka", "virtual-assistants-sri-lanka", "customer-support-outsourcing-sri-lanka"],
         law="Apply the UAE Personal Data Protection Law, or DIFC or ADGM rules if you are in a free zone, to data you send offshore, through your contract with the provider. Sri Lanka's data protection law applies to processors from 1 January 2027.",
         proof=[("Exporters listed with the Export Development Board offer virtual assistant and back office services with a notable client presence in the UAE.", "EDB directory", "https://www.srilankabusiness.com/exporters-directory/company-profiles/sterling-bpo-solution-pvt-ltd/"),
                ("A Colombo digital agency is expanding into the Middle East after working across 45 countries.", "Echelon", "https://echelon.lk/emarketingeye-from-pioneering-digital-marketing-in-sri-lanka-to-global-heavyweight"),
                ("Specialist accounting outsourcing firms in Colombo serve clients in the Middle East alongside the UK, US and Australia.", "Daily FT", "https://www.ft.lk/it-telecom-tech/Infomate-reveals-ambitious-growth-plans-and-introduces-new-world-class-facility/50-754756"),
                ("University research finds BIM modelling and bills of quantities well suited to outsourcing from Sri Lanka.", "University of Moratuwa", "https://dl.lib.uom.lk/items/a660b2ba-74ed-4549-899b-4a28d8f1e1ce/full")],
         faqs=[("What is the time difference between Dubai and Sri Lanka?", "Sri Lanka is 1.5 hours ahead of the UAE all year, as neither uses daylight saving."),
               ("Can a Dubai company hire staff in Sri Lanka without a company there?", "Yes, through a remote staffing provider or an employer of record, or by engaging contractors. See our guides to employers of record and to paying people in Sri Lanka.")]),
]

TZS = {"from-uk": "4.5 to 5.5 hrs ahead", "from-australia": "4.5 to 5.5 hrs behind Sydney", "from-usa": "9.5 to 13.5 hrs ahead", "from-uae": "1.5 hrs ahead"}

# ---------------------------------------------------------------- company directory
DIRECTORY = [
    ("Finance, accounting and shared services", [
        ("HSBC", "Its own Colombo centre since 2004: fund administration, lending and trade operations for 24 markets.", "Global (captive)", "https://www.about.hsbc.lk/hsbc-in-sri-lanka/hsbc-electronic-data-processing"),
        ("London Stock Exchange Group", "Colombo and Malabe hubs with more than 1,600 people, including finance and data roles.", "Global (captive)", "https://www.lseg.com/en/careers/where-we-work/colombo-sri-lanka"),
        ("Specialist accounting providers", "Accounting outsourcing firms with hundreds of staff running AP, AR, ledgers, reconciliations and reporting.", "UK, US, Australia, Nordics, Middle East", "https://www.ft.lk/it-telecom-tech/Infomate-reveals-ambitious-growth-plans-and-introduces-new-world-class-facility/50-754756"),
        ("Big Four delivery centres", "Global delivery centres supporting audit, business process and analytics work for their member firms.", "Global (captive)", "https://www.dailynews.lk/2024/03/27/business/467550/ey-gds-sri-lanka-increase-local-presence-by-100/"),
        ("Accounting teams for Australian firms", "Providers placing dedicated finance, HR and admin teams with Australian, Canadian, US and UK clients.", "Australia, Canada, US, UK", "https://srilankabusiness.com/exporters-directory/company-profiles/h-connect-international-pvt-ltd"),
    ]),
    ("Investment research and analytics", [
        ("Acuity Knowledge Partners", "Equity, credit and fixed income research, data science and deal support; began as Amba Research in Colombo in 2003.", "US, UK, Europe, Australia", "https://www.acuitykp.com/news/press-release/acuity-knowledge-partners-reaffirms-commitment-to-sri-lanka"),
    ]),
    ("Healthcare revenue cycle and medical billing", [
        ("Large revenue cycle centres", "Medical billing, coding and claims management, including a 300 seat centre in Kandy opened in 2024.", "US, UK, Australia", "https://dailymirror.lk/print/business-news/HealthRecon-Connect-opens-new-Kandy-office/273-296315"),
        ("Software led billing teams", "US revenue cycle teams running billing, submissions, posting and collections on their own platforms.", "US", "https://www.ft.lk/Healthcare/Medcube-releases-AI-driven-medical-billing-software/45-766387"),
        ("Medical transcription", "Teams of 250+ working around the clock for US hospital groups.", "US", "https://www.srilankabusiness.com/exporters-directory/company-profiles/medsource-pvt-ltd/"),
    ]),
    ("Insurance, HR, payroll and recruitment", [
        ("CFC", "The UK specialist insurer opened a 200 seat global services hub in Colombo in 2025.", "UK (captive)", "https://www.dailymirror.lk/business-news/Virtusa-partners-to-unveil-200-seat-digital-service-hub-in-Sri-Lanka/273-323084"),
        ("Private equity portfolio centres", "Centres serving the software companies of global private equity owners, with business process teams.", "Americas, Europe", "https://www.themorning.lk/articles/DVbn77E2JVlO4Il2tkMb"),
        ("Recruitment and payroll providers", "RPO, employer of record, PEO and payroll firms, the largest with 300+ staff.", "Global", "https://www.srilankabusiness.com/exporters-directory/company-profiles/sourceone-bpo-private-limited/"),
    ]),
    ("Remote staffing and virtual assistants", [
        ("Global remote staffing firms", "International staffing brands with Colombo offices, employing dedicated staff for overseas clients.", "Australia, global", "https://www.einpresswire.com/article/596646716/emapta-sri-lanka-celebrates-first-year-as-global-expansion-continues"),
        ("Local remote staffing providers", "Sri Lankan firms offering dedicated staff, employer of record and payroll for clients without an entity.", "Australia", "https://www.outsourceaccelerator.com/articles/hire-remote-staff-sri-lanka-australia/"),
        ("Virtual assistant services", "Round the clock assistant and back office services.", "Australia, UAE", "https://www.srilankabusiness.com/exporters-directory/company-profiles/sterling-bpo-solution-pvt-ltd/"),
    ]),
    ("Customer support and contact centres", [
        ("Global business process firms", "Customer care and operations from Colombo since 2004, with 300+ jobs added in 2025.", "UK, US, global", "https://www.dailymirror.lk/print/business-news/WNS-strengthens-commitment-to-SL-with-Orion-City-expansion/273-304576"),
        ("Local contact centres", "Inbound and outbound contact centres, including for airlines and hospitality.", "Global", "https://www.srilankabusiness.com/exporters-directory/company-profiles/the-edge-group-pvt-ltd/"),
    ]),
    ("Legal process outsourcing", [
        ("Specialist LPO firms", "Paralegal, research and contract support for clients in more than 14 jurisdictions.", "UK, Australia, Singapore", "https://www.ft.lk/HR/Women-led-LPO-services-firm-Velox-Partners-enters-new-office-space-in-Colombo/47-746421"),
        ("Law firm support centres", "Offshore teams handling administration, finance and client service for law firms.", "Law firms abroad", "https://dailymirror.lk/print/business-news/Imperial-establishes-offshore-LPO-firm-in-Sri-Lanka/273-294093"),
        ("Legal talent platforms", "Connecting Sri Lankan legal professionals with law firms and in-house teams.", "Australia, UK, US", "https://www.dailymirror.lk/press_releases/Beyond-the-Square-How-a-Homegrown-Startup-Is-Taking-Sri-Lankan-Legal-Talent-Global/335-324277"),
    ]),
    ("Engineering design, BIM and quantity surveying", [
        ("UK managed BIM teams", "Revit, clash detection, shop drawings and scan to BIM delivered from Sri Lanka.", "UK", "https://thesourcingcollective.co.uk/about-us-bim-manager-team/"),
        ("Engineering design studios", "BIM and CAD, 3D walkthroughs, surveys and quantity surveying.", "International", "https://www.ft.lk/Business/Nex-Gen-Engineering-Studio-opens-new-corporate-office/34-765199"),
    ]),
    ("Data, annotation and content processing", [
        ("Data services firms", "Data annotation and visual tasking; one won a 2025 Presidential Export Award.", "International", "https://ft.lk/business/OREL-IT-wins-top-honour-at-Presidential-Export-Awards/34-774823"),
        ("Content conversion firms", "Data and content conversion, some with Board of Investment status since 1994.", "International", "https://www.srilankabusiness.com/exporters-directory/company-profiles/innodata-lanka-pvt-ltd/"),
    ]),
    ("Digital marketing", [
        ("Digital agencies", "SEO, paid media and social for international clients; one founded in 2007 has worked across 45 countries.", "Southeast Asia, Australia, Middle East", "https://echelon.lk/emarketingeye-from-pioneering-digital-marketing-in-sri-lanka-to-global-heavyweight"),
    ]),
]

DIR_FAQS = [
    ("What are the biggest BPO companies in Sri Lanka?", "Among the largest are the captive centres of global firms such as HSBC and the London Stock Exchange Group, the investment research firm Acuity Knowledge Partners, and global business process firms that have operated in Colombo since 2004, alongside specialist providers in accounting, medical billing, legal support and remote staffing. We introduce buyers to the right ones for their needs."),
    ("How many BPO companies are there in Sri Lanka?", "The industry body SLASSCOM counts more than 680 IT and BPM companies employing about 175,000 people. There is no current official count of business process firms alone."),
    ("Which outsourcing companies in Sri Lanka serve Australian clients?", "Several remote staffing, accounting and payroll providers in Colombo serve Australia as a main market, and Australian firms signed new contracts to build Sri Lankan teams in 2026. Tell us what you need and we will introduce two or three that fit."),
    ("Are there medical billing companies in Sri Lanka?", "Yes. Revenue cycle firms in Colombo and Kandy serve mainly US healthcare providers, including one with a 300 seat Kandy centre opened in 2024."),
]


def build_markets(B, stories, caps, cta, markets_tbl):
    paths = []
    bylabel = {c["slug"]: c for c in caps}
    for m in MARKET_PAGES:
        prefix = "../../"
        path = f"offshoring/{m['slug']}/"
        faq, faq_ld = SP.faq_block(stories, m["faqs"])
        best = "".join(f'<li><a href="../{s}/"><strong>{e(bylabel[s]["label"])}</strong></a>: {e(bylabel[s]["short"])}</li>' for s in m["best"])
        proof = '<ul class="ticks">' + "".join(f"<li>{e(t)} {a(src, u)}</li>" for t, src, u in m["proof"]) + "</ul>"
        others = SP.chip_links([("From " + x["short"], f"../{x['slug']}/") for x in MARKET_PAGES if x is not m])
        body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Offshoring", "../")])}
  <h1>{e(m['h1'])}</h1>
  <p class="answer">{e(m['answer'])}</p>
  <p class="reviewed">Last reviewed 23 October 2026. Sources are linked next to each fact.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <img class="story-cover art" src="{prefix}assets/art/g-countries.svg" alt="Outsourcing to Sri Lanka from {e(m['name'])}, illustration" width="1200" height="900">
  {SP.stats_strip([(TZS[m['slug']], "time difference"), ("20+ years", "of global operations in Colombo"), ("$1.64B", "IT and BPM exports in 2025")])}
  <h2 class="h-sub mt">What {e(m['name'])} companies outsource to Sri Lanka</h2>
  <ul class="ticks">{best}</ul>
  <h2 class="h-sub mt">Evidence from {e(m['name'])}</h2>
  {proof}
  <h2 class="h-sub mt">Working hours</h2>
  <p class="body-l">Sri Lanka is {e(m['tz'])}, with no daylight saving.</p>
  {markets_tbl}
  <h2 class="h-sub mt">Contracts, data and compliance</h2>
  <p class="body-l">{e(m['law'])} For hiring routes and payroll, see <a href="{prefix}guides/how-to-hire-in-sri-lanka/">how to hire</a> and <a href="{prefix}guides/pay-employees-and-contractors-in-sri-lanka/">how to pay people in Sri Lanka</a>.</p>
  {cta(B, prefix, m['slug'])}
  {faq}
  <h2 class="h-sub mt">Outsourcing to Sri Lanka from other markets</h2>
  {others}
  <p class="body-l mt">See also: <a href="../">All business services</a> · <a href="../bpo-companies-sri-lanka/">BPO companies in Sri Lanka</a> · <a href="{prefix}compare/philippines/">Sri Lanka vs the Philippines</a></p>
</div></section>
"""
        head = faq_ld + SP.crumbs_ld(B, [("Offshoring", "offshoring/"), ("From " + m["short"], path)])
        B.write(path + "index.html", B.page(m["h1"], m["desc"], body, prefix, path, extra_head=head, active="services", seo_title=m["title"]))
        paths.append(path)
    return paths


def build_directory(B, stories, cta):
    prefix = "../../"
    path = "offshoring/bpo-companies-sri-lanka/"
    faq, faq_ld = SP.faq_block(stories, DIR_FAQS)
    blocks = ""
    n = 0
    for grp, rows in DIRECTORY:
        n += len(rows)
        blocks += f'<h2 class="h-sub mt">{e(grp)}</h2><div class="tbl"><table><thead><tr><th>Who</th><th>What they do from Sri Lanka</th><th>Markets</th></tr></thead><tbody>' + "".join(
            f"<tr><td><strong>{e(nm)}</strong></td><td>{e(wh)} {a('Source', u)}</td><td>{e(mk)}</td></tr>" for nm, wh, mk, u in rows) + "</tbody></table></div>"
    itemlist = "" and SP.ld({"@context": "https://schema.org", "@type": "ItemList", "name": "BPO and outsourcing companies in Sri Lanka", "numberOfItems": n,
                      "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": nm} for i, nm in enumerate(nm for _, rows in DIRECTORY for nm, _, _, _ in rows)]})
    body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Offshoring", "../")])}
  <h1>BPO and outsourcing companies in Sri Lanka (2026)</h1>
  <p class="answer">Sri Lanka's business process industry ranges from the captive centres of global firms, such as HSBC and the London Stock Exchange Group, to specialist providers in accounting, investment research, medical billing, legal support, remote staffing, engineering design and data. The industry body SLASSCOM counts more than 680 IT and BPM companies employing about 175,000 people. Below is who delivers business services from Sri Lanka to overseas clients, grouped by service, each with a public source. We name global firms running their own centres; for specialist providers we describe what exists and introduce buyers directly.</p>
  <p class="reviewed">Last reviewed 23 October 2026. Not a ranking or an endorsement.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  {blocks}
  <div class="reach mt"><h2>Get introduced to the right providers</h2><p>We know which Sri Lankan providers do this work well. Tell us the service, volumes and hours, and we will introduce two or three that fit, at no cost to you.</p>
  <div class="actions"><a class="btn" href="{prefix}talent/find/?route=offshoring-directory">Request introductions</a><a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a></div></div>
  {faq}
  <p class="body-l mt">See also: <a href="../">All business services</a> · <a href="../from-uk/">From the UK</a> · <a href="../from-australia/">From Australia</a> · <a href="../from-usa/">From the USA</a> · <a href="../from-uae/">From the UAE</a></p>
</div></section>
"""
    head = faq_ld + itemlist + SP.crumbs_ld(B, [("Offshoring", "offshoring/"), ("BPO companies", path)])
    B.write(path + "index.html", B.page("BPO and outsourcing companies in Sri Lanka (2026)",
                                        "Who provides BPO and outsourcing services in Sri Lanka: global captive centres and specialist providers in accounting, research, medical billing, legal, staffing, support and BIM. Sourced, with introductions.",
                                        body, prefix, path, extra_head=head, active="services", seo_title="BPO and outsourcing companies in Sri Lanka (2026 list)"))
    return [path]


ANSWERS = [
    ("Is Sri Lanka good for outsourcing business services?", "Yes for finance and accounting, investment research, medical billing, banking and insurance operations and specialist support. Global firms such as HSBC and LSEG have run operations in Colombo for over 20 years. It is smaller than the largest destinations, so it suits specialist teams more than very large voice operations.", "offshoring/"),
    ("What are the BPO companies in Sri Lanka?", "They range from captive centres of global firms such as HSBC and LSEG and research firms such as Acuity Knowledge Partners, to specialist providers in accounting, medical billing, legal and remote staffing. Our overview describes who does what, with sources, and we can introduce the right providers.", "offshoring/bpo-companies-sri-lanka/"),
    ("Can I outsource bookkeeping to Sri Lanka?", "Yes. Sri Lanka has more than 9,000 Chartered Accountants and 40,000 students, and providers serve UK, Australian, US and Gulf clients in Xero, QuickBooks, MYOB and Sage.", "offshoring/accounting-bookkeeping-outsourcing-sri-lanka/"),
    ("Is Sri Lanka good for medical billing outsourcing?", "Yes, especially for US providers. Revenue cycle firms in Colombo and Kandy work overnight relative to the US, including a 300 seat Kandy centre opened in 2024.", "offshoring/medical-billing-outsourcing-sri-lanka/"),
    ("What is the time difference for outsourcing to Sri Lanka from Australia?", "Sri Lanka is 4.5 to 5.5 hours behind Sydney and 2.5 hours behind Perth, so teams overlap the Australian afternoon.", "offshoring/from-australia/"),
]
