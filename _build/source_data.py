"""Data for the Source from Sri Lanka section (seo_source.py): export categories with sourced facts, the hub,
the import guide, Tender Radar, bid support and exporter services. Every figure carries its source.
No buyer is named anywhere in this section, and exporters are described rather than named."""
from urllib.parse import quote

REVIEWED = "27 October 2026"
PUBLISHED = "2026-10-27"
WA = "94716147945"


def wa(text):
    return f"https://wa.me/{WA}?text={quote(text)}"


BOOK = "https://calendly.com/digisavvyteams/30min"

# ---------------------------------------------------------------- shared sources
EDB_2025 = "https://www.ft.lk/top-story/Export-earnings-up-5-6-to-17-2-b-in-2025/26-787471"
EDB_9M = "https://www.newswire.lk/2026/10/26/sri-lankas-exports-reach-us-13-61-bn-in-first-nine-months-of-2026/"
EDB_9M_FT = "https://www.ft.lk/top-story/Exports-hit-record-in-Sept-nine-month-earnings-at-all-time-high/26-799228"
EDB_1H = "https://www.ft.lk/front-page/Export-earnings-exceed-9-b-in-1H/44-794983"


def src2(extra=""):
    return (f'2025 figures: Export Development Board via <a href="{EDB_2025}" rel="noopener nofollow">Daily FT</a>. '
            f'2026 figures: Export Development Board via <a href="{EDB_9M}" rel="noopener nofollow">Newswire</a>.{extra}')


# ---------------------------------------------------------------- export categories
from source_cats import CATS, SECTORS, BARS_SRC  # noqa: E402,F401

HOME_TILES = ["ceylon-tea", "ceylon-cinnamon", "coco-peat-coir", "coconut-products", "activated-carbon",
              "industrial-tyres", "rubber-gloves", "apparel-manufacturing", "electrical-cables-transformers", "seafood"]

# ---------------------------------------------------------------- hub and homepage
HUB_TITLE = "Sri Lanka exporters and export products list: source from Sri Lanka (2026)"
HUB_DESC = ("Buy direct from Sri Lankan exporters: Ceylon tea and cinnamon, coconut, coco peat and coir, activated carbon, tyres and gloves, apparel, "
            "electrical cables and transformers, seafood and more. Export figures, certificates to ask for and a reply within two working days.")
HUB_ANSWER = ("Sri Lanka exported US$13.58 billion of goods in 2025. The largest categories are apparel, tea, coconut products, rubber products, "
              "processed food, spices and electrical components, and the fastest growing in 2026 are electrical and electronic components, up 61% "
              "in the first nine months, and spices, up 30.5%. Buyers in the US, India, the UK and the EU source Ceylon tea and cinnamon, coconut and "
              "coir products, industrial tyres and gloves, apparel and a widening range of electrical goods. We match buyers with Sri Lankan exporters "
              "who make what they need and check them before we introduce them.")
HUB_STATS = [("US$13.58B", "merchandise exports in 2025, up 6.32%"), ("US$10.76B", "merchandise exports, January to September 2026, up 5.35%"),
             ("+61%", "electrical and electronic components, January to September 2026")]
HUB_STATS_SRC = src2()

HOME_LEDE = ("Ceylon tea and cinnamon, coconut and coir, industrial tyres and gloves, apparel, seafood and a fast growing electrical industry. "
             "Tell us what you are buying and we introduce exporters who make it, hold your certificates and already ship to your market.")
HOME_STATS = [("US$13.58B", "goods exported from Sri Lanka in 2025"), ("+61%", "electrical and electronic exports, January to September 2026"),
              ("US$221.56M", "cinnamon exports, January to September 2026, up 31%")]

