"""Static site generator for Ilinka's website. Run: python3 build.py"""
import json
from pathlib import Path
from html import escape

SITE = Path(__file__).parent / "site"
BASE = "https://invest-with-ilinka.vercel.app"   # change to the real domain before launch
TODAY = "2026-10-16"
IG = "https://www.instagram.com/invest.with.ilinka/"
COMPANY_IG = "https://www.instagram.com/capital.solutions.group/"

MARK = """<svg viewBox="0 0 100 140" fill="currentColor" aria-hidden="true"><path d="M10 136V64C10 37 27 17 50 5C73 17 90 37 90 64V136" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="square"/><path d="M44 20L46.6 38H41.4Z"/><rect x="41" y="38" width="6" height="85"/><rect x="37.5" y="80" width="3.5" height="43"/><rect x="55" y="54" width="3.4" height="69"/><rect x="51.5" y="54" width="10.5" height="2.2"/><rect x="28" y="121" width="48" height="3.2"/><rect x="73" y="114" width="3" height="10.2"/></svg>"""

WA_ICON = """<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3a.5.5 0 0 0 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.6-.3Z"/></svg>"""

ARCH_LINE = '<svg class="arch-line" viewBox="0 0 300 400" preserveAspectRatio="none" aria-hidden="true"><path d="M1 400V170C1 91 61 37 150 1C239 37 299 91 299 170V400"/></svg>'

