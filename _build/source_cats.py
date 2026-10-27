"""Export categories for the Source from Sri Lanka section. Every figure is sourced; research notes and raw keyword data
for each category are in the session's research files. No buyer is named, and exporters are described rather than named.
Order of CATS = order of the tiles on the hub."""

# ---------------------------------------------------------------- sources used on many pages
EDB25 = "https://www.srilankabusiness.com/news/sri-lankas-export-performance-exceeded-us-17.2-billion-in-2025.html"
EDB25_FT = "https://www.ft.lk/top-story/Export-earnings-up-5-6-to-17-2-b-in-2025/26-787471"
EDB9M = "https://www.newswire.lk/2026/10/26/sri-lankas-exports-reach-us-13-61-bn-in-first-nine-months-of-2026/"
EDB1H = "https://www.ft.lk/front-page/Export-earnings-exceed-9-b-in-1H/44-794983"
EDB_PROC = "https://www.srilankabusiness.com/pdf/export-procedure-2020.pdf"


def S2(extra=""):
    return (f'Sources: Export Development Board, <a href="{EDB25}" rel="noopener nofollow">2025 export performance</a> and '
            f'<a href="{EDB9M}" rel="noopener nofollow">January to September 2026</a> (via Newswire).{extra}')


def ln(label, url):
    return f' <a href="{url}" rel="noopener nofollow">{label}</a>'


CATS = []


def cat(**k):
    k.setdefault("tender", None)
    k.setdefault("names", [])
    k.setdefault("caveats", [])
    k.setdefault("stats_src", S2())
    CATS.append(k)


# ================================================================ sea and earth (group E)
FISH_R = "https://www.srilankabusiness.com/ebooks/industry-capability-report-fishery-products-industry-2025.pdf"
IOTC_NR = "https://iotc.org/sites/default/files/documents/2022/12/IOTC-2022-SC25-NR25E_Sri_Lanka.pdf"
IOTC_25 = "https://iotc.org/sites/default/files/documents/2025/12/Circular_2025-44-Allocated_catch_limits_for_tropical_tuna_in_2025E.pdf"
SIPPO_SF = "https://www.srilankabusiness.com/pdf/sippo-study-seafood-sri-lanka.pdf"
ORN_R = "https://srilankabusiness.com/ebooks/industry-capability-report-ornamental-fish-industry-2025.pdf"
FB_R = "https://www.srilankabusiness.com/ebooks/industry-capability-report-food-beverages-2021.pdf"
FB_PAGE = "https://www.srilankabusiness.com/food-and-beverages/"
GEM_BLOG = "https://www.srilankabusiness.com/blog/the-growing-market-for-sri-lankan-gemstones.html"
GEM_R = "https://www.srilankabusiness.com/ebooks/industry-capability-report-diamonds-gems-jewellery-2026.pdf"
GEM_TYPES = "https://www.srilankabusiness.com/gem-diamond-and-jewellery/about-sri-lanka-gems/sri-lanka-gemstones.html"
GEM_GUIDE = "https://www.srilankabusiness.com/faq/gem-diamond-and-jewellery/exporters/export-gems-sri-lanka-guide.html"
MIN_BLOG = "https://www.srilankabusiness.com/blog/mineral-resources-from-sri-lanka.html"
USGS = "https://pubs.usgs.gov/myb/vol3/2019/myb3-2019-sri-lanka.pdf"

SEAFOOD = dict(
    slug="seafood", label="Seafood", short="Yellowfin tuna, swordfish, shrimp, crab and lobster.", art="s-seafood", seller="seafood exporter",
    h1="Seafood exporters in Sri Lanka: yellowfin tuna, swordfish, shrimp and crab",
    title="Seafood exporters in Sri Lanka: tuna, swordfish, shrimp and crab suppliers",
    desc="Source yellowfin tuna, swordfish, shrimp, crab and lobster from Sri Lankan seafood exporters. EU approved plants, catch certificates, HS codes, markets and how to buy.",
    answer=("Sri Lanka exported US$240.19 million of seafood in 2025, led by yellowfin tuna and swordfish, fresh, chilled and frozen, with shrimp, crab, "
            "lobster and sea cucumber. The EU lifted its ban on Sri Lankan fishery exports in June 2016, and the Export Development Board counts 55 EU "
            "approved processing plants. The largest markets in 2024 were the US, Germany, the UK, France, Italy and the Netherlands. Supply follows the "
            "monsoon and yellowfin is under an Indian Ocean catch limit, so agree volumes and a season plan with your supplier."),
    stats=[("US$240.19M", "seafood exports in 2025, up 3.09%"), ("55", "EU approved processing plants"), ("US$180.81M", "January to September 2026, down 2.03%")],
    glance=[("Main products", "Yellowfin tuna and swordfish, fresh, chilled and frozen; tuna loins and fillets; shrimp, crab, lobster and sea cucumber"),
            ("Largest markets in 2024", "US, Germany, UK, France, Italy, Netherlands, Hong Kong, China, Canada, Japan"),
            ("Documents per shipment", "EU health certificate and catch certificate; export licence for sea cucumber and lobster"),
            ("Certificates to ask for", "EU approval number, HACCP, BRCGS or IFS Food, MSC or Friend of Sea where your market needs it"),
            ("Watch for", "Monsoon seasonality and the yellowfin catch limit")],
    products=[("Yellowfin tuna, fresh or chilled", "0302.32"), ("Yellowfin tuna, frozen", "0303.42"), ("Swordfish, fresh or chilled", "0302.47"), ("Swordfish, frozen", "0303.57"),
              ("Tuna loins and fish fillets", "0304"), ("Shrimps and prawns, frozen", "0306.17"), ("Crabs, live, fresh or chilled", "0306.33"), ("Crabs, frozen", "0306.14"),
              ("Rock lobster, frozen", "0306.11"), ("Sea cucumber, frozen", "0308.12"), ("Prepared crustaceans and molluscs", "1605")],
    names=["Ahi tuna", "tuna loins", "tuna steaks", "mud crab", "spiny lobster", "beche de mer"],
    evidence=[("The EU completely lifted its ban on Sri Lankan fishery exports in June 2016. It had been imposed in January 2015 over illegal, unreported and unregulated fishing.", "Ada Derana", "https://adaderana.lk/news/35701/-eu-ban-on-sri-lankan-fish-exports-completely-lifted"),
              ("The Export Development Board counts 55 EU approved fish processing plants in Sri Lanka.", "EDB fishery report 2025", FISH_R),
              ("Yellowfin tuna made up 36% of Sri Lanka's large pelagic catch of 87,546 tonnes in 2021, landed by more than 5,000 multi day boats.", "IOTC national report", IOTC_NR),
              ("Sri Lanka's exclusive economic zone covers 517,000 square kilometres, served by 25 major fishery harbours and 106 ice plants.", "EDB fishery report 2025", FISH_R),
              ("Fish fillets were the largest export line in 2024 at US$75.07 million, followed by fresh and chilled fish including tuna and swordfish at US$49.86 million.", "EDB fishery report 2025", FISH_R),
              ("Fresh and chilled seafood ships in gel ice packs, foam boxes and cartons, and in modified atmosphere and vacuum packs.", "EDB", "https://www.srilankabusiness.com/sea-food/why-sri-lankan-sea-food.html")],
    certs=[("EU approved establishment.", "Only plants on the EU list can ship to the EU. Sri Lanka's Department of Fisheries and Aquatic Resources keeps the list and certifies exports."),
           ("Catch certificate.", "Required for wild caught fish entering the EU under the regulation on illegal, unreported and unregulated fishing."),
           ("Health certificate and export licences.", "Issued by the Department of Fisheries and Aquatic Resources, including licences for sea cucumber and lobster."),
           ("HACCP.", "The baseline. The Export Development Board says exporters follow HACCP and Friend of Sea requirements; ask for the current certificate."),
           ("BRCGS or IFS Food, MSC or ASC.", "European importers increasingly expect a recognised food safety scheme and a sustainability label. Check which ones the plant holds."),
           ("US FDA seafood HACCP and SIMP.", "For the US, the importer verifies HACCP compliance and reports chain of custody data for tuna, swordfish, shrimp and sea cucumber.")],
    caveats=[("Supply is seasonal. Fishing inside the exclusive economic zone follows the monsoon, with better catches just before and after it.", "IOTC national report", IOTC_NR),
             ("Yellowfin tuna is under an Indian Ocean Tuna Commission catch limit: 32,958 tonnes for Sri Lanka in 2025.", "IOTC", IOTC_25),
             ("Fresh fish for Europe is time and temperature critical. A market study advises catching no more than three days before the flight and warns that fish arriving above 5°C may be rejected.", "SIPPO seafood study", SIPPO_SF),
             ("Three teatfish sea cucumber species are listed on CITES Appendix II. Confirm the species before you contract sea cucumber.", "CITES listing", "https://www.documentation.eauetbiodiversite.fr/fr/notice/three-species-of-teatfish-to-be-protected-by-cites-100808")],
    ask=["Is the plant on the EU approved list, and what is its approval number?", "Which species, product forms and sizes can you supply each month, and in which season?",
         "Can you provide catch certificates and traceability to the vessel for every lot?", "Which food safety and sustainability certificates do you hold, and for which site?",
         "How do you hold the cold chain from landing to the airport, and what temperatures do you log?"],
    faqs=[("Can Sri Lankan seafood be shipped to the EU?", "Yes. The EU lifted its January 2015 ban on Sri Lankan fishery exports in June 2016. Shipments must come from an EU approved establishment, of which the Export Development Board counts 55, with an EU health certificate and, for wild caught fish, a catch certificate."),
          ("Which seafood does Sri Lanka export most?", "By value in 2024: fish fillets including tuna loins (US$75.07 million), fresh and chilled fish such as tuna and swordfish (US$49.86 million), frozen fish (US$39.50 million) and crustaceans (US$36.23 million), according to the Export Development Board. Seafood exports totalled US$240.19 million in 2025."),
          ("Which countries buy Sri Lankan seafood?", "In 2024 the top markets for edible fish products were the US, Germany, the UK, France, Italy, the Netherlands, Hong Kong, China, Canada and Japan. Germany, France, Italy and the Netherlands together took about 36% of the value."),
          ("Is yellowfin tuna available all year?", "Boats fish through the year, but catches inside Sri Lanka's waters follow the monsoon and yellowfin is under a catch limit of 32,958 tonnes for 2025. Agree monthly volumes and a seasonal plan with your supplier.")],
)
cat(**SEAFOOD)

cat(
    slug="ornamental-fish", label="Ornamental fish", short="Guppies, freshwater and marine aquarium fish.", art="s-aquarium", seller="ornamental fish exporter",
    h1="Ornamental fish exporters in Sri Lanka: aquarium fish wholesale",
    title="Ornamental and aquarium fish exporters in Sri Lanka: wholesale guide",
    desc="Wholesale ornamental and aquarium fish from Sri Lanka: farm bred guppies and freshwater fish, marine fish and invertebrates. Markets, health certificates and how to buy.",
    answer=("Sri Lanka exports ornamental fish to more than 68 countries through about 85 active exporters, according to the Export Development Board. "
            "Freshwater fish led by guppies are bred on farms all year, while marine fish and invertebrates are mostly collected by divers. The US took about "
            "41% of the US$24.46 million exported in 2024. Exports fell 7.6% to US$22.6 million in 2025 and are down 26.71% in the first nine months of 2026, "
            "so check each exporter's current capacity before you plan volumes."),
    stats=[("US$22.6M", "ornamental fish exports in 2025, down 7.6%"), ("68+", "countries Sri Lankan exporters ship to"), ("111", "ornamental fish species in Sri Lanka")],
    glance=[("Main products", "Farm bred freshwater fish led by guppies; marine fish; marine invertebrates such as anemones, shrimps, crabs and starfish"),
            ("Largest markets in 2024", "US (about 41%), China, Australia, UK, Germany, Saudi Arabia, Canada, UAE"),
            ("Documents per shipment", "NAQDA health certificate; animal quarantine and fisheries permits; CITES papers for listed species"),
            ("Watch for", "Falling export volumes and export restrictions on some live species")],
    products=[("Live ornamental freshwater fish: guppy, platy, molly, swordtail, tetras, angelfish", "0301.11"), ("Live ornamental fish, marine and brackish", "0301.19"),
              ("Live marine invertebrates: shrimps, crabs, anemones, starfish", "0306 and 0308"), ("Aquarium and aquaculture feed", "2309.90")],
    names=["aquarium fish", "tropical fish", "guppies", "marine aquarium fish"],
    evidence=[("Sri Lanka has 111 ornamental fish species across freshwater, brackish and marine habitats.", "EDB ornamental fish report 2025", ORN_R),
              ("Exporters ship to more than 68 countries; the Export Development Board counts about 85 active exporters.", "EDB ornamental fish report 2025", ORN_R),
              ("The tropical climate allows freshwater fish to be bred all year, by small and medium farms. Guppies are the largest line.", "EDB ornamental fish report 2025", ORN_R),
              ("Exporters must obtain health certificates from NAQDA, which also trains farmers in breeding and farm management.", "EDB ornamental fish report 2025", ORN_R),
              ("The ornamental fish industry in Sri Lanka has a history of nearly 100 years.", "EDB", "https://www.srilankabusiness.com/aquarium-fish/")],
    certs=[("NAQDA health certificate.", "Required for every ornamental fish export."), ("Animal quarantine and fisheries permits.", "Listed in the Export Development Board's export procedure."),
           ("Department of Fisheries certificate.", "Needed for live species whose export is restricted."), ("CITES permits.", "Needed for listed species, which matters for some marine fish and invertebrates.")],
    caveats=[("Exports are falling: down 7.6% to US$22.6 million in 2025 and down 26.71% in January to September 2026.", "EDB", EDB25),
             ("Marine fish and invertebrates are mostly wild collected, and the Export Development Board warns that over collection can deplete wild stocks.", "EDB ornamental fish report 2025", ORN_R),
             ("Some live species, including endemic fish, are restricted for export. Do not expect endemic species to be freely available.", "EDB", "https://srilankabusiness.com/blog/export-ornamental-fish-sri-lanka.html")],
    ask=["Which species are farm bred and which are wild collected?", "What is your dead on arrival policy and how are claims settled?", "Can you share a current stock list with sizes and weekly volumes?",
         "How do you pack, and how long is the door to door transit to my airport?", "Do any of the species need CITES papers or a restricted species certificate?"],
    faqs=[("What ornamental fish can I source from Sri Lanka?", "Marine, freshwater and brackish water fish, plus marine invertebrates such as anemones, shrimps, crabs, starfish and sea urchins. Farm bred freshwater fish are the largest volume line, led by guppies."),
          ("What documents come with a shipment?", "A NAQDA health certificate, animal quarantine and fisheries permits, and CITES documents for listed species."),
          ("Who buys Sri Lankan ornamental fish?", "In 2024 the US took US$10.04 million of the US$24.46 million exported, about 41%, followed by China, Australia, the UK and Germany. Exporters ship to more than 68 countries."),
          ("Has Sri Lanka banned ornamental fish exports?", "No. A September 2025 ban covers the import, possession and sale of four invasive predatory species. Some live species need a Department of Fisheries certificate to be exported.")],
)

cat(
    slug="processed-food-beverages", label="Processed food and beverages", short="Biscuits, sauces, jams, cordials, drinks and feed.", art="s-food", seller="food manufacturer",
    h1="Processed food and beverage exporters in Sri Lanka: biscuits, sauces, drinks and feed",
    title="Sri Lankan food exporters and manufacturers: biscuits, sauces, beverages",
    desc="Source biscuits and wafers, confectionery, sauces, jams, cordials, ready to drink beverages and animal feed from Sri Lankan food manufacturers. Certificates, markets and how to buy.",
    answer=("Sri Lanka's food and beverage exports rose 24.23% to US$583.89 million in 2025, and processed food rose another 34.19% to US$243.28 million in "
            "the first nine months of 2026, with non alcoholic beverages up 46.78%. The Export Development Board lists more than 110 food and beverage "
            "manufacturers and marketers making biscuits and wafers, confectionery, sauces, jams, cordials, ready to drink beverages, ready to serve food "
            "and animal feed. Most processed food exporters hold ISO 22000, HACCP, BRC, kosher or organic certificates."),
    stats=[("US$583.89M", "food and beverage exports in 2025, up 24.23%"), ("+34.19%", "processed food exports, January to September 2026"), ("110+", "food and beverage manufacturers and marketers")],
    glance=[("Main products", "Biscuits and wafers, confectionery, sauces and condiments, jams, cordials and ready to drink beverages, ready to serve food, animal feed"),
            ("Largest markets (latest EDB split, 2021)", "India, US, Maldives, UAE, Australia for processed food; India, Vietnam and Japan for animal feed"),
            ("Certificates commonly held", "ISO 22000, HACCP, BRC, halal, kosher, organic"),
            ("Documents", "Export health certificate where the importing country asks for one; FDA food facility registration for the US"),
            ("Watch for", "Private label capacity varies by manufacturer, so confirm it early")],
    products=[("Sweet biscuits", "1905.31"), ("Waffles and wafers", "1905.32"), ("Sugar confectionery", "1704"), ("Jams, fruit jellies and purees", "2007"),
              ("Sauces, ketchup, chilli sauce and seasonings", "2103"), ("Food preparations, including beverage mixes and papadam", "2106"),
              ("Cordials and ready to drink fruit beverages", "2202"), ("Animal feed, including aquaculture and poultry feed", "2309.90"), ("Dog and cat food", "2309.10")],
    names=["Sri Lankan food products", "private label biscuits", "cordials", "fruit drinks", "chilli sauce"],
    evidence=[("Food and beverage exports rose 24.23% to US$583.89 million in 2025, with processed food up 40.4%.", "EDB", EDB25),
              ("Processed food exports rose 34.19% to US$243.28 million in January to September 2026, and non alcoholic beverages rose 46.78%.", "EDB via Newswire", EDB9M),
              ("The Export Development Board lists more than 110 food and beverage manufacturing and marketing organisations.", "EDB", FB_PAGE),
              ("Most processed food exporters hold ISO 22000, HACCP, BRC, kosher or organic certificates.", "EDB food and beverage report", FB_R)],
    certs=[("ISO 22000 and HACCP.", "The baseline for export food plants. Ask for the certificate and its scope."), ("BRCGS.", "Expected by many UK and EU retailers."),
           ("Halal, kosher and organic.", "Listed by the Export Development Board among certificates Sri Lankan food exporters hold."),
           ("Export health certificate.", "Issued by the Food Control Administrative Division where the importing country requires one."),
           ("FDA food facility registration.", "Needed for any plant that makes or packs food for the US, renewed every two years.")],
    caveats=[("The Export Development Board publishes two 2025 totals for this sector, US$583.89 million and US$430.49 million, because the scope differs. We quote the first.", "EDB", FB_PAGE),
             ("The sources we checked do not confirm private label capacity across the sector. Ask each manufacturer for private label references.", "EDB", "https://www.srilankabusiness.com/food-and-beverages/why-sri-lankan-food-and-beverages.html"),
             ("The Export Development Board lists high production costs, raw material shortfalls and imported machinery as weaknesses, which can affect minimum orders and lead times.", "EDB food and beverage report", FB_R)],
    ask=["Which food safety certificates does the plant hold, and does the scope cover my product?", "Do you make private label, and for which markets?",
         "What is the minimum order per SKU, and the shelf life?", "Can you meet my market's labelling and ingredient rules?", "Is the plant registered with the FDA, if I sell in the US?"],
    faqs=[("Which food safety certificates do Sri Lankan food manufacturers hold?", "The Export Development Board reports that most processed food exporters hold ISO 22000, HACCP, BRC, kosher or organic certificates, and lists ISO 9000 and halal too. Ask for the certificate and its scope."),
          ("Is Sri Lanka's food export sector growing?", "Yes. Food and beverage exports rose 24.23% to US$583.89 million in 2025, and processed food rose 34.19% to US$243.28 million in January to September 2026."),
          ("Can Sri Lankan manufacturers make private label food?", "Some do. The sources we checked do not confirm it sector wide, so ask each manufacturer for private label references in your market. Tell us what you need and we will check before we introduce anyone."),
          ("Where do Sri Lankan processed foods sell?", "The latest Export Development Board split, from 2021, shows India, the US, the Maldives, the UAE and Australia as the top processed food markets, and India, Vietnam and Japan for animal feed.")],
    tender="Government, institutional and agency food purchases go out to tender. Tender Radar matches them to your products and certificates.",
)

