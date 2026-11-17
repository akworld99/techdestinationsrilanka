# Tech Destination Sri Lanka

Static website for Tech Destination Sri Lanka. Served by GitHub Pages from the root of the `main` branch.

## Adding or editing a story

1. Stories live in `_build/content/*.txt`. Each story is a block of `key: value` lines, a `---` line, then the article text. Blocks are separated by a line of `=====`.
2. To use the real post graphic as the cover, save it as `_build/post-images/<slug>.jpg`. Without one, a branded cover is generated.
3. Run `python3 _build/build.py` (needs Python 3 and Pillow) and commit the result.

## Settings

At the top of `_build/build.py`: `SITE_URL` (change when a custom domain is connected), `BOOKING_URL` (Cal.com or Calendly link) and `FORM_ENDPOINT` (Formspree). The booking button and contact form appear once those are filled in.

## Industry and country pages

Content for `why-sri-lanka/<industry>/` and `hire-from/<country>/` lives in `_build/seo_data.py`. Guides, Tech 50 and Tech Tour are in `_build/seo_pages.py`. Salary figures and the exchange rate are at the top of that file. Review the guides every quarter and update `REVIEWED`.

## Search engines

- `sitemap.xml` lastmod dates come from `_build/lastmod.json`, which stores a hash of each page. A page's date only moves when its content changes, so commit `lastmod.json` with every build.
- `.github/workflows/indexnow.yml` runs after each GitHub Pages deploy and submits changed URLs to IndexNow (Bing, Yandex and others). Run it by hand from the Actions tab with "Submit every URL" ticked to resubmit the whole site.
- Google does not use IndexNow. Use Search Console's sitemap report and URL Inspection for Google.

## Source from Sri Lanka

Buyer pages for Sri Lankan exports live under `source/`: a hub, one page per export category, a request for quote page, Tender Radar (tender alerts on WhatsApp), bid support, exporter services and an import guide.

- Category records (figures, HS codes, evidence, certificates, caveats, FAQs) are in `_build/source_cats.py`. Every figure carries its source link. No buyer is named, and exporters are described rather than named.
- Hub, homepage band, Tender Radar, bid support and exporter copy is in `_build/source_data.py`. Page templates are in `_build/seo_source.py` and the artwork in `_build/art_source.py`.
- Update the export figures when the Export Development Board publishes new monthly or annual numbers, and change `REVIEWED` in `source_data.py`.

## Ceylon tea prices

`source/ceylon-tea/auction-prices/` (weekly Colombo auction averages by elevation, monthly averages, CSV) and `source/ceylon-tea/green-leaf-price-calculator/` (leaf rate for bought-leaf factories), plus a latest-prices box on the Ceylon tea page.

- Every sale is in `_build/tea/weekly.csv`, from Forbes & Walker Tea Brokers' "Weekly Tea Auction Quantities & Averages". `_build/tea_data.py` checks each row before it is stored: the three elevations must add up to the total quantity and their weighted average must match the total average.
- `.github/workflows/tea-prices.yml` runs `_build/tea_update.py` every Thursday and Saturday. It finds the broker's newest copy of the file, adds new sales, rebuilds the site and commits. Run it by hand from the Actions tab at any time; the run's `tea-update-report` artifact lists every file it read and any rows it rejected.
- To run it locally: `pip install pdfplumber`, then `python3 _build/tea_update.py` and `python3 _build/build.py`.
- The build also writes a page per month (`auction-prices/october-2026/`), per year (`auction-prices/2026/`) and per elevation (`auction-prices/low-grown/`), the latest figures as JSON (`data/colombo-tea-auction-latest.json`), tea entries in llms.txt and on the Answers page. All of it regenerates from the CSV, so the weekly job keeps every page current.
- Page copy and the calculator are in `_build/seo_tea.py`. The green leaf formula follows the Tea Research Institute's 2003 description; change the defaults there if the Tea Commissioner's Division revises it.