# ---------------------------------------------------------------- blog content
POSTS = [
    {
        "slug": "off-plan-property-dubai-guide",
        "title": "Off plan property in Dubai: how it works for international investors",
        "short": "Off plan property in Dubai explained",
        "desc": "How buying off plan property in Dubai works: payment plans, escrow protection, Oqood registration, fees and the questions to ask before you reserve a unit.",
        "cover": ("Off plan", "Investor guide"),
        "tag": "Guide",
        "read": 7,
        "answer": "Buying off plan means you reserve a property before or during construction and pay in stages, usually with a deposit at booking, instalments during the build and a final payment at handover. In Dubai, payments for registered off plan projects go into a project escrow account, and the sale is recorded with the Dubai Land Department through the Oqood system.",
        "toc": ["What off plan means", "How payment plans work", "How buyers are protected", "Fees to budget for", "Questions to ask before you reserve"],
        "body": """
<h2 id="s1">What off plan means</h2>
<p>An off plan property is one you buy from the developer before it is finished, sometimes before construction has started. You choose a unit from plans, renders and a show apartment, sign a sale and purchase agreement and pay in stages until the building is handed over.</p>
<p>International investors choose off plan for three main reasons: a lower amount of capital needed at the start, the chance to buy at launch pricing, and a brand new property at handover. The trade off is time. Your money is committed for the length of the build, and you cannot rent the unit until it is complete.</p>

<h2 id="s2">How payment plans work</h2>
<p>Every project sets its own schedule, but most follow the same shape. A typical plan looks like this:</p>
<table>
<thead><tr><th>Stage</th><th>When</th><th>What you pay</th></tr></thead>
<tbody>
<tr><td>Booking</td><td>When you reserve</td><td>A deposit, often 10% to 20% of the price</td></tr>
<tr><td>Construction</td><td>During the build</td><td>Instalments linked to dates or to construction milestones</td></tr>
<tr><td>Handover</td><td>On completion</td><td>The remaining balance</td></tr>
<tr><td>Post handover (some projects)</td><td>After you receive the keys</td><td>Part of the balance spread over an agreed period</td></tr>
</tbody>
</table>
<p class="note">The percentages above are an illustration of a common structure, not an offer. Every developer publishes its own plan, and the version in your signed agreement is the one that counts.</p>

<h2 id="s3">How buyers are protected</h2>
<p>Dubai has specific rules for off plan sales that are worth understanding before you commit:</p>
<ul>
<li><strong>Escrow accounts.</strong> Under Dubai Law No. 8 of 2007, money paid by buyers for an off plan project goes into an escrow account dedicated to that project, and is released to the developer as construction progresses.</li>
<li><strong>Oqood registration.</strong> Off plan sales are provisionally registered with the Dubai Land Department (DLD) through the Oqood system, which records you as the buyer of the unit before the title deed exists.</li>
<li><strong>RERA oversight.</strong> The Real Estate Regulatory Agency licenses developers and brokers and oversees projects in Dubai.</li>
</ul>
<p>Protection rules reduce risk, they do not remove it. Construction can be delayed, and market prices at handover can be higher or lower than your purchase price.</p>

<h2 id="s4">Fees to budget for</h2>
<p>The largest cost on top of the price is the DLD registration fee, which is 4% of the property value. Expect smaller fixed administration fees on top. Some developers run promotions that cover part of the DLD fee, so always ask. Once the property is handed over, you will also pay yearly service charges for the building, which affect your net rental yield.</p>

<h2 id="s5">Questions to ask before you reserve</h2>
<ol>
<li>Is the project registered with the DLD, and does it have a dedicated escrow account?</li>
<li>What is the developer's record on handing over previous projects on time?</li>
<li>What is the full payment schedule, and what happens if a payment is late?</li>
<li>What are the expected service charges per square foot once the building is complete?</li>
<li>What rents are similar finished units in the same community achieving today?</li>
<li>Can the unit be resold before handover, and what conditions apply?</li>
</ol>
<p>If you would like these answers for a specific project, along with a yield and payment plan breakdown, you can <a href="../index.html#contact">book a private consultation</a>.</p>
""",
        "faq": [
            ("Can foreigners buy off plan property in Dubai?", "Yes. Foreign buyers can purchase off plan property in Dubai's designated freehold areas, whether or not they live in the UAE."),
            ("Is my off plan payment protected in Dubai?", "Payments for registered off plan projects go into a project escrow account under Dubai Law No. 8 of 2007 and are released to the developer as construction progresses. This reduces risk but does not remove it."),
            ("What fees do I pay when buying off plan in Dubai?", "The main fee is the Dubai Land Department registration fee of 4% of the property value, plus smaller administration fees. Service charges apply once the property is handed over."),
        ],
        "sources": [
            ("Nakheel: Real estate regulations and buyer protection in Dubai", "https://www.nakheel.com/en/media-centre/blogs/detail/real-estate-regulations-and-buyer-protection-in-dubai"),
            ("Khaleej Times: How non residents can buy property in Dubai", "https://www.khaleejtimes.com/business/realty/how-non-uae-residents-can-buy-property-in-dubai-heres-what-you-need-to-know"),
        ],
    },
    {
        "slug": "dubai-rental-yield-calculation",
        "title": "Gross vs net rental yield in Dubai: how to calculate your return",
        "short": "How to calculate rental yield in Dubai",
        "desc": "The simple formulas for gross and net rental yield on a Dubai property, a worked example in AED, and the costs that make the difference between the two.",
        "cover": ("Net vs<br>gross", "Yield explained"),
        "tag": "Numbers",
        "read": 5,
        "answer": "Gross rental yield is the yearly rent divided by the property price, times 100. Net rental yield subtracts yearly costs such as service charges, maintenance and management fees from the rent before dividing by the price. Net yield is the figure that shows what you actually earn.",
        "toc": ["The two formulas", "A worked example", "Costs that reduce your yield", "Reading yield figures carefully"],
        "body": """
<h2 id="s1">The two formulas</h2>
<p><strong>Gross yield</strong> = yearly rent ÷ property price × 100</p>
<p><strong>Net yield</strong> = (yearly rent minus yearly costs) ÷ property price × 100</p>
<p>Gross yield is quick and useful for comparing listings. Net yield is more honest, because it accounts for the costs every owner pays. When someone quotes a yield, always ask which one it is.</p>

<h2 id="s2">A worked example</h2>
<p>Here is an illustrative two bedroom apartment. The figures are examples to show the method, not a forecast for any real property.</p>
<table>
<thead><tr><th>Item</th><th>Amount</th></tr></thead>
<tbody>
<tr><td>Purchase price</td><td class="num">AED 1,500,000</td></tr>
<tr><td>Yearly rent</td><td class="num">AED 110,000</td></tr>
<tr><td>Yearly service charges and costs</td><td class="num">AED 18,000</td></tr>
<tr><td>Gross yield</td><td class="num">7.3%</td></tr>
<tr><td>Net yield</td><td class="num">6.1%</td></tr>
</tbody>
</table>
<p>The gross yield is 110,000 ÷ 1,500,000 × 100 = 7.3%. After costs, the owner keeps AED 92,000 a year, so the net yield is 92,000 ÷ 1,500,000 × 100 = 6.1%. You can try your own numbers in the <a href="../index.html#yield">yield calculator</a>.</p>

<h2 id="s3">Costs that reduce your yield</h2>
<ul>
<li><strong>Service charges.</strong> Paid yearly to maintain the building and shared facilities, usually charged per square foot. They vary widely between buildings.</li>
<li><strong>Property management.</strong> If an agency manages tenants for you, expect a fee, often a percentage of the rent.</li>
<li><strong>Maintenance and repairs.</strong> Air conditioning servicing, appliances and repainting between tenants.</li>
<li><strong>Vacancy.</strong> Weeks without a tenant reduce the rent you actually receive in a year.</li>
<li><strong>Purchase costs.</strong> The 4% Dubai Land Department fee and other buying costs. Some investors add these to the price when calculating yield, which gives a more conservative figure.</li>
</ul>

<h2 id="s4">Reading yield figures carefully</h2>
<p>A high yield is not automatically a better investment. It can reflect a higher vacancy risk, an older building with rising service charges or an area where prices are growing slowly. Compare yield alongside capital growth potential, the quality of the building and how easily the unit could be resold.</p>
<p>For off plan property, rent only starts after handover, so the yield is an estimate based on what similar finished units achieve today. Treat any projected yield as an estimate with assumptions, never as a guarantee.</p>
""",
        "faq": [
            ("What is a good rental yield in Dubai?", "It depends on the area, building and property type. Compare net yield rather than gross yield, and weigh it against vacancy risk, service charges and capital growth potential."),
            ("What is the difference between gross and net yield?", "Gross yield uses the yearly rent only. Net yield subtracts yearly costs such as service charges, management and maintenance before dividing by the price, so it is lower and more realistic."),
            ("Do I pay income tax on rental income in Dubai?", "The UAE does not levy personal income tax on individuals, but you may owe tax on the income in your home country. Check with a tax adviser where you are resident."),
        ],
        "sources": [
            ("Nakheel: Real estate regulations and buyer protection in Dubai", "https://www.nakheel.com/en/media-centre/blogs/detail/real-estate-regulations-and-buyer-protection-in-dubai"),
        ],
    },
    {
        "slug": "dubai-golden-visa-property",
        "title": "Dubai Golden Visa through property: what investors need to know",
        "short": "Dubai Golden Visa through property",
        "desc": "The property route to a 10 year UAE Golden Visa in Dubai: the AED 2 million threshold, off plan and mortgaged properties, joint ownership and documents.",
        "cover": ("AED 2M", "Golden Visa"),
        "tag": "Residency",
        "read": 5,
        "answer": "In Dubai, property owners can apply for a renewable 10 year UAE Golden Visa when the property they own is worth at least AED 2 million, based on its Dubai Land Department certified value. The value can come from one property or several, and off plan and mortgaged properties can qualify under conditions.",
        "toc": ["The AED 2 million threshold", "Off plan and mortgaged properties", "Joint ownership", "Documents and steps", "Before you apply"],
        "body": """
<h2 id="s1">The AED 2 million threshold</h2>
<p>The property route to the Golden Visa in Dubai is based on the total value of the property you own, as certified by the Dubai Land Department (DLD). The minimum is AED 2 million. That value can be one home or a portfolio of properties registered in your name. The visa is valid for 10 years and can be renewed.</p>

<h2 id="s2">Off plan and mortgaged properties</h2>
<ul>
<li><strong>Off plan.</strong> Off plan properties can count toward the threshold, based on the DLD certified value of the property registered in your name.</li>
<li><strong>Mortgaged.</strong> Since January 2024, mortgaged properties can qualify based on their full certified value. You will need a letter from your bank confirming the mortgage.</li>
</ul>

<h2 id="s3">Joint ownership</h2>
<p>If you own a property with someone else, your own share must be worth at least AED 2 million. A property worth AED 3 million owned equally by two people would give each owner a share of AED 1.5 million, which is below the threshold for each of them.</p>

<h2 id="s4">Documents and steps</h2>
<ol>
<li>Confirm the DLD certified value of the property or properties in your name.</li>
<li>Prepare your title deeds (or Oqood registration for off plan), passport and photograph.</li>
<li>If the property is mortgaged, get the confirmation letter from your bank.</li>
<li>Apply through the Dubai Land Department and the residency authorities, then complete the medical test and Emirates ID steps.</li>
</ol>
<p>Golden Visa holders can sponsor family members for residency. Fees and the exact list of documents change from time to time, so check the latest requirements before applying.</p>

<h2 id="s5">Before you apply</h2>
<p>Selling the property can affect renewal, so plan your holding period with the visa in mind. If residency is one of your goals, it helps to shortlist properties that reach the threshold on their own, so you are not relying on a combination of smaller units.</p>
<p class="note">This article is general information, not legal or immigration advice. Confirm current rules and fees with the Dubai Land Department and the General Directorate of Residency and Foreigners Affairs (GDRFA) before you apply.</p>
""",
        "faq": [
            ("How much property do I need to buy for a Dubai Golden Visa?", "Property with a Dubai Land Department certified value of at least AED 2 million, owned in one property or across several."),
            ("Does an off plan property qualify for the Golden Visa?", "Yes, off plan property can qualify based on the DLD certified value of the property registered in your name."),
            ("Can I get a Golden Visa with a mortgaged property?", "Yes. Since January 2024 mortgaged property can qualify based on its full certified value, with a letter from your bank."),
        ],
        "sources": [
            ("Property Finder Help Centre: How to get a UAE Golden Visa through Dubai property", "https://help.propertyfinder.ae/hc/en-us/articles/37816365548946-How-to-get-a-UAE-Golden-Visa-through-Dubai-property"),
        ],
    },
    {
        "slug": "buy-dubai-property-from-abroad",
        "title": "How to buy property in Dubai from abroad, step by step",
        "short": "Buying Dubai property from abroad",
        "desc": "A clear step by step guide for overseas buyers: where foreigners can buy, the documents you need, fees, and how to complete a Dubai purchase without living in the UAE.",
        "cover": ("4%", "DLD fee"),
        "tag": "Guide",
        "read": 6,
        "answer": "Non residents can buy property in Dubai's designated freehold areas with a valid passport. The main steps are: set your goals and budget, shortlist properties, check the seller or developer, sign the sale agreement, pay the deposit and fees, and register the sale with the Dubai Land Department. Much of this can be done remotely, with a power of attorney if someone signs for you.",
        "toc": ["Where foreigners can buy", "The steps", "Documents you will need", "Fees to plan for", "Buying without flying in"],
        "body": """
<h2 id="s1">Where foreigners can buy</h2>
<p>Under Dubai Law No. 7 of 2006, foreign buyers can own property in areas designated for foreign ownership, known as freehold areas. Freehold ownership covers the property and the land and is not limited in time. Freehold areas include Downtown Dubai, Dubai Marina, Business Bay, Palm Jumeirah, Jumeirah Village and Arabian Ranches, among others. You do not need to live in the UAE to buy.</p>

<h2 id="s2">The steps</h2>
<ol>
<li><strong>Set your goals.</strong> Decide whether you want rental income, capital growth, residency or a home for yourself. This shapes everything else.</li>
<li><strong>Shortlist properties.</strong> Compare locations, building quality, payment plans and net yield.</li>
<li><strong>Check the seller or developer.</strong> Confirm that the seller owns the property and that it has no outstanding mortgage, or that the developer and project are registered.</li>
<li><strong>Sign the sale agreement.</strong> For resale, this is the standard contract issued by the Dubai Land Department. For off plan, it is the developer's sale and purchase agreement.</li>
<li><strong>Pay the deposit and fees.</strong> Payments go through traceable bank transfers or cheques, never cash.</li>
<li><strong>Register the sale.</strong> The transfer is registered with the Dubai Land Department at a registration trustee office, or through Oqood for off plan.</li>
</ol>

<h2 id="s3">Documents you will need</h2>
<ul>
<li>A valid passport (Emirates ID if you are a UAE resident)</li>
<li>The signed sale agreement</li>
<li>A no objection certificate from the developer, for resale properties in freehold communities</li>
<li>A power of attorney, if someone is signing on your behalf</li>
<li>Company documents, if you are buying through a company</li>
</ul>

<h2 id="s4">Fees to plan for</h2>
<table>
<thead><tr><th>Fee</th><th>Typical amount</th></tr></thead>
<tbody>
<tr><td>Dubai Land Department fee</td><td>4% of the property value</td></tr>
<tr><td>Registration trustee fee</td><td>AED 2,000 or 4,000 plus VAT, depending on the price</td></tr>
<tr><td>Title deed and admin fees</td><td>Smaller fixed amounts</td></tr>
<tr><td>Agency commission (resale)</td><td>Agreed with your agent</td></tr>
</tbody>
</table>
<p class="note">Fees change over time and some developers cover part of them on new launches. Confirm the full list for your purchase before you sign.</p>

<h2 id="s5">Buying without flying in</h2>
<p>Many international investors complete their purchase without visiting. Viewings can be done by video, contracts can be signed digitally or through a power of attorney, and payments are made by international transfer. For off plan purchases, the developer usually handles the Oqood registration. Visiting at least once before handover is still worthwhile if you can.</p>
<p>If you are planning a purchase from overseas, <a href="../index.html#contact">book a private consultation</a> and we can map out each step for your situation.</p>
""",
        "faq": [
            ("Can I buy property in Dubai without a residency visa?", "Yes. Non residents can buy in Dubai's freehold areas using a valid passport. Residency is not required to own property."),
            ("Can I buy Dubai property without visiting?", "Yes. Viewings can be done by video, documents signed digitally or through a power of attorney, and payments made by international bank transfer."),
            ("What is the Dubai Land Department fee?", "The DLD fee is 4% of the property value, plus smaller administration and registration trustee fees."),
        ],
        "sources": [
            ("Khaleej Times: How non residents can buy property in Dubai", "https://www.khaleejtimes.com/business/realty/how-non-uae-residents-can-buy-property-in-dubai-heres-what-you-need-to-know"),
            ("Nakheel: Real estate regulations and buyer protection in Dubai", "https://www.nakheel.com/en/media-centre/blogs/detail/real-estate-regulations-and-buyer-protection-in-dubai"),
        ],
    },
]