HUB_FAQS = []          # filled in source_cats
RFQ_FAQS = [
    ("Do you sell the products yourselves?", "No. We are not a trading company. Quotes, contracts, payment and shipping are agreed between you and the exporter. We find and check the exporters and stay on hand until your first shipment."),
    ("How do you choose which exporters to introduce?", "By the product and grade you need, the certificates you ask for, the markets they already ship to and their capacity for your volume. We check registration and certificates before we introduce anyone."),
    ("Can I get samples before I order?", "Yes. Most Sri Lankan exporters send samples before a first order. Agree in writing what the sample has to prove, such as grade, moisture or dimensions, so the order can be checked against it."),
    ("What if I only need a small quantity?", "Tell us anyway. Minimum orders vary by product and exporter, and some exporters accept a trial order before a full container."),
    ("Which markets do Sri Lankan exporters ship to?", "In 2025 the largest markets for Sri Lankan goods were the US, India, the UK, Germany, Italy, the Netherlands, France and Belgium, according to the Export Development Board. Many exporters also ship to the Gulf, Japan, China, Australia and Turkey."),
]

# ---------------------------------------------------------------- Tender Radar
RADAR_TITLE = "Tender alert service on WhatsApp: UN, World Bank and utility tenders"
RADAR_DESC = ("Tender Radar sends Sri Lankan exporters international tenders matched to their products, ratings and markets on WhatsApp, "
              "with deadline reminders, a weekly digest and a read on whether to bid.")
RADAR_LEDE = ("International tenders for what you make, found for you and sent to your WhatsApp. Each alert says what is being bought, "
              "by whom, by when and what the tender will ask you for, with our read on whether it is worth your time.")
SAMPLE_ALERT = [("Product", "Distribution transformers, 11 kV, 100 to 500 kVA, to IEC 60076"), ("Buyer", "National power utility, East Africa"),
                ("Quantity", "240 units in three lots"), ("Funding", "Development bank financed"), ("Closes", "In 24 days"),
                ("Asks for", "Bid security, type test reports from an accredited lab, supply records for similar units")]
SAMPLE_READ = "Fits your range. Your type tests cover 250 kVA, so check the 500 kVA lot before you bid. Reply BID for a go or no go review."
RADAR_WHY = [
    "Tenders are spread across national e-procurement portals, utility tender boards, development bank sites and UN procurement systems. Nobody on a factory floor has time to check them all.",
    "Notices are written in procurement language, often in long documents, and the clause that rules you out can sit on page 40.",
    "By the time a tender reaches you through an agent there are days left, not weeks, and no time to get type tests, guarantees and certificates in order.",
]
RADAR_STEPS = [
    ("Set your profile", "Products, ratings and sizes, the markets you can deliver to, the certificates and type tests you hold, and the smallest contract worth your time."),
    ("We scan the sources", "Utility and government tender portals, development bank and UN procurement notices, and supplier requests from contractors, every working day."),
    ("Matches reach your WhatsApp", "Only tenders that fit your profile, each with the buyer, quantity, deadline and key requirements, plus deadline reminders and a weekly digest."),
    ("Reply to act", "Reply BID for a go or no go review, DOCS for the document checklist, or STOP to pause alerts at any time."),
]
RADAR_SECTORS = [
    ("Power and electrical", "Distribution and power transformers, cables and conductors, switchgear, panels and meters for utilities, governments and contractors"),
    ("Pumps, engines and machinery", "Pumps for water and irrigation projects, generator sets, boilers and fabricated equipment"),
    ("Uniforms and apparel", "Uniforms, workwear and protective clothing for public services, health systems and large employers"),
    ("Rubber and medical supplies", "Examination, surgical and industrial gloves, and tyres for public fleets and ports"),
    ("Tea and food", "Government and institutional purchases of tea, spices and processed food"),
    ("Packaging and printing", "Cartons, labels and printed material for public bodies and international agencies"),
    ("Boats and marine", "Patrol, fisheries and passenger boats for governments and agencies"),
]
PLANS = [
    ("Radar", "For exporters who want to see what is out there.",
     ["Matched tenders on WhatsApp", "A weekly digest by WhatsApp or email", "Deadline reminders", "Matching on your products, ratings, markets and certificates"],
     "Start on WhatsApp", wa("Hi, I want Tender Radar alerts for my products.")),
    ("Radar and bid desk", "For exporters ready to bid this year.",
     ["Everything in Radar", "A go or no go review on the matches you flag", "A compliance matrix and document checklist per tender", "Bid preparation on the tenders you choose"],
     "Book a call", BOOK),
    ("Export partner", "For manufacturers building an export business.",
     ["Everything in Radar and bid desk", "Vendor registration with utilities, contractors and UN procurement", "A certification and type testing roadmap", "Buyer outreach in two target markets"],
     "Talk to us", BOOK),
]
RADAR_FAQS = []        # filled in source_cats
RADAR_SOURCES = []     # filled in source_cats
TENDER_REQS = []       # filled in source_cats

