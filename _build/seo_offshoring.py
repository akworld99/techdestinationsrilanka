"""Non-tech offshoring section: a hub on outsourcing to Sri Lanka and one page per business service capability."""
import html

import seo_pages as SP
import seo_offshoring_plus as X
from seo_pages import a

e = html.escape
REVIEWED = "23 October 2026"

# Shared sources
EDB_EXPORTS = "https://www.ft.lk/top-story/Export-earnings-up-5-6-to-17-2-b-in-2025/26-787471"
SLASSCOM_2B = "https://economynext.com/sri-lankas-it-bpo-export-revenue-lower-than-reality-after-crisis-expert-260080/"
SLASSCOM_WF = "https://www.ft.lk/it-telecom-tech/SLASSCOM-reflects-on-a-year-of-creating-opportunities-strengthening-Sri-Lanka-s-knowledge-and-innovation-industry/50-794672"
CASL = "https://www.dailymirror.lk/print/business-news/CA-SL-sets-new-benchmark-with-highest-Chartered-Accountant-number-in-a-single-year/273-324294"
CIMA = "https://www.ft.lk/Most-Admired-Companies-of-Sri-Lanka-2022/AICPA-CIMA/10571-752623"
IPS_AI = "https://www.ft.lk/front-page/Nearly-quarter-of-workforce-exposed-to-GenAI-IPS/44-780522"
EDB_BPM = "https://srilankabusiness.com/bpm"
HSBC = "https://www.about.hsbc.lk/hsbc-in-sri-lanka/hsbc-electronic-data-processing"
LSEG = "https://www.lseg.com/en/careers/where-we-work/colombo-sri-lanka"
FREELANCE = "https://www.themorning.lk/articles/q4VI3ypwaWrlLnH1Rykw"

MARKETS = [
    ("United Kingdom", "4.5 to 5.5 hours ahead", "A Sri Lankan shift starting early afternoon covers the full UK day. Work processed in the Sri Lankan morning is ready before London opens."),
    ("Australia", "4.5 to 5.5 hours behind Sydney, 2.5 behind Perth", "The Sri Lankan morning overlaps the Australian afternoon, and overnight work is ready for the next Australian morning."),
    ("United Arab Emirates", "1.5 hours ahead", "Practically the same working day, with a short flight between Colombo and Dubai."),
    ("United States", "9.5 to 13.5 hours ahead", "Best for overnight processing that is done when the US day starts. Live US-hours support needs night shifts."),
]