HOME_FAQ = [
    ("Can I invest in Dubai property from abroad?", "Yes. Foreign buyers can purchase in Dubai's designated freehold areas without living in the UAE, and much of the process can be handled remotely."),
    ("What does off plan mean?", "You buy a property before or during construction and pay in stages, usually a deposit, instalments during the build and the balance at handover."),
    ("How much do I need to start?", "It depends on the project and its payment plan. In a private consultation we map options to your exact budget and goals."),
    ("Can property in Dubai lead to a Golden Visa?", "Owning property with a Dubai Land Department certified value of at least AED 2 million can make you eligible to apply for a renewable 10 year UAE Golden Visa."),
    ("Is the first consultation free?", "Yes. The first private consultation is free and there is no obligation."),
]

# ---------------------------------------------------------------- shared parts
NAV = [("index.html#about", "About"), ("index.html#services", "Services"), ("index.html#yield", "ROI calculator"), ("blog/index.html", "Journal"), ("index.html#faq", "FAQ")]


def header(r, current=""):
    links = "".join(
        f'<a href="{r}{href}"{" aria-current=\"page\"" if label == current else ""}>{label}</a>' for href, label in NAV)
    dlinks = "".join(
        f'<a href="{r}{href}"{" aria-current=\"page\"" if label == current else ""}>{label}<small>{sub}</small></a>'
        for (href, label), sub in zip(NAV + [("index.html#contact", "Contact")], ["Meet Ilinka", "What I offer", "Estimate a yield", "Insights", "Answers", "Book a call"]))
    return f"""
<a class="skip" href="#main">Skip to content</a>
<header class="header">
  <div class="header-inner">
    <a class="brand" href="{r}index.html" aria-label="Ilinka, Dubai Real Estate Consultant, home">
      <span class="brand-mark">{MARK}</span>
      <span class="brand-text"><span class="brand-name">ILINKA</span><span class="brand-sub">DUBAI REAL ESTATE CONSULTANT</span></span>
    </a>
    <nav class="nav-links" aria-label="Main">{links}<a class="btn btn-gold" href="{r}index.html#contact">Book a consultation</a></nav>
    <button class="burger" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="drawer" id="drawer" aria-label="Menu">
  <nav class="drawer-links" aria-label="Mobile">{dlinks}</nav>
  <div class="drawer-foot">
    <a class="btn btn-gold" href="{r}index.html#contact">Book a private consultation</a>
    <div class="drawer-social"><a href="{IG}" target="_blank" rel="noopener">Instagram</a><a href="{r}index.html#contact" data-wa>WhatsApp</a><span>Dubai, UAE</span></div>
  </div>
</div>
<div class="actionbar" aria-label="Quick actions">
  <a class="btn btn-gold" href="{r}index.html#contact">Book a consultation</a>
  <a class="btn btn-ghost wa" href="{r}index.html#contact" data-wa aria-label="Message on WhatsApp">{WA_ICON}</a>
</div>
<div class="cursor is-hidden" aria-hidden="true">
  <svg class="cursor-arch" viewBox="0 0 300 400" preserveAspectRatio="none"><path d="M6 398V172C6 95 63 42 150 6C237 42 294 95 294 172V398Z"/></svg>
  <span class="cursor-dot"></span><span class="cursor-label"></span>
</div>"""


