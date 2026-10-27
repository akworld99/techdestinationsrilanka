"""Buyer market pages: import from Sri Lanka to the UK, USA, Australia, UAE, EU and India.
Top export tables are from the Export Development Board's market and country briefs (Sri Lanka Customs data, 2025).
Only facts opened on the linked page are used; no buyers are named."""

EDB_MP = "https://www.srilankabusiness.com/pdfs/market-profiles/2026/"
NEWS9M = "https://www.newswire.lk/2026/10/26/sri-lankas-exports-reach-us-13-61-bn-in-first-nine-months-of-2026/"
EDB9M = "https://www.srilankabusiness.com/news/sri-lankas-exports-surpass-usd-13-6-bn-in-the-first-nine-months-of-2026-recording-5-percent-growth.html"
EDB25 = "https://www.srilankabusiness.com/news/sri-lankas-export-performance-exceeded-us-17.2-billion-in-2025.html"

AP, CO, TEA, TY, GL, FOOD = "apparel-manufacturing", "coconut-products", "ceylon-tea", "industrial-tyres", "rubber-gloves", "processed-food-beverages"


def _src(country, file):
    return (f'Source: Export Development Board, <a href="{EDB_MP}{file}" rel="noopener">market and country brief on {country}</a>, '
            "using Sri Lanka Customs data. Selected lines from the brief's top 20; values in US$ million. Products link to our buyer's guide for that category.")