CAPS = [
    dict(
        slug="accounting-bookkeeping-outsourcing-sri-lanka", label="Accounting and bookkeeping",
        h1="Accounting and bookkeeping outsourcing to Sri Lanka",
        title="Accounting and bookkeeping outsourcing in Sri Lanka (2026)",
        desc="Outsource bookkeeping, accounts payable, month-end close and management accounts to qualified accountants in Sri Lanka. Evidence, providers, costs and how to start.",
        short="Bookkeeping, AP and AR, month-end close, management accounts and FP&A.",
        answer="Sri Lanka has one of the deepest pools of professionally qualified accountants of any offshore destination: CA Sri Lanka alone has more than 9,000 members and 40,000 students, and around 15,000 people are CIMA students or members. Global banks and exchanges run finance operations in Colombo, including HSBC since 2004 and the London Stock Exchange Group, whose Colombo hubs employ more than 1,600 people. Accounting firms and companies in the UK, Australia, the US and the Gulf outsource bookkeeping, accounts payable and receivable, reconciliations, month-end close and management reporting to Sri Lankan teams.",
        stats=[("9,000+", "CA Sri Lanka members, plus 40,000+ students"), ("15,000", "CIMA students and members"), ("1,600+", "people at LSEG's Colombo hubs")],
        what=["Bookkeeping in Xero, QuickBooks, MYOB, Sage and NetSuite", "Accounts payable and receivable, bank and intercompany reconciliations", "Month-end and year-end close, journals and accruals", "Management accounts with commentary", "FP&A support: budgets, forecasts and variance analysis", "Audit support and working papers for accounting firms", "Payroll processing alongside the ledger"],
        evidence=[
            ("CA Sri Lanka had more than 9,000 members and 40,000 students in November 2025, with its largest ever graduating cohort.", "Daily Mirror", CASL),
            ("AICPA and CIMA count about 15,000 students and members in Sri Lanka.", "Daily FT", CIMA),
            ("HSBC has run operations in Colombo since 2004, including fund administration and lending operations for 24 markets.", "HSBC Sri Lanka", HSBC),
            ("LSEG's Colombo and Malabe hubs employ more than 1,600 people, including financial control and accounting roles.", "LSEG careers", LSEG),
            ("Specialist accounting outsourcing firms serve clients in the UK, US, Australia, the Nordics and the Middle East.", "Daily FT", "https://www.ft.lk/it-telecom-tech/Infomate-reveals-ambitious-growth-plans-and-introduces-new-world-class-facility/50-754756"),
        ],
        ai="Invoice capture, AP keying, bank feeds and routine journals are being automated by OCR and AI accounting tools, and a 2025 Institute of Policy Studies study names clerical roles as the most exposed in Sri Lanka. The work worth outsourcing now is the judgement layer: owning the close, handling exceptions, writing management commentary, reviewing what the automation produces and keeping controls tight. That is where qualified Sri Lankan accountants add value, so buy accountants, not data entry.",
        faqs=[
            ("Is Sri Lanka good for accounting outsourcing?", "Yes. It has a large base of professionally qualified accountants, with more than 9,000 Chartered Accountants and 40,000 students, plus CIMA and ACCA qualified staff, and global banks such as HSBC and LSEG run finance operations in Colombo."),
            ("What accounting work can be outsourced to Sri Lanka?", "Bookkeeping, accounts payable and receivable, reconciliations, month-end close, management accounts, FP&A support, audit support and payroll."),
            ("Do Sri Lankan accountants know UK, Australian and US accounting?", "Many are CIMA, ACCA or CA qualified, which teach IFRS, and firms serving the UK and Australia train staff on local rules such as VAT, GST and BAS. Ask any provider for staff with your specific software and jurisdiction."),
            ("How do I start outsourcing bookkeeping to Sri Lanka?", "Start with one well documented process, such as accounts payable or reconciliations, with one or two people through a provider, then expand once quality is proven. Tell us your volumes and software and we will introduce suitable teams."),
        ],
    ),
    dict(
        slug="investment-research-kpo-sri-lanka", label="Investment research and KPO",
        h1="Investment research and KPO outsourcing to Sri Lanka",
        title="Investment research and KPO outsourcing in Sri Lanka",
        desc="Equity research, credit analysis, data science and fund operations delivered from Colombo for global banks, asset managers and funds. Evidence and how to engage.",
        short="Equity and credit research, financial data, fund operations.",
        answer="Colombo has supported Wall Street and City of London firms for more than two decades. Amba Research, now part of Acuity Knowledge Partners, started in Sri Lanka in 2003, and Acuity's Colombo team serves more than 50 global financial institutions with equity and fixed income research, credit analytics, quantitative work and investment banking support. The London Stock Exchange Group employs more than 1,600 people in Colombo, including data and analytics roles.",
        stats=[("2003", "Amba Research starts in Colombo"), ("50+", "global financial institutions served by Acuity's Colombo team"), ("1,600+", "LSEG employees in Colombo")],
        what=["Equity and fixed income research support", "Credit analysis and commercial lending analytics", "Financial modelling and model maintenance", "Quantitative research and data science", "Fund administration and fund marketing support", "Investment banking pitch and deal support", "Market and competitive research"],
        evidence=[
            ("Acuity Knowledge Partners' Sri Lankan team serves more than 50 leading global financial institutions.", "Acuity", "https://www.acuitykp.com/news/press-release/acuity-knowledge-partners-reaffirms-commitment-to-sri-lanka"),
            ("Colombo teams cover equity and fixed income research, quant and data science, credit analytics and investment banking support for buy and sell side clients.", "Echelon", "https://echelon.lk/the-wall-street-experience-working-from-colombo"),
            ("Amba Research began in Sri Lanka in 2003 and was acquired by Moody's in 2013.", "Daily FT", "https://www.ft.lk/front-page/moodys-acquires-amba-investment-services/44-227314"),
            ("LSEG's Colombo hubs employ more than 1,600 people, including data and analytics roles.", "LSEG careers", LSEG),
            ("HSBC's Colombo centre handles fund administration for its global businesses.", "HSBC Sri Lanka", HSBC),
        ],
        ai="Data extraction from filings, model roll-forwards and first drafts of earnings notes are increasingly automated. The value of an offshore research team now sits in analysis: credit judgement, alternative data, quantitative work and research tailored to your strategy, with analysts using AI tools rather than replaced by them.",
        faqs=[
            ("Which investment research firms operate in Sri Lanka?", "Acuity Knowledge Partners, which began as Amba Research in Colombo in 2003, is the best known. The London Stock Exchange Group and HSBC also run data, analytics and fund operations in Colombo."),
            ("Is Sri Lanka a good location for KPO?", "Yes for finance led knowledge work. It combines professionally qualified accountants and analysts with more than 20 years of serving global banks, though the pool is smaller than the largest KPO destinations."),
            ("Can a small fund or family office use a Sri Lankan research team?", "Yes. Dedicated analysts can be hired through a provider or an employer of record without opening an office. Tell us the coverage you need and we will introduce options."),
        ],
    ),
    dict(
        slug="virtual-assistants-sri-lanka", label="Virtual assistants",
        h1="Hire virtual assistants and remote admin staff in Sri Lanka",
        title="Virtual assistants in Sri Lanka: hire offshore admin and EA support",
        desc="Hire virtual assistants, executive assistants and operations coordinators in Sri Lanka. Who provides them, how much time zone overlap you get, and where AI changes the role.",
        short="Executive and operations assistants, admin and coordination.",
        answer="Australian, UK and Gulf businesses hire virtual and executive assistants in Sri Lanka through remote staffing firms that employ the assistant locally and manage payroll, equipment and compliance. The strongest demand comes from Australia, where the time zone gives a shared afternoon, and from the UAE, which works almost the same day. The role is changing fast: routine scheduling and inbox work is being handled by AI, so the best Sri Lankan assistants are hired as operations coordinators who run those tools and own workflows.",
        stats=[("1.5 hrs", "time difference with the UAE"), ("150,000", "online freelancers in Sri Lanka (ICTA survey)"), ("2022", "year global staffing firm Emapta opened in Colombo")],
        what=["Executive assistant support: calendar, travel, inbox", "Operations coordination and project administration", "CRM updates and sales administration", "Customer and supplier follow-up", "Research and document preparation", "E-commerce and order administration", "Recruitment coordination"],
        evidence=[
            ("Global remote staffing firm Emapta opened its Colombo office in February 2022.", "EIN Presswire", "https://www.einpresswire.com/article/596646716/emapta-sri-lanka-celebrates-first-year-as-global-expansion-continues"),
            ("Sri Lankan staffing firms provide remote staff, employer of record, payroll and recruitment for Australian companies without a local entity.", "Outsource Accelerator", "https://www.outsourceaccelerator.com/articles/hire-remote-staff-sri-lanka-australia/"),
            ("Exporters listed with the Export Development Board offer dedicated virtual assistant services to clients in Australia and the UAE.", "EDB directory", "https://www.srilankabusiness.com/exporters-directory/company-profiles/sterling-bpo-solution-pvt-ltd/"),
            ("An ICTA survey counted about 150,000 online freelancers in Sri Lanka.", "The Morning", FREELANCE),
            ("Clerical support work is the occupation most exposed to generative AI in Sri Lanka, according to the Institute of Policy Studies.", "Daily FT", IPS_AI),
        ],
        ai="This is the most exposed category. AI now drafts emails, books meetings, summarises calls and fills spreadsheets. Hiring a low cost assistant to do those tasks by hand no longer makes sense. Hire someone to own outcomes instead: run your AI tools, keep the CRM clean, chase people and coordinate projects. That is the role Sri Lankan assistants with strong English and business backgrounds fill well.",
        faqs=[
            ("How do I hire a virtual assistant from Sri Lanka?", "Through a remote staffing provider that employs the assistant locally, through an employer of record, or by contracting a freelancer directly. A provider is easiest for a full time, dedicated assistant. See our guide to paying contractors and employees in Sri Lanka."),
            ("Is Sri Lanka or the Philippines better for virtual assistants?", "The Philippines is much larger and scores higher on general English rankings. Sri Lanka suits businesses in the UAE, UK and Australia that want assistants with stronger business, finance or operations backgrounds. Our comparison page covers the differences."),
            ("Can a Sri Lankan virtual assistant work Australian hours?", "Mostly. Sydney is 4.5 to 5.5 hours ahead, so a Sri Lankan assistant starting early overlaps your afternoon fully and your morning partly."),
        ],
    ),
    dict(
        slug="digital-marketing-outsourcing-sri-lanka", label="Digital marketing",
        h1="Digital marketing outsourcing to Sri Lanka",
        title="Digital marketing outsourcing to Sri Lanka: offshore SEO, PPC and content",
        desc="Outsource SEO, paid media, social, content and marketing operations to Sri Lankan teams. What they do well, who uses them and how to set up an offshore marketing team.",
        short="SEO, paid media, social, content and marketing operations.",
        answer="Sri Lankan agencies and remote teams run SEO, paid search and social, content, email and marketing operations for clients in Australia, Southeast Asia, the Middle East and the UK. Digital marketing, advertising and PR outsourcing is one of the business services the Export Development Board promotes, and Australian firms are now building dedicated offshore marketing teams in Colombo. Evidence on the size of this market is thin, so judge providers on case studies rather than country statistics.",
        stats=[("45", "countries one Colombo agency says it has worked in"), ("150,000", "online freelancers, many in design and writing"), ("UTC+5:30", "same working day as the Gulf")],
        what=["SEO: technical, on-page and content", "Paid search and paid social management", "Social media management and community", "Email marketing and automation", "Marketing operations in HubSpot and Salesforce", "Analytics, reporting and attribution", "Landing pages and conversion optimisation"],
        evidence=[
            ("The Export Development Board lists digital marketing, advertising and PR outsourcing among Sri Lanka's business process services.", "EDB", EDB_BPM),
            ("A Colombo digital agency founded in 2007 says it has worked across 45 countries and is expanding into Australia and the Middle East.", "Echelon", "https://echelon.lk/emarketingeye-from-pioneering-digital-marketing-in-sri-lanka-to-global-heavyweight"),
            ("Two Australian companies, one of them a digital marketing firm, signed two year contracts in 2026 to build teams in Sri Lanka.", "Outsource Accelerator", "https://news.outsourceaccelerator.com/formix-australian-it-contracts/"),
            ("About 150,000 Sri Lankans work as online freelancers, with writing and design among the main activities.", "The Morning", FREELANCE),
        ],
        ai="Volume content, ad copy variants, basic audits and scheduling are now cheap to automate. What still needs people is strategy, managing ad spend for return, analytics, conversion work, marketing operations and checking what the AI produces. Build a performance and operations team, not a content factory.",
        faqs=[
            ("Is it worth outsourcing digital marketing to Sri Lanka?", "It can be, for execution and operations work such as paid media management, SEO, email and CRM operations, with strategy kept close to your business. Choose providers on results they can show for clients in your market."),
            ("What are the best digital marketing companies in Sri Lanka?", "Quality varies widely and there is no reliable ranking. Ask for case studies in your country and channel. We can introduce agencies and specialists that fit your brief."),
            ("Can I hire a dedicated offshore marketing team in Sri Lanka?", "Yes. Remote staffing providers and employers of record let you hire marketers who work only for you. See how hiring and payroll work in our guides."),
        ],
    ),
    dict(
        slug="customer-support-outsourcing-sri-lanka", label="Customer support",
        h1="Customer support and back office outsourcing to Sri Lanka",
        title="Customer support outsourcing to Sri Lanka: BPO and call centres",
        desc="Email, chat and voice support, operations and back office from Sri Lanka. Which companies run them, the time zone fit for UK, Australian and Gulf customers, and AI's impact.",
        short="Email, chat and voice support, customer operations and back office.",
        answer="Sri Lanka's strongest track record in customer operations is in banking, insurance and complex servicing rather than high volume call centres. HSBC has served customers in 24 markets from Colombo since 2004, WNS has delivered from Colombo for more than 20 years and added over 300 jobs in 2025, and local business process firms run contact centres for airlines, hospitality and retail. The time zone suits UK, Gulf and Australian customers well. For live US hours, teams work night shifts.",
        stats=[("2004", "HSBC and WNS begin operations in Colombo"), ("24", "markets served by HSBC's Colombo centre"), ("300+", "jobs WNS added in Colombo in 2025")],
        what=["Email and chat support", "Voice support for the UK, Gulf and Australia", "Order, claims and account servicing", "Customer due diligence and KYC operations", "Escalations and complaints handling", "Quality assurance of AI agents and knowledge bases"],
        evidence=[
            ("HSBC's Colombo centre has handled customer due diligence, lending operations and trade transactions for 24 markets since 2004.", "HSBC Sri Lanka", HSBC),
            ("WNS added 13,000 square feet and more than 300 jobs in Colombo in March 2025.", "Daily Mirror", "https://www.dailymirror.lk/print/business-news/WNS-strengthens-commitment-to-SL-with-Orion-City-expansion/273-304576"),
            ("Local business process firms run inbound and outbound contact centres, including for airlines and hospitality.", "EDB directory", "https://www.srilankabusiness.com/exporters-directory/company-profiles/the-edge-group-pvt-ltd/"),
            ("Official figures put Sri Lanka's IT and business process exports at USD 1.64 billion in 2025, up 8.8%.", "Daily FT", EDB_EXPORTS),
        ],
        ai="Tier one chat and email, such as order status and password resets, is moving to AI agents. Outsourced teams are now most valuable for escalations, regulated and complex cases, retention conversations, and supervising and improving the AI agents themselves. Sri Lanka's banking and insurance servicing background fits that shift.",
        faqs=[
            ("Are there call centres in Sri Lanka for international clients?", "Yes, though the sector is smaller than the largest call centre destinations. Its strengths are banking, insurance and complex servicing, with operations such as HSBC's and WNS's running since 2004."),
            ("Can a Sri Lankan team support customers in UK hours?", "Yes. Sri Lanka is 4.5 to 5.5 hours ahead of the UK, so an afternoon and evening shift covers the UK business day."),
            ("Is customer support outsourcing still worth it with AI?", "For simple, repetitive queries, AI is now cheaper. For complex, regulated or high value conversations, and for running and checking the AI, people still matter, and that is where an offshore team pays off."),
        ],
    ),
    dict(
        slug="medical-billing-outsourcing-sri-lanka", label="Medical billing and RCM",
        h1="Medical billing and revenue cycle outsourcing to Sri Lanka",
        title="Medical billing and RCM outsourcing to Sri Lanka",
        desc="US medical billing, coding, denials and AR follow-up delivered from Sri Lanka. Providers, evidence, the US time zone model and where AI changes the work.",
        short="Medical billing, coding, denials and AR follow-up for US providers.",
        answer="Sri Lanka has a long running healthcare revenue cycle industry serving mainly US hospitals and practices. Medical billing, coding, claims submission, payment posting, denials management and AR follow-up are delivered from Colombo and Kandy, where one provider opened a 300 seat centre in 2024. The overnight time difference with the US means claims worked in Sri Lanka are processed by the time US offices open.",
        stats=[("300", "seats in one Kandy medical billing centre"), ("2,000+", "people in healthcare RCM by 2018"), ("Overnight", "turnaround for US claims")],
        what=["Medical billing and claims submission", "Medical coding and coding audits", "Eligibility and benefits verification", "Payment posting", "Denials management and AR follow-up", "Credentialing support"],
        evidence=[
            ("A 300 seat centre in Kandy opened in 2024 for medical billing, coding and claims management serving the US, UK and Australia.", "Daily Mirror", "https://dailymirror.lk/print/business-news/HealthRecon-Connect-opens-new-Kandy-office/273-296315"),
            ("A Colombo company runs a US revenue cycle team, covering billing, submissions, posting and collections, on its own software.", "Daily FT", "https://www.ft.lk/Healthcare/Medcube-releases-AI-driven-medical-billing-software/45-766387"),
            ("Healthcare RCM companies in Sri Lanka grew from 3 in 2012 to 11 in 2018, and employment from 375 to more than 2,000.", "Daily FT, 2018", "https://www.ft.lk/business/Aspire-RCM-offers-young-professionals-and-RCM-companies-pathway-to-shine-in-booming-KPO-industry/34-661978"),
            ("Medical transcription teams in Sri Lanka work around the clock for US hospital groups.", "EDB directory", "https://www.srilankabusiness.com/exporters-directory/company-profiles/medsource-pvt-ltd/"),
        ],
        ai="Transcription is largely being replaced by speech recognition and AI scribes, and charge entry and eligibility checks are increasingly automated. The work that stays human is denials management, complex AR follow-up, certified coding audits and payer communication. Choose a provider that already uses automation and sells those skills.",
        faqs=[
            ("Is Sri Lanka good for medical billing outsourcing?", "Yes, especially for US practices and hospital groups. The industry has served US clients for more than a decade, works overnight relative to the US, and has providers with hundreds of seats."),
            ("Is outsourcing medical billing to Sri Lanka HIPAA compliant?", "It can be. Compliance depends on the provider's controls and the business associate agreement you sign, not the country. Ask for their security certifications and audit history."),
            ("What does medical billing outsourcing to Sri Lanka cost?", "Providers price per FTE or as a percentage of collections. Ask two or three for quotes on your specialty and volume. We can introduce providers."),
        ],
    ),
    dict(
        slug="legal-process-outsourcing-sri-lanka", label="Legal process outsourcing",
        h1="Legal process outsourcing (LPO) to Sri Lanka",
        title="Legal process outsourcing to Sri Lanka: offshore paralegal and legal support",
        desc="Offshore paralegals, contract review, legal research, conveyancing and company secretarial support from Sri Lanka for UK, Australian and US law firms.",
        short="Paralegal, contract review, legal research and company secretarial.",
        answer="Sri Lankan legal process outsourcing firms provide paralegal support, contract drafting and review, legal research, matter administration and company secretarial work for law firms and in-house teams in the UK, Australia, Singapore and the US. Sri Lankan lawyers train in English in a system with common law roots, which makes them a natural fit for UK and Australian work. This is a small, specialist market: choose providers on the jurisdictions they already serve.",
        stats=[("14+", "jurisdictions served by one Colombo LPO"), ("UK, AU, US", "main client markets"), ("English", "language of legal training")],
        what=["Paralegal and legal assistant support", "Contract drafting under instruction and contract review", "Legal research and memos", "Document review and e-discovery QA", "Conveyancing and matter administration", "Company secretarial and corporate compliance"],
        evidence=[
            ("A women led Colombo LPO, operating since 2020, serves clients in the UK, Australia, Singapore and Southeast Asia across more than 14 jurisdictions.", "Daily FT", "https://www.ft.lk/HR/Women-led-LPO-services-firm-Velox-Partners-enters-new-office-space-in-Colombo/47-746421"),
            ("A firm established an offshore LPO in Sri Lanka in 2024 to support law firms with administration, finance and client service.", "Daily Mirror", "https://dailymirror.lk/print/business-news/Imperial-establishes-offshore-LPO-firm-in-Sri-Lanka/273-294093"),
            ("A legal services provider connects Sri Lankan legal professionals with law firms and in-house teams in Australia, the UK and the US.", "Daily Mirror", "https://www.dailymirror.lk/press_releases/Beyond-the-Square-How-a-Homegrown-Startup-Is-Taking-Sri-Lankan-Legal-Talent-Global/335-324277"),
            ("The Export Development Board lists legal and company secretarial services among Sri Lanka's business process services.", "EDB", EDB_BPM),
        ],
        ai="First pass document review, clause extraction and research summaries are being automated by legal AI tools. The useful offshore role is now the qualified reviewer: lawyers who check AI output, draft under instruction and run matter administration. Buy legal judgement, not page turning.",
        faqs=[
            ("What is legal process outsourcing?", "Sending legal support work, such as research, document and contract review, drafting under instruction and administration, to a specialist team, often offshore, supervised by your own lawyers."),
            ("Is Sri Lanka good for legal process outsourcing?", "For UK, Australian and Singapore work it can be: lawyers are trained in English in a system with common law roots, and specialist LPO firms already serve those markets. The market is small, so check each provider's experience in your jurisdiction."),
            ("Can Sri Lankan paralegals work on UK matters?", "Yes, under the supervision of your qualified lawyers, which is how legal process outsourcing works everywhere. Regulated activities stay with your firm."),
        ],
    ),
    dict(
        slug="engineering-design-bim-outsourcing-sri-lanka", label="Engineering, BIM and quantity surveying",
        h1="Engineering design, BIM and quantity surveying outsourcing to Sri Lanka",
        title="BIM, CAD drafting and quantity surveying outsourcing to Sri Lanka",
        desc="BIM modelling, CAD drafting, structural detailing and quantity surveying from Sri Lanka for UK, Australian and Gulf construction firms. Evidence and how to engage.",
        short="BIM modelling, CAD drafting, detailing, estimating and BOQs.",
        answer="Sri Lankan engineering and design firms deliver BIM modelling, Revit and CAD drafting, structural detailing, 3D visualisation and quantity surveying for construction clients in the UK, Australia and the Gulf. Quantity surveying is a well established profession in Sri Lanka with strong links to Gulf construction, and university research identifies BIM modelling and bill of quantities preparation as well suited to outsourcing. This is a growing, specialist area with smaller firms rather than large centres.",
        stats=[("1.5 hrs", "time difference with Gulf project teams"), ("BIM and BOQ", "tasks research finds best suited to outsourcing"), ("UK, AU, Gulf", "main client markets")],
        what=["BIM modelling and coordination in Revit", "Clash detection and scan to BIM", "CAD drafting and shop drawings", "Structural and MEP detailing", "Quantity take off, BOQ preparation and estimating", "Architectural visualisation and walkthroughs"],
        evidence=[
            ("A UK managed, architect founded BIM team delivers Revit families, clash detection, shop drawings and scan to BIM from Sri Lanka.", "The Sourcing Collective", "https://thesourcingcollective.co.uk/about-us-bim-manager-team/"),
            ("A University of Moratuwa study (2023) finds outsourcing quantity surveying feasible, with BIM model creation and BOQ preparation the most suitable activities.", "University of Moratuwa", "https://dl.lib.uom.lk/items/a660b2ba-74ed-4549-899b-4a28d8f1e1ce/full"),
            ("A Colombo BIM and CAD studio opened a new office in 2024 citing international work.", "Daily FT", "https://www.ft.lk/Business/Nex-Gen-Engineering-Studio-opens-new-corporate-office/34-765199"),
            ("The Export Development Board lists civil engineering services among Sri Lanka's business process services.", "EDB", EDB_BPM),
        ],
        ai="Automated take off and AI assisted drafting are improving, but BIM coordination, clash resolution, code compliant detailing and quantity surveying judgement remain skilled work. Exposure is lower here than in most back office categories.",
        faqs=[
            ("Can I outsource BIM modelling to Sri Lanka?", "Yes. Sri Lankan firms model and coordinate in Revit for UK and Australian projects, including clash detection and scan to BIM."),
            ("Is quantity surveying outsourced to Sri Lanka?", "Yes. Sri Lanka has a strong quantity surveying profession, and take off, bills of quantities and estimating are commonly done for Gulf, UK and Australian contractors."),
            ("How do I find a BIM or QS team in Sri Lanka?", "Tell us the software, standards and project types and we will introduce firms or individuals who fit."),
        ],
    ),
    dict(
        slug="data-annotation-sri-lanka", label="Data annotation and AI data",
        h1="Data annotation and AI training data services in Sri Lanka",
        title="Data annotation and AI training data services in Sri Lanka",
        desc="Data labelling, annotation, data conversion and Sinhala and Tamil language data from Sri Lanka. An honest view of the capability and how it is changing.",
        short="Labelling, data conversion, LLM evaluation and local language data.",
        answer="Sri Lankan companies provide data annotation, image labelling, data conversion and content processing for international clients, and some have done data work for more than 30 years. It is an emerging rather than a large scale capability: there is no big dedicated annotation centre, but there are established data processing firms and a growing pool of graduates for higher value work such as LLM evaluation and Sinhala and Tamil language data.",
        stats=[("1994", "a data conversion firm gains BOI status"), ("2025", "Presidential Export Award for a data services firm"), ("Sinhala, Tamil", "low resource language data")],
        what=["Image, text and video annotation", "Data conversion and structuring", "LLM output evaluation and rating", "Domain expert labelling in finance and legal", "Sinhala and Tamil language data", "Data quality checks"],
        evidence=[
            ("A Colombo data services firm founded in 2010 offers data annotation and visual tasking, and won the most innovative service provider award at the 2025 Presidential Export Awards.", "Daily FT", "https://ft.lk/business/OREL-IT-wins-top-honour-at-Presidential-Export-Awards/34-774823"),
            ("A data and content conversion company has operated with Board of Investment status since 1994.", "EDB directory", "https://www.srilankabusiness.com/exporters-directory/company-profiles/innodata-lanka-pvt-ltd/"),
            ("Business process firms list image annotation among their services.", "Echelon", "https://echelon.lk/the-growing-influence-of-sri-lankas-bpm-industry"),
            ("Data analysis roles in business process work are becoming more exposed to generative AI.", "Echelon", "https://echelon.lk/ai-exposure-outpaces-job-readiness/"),
        ],
        ai="Simple labelling is being automated by pre-labelling models. Demand is moving to evaluation of AI output, expert annotation and low resource languages, where people with domain knowledge are needed.",
        faqs=[
            ("Are there data annotation companies in Sri Lanka?", "Yes, mostly established data processing and business process firms that offer annotation alongside other work. It is an emerging capability rather than a large industry."),
            ("Can Sri Lankan teams do LLM evaluation and RLHF?", "Yes, especially where English skills and domain knowledge matter, and for Sinhala and Tamil language data."),
        ],
    ),
    dict(
        slug="insurance-hr-payroll-outsourcing-sri-lanka", label="Insurance, HR and payroll",
        h1="Insurance back office, HR and payroll outsourcing to Sri Lanka",
        title="Insurance back office, HR and payroll outsourcing to Sri Lanka",
        desc="Underwriting support, policy and claims administration, payroll, HR and recruitment process outsourcing from Sri Lanka. Evidence and how to engage.",
        short="Underwriting support, claims, payroll, HR and recruitment.",
        answer="UK insurers and global software groups run back office operations from Colombo. In October 2025 the UK specialist insurer CFC opened a 200 seat global services hub in Colombo with Virtusa, and a company owned by the investors behind IFS hired 370 people in nine months to serve portfolio companies in the Americas and Europe, including business process work. Sri Lankan firms also run payroll, HR and recruitment process outsourcing for Australian and UK employers.",
        stats=[("200", "seats in a UK insurer's Colombo hub (2025)"), ("370", "hires in nine months at IGT 1 Lanka"), ("UK and AU", "main client markets")],
        what=["Underwriting support and policy administration", "Claims intake and processing", "Payroll processing, including Australian awards", "HR administration and onboarding", "Recruitment process outsourcing", "Compliance and reporting support"],
        evidence=[
            ("UK specialist insurer CFC and Virtusa opened a 200 seat global services hub in Colombo in October 2025.", "Daily Mirror", "https://www.dailymirror.lk/business-news/Virtusa-partners-to-unveil-200-seat-digital-service-hub-in-Sri-Lanka/273-323084"),
            ("IGT 1 Lanka, owned by investors including EQT and Hg, hired 370 people in nine months for IT, cloud and business process work for portfolio companies.", "The Morning", "https://www.themorning.lk/articles/DVbn77E2JVlO4Il2tkMb"),
            ("Sri Lankan providers run recruitment process outsourcing, employer of record and virtual staffing with more than 300 staff.", "EDB directory", "https://www.srilankabusiness.com/exporters-directory/company-profiles/sourceone-bpo-private-limited/"),
            ("The Export Development Board lists insurance, banking and HR services among Sri Lanka's business process services.", "EDB", EDB_BPM),
        ],
        ai="Claims intake, data entry for policy administration and payroll calculation are highly automatable. The human value is underwriting support, complex claims, compliance, multi-country payroll rules and candidate experience in recruitment.",
        faqs=[
            ("Do insurers outsource to Sri Lanka?", "Yes. UK specialist insurer CFC opened a 200 seat hub in Colombo in 2025, and UK insurers have used Sri Lankan back offices for claims and administration since the 2000s."),
            ("Can Sri Lankan teams run Australian payroll?", "Yes. Providers serving Australian employers handle payroll including award interpretation. Check experience with your payroll system."),
        ],
    ),
]