def footer(r):
    posts = "".join(f'<li><a href="{r}blog/{p["slug"]}.html">{p["short"]}</a></li>' for p in POSTS)
    return f"""
<footer class="footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <a class="brand" href="{r}index.html" aria-label="Ilinka, home"><span class="brand-mark">{MARK}</span><span class="brand-text"><span class="brand-name">ILINKA</span><span class="brand-sub">DUBAI REAL ESTATE CONSULTANT</span></span></a>
        <p class="footer-about">Ilinka is a real estate consultant at Capital Solutions Group in Dubai, helping international investors buy off plan and luxury property.</p>
      </div>
      <div><h3>Explore</h3><ul><li><a href="{r}index.html#about">About Ilinka</a></li><li><a href="{r}index.html#services">Services</a></li><li><a href="{r}index.html#yield">ROI calculator</a></li><li><a href="{r}index.html#process">Process</a></li><li><a href="{r}index.html#contact">Contact</a></li></ul></div>
      <div><h3>Journal</h3><ul>{posts}</ul></div>
      <div><h3>Connect</h3><ul><li><a href="{IG}" target="_blank" rel="noopener">Instagram</a></li><li><a href="{COMPANY_IG}" target="_blank" rel="noopener">Capital Solutions Group</a></li><li><a href="{r}index.html#contact" data-wa>WhatsApp</a></li></ul></div>
    </div>
    <div class="footer-base">
      <p>Information on this website is general and is not financial, legal or tax advice. Property values and rental income can fall as well as rise. Estimated returns are illustrations based on stated assumptions.</p>
      <p>© <span id="year">2026</span> Ilinka. Dubai, UAE.</p>
    </div>
  </div>
</footer>
<script src="{r}assets/js/main.js" defer></script>"""


def head(r, title, desc, path, og_type="website", schema=None, preload=""):
    url = f"{BASE}/{path}".replace("/index.html", "/")
    ld = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>' if schema else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="Ilinka">
