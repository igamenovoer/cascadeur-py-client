# About Crawling / Extracting Sphinx API Documentation (Cascadeur Python API Example)

This hint explains practical, reproducible approaches to obtain structured data (symbols, signatures, descriptions) from a Sphinx‑generated API site like `https://cascadeur.com/python-api/`.

---
## 1. Recognize Sphinx Sites
Typical indicators:
- `objects.inv` file present at site root or under the docs path
- Repeated method/function anchor listings on an index page
- HTML elements like `<dl class="py class">`, `<dt class="sig sig-object">`, or roles rendered as `<span class="pre">`
- Sidebar with search powered by Sphinx (often `_static/` assets)

Why it matters: Sphinx provides a machine-readable inventory (`objects.inv`) mapping fully-qualified names to page + anchor, so you can avoid blind crawling.

---
## 2. Strategy Overview (Choose the Smallest That Works)
| Goal | Recommended Approach |
|------|----------------------|
| Precise symbol coverage | Parse `objects.inv` + fetch each unique page once |
| Whole-site mirror | `wget` / `httrack` (static) |
| Pipeline / scheduling / scaling | Scrapy spider (Python) |
| Dynamic JS (not typical for Sphinx) | Playwright / Splash / Browserless |
| Quick RAG-ready Markdown | Firecrawl (SaaS or self-host), Apify Actor |

---
## 3. Core Sphinx Inventory Method
1. Download `objects.inv`.
2. Parse it (e.g. `sphobjinv`).
3. Group symbols by page to minimize HTTP requests.
4. Fetch each page; parse HTML for definitions & doc blocks.
5. Normalize & deduplicate symbols (some appear multiple times on large index pages).
6. Emit structured JSON (symbol, kind/role, signature, summary, full doc, source URL, anchor, retrieval timestamp, checksum).

### 3.1 Installation
```bash
pip install sphobjinv beautifulsoup4 lxml
```

### 3.2 Minimal Extraction Script
```python
import sphobjinv, requests, bs4, urllib.parse, json, time, hashlib, collections

BASE = "https://cascadeur.com/python-api/"
INV_URL = BASE + "objects.inv"

inv = sphobjinv.Inventory(url=INV_URL)
by_page = collections.defaultdict(list)
for obj in inv.objects:
    # obj.uri like 'module/path.html#symbol'
    page, *anchor = obj.uri.split('#')
    page_url = urllib.parse.urljoin(BASE, page)
    by_page[page_url].append((obj, anchor[0] if anchor else None))

results = []
for page_url, entries in by_page.items():
    html = requests.get(page_url, timeout=30).text
    soup = bs4.BeautifulSoup(html, 'lxml')
    for obj, anchor in entries:
        node = soup.find(id=anchor) if anchor else None
        if not node:
            continue
        # Move up to enclosing signature block if applicable
        sig_container = node
        for _ in range(3):
            if sig_container.name in ('dt','h1','h2','h3'): break
            sig_container = sig_container.parent if sig_container.parent else sig_container
        signature_text = sig_container.get_text(' ', strip=True)
        # Collect following descriptive siblings until next signature/heading
        desc_parts = []
        for sib in sig_container.next_siblings:
            if getattr(sib, 'name', None) in ('dt','h1','h2','h3'): break
            if getattr(sib, 'name', None) in ('dd','p','div'):
                txt = bs4.BeautifulSoup(str(sib), 'lxml').get_text(' ', strip=True)
                if txt: desc_parts.append(txt)
        full_doc = ' '.join(desc_parts)
        raw = signature_text + '\n' + full_doc
        results.append({
            'name': obj.name,
            'role': obj.role,
            'domain': obj.domain,
            'priority': obj.priority,
            'page_url': page_url,
            'anchor': anchor,
            'source_url': page_url + (f"#{anchor}" if anchor else ''),
            'signature': signature_text,
            'doc': full_doc,
            'checksum': hashlib.sha256(raw.encode('utf-8')).hexdigest(),
            'retrieved_at': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        })

# Optional: deduplicate by (name, role, signature)
uniq = {}
for r in results:
    key = (r['name'], r['role'], r['signature'])
    if key not in uniq:
        uniq[key] = r

print(json.dumps(list(uniq.values())[:5], indent=2))  # sample
```

### 3.3 Dedupe / Normalization Notes
- Duplicate anchors can appear where overview pages aggregate multiple symbols.
- Use normalized signature (collapse whitespace) + name + role as identity.
- Keep a checksum to detect doc drift across versions.

---
## 4. Full-Site Static Mirror (Baseline)
```bash
wget -e robots=off -r -np -k -E -p -nH --cut-dirs=1 https://cascadeur.com/python-api/
```
Pros: quick offline copy. Cons: no structured symbol metadata without extra parsing.