cat(
    slug="gems-jewellery", label="Gems and jewellery", short="Ceylon sapphire, padparadscha, spinel and cut diamonds.", art="s-gems", seller="gem exporter",
    h1="Ceylon sapphires and gems from Sri Lanka: wholesale buying guide",
    title="Ceylon sapphire wholesale and Sri Lanka gem exporters: buyer's guide",
    desc="Buy Ceylon blue sapphire, padparadscha, spinel and other gems wholesale from licensed Sri Lankan exporters. Export rules, gem certificates, treatments and markets.",
    answer=("Sri Lanka exported US$334 million of gems, diamonds and jewellery in 2025: US$189 million of gemstones, US$127 million of diamonds and US$17.8 "
            "million of jewellery, according to the Export Development Board. It is known for Ceylon blue sapphire, padparadscha, star and fancy sapphires "
            "and spinel, mined mainly around Ratnapura and Elahera. Only cut and polished stones may be exported, every exporter needs a National Gem and "
            "Jewellery Authority licence, and about 70% of the stones exported are foreign in origin, so ask for a lab report that states origin and treatment."),
    stats=[("US$334M", "gem, diamond and jewellery exports in 2025"), ("US$189M", "of that in gemstones"), ("75+", "gem varieties sourced in Sri Lanka")],
    stats_src=f'Source: Export Development Board,{ln("gem sector 2025", GEM_BLOG)}.',
    glance=[("Main products", "Blue sapphire, padparadscha, star and fancy sapphires, spinel, cat's eye, moonstone; small cut diamonds; gold jewellery"),
            ("Main markets", "US, Thailand, Switzerland, Hong Kong, UAE, India, France, UK, Singapore"),
            ("Export rules", "Cut and polished stones only; licensed dealers; inspection by the National Gem and Jewellery Authority and Customs"),
            ("Reports to ask for", "A government NGJA lab report or a recognised international lab report stating treatment and origin"),
            ("Watch for", "Heat treatment disclosure and country of origin")],
    products=[("Sapphires, cut and polished: blue, padparadscha, star and fancy", "7103.91"), ("Other gems, cut: spinel, cat's eye, alexandrite, moonstone, tourmaline", "7103.99"),
              ("Cut and polished diamonds, including small brilliants", "7102.39"), ("Gold and platinum jewellery", "7113.19"), ("Silver jewellery", "7113.11")],
    names=["Ceylon sapphire", "Sri Lankan sapphire", "padparadscha", "blue sapphire", "spinel"],
    evidence=[("Gem, diamond and jewellery exports earned US$334 million in 2025: gemstones US$189 million, diamonds US$127 million and jewellery US$17.8 million.", "EDB", GEM_BLOG),
              ("Ratnapura and Elahera are the main gem fields, and Sri Lanka exports Ceylon blue sapphire, padparadscha, star sapphires and fancy sapphires.", "EDB", GEM_TYPES),
              ("The Export Development Board ranks Sri Lanka as the ninth largest exporter of precious stones, with more than 75 varieties.", "EDB", "https://www.srilankabusiness.com/gem-diamond-and-jewellery/"),
              ("Sri Lanka is the second largest supplier of spinel to the world gem market.", "EDB", GEM_TYPES),
              ("Sri Lanka has no diamond mines; its diamond industry cuts imported rough and specialises in small diamonds.", "EDB gem report 2026", GEM_R),
              ("The National Gem and Jewellery Authority runs the main government gem testing laboratory, in Colombo and Ratnapura.", "EDB", "https://www.srilankabusiness.com/faq/gem-diamond-and-jewellery/exporters/gem-testing-labs-sri-lanka.html")],
    certs=[("NGJA dealer licence.", "Every gem exporter must hold an Official Gem Dealers Licence from the National Gem and Jewellery Authority, which keeps a registry of licensed dealers."),
           ("Export inspection.", "Gem exports are cleared under inspection by the National Gem and Jewellery Authority and Sri Lanka Customs."),
           ("Lab report.", "Not legally required for every shipment but recommended for commercial exports. A genuine report states treatments and, if you ask, origin."),
           ("Kimberley Process.", "Sri Lanka is a Kimberley Process participant, which covers trade in rough diamonds."),
           ("Treatment disclosure.", "In the US, sellers must disclose treatments that are not permanent or that affect value.")],
    caveats=[("Heat treatment is common. Pale geuda sapphire is heated to turn it blue, a practice dating from the 1970s, so ask for a report that says heated or no indication of heating.", "International Gem Society", "https://gemsociety.org/wp-content/uploads/2016/05/HEAT-TREATMENT-Geuda-Sapphire-Sri-Lanka.pdf"),
             ("Padparadscha is defined by colour, and only heat treatment is accepted. Beryllium diffused stones can imitate the colour, so insist on a lab report.", "International Gem Society", "https://www.gemsociety.org/gems/padparadscha-sapphire/"),
             ("About 70% of the stones Sri Lanka exports are foreign in origin. If origin matters to your customer, ask for an origin determination.", "EDB", GEM_BLOG),
             ("Gems cannot be sent as samples under the export procedure, so plan for inspected commercial shipments.", "EDB export procedure", EDB_PROC)],
    ask=["What is your NGJA dealer licence number?", "Will each stone come with a lab report stating treatment and origin, and from which lab?",
         "Were the stones mined in Sri Lanka, and can you show how you know?", "Who cut the stones, and can you recut to my specification?", "What are your return terms if a lab result differs?"],
    faqs=[("Can I buy rough gemstones from Sri Lanka?", "No. Only cut and polished gemstones may be exported; rough stones cannot legally leave Sri Lanka. Rough gems and diamonds can be imported duty free for cutting."),
          ("How do I check a Sri Lankan gem dealer?", "Buy from a dealer with a National Gem and Jewellery Authority dealer licence, which you can check in its registry, and ask for a report from the government NGJA laboratory or another recognised lab."),
          ("Are all gems exported from Sri Lanka mined there?", "No. The Export Development Board says about 70% of the stones exported are foreign in origin, and Sri Lanka has no diamond mines. Ask for an origin determination on the lab report."),
          ("What is a Ceylon sapphire?", "A sapphire mined in Sri Lanka, historically called Ceylon. Sri Lanka exports blue sapphire, padparadscha, star sapphires and fancy coloured sapphires, mainly from Ratnapura and Elahera.")],
)

cat(
    slug="graphite-minerals", label="Graphite and minerals", short="Vein graphite, ilmenite, quartz and mica.", art="s-minerals", seller="mineral exporter",
    h1="Sri Lanka vein graphite, ilmenite and quartz: mineral suppliers and export rules",
    title="Sri Lanka vein graphite and mineral suppliers: graphite, ilmenite, quartz",
    desc="Source natural vein graphite, ilmenite, rutile, zircon, vein quartz and mica from Sri Lanka. Grades, export licences, volumes and what to check before you buy.",
    answer=("Sri Lanka is the only country that commercially produces natural crystalline vein graphite, graded above 90% carbon, according to the Export "
            "Development Board. It also exports ilmenite, rutile and zircon from the Pulmoddai beach sand deposit, high purity vein quartz and mica. Volumes "
            "are small: about 4,000 tonnes of vein graphite in 2019 by US Geological Survey estimates. Raw and semi finished minerals need an export licence "
            "from the Geological Survey and Mines Bureau."),
    stats=[("90%+", "carbon in Sri Lankan vein graphite"), ("4,000 t", "vein graphite output, 2019 estimate"), ("98%+", "silica in high purity vein quartz")],
    stats_src=f'Sources: Export Development Board,{ln("mineral resources", MIN_BLOG)}; US Geological Survey,{ln("Minerals Yearbook 2019", USGS)}.',
    glance=[("Main products", "Vein graphite lump, chip and powder; ilmenite, rutile and zircon; vein quartz and silica sand; mica"),
            ("Main markets named by EDB", "UK, Eastern and Western Europe, US, India, Pakistan, China"),
            ("Licence", "Geological Survey and Mines Bureau export licence for raw and semi finished minerals"),
            ("Watch for", "Small volumes, export cess on raw forms, and full documentary checks")],
    products=[("Natural vein graphite, powder or flake", "2504.10"), ("Natural vein graphite, lump and chip", "2504.90"), ("Ilmenite", "2614.00"), ("Rutile", "2614.00"),
              ("Zircon", "2615.10"), ("Vein quartz", "2506.10"), ("Silica sand", "2505.10"), ("Mica, sheets and powder", "2525")],
    names=["vein graphite", "lump graphite", "Ceylon graphite", "mineral sands"],
    evidence=[("Sri Lanka is the only country that commercially produces natural crystalline vein graphite.", "EDB", "https://www.srilankabusiness.com/news/edb-eyes-expansion-of-sri-lanka-s-graphite-industry-to-boost-mineral-export-revenue.html"),
              ("Sri Lankan vein graphite is graded above 90% carbon.", "EDB", MIN_BLOG),
              ("Vein graphite output was about 4,000 tonnes in 2019, and ilmenite and leucoxene 43,779 tonnes.", "US Geological Survey", USGS),
              ("The Pulmoddai beach sand deposit north of Trincomalee is the main mineral sand source, and ilmenite is its main mineral.", "EDB", MIN_BLOG),
              ("High purity vein quartz with more than 98% silica is found in many districts, and white silica sand above 98% in Puttalam.", "EDB", MIN_BLOG)],
    certs=[("GSMB export licence.", "Minerals in raw and semi finished form need an export licence from the Geological Survey and Mines Bureau."),
           ("Export cess.", "Raw forms carry an export cess, for example Rs 4,400 a tonne on raw vein quartz, so check whether quotes include it."),
           ("Certificate of analysis.", "No national standard applies, so set carbon content, particle size and moisture in the contract and test with an independent lab.")],
    caveats=[("Graphite export volumes have fallen since 2015 while unit prices rose, according to a 2025 University of Moratuwa study of UN trade data.", "University of Moratuwa", "https://dl.lib.uom.lk/items/8c07a5d8-05cd-45ca-9e16-5fcc3c97446c/full"),
             ("A parliamentary inquiry in September 2025 found clear quartz being exported illegally and royalty collection failures, so do full documentary checks.", "Ada Derana", "https://adaderana.lk/news/112617/clear-quartz-illegally-exported-from-sri-lanka-cope-inquiry-finds")],
    ask=["Do you hold a Geological Survey and Mines Bureau export licence for this mineral?", "Which mine or deposit does the material come from?",
         "Can you supply an independent certificate of analysis for each lot?", "What monthly volume can you commit to, and at what particle sizes?", "Does your price include the export cess?"],
    faqs=[("What is Sri Lankan vein graphite?", "Natural crystalline graphite found in veins, which Sri Lanka is the only country to produce commercially. It is graded above 90% carbon and used in lubricants, carbon brushes, brake pads and refractories."),
          ("How much graphite does Sri Lanka produce?", "About 4,000 tonnes of vein graphite in 2019 by US Geological Survey estimates, so confirm capacity before you contract."),
          ("Can minerals be exported raw?", "Only under a Geological Survey and Mines Bureau export licence, and raw forms carry an export cess."),
          ("Where do Sri Lankan minerals go?", "The Export Development Board names the UK, Eastern and Western Europe, the US, India, Pakistan and China as the main markets.")],
)


# ================================================================ rubber, apparel and leather (group C)
RUB_R = "https://www.srilankabusiness.com/ebooks/industry-capability-report-rubber-2026.pdf"
TYRE_PAGE = "https://www.srilankabusiness.com/rubber/tyre-sector.html"
US_301 = "https://election.newsfirst.lk/2026/07/24/sri-lanka-among-17-economies-facing-10-us-tariff-under-section-301-action"
SLAEA_EXP = "https://www.srilanka-apparel.com/exports-performance/"
SLAEA_GB = "https://www.srilanka-apparel.com/giving-back/"
APP_R = "https://srilankabusiness.com/ebooks/industry-capability-report-apparel-2025.pdf"
FW_R = "https://www.srilankabusiness.com/ebooks/industry-capability-report-footwear-leather-2024.pdf"
FW_BRO = "https://www.srilankabusiness.com/pdf/footwear-and-leather-products-ebrochures-1.pdf"
US_TARIFF_CAVEAT = ("In July 2026 the US placed Sri Lanka in its 10% Section 301 tariff category, added on top of normal customs duties. Rates have changed several times since 2025, so check the current rate before you cost a landed price.", "News First", US_301)

cat(
    slug="industrial-tyres", label="Industrial and solid tyres", short="Solid forklift tyres, press on bands, OTR and agri tyres.", art="s-tyres", seller="tyre manufacturer",
    h1="Solid tyre manufacturers in Sri Lanka: forklift, industrial and OTR tyres",
    title="Solid tyre manufacturers in Sri Lanka: forklift and industrial tyres",
    desc="Source solid forklift tyres, press on bands, industrial, agricultural and off the road tyres from Sri Lankan manufacturers. Market share, HS codes, standards and how to buy.",
    answer=("Sri Lanka is the world's leading solid tyre exporter, with about 25% of world demand by the Export Development Board's estimate. Tyres and tubes "
            "earned US$522 million in 2025, the largest rubber product line, and solid tyres make up 61% of tyre export value. Manufacturers, including joint "
            "ventures with international tyre makers, also produce pneumatic and semi pneumatic tyres, tubes and retreading material. Solid tyres go mainly to "
            "the US and the EU; most pneumatic tyre exports go to Asia Pacific."),
    stats=[("~25%", "of world solid tyre demand, EDB estimate"), ("US$522M", "tyre and tube exports in 2025"), ("+7.67%", "tyres and tubes, January to September 2026")],
    stats_src=f'Sources: Export Development Board,{ln("rubber report 2026", RUB_R)}; EDB via{ln("Newswire", EDB9M)}.',
    glance=[("Main products", "Solid and resilient tyres for forklifts and material handling, press on bands, pneumatic agricultural, OTR and industrial tyres, tubes, retreading material"),
            ("Main markets", "US and EU for solid tyres, led by the US and Germany; Asia Pacific for pneumatic tyres"),
            ("Standards to ask for", "EU REACH documentation, ISO 9001, and test reports for your market"),
            ("Watch for", "US tariff changes and natural rubber price swings")],
    products=[("Solid and cushion tyres, including forklift tyres and press on bands", "4012.90"), ("Retreaded pneumatic tyres", "4012.11 to 4012.19"),
              ("New pneumatic tyres for agricultural and forestry machines", "4011.70"), ("New pneumatic tyres for construction, mining and industrial handling", "4011.80"),
              ("New pneumatic tyres for buses and lorries", "4011.20"), ("Inner tubes", "4013")],
    names=["forklift tyres", "solid resilient tyres", "press on bands", "OTR tyres", "industrial tyres"],
    evidence=[("The Export Development Board describes Sri Lanka as the leading solid tyre exporter in the world, at about 25% of world demand.", "EDB rubber report 2026", RUB_R),
              ("Tyres and tubes earned US$522 million of the US$915 million rubber finished products total in 2025.", "EDB rubber report 2026", RUB_R),
              ("Solid tyres account for 61% of tyre export value and new pneumatic tyres for 38%.", "EDB", TYRE_PAGE),
              ("The industry includes joint ventures between Sri Lankan companies and international tyre makers, and also produces pneumatic and semi pneumatic tyres, tubes and retreading material.", "EDB", TYRE_PAGE),
              ("Pneumatic and retreaded tyre and tube exports reached US$54.95 million in September 2026, up 39.57% on a year earlier.", "EDB via Newswire", EDB9M)],
    certs=[("EU REACH.", "The Export Development Board says Sri Lankan tyres are made under EU REACH rules. Ask each supplier for its substances of very high concern declaration."),
           ("ISO 9001 and ISO 14001.", "Ask for current certificates for the plant that will make your tyres."),
           ("Test reports for your market.", "Load and speed ratings, and E-mark or DOT marking where your market requires it for pneumatic tyres.")],
    caveats=[("The Export Development Board's own estimate of Sri Lanka's solid tyre share ranges from 14% to about 25% across its documents. Treat it as an estimate.", "EDB rubber report 2017", "https://www.srilankabusiness.com/ebooks/2017-06-industry-capability-report-sri-lankan-rubber.pdf"),
             ("Tyre and tube exports fell to US$522 million in 2025 from US$599 million in 2024, before rising again in 2026.", "EDB rubber report 2026", RUB_R),
             US_TARIFF_CAVEAT],
    ask=["Which tyre sizes, compounds and load ratings do you make, including non marking compounds?", "Do you make press on bands and resilient tyres for my machine models?",
         "Can you provide REACH declarations and test reports for my market?", "What is the minimum order per size, and the lead time for a mixed container?", "Do you offer private label or my own branding on the sidewall?"],
    faqs=[("What HS code covers solid forklift tyres?", "Solid and cushion tyres, including press on bands, come under HS 4012.90. New pneumatic tyres for industrial handling machines are 4011.80 and for agricultural machines 4011.70. Confirm the national tariff line with your customs broker."),
          ("Which countries buy Sri Lankan solid tyres?", "The Export Development Board names the US and EU countries as the main buyers. UN trade data for 2025 show exports in the tyre group that includes solid tyres of US$140.24 million to the US and US$39.52 million to Germany."),
          ("Does Sri Lanka also make pneumatic tyres?", "Yes. Manufacturers also make pneumatic and semi pneumatic tyres, tubes and retreading material, and most pneumatic tyre exports go to Asia Pacific."),
          ("Do Sri Lankan tyres meet EU chemical rules?", "The Export Development Board says they are made under EU REACH regulation. Ask each supplier for its own REACH documentation and test reports.")],
    tender="Ports, public fleets and utilities buy industrial tyres through tenders. Tender Radar matches them to your sizes and compounds.",
)