<meta name="theme-color" content="#101114">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Ilinka | Dubai Real Estate Consultant">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/img/og-image.jpg">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(desc)}">
<meta name="twitter:image" content="{BASE}/assets/img/og-image.jpg">
<link rel="icon" href="{r}assets/img/ilinka-mark.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/img/ilinka-avatar.webp">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="alternate" type="text/plain" title="LLM summary" href="{r}llms.txt">
<link rel="preload" href="{r}assets/fonts/playfair-display-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{r}assets/fonts/montserrat-latin-500-normal.woff2" as="font" type="font/woff2" crossorigin>
{preload}
<link rel="stylesheet" href="{r}assets/css/styles.css">
{ld}
</head>"""


PERSON = {
    "@type": "Person", "@id": f"{BASE}/#ilinka", "name": "Ilinka",
    "jobTitle": "Real Estate Consultant",
    "description": "Dubai real estate consultant helping international investors buy off plan and luxury property.",
    "image": f"{BASE}/assets/img/ilinka-portrait.webp", "url": f"{BASE}/",
    "worksFor": {"@type": "Organization", "name": "Capital Solutions Group", "sameAs": COMPANY_IG},
    "workLocation": {"@type": "Place", "name": "Dubai, United Arab Emirates"},
    "knowsAbout": ["Dubai real estate", "Off plan property", "Luxury property", "Rental yield", "UAE Golden Visa", "Property investment for international buyers"],
    "sameAs": [IG],
}


def faq_schema(faq):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def faq_html(faq):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)


def card(p, r):
    big, small = p["cover"]
    return f"""<a class="card" href="{r}blog/{p['slug']}.html" data-cursor="Read">
  <div class="cover"><div class="cover-top"><span>{p['tag']}</span><span>{p['read']} min</span></div>
  <p class="cover-big" aria-hidden="true">{big}<small>{small}</small></p><span class="cover-foot"></span></div>
  <div class="card-body"><h3>{p['title']}</h3><p>{p['desc']}</p><span class="card-meta">Read the article</span></div>
</a>"""


ICONS = {
    "building": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M8 42h32M12 42V14l12-6v34M24 16h12v26M16 18h4M16 24h4M16 30h4M28 22h4M28 28h4M28 34h4M16 36h4"/></svg>',
    "diamond": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M14 10h20l8 10-18 20L6 20zM6 20h36M18 10l-4 10 10 20 10-20-4-10"/></svg>',
    "chart": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><path d="M8 42h34M12 42V30h6v12M22 42V24h6v12M32 42V18h6v24M10 24l10-8 8 4 14-10M36 10h6v6"/></svg>',
    "globe": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true"><circle cx="24" cy="24" r="17"/><path d="M7 24h34M24 7c5 5 7 11 7 17s-2 12-7 17c-5-5-7-11-7-17s2-12 7-17ZM10 15h28M10 33h28"/></svg>',
}


# ---------------------------------------------------------------- home
def build_home():
    r = ""
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": f"{BASE}/#website", "url": f"{BASE}/", "name": "Ilinka | Dubai Real Estate Consultant", "inLanguage": "en", "publisher": {"@id": f"{BASE}/#ilinka"}},
        PERSON,
        {"@type": "RealEstateAgent", "@id": f"{BASE}/#agent", "name": "Ilinka, Dubai Real Estate Consultant", "url": f"{BASE}/",
         "image": f"{BASE}/assets/img/ilinka-portrait.webp", "logo": f"{BASE}/assets/img/ilinka-mark.svg",
         "description": "Off plan and luxury real estate consultancy in Dubai for international investors, with yield breakdowns, developer access and support from consultation to handover.",
         "employee": {"@id": f"{BASE}/#ilinka"}, "parentOrganization": {"@type": "Organization", "name": "Capital Solutions Group"},
         "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"},
         "areaServed": [{"@type": "City", "name": "Dubai"}, {"@type": "Country", "name": "United Arab Emirates"}],
         "sameAs": [IG],
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
             {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in ["Off plan property advisory", "Luxury property search", "Rental yield and ROI analysis", "Support for overseas investors"]]}},
        {"@type": "WebPage", "@id": f"{BASE}/#webpage", "url": f"{BASE}/", "name": "Ilinka | Dubai Real Estate Consultant for International Investors", "isPartOf": {"@id": f"{BASE}/#website"}, "about": {"@id": f"{BASE}/#agent"}, "dateModified": TODAY,
         "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".hero-intro", ".meet-copy .quote"]}},
        faq_schema(HOME_FAQ),
    ]}
    pre = '<link rel="preload" as="image" href="assets/img/dubai-skyline-dusk.webp" media="(min-width: 921px)" fetchpriority="high">\n<link rel="preload" as="image" href="assets/img/dubai-skyline-dusk-small.webp" media="(max-width: 920px)" fetchpriority="high">'
    cards = "".join(card(p, r) for p in POSTS[:3])
    html = head(r, "Ilinka | Dubai Real Estate Consultant for International Investors",
                "Ilinka is a Dubai real estate consultant at Capital Solutions Group, helping global investors buy off plan and luxury property with clear ROI breakdowns.",
                "index.html", schema=schema, preload=pre) + f"""
<body>
{header(r)}
<main id="main">

<section class="hero" aria-labelledby="hero-title">
  <div class="hero-media">
    <picture>
      <source media="(max-width: 920px)" srcset="assets/img/dubai-skyline-dusk-small.webp">
      <img src="assets/img/dubai-skyline-dusk.webp" alt="Dubai skyline at dusk with the Burj Khalifa" width="1029" height="941" fetchpriority="high">
    </picture>
  </div>
  <div class="hero-inner">
    <div class="hero-copy">
      <span class="label">Dubai</span>
      <h1 id="hero-title"><span>Your Next</span><span>Investment</span><span>Destination</span></h1>
      <hr class="rule">
      <p class="hero-tag">Prime properties.<br>Stronger returns.</p>
      <p class="hero-intro">I'm Ilinka, a real estate consultant at Capital Solutions Group. I help international investors buy off plan and luxury property in Dubai, with the numbers clear before they commit.</p>
      <div class="hero-actions">
        <a class="btn btn-gold" href="#contact">Book a private consultation</a>
        <a class="btn btn-ghost" href="#yield">Estimate your ROI</a>
      </div>
    </div>
  </div>
  <a class="consultant" href="#about">
    <img src="assets/img/ilinka-avatar.webp" alt="" width="52" height="52">
    <span><b>Ilinka</b><small>Consultant at Capital Solutions Group</small></span>
  </a>
  <div class="hero-strip"><ul><li>Invest</li><li>Grow</li><li>Build your future</li></ul><span>Off plan and luxury real estate</span></div>