def _ev(items):
    return '<ul class="ticks">' + "".join(f"<li>{e(t)} {a(src, url)}</li>" for t, src, url in items) + "</ul>"


def _markets():
    return '<div class="tbl"><table><thead><tr><th>Your market</th><th>Time difference</th><th>How it works</th></tr></thead><tbody>' + "".join(
        f"<tr><td><strong>{e(m)}</strong></td><td>{e(t)}</td><td>{e(h)}</td></tr>" for m, t, h in MARKETS) + "</tbody></table></div>"


def _cta(B, prefix, slug=""):
    q = f"?route=offshoring-{slug}" if slug else "?route=offshoring"
    return f"""<div class="reach mt"><h2>Tell us what you want to offshore</h2><p>Describe the work, volumes and hours. We will tell you honestly whether Sri Lanka fits and introduce providers or people who do it today.</p>
  <div class="actions"><a class="btn" href="{prefix}talent/find/{q}">Tell us what you need</a><a class="btn btn-ghost" href="{B.BOOKING_URL}" rel="noopener">Schedule a call</a><a class="btn btn-ghost" href="mailto:{B.EMAIL}">Email us</a></div></div>"""


ART = {'accounting-bookkeeping-outsourcing-sri-lanka': 'o-accounting', 'investment-research-kpo-sri-lanka': 'o-research', 'virtual-assistants-sri-lanka': 'o-va', 'digital-marketing-outsourcing-sri-lanka': 'o-marketing', 'customer-support-outsourcing-sri-lanka': 'o-support', 'medical-billing-outsourcing-sri-lanka': 'o-medical', 'legal-process-outsourcing-sri-lanka': 'o-legal', 'engineering-design-bim-outsourcing-sri-lanka': 'o-bim', 'data-annotation-sri-lanka': 'o-annotation', 'insurance-hr-payroll-outsourcing-sri-lanka': 'o-insurance'}