cat(
    slug="rubber-gloves", label="Rubber gloves and rubber products", short="Examination, surgical, industrial and household gloves, seals, mats.", art="s-gloves", seller="glove manufacturer",
    h1="Rubber glove manufacturers in Sri Lanka: examination, surgical, industrial and household gloves",
    title="Rubber glove manufacturers in Sri Lanka: latex, surgical and industrial",
    desc="Source latex examination and surgical gloves, industrial and household gloves, seals, gaskets and mats from Sri Lankan rubber product manufacturers. Standards, HS codes and markets.",
    answer=("Sri Lanka exported US$293 million of industrial and surgical rubber gloves in 2025, its second largest rubber product line after tyres, and glove "
            "exports rose 34.38% in September 2026. Manufacturers make gloves for healthcare, industrial, household and agricultural use, as well as seals, "
            "gaskets, washers, mats, rubber bands and hoses, using Sri Lankan natural rubber including latex crepe. About 75 rubber product exporters are "
            "registered with the Board of Investment. For medical gloves in the UK or EU, ask for EN 455 test reports."),
    stats=[("US$293M", "industrial and surgical glove exports in 2025"), ("+34.38%", "glove exports, September 2026"), ("~75", "rubber product exporters registered with the BOI")],
    stats_src=f'Sources: Export Development Board,{ln("rubber report 2026", RUB_R)}; EDB via{ln("Newswire", EDB9M)}.',
    glance=[("Main products", "Latex examination and surgical gloves, industrial and household gloves, seals, gaskets and washers, rubber mats, bands, hoses"),
            ("Largest markets in 2025", "US, Germany, UK and India for rubber gloves and apparel articles; Italy, Belgium, France and Canada also named by EDB"),
            ("Standards to ask for", "EN 455 parts 1 to 4 and AQL for medical gloves; EN ISO 374 for chemical protection; ISO 9001 and ISO 14001"),
            ("Watch for", "Natural rubber price swings and the cost of testing")],
    products=[("Medical, surgical and examination gloves", "4015.12"), ("Household and industrial rubber gloves", "4015.19"), ("Other rubber apparel and accessories", "4015.90"),
              ("Gaskets, washers and seals", "4016.93"), ("Rubber floor coverings and mats", "4016.91"), ("Other articles of vulcanised rubber, including bands and sealing rings", "4016.99")],
    names=["latex gloves", "examination gloves", "surgical gloves", "household gloves", "rubber gaskets"],
    evidence=[("Industrial and surgical rubber gloves earned US$293 million in 2025, the second largest rubber product line after tyres.", "EDB rubber report 2026", RUB_R),
              ("Sri Lankan gloves cover industrial, household, agricultural and healthcare uses.", "EDB rubber brochure", "https://www.srilankabusiness.com/pdf/rubber-products-ebrochures-1.pdf"),
              ("Sri Lanka produces a full range of natural rubber grades, including latex crepe, ribbed smoked sheets and centrifuged latex.", "EDB rubber report 2026", RUB_R),
              ("Around 75 rubber product export companies are registered with the Board of Investment.", "EDB rubber report 2026", RUB_R),
              ("Glove exports reached US$31.70 million in September 2026, up 34.38%, and gaskets, washers and seals rose 27.78% in January to September.", "EDB via Newswire", EDB9M)],
    certs=[("EN 455 and AQL.", "For medical gloves in the UK and EU: EN 455 parts 1 to 4, typically with an AQL of 1.5 for freedom from holes. Ask for the test reports."),
           ("CE or UKCA marking.", "Required for medical and protective gloves sold in the EU and UK, with the notified body number where it applies."),
           ("ISO 9001 and ISO 14001.", "Ask for current certificates for the plant that will make your order.")],
    caveats=[("The Export Development Board lists the high cost of testing and certification as a sector weakness, so confirm which certificates a factory already holds.", "EDB rubber report 2026", RUB_R),
             ("Natural rubber supply and prices swing; the Export Development Board lists inadequate raw material and price fluctuations as weaknesses.", "EDB rubber report 2026", RUB_R),
             US_TARIFF_CAVEAT],
    ask=["Which glove types, materials, sizes and thicknesses do you make?", "Can you share EN 455 test reports from an accredited lab, and your AQL levels?",
         "Is the glove CE or UKCA marked, and which notified body is involved?", "What are your monthly capacity and lead times?", "Do you pack under private label?"],
    faqs=[("Which HS codes apply to rubber gloves?", "Medical, surgical and examination gloves of vulcanised rubber are HS 4015.12. Household and industrial rubber gloves are 4015.19. Gaskets and seals are 4016.93 and rubber mats 4016.91."),
          ("What kinds of gloves does Sri Lanka export?", "Gloves for industrial, household, agricultural and healthcare use. Industrial and surgical gloves earned US$293 million in 2025."),
          ("Which standards should I ask a glove supplier for?", "For medical gloves sold in the UK or EU, EN 455 test reports and CE or UKCA marking. For chemical protection, EN ISO 374. Ask which certificates the factory already holds before you order."),
          ("Where do Sri Lankan rubber gloves go?", "UN trade data for 2025 show rubber apparel articles, mostly gloves, worth US$74.28 million to the US, US$25.56 million to Germany, US$17.05 million to the UK and US$16.20 million to India.")],
    tender="Health systems, UN agencies and public buyers tender for examination and surgical gloves to EN 455. Tender Radar sends you the ones that fit.",
)

cat(
    slug="apparel-manufacturing", label="Apparel and textiles", short="Activewear, intimates, swimwear, workwear and fabrics.", art="s-apparel", seller="apparel manufacturer",
    h1="Apparel manufacturers in Sri Lanka: activewear, intimates, swimwear and workwear",
    title="Apparel and clothing manufacturers in Sri Lanka: buyer's guide (2026)",
    desc="Find clothing and garment manufacturers in Sri Lanka for activewear, lingerie, swimwear, workwear, uniforms and children's wear. Certifications, markets, LEED factories and how to start.",
    answer=("Apparel is Sri Lanka's largest export, at US$4.91 billion for apparel and textiles in 2025. Manufacturers make sportswear and activewear, lingerie "
            "and intimate wear, swimwear, loungewear, bridal wear, workwear and children's wear, mostly for the US, the EU and the UK. The industry sells on "
            "ethical and green manufacturing: 17 factories are LEED certified, and Garments Without Guilt certifies labour standards. Exports are down 5.68% "
            "in the first nine months of 2026 as US and EU demand softened, which means capacity for new buyers."),
    stats=[("US$4.91B", "apparel and textile exports in 2025"), ("17", "LEED certified apparel factories"), ("US$1.95B", "apparel exports to the US in 2025")],
    stats_src=f'Sources: Export Development Board,{ln("2025 export performance", EDB25)}; Sri Lanka Apparel Exporters Association,{ln("export tables", SLAEA_EXP)} and{ln("certifications", SLAEA_GB)}.',
    glance=[("Main products", "Activewear and sportswear, lingerie and intimate wear, swimwear, loungewear, bridal wear, workwear, children's wear, knitted fabric"),
            ("Largest markets in 2025", "US (US$1.95 billion), EU (US$1.58 billion), UK (US$680 million)"),
            ("Certifications common in the industry", "Garments Without Guilt, WRAP, GOTS, Fair Trade, Higg Index, LEED, ISO 9001"),
            ("Watch for", "Most factories are small and medium firms, so capacity and compliance vary")],
    products=[("Knitted apparel", "Chapter 61"), ("Woven apparel", "Chapter 62"), ("Bras, intimate wear and lingerie", "6212"), ("Track suits, activewear and swimwear", "6112"),
              ("Other made up textile articles", "Chapter 63"), ("Knitted and crocheted fabric", "Chapter 60")],
    names=["garment manufacturers", "clothing manufacturers", "intimate apparel", "activewear", "uniforms"],
    evidence=[("17 Sri Lankan apparel manufacturing facilities are LEED certified.", "Sri Lanka Apparel Exporters Association", SLAEA_GB),
              ("Sri Lanka has the world's first manufacturing facility certified Net Zero Carbon.", "Board of Investment", "https://investsrilanka.com/home/why-sri-lanka/aperal_subpage/"),
              ("The range covers sportswear, lingerie, loungewear, bridal wear, workwear, swimwear and children's wear.", "EDB apparel report 2025", APP_R),
              ("The industry commits to ethical manufacturing, free of discrimination, sweatshop practices and child labour, under the Garments Without Guilt banner.", "EDB apparel report 2025", APP_R),
              ("In 2025 Sri Lanka exported US$1.95 billion of apparel to the US, US$1.58 billion to the EU and US$680 million to the UK.", "Sri Lanka Apparel Exporters Association", SLAEA_EXP)],
    certs=[("Garments Without Guilt.", "An ethical compliance certification issued by the Joint Apparel Association Forum."), ("WRAP.", "Compliance with lawful, humane and ethical manufacturing."),
           ("GOTS, Fair Trade and Higg Index.", "Listed among certifications held across the industry; ask which apply to the factory you use."),
           ("LEED and carbon neutral certification.", "For brands that report on factory emissions."), ("ISO 9001 and ISO 14001.", "Quality and environmental management.")],
    caveats=[("Apparel and textile exports fell 5.68% in January to September 2026, linked to weaker demand in the US and EU.", "EDB via Newswire", EDB9M),
             ("Most export clothing factories are small and medium firms spread across the country, so capacity and compliance vary widely between suppliers.", "EDB apparel report 2025", APP_R),
             US_TARIFF_CAVEAT],
    ask=["Which product categories and fabrics do you specialise in, and for which markets?", "What are your minimum order quantities per style and colour?",
         "Which certifications does the factory hold, and can I see the latest social audit?", "Do you handle development and sampling in house?", "Where do you source fabric and trims, and can you work with my nominated mills?"],
    faqs=[("How do I find an apparel manufacturer in Sri Lanka?", "Start from the product: activewear, intimates, swimwear, workwear or children's wear. The Sri Lanka Apparel Exporters Association's member directory can be filtered by product, or tell us your category, volumes and target price and we will introduce manufacturers who fit."),
          ("What does Sri Lanka's apparel industry specialise in?", "Sportswear and activewear, lingerie and intimate wear, loungewear, bridal wear, workwear, swimwear and children's wear, according to the Export Development Board."),
          ("What is Garments Without Guilt?", "An ethical compliance certification issued by the Joint Apparel Association Forum, covering labour standards in Sri Lankan apparel factories."),
          ("Which markets buy the most Sri Lankan apparel?", "In 2025 the US took US$1.95 billion, the EU US$1.58 billion and the UK US$680 million.")],
    tender="Uniform and workwear contracts from public services, health systems and UN agencies go out to tender. Tender Radar matches them to what you make.",
)

cat(
    slug="leather-footwear", label="Footwear and leather goods", short="Shoes, safety boots, sole crepe and leather goods.", art="s-leather", seller="footwear manufacturer",
    h1="Footwear and leather goods manufacturers in Sri Lanka",
    title="Shoe and leather goods manufacturers in Sri Lanka: buyer's guide",
    desc="Source shoes, safety footwear, rubber boots, thongs, sole crepe soles and leather goods from Sri Lankan manufacturers. Capacity, materials, markets and what to check.",
    answer=("Sri Lanka's footwear industry can make 25 to 35 million pairs a year, plus 30 to 35 million pairs of rubber thongs, according to the Export "
            "Development Board. It makes leather and canvas shoes, safety shoes, rubber boots and sports shoes, and small leather goods such as wallets, "
            "belts and bags. Sri Lanka is the only producer of sole crepe, a natural rubber used for unit soles. The sector is small, at US$46.4 million of "
            "exports in 2023, and most leather is imported, so check materials and capacity early."),
    stats=[("25 to 35M", "pairs of footwear a year, capacity estimate"), ("Only", "producer of natural sole crepe"), ("~15 days", "sailing time from Colombo to London")],
    stats_src=f'Source: Export Development Board,{ln("footwear and leather report 2024", FW_R)}.',
    glance=[("Main products", "Leather shoes, safety shoes, sports and canvas shoes, rubber boots, thongs, unit soles, wallets, belts, bags"),
            ("Main markets", "US, UK, Italy, Germany and other EU countries"), ("Materials", "Mostly imported leather; Sri Lankan natural rubber and sole crepe"),
            ("Watch for", "Limited leather supply and a smaller supplier base than apparel")],
    products=[("Footwear with leather uppers, including safety shoes", "6403"), ("Rubber and plastic footwear, including thongs and boots", "6402"), ("Textile upper footwear, including canvas shoes", "6404"),
              ("Footwear parts, uppers and soles", "6406"), ("Travel bags, handbags, wallets and purses", "4202"), ("Leather gloves and garments", "4203")],
    names=["shoe manufacturers", "safety shoes", "flip flops", "crepe soles", "leather goods"],
    evidence=[("Sri Lanka is the only producer of sole crepe, a natural rubber used for unit soles.", "EDB footwear brochure", FW_BRO),
              ("Footwear capacity is estimated at 25 to 35 million pairs a year, plus 30 to 35 million pairs of rubber thongs.", "EDB footwear report 2024", FW_R),
              ("Sailing time from Colombo to London is about 15 days.", "EDB footwear report 2024", FW_R),
              ("Value addition in the footwear sector is 35% to 45%.", "EDB footwear report 2024", FW_R),
              ("Sri Lanka has five chrome leather tanneries and one vegetable leather tannery.", "EDB footwear report 2024", FW_R)],
    certs=[("Social compliance audit.", "The Export Development Board cites adherence to international labour practices; ask for the factory's latest audit."),
           ("Safety footwear standard.", "For safety shoes, ask for test reports to the standard your market uses, such as EN ISO 20345."),
           ("Material declarations.", "Leather origin and chemical compliance, such as REACH for the EU.")],
    caveats=[("Most leather goods are made from imported leather because local supply of tanned leather is inadequate.", "EDB footwear report 2024", FW_R),
             ("Exports fell from US$140 million in 2016 to US$46.4 million in 2023, so the supplier base is small.", "EDB footwear report 2024", FW_R),
             ("Most sole makers serve only their own shoe production, so independent component capacity is limited.", "EDB footwear report 2024", FW_R)],
    ask=["Which footwear types and constructions do you make?", "Where does your leather come from, and can you document it?", "What is the minimum order per style and size run?",
         "Do you have test reports for safety footwear in my market?", "Can you use sole crepe or natural rubber soles for my range?"],
    faqs=[("What footwear and leather products does Sri Lanka export?", "Canvas and rubber boots, thongs, sports shoes, leather shoes and safety shoes, plus small leather goods such as gloves, wallets, bags, purses and belts."),
          ("Is the leather made in Sri Lanka?", "Mostly not. The Export Development Board says the bulk of leather products are made from imported leather, which comes in duty free."),
          ("What is sole crepe?", "A natural rubber used to make unit soles. Sri Lanka is its only producer."),
          ("How big is the footwear sector?", "Small: US$25.93 million of footwear and US$20.47 million of leather products in 2023, with capacity for 25 to 35 million pairs a year.")],
)


# ================================================================ plantation, spice and herbal (group A)
TEA_FT25 = "https://www.ft.lk/front-page/Tea-exports-top-1-5-b-in-2025-despite-price-pressures/44-787299"
TEA_FT24 = "https://www.ft.lk/front-page/Tea-exports-garner-1-43-b-on-245-5-m-kilos-in-2024/44-772138"
TEA_LOGO = "https://www.srilankabusiness.com/tea/about-tea/ceylon-tea-logo.html"
TEA_CAP = "https://www.srilankabusiness.com/tea/about-tea/industry-capability.html"
TEA_AUC = "https://www.srilankabusiness.com/tea/the-tea-auction.html"
TEA_EDB = "https://www.srilankabusiness.com/tea/"
CIN_GI = "https://www.srilankabusiness.com/spices/ceylon-cinnamon-geographical-indication.html"
CIN_EU = "https://eur-lex.europa.eu/eli/reg_impl/2022/144/oj/eng"
CIN_CAP = "https://www.srilankabusiness.com/spices/about/industry-capability.html"
CIN_GRADE = "https://www.srilankabusiness.com/spices/about/cinnamon-cultivation-sri-lanka.html"
CIN_SLS = "https://faolex.fao.org/docs/pdf/srl133795.pdf"
CIN_MX = "https://www.srilankabusiness.com/pdfs/market-profiles/2026/mexico-2026.pdf"
CIN_PRICE = "https://www.dailymirror.lk/business/Sri-Lanka-targets-US-300mn-in-cinnamon-exports-as-Alba-price-hits-record-Rs-7-500/215-346480"
SPICE_EDB = "https://www.srilankabusiness.com/spices/"
SPICE_MKT = "https://www.srilankabusiness.com/spices/major-export-markets.html"
SPICE_DOCS = "https://srilankabusiness.com/spices/pure-ceylon-cinnamon.html"
AYU_WS = "https://www.srilankabusiness.com/news/edb-hosts-successful-workshop-on-developing-ayurvedic-and-herbal-cosmetic-products-for-export.html"
AYU_MKT = "https://www.srilankabusiness.com/emarketplace/ayurvedic"

cat(
    slug="ceylon-tea", label="Ceylon tea", short="Bulk, packets, tea bags, green, white and instant tea.", art="s-tea", seller="tea exporter",
    h1="Ceylon tea suppliers and exporters in Sri Lanka: bulk, packets and private label",
    title="Ceylon tea suppliers and exporters: bulk, wholesale and private label",
    desc="Buy Ceylon tea in bulk, packets, tea bags or private label from Sri Lankan tea exporters. The Lion logo, the Colombo auction, grades by elevation, certificates and markets.",
    answer=("Sri Lanka exported US$1.51 billion of tea in 2025, about 257 million kilograms, and supplied 13% of the world's tea exports in 2024. Ceylon tea is "
            "grown in seven regions and graded by elevation, and about 93% is made by orthodox methods. Most of it is sold through the Colombo Tea Auction, which "
            "runs every Tuesday and Wednesday. Exporters supply bulk tea, packets, tea bags, green, white and instant tea, and 59% of exports in 2025 were value "
            "added. Only 100% Ceylon tea packed in Sri Lanka may carry the Sri Lanka Tea Board's Lion logo."),
    stats=[("US$1.51B", "tea exports in 2025, up 4.97%"), ("13%", "of world tea exports in 2024"), ("59%", "of 2025 tea exports in value added form")],
    stats_src=f'Sources: Export Development Board,{ln("2025 exports", EDB25)} and{ln("tea sector", TEA_EDB)}; Daily FT,{ln("2025 tea exports", TEA_FT25)}.',
    glance=[("Main products", "Bulk black tea, tea packets, tea bags, green and white tea, instant tea, iced tea and concentrates"),
            ("Largest markets in 2025 by volume", "Iraq, Russia, Turkiye, Libya, UAE, Chile, China, Iran, Azerbaijan, Saudi Arabia"),
            ("Grades", "High grown from 1,200 m, medium grown 600 to 1,200 m, low grown below 600 m, across seven regions"),
            ("Standards", "ISO 3720 minimum; ISO 22000; organic to EU, USDA NOP and JAS; Rainforest Alliance and Fairtrade available"),
            ("Watch for", "Tea exports are down 6.83% in 2026 and production is tight")],
    products=[("Black tea in bulk, packs over 3 kg", "0902.40"), ("Tea packets and tea bags, packs up to 3 kg", "0902.30"), ("Green tea", "0902.10 and 0902.20"),
              ("Instant tea and extracts", "2101.20"), ("White, oolong, organic, decaffeinated and flavoured tea", "0902")],
    names=["Ceylon black tea", "Sri Lankan tea", "orthodox tea", "tea bags", "private label tea"],
    evidence=[("Sri Lanka supplied 13% of global tea exports in 2024.", "EDB", TEA_EDB),
              ("Tea exports reached 257.44 million kg in 2025, worth US$1.51 billion at an average FOB of US$5.85 a kg.", "Daily FT", TEA_FT25),
              ("The Colombo Tea Auction runs every Tuesday and Wednesday and sells about 6.5 million kg a week.", "EDB", TEA_AUC),
              ("Ceylon tea is grown in seven regions, including Nuwara Eliya, Uva and Dimbula, and graded by elevation.", "EDB", TEA_CAP),
              ("About 93% of Ceylon tea is made by orthodox and artisanal methods, handpicked as two leaves and a bud.", "EDB", TEA_CAP),
              ("Value added segments reached 59% of tea exports in 2025, an 11 year high.", "Daily FT", TEA_FT25)],
    certs=[("Lion logo.", "Owned by the Sri Lanka Tea Board; only for 100% Ceylon tea packed in Sri Lanka by a licensed packer. Blends do not qualify."),
           ("ISO 3720.", "The minimum product standard for Ceylon black tea."), ("ISO 22000.", "Food safety; the Export Development Board says Ceylon tea meets the ISO 22000 series and EU health and safety rules."),
           ("Organic.", "EU organic, USDA NOP, JAS and NASAA certification is available in the industry."), ("Rainforest Alliance, Fairtrade and Ethical Tea Partnership.", "Listed as industry partnerships; check the estate or factory you buy from.")],
    caveats=[("Tea earnings fell 6.83% in January to September 2026, with bulk tea down 11.13%; tea bags rose 53.39%.", "EDB via Newswire", EDB9M),
             ("2024 production was 262 million kg, below the industry's stated capacity, so supply of some grades is tight.", "Daily FT", TEA_FT24),
             ("If you blend or pack outside Sri Lanka, you cannot use the Lion logo.", "EDB", TEA_LOGO)],
    ask=["Which regions and elevations do you buy from, and can you match my blend?", "Do you buy at the Colombo auction, and how do you price forward contracts?",
         "Are you a licensed packer for the Lion logo?", "Which certificates do you hold: ISO 22000, organic, Rainforest Alliance?", "What is your minimum order for private label packs or tea bags?"],
    faqs=[("What does the Lion logo on Ceylon tea guarantee?", "The Sri Lanka Tea Board owns it. It can only appear on packs of 100% pure Ceylon tea, packed in Sri Lanka by a licensed packer and meeting Tea Board quality standards. A blend does not qualify, even at 95% Ceylon tea."),
          ("In what formats can I buy Ceylon tea?", "Bulk tea, tea packets, tea bags and instant tea, in black, green, white and oolong, with organic, decaffeinated and flavoured versions. In 2025 packets were about 45% of export volume and bulk tea 106.8 million kg."),
          ("How is Ceylon tea traded?", "Most tea is sold at the Colombo Tea Auction every Tuesday and Wednesday, about 6.5 million kg a week. Exporters buy at auction and sell to overseas buyers in bulk, packed or private label form."),
          ("Which countries buy the most Ceylon tea?", "By volume in 2025: Iraq, Russia, Turkiye, Libya and the UAE, followed by Chile, China, Iran, Azerbaijan and Saudi Arabia. The Middle East and North Africa took half of exports in 2024.")],
    tender="Government and institutional tea purchases go out to tender in several markets. Tender Radar sends you the ones that fit your grades and certificates.",
)