</section>

<section class="sec light" id="about" aria-labelledby="about-title">
  <div class="wrap meet">
    <div class="meet-media">
      <div class="arch"><img src="assets/img/ilinka-portrait.webp" alt="Portrait of Ilinka, Dubai real estate consultant" width="675" height="880" loading="lazy">{ARCH_LINE}</div>
    </div>
    <div class="meet-copy">
      <span class="label">Meet your consultant</span>
      <h2 class="h2" id="about-title">I'm Ilinka. I help investors see the numbers before they choose the view.</h2>
      <p>Dubai moves fast, and most overseas buyers are shown listings rather than a strategy. Finding the right property takes data, a plan and someone on the ground you can trust.</p>
      <p>As a Property Consultant at Capital Solutions Group, I work closely with international investors to clear the noise and find properties that fit their financial goals. Through our direct access to Dubai's leading developers and new off plan launches, you see the strongest options and the most flexible payment plans.</p>
      <blockquote class="quote">“My mission is to help global investors secure high yield real estate and maximise their capital growth.”</blockquote>
      <dl class="facts">
        <div><dt>Based in</dt><dd>Dubai, UAE</dd></div>
        <div><dt>Focus</dt><dd>Off plan and luxury</dd></div>
        <div><dt>Clients</dt><dd>Global investors</dd></div>
      </dl>
    </div>
  </div>
</section>

<section class="sec light-2" id="services" aria-labelledby="offer-title">
  <div class="wrap">
    <div class="offer-head">
      <div><span class="label">What I offer</span><h2 class="h2" id="offer-title">Four ways I help you invest</h2></div>
      <a class="btn btn-ghost" href="#contact">Discuss your goals</a>
    </div>
    <div class="offer-grid">
      <article class="offer-item">{ICONS['building']}<h3>Off plan properties</h3><p>Early access to new launches and flexible payment plans, with escrow and registration checked.</p></article>
      <article class="offer-item">{ICONS['diamond']}<h3>Luxury real estate</h3><p>Curated residences in established and emerging communities, matched to how you will use them.</p></article>
      <article class="offer-item">{ICONS['chart']}<h3>Maximise ROI</h3><p>Yield, service charges and payment plans broken down for every property on your shortlist.</p></article>
      <article class="offer-item">{ICONS['globe']}<h3>Global investors</h3><p>One point of contact from consultation to handover, so you can invest from anywhere.</p></article>
    </div>
  </div>
</section>

<section class="band" aria-labelledby="band-title">
  <div class="band-media"><img src="assets/img/dubai-terrace-view.webp" alt="Luxury terrace overlooking the Dubai skyline and water" width="943" height="852" loading="lazy"></div>
  <div class="wrap">
    <div class="band-copy">
      <h2 id="band-title"><span>Luxury Living.</span><span>Smarter Investing.</span></h2>
      <hr class="rule">
      <p>A beautiful view is only half the decision. The other half is the payment plan, the service charges and what similar homes rent for. I bring both to every shortlist.</p>
      <span class="label">Off plan and luxury real estate</span>
    </div>
  </div>
</section>

<section class="sec" id="yield" aria-labelledby="yield-title">
  <div class="wrap calc" id="calc">
    <div class="calc-copy">
      <span class="label">ROI calculator</span>
      <h2 class="h2" id="yield-title">Estimate your rental yield</h2>
      <p class="lead">Enter a price, the yearly rent you expect and yearly costs. The arch fills as the yield rises.</p>
      <div class="calc-fields">
        <div class="field"><label for="price">Property price</label><div class="money"><span>AED</span><input id="price" type="number" inputmode="numeric" min="0" step="10000" value="1500000"></div></div>
        <div class="field"><label for="rent">Expected yearly rent</label><div class="money"><span>AED</span><input id="rent" type="number" inputmode="numeric" min="0" step="1000" value="110000"></div></div>
        <div class="field"><label for="costs">Yearly service charges and costs</label><div class="money"><span>AED</span><input id="costs" type="number" inputmode="numeric" min="0" step="1000" value="18000"></div></div>
      </div>
    </div>
    <div class="dial" aria-live="polite">
      <div class="dial-face">
        <svg viewBox="0 0 240 170" aria-hidden="true">
          <path class="d-track" d="M24 166V100C24 58 64 28 120 10C176 28 216 58 216 100V166"/>
          <path class="d-gross" id="dGross" pathLength="100" d="M24 166V100C24 58 64 28 120 10C176 28 216 58 216 100V166"/>
          <path class="d-net" id="dNet" pathLength="100" d="M40 166V102C40 66 74 42 120 26C166 42 200 66 200 102V166"/>
        </svg>
        <div class="dial-read"><span class="num" id="netYield">6.1%</span><small>Estimated net yield</small></div>
      </div>
      <div class="legend"><span><i style="background:#C6A15B"></i>Gross</span><span><i style="background:#C7B69D"></i>Net</span><span>Full arch: 12%</span></div>
      <dl>
        <div><dt>Gross yield</dt><dd class="num" id="grossYield">7.3%</dd></div>
        <div><dt>Net yearly income</dt><dd class="num" id="netIncome">AED 92,000</dd></div>
      </dl>
      <p class="fine">An illustrative estimate, not financial advice or a guaranteed return. Real results depend on the property, occupancy, service charges and the market. <a href="blog/dubai-rental-yield-calculation.html" style="color:#C6A15B">How yield is calculated</a></p>
    </div>
  </div>
</section>

<section class="sec light" id="process" aria-labelledby="process-title">
  <div class="wrap">
    <div class="process-head"><span class="label">How it works</span><h2 class="h2" id="process-title">From first call to handover</h2></div>
    <ol class="steps">
      <li class="step"><span class="step-n">1</span><h3>Private consultation</h3><p>We talk through your budget, timeline and whether you want income, growth or residency.</p></li>
      <li class="step"><span class="step-n">2</span><h3>Strategy and shortlist</h3><p>You receive a focused shortlist, each property with a yield and payment plan breakdown.</p></li>
      <li class="step"><span class="step-n">3</span><h3>Reserve your unit</h3><p>I guide you through reservation, contracts, payments and registration with the developer.</p></li>
      <li class="step"><span class="step-n">4</span><h3>Through to handover</h3><p>Construction updates, handover and next steps such as leasing or resale.</p></li>
    </ol>
  </div>