# ---------------------------------------------------------------- bid support and consultancy
BID_TITLE = "Tender consultant and bid support for Sri Lankan exporters"
BID_DESC = ("Bid support for Sri Lankan manufacturers on international tenders: go or no go reviews, compliance matrices, technical, commercial and "
            "document packs, and export consultancy on markets, vendor registration and certification.")
BID_ANSWER = ("We help Sri Lankan manufacturers bid for international tenders and build the export business around them. On a live tender we read "
              "the documents, tell you honestly whether to bid, build the compliance matrix, and prepare the technical, commercial and document packs "
              "with your team until the bid is submitted. Around the bid, we help with market selection, vendor registration, certification roadmaps "
              "and buyer outreach.")
BID_STEPS = [
    ("Read the tender", "Eligibility, qualification criteria, evaluation method, lots, deadlines and the clauses that can rule you out."),
    ("Go or no go", "A short written view on fit, gaps and the cost of bidding, so you only bid where you can win."),
    ("Ask before the deadline", "Clarification questions drafted and sent within the buyer's clarification window."),
    ("Compliance matrix", "Every requirement mapped to your evidence, clause by clause, with gaps flagged early."),
    ("Technical submission", "Guaranteed technical particulars, data sheets, drawings, type test reports and a clear list of deviations."),
    ("Commercial submission", "Price schedules, delivery terms, freight and insurance, currency and payment terms, and the bid security with your bank."),
    ("Documents and forms", "Manufacturer's authorisation, experience certificates, financial statements, ISO certificates, and notarisation or legalisation where asked."),
    ("Submit and follow up", "Upload on the procurement portal or send by courier, then answer clarifications during evaluation and prepare the performance security if you win."),
]
CONSULT = [
    ("Export readiness review.", "Where your product, documents and certificates stand against what buyers in your target markets ask for."),
    ("Certification and type testing roadmap.", "Which certificates and type tests open which tenders and markets, and in what order to get them."),
    ("Market selection.", "Where your product and price can win, using trade data and tender history."),
    ("Vendor registration.", "Supplier registration with utilities, contractors, UN procurement and e-procurement portals in your target markets."),
    ("Agents and distributors.", "Finding and checking local partners where a tender or a market needs one."),
    ("Buyer facing marketing.", "A website, catalogue and LinkedIn presence a foreign procurement team will trust, and outreach to buyers in your target markets."),
]
BID_PRINCIPLES = [
    "You stay the bidder. Every document goes out under your name and your signature.",
    "Confidential by default. We sign a non disclosure agreement before you share prices or drawings.",
    "One bidder per tender. We do not work for two competing bidders on the same tender.",
    "Honest calls. If we think a tender is not winnable, we say so before you spend money on it.",
]
BID_TEAM = ("Tech Destination Sri Lanka is run from Colombo by people with backgrounds in freight and logistics, ERP for manufacturers, and B2B demand "
            "generation for buyers in North America, Europe and Asia Pacific. We know how bids are scored, how goods leave Colombo and how overseas "
            "buyers find suppliers. For type testing, legal and banking steps we bring in specialists you deal with directly.")