---
## 5. Scrapy Spider Skeleton
Use when you need throttling, retry, pipelines:
```python
import scrapy
from sphobjinv import Inventory

class SphinxApiSpider(scrapy.Spider):
    name = 'cascadeur_api'
    start_urls = ['https://cascadeur.com/python-api/objects.inv']

    def parse(self, response):
        inv = Inventory(stream=response.body)
        pages = {}
        for o in inv.objects:
            page = o.uri.split('#')[0]
            pages.setdefault(page, []).append(o)
        for page, objs in pages.items():
            url = response.urljoin(page)
            yield scrapy.Request(url, callback=self.parse_page, meta={'objects': objs})

    def parse_page(self, response):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')
        for o in response.meta['objects']:
            anchor = o.uri.split('#')[1] if '#' in o.uri else None
            node = soup.find(id=anchor) if anchor else None
            if not node:
                continue
            yield {
                'name': o.name,
                'role': o.role,
                'url': response.url + (f"#{anchor}" if anchor else ''),
                # ... extract signature/doc similarly ...
            }
```

---
## 6. Async Lightweight Crawler
```python
import asyncio, aiohttp, sphobjinv, bs4, urllib.parse, collections
BASE = 'https://cascadeur.com/python-api/'
inv = sphobjinv.Inventory(url=BASE + 'objects.inv')
by_page = collections.defaultdict(list)
for o in inv.objects:
    page = o.uri.split('#')[0]
    by_page[urllib.parse.urljoin(BASE, page)].append(o)

async def fetch(session, url):
    async with session.get(url) as r:
        return await r.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = {asyncio.create_task(fetch(session,u)): u for u in by_page}
        for task in asyncio.as_completed(tasks):
            html = await task
            url = tasks[task]
            soup = bs4.BeautifulSoup(html, 'lxml')
            # parse...
asyncio.run(main())
```

Limit concurrency (e.g. a semaphore) to be polite.

---
## 7. Cleaning & Structuring Tips
- Strip navigation/sidebar blocks (`div.sphinxsidebar`, footers).
- Preserve code examples (`pre`, `code`) with separate field.
- Segment long docs into paragraphs for downstream embeddings (token control).
- Store retrieval metadata (timestamp, URL, checksum, version tag).

---
## 8. Version Tracking
Store:
- `objects.inv` hash
- Per-symbol checksum
Re-run extraction only if the inventory hash changes.

---
## 9. SaaS / Hosted Options
| Service | Use Case | Notes |
|---------|----------|-------|
| Firecrawl (API/self-host) | Convert whole site to Markdown/JSON | Quick RAG ingestion |
| Apify | Repeatable scheduled crawls | Build custom Actor around inventory logic |
| Zyte / ScrapingBee | Rendering + proxy | Overkill for static Sphinx |
| Tavily | API-level search & summarization | Complement, not full structured export |

---
## 10. When You Need Headless Browsers
Only if pages rely on client-side rendering (React/Vue). Sphinx classic builds do not; avoid headless overhead.

Playwright example (for dynamic sites):
```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://cascadeur.com/python-api/')
    html = page.content()
    # parse html
```

---
## 11. Legal & Ethical Considerations
- Check `robots.txt` and site Terms of Use.
- Rate-limit (sleep or concurrency cap).
- Provide attribution if redistributing content.

---
## 12. Common Pitfalls
| Pitfall | Mitigation |
|---------|------------|
| Duplicate symbol entries | Hash (name, role, normalized signature) |
| Missing anchors | Fallback: search `id` variations or skip with log |
| Layout/theme changes | Rely on semantic tags (`dl`, `dt`) not brittle CSS paths |
| Large pages causing memory growth | Stream processing / early JSON flush |

---
## 13. Next Steps Integration
After extraction you can:
- Build a local search index (Whoosh, Lunr, Tantivy/PyO3).
- Feed into embeddings (chunk by ~512-1024 tokens). Store vector IDs referencing `source_url#anchor`.
- Auto-generate stubs or type hints if underlying package not installed.

---
## 14. Reference Links
- Sphinx: https://www.sphinx-doc.org/en/master/usage/inventory.html
- sphobjinv: https://sphobjinv.readthedocs.io/
- Scrapy: https://docs.scrapy.org/
- Firecrawl: https://firecrawl.dev/
- Apify: https://apify.com/
- Playwright: https://playwright.dev/python/
- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

---
**Summary:** Prefer the inventory-driven approach for Sphinx sites: fewer requests, complete symbol coverage, and structured output with minimal parsing complexity.
