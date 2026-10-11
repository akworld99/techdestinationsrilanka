"""Capability-first copy for the industry, country, solution and role pages.

These pages show what gets built in Sri Lanka. They do not promote the service companies we have featured:
no logos, no links and no vendor names. Global companies that run their own centres here are named as evidence."""

RATE = ("USD 25 to 40", "an hour, typical partner rates per the Export Development Board")
GRADS = ("12,000+", "technology graduates a year")
EXPORTS = ("$1.645B", "IT and BPM exports in 2025")
EU_OVERLAP = ("4.5 to 5.5", "shared working hours a day")

# How a featured service company is described when older copy still refers to it.
ANON = {
    "creative-software": "a Colombo engineering firm with Scandinavian clients", "tiqri": "a Norwegian owned software company in Colombo",
    "gapstars": "a Dutch founded engineering company in Colombo", "xeynergy": "a Sri Lankan software engineering firm",
    "rootcode": "a Colombo AI and product engineering company", "inivos": "a Sri Lankan engineering company",
    "dijital-team": "a Colombo managed teams provider", "oceans": "a talent company that places Sri Lankan professionals",
    "infomate": "a Sri Lankan finance outsourcing firm", "frontwalker": "a Stockholm listed software group",
    "roar-global": "a Colombo AI and media company", "simcentric": "a Colombo simulation software company",
    "surge-global": "a Sri Lankan technology services company", "codegen": "a Sri Lankan travel technology company",
    "healthrecon-connect": "a healthcare revenue operations company", "superloop": "an ASX listed telecom",
    "igt1-lanka": "a software centre set up by the owners of IFS", "orion-city": "Orion City",
}