</section>

<section class="sec light-2" id="journal" aria-labelledby="journal-title">
  <div class="wrap">
    <div class="journal-head"><div><span class="label">The journal</span><h2 class="h2" id="journal-title">Insights for Dubai investors</h2></div><a class="btn btn-ghost" href="blog/index.html">All articles</a></div>
    <div class="cards">{cards}</div>
  </div>
</section>

<section class="sec" id="faq" aria-labelledby="faq-title">
  <div class="wrap faq-grid">
    <div><span class="label">FAQ</span><h2 class="h2" id="faq-title">Questions investors ask</h2><p class="lead" style="margin-top:18px">Short answers to the questions I hear most. For anything specific to your situation, book a consultation.</p></div>
    <div class="faq-list">{faq_html(HOME_FAQ)}</div>
  </div>
</section>

<section class="sec" id="contact" aria-labelledby="contact-title" style="padding-top:0">
  <div class="wrap contact">
    <div class="contact-visual"><img src="assets/img/consultation-notebook.webp" alt="Black notebook with the Ilinka monogram and a gold pen" width="668" height="624" loading="lazy"><p>Your Goals.<br>My Priority.</p></div>
    <div class="contact-form">
      <span class="label">Private consultation</span>
      <h2 class="h2" id="contact-title">Let's plan your next investment</h2>
      <p>Tell me a little about what you're looking for. I'll reply to arrange a free, no obligation consultation.</p>
      <form class="form" id="consultForm">
        <div class="field"><label for="fName">Your name</label><input id="fName" name="name" autocomplete="name" required></div>
        <div class="field"><label for="fEmail">Email</label><input id="fEmail" name="email" type="email" autocomplete="email" required></div>
        <div class="row">
          <div class="field"><label for="fBudget">Budget</label><select id="fBudget" name="budget" required><option value="">Choose a range</option><option>Under AED 1M</option><option>AED 1M to 2M</option><option>AED 2M to 5M</option><option>Above AED 5M</option></select></div>
          <div class="field"><label for="fGoal">Main goal</label><select id="fGoal" name="goal" required><option value="">Choose a goal</option><option>Rental income</option><option>Capital growth</option><option>Golden Visa</option><option>A home for me</option></select></div>
        </div>
        <div class="field"><label for="fMsg">Anything else? <span class="opt">(optional)</span></label><textarea id="fMsg" name="message" rows="3"></textarea></div>
        <button class="btn btn-gold" type="submit">Request my consultation</button>
        <p class="form-note" id="formNote" role="status"></p>
      </form>
      <div class="contact-alt"><a href="{IG}" target="_blank" rel="noopener">DM on Instagram</a><a href="#contact" data-wa>Message on WhatsApp</a></div>
    </div>
  </div>
</section>
</main>
{footer(r)}
</body>
</html>"""
    (SITE / "index.html").write_text(html)


# ---------------------------------------------------------------- blog
def build_blog_index():
    r = "../"
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "@id": f"{BASE}/blog/#blog", "url": f"{BASE}/blog/", "name": "The Journal by Ilinka", "description": "Guides on Dubai off plan property, rental yield, Golden Visa and buying from abroad.", "author": {"@id": f"{BASE}/#ilinka"}, "publisher": PERSON,
         "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f"{BASE}/blog/{p['slug']}.html", "datePublished": TODAY} for p in POSTS]},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"}, {"@type": "ListItem", "position": 2, "name": "Journal", "item": f"{BASE}/blog/"}]},
    ]}
    cards = "".join(card(p, r) for p in POSTS)
    html = head(r, "The Journal | Dubai Property Insights by Ilinka",
                "Clear guides for international investors on Dubai off plan property, rental yield, the Golden Visa and buying from abroad.",
                "blog/index.html", schema=schema) + f"""
<body>
{header(r, "Journal")}
<main id="main">
  <section class="page-hero">
    <div class="wrap">
      <ol class="crumbs" aria-label="Breadcrumb"><li><a href="../index.html">Home</a></li><li aria-current="page">Journal</li></ol>
      <span class="label">The journal</span>
      <h1>Insights for Dubai investors</h1>
      <p class="lead">Plain answers to the questions international buyers ask, from how off plan works to what a yield figure really means.</p>
    </div>
  </section>
  <section class="sec light"><div class="wrap"><div class="cards">{cards}</div></div></section>
  <section class="sec" style="text-align:center"><div class="wrap" style="max-width:720px">
    <h2 class="h2">Have a question about a specific project?</h2>
    <p class="lead" style="margin:18px auto 30px">Book a free private consultation and get a yield and payment plan breakdown for the properties you are considering.</p>
    <a class="btn btn-gold" href="../index.html#contact">Book a consultation</a>
  </div></section>
</main>
{footer(r)}
</body>
</html>"""
    (SITE / "blog" / "index.html").write_text(html)


def build_post(p):
    r = "../"
    url = f"{BASE}/blog/{p['slug']}.html"
    words = len(p["body"].split())
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "BlogPosting", "@id": f"{url}#article", "headline": p["title"], "description": p["desc"], "url": url,
         "mainEntityOfPage": url, "datePublished": TODAY, "dateModified": TODAY, "inLanguage": "en", "wordCount": words,
         "image": f"{BASE}/assets/img/og-image.jpg", "author": {"@type": "Person", "@id": f"{BASE}/#ilinka", "name": "Ilinka", "url": f"{BASE}/#about", "jobTitle": "Real Estate Consultant"},
         "publisher": {"@type": "Person", "@id": f"{BASE}/#ilinka", "name": "Ilinka"}, "isPartOf": {"@id": f"{BASE}/blog/#blog"},
         "about": ["Dubai real estate"], "citation": [u for _, u in p["sources"]]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": "Journal", "item": f"{BASE}/blog/"},
            {"@type": "ListItem", "position": 3, "name": p["short"], "item": url}]},
        faq_schema(p["faq"]),
    ]}
    toc = "".join(f'<li><a href="#s{i + 1}">{t}</a></li>' for i, t in enumerate(p["toc"]))
    srcs = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for t, u in p["sources"])
    faq = faq_html(p["faq"])
    related = "".join(card(q, r) for q in POSTS if q["slug"] != p["slug"])
    html = head(r, f"{p['title']} | Ilinka", p["desc"], f"blog/{p['slug']}.html", og_type="article", schema=schema) + f"""
