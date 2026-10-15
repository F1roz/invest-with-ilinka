# Ilinka website: launch notes

## Before you deploy
1. **Domain.** Replace `https://invest-with-ilinka.vercel.app` with the real domain in every `.html` file, `sitemap.xml`, `robots.txt` and `llms.txt` (one find and replace across the folder). To regenerate the site instead, change `BASE` in `build.py` and run `python3 build.py`.
2. **Contact.** Add Ilinka's WhatsApp number and/or email at the top of `assets/js/main.js`.
3. **Deploy.** Upload the whole folder to Vercel (or any static host). No build step is needed.

## After launch
- Submit `https://YOUR-DOMAIN/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
- Test the structured data at https://search.google.com/test/rich-results.
- Create or claim a Google Business Profile for Ilinka and link it to the site.

## SEO, GEO and AEO setup included
- Unique titles, meta descriptions, canonical URLs, Open Graph and Twitter cards on every page.
- JSON-LD: WebSite, Person, RealEstateAgent, FAQPage, Blog, BlogPosting and BreadcrumbList.
- Answer-first summaries, FAQ blocks, sources and author bios on every article.
- `llms.txt` summary for AI assistants, and `robots.txt` that allows search and AI crawlers.
- Self-hosted fonts, preloaded hero image, lazy-loaded images below the fold.

## Pages
- `/` home
- `/blog/` journal
- `/blog/off-plan-property-dubai-guide.html`
- `/blog/dubai-rental-yield-calculation.html`
- `/blog/dubai-golden-visa-property.html`
- `/blog/buy-dubai-property-from-abroad.html`
- `/404.html`