cat(
    slug="ceylon-cinnamon", label="Ceylon cinnamon", short="Alba quills, powder, cut sticks, leaf and bark oil.", art="s-cinnamon", seller="cinnamon exporter",
    h1="Ceylon cinnamon suppliers and exporters in Sri Lanka: Alba quills, powder and oils",
    title="Ceylon cinnamon suppliers and exporters: wholesale, bulk and Alba grade",
    desc="Buy true Ceylon cinnamon wholesale from Sri Lankan exporters: Alba and Continental quills, cut sticks, powder, leaf and bark oil. EU PGI, SLS standard, grades, HS codes and markets.",
    answer=("Sri Lanka is the world's largest producer and exporter of true cinnamon, Cinnamomum zeylanicum, and Ceylon cinnamon has been a protected "
            "geographical indication in the EU since February 2022. Cinnamon exports reached US$221.56 million in the first nine months of 2026, up 31%. Quills "
            "are graded by diameter into Alba, Continental, Mexican and Hamburg, and every export of quills, chips and powder must meet the national standard SLS "
            "81:2010 with a clearance certificate. The largest markets are Mexico, the US and Peru."),
    stats=[("US$221.56M", "cinnamon exports, January to September 2026"), ("+31%", "on a year earlier"), ("2022", "EU protected geographical indication")],
    glance=[("Main products", "Quills by grade, quillings, featherings and chips, cut quills, powder, leaf oil, bark oil, oleoresin"),
            ("Grades", "Alba (thinnest, about 6 mm), Continental, Mexican, Hamburg"),
            ("Largest markets", "Mexico, US, Peru, then Colombia, Ecuador, Bolivia, Guatemala, Chile, Spain"),
            ("Mandatory for export", "SLS 81:2010 conformity and a Sri Lanka Standards Institution clearance certificate"),
            ("Watch for", "Record raw material prices in 2026 as demand climbs")],
    products=[("Cinnamon quills, cut quills, quillings, featherings and chips", "0906.11"), ("Other whole cinnamon", "0906.19"), ("Crushed cinnamon", "0906.20.10"),
              ("Ground cinnamon powder", "0906.20.20"), ("Cinnamon leaf oil", "3301.90.30"), ("Cinnamon bark oil", "3301.90.40"), ("Cinnamon oleoresin", "3301.90.10")],
    names=["true cinnamon", "Ceylon cinnamon sticks", "Alba cinnamon", "C5 cinnamon", "Cinnamomum zeylanicum"],
    evidence=[("The EU registered Ceylon cinnamon as a protected geographical indication under Regulation (EU) 2022/144, Sri Lanka's first.", "EUR-Lex", CIN_EU),
              ("The PGI mark covers cut quills, powder, leaf oil and bark oil made only from 100% Ceylon cinnamon grown and processed in Sri Lanka.", "EDB", CIN_GI),
              ("The Export Development Board says Sri Lanka is the largest producer and exporter of cinnamon, with 90% of the global market.", "EDB", "https://srilankabusiness.com/news/ceylon-cinnamon-receives-geographical-indication-certification-from-the-european-union.html"),
              ("Quills are graded by diameter into Alba, Continental, Mexican and Hamburg; Alba, the most expensive, has a 6 mm quill.", "EDB", CIN_GRADE),
              ("Since 2014, quills, chips and crushed or ground cinnamon can only be exported if they meet SLS 81:2010 and carry a Sri Lanka Standards Institution clearance certificate.", "Gazette 1813/15", CIN_SLS),
              ("Cinnamon exports to Mexico were US$91.0 million in 2025, the top product Sri Lanka ships there.", "EDB Mexico profile", CIN_MX)],
    certs=[("SLS 81:2010 clearance.", "Mandatory for every export of quills, chips and powder."), ("EU PGI mark.", "Licensed to members of the Ceylon cinnamon PGI association for value added packs."),
           ("Pure Ceylon Cinnamon trademark.", "Registered in the EU, Mexico, the US, Peru and Colombia to set it apart from cassia."),
           ("Certificate of origin, quarantine and quality certificates.", "Standard documents for spice exports."), ("GMP, HACCP, ISO 22000 and organic.", "Ask which the processor holds; organic cinnamon has its own tariff lines.")],
    caveats=[("Farm gate Alba prices hit a record Rs 7,500 a kg in July 2026 as demand climbed, so lock prices and volumes early.", "Daily Mirror", CIN_PRICE),
             ("Share figures depend on whether cassia is counted and on the year: the Export Development Board says 90% of the global market, but an older EDB page gives 41% of world cinnamon exports.", "EDB", "https://www.srilankabusiness.com/spices/ceylon-cinnamon-as-spice.html"),
             ("Ceylon cinnamon is sold as low in coumarin, but no figure is published, so ask for lab results if you need a coumarin limit.", "EDB", "https://www.srilankabusiness.com/spices/ceylon-cinnamon-as-spice.html")],
    ask=["Which grades can you supply each month, and at what moisture?", "Can you share the SLS clearance certificate and a recent lab report, including coumarin?",
         "Are you a member of the PGI association, if I want the PGI mark on retail packs?", "Do you process powder in house, and is it sterilised?", "Which organic and food safety certificates do you hold?"],
    faqs=[("What is Alba grade cinnamon?", "The thinnest and most expensive grade of Ceylon cinnamon quill, with a diameter of about 6 mm. The other quill grades, by increasing diameter, are Continental, Mexican and Hamburg."),
          ("How do I import Ceylon cinnamon in bulk?", "Agree grade, moisture and packing with an exporter, who obtains the Sri Lanka Standards Institution clearance under SLS 81:2010 and a certificate of origin. Then check your own market's food rules. Tell us your grade and volume and we will introduce exporters."),
          ("How can I tell Ceylon cinnamon from cassia?", "Ceylon cinnamon is Cinnamomum zeylanicum. Packs with the EU PGI mark must contain 100% Ceylon cinnamon grown and processed in Sri Lanka, and the Pure Ceylon Cinnamon trademark is registered in the EU, Mexico, the US, Peru and Colombia."),
          ("Which HS codes cover Ceylon cinnamon?", "Quills, quillings, featherings and chips are 0906.11, crushed cinnamon 0906.20.10, powder 0906.20.20, leaf oil 3301.90.30 and bark oil 3301.90.40.")],
)

cat(
    slug="spices-essential-oils", label="Spices and essential oils", short="Pepper, cloves, nutmeg, cardamom, oils and oleoresins.", art="s-spices", seller="spice exporter",
    h1="Sri Lankan spice exporters: black pepper, cloves, nutmeg, essential oils and oleoresins",
    title="Sri Lankan spice exporters: pepper, cloves, nutmeg and essential oils",
    desc="Source Ceylon black pepper, cloves, nutmeg and mace, cardamom, essential oils and oleoresins from Sri Lankan spice exporters. HS codes, markets, documents and what to check.",
    answer=("Sri Lanka exported US$449.9 million of spices, essential oils and oleoresins in 2025, and the sector grew 30.53% in the first nine months of 2026, "
            "with pepper up 61% to US$136.26 million. Beyond cinnamon, exporters supply black pepper, cloves, nutmeg and mace, cardamom, ginger and turmeric, "
            "and essential oils and oleoresins from four main distilleries and about 170 field units. Pepper, cloves, nutmeg and cardamom are sold under the "
            "Ceylon Spices geographical indication. Most spices ship in bulk, unprocessed form."),
    stats=[("US$449.9M", "spices and essential oils in 2025"), ("+61.45%", "pepper exports, January to September 2026"), ("~6%", "of world pepper demand")],
    stats_src=S2(f' Pepper share: Export Development Board,{ln("spice capability", CIN_CAP)}.'),
    glance=[("Main products", "Black and white pepper, cloves, nutmeg and mace, cardamom, ginger, turmeric, curry mixes, essential oils, oleoresins"),
            ("Main markets named by EDB", "India, Germany, the US and the UAE for pepper and cloves; the US, India and Europe for oils"),
            ("Documents", "Certificate of origin, quarantine certificate and quality certificate"),
            ("Watch for", "Sharp swings in price and availability from year to year")],
    products=[("Black pepper, whole", "0904.11"), ("Pepper, crushed or ground", "0904.12"), ("Cloves", "0907.10"), ("Nutmeg", "0908.11 and 0908.12"), ("Mace", "0908.21 and 0908.22"),
              ("Cardamom", "0908.31 and 0908.32"), ("Ginger and turmeric", "0910.11 to 0910.30"), ("Essential oils: citronella, clove, nutmeg, pepper, cardamom", "3301.90"), ("Spice oleoresins", "3301.90.10")],
    names=["Ceylon pepper", "Ceylon cloves", "citronella oil", "clove oil", "nutmeg oil"],
    evidence=[("Spices, essential oils and oleoresins earned US$449.91 million on 40,302 tonnes in 2025.", "EDB", SPICE_EDB),
              ("Ceylon pepper, cloves, nutmeg and cardamom are branded under the Ceylon Spices geographical indication.", "EDB", SPICE_EDB),
              ("Sri Lanka supplies about 6% of world pepper demand, and its pepper has a high piperine level.", "EDB", CIN_CAP),
              ("Sri Lanka is among the top ten clove exporters, producing about 5,301 tonnes a year.", "EDB", CIN_CAP),
              ("Essential oils come from four main distilleries, 12 small and medium distilleries and nearly 170 field distillation units.", "EDB", CIN_CAP),
              ("Pepper exports rose 61.45% to US$136.26 million in January to September 2026.", "EDB via Newswire", EDB9M)],
    certs=[("Certificate of origin, quarantine and quality certificates.", "The standard set for spice exports."), ("GMP, HACCP and ISO 22000.", "Ask which the processor holds."),
           ("Organic.", "Separate tariff lines exist for organic pepper, cloves and nutmeg; ask for the certificate and its scope."),
           ("Your market's residue limits.", "Agree pesticide residue and aflatoxin testing in the contract.")],
    caveats=[("Earnings swing sharply: spices fell 2.59% in 2025, then rose 30.53% in January to September 2026. Expect price and availability to move.", "EDB via Newswire", EDB9M),
             ("Cardamom volumes are small, about 320 tonnes a year.", "EDB", CIN_CAP),
             ("Most spices ship in bulk, unprocessed form; confirm cleaning, sterilising and grinding capability if you need it.", "EDB", CIN_CAP)],
    ask=["What density and moisture can you guarantee for pepper?", "Can you clean, sort, sterilise and grind in house?", "Which residue and aflatoxin tests do you run, and at which lab?",
         "What volumes can you commit to each season?", "Which organic and food safety certificates do you hold?"],
    faqs=[("Which spices can I source from Sri Lanka besides cinnamon?", "Pepper, cloves, cardamom, nutmeg and mace, ginger, turmeric and vanilla, plus spice mixes and curry powder. Most are exported in bulk."),
          ("What makes Ceylon pepper different?", "The Export Development Board says Sri Lankan pepper has a high piperine level. Sri Lanka meets about 6% of world pepper demand, and its main pepper markets are India, Germany and the US."),
          ("Which essential oils does Sri Lanka produce?", "Cinnamon, pepper, cardamom, citronella, clove and nutmeg oils, mainly for perfumery, cosmetics and toiletries, plus spice oleoresins."),
          ("What documents come with a spice shipment?", "A certificate of origin, a quarantine certificate and a quality certificate, with any food safety certificates the exporter holds.")],
)

cat(
    slug="ayurveda-herbal-products", label="Ayurveda and herbal products", short="Herbal teas, oils, balms and natural cosmetics.", art="s-herbal", seller="herbal products manufacturer",
    h1="Ayurvedic and herbal product manufacturers in Sri Lanka: herbal teas, oils and natural cosmetics",
    title="Ayurvedic and herbal products from Sri Lanka: manufacturers and private label",
    desc="Source herbal teas, ayurvedic oils and balms, natural cosmetics and spice essential oils from Sri Lankan manufacturers. Regulators, certificates and what to check for your market.",
    answer=("Sri Lankan manufacturers make herbal teas such as Ranawara, Gotukola, Moringa and Bael flower, ayurvedic massage oils and balms, herbal soaps and "
            "hair care, and natural cosmetics, many using Sri Lankan spice oils. Ayurveda is governed by the Ayurveda Act of 1961 and the Department of Ayurveda, "
            "and the National Medicines Regulatory Authority covers some products. It is a small, developing export category: official export figures are not "
            "published separately, so check each manufacturer's certificates and how its products are classified in your market."),
    stats=[("93", "ayurvedic items listed on the EDB eMarketplace"), ("66", "herbal cosmetic items listed"), ("1961", "Ayurveda Act that governs the sector")],
    stats_src=f'Sources: Export Development Board,{ln("eMarketplace", AYU_MKT)} and{ln("ayurveda services", "https://www.srilankabusiness.com/news/edb-s-role-in-promoting-ayurveda-services.html")}.',
    glance=[("Main products", "Herbal teas, ayurvedic oils and balms, herbal soaps and hair care, capsules and elixirs, natural cosmetics, spice essential oils"),
            ("Regulators in Sri Lanka", "Department of Ayurveda; National Medicines Regulatory Authority; Consumer Affairs Authority"),
            ("Certificates to ask for", "GMP, HACCP, ISO 22000 for teas, organic where claimed"),
            ("Watch for", "Health claims that your market treats as medicines")],
    products=[("Herbal teas and infusions", "1211 and 2106"), ("Ayurvedic oils, balms and capsules", "3004 or 3304 depending on claims"), ("Herbal soaps and hair care", "3401 and 3305"),
              ("Spice essential oils for cosmetics", "3301.90")],
    names=["ayurvedic products", "herbal tea", "natural cosmetics", "Ranawara tea"],
    evidence=[("Ayurveda in Sri Lanka is governed by the Ayurveda Act, No. 31 of 1961, administered by the Department of Ayurveda.", "EDB", "https://www.srilankabusiness.com/news/edb-s-role-in-promoting-ayurveda-services.html"),
              ("In July 2025 the Export Development Board ran an export workshop on ayurvedic and herbal cosmetics with the medicines regulator and the Industrial Technology Institute.", "EDB", AYU_WS),
              ("Ceylon herbal teas include Ranawara, Gotukola, Moringa, Coriander, Bael flower and Hibiscus.", "EDB", "https://www.srilankabusiness.com/faq/tea/buyer/what-are-types-of-tea.html"),
              ("Sri Lankan essential oils go mainly into perfumery, cosmetics and toiletries.", "EDB", CIN_CAP)],
    certs=[("GMP and HACCP.", "Ask for current certificates for the plant that makes your product."), ("Organic.", "Only where the product claims it; ask for the certificate and scope."),
           ("Your market's rules.", "Check whether each product is a cosmetic, a food or a herbal medicine where you sell it, before you order.")],
    caveats=[("No separate official export figures were found for ayurvedic and herbal products.", "EDB", AYU_WS),
             ("Some products carry health claims that many markets regulate as medicines. Check classification and claims against your own rules.", "EDB eMarketplace", "https://www.srilankabusiness.com/emarketplace/ayurvedic/herbal-products/herbal-cosmetics")],
    ask=["Which products do you make in house, and which do you buy in?", "Do you hold GMP, and does it cover the products I want?", "Can you supply full ingredient lists and test reports for my market?",
         "Do you make private label, and what are the minimum orders?", "Which claims are on the pack, and are they allowed where I sell?"],
    faqs=[("What ayurvedic and herbal products can I source from Sri Lanka?", "Herbal teas, massage oils and balms, herbal soaps, toothpaste, hair and body care, ayurvedic capsules and elixirs, and tea based cosmetics."),
          ("Who regulates ayurvedic products in Sri Lanka?", "The Department of Ayurveda under the Ayurveda Act of 1961, with the National Medicines Regulatory Authority and the Consumer Affairs Authority involved for some products."),
          ("Can I get private label herbal tea or cosmetics?", "Some manufacturers make private label. Tell us the product, market and volumes and we will check certificates before introducing anyone.")],
)


# ================================================================ coconut, produce and plants (group B)
COCO_PAGE = "https://www.srilankabusiness.com/coconut/sri-lankan-coconut-and-coconut-based-products.html"
COCO_R = "https://srilankabusiness.com/ebooks/industry-capability-report-coconut-and-coconut-based-products-2021.pdf"
EPI24 = "https://www.srilankabusiness.com/ebooks/export-performance-indicators-of-sri-lanka-2024.pdf"
KERNEL = "https://www.srilankabusiness.com/coconut/coconut-kernel-products.html"
COCO_BRO = "https://www.srilankabusiness.com/pdf/coconut-and-coconut-based-products-ebrochures-1.pdf"
CCCI = "https://ft.lk/front-page/CCCI-calls-for-urgent-Govt-action-on-local-coconut-crisis/44-772034"
ICC_DC = "https://mail.coconutcommunity.org/page-content/market-review-of-dessicated-coconut-june-2025-mr-82"
ICC_FIB = "https://mail.coconutcommunity.org/page-content/market-review-of-coconut-fiber-november-2025-mr-87"
EDB9M_EDB = "https://www.srilankabusiness.com/news/sri-lankas-exports-surpass-usd-13-6-bn-in-the-first-nine-months-of-2026-recording-5-percent-growth.html"
PEAT_R = "https://www.srilankabusiness.com/pdf/sri-lankan-cocopeat-on-the-global-stage-a-strategic-exploration-of-local-dynamics-market-entry-and-global-opportunities.pdf"
RHP = "https://www.ft.lk/agriculture/Sri-Lankan-cocopeat-companies-visit-RHP-Knowledge-Centre-in-the-Netherlands/31-793976"
FIBRE = "https://www.srilankabusiness.com/coconut/coconut-fibre-products.html"
AC_BLOG = "https://www.srilankabusiness.com/blog/activated-carbon-sri-lanka.html"
SHELL = "https://www.srilankabusiness.com/coconut/coconut-shell-products.html"
ICC_BUL = "https://mail.coconutcommunity.org/files/document/20260206102134pub-quarterly-bulletin.pdf"
FV_R = "https://www.srilankabusiness.com/ebooks/industry-capability-report-fresh-fruits-vegetable-2021.pdf"
FV_Q = "https://www.srilankabusiness.com/fruits-and-vegetables/quality-standards.html"
PINE = "https://www.srilankabusiness.com/news/historic-milestone-in-sri-lankan-pineapple-exports-to-pakistan.html"
FLOR_R = "https://www.srilankabusiness.com/ebooks/industry-capability-report-floriculture-industry-2021.pdf"
FLOR_BRO = "https://www.srilankabusiness.com/pdf/floriculture-products-ebrochures-1.pdf"
FLOR_OV = "https://www.srilankabusiness.com/floriculture/overview.html"