def _cards(prefix_to_section, prefix_to_root):
    return '<div class="tile-grid five">' + "".join(
        f'<a class="tile" href="{prefix_to_section}{c["slug"]}/"><img src="{prefix_to_root}assets/art/{ART[c["slug"]]}.svg" alt="{e(c["label"])} outsourcing in Sri Lanka, illustration" loading="lazy" width="1200" height="900">'
        f'<span class="tile-body"><strong>{e(c["label"])}</strong><span>{e(c["short"])}</span></span></a>' for c in CAPS) + "</div>"


def home_section(B):
    """Homepage band introducing business services offshoring."""
    return f"""<section class="section biz">
  <div class="wrap">
    <div class="biz-head">
      <div>
        <p class="eyebrow">Beyond software</p>
        <h2>Offshore business teams in Sri Lanka</h2>
        <p class="biz-lede">Global banks, insurers and research firms have run operations in Colombo for more than 20 years. Companies in the UK, Australia, the US and the Gulf now offshore accounting, research, medical billing, support, legal and design work here too.</p>
        <div class="actions"><a class="btn btn-saffron" href="offshoring/">See all services</a><a class="btn btn-ondark" href="talent/find/?route=offshoring">Tell us what you need</a></div>
      </div>
      <ul class="biz-stats">
        <li><strong>$1.64B</strong><span>IT and business process exports in 2025</span></li>
        <li><strong>9,000+</strong><span>Chartered Accountants, plus 40,000 students</span></li>
        <li><strong>1.5 hrs</strong><span>from Dubai, a shared afternoon with Sydney</span></li>
      </ul>
    </div>
    {_cards("offshoring/", "")}
  </div>
</section>"""