BID_FAQS = [
    ("Do you write the whole bid for us?", "We can, working from your data, prices and documents. Most manufacturers keep pricing in house and use us for reading the tender, the compliance matrix, the technical pack and the final checks."),
    ("What is a go or no go review?", "A short written assessment of a tender before you commit: whether you meet the eligibility and qualification criteria, which documents you are missing, how bids will be evaluated, and what bidding will cost you in time, tests and bank guarantees."),
    ("Can you help if we have never exported?", "Yes, but start with an export readiness review. Many tenders ask for past supply records and type tests, so the first step may be a smaller tender, a contractor's approved supplier list or a distributor rather than a large utility bid."),
    ("Which tenders do you support?", "Mainly electrical and engineering equipment, uniforms and apparel, rubber and medical supplies, tea and food, packaging and boats, from utilities, governments, development bank funded projects, UN agencies and contractors."),
]

# ---------------------------------------------------------------- for exporters
EXP_TITLE = "Services for Sri Lankan exporters: buyer requests, tenders and bids"
EXP_DESC = "Services for Sri Lankan exporters: buyer requests matched to your products, Tender Radar alerts on WhatsApp, bid support and export consultancy."
EXP_ANSWER = ("Overseas buyers look for suppliers through search, procurement portals and people they trust. We put Sri Lankan exporters in front of "
              "them in three ways: buyer requests that reach us through this site, international tenders matched to what you make, and help to win both.")
EXP_SERVICES = [
    ("s-rfq", "Buyer requests", "Buyers send us requests for Sri Lankan products through this site. We match each one to exporters who make the product and hold the certificates.", "#exporter-form", "Join the network"),
    ("s-radar", "Tender Radar", "International tenders matched to your products and markets, sent to your WhatsApp with a read on whether to bid.", "../tender-radar/", "See Tender Radar"),
    ("s-bid", "Bid support", "From the go or no go review to submission: compliance matrix, technical, commercial and document packs.", "../bid-support/", "See bid support"),
    ("s-exporters", "Export consultancy", "Market selection, vendor registration, certification roadmaps, agents and distributors.", "../bid-support/", "See consultancy"),
    ("s-import", "Buyer facing marketing", "A website, catalogue and LinkedIn presence a foreign procurement team will trust, and outreach to buyers in your target markets.", "../../contact/", "Talk to us"),
    ("g-ecosystem", "Company spotlight", "A sourced feature on your company for the founders, buyers and investors who follow Tech Destination Sri Lanka.", "../../get-featured/", "Get featured"),
]
EXP_HOW = [
    "Our category pages are written for the searches overseas buyers make, such as Ceylon cinnamon suppliers or coco peat blocks, and every page ends in a request for quote.",
    "Requests are matched by product, grade, certificates, market and capacity, so you only hear about buyers you can serve.",
    "We tell you about a request first and introduce you only if you want to quote. Quotes, samples and contracts are between you and the buyer.",
]
EXP_FAQS = [
    ("What does it take to join the network?", "A registered Sri Lankan company that exports or is ready to export, the product details and certificates on the form, and a short call so we understand your capacity."),
    ("Will you share my details with buyers without asking?", "No. We tell you about a buyer request first and introduce you only if you want to quote."),
    ("Do you work with small exporters?", "Yes. Some buyer requests are for trial orders, and Tender Radar can be set to smaller contracts."),
    ("Do you only work with electrical and engineering exporters?", "No. Buyer requests cover every category on this site. Tender Radar is strongest for electrical and engineering goods, uniforms, gloves, tea, packaging and boats, where public buyers use tenders."),
]

# ---------------------------------------------------------------- import guide (filled in source_cats)
GUIDE_TITLE = "How to import from Sri Lanka: duties for the UK, EU, US and India (2026)"
GUIDE_DESC = "How to import from Sri Lanka: trade agreements and duty access, export documents, shipping from Colombo, payment terms and how to check an exporter."
GUIDE_ANSWER = ""
GUIDE_STEPS = []
GUIDE_SECTIONS = []
GUIDE_FAQS = []
TRADE_SHORT = []

from source_cats import fill  # noqa: E402
fill(globals())