MARKETS = [
    dict(
        slug="import-from-sri-lanka-to-uk", short="UK", the="the UK", label="United Kingdom", to="United Kingdom",
        title="Import from Sri Lanka to the UK: duties, rules and suppliers",
        h1="Import from Sri Lanka to the UK: what sells, duty access and import rules",
        desc="Importing from Sri Lanka to the UK: zero duty on 7,000+ products under the DCTS, what the UK buys, IPAFFS and catch certificate rules, and vetted suppliers.",
        answer=("The UK bought US$929 million of goods from Sri Lanka in 2025, mostly clothing, followed by coconut milk and rubber gloves. "
                "Sri Lanka is in the Enhanced Preferences tier of the UK's Developing Countries Trading Scheme, which gives zero duty on more than 7,000 products "
                "for goods that meet its rules of origin. Animal products and high risk food must be pre-notified on IPAFFS before arrival, and wild caught fish needs a catch certificate. "
                "Exports to the UK fell 9.33% in January to September 2026, to US$654 million."),
        stats=[("US$929M", "Sri Lankan goods exported to the UK in 2025"), ("7,000+", "products at zero duty under the UK DCTS, at HS 6 digit level"), ("US$654M", "January to September 2026, down 9.33%")],
        top=dict(head=["Product", "2025"], src=_src("the United Kingdom", "united-kingdom-2026.pdf"), rows=[
            ("Women's outerwear", (209.41,), AP), ("Men's and women's undergarments", (132.63,), AP), ("Babies' garments", (126.68,), AP),
            ("Men's outerwear", (85.24,), AP), ("T-shirts", (49.38,), AP), ("Liquid coconut milk", (24.03,), CO), ("Activewear and sportswear", (17.49,), AP),
            ("Industrial and surgical rubber gloves", (17.27,), GL), ("Knitwear, jerseys and pullovers", (16.93,), AP), ("Textile gloves and mittens", (15.25,), AP),
            ("Fresh or chilled fish", (12.65,), "seafood"), ("Coco peat, fibre pith and moulded products", (11.51,), "coco-peat-coir"),
            ("Pneumatic and retreaded tyres and tubes", (11.20,), TY), ("Tea packets", (10.85,), TEA), ("All goods", (929.03,), None)]),
        duty=[
            ("Sri Lanka is in the Enhanced Preferences tier of the UK Developing Countries Trading Scheme, with zero duty on more than 7,000 eligible products at HS 6 digit level.", "EDB, UK DCTS profile", "https://www.srilankabusiness.com/pdfs/market-access-profiles/uk-dcts.pdf"),
            ("The UK has relaxed DCTS rules of origin for Sri Lankan garments (HS chapters 61 and 62), so fabric and other inputs can come from any country without losing tariff free access, as announced in August 2025.", "Ada Derana", "https://www.adaderana.lk/news/111648/details-of-uks-liberalised-trade-rules-for-sri-lankan-garment-sector-released"),
            ("UK buyers took US$654.36 million of Sri Lankan goods in January to September 2026, down 9.33%, and apparel to the UK fell 10.41%.", "EDB, January to September 2026", EDB9M),
        ],
        rules=[
            ("Products of animal origin, and high risk food not of animal origin, must be pre-notified on IPAFFS at least one working day before arrival.", "Dover Port Health Authority", "https://www.doverporthealth.gov.uk/pre-notifications"),
            ("Fish and fishery products under CN 03, 1604 or 1605 with more than 20% wild caught content need an IUU catch certificate, plus a processing statement if processed outside the flag state.", "Dover Port Health Authority", "https://www.doverporthealth.gov.uk/import-guidance/illegal-unreported-and-unregulated"),
        ],
        cats=[AP, CO, GL, TEA, "spices-essential-oils"],
        faqs=[
            ("Is there import duty from Sri Lanka to the UK?", "Many Sri Lankan goods enter at zero duty. Sri Lanka is in the Enhanced Preferences tier of the UK Developing Countries Trading Scheme, which covers more than 7,000 products at HS 6 digit level, provided the goods meet the scheme's rules of origin. Import VAT still applies."),
            ("What does the UK import from Sri Lanka?", "Mostly clothing: women's and men's outerwear, undergarments, babies' garments and T-shirts. Coconut milk, activewear, rubber gloves, knitwear and textile gloves follow, according to the EDB's 2025 brief on the UK."),
            ("Do I need to pre-notify food imports from Sri Lanka to the UK?", "Products of animal origin and high risk food not of animal origin must be pre-notified on IPAFFS at least one working day before arrival. Wild caught fish also needs a catch certificate."),
        ]),
    dict(
        slug="import-from-sri-lanka-to-usa", short="USA", the="the US", label="United States", to="United States",
        title="Import from Sri Lanka to the USA: tariffs, FDA and suppliers",
        h1="Import from Sri Lanka to the USA: what sells, tariffs and FDA rules",
        desc="Importing from Sri Lanka to the USA: the extra 10% Section 301 duty, what the US buys from Sri Lanka, FDA prior notice and registration, and vetted suppliers.",
        answer=("The United States is Sri Lanka's largest market. It bought US$3.0 billion of Sri Lankan goods in 2025, led by undergarments, outerwear and other clothing, "
                "followed by rubber tyres, textile gloves, rubber gloves and activated carbon. Since 24 July 2026 Sri Lankan goods pay an additional 10% Section 301 duty on top of normal duty, with some exclusions. "
                "Commercial food shipments need FDA prior notice before they arrive. Exports to the US were flat in January to September 2026, at US$2.25 billion."),
        stats=[("US$3.0B", "Sri Lankan goods exported to the US in 2025"), ("10%", "additional Section 301 duty since 24 July 2026"), ("US$2.25B", "January to September 2026, up 0.05%")],
        top=dict(head=["Product", "2025"], src=_src("the USA", "usa-2026.pdf"), rows=[
            ("Men's and women's undergarments", (662.70,), AP), ("Women's outerwear", (439.83,), AP), ("Men's outerwear", (252.48,), AP),
            ("Pneumatic and retreaded tyres and tubes", (187.53,), TY), ("Textile gloves and mittens", (170.79,), AP), ("T-shirts", (158.57,), AP),
            ("Industrial and surgical rubber gloves", (75.36,), GL), ("Knitwear, jerseys and pullovers", (72.70,), AP), ("Activated carbon", (63.74,), "activated-carbon"),
            ("Activewear and sportswear", (63.65,), AP), ("All goods", (2999.15,), None)]),
        duty=[
            ("Sri Lanka is one of 17 economies whose goods pay an additional 10% Section 301 duty, on goods entered from 12:01 a.m. eastern time on 24 July 2026. Exclusions include goods subject to Section 232 tariffs.", "EY Tax News", "https://taxnews.ey.com/news/2026-1603-ustr-takes-final-action-imposing-tariffs-on-60-trading-partners-as-section-122-tariffs-expire"),
            ("Normal duty depends on the HS code. Look up the line in the US Harmonized Tariff Schedule and confirm the total with your customs broker.", "USITC Harmonized Tariff Schedule", "https://hts.usitc.gov/"),
            ("US buyers took US$2,252.99 million of Sri Lankan goods in January to September 2026, up 0.05%, and apparel to the US fell 3.83%.", "EDB, January to September 2026", EDB9M),
        ],
        rules=[
            ("For commercial food shipments, FDA must receive and confirm prior notice before the food arrives (USDA regulated meat, poultry and egg products are exempt): at least 8 hours ahead by sea, 4 hours by air or rail and 2 hours by road. Food without adequate prior notice can be refused and held at the port.", "US FDA", "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/what-you-need-know-about-prior-notice-imported-food-shipments"),
            ("Registered food facilities must renew their FDA registration between 1 October and 31 December of each even numbered year. The current window closes on 31 December 2026, so ask your exporter to confirm it has renewed.", "US FDA", "https://www.fda.gov/food/online-registration-food-facilities/food-facility-registration-user-guide-biennial-registration-renewal"),
        ],
        cats=[AP, TY, GL, "activated-carbon", "ceylon-cinnamon"],
        faqs=[
            ("What is the tariff on imports from Sri Lanka to the USA?", "Normal duty for the HS code, plus an additional 10% Section 301 duty on Sri Lankan goods entered since 24 July 2026, with exclusions such as goods under Section 232 tariffs. Look up the line in the Harmonized Tariff Schedule and ask your customs broker for the current total."),
            ("What does the US import from Sri Lanka?", "Clothing leads, with US$663 million of undergarments and US$440 million of women's outerwear in 2025, followed by men's outerwear, rubber tyres, textile gloves, T-shirts, rubber gloves, knitwear, activated carbon and activewear."),
            ("What FDA steps apply to food from Sri Lanka?", "FDA must receive prior notice of each commercial food shipment before it arrives, at least 8 hours ahead for sea freight. Registered food facilities renew their FDA registration between 1 October and 31 December of each even numbered year, so ask your exporter to confirm it renewed in 2026."),
        ]),
    dict(
        slug="import-from-sri-lanka-to-australia", short="Australia", the="Australia", label="Australia", to="Australia",
        title="Import from Sri Lanka to Australia: duty, BICON, suppliers",
        h1="Importing from Sri Lanka to Australia: what sells, duty and biosecurity",
        desc="Importing from Sri Lanka to Australia: DCS preference rates, no FTA, BICON rules for tea, spices and coco peat, what Australia buys and vetted suppliers.",
        answer=("Australia bought US$262 million of goods from Sri Lanka in 2025, led by clothing, textile gloves, packet tea, tyres and rubber gloves. "
                "There is no free trade agreement, but Sri Lanka is listed as a developing country under the Australian System of Tariff Preferences, so DCS preference rates apply "
                "where the tariff sets one. Plant products must clear biosecurity, so check BICON for tea, spices, coco peat and coconut products before you order."),
        stats=[("US$262M", "Sri Lankan goods exported to Australia in 2025"), ("DCS", "developing country preference rates apply"), ("US$18.8M", "packet tea shipped to Australia in 2025")],
        top=dict(head=["Product", "2025"], src=_src("Australia", "australia-2026.pdf"), rows=[
            ("Women's outerwear", (33.50,), AP), ("Textile gloves and mittens", (20.90,), AP), ("Tea packets", (18.80,), TEA), ("Men's and women's undergarments", (16.90,), AP),
            ("T-shirts", (16.30,), AP), ("Men's outerwear", (13.90,), AP), ("Pneumatic and retreaded tyres and tubes", (13.00,), TY),
            ("Industrial and surgical rubber gloves", (12.40,), GL), ("Electrical and electronic products", (10.50,), "electrical-cables-transformers"), ("Coconut oil", (9.31,), CO),
            ("All goods", (262.00,), None)]),
        duty=[
            ("Sri Lanka is listed in Schedule 1, Part 4, Division 1 of Australia's tariff preference lists: developing countries subject to DCS rates of duty.", "Australian Border Force", "https://www.abf.gov.au/importing-exporting-and-manufacturing/tariff-classification/current-tariff/schedule-1"),
            ("Under section 14 of the Customs Tariff Act, a rate marked DCS in the tariff applies to goods from the developing countries in Part 4.", "Customs Tariff Act 1995, section 14", "https://www5.austlii.edu.au/au/legis/cth/consol_act/cta1995178/s14.html"),
            ("There is no Australia and Sri Lanka free trade agreement. The two countries have a Trade and Investment Framework Arrangement, signed in 2017 and renewed in 2023.", "DFAT, Sri Lanka country brief", "https://dfat.gov.au/geo/sri-lanka/sri-lanka-country-brief"),
            ("From 1 July 2024 Australia cut duty to Free on goods under 457 tariff headings and subheadings.", "Customs Tariff Alteration 2024", "https://legislation.gov.au/F2024L00659/asmade/2024-06-07/es/original/pdf"),
        ],
        rules=[
            ("Check BICON for every product. Pure black or green tea needs no import permit or mandatory inspection on arrival; some herbal teas need a permit, and spices, seeds and grains may need processing or treatment.", "Department of Agriculture, Fisheries and Forestry", "https://www.agriculture.gov.au/import/goods/plant-products/importing-plant-products-for-human-consumption"),
            ("Coir peat used as a growing medium, mulch or fertiliser must meet the BICON coir peat conditions. Check the live BICON case for permit and treatment requirements before you ship.", "Department of Agriculture, Fisheries and Forestry", "https://www.agriculture.gov.au/import/goods/plant-products/information-about-importing-plant-products-for-environmental-uses"),
            ("Imported food can be referred to the Imported Food Inspection Scheme for inspection and testing, and stays on hold until it passes. Importers are responsible for meeting the Food Standards Code.", "Department of Agriculture, Fisheries and Forestry", "https://www.agriculture.gov.au/biosecurity-trade/import/goods/food/how"),
        ],
        cats=[AP, TEA, TY, "coco-peat-coir", CO],
        faqs=[
            ("Is there a free trade agreement between Australia and Sri Lanka?", "No. The two countries have a Trade and Investment Framework Arrangement, signed in 2017 and renewed in 2023. Sri Lanka gets developing country (DCS) preference rates under Australia's tariff where a DCS rate is set."),
            ("Can I import tea and spices from Sri Lanka into Australia?", "Yes, subject to biosecurity. Pure black or green tea needs no import permit or mandatory inspection; some herbal teas need a permit, and spices may need treatment. Check each product in BICON before you order."),
            ("Can I import coco peat from Sri Lanka into Australia?", "Yes, if it meets the BICON coir peat conditions. Check the live BICON case for permit and treatment requirements before the exporter ships."),
        ]),
    dict(
        slug="import-from-sri-lanka-to-uae", short="UAE", the="the UAE", label="United Arab Emirates", to="United Arab Emirates",
        title="Sri Lanka to Dubai and UAE: import duty, rules, suppliers",
        h1="Importing from Sri Lanka to Dubai and the UAE: what sells, duty and food rules",
        desc="Importing from Sri Lanka to Dubai and the UAE: 5% customs duty, CEPA status, Ceylon tea and coconut products the UAE buys, food registration and suppliers.",
        answer=("The UAE bought US$341 million of goods from Sri Lanka in 2025, and tea was the largest line, at US$101.5 million in bulk and packets. "
                "Petroleum oils, clothing, cocoa preparations, coconut milk powder, desiccated coconut and king coconut follow. Most goods pay the UAE's standard 5% customs duty, "
                "though some are rated differently, and no UAE and Sri Lanka trade agreement was in force in October 2026. Exports to the UAE fell 10.5% in January to September 2026, to US$232 million. In Dubai, food product approvals and import permits run through Dubai Municipality's digital systems."),
        stats=[("US$341M", "Sri Lankan goods exported to the UAE in 2025"), ("US$101.5M", "Ceylon tea, bulk and packets, 2025"), ("5%", "standard UAE customs duty on most goods")],
        top=dict(head=["Product", "2025"], src=_src("the UAE", "uae-2026.pdf"), rows=[
            ("Tea in bulk", (70.86,), TEA), ("Petroleum oils", (31.09,), None), ("Tea packets", (30.66,), TEA), ("Men's and women's undergarments", (15.85,), AP),
            ("Cocoa and cocoa preparations", (14.97,), FOOD), ("Coconut milk powder", (12.20,), CO), ("Women's outerwear", (12.17,), AP), ("Desiccated coconut", (10.94,), CO),
            ("Other food preparations", (8.98,), FOOD), ("Fresh coconuts and king coconut", (8.23,), "fruits-vegetables"), ("Melons and papayas", (5.34,), "fruits-vegetables"),
            ("Tea bags", (4.03,), TEA), ("Coco peat, fibre pith and moulded products", (3.64,), "coco-peat-coir"), ("Nutmeg and mace", (3.58,), "spices-essential-oils"),
            ("All goods", (341.06,), None)]),
        duty=[
            ("The UAE charges 5% customs duty on the value of goods imported from abroad, with some goods at other rates.", "Sharjah Customs, customs tariff", "https://www.sharjahcustoms.gov.ae/en/customs-tari"),
            ("No UAE and Sri Lanka Comprehensive Economic Partnership Agreement was in force in October 2026. In September 2026 Sri Lanka's Foreign Minister said Sri Lanka wanted it concluded faster.", "Ministry of Foreign Affairs, Sri Lanka", "https://www.mfa.gov.lk/en/news/minister-vijitha-herath-concludes-visit-dubai-united-arab-emirates"),
            ("A separate investment protection agreement, not a trade deal, was signed in February 2025.", "Embassy of Sri Lanka, Abu Dhabi", "https://abudhabi.embassy.gov.lk/?p=9623"),
            ("Exports to the UAE fell 10.5% in January to September 2026, to US$232.06 million.", "EDB, January to September 2026", EDB9M),
        ],
        rules=[
            ("Dubai Municipality's Montaji+ platform manages food product approvals and regulatory status for food imports and exports, with more than 1.7 million registered products.", "Dubai Municipality", "https://www.dm.gov.ae/latest-digital-food-safety-services-showcased-at-gulfood-2025/"),
            ("Dubai's Unified Permit System handles food permit approvals and is linked to the emirate's food inspection checks.", "Dubai Municipality", "https://www.dm.gov.ae/latest-digital-food-safety-services-showcased-at-gulfood-2025/"),
        ],
        cats=[TEA, CO, FOOD, "fruits-vegetables", "spices-essential-oils"],
        faqs=[
            ("What is the import duty from Sri Lanka to the UAE?", "Most goods pay the standard UAE customs duty of 5% of the value, but some are rated differently, so check the HS code. No UAE and Sri Lanka trade agreement was in force in October 2026, so there is no preference rate yet."),
            ("What does the UAE import from Sri Lanka?", "Tea first: US$70.9 million in bulk and US$30.7 million in packets in 2025. Then petroleum oils, undergarments, cocoa preparations, coconut milk powder, women's outerwear, desiccated coconut, food preparations and king coconut."),
            ("Is there a UAE and Sri Lanka CEPA?", "Not as of October 2026. Sri Lanka wants one: in September 2026 its Foreign Minister said Sri Lanka wanted the CEPA concluded faster. A separate investment protection agreement was signed in February 2025."),
        ]),
    dict(
        slug="import-from-sri-lanka-to-eu", short="EU", the="the EU", label="European Union", to="European Union",
        title="Import from Sri Lanka to the EU: GSP+, EUDR and suppliers",
        h1="Import from Sri Lanka to the EU: Germany, the Netherlands, GSP+ and the rules",
        desc="Importing from Sri Lanka to the EU: GSP+ duty free access on 66% of lines, what Germany and the Netherlands buy, EUDR and catch certificate rules, suppliers.",
        answer=("Sri Lanka has had GSP+ access to the EU since 2017, which gives duty free entry on 66% of EU tariff lines. Germany bought US$706 million of Sri Lankan goods in 2025, "
                "Italy US$680 million and the Netherlands US$475 million. Germany and the Netherlands buy mostly clothing, coconut milk, tyres, gloves, fish and tea. New EU GSP rules apply from 1 January 2027, "
                "and Sri Lanka must reapply for GSP+ by the end of 2028. Rubber is covered by the EU Deforestation Regulation, which applies to large and medium operators from 30 December 2026."),
        stats=[("66%", "of EU tariff lines duty free under GSP+"), ("US$706M", "Sri Lankan goods exported to Germany in 2025"), ("US$475M", "to the Netherlands in 2025")],
        top=dict(head=["Product", "Germany, 2025", "Netherlands, 2025"],
                 src=(f'Source: Export Development Board market and country briefs on <a href="{EDB_MP}germany-2026.pdf" rel="noopener">Germany</a> and '
                      f'<a href="{EDB_MP}netherlands-2026.pdf" rel="noopener">the Netherlands</a>, using Sri Lanka Customs data. Selected lines from each brief\'s top 20; values in US$ million, and a dash means the line is not in that brief\'s top 20.'),
                 rows=[
                     ("Men's and women's undergarments", (51.71, 115.00), AP), ("Men's outerwear", (71.00, 46.40), AP), ("Liquid coconut milk", (52.96, 43.50), CO),
                     ("Women's outerwear", (52.18, 18.30), AP), ("T-shirts", (26.44, 34.10), AP), ("Pneumatic and retreaded tyres and tubes", (48.27, 9.93), TY),
                     ("Frozen fish", (26.70, 18.40), "seafood"), ("Textile gloves and mittens", (46.25, 6.13), AP), ("Tea packets", (16.30, 23.70), TEA),
                     ("Industrial and surgical rubber gloves", (25.96, 8.50), GL), ("Coconut oil", (21.26, 7.87), CO), ("Tea in bulk", (26.03, None), TEA),
                     ("Coconut cream", (None, 17.70), CO), ("Desiccated coconut", (15.73, 7.28), CO), ("Coco peat, fibre pith and moulded products", (None, 9.57), "coco-peat-coir"),
                     ("Pepper", (9.03, None), "spices-essential-oils"), ("All goods", (706.49, 474.80), None)]),
        duty=[
            ("Sri Lanka has had EU GSP+ since 2017, giving duty free access on 66% of EU tariff lines.", "European Commission", "https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/sri-lanka_en"),
            ("New EU GSP rules apply from 1 January 2027, and Sri Lanka must reapply for GSP+ by 31 December 2028.", "Daily Mirror", "https://www.dailymirror.lk/news-features/Sri-Lanka-faces-tougher-test-to-retain-EU-GSP-benefits/131-348072"),
            ("Goods exports to the EU were down 0.15% in January to September 2026: Italy US$514.28 million, Germany US$513.08 million and the Netherlands US$328.12 million.", "EDB, January to September 2026", EDB9M),
        ],
        rules=[
            ("Rubber is one of the commodities covered by the EU Deforestation Regulation: operators must be able to show covered products do not come from recently deforested land. It applies from 30 December 2026 for large and medium operators and from 30 June 2027 for micro and small ones.", "European Commission", "https://environment.ec.europa.eu/topics/forests/deforestation/regulation-deforestation-free-products_en"),
            ("In the Netherlands, consignments subject to border controls must be pre-notified to the NVWA at least one working day before arrival, by submitting an electronic CHED through the NVWA's national system.", "NVWA", "https://english.nvwa.nl/topics/import-of-animals-and-animal-products/information-on-prior-notification-of-consignments-in-the-netherlands-for-foreign-operators"),
            ("Since 10 January 2026, catch certificates for fishery imports into the EU are submitted and checked digitally in the EU's CATCH system, replacing the paper process.", "European Commission, Oceans and Fisheries", "https://oceans-and-fisheries.ec.europa.eu/news/new-digital-certification-system-tackle-illegal-fishing-2026-01-12_en"),
        ],
        cats=[AP, CO, TY, "seafood", "ceylon-cinnamon"],
        faqs=[
            ("Does Sri Lanka have GSP+?", "Yes. Sri Lanka has had GSP+ since 2017, giving duty free access on 66% of EU tariff lines. New EU GSP rules apply from 1 January 2027 and Sri Lanka must reapply by 31 December 2028."),
            ("What do Germany and the Netherlands import from Sri Lanka?", "Mostly clothing, with liquid coconut milk, tyres, textile and rubber gloves, frozen fish and tea. Germany bought US$706 million of Sri Lankan goods in 2025 and the Netherlands US$475 million."),
            ("Does the EU Deforestation Regulation affect Sri Lankan rubber?", "Yes. Rubber is one of the commodities it covers, so operators must be able to show covered products do not come from recently deforested land. It applies from 30 December 2026 for large and medium operators and from 30 June 2027 for micro and small ones."),
        ]),
    dict(
        slug="import-from-sri-lanka-to-india", short="India", the="India", label="India", to="India",
        title="Import from Sri Lanka to India: ISFTA duty and suppliers",
        h1="Import from Sri Lanka to India: what sells, ISFTA duty and import rules",
        desc="Importing from Sri Lanka to India: duty free entry under the ISFTA, the negative list and quotas, pepper rules, FSSAI clearance, what India buys and suppliers.",
        answer=("India is Sri Lanka's second largest market. It bought US$1.04 billion of Sri Lankan goods in 2025, up 17.21%, led by petroleum oils, animal feed, pepper, areca nuts and animal and vegetable fats and oils. "
                "Under the India and Sri Lanka Free Trade Agreement, in force since March 2000, most Sri Lankan goods enter duty free if they meet its rules of origin, "
                "except 429 lines on India's negative list; pepper, garments, tea and desiccated coconut get preferences only within annual quotas. Food imports clear through FSSAI's online import clearance system."),
        stats=[("US$1.04B", "Sri Lankan goods exported to India in 2025, up 17.21%"), ("+12.3%", "January to September 2026, to US$890M"), ("Since 2000", "India and Sri Lanka Free Trade Agreement")],
        top=dict(head=["Product", "2025"], src=_src("India", "india-2026.pdf"), rows=[
            ("Petroleum oils", (151.56,), None), ("Animal feed", (131.85,), FOOD), ("Pepper", (84.25,), "spices-essential-oils"), ("Areca nuts", (70.48,), None),
            ("Animal and vegetable fats and oils", (50.46,), None), ("Base metal products", (50.26,), "light-engineering"), ("Women's outerwear", (30.09,), AP),
            ("Non-alcoholic beverages", (29.31,), FOOD), ("Coconut milk powder", (24.64,), CO), ("Wood pulp, waste paper and paperboard", (24.50,), None),
            ("All goods", (1035.72,), None)]),
        duty=[
            ("The India and Sri Lanka Free Trade Agreement has been in force since 1 March 2000. India's negative list has 429 tariff lines. To qualify, goods need a change of tariff heading and 35% value addition, or 25% in Sri Lanka where Indian inputs bring the total to 35%.", "EDB, ISFTA profile", "https://www.srilankabusiness.com/pdfs/market-access-profiles/isfta.pdf"),
            ("India's annual ISFTA quotas: vanaspati, bakery shortening and margarine 250,000 tonnes at zero duty, pepper 2,500 tonnes at zero duty, garments 8 million pieces at zero duty, desiccated coconut 500 tonnes at a 30% margin of preference and tea 15,000 tonnes at 7.5% duty.", "EDB, ISFTA profile", "https://www.srilankabusiness.com/pdfs/market-access-profiles/isfta.pdf"),
            ("Exports to India rose 12.3% in January to September 2026, to US$889.84 million.", "EDB, January to September 2026", EDB9M),
        ],
        rules=[
            ("Food imports are cleared through FSSAI's Food Import Clearance System, linked to Customs ICEGate: importers apply online, book the joint inspection and have samples sent to labs through it.", "FSSAI", "https://foodregulatory.fssai.gov.in/fics"),
            ("India set a minimum import price of Rs 500 per kg CIF for black pepper; imports below it are prohibited, as the government told Parliament in February 2021. Confirm the current rule with your customs broker.", "Lok Sabha answer, 3 February 2021", "https://eparlib.nic.in/bitstream/123456789/992871/1/AU306.pdf"),
        ],
        cats=["spices-essential-oils", FOOD, CO, "light-engineering", AP],
        faqs=[
            ("What is the import duty from Sri Lanka to India?", "Under the India and Sri Lanka Free Trade Agreement, most Sri Lankan goods enter duty free if they meet its rules of origin: a change of tariff heading and 35% value addition, or 25% where Indian inputs bring the total to 35%. The exceptions are 429 tariff lines on India's negative list, and pepper, garments, tea and desiccated coconut get preferences only within annual quotas."),
            ("What does India import from Sri Lanka?", "In 2025 the largest lines were petroleum oils, animal feed, pepper, areca nuts, fats and oils, base metal products, women's outerwear, non-alcoholic beverages, coconut milk powder and paper."),
            ("Is there a minimum import price for black pepper from Sri Lanka?", "India set a minimum import price of Rs 500 per kg CIF for black pepper, and imports below it are prohibited, as the government told Parliament in 2021. Confirm the current rule with your customs broker before you contract."),
        ]),
]