<body>
{header(r, "Journal")}
<main id="main">
  <article>
    <header class="page-hero article-hero">
      <div class="wrap">
        <ol class="crumbs" aria-label="Breadcrumb"><li><a href="../index.html">Home</a></li><li><a href="index.html">Journal</a></li><li aria-current="page">{p['short']}</li></ol>
        <span class="label">{p['tag']}</span>
        <h1>{p['title']}</h1>
        <div class="byline"><img src="../assets/img/ilinka-avatar.webp" alt="" width="48" height="48"><span>By <b>Ilinka</b>, Real Estate Consultant at Capital Solutions Group<br><time datetime="{TODAY}">16 October 2026</time> · {p['read']} minute read</span></div>
      </div>
    </header>
    <section class="sec light">
      <div class="wrap article">
        <div class="prose">
          <div class="answer"><strong>Short answer</strong><p>{p['answer']}</p></div>
          {p['body']}
          <h2 id="faq">Frequently asked questions</h2>
          <div class="faq-list">{faq}</div>
          <h2 id="sources">Sources</h2>
          <ul class="sources">{srcs}</ul>
          <p class="note">This article is general information, not financial, legal or tax advice. Rules and fees can change, so confirm the current position with the Dubai Land Department or a qualified adviser before acting.</p>
          <div class="author">
            <img src="../assets/img/ilinka-avatar.webp" alt="Ilinka" width="96" height="96">
            <div><h2>Written by Ilinka</h2><p>Real Estate Consultant at Capital Solutions Group in Dubai. Ilinka helps international investors buy off plan and luxury property with clear yield and payment plan breakdowns. <a href="../index.html#contact">Book a consultation</a>.</p></div>
          </div>
        </div>
        <aside class="toc" aria-label="On this page">
          <span class="label">On this page</span>
          <ol>{toc}<li><a href="#faq">FAQ</a></li></ol>
          <a class="btn btn-gold" href="../index.html#contact">Book a consultation</a>
        </aside>
      </div>
    </section>
  </article>
  <section class="sec light-2 related" aria-labelledby="more-title">
    <div class="wrap"><div class="journal-head"><h2 class="h2" id="more-title">Keep reading</h2><a class="btn btn-ghost" href="index.html">All articles</a></div><div class="cards">{related}</div></div>
  </section>
</main>
{footer(r)}
</body>
</html>"""
    (SITE / "blog" / f"{p['slug']}.html").write_text(html)


def build_misc():
    r = ""
    (SITE / "404.html").write_text(head(r, "Page not found | Ilinka", "This page could not be found.", "404.html").replace(
        '<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">') + f"""
<body>
{header("/")}
<main id="main" class="lost"><div><img src="/assets/img/ilinka-mark.svg" alt=""><h1>This page has moved or never existed.</h1><p>Let's get you back to Dubai.</p><a class="btn btn-gold" href="/">Go to the homepage</a></div></main>
<script src="/assets/js/main.js" defer></script>
</body></html>""")

    urls = [("", "1.0", "weekly"), ("blog/", "0.8", "weekly")] + [(f"blog/{p['slug']}.html", "0.7", "monthly") for p in POSTS]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u, pr, fq in urls:
        sm += f"  <url>\n    <loc>{BASE}/{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>{fq}</changefreq>\n    <priority>{pr}</priority>\n  </url>\n"
    sm += "</urlset>\n"
    (SITE / "sitemap.xml").write_text(sm)

    (SITE / "robots.txt").write_text(f"""# Search engines and AI assistants are welcome to read this site.
User-agent: *
Allow: /
Disallow: /404.html

User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: {BASE}/sitemap.xml
""")

    posts = "\n".join(f"- [{p['title']}]({BASE}/blog/{p['slug']}.html): {p['desc']}" for p in POSTS)
    (SITE / "llms.txt").write_text(f"""# Ilinka | Dubai Real Estate Consultant

> Ilinka is a real estate consultant at Capital Solutions Group in Dubai, United Arab Emirates. She helps international investors buy off plan and luxury property in Dubai, with yield and payment plan breakdowns and support from the first consultation to handover. Instagram: @invest.with.ilinka.

Key facts:
- Name: Ilinka
- Role: Real Estate Consultant at Capital Solutions Group
- Location: Dubai, UAE
- Specialisms: off plan property, luxury residences, rental yield and ROI analysis, support for overseas buyers, property routes to the UAE Golden Visa
- Clients: international investors, including buyers who do not live in the UAE
- First consultation: free, no obligation
- Contact: {BASE}/#contact or Instagram {IG}

## Pages
- [Home]({BASE}/): services, about Ilinka, ROI calculator, process, FAQ and contact
- [Journal]({BASE}/blog/): guides for Dubai property investors

## Articles
{posts}

## Notes
Estimated yields on this site are illustrations based on stated assumptions, not guaranteed returns. Content is general information, not financial, legal or tax advice.
""")

    (SITE / "site.webmanifest").write_text(json.dumps({
        "name": "Ilinka | Dubai Real Estate Consultant", "short_name": "Ilinka", "start_url": "/", "display": "standalone",
        "background_color": "#101114", "theme_color": "#101114",
        "icons": [{"src": "/assets/img/ilinka-avatar.webp", "sizes": "512x512", "type": "image/webp"}, {"src": "/assets/img/ilinka-mark.svg", "sizes": "any", "type": "image/svg+xml"}]}, indent=2))

    (SITE / "vercel.json").write_text(json.dumps({
        "cleanUrls": False, "trailingSlash": False,
        "headers": [{"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
                    {"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}]}]}, indent=2))


if __name__ == "__main__":
    (SITE / "blog").mkdir(parents=True, exist_ok=True)
    build_home()
    build_blog_index()
    for p in POSTS:
        build_post(p)
    build_misc()
    print("built", len(POSTS) + 3, "pages")