cat(
    slug="coconut-products", label="Coconut food products", short="Desiccated coconut, milk, cream, powder and VCO.", art="s-coconut", seller="coconut processor",
    h1="Desiccated coconut, coconut milk and virgin coconut oil suppliers in Sri Lanka",
    title="Desiccated coconut and coconut milk suppliers in Sri Lanka: wholesale",
    desc="Source desiccated coconut, coconut milk and cream, milk powder, virgin coconut oil and coconut water from Sri Lankan processors. Grades, certificates, HS codes, markets and supply risks.",
    answer=("Sri Lanka's coconut and coconut based exports rose 42.66% to US$1.23 billion in 2025, led by coconut cream, coconut oil and milk powder. The Export "
            "Development Board ranks Sri Lanka the fourth largest exporter of coconut products, and in 2024 it exported US$138 million of liquid coconut milk and "
            "US$112 million of desiccated coconut. Kernel processors hold ISO 22000, FSSC 22000, HACCP and BRC certificates, and every desiccated coconut shipment "
            "carries a Coconut Development Authority certificate. Nut supply has been falling, so build price review clauses into contracts."),
    stats=[("US$1.23B", "coconut and coconut based exports in 2025, up 42.66%"), ("US$138M", "liquid coconut milk exports in 2024"), ("US$112M", "desiccated coconut exports in 2024")],
    stats_src=f'Sources: Export Development Board,{ln("2025 exports", EDB25)} and{ln("export performance indicators 2024", EPI24)}.',
    glance=[("Main products", "Desiccated coconut in fine, medium and super fine cuts, liquid coconut milk, cream, milk powder, coconut oil, virgin coconut oil, coconut water, flour"),
            ("Main markets", "Germany, Netherlands, UK and US for milk and cream; US and Europe for oils; Pakistan, US, Middle East and EU for desiccated coconut"),
            ("Certificates common in the industry", "ISO 22000, FSSC 22000, HACCP, BRC; organic at farm level"),
            ("Documents", "Coconut Development Authority certificate with every desiccated coconut shipment"),
            ("Watch for", "Falling nut harvests and sharp price swings")],
    products=[("Desiccated coconut", "0801.11"), ("Coconut oil", "1513.11"), ("Virgin coconut oil", "1513.11 and 1513.19"), ("Liquid coconut milk", "2008.19"),
              ("Coconut milk powder and coconut cream", "2008.19"), ("Coconut water", "2106.90"), ("Coconut flour", "1106.30")],
    names=["DC", "coconut cream", "VCO", "coconut milk powder"],
    evidence=[("The Export Development Board ranks Sri Lanka the fourth largest exporter of coconut products.", "EDB", COCO_PAGE),
              ("In 2018 Sri Lanka was the largest exporter of coconut milk, cream and milk powder, and the third largest exporter of desiccated coconut.", "EDB coconut report", COCO_R),
              ("Coconut and coconut based exports rose 42.66% to US$1,233.01 million in 2025.", "EDB via Daily FT", EDB25_FT),
              ("Kernel product facilities are certified under ISO 22000, FSSC 22000, HACCP and BRC.", "EDB", KERNEL),
              ("Desiccated coconut comes in super fine, fine and medium cuts with moisture held at 2.5% to 3.0%.", "EDB", KERNEL)],
    certs=[("ISO 22000 or FSSC 22000.", "Food safety, held across kernel product mills."), ("HACCP and BRC.", "Ask for current certificates and the latest audit."),
           ("Coconut Development Authority certificate.", "Required with every desiccated coconut shipment."), ("Organic.", "Some farms are organic certified; ask for the scheme and certifier."),
           ("Halal and kosher.", "Available from some processors; confirm for your product.")],
    caveats=[("Nut output fell to 2,684 million nuts in 2024 from 2,950 million in 2023, tightening raw material supply.", "Daily FT", CCCI),
             ("The International Coconut Community reported Sri Lankan desiccated coconut among the highest priced in the world and expects the market to stay volatile.", "International Coconut Community", ICC_DC),
             ("Kernel product exports fell 29.15% in September 2026, so monthly volumes can swing sharply.", "EDB", EDB9M_EDB),
             ("Exporters may import limited quantities of kernel products for re export. If you need 100% Sri Lankan origin, specify it and ask for origin documents.", "Daily FT", "https://www.ft.lk/front-page/Coconut-exports-cross-1-b-in-2025/44-786461")],
    ask=["Which cuts, fat content and moisture levels do you supply?", "Is all kernel 100% Sri Lankan origin?", "Which food safety certificates do you hold, and when is the next audit?",
         "Do you make private label coconut milk or cream, and in which pack formats?", "How do you price contracts when nut prices move?"],
    faqs=[("Which HS codes apply to desiccated coconut and coconut milk?", "Desiccated coconut is 0801.11, coconut oil 1513.11, coconut milk, cream and milk powder 2008.19, and coconut water 2106.90. Confirm the national tariff line in your market with your customs broker."),
          ("What food safety certificates do Sri Lankan coconut processors hold?", "ISO 22000, FSSC 22000, HACCP and BRC, according to the Export Development Board, and every desiccated coconut shipment carries a Coconut Development Authority certificate."),
          ("How large are Sri Lanka's coconut food exports?", "In 2024: US$138 million of liquid coconut milk, US$112 million of desiccated coconut, US$83 million of coconut oil, US$57 million of milk powder and US$45 million of cream. All coconut exports reached US$1.23 billion in 2025."),
          ("Is supply reliable all year?", "Supply follows the nut harvest, which has fallen since 2023. Agree buffer stock and price review clauses with your supplier.")],
)

cat(
    slug="coco-peat-coir", label="Coco peat and coir", short="Coco peat blocks, grow bags, coir fibre, twine, husk chips.", art="s-cocopeat", seller="coco peat exporter",
    h1="Coco peat and coir suppliers in Sri Lanka: blocks, grow bags, fibre and husk chips",
    title="Coco peat suppliers and coir exporters in Sri Lanka: blocks and grow bags",
    desc="Source coco peat blocks, grow bags, discs and plugs, coir fibre, twine, geotextiles and husk chips from Sri Lankan exporters. Washed, buffered, RHP, HS codes and markets.",
    answer=("Sri Lanka exported US$197.54 million of coco peat, fibre pith and moulded products in 2024, and the Export Development Board describes it as the third "
            "largest coco peat exporter and the largest supplier of brown coir fibre, at about 100,000 tonnes a year. Exporters supply blocks and bricks, grow bags, "
            "discs, cubes and plugs, washed, unwashed or buffered with calcium nitrate, plus coir fibre, twine, geotextiles, mats and husk chips. Many products for "
            "Europe need RHP certification."),
    stats=[("US$197.54M", "coco peat, pith and moulded products in 2024"), ("~100,000 t", "brown coir fibre exported a year"), ("+334%", "husk chip exports, January to September 2026")],
    stats_src=f'Sources: Export Development Board,{ln("export performance indicators 2024", EPI24)},{ln("coconut products", COCO_PAGE)} and{ln("January to September 2026", EDB9M)} (via Newswire).',
    glance=[("Main products", "Coco peat blocks, bricks and briquettes, grow bags, discs, cubes, open tops and plugs, husk chips, bristle and mattress fibre, twine, geotextiles, mats"),
            ("Processing options", "Washed low EC, unwashed high EC, or buffered with calcium nitrate"),
            ("Largest markets in 2022", "Mexico, China, Netherlands, Japan, US, South Korea"),
            ("Certificates to ask for", "RHP for European growing media, ISO 9001 and 14001, organic where needed, phytosanitary certificate"),
            ("Watch for", "Husk supply and price swings")],
    products=[("Coco peat, fibre pith and moulded products", "5305.00"), ("Bristle, mattress and mixed coir fibre", "5305.00"), ("Coir yarn", "5308.10"),
              ("Coir twine and rope", "5607.90"), ("Coir geotextiles", "5311.00"), ("Coconut husk chips", "1404.90")],
    names=["coir pith", "cocopeat", "coco coir", "grow bags", "coir fibre"],
    evidence=[("Sri Lanka is the largest supplier of brown coir fibre, exporting about 100,000 tonnes a year.", "EDB", COCO_PAGE),
              ("The Export Development Board describes Sri Lanka as the third largest coco peat exporter.", "EDB coco peat study", PEAT_R),
              ("Coco peat, fibre pith and moulded products earned US$197.54 million in 2024, up from US$160.72 million in 2023.", "EDB", EPI24),
              ("Moulded coir products for horticulture rose 29% in value to US$182.64 million in January to September 2025, the largest coir category.", "International Coconut Community", ICC_FIB),
              ("Coco peat is supplied washed (low EC), unwashed (high EC) or buffered with calcium nitrate.", "EDB coco peat study", PEAT_R),
              ("Coir twine comes in 2 and 3 ply from 3.5 mm to 12 mm, and coir geotextiles last up to five years.", "EDB", FIBRE)],
    certs=[("RHP.", "Many coco peat products entering Europe, particularly the Netherlands, must meet RHP standards. Ask whether the product and site hold the mark."),
           ("Lot test reports.", "EC, pH, moisture and expansion volume for each lot."), ("ISO 9001 and ISO 14001.", "The Export Development Board says coir manufacturers work to these."),
           ("Organic.", "Available from some exporters for coco peat; ask for the certifier."), ("Phytosanitary certificate.", "Issued by the National Plant Quarantine Service where your country requires it.")],
    caveats=[("Husk supply is limited: husk chip volumes fell 33% in January to September 2025.", "International Coconut Community", ICC_FIB),
             ("Prices swing: coir and coco peat prices fell by an average of 68% in 2022, and fibre prices roughly doubled from early 2024 to late 2025.", "EDB coco peat study", PEAT_R),
             ("Coco peat and moulded product exports fell 10.63% in September 2026 even as husk chips rose, so monthly volumes are uneven.", "EDB", EDB9M_EDB)],
    ask=["Is the product washed, unwashed or buffered, and what EC do you guarantee?", "Does the site hold RHP, if I sell in Europe?", "What expansion volume and moisture do you guarantee per block?",
         "Can you make grow bags to my dimensions and fill?", "What is your monthly capacity in containers?"],
    faqs=[("What forms of coco peat can Sri Lankan suppliers ship?", "Compressed blocks, bricks and briquettes, loose coco peat, grow bags, discs, cubes, open tops and nursery plugs, washed, unwashed or buffered with calcium nitrate."),
          ("Do Sri Lankan coco peat products meet European requirements?", "Many coco peat products entering Europe must meet RHP standards. Ask each supplier whether the product and site hold the RHP mark."),
          ("Where does Sri Lankan coco peat go?", "In 2022 the largest markets were Mexico, China, the Netherlands, Japan, the US and South Korea."),
          ("Which HS codes cover coir products?", "Coco peat, pith and fibre are grouped under 5305.00, coir twine and rope under 5607.90, geotextiles under 5311.00 and coconut husk chips under 1404.90.")],
)

cat(
    slug="activated-carbon", label="Coconut shell activated carbon", short="Granular, powdered and pellet activated carbon, shell charcoal.", art="s-carbon", seller="activated carbon producer",
    h1="Coconut shell activated carbon manufacturers in Sri Lanka",
    title="Coconut shell activated carbon manufacturers and exporters in Sri Lanka",
    desc="Source granular, powdered and pelletised coconut shell activated carbon and shell charcoal from Sri Lankan producers for water treatment, gold recovery, air and food. Specs, HS codes and markets.",
    answer=("Sri Lanka is among the top three producers of activated carbon in the world, according to the Export Development Board, and exports reached US$155.55 "
            "million in 2024. Exports rose 37.79% in the first nine months of 2026. Producers make granular, powdered and pelletised coconut shell activated carbon "
            "for water treatment, air and gas treatment, gold recovery, food and beverage and energy storage, and the main markets are the US, the EU, Japan and "
            "South Korea. Grade specifications are agreed supplier by supplier, so ask for a certificate of analysis per lot."),
    stats=[("Top 3", "activated carbon producer, EDB ranking"), ("US$155.55M", "activated carbon exports in 2024"), ("+37.79%", "January to September 2026")],
    stats_src=f'Sources: Export Development Board,{ln("coconut products", COCO_PAGE)} and{ln("export performance indicators 2024", EPI24)}; EDB via{ln("Newswire", EDB9M)}.',
    glance=[("Main products", "Granular activated carbon (standard, washed, impregnated), powdered, extruded pellets, coconut shell charcoal"),
            ("Applications", "Water treatment, air and gas treatment, gold recovery, food and beverage, energy storage"),
            ("Main markets", "US, EU, Japan, South Korea; exports to China up 78.33% in January to September 2026"),
            ("Specs to agree", "Iodine number, mesh size, hardness, ash, moisture and CTC, with a certificate of analysis per lot"),
            ("Watch for", "Shell supply follows the coconut harvest")],
    products=[("Activated carbon", "3802.10"), ("Coconut shell charcoal", "4402.90"), ("Coconut shell pieces and powder", "1404.90")],
    names=["GAC", "coconut shell carbon", "activated charcoal", "gold recovery carbon"],
    evidence=[("Sri Lanka is among the top three producers of activated carbon in the global market.", "EDB", COCO_PAGE),
              ("Activated carbon exports were US$155.55 million in 2024, up from US$132.80 million in 2023.", "EDB", EPI24),
              ("Activated carbon exports reached US$25.26 million in September 2026, up 43.52%.", "EDB", EDB9M_EDB),
              ("Sri Lanka pioneered green charcoaling in Asia.", "EDB", COCO_PAGE),
              ("Sri Lankan coconut shell activated carbon serves water treatment, air and gas treatment, gold recovery, food and beverage and energy storage.", "EDB", SHELL)],
    certs=[("Certificate of analysis per lot.", "Iodine number, mesh size, hardness, ash, moisture and CTC as agreed in the contract."),
           ("Drinking water approvals.", "For potable water, ask for AWWA B604 conformity or NSF/ANSI 61 certification where your market requires it."),
           ("Food grade, halal and kosher.", "Ask for these if the carbon is for food and beverage use."), ("ISO 9001 and ISO 14001.", "Ask for current certificates for the producing site.")],
    caveats=[("Shell supply depends on the coconut harvest, which fell to 2,684 million nuts in 2024.", "Daily FT", CCCI),
             ("Sri Lanka also imports shell charcoal and activated carbon. If you need Sri Lankan origin shell, specify it and ask for origin documents.", "International Coconut Community", ICC_BUL)],
    ask=["Which grades do you make, and what iodine number, mesh and hardness can you guarantee?", "Do you activate from shell charcoal you make yourself?",
         "Can you supply AWWA B604 or NSF/ANSI 61 documentation for drinking water use?", "Do you make impregnated or washed grades?", "What is your monthly capacity per grade?"],
    faqs=[("How significant is Sri Lanka for activated carbon?", "The Export Development Board places Sri Lanka among the top three producers. Exports were US$155.55 million in 2024 and rose 37.79% in January to September 2026."),
          ("Which HS codes apply?", "Activated carbon is 3802.10 and coconut shell charcoal 4402.90."),
          ("What is Sri Lankan activated carbon used for?", "Water treatment, air and gas treatment, gold recovery, food and beverage and energy storage."),
          ("Which markets buy Sri Lankan activated carbon?", "The US, the EU, Japan and South Korea, with exports to China growing fast in 2026.")],
    tender="Water utilities and mining projects tender for granular activated carbon. Tender Radar sends you the ones that fit your grades.",
)

cat(
    slug="fruits-vegetables", label="Fruits and vegetables", short="Pineapple, banana, papaya, king coconut water, gherkins.", art="s-fruit", seller="fruit and vegetable exporter",
    h1="Fruit and vegetable exporters in Sri Lanka: pineapple, banana, papaya and king coconut",
    title="Fruit and vegetable exporters in Sri Lanka: fresh and processed",
    desc="Source fresh pineapple, banana, papaya and vegetables, king coconut water, gherkins and dried fruit from Sri Lankan exporters. Markets, phytosanitary rules, certificates and supply.",
    answer=("Sri Lanka exported US$71.51 million of fruits, nuts and vegetables in 2024, led by bananas, papaya and melons, vegetables and gherkins, plus bottled "
            "king coconut water, a fruit indigenous to Sri Lanka. About 65% of fresh produce goes to the Middle East and the Maldives, and almost all processed "
            "products go to Europe. Fresh shipments travel with a phytosanitary certificate from the National Plant Quarantine Service, and some farms are "
            "GlobalG.A.P. certified. It is a small category, so steady volumes of one fresh line may need several growers."),
    stats=[("US$71.51M", "fruit, nut and vegetable exports in 2024"), ("65%", "of fresh produce goes to the Middle East and Maldives"), ("2026", "first pineapple shipment to Pakistan")],
    stats_src=f'Sources: Export Development Board,{ln("export performance indicators 2024", EPI24)},{ln("major markets", "https://www.srilankabusiness.com/fruits-and-vegetables/major-markets.html")} and{ln("pineapple access", PINE)}.',
    glance=[("Main products", "Bananas, papaya and melons, pineapple, king coconut and king coconut water, gherkins, vegetables, frozen and dried fruit"),
            ("Largest markets in 2021", "UAE, Maldives, Saudi Arabia, UK, Qatar; Switzerland, Germany and France for processed products"),
            ("Documents", "Phytosanitary certificate from the National Plant Quarantine Service"),
            ("Certificates to ask for", "GlobalG.A.P. for farms; ISO 22000, HACCP, halal or kosher for processed products"),
            ("Watch for", "Small holdings and uneven supply")],
    products=[("Bananas", "0803"), ("Pineapples", "0804.30"), ("Papaya and melons", "0807"), ("King coconut and fresh coconuts", "0801.12 and 0801.19"),
              ("King coconut water", "2106.90"), ("Gherkins, fresh or preserved", "0707 and 2001.10"), ("Frozen fruit", "0811")],
    names=["king coconut", "thambili", "Sri Lankan pineapple", "gherkins"],
    evidence=[("About 65% of fresh produce exports go to the Middle East and the Maldives, and almost all processed products go to Europe.", "EDB", "https://www.srilankabusiness.com/fruits-and-vegetables/major-markets.html"),
              ("Fruits, nuts and vegetables exports were US$71.51 million in 2024, including bananas at US$16.57 million and gherkins at US$3.99 million.", "EDB", EPI24),
              ("King coconut is indigenous to Sri Lanka, and exporters supply bottled king coconut water.", "EDB", "https://www.srilankabusiness.com/coconut/coconut-water-based-products.html"),
              ("Fresh pineapple gained access to Pakistan in 2026 after orchard and pack house audits, from GAP certified fields.", "EDB", PINE),
              ("Some farms are GlobalG.A.P. certified, and processors work to ISO 22000 and hold HACCP, halal and kosher certificates.", "EDB", FV_Q)],
    certs=[("Phytosanitary certificate.", "Issued by the National Plant Quarantine Service for fresh produce where your country requires it."), ("GlobalG.A.P.", "Held by some farms; ask for the certificate number."),
           ("ISO 22000 and HACCP.", "For processed fruit and vegetables."), ("Market access protocol.", "Check your country allows the specific fresh fruit from Sri Lanka.")],
    caveats=[("Small holdings and gaps in continuity of supply are listed as sector weaknesses, along with high packaging and air freight costs.", "EDB fruit and vegetable report", FV_R),
             ("Market access is set fruit by fruit and country by country; fresh pineapple to Pakistan only began in August 2026.", "EDB", PINE)],
    ask=["Do you grow, or buy from out growers, and how do you keep supply continuous?", "Is the farm GlobalG.A.P. certified?", "Does my country allow imports of this fruit from Sri Lanka?",
         "How do you pack and cool for air or sea freight?", "Which processed formats can you supply: frozen, dried, in brine?"],
    faqs=[("Where do Sri Lankan fruit and vegetable exports go?", "About 65% of fresh produce goes to the Middle East and the Maldives, and almost all processed products go to Europe."),
          ("What certificates do Sri Lankan fruit exporters hold?", "Some farms are GlobalG.A.P. certified, processors work to ISO 22000 and HACCP, and fresh produce ships with a phytosanitary certificate."),
          ("Can I source king coconut water from Sri Lanka?", "Yes. King coconut is indigenous to Sri Lanka and exporters supply it bottled."),
          ("How big is the category?", "US$71.51 million in 2024, so it suits specialist and mixed programmes better than very large single line volumes.")],
)