HUB_FAQS = [
    ("Is Sri Lanka good for outsourcing?", "For finance and accounting, investment research, healthcare revenue cycle, banking and insurance operations and software, yes. It exported USD 1.64 billion of IT and business process services in 2025 according to official data, and global firms including HSBC, LSEG and WNS have run operations in Colombo for more than 20 years. It is smaller than the largest outsourcing destinations, so it suits specialist teams better than very large, low cost voice operations."),
    ("What are the main BPO services in Sri Lanka?", "Finance and accounting, investment research and analytics, banking and insurance operations, healthcare revenue cycle management, customer operations, legal process outsourcing, engineering design and quantity surveying, digital marketing and virtual assistance."),
    ("How big is Sri Lanka's BPO industry?", "Official Export Development Board data puts combined IT and business process exports at USD 1.64 billion in 2025, up 8.8%. The industry body SLASSCOM estimates the real figure is closer to USD 2 billion because some revenue is invoiced offshore, and counts about 175,000 people across more than 680 IT and BPM companies."),
    ("What time zone is Sri Lanka in for outsourcing?", "UTC+5:30 all year with no daylight saving. That is 1.5 hours ahead of the UAE, 4.5 to 5.5 hours ahead of the UK and 4.5 to 5.5 hours behind Sydney, so teams share most of the working day with the Gulf and part of it with the UK and Australia."),
    ("Sri Lanka or the Philippines for outsourcing?", "The Philippines is far larger and leads on general English rankings and high volume voice support. Sri Lanka is smaller and stronger in qualified finance and accounting, investment research, banking and insurance operations and software. Many companies use the Philippines for volume support and Sri Lanka for finance and specialist work."),
    ("How do I start outsourcing to Sri Lanka?", "Pick one well documented process, choose a provider or hire a dedicated team through a staffing provider or employer of record, start with a small pilot and expand once quality is proven. Tell us what you need and we will introduce options."),
]


