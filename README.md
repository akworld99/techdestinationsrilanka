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