cat(
    slug="floriculture", label="Cut foliage and live plants", short="Cut foliage, pot plants, aquarium plants and cuttings.", art="s-flora", seller="floriculture exporter",
    h1="Cut foliage, live plant and aquarium plant exporters in Sri Lanka",
    title="Cut foliage and aquarium plant exporters in Sri Lanka: wholesale",
    desc="Source cut foliage, indoor pot plants, cuttings, tissue culture plants and aquarium plants from Sri Lankan producer exporters. Markets, certificates and plant health rules.",
    answer=("Sri Lanka exported US$13.67 million of cut flowers and foliage in 2024, almost all of it foliage such as dracaena and cordyline, plus a further US$16.63 "
            "million of live plants and parts of plants. Exporters also supply aquarium plants including Cryptocoryne, Anubias and Echinodorus. Europe takes 60% of "
            "floriculture exports, led by the Netherlands. The main exporters grow in their own nurseries and hold GLOBALG.A.P., MPS and Fair Trade certificates. "
            "Units are small, so large programmes may need several growers."),
    stats=[("US$13.67M", "cut flowers and foliage exports in 2024"), ("60%", "of floriculture exports go to Europe"), ("US$16.63M", "live plants and parts of plants, 2024")],
    stats_src=f'Sources: Export Development Board,{ln("export performance indicators 2024", EPI24)} and{ln("floriculture overview", FLOR_OV)}.',
    glance=[("Main products", "Cut foliage, indoor pot plants, young plants and cuttings, tissue culture plants, aquarium plants, some cut flowers"),
            ("Largest foliage markets in 2021", "Netherlands, Japan, Saudi Arabia, Australia, UK; Germany for aquatic plants"),
            ("Certificates", "GLOBALG.A.P., MPS, Fair Trade; phytosanitary certificate; CITES for listed species"),
            ("Watch for", "Air freight capacity and small production units")],
    products=[("Cut foliage", "0604"), ("Live plants, pot plants and cuttings", "0602"), ("Aquarium plants and tissue culture plants", "0602.90"), ("Cut flowers", "0603")],
    names=["dracaena", "cordyline", "aquatic plants", "foliage plants"],
    evidence=[("Europe takes 60% of Sri Lankan floriculture exports.", "EDB", FLOR_OV),
              ("Cut flowers and foliage exports were US$13.67 million in 2024, of which foliage was US$11.69 million.", "EDB", EPI24),
              ("Export companies hold GLOBALG.A.P., MPS and Fair Trade certifications.", "EDB floriculture brochure", FLOR_BRO),
              ("All major exporters are producer exporters running their own nurseries.", "EDB", "https://www.srilankabusiness.com/floriculture/supply-base-and-major-markets.html"),
              ("Aquarium plant exports include Cryptocoryne, Echinodorus, Anubias, Lagenandra and Aponogeton.", "EDB", "https://www.srilankabusiness.com/floriculture/aquarium-plants.html")],
    certs=[("Phytosanitary certificate.", "Issued after plant quarantine checks by the National Plant Quarantine Service."), ("GLOBALG.A.P., MPS and Fair Trade.", "Held by export companies; ask for the current certificate."),
           ("CITES.", "Needed for listed species, including some orchids.")],
    caveats=[("Cold storage at the airport, direct flights to the Netherlands and air freight rates are the sector's main constraints.", "EDB floriculture report", FLOR_R),
             ("Cut flower and foliage exports fell from US$15.01 million in 2023 to US$13.67 million in 2024.", "EDB", EPI24)],
    ask=["Do you grow in your own nurseries, and what is your weekly volume per variety?", "Which certificates do you hold: GLOBALG.A.P., MPS, Fair Trade?",
         "How do you pack and keep the cold chain to the airport?", "Does any variety need CITES papers or an import permit in my country?", "Can you grow to my specification or contract grow new varieties?"],
    faqs=[("What floriculture products does Sri Lanka export most?", "Cut foliage, at US$11.69 million of the US$13.67 million cut flowers and foliage total in 2024, plus live plants and aquarium plants."),
          ("Which markets buy Sri Lankan foliage?", "The Netherlands, Japan, Saudi Arabia, Australia and the UK. Europe takes 60% of floriculture exports."),
          ("Which aquarium plants are available?", "Cryptocoryne, Echinodorus, Anubias, Lagenandra and Aponogeton, grown for export in supervised nurseries.")],
)


# ================================================================ industrial and manufactured goods (group D)
EEC_PAGE = "https://www.srilankabusiness.com/electrical-and-electronics/"
EEC_PROD = "https://www.srilankabusiness.com/electrical-and-electronics/sri-lankan-electrical-and-electronic-products.html"
EEC_TR = "https://srilankabusiness.com/electrical-and-electronics/about/electronic-electrical-transformers-coils-and-inductors.html"
CBSL_EEC = "https://www.cbsl.gov.lk/sites/default/files/cbslweb_documents/Winning_Industries_Electronics_and_Electrical_Components.pdf"
EEC_CABLE = "https://www.srilankabusiness.com/edb/success-stories/electrical-and-electronics/acl-cables.html"
TR_NEPAL = "https://www.ft.lk/Business/ltl-wins-nepal-tender/34-296310"
TR_PAK = "https://www.ft.lk/Business/ltl-transformers-procures-large-contract-in-pakistan/34-589546"
LE_PAGE = "https://www.srilankabusiness.com/light-engineering/export-potential-sri-lanka-light-engineering-sector.html"
IN_PROF = "https://www.srilankabusiness.com/pdfs/market-profiles/2026/india-2026.pdf"
NO_PROF = "https://www.srilankabusiness.com/pdfs/market-profiles/2026/norway-2026.pdf"
BOI_BOAT = "https://investsrilanka.com/wp-content/uploads/2025/12/Boat-Manufacturing-Ship-Building-Ssector-2025.pdf"
BOAT_DOC = "https://slhc.com.my/wp-content/uploads/2025/10/BOAT-AND-SHIP-BUILDING-SECTOR.pdf"
BOAT_LEIS = "https://www.srilankabusiness.com/blog/sri-lanka-leisure-recreational-boat-export-potential.html"
PRINT_TR = "https://www.srilankabusiness.com/printing-and-stationery/exporter-information/industry-trends.html"
PRINT_OV = "https://www.srilankabusiness.com/printing-and-stationery/overview.html"
PRINT_PP = "https://www.srilankabusiness.com/printing-prepress-packaging/"
CER_R = "https://srilankabusiness.com/ebooks/industry-capability-report-ceramic-2025.pdf"
CER_TW = "https://www.srilankabusiness.com/ceramic-and-porcelain/porcelain-tableware.html"
CER_PAGE = "https://www.srilankabusiness.com/ceramic-and-porcelain/"
WOOD_WHY = "https://www.srilankabusiness.com/wooden/why-sri-lankan-wooden-products.html"
WOOD_PAGE = "https://srilankabusiness.com/wooden"
EUDR = "https://www.lovguiden.dk/en/det-offentlige/eu-udenrigstjenesten/2026-10-22-eu-og-sri-lanka-holder-workshop-om-skovrydningsforordningen-og-gummi"

cat(
    slug="electrical-cables-transformers", label="Electrical and electronics", short="Cables, transformers, switchgear, panels and PCBA.", art="s-electrical", seller="electrical manufacturer",
    h1="Electrical cable, transformer and switchgear manufacturers in Sri Lanka",
    title="Transformer, cable and switchgear manufacturers in Sri Lanka",
    desc="Source power and distribution transformers, power cables, switchgear, panels and electronics assembly from Sri Lankan manufacturers. Export growth, standards, tenders and how to buy.",
    answer=("Sri Lanka's electrical and electronic component exports reached US$508.86 million in the first nine months of 2026, up 61% and already above the "
            "US$438.49 million earned in all of 2025. Growth is led by insulated wires and cables, up 82.59%, transformers, up 33.46%, and switches, boards and "
            "panels, up 31.49%. More than 100 manufacturers and service providers work across electronics manufacturing services, components, own products and "
            "design, and Sri Lankan transformer makers have won national utility tenders abroad for over a thousand units at a time."),
    stats=[("US$508.86M", "exports, January to September 2026, up 61.05%"), ("+82.59%", "insulated wires and cables in the same period"), ("100+", "manufacturers and service providers")],
    stats_src=S2(f' Manufacturer count: Export Development Board,{ln("electrical and electronics", EEC_PROD)}.'),
    glance=[("Main products", "Power and distribution transformers, power, control and data cables, winding wire, LV switchboards and panels, switches and sockets, PCB assembly, wire harnesses, coils and inductors"),
            ("Markets", "Switzerland, Germany, the US, the Maldives, Australia, the UK, Japan, Norway; India and Bangladesh in the region"),
            ("Standards tenders ask for", "IEC 60076 for transformers, IEC 60502 for cables, IEC 61439 for switchgear assemblies, type tests at an accredited lab, ISO 9001"),
            ("Watch for", "Type test coverage for the exact ratings you buy")],
    products=[("Insulated wires and cables, including power, data and winding wire", "8544"), ("Electrical transformers and static converters", "8504"),
              ("Boards, panels and consoles for electric control", "8537"), ("Parts of boards and panels", "8538"), ("Switches and sockets up to 1,000 V", "8536"),
              ("Printed circuit assemblies", "8534 and 8543"), ("Telephone sets and audio and video equipment", "8517 and 8518")],
    names=["distribution transformers", "power cables", "LV switchgear", "panel boards", "EMS", "PCBA"],
    evidence=[("Electrical and electronic component exports reached US$508.86 million in January to September 2026, up 61.05%, led by insulated wires and cables (+82.59%), transformers (+33.46%) and switches, boards and panels (+31.49%).", "EDB via Newswire", EDB9M),
              ("The sector has more than 100 manufacturers and service providers across electronics manufacturing services, component manufacturing, own products and design.", "EDB", EEC_PROD),
              ("The sector earned US$438.49 million in 2025 and employs 37,000 people.", "EDB", EEC_PAGE),
              ("Transformer, coil and inductor makers state conformity with ISO 9001, ISO 14001 and the EU RoHS directive.", "EDB", EEC_TR),
              ("A Sri Lankan transformer maker won a national utility tender for 1,040 distribution transformers in South Asia.", "Daily FT", TR_NEPAL),
              ("A Sri Lankan cable maker exports to Sweden, the UK, Africa, the Maldives, Australia, New Zealand and the Caribbean.", "EDB", EEC_CABLE)],
    certs=[("IEC 60076.", "The standard power and distribution transformer tenders specify, with type test reports often no older than five years."),
           ("IEC 60502.", "Power cables, with conductors to IEC 60228."), ("IEC 61439.", "Low voltage switchgear and controlgear assemblies, with type test or design verification certificates."),
           ("Accredited type tests.", "Short circuit and other type tests at an ISO/IEC 17025 accredited laboratory; ask which ratings each report covers."),
           ("ISO 9001, ISO 14001 and RoHS.", "Held by transformer and coil makers, according to the Export Development Board.")],
    caveats=[("Monthly figures swing: exports fell 11.09% in December 2025 before rising 123.48% in the first half of 2026.", "EDB via Daily FT", EDB25_FT),
             ("Local product testing services are limited, so ask for third party type test reports rather than relying on local tests.", "Central Bank of Sri Lanka", CBSL_EEC),
             ("Several of the largest exporters are units of foreign groups, so check that a claim describes the Sri Lankan plant, not the parent group.", "EDB", "https://www.srilankabusiness.com/edb/success-stories/electrical-and-electronics")],
    ask=["Which ratings and voltage classes do your type test reports cover, and from which lab?", "Which IEC or BS standards do you build to for this product?",
         "Can you share supply records for similar units in the last three years?", "Will you allow our engineers to witness factory acceptance tests?", "What are your guaranteed losses and the tolerance on them?"],
    faqs=[("What electrical and electronic products does Sri Lanka export?", "Insulated wires and cables, transformers, switches, boards and panels, printed circuit assemblies, telephone and audio equipment, wire harnesses, coils and inductors, from more than 100 manufacturers and service providers."),
          ("How fast is the sector growing?", "Exports reached US$508.86 million in January to September 2026, up 61.05%, against US$438.49 million in all of 2025."),
          ("Which countries buy Sri Lankan electrical products?", "Switzerland, Germany, the US, the Maldives, Australia, the UK, Japan and Norway, with India and Bangladesh in the region."),
          ("Do Sri Lankan transformer makers bid on international tenders?", "Yes. Sri Lankan transformer makers have won national utility tenders abroad, including one for 1,040 distribution transformers. Our Tender Radar sends exporters matched utility tenders, and our bid desk helps them prepare.")],
    tender="Utilities, governments and development bank projects buy transformers, cables and switchgear by tender. Tender Radar sends matched tenders to your WhatsApp.",
)

cat(
    slug="light-engineering", label="Light engineering and machinery", short="Pumps, engines, boilers, castings and fabrication.", art="s-engineering", seller="engineering manufacturer",
    h1="Pump, engine and light engineering manufacturers in Sri Lanka",
    title="Light engineering manufacturers in Sri Lanka: pumps, machinery, fabrication",
    desc="Source pumps, engines, boilers, agricultural and processing machinery, castings, aluminium extrusions, fasteners and metal fabrication from Sri Lankan manufacturers.",
    answer=("Sri Lanka's exports of boilers, piston engines, pumps and vacuum pumps reached US$171.39 million in the first half of 2026 and grew 508.71% in the "
            "first nine months. The wider light engineering industry has more than 500 manufacturing units making pumps, agricultural, tea and rubber processing "
            "machinery, castings, aluminium extrusions, fasteners, steel structures and auto parts. The Export Development Board says Sri Lankan makers can serve "
            "small order and niche requirements. Growth in pumps and engines is from a low base, so check supplier depth case by case."),
    stats=[("US$171.39M", "boilers, engines and pumps, January to June 2026"), ("+508.71%", "same group, January to September 2026"), ("500+", "light engineering manufacturing units")],
    stats_src=f'Sources: Export Development Board via{ln("Daily FT", EDB1H)} and{ln("Newswire", EDB9M)}; EDB,{ln("light engineering", LE_PAGE)}.',
    glance=[("Main products", "Pumps, engines and boilers, tea and rubber processing machinery, rice mills, agricultural machinery, castings, aluminium extrusions, fasteners, steel structures"),
            ("Markets", "India, the US, Germany, Bangladesh, Switzerland, the Maldives, plus China, Singapore, Japan, South Korea and the EU"),
            ("Certificates to ask for", "ISO 9001; material test certificates; CE marking for machinery sold in the EU"),
            ("Watch for", "Scrap based raw material and new export lines with short track records")],
    products=[("Boilers", "8402"), ("Piston engines", "8407 and 8408"), ("Pumps for liquids", "8413"), ("Vacuum pumps and compressors", "8414"),
              ("Agricultural and processing machinery", "8432, 8433, 8437 and 8438"), ("Steel and aluminium structures", "7308 and 7610"), ("Aluminium extrusions", "7604"), ("Nails, screws, bolts and nuts", "7317 and 7318")],
    names=["water pumps", "metal fabrication", "tea machinery", "aluminium profiles", "fasteners"],
    evidence=[("Exports of boilers, piston engines, pumps and vacuum pumps reached US$171.39 million in January to June 2026.", "EDB via Daily FT", EDB1H),
              ("Exports of the same group to India rose from US$0.24 million in 2024 to US$11.3 million in 2025.", "EDB India market profile", IN_PROF),
              ("The light engineering industry has more than 500 manufacturing units and employs over 100,000 people directly and indirectly.", "EDB", LE_PAGE),
              ("The Export Development Board says Sri Lanka can cater to small order requirements in niche markets.", "EDB", LE_PAGE),
              ("The US bought US$39.12 million of Sri Lankan nails, screws, bolts and nuts in 2025.", "EDB US market profile", "https://www.srilankabusiness.com/pdfs/market-profiles/2026/usa-2026.pdf")],
    certs=[("ISO 9001.", "Held by listed exporters; ask for the certificate for the producing site."), ("Material test certificates.", "Most makers use metal scrap, so ask for alloy and traceability certificates."),
           ("CE marking and pump test standards.", "Machinery for the EU needs CE marking; pump performance tests to ISO 9906 where specified.")],
    caveats=[("The latest sector wide export figure is US$306 million for 2019; no 2025 total has been published.", "EDB", LE_PAGE),
             ("The jump in pumps and engines comes from a very low base, so supplier depth varies.", "EDB India market profile", IN_PROF)],
    ask=["Which products do you make in house, and which do you assemble?", "Can you supply material test certificates for each lot?", "Do your machines carry CE marking, if I sell in the EU?",
         "What is your capacity per month for my product?", "Can you build to my drawings and standards?"],
    faqs=[("What light engineering products does Sri Lanka export?", "Agricultural and construction machinery, tea and rubber processing machinery, rice mills, pumps, castings, copper products, auto parts, aluminium extrusions, bicycles, fasteners and steel furniture."),
          ("Does Sri Lanka export pumps and engines?", "Yes. Boilers, piston engines, pumps and vacuum pumps reached US$171.39 million in January to June 2026."),
          ("Can Sri Lankan engineering firms take small orders?", "The Export Development Board says they can cater to small order and niche requirements.")],
    tender="Water, irrigation and power projects tender for pumps, gensets and fabricated equipment. Tender Radar matches them to what you make.",
)