COPY = {
    # ---------------- industries
    "healthtech": dict(
        answer="Sri Lankan engineers already work on regulated healthcare systems for Norway, the United States and Australia. A Colombo team has been a long standing engineering partner on Norway's leading electronic health record platform, and HITRUST certified revenue operations for US healthcare providers run from Sri Lanka. Healthtech companies come here for engineers who are used to patient data, audits and long product lifecycles.",
        stats=[("HITRUST", "and SOC 1 audited healthcare operations run from Colombo"), GRADS, RATE],
        proof=["Engineering on Norway's leading electronic health record platform, where a director at the client credits the Colombo team as a significant contributor.",
               "Insurance verification, billing, claims and collections for US, Australian and New Zealand providers under HITRUST and SOC 1 controls.",
               "Software for the scanning and tracking devices used in hospitals worldwide, built at Zebra Technologies' R&D centre in Colombo."]),
    "automotive": dict(
        answer="Sri Lankan engineers already contribute to European vehicle software: embedded systems, electric vehicle software and software defined vehicle platforms, for a supplier whose work reaches brands including Volkswagen, BMW, Audi, Mercedes and DAF. A Sri Lankan team also designed and built an all electric supercar and the country's largest EV charging network. Automotive companies come here for embedded and systems engineers who can work to safety standards.",
        stats=[("2015", "Synopsys opened chip design R&D in Colombo"), EU_OVERLAP, RATE],
        proof=["Embedded systems, electric vehicle software and software defined vehicle platforms for European vehicle programmes.",
               "An all electric supercar and a national EV charging network, designed and built locally.",
               "Emulation and prototyping tools that chip designers use to verify automotive silicon, developed at Synopsys in Colombo.",
               "IT services for Michelin's operations across Asia."]),
    "fintech": dict(
        answer="Some of the most demanding financial software in the world was built by Sri Lankan engineers. The London Stock Exchange chose a trading platform built in Colombo and then bought the company behind it. JPMorganChase acquired a wealth infrastructure platform founded by two Sri Lankans in 2026. Engineers in Colombo serve four of the top five US banks. Fintech companies come here for engineers who understand low latency, regulation and scale.",
        stats=[("2008", "the London Stock Exchange chose a trading platform built in Colombo"), ("2026", "JPMorganChase acquired a Sri Lankan founded wealth platform"), ("4 of 5", "top US banks served by engineers in Colombo")],
        proof=["The trading platform the London Stock Exchange selected in 2008, which now runs exchanges on several continents.",
               "Cloud native infrastructure for the UK pension and wealth market, acquired by JPMorganChase.",
               "Digital engineering for four of the top five US banks.",
               "Accounting operations for 150+ international clients, run by qualified finance teams."]),
    "ai": dict(
        answer="Sri Lankan teams now build AI products as well as services. Colombo companies ship their own AI developer tools and agentic software engineering platforms, and one is helping build national AI infrastructure for the Estonian government. AI companies come here for engineers who already build with frontier models in production.",
        stats=[("Estonia", "national AI platforms are built with a Colombo team"), GRADS, ("#3 in Asia", "for affordable tech talent, Startup Genome 2026")],
        proof=["The next generation of Estonia's government citizen assistant, and an AI crop health platform for the City of Porto.",
               "Agentic software engineering tools and AI products built and sold by Sri Lankan companies.",
               "Generative AI work for a global enterprise software portfolio.",
               "Data, analytics and machine learning for pricing and supply chain at Sysco."]),
    "enterprise-software": dict(
        answer="Enterprise software is the deepest part of Sri Lanka's tech industry. IFS does about 60% of its global product development in Colombo. WSO2, an API and identity software company founded and headquartered here, sold for $600 million in 2024. Sysco builds the core systems of the world's largest foodservice distributor here, on the same codebase as its US teams. Software companies come here for product engineers who have maintained large systems for years.",
        stats=[("60%", "of IFS product development is done in Colombo"), ("$600M", "paid by EQT for WSO2 in 2024"), ("2,200+", "IFS people in Colombo")],
        proof=["About 60% of IFS global product development, done by 2,200+ people in Colombo.",
               "API management, integration and identity software used by 700+ enterprises in 70+ countries, built and led from Colombo at WSO2.",
               "Sysco's core systems, on the same codebase, sprint cycles and engineering standards as its teams in Texas.",
               "Dedicated product teams for Scandinavian software companies, some of them running for more than 20 years."]),
    "semiconductors-embedded": dict(
        answer="Chip design and device software are engineered in Sri Lanka today. Synopsys, the global leader in electronic design automation, has run R&D in Colombo since 2015, working on logic synthesis, FPGA prototyping and emulation. Zebra Technologies builds software for its scanners and mobile computers at its Colombo R&D centre. Semiconductor and embedded companies come here for engineers trained in a university curriculum that Synopsys helped design.",
        stats=[("2015", "Synopsys R&D opened in Colombo"), ("3", "universities built a VLSI curriculum with Synopsys"), GRADS],
        proof=["Core product work at Synopsys on RTL compilation, logic synthesis, HAPS prototyping and the ZeBu emulation platform.",
               "A wholly owned Zebra Technologies software R&D centre building for its global device platforms across mobile, cloud and IoT.",
               "Embedded systems and vehicle software for European automotive programmes.",
               "High fidelity simulation software on Unreal Engine, engineered in Colombo under ISO 27001."]),
    "logistics-travel": dict(
        answer="Sri Lankan engineers build software that moves goods and people at scale. A reservations platform built in Colombo serves airlines, tour operators and cruise lines in 20+ countries. A Colombo team has spent more than ten years on automated warehouse storage and retrieval systems with a Norwegian client. Sysco's sourcing, warehouse, pricing and last mile systems are engineered here. Logistics and travel companies come here for engineers who know high volume transactional systems.",
        stats=[("20+", "countries served by a travel platform built in Colombo"), ("10+ years", "of automated warehousing work with a Norwegian client"), RATE],
        proof=["A reservations platform used by airlines, tour operators, cruise lines and online travel agencies in 20+ countries.",
               "Automated storage and retrieval systems, built by a dedicated Colombo team working with a Norwegian one.",
               "Sourcing, merchandising, warehouse, pricing and last mile delivery software for Sysco.",
               "Software behind Zebra's barcode, RFID and real time location systems used in warehouses worldwide."]),
    "govtech": dict(
        answer="Governments already rely on Sri Lankan engineering. A Colombo company works on national AI infrastructure for Estonia, one of the world's most digital governments. A Stockholm listed public sector software group calls Colombo its global tech center. A Sri Lankan firm won a technology transformation contract with the government of Qatar. Govtech companies come here for teams that have passed public sector security and procurement scrutiny.",
        stats=[("Estonia", "national AI platforms are built with a Colombo team"), ("Qatar", "government technology contract won in 2024"), ("UK", "Ministry of Defence chose simulation software engineered in Colombo")],
        proof=["Platforms for the Estonian government, including the next generation of its citizen assistant.",
               "Public sector software for a Stockholm listed group, delivered by 100+ engineers in Colombo.",
               "A technology transformation contract with the government of Qatar.",
               "Training simulation software selected for a UK Ministry of Defence contract in 2026.",
               "Engineering on the health record platform used across Norway's public healthcare system."]),
    "finance-accounting": dict(
        answer="Sri Lanka has one of the largest pools of globally certified accountants outside the UK, and global firms have built on it for two decades. WNS, now part of Capgemini, has delivered from Colombo since 2004. EY chose Sri Lanka as one of nine countries for its global delivery network. Sri Lankan firms run finance operations for clients in 10+ countries. Companies come here for qualified finance professionals who work on SAP, Oracle, NetSuite and Microsoft Dynamics every day.",
        stats=[("2004", "WNS began delivering from Colombo"), ("9", "countries in EY's global delivery network, including Sri Lanka"), ("15%", "statutory employer contributions on top of salary")],
        proof=["Finance and accounting outsourcing for Fortune 500 and blue chip clients, recognised in Everest Group's 2025 PEAK Matrix.",
               "Finance, legal, HR and process automation services delivered by 800+ people at WNS.",
               "Consulting, technology and audit support for EY member firms worldwide, from 500+ staff.",
               "Revenue cycle operations for US healthcare, pairing automation with certified professionals.",
               "A Michelin shared service centre handling procurement and core support functions."]),
    # ---------------- countries
    "usa": dict(
        answer="US companies have built core engineering in Sri Lanka for more than 20 years. Sysco builds its core software in Colombo on the same codebase as its Texas teams. Synopsys and Zebra Technologies run product R&D here. Virtusa, cofounded by a Sri Lankan in Boston, has 3,000+ engineers in Colombo. US startups add Sri Lankan operators and specialists to their teams through talent partners.",
        stats=[("20+ years", "US companies have built engineering in Sri Lanka"), ("#54", "Sysco's Fortune 500 rank"), ("3,000+", "Virtusa engineers in Colombo")],
        proof=["Sysco's innovation and engineering arm, working with teams in Austin and Houston.", "Chip design software R&D for Synopsys.", "A software R&D centre for Zebra Technologies.",
               "Digital engineering for 20+ Fortune 50 companies and four of the top five US banks.", "HITRUST certified revenue operations for hundreds of US healthcare providers.",
               "Operations, marketing and finance specialists working inside US startups."]),
    "uk": dict(
        answer="British institutions have trusted Sri Lankan engineering with critical systems. The London Stock Exchange chose a trading platform built in Colombo and bought the company behind it. A wealth platform built for the UK pension market by Sri Lankan founders was acquired by JPMorganChase in 2026. The UK Ministry of Defence selected training simulation software engineered in Colombo. UK travel brands run on reservations technology built here.",
        stats=[("3.5 to 4.5", "shared working hours a day"), ("2008", "the LSE chose a trading platform built in Colombo"), ("2026", "JPMorganChase acquired a Sri Lankan founded UK wealth platform")],
        proof=["The Millennium Exchange trading platform for the London Stock Exchange.", "Infrastructure for UK digital wealth managers and pension providers, now part of JP Morgan Personal Investing.",
               "Training simulation software selected by the UK Ministry of Defence.", "Reservations technology for UK travel brands.", "Finance operations for blue chip UK clients.",
               "Dedicated engineering teams for UK and European companies."]),
    "nordics": dict(
        answer="Nordic companies have the longest record of building software in Sri Lanka. IFS, founded in Sweden, does about 60% of its global product development in Colombo. Colombo teams have served Swedish, Norwegian and Danish clients for 25 years, including work on Norway's largest health records platform. A Stockholm listed software group calls Colombo its global tech center.",
        stats=[("27 years", "IFS has operated in Sri Lanka"), EU_OVERLAP, ("25 years", "of dedicated teams for Scandinavian clients")],
        proof=["About 60% of IFS global product development, with 2,200+ people in Colombo.", "Dedicated teams for Scandinavian clients since 1999.",
               "Client relationships with Norwegian companies that have lasted more than a decade.", "Software for a Stockholm listed group, delivered by 100+ engineers.",
               "Finance operations for a Norwegian accounting firm since 2010.", "Government platforms for Estonia."]),
    "norway": dict(
        answer="Norwegian companies have relied on Sri Lankan teams for well over a decade. A Colombo team is a long standing engineering partner on Norway's leading electronic health record platform. A Norwegian owned software company has delivered from Colombo for 15 years, including more than ten years on automated warehousing. A Norwegian accounting firm has run its finance operations from Sri Lanka since 2010.",
        stats=[("15+ years", "of software delivery to Norway from Colombo"), ("2010", "a Norwegian accounting firm moved finance operations here, and stayed"), EU_OVERLAP],
        proof=["Engineering on Norway's leading digital health platform. A director at the client credits the Colombo team as a significant contributor.",
               "Automated storage and retrieval systems, built with a Norwegian team for more than ten years.",
               "Finance operations for a Norwegian accounting firm that chose its Sri Lankan partner from 20 candidates."]),
    "sweden": dict(
        answer="Sweden's best known enterprise software company does most of its engineering in Sri Lanka. IFS, founded in Sweden, does about 60% of its global product development in Colombo, with 2,200+ people. A Stockholm listed software group calls its Colombo office its global tech center, and Colombo teams have built products for Swedish clients for 25 years.",
        stats=[("60%", "of IFS product development is done in Colombo"), ("2,200+", "IFS people in Colombo"), EU_OVERLAP],
        proof=["IFS is the second largest tech employer in Sri Lanka.", "Software for a Stockholm listed group, delivered by 100+ engineers in Colombo.",
               "Dedicated product teams for Swedish software companies since 1999.", "A new software centre in Port City Colombo launched by EQT, the Stockholm based investor, with Hg and TA Associates."]),
    "netherlands": dict(
        answer="Dutch companies have chosen Sri Lanka after looking at the alternatives. One Dutch founder researched where to build software teams for European companies, picked Sri Lanka in 2015, and now runs a 300+ person engineering company in Colombo. A Dutch technology group with 40+ years in automotive software scaled its engineering capacity through a Colombo partner.",
        stats=[("2015", "a Dutch founder chose Sri Lanka for European engineering teams"), ("40+ years", "of automotive software at a Dutch group now building in Colombo"), EU_OVERLAP],
        proof=["Embedded engineering teams for Dutch scaleups, and for railway safety systems used across the Netherlands.", "Embedded and electric vehicle software for a Dutch automotive technology group.",
               "25 years of dedicated teams for Northern European clients."]),
    "germany": dict(
        answer="German industry already uses software that Sri Lankan engineers help build. Engineers in Colombo contribute to vehicle software for brands including Volkswagen, BMW, Audi and Mercedes through a European automotive supplier. The Synopsys team in Colombo works on verification tools that chip designers use for automotive silicon. Fewer German companies than Nordic or Dutch ones have opened their own teams here so far, which means less competition for the talent.",
        stats=[EU_OVERLAP, ("2015", "Synopsys R&D opened in Colombo"), RATE],
        proof=["Embedded systems, electric vehicle software and software defined vehicle platforms built to strict safety standards.",
               "Emulation and prototyping tools at Synopsys, used to verify chips for automotive, 5G and data center applications.",
               "Dedicated teams for companies in Austria and the Benelux, a model that transfers directly to German scaleups."]),
    "australia": dict(
        answer="Australian companies run live operations from Sri Lanka. An ASX listed telecom runs network engineering, security and 24x7 operations from Colombo and benchmarks salaries to the Australian dollar. One Colombo provider built a 200 person team in two years for Australian and international clients. Simulation software cofounded by an Australian is engineered here.",
        stats=[("3.5 to 4.5", "shared working hours with Sydney"), ("24x7", "network operations for an ASX listed telecom run from Colombo"), ("200", "person team built in two years for Australian clients")],
        proof=["Network engineering, cybersecurity, cloud and 24x7 operations for an Australian national network.", "Dedicated IT teams for Australian companies.",
               "Simulation software from a company cofounded by an Australian and a Sri Lankan.", "Revenue operations for healthcare providers in Australia and New Zealand.", "Finance operations for Australian clients."]),
    "uae-gulf": dict(
        answer="For Gulf companies, Sri Lanka is the closest deep engineering market. Colombo is 1.5 hours ahead of the UAE and Oman and a direct flight away. A Sri Lankan firm won a technology transformation contract with the government of Qatar. Colombo engineering companies serve UAE clients, some through hubs in Dubai.",
        stats=[("1.5 hours", "ahead of the UAE and Oman"), ("6.5 to 7.5", "shared working hours a day"), ("Qatar", "government technology contract won by a Sri Lankan firm in 2024")],
        proof=["Technology transformation for the government of Qatar.", "Engineering for UAE clients, with a hub in Dubai and delivery from Colombo.", "Software delivery for clients across the Middle East.", "Reservations technology for Gulf travel companies."]),
    # ---------------- ways to build
    "software-outsourcing-sri-lanka": dict(
        proof=["Dedicated product teams for Scandinavian software companies, running for 25 years.", "Digital engineering for Fortune 500 clients by 3,000+ engineers at Virtusa.",
               "Full lifecycle delivery for US clients.", "Product engineering and AI for European governments.", "Software, data and security work for the government of Qatar.",
               "Enterprise and automotive software for European programmes."]),
    "dedicated-development-team-sri-lanka": dict(
        answer="A dedicated development team is a group of engineers employed and managed by a Sri Lankan company who work only on your product, as an extension of your own team. It is the most common way foreign companies start in Sri Lanka. Some of these teams have run for 25 years for Scandinavian clients, and relationships of more than a decade are common.",
        stats=[("25 years", "the longest running dedicated teams, for Scandinavian clients"), ("10+ years", "client relationships are common"), RATE],
        proof=["A Colombo team that DIPS of Norway credits as a significant contributor to its health record platform.", "One long term team per client instead of a rotating pool.",
               "Teams that embed in the client's company and regularly travel to its headquarters.", "Dedicated IT teams for clients in Australia, the US, Europe and the UK."]),
    "staff-augmentation-sri-lanka": dict(
        answer="Staff augmentation means adding individual Sri Lankan professionals to your existing team, managed by you, without setting up a local company. You can do it through an employer of record, by contracting people directly, or through a talent partner. Hundreds of US startups and agencies already work with Sri Lankan professionals this way.",
        stats=[("3", "routes: employer of record, contractors or a talent partner"), ("15%", "statutory employer contributions on top of salary"), ("7 to 14", "working days to register a company if you outgrow it")],
        proof=["Executive assistants, marketing, finance and operations specialists working inside US startups.", "Engineers embedded directly into European scaleups.",
               "Engineering, QA, DevOps and product people working inside US client teams."]),
    "offshore-development-center-sri-lanka": dict(
        proof=["IFS, HCLTech, EY, Sysco and HSBC all run scaled operations in Sri Lanka.", "Sysco: the engineering arm of the world's largest foodservice distributor.", "Synopsys: chip design software R&D since 2015.",
               "Zebra Technologies: a wholly owned software R&D subsidiary.", "EY: one of nine countries in its global delivery network.", "Michelin: IT services for Asia and a shared service centre.",
               "An ASX listed telecom: 24x7 network operations."]),
    "sri-lanka-for-startups": dict(
        answer="Startups use Sri Lanka to build a senior engineering team at a fraction of home market cost without lowering the bar. One wealth platform built with 50+ engineers in Sri Lanka was acquired by JPMorganChase less than three years after its first client. Hundreds of US startups already work with Sri Lankan operators and specialists, and Dutch scaleups run embedded engineering teams here.",
        stats=[("< 3 years", "from first client to a JPMorganChase acquisition for one Sri Lankan founded startup"), ("#3 in Asia", "for affordable tech talent, Startup Genome 2026"), ("15%", "tax on exported services")],
        proof=["A wealth platform founded by two Sri Lankans in 2019 and acquired by JPMorganChase in 2026.", "Operators and specialists working inside hundreds of US startups.",
               "Embedded engineering teams for European scaleups.", "A Colombo startup that now builds for European governments."]),
    # ---------------- roles
    "software-engineers": dict(proof=["Full stack engineering on the same codebase as Sysco's US teams.", "API, integration and identity products at WSO2, built by 780 engineers.",
                                      "Digital engineering for Fortune 500 clients at Virtusa, with 3,000+ engineers in Colombo.", "Dedicated product teams for Scandinavian software companies.", "Embedded teams inside European scaleups."]),
    "qa-engineers": dict(proof=["QA and test automation within full lifecycle delivery for US clients.", "QA inside dedicated long term product teams.", "Quality engineering as a core discipline at Sysco."]),
    "devops-engineers": dict(proof=["Cloud, infrastructure and 24x7 network operations for an Australian carrier.", "Cloud infrastructure for Sysco, a Fortune 500 distributor.", "DevOps and support across the technology lifecycle for US clients."]),
    "data-ai-engineers": dict(proof=["AI platforms for the Estonian government.", "Agentic AI products built and sold by Sri Lankan companies.", "Data, analytics and machine learning for pricing and supply chain at Sysco."]),
    "erp-consultants": dict(proof=["About 60% of IFS global product development is done in Colombo.", "IFS consulting alongside product engineering, by people who came up through IFS.", "Finance teams working daily on SAP, Oracle, NetSuite and Dynamics."]),
    "cybersecurity-engineers": dict(proof=["Cybersecurity for a national telecom network in Australia.", "Security and engineering teams deployed on government projects abroad.", "Operations run under HITRUST and SOC 1 controls."]),
    "designers-product-managers": dict(proof=["Dedicated design studios inside Colombo engineering companies.", "Product management within delivery for US clients.", "UI and UX as a core engineering discipline at Sysco."]),
    "accountants": dict(proof=["Finance operations for 150+ clients in 10+ countries.", "Finance and accounting services at WNS, from Colombo since 2004.", "Support for EY member firms worldwide, from 500+ staff.", "Revenue cycle work for US healthcare."]),
}