def build(B, stories):
    paths = []
    for c in CAPS:
        prefix = "../../"
        path = f"offshoring/{c['slug']}/"
        c["_art"] = ART[c["slug"]]
        faq, faq_ld = SP.faq_block(stories, c["faqs"] + X.EXTRA[c["slug"]]["faqs"])
        others = SP.chip_links([(x["label"], f"../{x['slug']}/") for x in CAPS if x is not c])
        body = f"""
<section class="page-head"><div class="wrap narrow">
  {SP.crumb_html([("Offshoring", "../")])}
  <h1>{e(c['h1'])}</h1>
  <p class="answer">{e(c['answer'])}</p>
  <p class="reviewed">Last reviewed {REVIEWED}. Sources are linked next to each fact.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  <img class="story-cover art" src="{prefix}assets/art/{ART[c['slug']]}.svg" alt="{e(c['h1'])}, illustration" width="1200" height="900">
  {SP.stats_strip(c['stats'])}
  <h2 class="h-sub mt">{e(c['label'])} outsourcing in Sri Lanka at a glance</h2>
  {X.glance_html(c)}
  <h2 class="h-sub mt">What Sri Lankan teams do</h2>
  <ul class="ticks">{''.join(f'<li>{e(w)}</li>' for w in c['what'])}</ul>
  <h2 class="h-sub mt">The evidence</h2>
  {_ev(c['evidence'])}
  <h2 class="h-sub mt">How it fits your time zone</h2>
  {_markets()}
  <h2 class="h-sub mt">AI: what is being automated, and what is not</h2>
  <p class="body-l">{e(c['ai'])}</p>
  {X.depth_html(c, prefix)}
  <h2 class="h-sub mt">Ways to set it up</h2>
  <ul class="ticks">
    <li><strong>A managed provider</strong> runs the process for you under a service agreement. Fastest to start.</li>
    <li><strong>A dedicated team</strong> works only for you, employed by a staffing provider or an <a href="{prefix}guides/employer-of-record-sri-lanka/">employer of record</a>.</li>
    <li><strong>Contractors</strong> for specialist or part time work. See <a href="{prefix}guides/pay-employees-and-contractors-in-sri-lanka/">how to pay people in Sri Lanka</a>.</li>
    <li><strong>Your own centre</strong> once you pass a few dozen people. See the <a href="{prefix}guides/set-up-a-company-in-sri-lanka/">setup guide</a>.</li>
  </ul>
  {_cta(B, prefix, c['slug'])}
  {faq}
  <h2 class="h-sub mt">Other services from Sri Lanka</h2>
  {others}
  <p class="body-l mt">See also: <a href="../">Outsourcing to Sri Lanka overview</a> · <a href="../bpo-companies-sri-lanka/">BPO companies in Sri Lanka</a> · <a href="{prefix}compare/philippines/">Sri Lanka vs the Philippines</a> · <a href="{prefix}guides/how-to-hire-in-sri-lanka/">How to hire in Sri Lanka</a></p>
  <p class="body-l">By market: <a href="../from-uk/">from the UK</a> · <a href="../from-australia/">from Australia</a> · <a href="../from-usa/">from the USA</a> · <a href="../from-uae/">from the UAE</a></p>
</div></section>
"""
        head = faq_ld + X.schema(B, c, path) + SP.crumbs_ld(B, [("Offshoring", "offshoring/"), (c["label"], path)])
        B.write(path + "index.html", B.page(c["h1"], c["desc"], body, prefix, path, extra_head=head, active="services", seo_title=c["title"]))
        paths.append(path)

    prefix = "../"
    faq, faq_ld = SP.faq_block(stories, HUB_FAQS)
    rows = "".join(f'<tr><td><a href="{c["slug"]}/"><strong>{e(c["label"])}</strong></a></td><td>{e(c["short"])}</td><td>{e(c["stats"][0][0])} {e(c["stats"][0][1])}</td></tr>' for c in CAPS)
    body = f"""
<section class="page-head"><div class="wrap narrow">
  <h1>Outsourcing to Sri Lanka: business services beyond tech</h1>
  <p class="answer">Sri Lanka is best known for software, but its business process industry is just as established. Global banks, exchanges and insurers have run operations in Colombo for more than 20 years, and companies in the UK, Australia, the US and the Gulf outsource accounting, investment research, healthcare billing, customer operations, legal support, engineering design, marketing and virtual assistance there. Official data puts combined IT and business process exports at USD 1.64 billion in 2025, and the industry estimates about 175,000 people work in more than 680 IT and BPM companies.</p>
  <p class="reviewed">Last reviewed {REVIEWED}. General information with sources linked; not a ranking of providers.</p>
</div></section>
<section class="section top-0"><div class="wrap narrow">
  {SP.stats_strip([("$1.64B", "IT and BPM exports in 2025 (official)"), ("175,000", "people in IT and BPM (SLASSCOM)"), ("9,000+", "Chartered Accountants, plus 40,000 students")])}
  <p class="body-l">The official export figure is from the Export Development Board ({a("Daily FT", EDB_EXPORTS)}). SLASSCOM estimates the real total is closer to USD 2 billion because some revenue is invoiced through overseas entities ({a("EconomyNext", SLASSCOM_2B)}). Workforce and company counts: {a("SLASSCOM via Daily FT", SLASSCOM_WF)}. Accountants: {a("Daily Mirror", CASL)}.</p>
  <h2 class="h-sub mt">What you can outsource to Sri Lanka</h2>
  <div class="tbl"><table><thead><tr><th>Service</th><th>What teams do</th><th>One fact</th></tr></thead><tbody>{rows}</tbody></table></div>
</div>
<div class="wrap"><h2 class="h-sub mt">Explore by service</h2>{_cards("", prefix)}</div>
<div class="wrap narrow">
  <h2 class="h-sub mt">Why companies choose Sri Lanka for business services</h2>
  <ul class="ticks">
    <li><strong>Qualified people, not just labour.</strong> More than 9,000 Chartered Accountants and 40,000 students, around 15,000 CIMA students and members, and English medium professional training.</li>
    <li><strong>A long record with demanding clients.</strong> HSBC ({a("since 2004", HSBC)}), the London Stock Exchange Group ({a("1,600+ people", LSEG)}) and investment research teams serving more than 50 global financial institutions.</li>
    <li><strong>Time zones that work for the Gulf, UK and Australia.</strong> 1.5 hours from Dubai, a shared afternoon with Sydney and an overlap with the UK day.</li>
    <li><strong>Open to foreign companies.</strong> Business services companies can be fully foreign owned. See the <a href="{prefix}guides/set-up-a-company-in-sri-lanka/">setup guide</a>.</li>
  </ul>
  <h2 class="h-sub mt">Where it fits less well</h2>
  <ul class="ticks">
    <li>Very large voice operations of thousands of seats. The Philippines is far bigger for that. See <a href="{prefix}compare/philippines/">Sri Lanka vs the Philippines</a>.</li>
    <li>Pure data entry. It is being automated, and a 2025 study names clerical work as the most AI-exposed job group in Sri Lanka ({a("Institute of Policy Studies", IPS_AI)}). Outsource judgement work, not keystrokes.</li>
    <li>Live US daytime coverage, which needs night shifts.</li>
  </ul>
  <h2 class="h-sub mt">By buyer market</h2>
  {_markets()}
  <div class="doors wrap3 mt">
    <a class="door has-art" href="from-uk/"><img class="door-art" src="../assets/art/g-countries.svg" alt="" loading="lazy" width="1200" height="900"><h3>From the UK</h3><p>Accounting, insurance, legal and BIM teams that cover the UK day.</p><span class="door-go">UK guide</span></a>
    <a class="door has-art" href="from-australia/"><img class="door-art" src="../assets/art/g-why.svg" alt="" loading="lazy" width="1200" height="900"><h3>From Australia</h3><p>Offshore accountants, assistants and marketers with a shared afternoon.</p><span class="door-go">Australia guide</span></a>
    <a class="door has-art" href="from-usa/"><img class="door-art" src="../assets/art/o-medical.svg" alt="" loading="lazy" width="1200" height="900"><h3>From the USA</h3><p>Medical billing, research and back office with overnight turnaround.</p><span class="door-go">USA guide</span></a>
    <a class="door has-art" href="from-uae/"><img class="door-art" src="../assets/art/g-offshoring.svg" alt="" loading="lazy" width="1200" height="900"><h3>From the UAE</h3><p>Teams 1.5 hours away that share almost the whole working day.</p><span class="door-go">UAE guide</span></a>
    <a class="door has-art" href="bpo-companies-sri-lanka/"><img class="door-art" src="../assets/art/o-support.svg" alt="" loading="lazy" width="1200" height="900"><h3>BPO companies in Sri Lanka</h3><p>Who delivers which service from Sri Lanka, with sources.</p><span class="door-go">See the directory</span></a>
  </div>
  {_cta(B, prefix)}
  {faq}
  <p class="body-l mt">Looking for software teams instead? See <a href="{prefix}solutions/software-outsourcing-sri-lanka/">software outsourcing</a>, <a href="{prefix}solutions/dedicated-development-team-sri-lanka/">dedicated teams</a> and <a href="{prefix}why-sri-lanka/finance-accounting/">finance and shared services</a>.</p>
</div></section>
"""
    art = SP.ld({"@context": "https://schema.org", "@type": "Article", "headline": "Outsourcing to Sri Lanka: business services beyond tech", "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                 "author": {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"}, "publisher": {"@type": "Organization", "name": B.SITE_NAME, "url": B.SITE_URL + "/"},
                 "mainEntityOfPage": f"{B.SITE_URL}/offshoring/", "image": f"{B.SITE_URL}/assets/art/g-offshoring.svg", "about": ["Business process outsourcing", "Sri Lanka"]})
    head = faq_ld + art + SP.crumbs_ld(B, [("Offshoring", "offshoring/")])
    B.write("offshoring/index.html", B.page("Outsourcing to Sri Lanka: business services beyond tech",
                                            "Outsourcing companies and BPO services in Sri Lanka: accounting, investment research, medical billing, customer support, legal, BIM, marketing and virtual assistants. Evidence and sources.",
                                            body, prefix, "offshoring/", extra_head=head, active="services",
                                            seo_title="Outsourcing to Sri Lanka: BPO companies and services (2026)"))
    paths += X.build_markets(B, stories, CAPS, _cta, _markets()) + X.build_directory(B, stories, _cta)
    return paths + ["offshoring/"]