cat(
    slug="boat-building", label="Boats and marine", short="Fibreglass boats, workboats, catamarans and patrol craft.", art="s-boats", seller="boat builder",
    h1="Boat builders in Sri Lanka: fibreglass boats, catamarans, workboats and patrol craft",
    title="Boat builders in Sri Lanka: fibreglass, catamaran and workboat yards",
    desc="Commission fibreglass boats, catamarans, fishing vessels, passenger and crew boats, patrol craft and pontoons from Sri Lankan boatyards. Classification, CE marking, markets and what to check.",
    answer=("Sri Lankan boatyards build yachts and leisure boats, catamarans, fishing vessels, passenger and crew boats, landing craft, tugs, patrol and rescue "
            "craft and pontoons, mostly in fibreglass and composite, with larger vessels in aluminium and steel. Norway bought US$43.1 million of Sri Lankan built "
            "boats in 2025, up from US$21 million in 2023. Yards build to Lloyd's Register, DNV, Bureau Veritas and ABS rules, but the Export Development Board "
            "names certification as the sector's biggest barrier for leisure boats, so confirm CE or class documents per yard and model."),
    stats=[("US$43.1M", "boat exports to Norway in 2025"), ("US$40M+", "boat building exports in 2024"), ("~76", "active boatyards")],
    stats_src=f'Sources: Export Development Board,{ln("Norway market profile", NO_PROF)}; Board of Investment,{ln("boat building sector 2025", BOI_BOAT)}.',
    glance=[("Main products", "Yachts and leisure boats, catamarans, fishing vessels, passenger and crew boats, landing craft, tugs, patrol and rescue craft, pontoons"),
            ("Main markets", "Norway, the Maldives, France, India, Spain, the US, the Netherlands"),
            ("Classification", "Lloyd's Register, DNV, Bureau Veritas, ABS; CE marking for EU leisure boats; ABYC for the US"),
            ("Watch for", "Certification and working capital at smaller yards")],
    products=[("Yachts and pleasure boats", "8903"), ("Fishing vessels", "8902"), ("Passenger, crew and cargo boats", "8901"), ("Tugs", "8904"), ("Patrol and rescue craft", "8906"), ("Pontoons and floating structures", "8907")],
    names=["FRP boats", "fiberglass boats", "catamarans", "workboats", "patrol boats"],
    evidence=[("Norway bought US$43.1 million of Sri Lankan built boats in 2025, up from US$21 million in 2023.", "EDB Norway market profile", NO_PROF),
              ("The sector exported more than US$40 million in 2024, with about 76 active boatyards and about 5,000 direct jobs.", "Board of Investment", BOI_BOAT),
              ("Vessels are built to Lloyd's Register, DNV, Bureau Veritas and ABS rules.", "EDB boat building sector document", BOAT_DOC),
              ("Most hulls are fibreglass and composite; larger vessels are built in aluminium and steel.", "EDB", "https://www.srilankabusiness.com/blog/big-opportunities-for-boat-and-ship-building-sector.html"),
              ("In September 2026 the government committed to a dedicated boat manufacturing zone.", "Daily Mirror", "https://www.dailymirror.lk/business-news/Govt-commits-to-boat-manufacturing-zone-EDB-to-pick-site/273-350856")],
    certs=[("Classification.", "Ask which society the vessel is built and surveyed to: Lloyd's Register, DNV, Bureau Veritas or ABS."),
           ("CE marking.", "Required for leisure boats sold in the EU under the Recreational Craft Directive 2013/53/EU."), ("ABYC and NMMA.", "Expected for leisure boats sold in the US.")],
    caveats=[("The Export Development Board names certification and compliance as the sector's most significant barrier for leisure boats.", "EDB", BOAT_LEIS),
             ("Exports depend on individual vessel orders and are concentrated in one market, so revenue is lumpy and yard capacity varies.", "EDB Norway market profile", NO_PROF),
             ("Financing and working capital remain challenges for small and medium builders, which matters for large or long lead orders.", "EDB", BOAT_LEIS)],
    ask=["Which vessels of this type and size have you delivered, and to whom can we speak?", "Which classification society will survey the build?", "Can you deliver CE or ABYC documentation for this model?",
         "What is the build slot and the payment schedule?", "How do you handle warranty and after sales support abroad?"],
    faqs=[("What boats are built in Sri Lanka for export?", "Yachts and leisure boats, catamarans, fishing vessels, passenger and crew boats, landing craft, tugs, patrol and rescue craft, pontoons and floating restaurants."),
          ("Who buys Sri Lankan boats?", "Norway is the largest market, at US$43.1 million in 2025, followed by the Maldives. France, India, Spain, the US and the Netherlands are also named."),
          ("Are Sri Lankan boats classed and CE marked?", "Yards build to Lloyd's Register, DNV, Bureau Veritas and ABS rules. EU leisure boats need CE marking, so confirm the documents per yard and model.")],
    tender="Governments and agencies tender for patrol, fisheries and passenger boats. Tender Radar sends you the ones that fit your yard.",
)

cat(
    slug="printing-packaging", label="Printing and packaging", short="Cartons, labels, tags, books and paper products.", art="s-packaging", seller="printing and packaging company",
    h1="Printing and packaging companies in Sri Lanka: cartons, labels and book printing",
    title="Packaging manufacturers and printers in Sri Lanka: cartons, labels, books",
    desc="Source corrugated cartons, printed boxes, labels and garment tags, paper sacks, kraft paper and book printing from Sri Lankan printers and packaging makers. Markets and what to check.",
    answer=("Sri Lankan printers and packaging makers supply tea cartons, printed paperboard boxes, corrugated cartons, labels and garment tags, paper sacks and "
            "recycled kraft paper, and print books, catalogues, stationery and calendars on flexo and offset presses. The industry has more than 50 years of "
            "prepress experience, and export revenue was an estimated US$118 million in 2019, the latest sector total published. Much of the packaging serves "
            "Sri Lanka's own tea and apparel exporters. Certificates such as FSC, BRCGS or food contact compliance vary by company."),
    stats=[("US$118M", "printing and paper product exports, 2019 estimate"), ("50+ years", "of prepress experience")],
    stats_src=f'Source: Export Development Board,{ln("industry trends", PRINT_TR)} and{ln("printing and packaging", PRINT_PP)}.',
    glance=[("Main products", "Corrugated cartons, printed paperboard boxes, tea cartons, labels and garment tags, paper sacks, kraft paper, books, catalogues, stationery"),
            ("Main markets", "Exported largely to the EU; also the UK, the US, Australia, Singapore, the Maldives and Bangladesh"),
            ("Certificates to ask for", "FSC chain of custody, BRCGS Packaging or ISO 22000 for food packaging, EU food contact compliance"),
            ("Watch for", "Certificates vary company by company")],
    products=[("Cartons, boxes and bags of paper and paperboard", "4819"), ("Paper labels and tags", "4821"), ("Kraft paper and paperboard", "4804 and 4805"),
              ("Printed books and brochures", "4901"), ("Other printed matter, calendars and cards", "4909 to 4911")],
    names=["corrugated boxes", "printed cartons", "garment tags", "offset printing", "book printing"],
    evidence=[("Sri Lanka's printing industry has more than 50 years of prepress experience.", "EDB", PRINT_PP),
              ("Printing and paper product exports grew from US$83 million in 2015 to an estimated US$118 million in 2019.", "EDB", PRINT_TR),
              ("Export packaging lines include tea cartons, apparel inner cartons, printed paperboard boxes and corrugated cartons, on flexo and offset.", "EDB", PRINT_OV),
              ("A listed kraft paper producer states all its products are FSC certified for export packaging.", "EDB", PRINT_PP)],
    certs=[("FSC chain of custody.", "Check the certificate code on the FSC database."), ("BRCGS Packaging Materials or ISO 22000.", "For food and tea packaging."),
           ("EU food contact compliance.", "Regulation 1935/2004 and good manufacturing practice for packaging that touches food."), ("Colour management.", "Ask for ISO 12647 or G7 if colour matching matters to you.")],
    caveats=[("Sector export figures are dated, with 2019 the latest total, and differ between official pages.", "EDB", PRINT_OV),
             ("No ISO, BRCGS or food contact certificates are listed sector wide, so verify each supplier.", "EDB", PRINT_PP)],
    ask=["Which certificates do you hold: FSC, BRCGS Packaging, ISO 22000?", "Which presses and finishing do you run, and what sizes?", "Can you proof to my colour standard?",
         "What are your minimum runs and lead times?", "Can you consolidate packaging with my product shipment from Sri Lanka?"],
    faqs=[("What printing and packaging does Sri Lanka export?", "Books, catalogues and stationery; tea cartons, printed boxes, corrugated cartons, labels and garment tags; paper sacks; and recycled kraft paper."),
          ("Can Sri Lankan suppliers provide FSC certified packaging?", "Some can. At least one kraft paper producer states all its products are FSC certified. Ask each supplier for its chain of custody code."),
          ("Which markets do Sri Lankan printers serve?", "Mainly the EU, plus the UK, the US, Australia, Singapore, India, the Maldives and Bangladesh.")],
    tender="Public bodies and international agencies tender for printed material and packaging. Tender Radar sends you the ones that fit.",
)

cat(
    slug="ceramics-porcelain", label="Ceramics and porcelain", short="Porcelain tableware, hotelware, tiles and ornaments.", art="s-ceramics", seller="porcelain manufacturer",
    h1="Porcelain tableware and ceramics manufacturers in Sri Lanka",
    title="Porcelain tableware and ceramic manufacturers in Sri Lanka: hotelware",
    desc="Source porcelain and fine china tableware, hotelware, ceramic tiles and ornamental ware from Sri Lankan manufacturers. FDA and ASTM conformity, decoration, markets and what to check.",
    answer=("Sri Lanka exported US$20.76 million of tableware and kitchenware in 2024, mostly porcelain and fine china, along with wall and floor tiles and "
            "ornamental ware. The Export Development Board says Sri Lankan tableware conforms to US FDA norms and ASTM standards, with in glaze, on glaze and "
            "under glaze decoration, heavy metal free designs and microwave safe gold and platinum. The industry uses local quartz, feldspar, dolomite and china "
            "clay and employs more than 20,000 people. Main tableware markets include India, the US and Japan."),
    stats=[("US$20.76M", "tableware and kitchenware exports in 2024"), ("20,000+", "people in the ceramics industry"), ("8.4M", "pieces a year at one porcelain maker")],
    stats_src=f'Sources: Export Development Board,{ln("ceramic report 2025", CER_R)} and{ln("ceramics and porcelain", CER_PAGE)}.',
    glance=[("Main products", "Porcelain and fine china tableware, hotelware, stoneware, wall and floor tiles, clay roofing tiles, ornaments, bathware"),
            ("Main tableware markets", "India, the US, Japan, the UAE, the UK, Germany, Kenya, Italy, Australia, Mexico"),
            ("Standards", "US FDA lead and cadmium limits and ASTM; ISO 13006 for tiles; EU food contact rules"),
            ("Watch for", "Tableware exports have fallen since 2022 and the industry is concentrated")],
    products=[("Porcelain and china tableware and kitchenware", "6911"), ("Other ceramic tableware", "6912"), ("Ceramic wall and floor tiles", "6907"), ("Ornamental ceramic ware", "6913"), ("Ceramic sanitaryware", "6910")],
    names=["porcelain dinnerware", "hotel crockery", "fine china", "ceramic tiles"],
    evidence=[("Porcelain and china tableware exports were US$18.97 million in 2024, within US$20.76 million of tableware and kitchenware.", "EDB ceramic report 2025", CER_R),
              ("Sri Lankan tableware conforms to US FDA norms and ASTM standards.", "EDB", CER_TW),
              ("Decoration includes in glaze, on glaze and under glaze, heavy metal free decoration and microwave safe gold and platinum.", "EDB", CER_TW),
              ("The industry uses local quartz, feldspar, dolomite and china clay.", "EDB", CER_PAGE),
              ("One listed porcelain exporter has capacity of 8.4 million pieces a year and ships to more than 44 countries.", "EDB", CER_PAGE)],
    certs=[("Lead and cadmium leach tests.", "To US FDA limits, or EU rules for Europe, for your designs."), ("ISO 13006.", "For ceramic tiles."), ("ISO 9001 and ISO 14001.", "Held by listed tableware exporters.")],
    caveats=[("Tableware and kitchenware exports fell from US$27.45 million in 2022 to US$20.76 million in 2024.", "EDB ceramic report 2025", CER_R),
             ("The industry is concentrated in a few key tableware makers, so capacity for large hotel programmes needs early booking.", "EDB ceramic report 2025", CER_R)],
    ask=["Can you share leach test reports for these decorations?", "What is your capacity and lead time for a hotel programme?", "Can you develop my own shapes and decals?",
         "Do you hold stock patterns for repeat orders?", "How do you pack against breakage for sea freight?"],
    faqs=[("What ceramic products does Sri Lanka export?", "Porcelain and fine china tableware and kitchenware, other ceramic tableware, wall and floor tiles, roofing tiles, ornaments and bathware."),
          ("Is Sri Lankan porcelain tableware food safe?", "The Export Development Board says it conforms to US FDA norms and ASTM standards, with heavy metal free decorations available. Ask each supplier for leach test reports on your designs."),
          ("Where does Sri Lankan tableware sell?", "India, the US, Japan, the UAE, the UK, Germany, Kenya, Italy, Australia and Mexico are the top tableware markets.")],
)

cat(
    slug="wood-furniture", label="Wood products and furniture", short="Rubberwood furniture, flooring, brush handles and toys.", art="s-wood", seller="furniture manufacturer",
    h1="Furniture and wood product manufacturers in Sri Lanka",
    title="Furniture manufacturers and wood product exporters in Sri Lanka",
    desc="Source rubberwood and hardwood furniture, parquet flooring, brush handles, panels and wooden toys from Sri Lankan manufacturers. EUDR, FSC, markets and what to check.",
    answer=("Sri Lanka's wood exports are mainly furniture, parquet flooring, brush handles, wooden panels and wooden toys. Manufacturers make office, bedroom "
            "and kitchen furniture, often in treated rubberwood from rubber trees no longer tapped for latex. India bought US$17.78 million of Sri Lankan "
            "furniture and seats in 2025. For the EU, the deforestation regulation applies to wood products for large and medium operators from 30 December "
            "2026, so ask for traceability and legality evidence with every shipment."),
    stats=[("US$17.78M", "furniture and seats exported to India in 2025"), ("30 Dec 2026", "EU deforestation rule applies to wood, large and medium operators")],
    stats_src=f'Sources: Export Development Board,{ln("India market profile", IN_PROF)}; Lovguiden,{ln("EUDR timeline", EUDR)}.',
    glance=[("Main products", "Office, bedroom and kitchen furniture, ready to assemble furniture, parquet flooring, brush handles and blocks, panels, jewellery boxes, hangers, wooden toys"),
            ("Timber", "Treated rubberwood and hardwood"), ("Markets", "India, the UK, the US, Canada, Europe, Australia, New Zealand, the Middle East"),
            ("Documents to ask for", "EUDR traceability for the EU, FSC chain of custody, US Lacey Act declaration, ISPM 15 for packaging"),
            ("Watch for", "Volume and delivery capacity at smaller makers")],
    products=[("Wooden furniture", "9403"), ("Seats and chairs", "9401"), ("Tool and brush handles and brush blocks", "4417"), ("Builders' joinery and parquet flooring", "4418"),
              ("Plywood and panels", "4412"), ("Wooden boxes, hangers and handicrafts", "4420 and 4421"), ("Wooden toys", "9503")],
    names=["rubberwood furniture", "brush handles", "parquet", "wooden toys"],
    evidence=[("Sri Lanka's wood exports consist mainly of furniture, parquet flooring, brush handles, wooden panels and wooden toys.", "EDB", WOOD_WHY),
              ("Manufacturers use treated rubberwood, from rubber trees no longer productive for latex, for affordable furniture.", "EDB", WOOD_PAGE),
              ("India bought US$17.78 million of Sri Lankan furniture and seats in 2025.", "EDB India market profile", IN_PROF),
              ("The Export Development Board and a certification body ran an EU deforestation regulation readiness workshop for wood exporters in May 2026.", "EDB", "https://www.srilankabusiness.com/news/edb-and-control-union-sri-lanka-host-awareness-workshop-on-implementation-of-eu-deforestation-regulation-eudr-to-strengthen-coffee-and-wood-product-exports.html")],
    certs=[("EU deforestation regulation.", "From 30 December 2026 for large and medium operators: deforestation free, legal and traceable to the plot of land."),
           ("FSC chain of custody.", "Check the certificate code on the FSC database."), ("ISPM 15.", "For wooden pallets and crates used in the shipment."),
           ("Furniture standards.", "BIFMA for US office furniture or EN standards in Europe, where your buyers ask.")],
    caveats=[("Furniture exports to India, the largest itemised market, fell from US$25.7 million in 2023 to US$17.78 million in 2025.", "EDB India market profile", IN_PROF),
             ("Sustainability claims on official sector pages are not backed by cited evidence, so verify FSC or legality documents per supplier.", "EDB", WOOD_WHY)],
    ask=["Which timber do you use, and can you trace it to source?", "Can you provide EUDR documentation, if I sell in the EU?", "Do you hold FSC chain of custody?",
         "What is your monthly capacity, and can you ship flat pack?", "Can you build to my designs and finish standards?"],
    faqs=[("What wood products does Sri Lanka export?", "Furniture, parquet flooring, brush handles and brooms, wooden panels, plywood, builders' joinery, jewellery boxes, hangers, handicrafts and wooden toys."),
          ("What timber do Sri Lankan furniture makers use?", "Hardwood and treated rubberwood from rubber trees past their latex producing life."),
          ("Is Sri Lankan furniture ready for the EU deforestation regulation?", "The rule applies to wood products from 30 December 2026 for large and medium operators. Ask suppliers for plot level traceability and legality evidence for each shipment.")],
)


# ================================================================ order, hub chart, tenders and import guide
ORDER = ["apparel-manufacturing", "ceylon-tea", "ceylon-cinnamon", "coconut-products", "coco-peat-coir", "activated-carbon", "industrial-tyres", "rubber-gloves",
         "electrical-cables-transformers", "spices-essential-oils", "processed-food-beverages", "seafood", "gems-jewellery", "light-engineering", "boat-building",
         "fruits-vegetables", "floriculture", "ornamental-fish", "ceramics-porcelain", "printing-packaging", "wood-furniture", "leather-footwear", "graphite-minerals", "ayurveda-herbal-products"]
assert sorted(ORDER) == sorted(c["slug"] for c in CATS), "ORDER and CATS differ"
CATS.sort(key=lambda c: ORDER.index(c["slug"]))

M = "−"  # minus sign for falls
SECTORS = [  # label, link, 2025 US$ million, Jan to Sep 2026 change, note
    ("Apparel and textiles", "apparel-manufacturing/", 4909.05, f"{M}5.68%", "Activewear, intimates, swimwear, workwear, fabric"),
    ("Tea", "ceylon-tea/", 1507.19, f"{M}6.83%", "Bulk, packets, tea bags, instant"),
    ("Coconut and coconut based products", "coconut-products/", 1233.01, "+3.68%", "Food products, coco peat and coir, activated carbon"),
    ("Rubber and rubber products", "industrial-tyres/", 945.73, "+8.44%", "Solid and pneumatic tyres, gloves, seals"),
    ("Food and beverages", "processed-food-beverages/", 583.89, "+20.90%", "Processed food, beverages, animal feed"),
    ("Spices and essential oils", "spices-essential-oils/", 449.90, "+30.53%", "Cinnamon, pepper, cloves, oils, oleoresins"),
    ("Electrical and electronic components", "electrical-cables-transformers/", 438.49, "+61.05%", "Cables, transformers, switchgear, panels"),
    ("Gems, diamonds and jewellery", "gems-jewellery/", 334.13, "Not yet published", "Sapphires, spinel, cut diamonds, jewellery"),
    ("Seafood", "seafood/", 240.19, f"{M}2.03%", "Tuna, swordfish, shrimp, crab"),
    ("Ornamental fish", "ornamental-fish/", 22.60, f"{M}26.71%", "Freshwater and marine aquarium fish"),
]
BARS_SRC = (f'Sources: Export Development Board,{ln("2025 export performance", EDB25)} and{ln("January to September 2026", EDB9M)} (via Newswire); '
            f'gems from the EDB{ln("gem sector page", "https://www.srilankabusiness.com/gem-diamond-and-jewellery/")}. ICT and BPM services, US$1.64 billion in 2025, are covered in our{" "}<a href="../offshoring/">outsourcing</a> section.')