def apply(items):
    for x in items:
        x["cites"] = [p[0] for p in x.get("proof", []) if isinstance(p, tuple)]
        x.update(COPY.get(x["slug"], {}))


# Sentence level rewrites for older section, FAQ and description copy that named featured service companies.
REWRITE = {
    "Creative Software's Scandinavian clients flew to Colombo for its 25th anniversary.": "Some Colombo teams have worked with the same Scandinavian health and software clients for 25 years.",
    "Yes. HealthRecon Connect handles US patient and claims data under HITRUST certification and SOC 1 audits, and Creative Software's Colombo team contributes to Norway's leading electronic health record platform.": "Yes. US patient and claims data is handled in Colombo under HITRUST certification and SOC 1 audits, and a Colombo team contributes to Norway's leading electronic health record platform.",
    "Published examples include DIPS of Norway through Creative Software, HealthRecon Connect serving US and ANZ providers, and Zebra Technologies, whose devices are used in hospitals.": "Published examples include DIPS of Norway, US and ANZ healthcare providers, and Zebra Technologies, whose devices are used in hospitals.",
    "Inivos was founded in 2019 by engineers who came up through IFS. Within a few years its team was contributing to safety critical automotive work. That shift shows": "One Colombo engineering company was founded in 2019 by enterprise software engineers. Within a few years its team was contributing to safety critical automotive work. That shift shows",
    "CodeGen's Vega and ChargeNET show that": "A locally designed electric supercar and a national charging network show that",
    "Yes. Inivos engineers contribute to": "Yes. Engineers in Colombo contribute to",
    "Yes. CodeGen built the Vega electric supercar and the ChargeNET charging network in Sri Lanka.": "Yes. An all electric supercar and the country's largest EV charging network were designed and built in Sri Lanka.",
    "Yes. Infomate and WNS run finance": "Yes. WNS and Sri Lankan outsourcing firms run finance",
    "Xeynergy restructured how its engineers work alongside AI in 2025 and then started building its own AI products. That pattern is spreading.": "Engineering firms here restructured how their engineers work alongside AI in 2025, and some then started building their own AI products.",
    "Roar AI runs on infrastructure hosted in Sri Lanka and bills in rupees.": "AI model hosting is now available on infrastructure in Sri Lanka, billed in rupees.",
    "Yes. Roar Global runs an AI gateway with 200+ models, Xeynergy builds Accxis360 and BetterCode AI, and Rootcode builds AI platforms for European governments.": "Yes. Sri Lankan companies sell their own AI developer tools and products, and one builds AI platforms for European governments.",
    "Rootcode ranked first in Asia Pacific at the 2025 APICTA Awards, and": "A Sri Lankan company ranked first in Asia Pacific at the 2025 APICTA Awards, and",
    "launched IGT1 Lanka in 2025 to serve": "launched a second company in Colombo in 2025 to serve",
    "IFS, WSO2, Sysco LABS, Virtusa and IGT1 Lanka all run": "IFS, WSO2, Sysco and Virtusa all run",
    "and firms such as Creative Software and Inivos employ engineers and consultants who came through that ecosystem.": "and a number of Sri Lankan firms employ engineers and consultants who came through that ecosystem.",
    "Yes. Zebra Technologies, Inivos and SimCentric all employ embedded, device or simulation engineers in Colombo.": "Yes. Zebra Technologies and several Sri Lankan companies employ embedded, device or simulation engineers in Colombo.",
    "CodeGen's travelbox platform, used by 250+ travel businesses including airlines and tour operators, is engineered in Colombo.": "A reservations platform used by airlines, tour operators and cruise lines in 20+ countries is engineered in Colombo.",
    "Yes. Tiqri's Colombo team has worked": "Yes. A Colombo team has worked",
    "Rootcode and SimCentric hold ISO 27001. Frontwalker is governed by the disclosure rules of a public listing in Stockholm.": "Sri Lankan companies doing this work hold ISO 27001, and some sit inside groups governed by the disclosure rules of a European stock exchange listing.",
    "platforms for the Estonian government by Rootcode, a Qatar government transformation contract won by Surge Global, and Norway's public health record platform, which Creative Software helps build.": "platforms for the Estonian government, a Qatar government transformation contract, and Norway's public health record platform.",
    "Several are. Rootcode holds ISO 9001 and ISO 27001, and SimCentric holds ISO 27001.": "Several are. Companies doing public sector work from Colombo hold ISO 9001 and ISO 27001.",
    "Infomate, WNS and EY run finance": "WNS, EY and Sri Lankan firms run finance",
    "HealthRecon Connect's HRC Labs handles volume with machine learning,": "In healthcare revenue operations, for example, machine learning handles the volume,",
    "Infomate built Sri Lanka's first rural BPO centres in Jaffna, Mahawilachchiya and Seenigama, and HealthRecon Connect opened a delivery centre in Kandy.": "Finance and BPO centres operate in Jaffna, Kandy and rural towns as well as Colombo.",
    "and firms such as Infomate have run international finance operations here since 2005.": "and international finance operations have run here since 2004.",
    "Michelin, HSBC and Infomate all run": "Michelin and HSBC all run",
    "or use a company such as Oceans.": "or use a talent partner.",
    "JP Morgan Personal Investing through WealthOS, and the UK Ministry of Defence through SimCentric are published examples.": "JP Morgan Personal Investing and the UK Ministry of Defence are published examples.",
    "IFS, Creative Software, Tiqri and Frontwalker have built Nordic software in Sri Lanka for up to 27 years.": "Nordic companies, led by IFS, have built software in Sri Lanka for up to 27 years.",
    "IFS has done it for 27 years, Creative Software for 25 and Tiqri for 15.": "IFS has done it for 27 years, and other Nordic clients for 15 to 25.",
    "IFS and Frontwalker from Sweden, and Tiqri and DIPS (through Creative Software) from Norway, are published examples.": "IFS from Sweden and DIPS from Norway are published examples.",
    "DIPS, Tiqri and a Norwegian accounting firm have built": "DIPS, a Norwegian software group and a Norwegian accounting firm have built",
    "DIPS AS works with Creative Software on its health record platform, and Tiqri, a Norwegian parented company, runs its core engineering in Colombo.": "DIPS AS works with a Colombo team on its health record platform, and a Norwegian parented software company runs its core engineering in Colombo.",
    "They already do. Creative Software's engineers contribute": "They already do. Engineers in Colombo contribute",
    "and Frontwalker calls Colombo its global tech center.": "and a Stockholm listed software group calls Colombo its global tech center.",
    "IFS and Frontwalker both run large engineering operations in Colombo. EQT, the Swedish investment firm, owns WSO2 and co owns IFS and IGT1 Lanka.": "IFS runs its largest engineering operation in Colombo. EQT, the Swedish investment firm, owns WSO2 and co owns IFS.",
    "Gapstars and ICT Group have built Dutch engineering capacity in Sri Lanka.": "Dutch founders and technology groups have built engineering capacity in Sri Lanka.",
    "Gapstars runs its largest engineering base in Colombo for clients such as Otrium and Dual Inventive, and ICT Group works with Inivos on automotive software.": "A Dutch founded company runs its largest engineering base in Colombo for Dutch scaleups, and ICT Group works with a Colombo partner on automotive software.",
    "Gapstars regularly flies its Colombo engineers to client headquarters in Europe.": "Colombo engineers working for Dutch clients regularly travel to client headquarters in Europe.",
    "Yes, through suppliers. Inivos contributes to projects": "Yes, through suppliers. Engineers in Colombo contribute to projects",
    "Superloop runs 24x7 network operations from Colombo and Dijital Team built a 200 person team in two years.": "An ASX listed telecom runs 24x7 network operations from Colombo, and Australian companies have built teams of 200 people here.",
    "Superloop and Dijital Team both run technical teams in Colombo. SimCentric has offices in Australia and its engineering centre in Sri Lanka.": "An ASX listed telecom runs network engineering and operations from Colombo, and other Australian companies run dedicated technical teams here.",
    "which is one reason Superloop runs network operations there.": "which is one reason an Australian telecom runs network operations there.",
    "Yes. Surge Global won a government technology transformation contract in Qatar, and Gapstars and Tiqri both serve clients in the region.": "Yes. A Sri Lankan firm won a government technology transformation contract in Qatar, and several Colombo companies serve clients in the region.",
    "Companies we have reported on include Virtusa, Creative Software, Tiqri, Gapstars, Xeynergy, Rootcode, Surge Global, Frontwalker and Inivos. Each has a sourced story on this site.": "There are several hundred, from firms of 3,000+ engineers such as Virtusa to specialist teams of under 100. Tell us the work and we will introduce the ones that fit.",
    "Creative Software, Tiqri, Gapstars, Dijital Team, Frontwalker and Xeynergy all run dedicated teams for international clients.": "Many Sri Lankan engineering companies do. Tell us the stack and team size and we will introduce the ones that fit.",
    "Orion City houses IFS, Virtusa, Synopsys and Michelin teams among 85+ companies. TRACE Expert City,": "Orion City, TRACE Expert City,",
    "the World Trade Center and Port City Colombo are the other main hubs.": "the World Trade Center and Port City Colombo are the main hubs.",
    "Michelin, EY, HCLTech, HSBC and Superloop all run": "Michelin, EY, HCLTech and HSBC all run",
    "Superloop, for one, gives every Colombo employee company stock.": "Some foreign employers give every Colombo employee company stock.",
    "WealthOS, acquired by JPMorganChase in 2026, built its platform with a Sri Lankan team. Oceans places Sri Lankan talent with US startups such as Morning Brew and beehiiv, and Gapstars works with Dutch scaleups such as Otrium.": "A wealth platform acquired by JPMorganChase in 2026 was built with a Sri Lankan team. US startups such as Morning Brew and beehiiv work with Sri Lankan professionals, as do Dutch scaleups.",
    "Oceans says its clients save 50% to 80% compared with US hires. The Export Development Board cites": "The Export Development Board cites",
}


def _deep(x):
    if isinstance(x, str):
        for old, new in REWRITE.items():
            if old in x:
                x = x.replace(old, new)
                USED.add(old)
        return x
    if isinstance(x, dict):
        return {k: _deep(v) for k, v in x.items()}
    if isinstance(x, list):
        return [_deep(v) for v in x]
    if isinstance(x, tuple):
        return tuple(_deep(v) for v in x)
    return x


USED = set()
_apply = apply


def apply(items):  # noqa: F811
    _apply(items)
    for x in items:
        cites = x["cites"]
        x.update(_deep({k: v for k, v in x.items() if k != "cites"}))
        x["cites"] = cites