# ---------------------------------------------------------------- tender sources and requirements (no buyer is named)
UNGM_REG = "https://help.ungm.org/hc/en-us/articles/360012808340-What-are-the-requirements-for-registration-on-UNGM"
UN_VEND = "https://www.un.org/Depts/ptd/vendors"
WB_ELIG = "https://www.kplc.co.ke/storage/01J6SC6T0EX8XX1WC4JE9R1EJD.pdf"
WB_OPP = "https://thedocs.worldbank.org/en/doc/6afd2f710ab8c427b0298a274da59a69-0360012026/original/Procurement-for-Development-052026.pdf"
WB_SPD = "https://rsu-sindh.gov.pk/contents/Tenders/Bidding-Documents-For-Tablets.pdf"
ADB_POL = "https://www.adb.org/sites/default/files/institutional-document/1144596/adb-procurement-policy.pdf"
ADB_LK = "https://www.adb.org/countries/sri-lanka/overview"
AFDB = "https://www.afdb.org/en/projects-and-operations/procurement/resources-for-businesses/"
UNICEF = "https://www.unicef.org/supply/become-unicef-supplier"
NAT_EP = "https://www.bppa.gov.bd/advertisement-goods/details-87597.html"
T_TRAFO = "https://gplinc.com/pl/plc/media/201211_Tender-document-for-the-supply-of-Distribution-Transformers-GPL-PD-058-2020-final.pdf"
T_UNOPS = "https://www.ungm.org/Public/Notice/290786"
T_SPEC = "https://dded.gov.in/daman_diu_electricity_department/downloads/pdf/tenders/1307616566.pdf"
T_CABLE = "https://nawec.gm/wp-content/uploads/2026/06/INVITATION-TO-BID-ELECTRICAL-CABLES-AND-CONDUCTORS.pdf"
T_SWGR = "https://tenders.bhel.com/sites/default/files/PQR-2024-01-30-02%3A11%3A45.pdf"
T_FAT = "https://efl.com.fj/wp-content/uploads/2024/03/MR-74-2024-Tender-Specs.pdf"
T_UNIF = "https://www.ungm.org/Public/Notice/307327"
T_GLOVE = "https://www.sccl.nhs.uk/wp-content/uploads/2026/01/Schedule-A2-A-Product-Specification-Gloves-FINAL-PDF.pdf"
T_GLOVE_SE = "https://www.upphandlingsmyndigheten.se/en/criteria/nursing-and-care/medical-consumables/disposable-gloves-for-medical-use/standards-for-the-manufacture-and-inspection-of-disposable-gloves/"
WA_OPTIN = "https://developers.facebook.com/documentation/business-messaging/whatsapp/getting-opt-in"

RADAR_SOURCES = [
    ("UN agencies publish procurement on the UN Global Marketplace. Basic supplier registration asks only for general company information.", "UNGM", UNGM_REG),
    ("UN Secretariat awards above US$500,000 need Level 2 supplier registration; Basic level covers awards below US$150,000.", "UN Procurement Division", UN_VEND),
    ("The World Bank counts about 40,000 procurement opportunities a year on the projects it finances.", "World Bank", WB_OPP),
    ("Bidding documents for World Bank financed goods admit firms from all countries.", "Utility bidding document under World Bank rules", WB_ELIG),
    ("Asian Development Bank financed contracts are open to suppliers from member countries; Sri Lanka has been a member since 1966.", "Asian Development Bank", ADB_POL),
    ("Sri Lanka is not an African Development Bank member, so its exporters target contracts financed through the African Development Fund window, which is open to any country.", "African Development Bank", AFDB),
    ("UNICEF buys health, nutrition, water and sanitation and education supplies, with suppliers registering through the UN Global Marketplace.", "UNICEF", UNICEF),
    ("National utilities and government buyers publish their own tenders on national e-procurement systems. Eligibility for foreign firms varies, so read the clause in each notice.", "National e-procurement notice", NAT_EP),
]
TENDER_REQS = [
    ("A bid security, for example 2% of the bid price, by bank guarantee.", "Utility transformer tender", T_TRAFO),
    ("A performance security of 10% of the contract price if you win.", "UN power transformer tender", T_UNOPS),
    ("A manufacturer's authorisation if the bidder does not make the goods itself.", "World Bank standard bidding document", WB_SPD),
    ("Transformer type tests to IEC 60076, with reports often no older than five years.", "Utility transformer specification", T_SPEC),
    ("Cables to IEC 60502 with conductors to IEC 60228.", "Utility cable tender", T_CABLE),
    ("Switchgear panels with valid type test certificates to IEC 61439, and ISO 9001 for the factory.", "Switchgear prequalification", T_SWGR),
    ("Past supply records, for example two supplies of similar items in three years, and a minimum average turnover.", "Utility transformer tender", T_TRAFO),
    ("Guaranteed technical particulars with binding values, such as losses with no positive tolerance.", "Utility transformer tender", T_TRAFO),
    ("Factory acceptance tests witnessed by the buyer's engineers.", "Pacific utility transformer tender", T_FAT),
    ("For uniforms: manufacturer status or a letter from the manufacturer, pre production samples and a documented quality system.", "UN uniforms tender", T_UNIF),
    ("For medical gloves: EN 455 parts 1 to 4, an AQL of 1.5 for holes, and test reports from ISO/IEC 17025 accredited labs.", "Public health glove specification", T_GLOVE),
]

# ---------------------------------------------------------------- trade access and import guide
EU_LK = "https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/sri-lanka_en"
GSP_26 = "https://www.dailymirror.lk/news-features/Sri-Lanka-faces-tougher-test-to-retain-EU-GSP-benefits/131-348072"
GSP_HUB = "https://gsphub.eu/country-info/Sri%20Lanka"
ISFTA = "https://www.srilankabusiness.com/pdfs/market-access-profiles/isfta.pdf"
PSFTA = "https://www.srilankabusiness.com/pdfs/market-access-profiles/psfta.pdf"
SLSFTA = "https://www.enterprisesg.gov.sg/grow-your-business/go-global/international-agreements/free-trade-agreements/find-an-fta/slsfta"
DCTS = "https://www.srilankabusiness.com/pdfs/market-access-profiles/uk-dcts.pdf"
DCTS_ROO = "https://www.adaderana.lk/news/111648/details-of-uks-liberalised-trade-rules-for-sri-lankan-garment-sector-released"
THAI = "https://hirunews.lk/english/business/485930/review-on-free-trade-agreement-effectiveness-submitted-to-cabinet"
US_IEEPA = "https://www.ft.lk/columns/Sri-Lanka-after-IEEPA-Navigating-tariffs-in-a-volatile-US-trade-environment/4-789003"
DOC_CC = "https://www.doc.gov.lk/images/pdf/CitizenCharter/CitizenCharter1.pdf"
EDB_GG = "https://www.srilankabusiness.com/pdf/general-guidance-to-export.pdf"
NPQS = "https://doa.gov.lk/npqs-services-export/"
CUSTOMS = "https://www.customs.gov.lk/business/exporting-goods"
SLPA = "https://news.slpa.lk/?p=10083"
TRANS = "https://www.maritimegateway.com/stronger-local-trade-drives-colombo-port-throughput-growth-in-2025"
RANK = "https://www.ft.lk/front-page/Colombo-Port-surges-into-Global-Top-20/44-796542"
CONGEST = "https://www.dailymirror.lk/print/business-news/Colombo-transshipment-climbs-as-adverse-weather-threatens-to-worsen-port-congestion/273-350857"
EDB_FAQ = "https://www.srilankabusiness.com/exporters/guide/exporters-frequently-asked-questions.html"
FX = "https://newsfirst.lk/2026/06/09/cbsl-issues-new-gazette-exporters-mandated-to-convert-residual-proceeds-by-10th-of-following-month"
FX2 = "https://www.ft.lk/columns/Repatriation-of-export-proceeds-into-Sri-Lanka-and-conversion-A-practical-perspective/4-793764"
DIR = "https://www.srilankabusiness.com/edb/sri-lanka-exporters-directory.html"
BUYREG = "https://www.srilankabusiness.com/buyers/register-with-edb/"

TRADE_SHORT = [
    ("European Union: GSP+ since 2017 removes EU duties on 66% of tariff lines, including textiles and fisheries.", "European Commission", EU_LK),
    ("New EU GSP rules apply from 1 January 2027, and current beneficiaries such as Sri Lanka must reapply by 31 December 2028.", "Daily Mirror", GSP_26),
    ("United Kingdom: Enhanced Preferences under the Developing Countries Trading Scheme, with zero duty on more than 7,000 product lines.", "EDB", DCTS),
    ("India: most Sri Lankan origin goods enter duty free under a free trade agreement in force since 2000, apart from a negative list and quota items.", "EDB", ISFTA),
    ("Singapore and Pakistan: free trade agreements cover 80% of Singapore's tariff lines and give Pakistan market access with a negative list.", "Enterprise Singapore", SLSFTA),
    ("United States: in July 2026 Sri Lanka was placed in the 10% Section 301 tariff category, added on top of normal duties.", "News First", US_301),
]

GUIDE_ANSWER = ("Importing from Sri Lanka means agreeing the specification and terms with an exporter, shipping from the Port of Colombo or by air, and using a "
                "certificate of origin to claim lower duties where your country offers them. The EU removes duties on 66% of tariff lines under GSP+, the UK gives "
                "zero duty on more than 7,000 product lines, and India admits most Sri Lankan goods duty free. US imports pay a 10% Section 301 tariff on top of "
                "normal duties since July 2026. Colombo handled a record 8.29 million containers (TEUs) in 2025.")
GUIDE_STEPS = [
    ("Define what you are buying", "Product, grade, packing, labelling, quantity and the certificates you need. Ask your customs broker for the HS code and your duty rate, with and without a trade preference."),
    ("Shortlist and check exporters", "Check registration, certificates and export history. The Export Development Board's directory and our request for quote are two places to start."),
    ("Samples and price", "Approve samples in writing and agree the price on clear delivery terms, such as FOB Colombo or CIF to your port."),
    ("Contract and payment", "Agree inspection, payment terms such as a letter of credit or documents against payment, and what happens if a shipment fails inspection."),
    ("Documents", "Commercial invoice, packing list, bill of lading or air waybill, certificate of origin, and the product certificates your market needs."),
    ("Ship and clear", "Ship by sea from Colombo or by air from Bandaranaike International Airport, and clear customs with the certificate of origin to claim any preference."),
]
GUIDE_SECTIONS = [
    ("duty", "Duties and trade agreements", "Your duty depends on the product, your country and whether the goods qualify as Sri Lankan origin.", [
        ("Sri Lanka has had EU GSP+ since 19 May 2017. It fully removes EU duties on 66% of tariff lines, including textiles and fisheries.", "European Commission", EU_LK),
        ("In 2025, 69% of eligible Sri Lankan exports to the EU used GSP+; apparel was 48% of preferential imports, rubber 17% and food preparations 12%.", "GSP Hub", GSP_HUB),
        ("New EU GSP rules apply from 1 January 2027. Countries that are GSP+ beneficiaries on 31 December 2026 must reapply by 31 December 2028.", "Daily Mirror", GSP_26),
        ("Sri Lanka is in the Enhanced Preferences tier of the UK Developing Countries Trading Scheme, with zero duty on more than 7,000 product lines.", "EDB", DCTS),
        ("From early 2026, relaxed UK rules of origin let Sri Lankan garment makers use inputs from any country and keep duty free access.", "Ada Derana", DCTS_ROO),
        ("Under the India Sri Lanka Free Trade Agreement, in force since 1 March 2000, Sri Lankan origin goods enter India duty free except a negative list of 429 tariff lines and quota items such as garments, tea, pepper and desiccated coconut. Goods need at least 35% domestic value addition.", "EDB", ISFTA),
        ("The Pakistan Sri Lanka Free Trade Agreement has operated since June 2005, with a 10,000 tonne a year duty free quota for tea.", "EDB", PSFTA),
        ("The Singapore Sri Lanka Free Trade Agreement, in force since May 2018, removes tariffs on 80% of tariff lines over up to 15 years.", "Enterprise Singapore", SLSFTA),
        ("A free trade agreement with Thailand was signed in February 2024; check its status for your product before you rely on it.", "Hiru News", THAI),
        ("The US set a 20% reciprocal tariff on Sri Lanka in August 2025. After the Supreme Court struck down those tariffs in February 2026, a temporary 10% tariff applied.", "Daily FT", US_IEEPA),
        ("In July 2026 the US placed Sri Lanka in its 10% Section 301 tariff category, added on top of normal customs duties.", "News First", US_301),
    ]),
    ("documents", "Export documents you will receive", "", [
        ("The Department of Commerce issues certificates of origin under all GSP schemes and free trade agreements, usually within two hours for air and three for sea freight.", "Department of Commerce", DOC_CC),
        ("Non preferential certificates of origin come from the chambers of commerce.", "EDB", EDB_GG),
        ("The National Plant Quarantine Service issues phytosanitary certificates on the IPPC model, after the exporter registers and books an inspection.", "Department of Agriculture", NPQS),
        ("Health certificates for fish and animal products come from the animal health and fisheries authorities, and for food from the Ministry of Health's Food Control Administrative Division.", "EDB export procedure", EDB_PROC),
        ("Cinnamon and cashew need a compulsory pre shipment quality certificate.", "EDB export procedure", EDB_PROC),
        ("The export declaration is the CusDec, filed online by the exporter or a customs house agent, and goods must ship within 30 days of registration.", "Sri Lanka Customs", CUSTOMS),
    ]),
    ("shipping", "Shipping from Sri Lanka", "", [
        ("The Port of Colombo handled a record 8,291,178 TEUs in 2025.", "Sri Lanka Ports Authority", SLPA),
        ("About 80% of Colombo's container volume is transhipment, which gives direct sailings to many ports.", "Maritime Gateway", TRANS),
        ("Colombo rose to 20th among the world's container ports in the first half of 2026.", "Daily FT", RANK),
        ("In September 2026 yard operations ran at 125% of capacity, so allow for congestion in your lead times.", "Daily Mirror", CONGEST),
    ]),
    ("payment", "Payment terms", "", [
        ("Sri Lankan exporters use advance payment, letters of credit, documents against payment, documents against acceptance and open account.", "EDB", EDB_FAQ),
        ("Under documents against payment, the buyer's bank releases the shipping documents only after payment.", "EDB", EDB_FAQ),
        ("Exporters must bring export proceeds into Sri Lanka within 180 days of shipment.", "Daily FT", FX2),
        ("Since June 2026 exporters must convert remaining export proceeds into rupees by the 10th of the following month.", "News First", FX),
    ]),
    ("checks", "How to check a Sri Lankan exporter", "", [
        ("The Export Development Board's exporters directory lists each exporter's details and products. Listing is voluntary, and exporters submit certifications and clearances to be listed.", "EDB", DIR),
        ("Exporters register with Sri Lanka Customs and the Inland Revenue Department; Export Development Board registration is voluntary.", "EDB", EDB_FAQ),
        ("Foreign buyers can register with the Export Development Board for sourcing help and matchmaking.", "EDB", BUYREG),
    ]),
]
GUIDE_FAQS = [
    ("Is it duty free to import from Sri Lanka to the UK?", "Many products are. Sri Lanka is in the Enhanced Preferences tier of the UK Developing Countries Trading Scheme, with zero duty on more than 7,000 product lines, as long as the goods meet the rules of origin."),
    ("What is the import duty from Sri Lanka to India?", "Under the India Sri Lanka Free Trade Agreement, Sri Lankan origin goods enter India duty free except a negative list of 429 tariff lines and quota items such as garments, tea, pepper and desiccated coconut. Goods need at least 35% Sri Lankan value addition."),
    ("What tariff does the US charge on Sri Lankan goods?", "In July 2026 Sri Lanka was placed in the 10% Section 301 tariff category, added on top of normal customs duties. Rates have changed several times since 2025, so check the current rate with your customs broker."),
    ("Does Sri Lanka still have GSP+ with the EU?", "Yes. Sri Lanka has had GSP+ since 2017. New EU GSP rules apply from 1 January 2027, and Sri Lanka must reapply by the end of 2028."),
    ("Who issues certificates of origin in Sri Lanka?", "The Department of Commerce issues preferential certificates of origin under GSP schemes and free trade agreements; chambers of commerce issue non preferential ones."),
    ("How do I pay a Sri Lankan exporter safely?", "Letters of credit and documents against payment protect buyers best on a first order. Agree inspection before shipment, and move to open account once trust is built."),
]

HUB_FAQS = [
    ("What are Sri Lanka's main export products?", "By value in 2025: apparel and textiles (US$4.91 billion), tea (US$1.51 billion), coconut products (US$1.23 billion), rubber products (US$946 million), food and beverages (US$584 million), spices and essential oils (US$450 million), electrical and electronic components (US$438 million), gems, diamonds and jewellery (US$334 million) and seafood (US$240 million), according to the Export Development Board."),
    ("What is Sri Lanka famous for exporting?", "Ceylon tea and Ceylon cinnamon, Ceylon sapphires, coconut and coir products, solid tyres, where the Export Development Board estimates Sri Lanka has about a quarter of world demand, rubber gloves, apparel and vein graphite."),
    ("Which countries buy the most from Sri Lanka?", "In 2025 the largest markets were the US (US$3.0 billion), India (US$1.04 billion), the UK (US$929 million), Germany (US$706 million) and Italy (US$680 million)."),
    ("How do I find reliable exporters in Sri Lanka?", "Start with the product and the certificates you need, check registration and export history, and see samples before a first order. Send us a request for quote and we introduce exporters we have checked."),
    ("Does Sri Lanka have trade agreements that cut import duties?", "Yes. The EU gives GSP+ access, the UK gives Enhanced Preferences, and Sri Lanka has free trade agreements with India, Pakistan and Singapore. Our import guide covers each one."),
]

RADAR_FAQS = [
    ("Which tenders does Tender Radar cover?", "International tenders for electrical and engineering equipment, pumps and machinery, uniforms, gloves and medical rubber products, tea and food, packaging and boats, from utilities, governments, development bank financed projects, UN agencies and contractors."),
    ("Can Sri Lankan companies bid on World Bank, ADB and UN tenders?", "In most cases, yes. World Bank financed contracts are open to firms from all countries, Asian Development Bank financed contracts to member countries including Sri Lanka, and UN agencies buy through the UN Global Marketplace. African Development Bank contracts are for members, but African Development Fund financed contracts are open to any country."),
    ("Do you bid for us?", "No. You stay the bidder and every document goes out under your name. Our bid desk helps you read the tender, check your documents and prepare the bid."),
    ("Why WhatsApp?", "Because export managers read WhatsApp faster than email. You opt in to alerts, as WhatsApp's business rules require, and you can pause them any time by replying STOP. The weekly digest can come by email too."),
    ("How quickly do alerts arrive?", "We check sources every working day and send a match the day we find it, with a reminder before the deadline."),
    ("What does a typical tender ask for?", "Usually a bid security, a performance security if you win, the manufacturer's authorisation, type test reports to the relevant IEC standard, ISO 9001, past supply records and minimum turnover. The details are in each tender, and Radar flags them in every alert."),
]


def fill(g):
    for k in ("HUB_FAQS", "RADAR_FAQS", "RADAR_SOURCES", "TENDER_REQS", "GUIDE_ANSWER", "GUIDE_STEPS", "GUIDE_SECTIONS", "GUIDE_FAQS", "TRADE_SHORT"):
        g[k] = globals()[k]
