# HowTo: Crawl a Sphinx API Site with Scrapy Using `objects.inv`, Robust Retries & Resume

This guide shows how to combine Sphinx-specific knowledge (the `objects.inv` inventory) with Scrapy features (retry, backoff, caching, resume) to reliably extract structured API symbol docs even with intermittent network failures.

---
## 1. Why Combine `objects.inv` + Scrapy?
| Challenge | Naïve Crawl | Inventory‑Aware Crawl |
|-----------|-------------|-----------------------|
| Coverage of symbols | Risk of missed anchors | Exact symbol → page+anchor map |
| Duplicate page hits | Many | One per page (group symbols) |
| Retry / resume after crash | Manual scripting | Built-in: `RetryMiddleware`, `JOBDIR` |
| Throughput + politeness | Harder to tune | Scrapy settings (concurrency, delays) |

---
## 2. High-Level Flow
1. Start URL: `objects.inv` only.
2. Parse inventory (via `sphobjinv`) into objects list.
3. Group inventory entries by page (strip `#anchor`).
4. Schedule one Scrapy Request per unique page (metadata carries list of symbols on that page).
5. In `parse_page`, locate each anchor, extract signature + doc block.
6. Yield structured items; pipeline writes JSONL (append-safe, resumable).

---
## 3. Key Resilience Techniques
| Aspect | Technique | Snippet / Setting |
|--------|-----------|-------------------|
| Lost connections / 5xx | `RetryMiddleware` (increase attempts) | `RETRY_TIMES = 5` |
| Exponential backoff | Custom downloader middleware | see §7.2 |
| Graceful restart | Job directory | run: `scrapy crawl cascadeur_api -s JOBDIR=jobdata/cascadeur` |
| Avoid refetch unchanged | HTTPCACHE | `HTTPCACHE_ENABLED = True` |
| Partial output durability | JSON Lines pipeline + flush | custom pipeline |
| Duplicate symbol elimination | In-memory set or pipeline dedupe | (name, role, signature) |
| Anchor not found | Fallback search / log warning | search by partial id prefix |
| Resource throttling | AutoThrottle | `AUTOTHROTTLE_ENABLED = True` |

---
## 4. Project Setup
```bash
pip install scrapy sphobjinv beautifulsoup4 lxml
scrapy startproject sphinx_crawler
cd sphinx_crawler
```

Directory focus (inside `sphinx_crawler/`):
```
spiders/
  cascadeur_api.py
pipelines.py
settings.py
```

---
## 5. Settings (`settings.py`)
Add / modify:
```python
BOT_NAME = "sphinx_crawler"
ROBOTSTXT_OBEY = True  # set False only if permitted explicitly
CONCURRENT_REQUESTS = 8
DOWNLOAD_DELAY = 0.25  # gentle
RETRY_TIMES = 5
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408]
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 0.5
AUTOTHROTTLE_MAX_DELAY = 10
AUTOTHROTTLE_TARGET_CONCURRENCY = 4.0
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 3600
HTTPCACHE_IGNORE_HTTP_CODES = []
FEED_EXPORT_ENCODING = "utf-8"
ITEM_PIPELINES = {"sphinx_crawler.pipelines.SymbolPipeline": 300}
DOWNLOADER_MIDDLEWARES = {
    "sphinx_crawler.middlewares.ExponentialBackoffRetryMiddleware": 543,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": 550,
}
```

---
## 6. Spider (`spiders/cascadeur_api.py`)
```python
import scrapy
import sphobjinv
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import defaultdict

BASE = "https://cascadeur.com/python-api/"
INV  = BASE + "objects.inv"

class CascadeurApiSpider(scrapy.Spider):
    name = "cascadeur_api"
    start_urls = [INV]

    custom_settings = {
        # Optionally override global settings here
    }

    def parse(self, response):
        # Parse inventory from body bytes (sphobjinv can take stream/bytes)
        inv = sphobjinv.Inventory(stream=response.body)
        by_page = defaultdict(list)
        for o in inv.objects:
            page = o.uri.split('#')[0]
            by_page[urljoin(BASE, page)].append(o)
        for page_url, objs in by_page.items():
            yield scrapy.Request(
                page_url,
                callback=self.parse_page,
                meta={"symbols": objs, "retry_anchor_scan": True},
                errback=self.errback_page
            )

    def errback_page(self, failure):
        self.logger.warning(f"Page request failed: {failure.request.url} -> {failure.value}")
        # Scrapy retry will already have acted; you can add custom logging here.

    def parse_page(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        page_url = response.url
        for obj in response.meta["symbols"]:
            anchor = obj.uri.split('#')[1] if '#' in obj.uri else None
            node = soup.find(id=anchor) if anchor else None
            if not node and anchor:
                # Fallback: partial match (first 30 chars) if theme truncated IDs
                node = soup.find(id=lambda i: i and i.startswith(anchor[:30]))
            if not node:
                self.logger.debug(f"Anchor missing {anchor} on {page_url}")
                continue
            sig = self._closest_sig(node)
            signature_text = sig.get_text(' ', strip=True)
            doc_text = self._collect_doc(sig)
            yield {
                "name": obj.name,
                "role": obj.role,
                "domain": obj.domain,
                "priority": obj.priority,
                "page_url": page_url,
                "anchor": anchor,
                "source_url": page_url + (f"#{anchor}" if anchor else ''),
                "signature": signature_text,
                "doc": doc_text,
            }

    def _closest_sig(self, node):
        # Walk up to dt/h1/h2/h3 container; stop early if found
        cur = node
        for _ in range(6):
            if cur.name in ("dt", "h1", "h2", "h3"): return cur
            if cur.parent: cur = cur.parent
        return node

    def _collect_doc(self, sig_node):
        out = []
        for sib in sig_node.next_siblings:
            name = getattr(sib, 'name', None)
            if name in ("dt", "h1", "h2", "h3"): break
            if name in ("dd", "p", "div", "pre"):  # include code/pre blocks
                text = " ".join(sib.get_text('\n', strip=True).split())
                if text: out.append(text)
        return "\n".join(out)
```

---
## 7. Enhanced Reliability Components
### 7.1 Item Pipeline (`pipelines.py`)
```python
import json, hashlib
from pathlib import Path

class SymbolPipeline:
    def open_spider(self, spider):
        self.path = Path("data/symbols.jsonl")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.seen = set()
        if self.path.exists():
            for line in self.path.open('r', encoding='utf-8'):
                try:
                    obj = json.loads(line)
                    key = (obj['name'], obj['role'], obj.get('signature'))
                    self.seen.add(key)
                except Exception:
                    pass
        self.f = self.path.open('a', encoding='utf-8')

    def process_item(self, item, spider):
        key = (item['name'], item['role'], item['signature'])
        if key in self.seen:
            return item
        self.seen.add(key)
        item['checksum'] = hashlib.sha256(
            (item['name'] + item['signature'] + (item.get('doc') or '')).encode('utf-8')
        ).hexdigest()
        self.f.write(json.dumps(item, ensure_ascii=False) + "\n")
        self.f.flush()
        return item

    def close_spider(self, spider):
        self.f.close()
```

### 7.2 Custom Exponential Backoff Middleware (`middlewares.py`)
```python
import math, random, time
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message

class ExponentialBackoffRetryMiddleware(RetryMiddleware):
    def __init__(self, settings):
        super().__init__(settings)
        self.base_delay = settings.getfloat("BACKOFF_BASE", 0.5)
        self.max_delay = settings.getfloat("BACKOFF_MAX", 20.0)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def _retry(self, request, reason, spider):
        retries = request.meta.get('retry_times', 0) + 1
        delay = min(self.max_delay, self.base_delay * (2 ** (retries - 1)))
        # Jitter
        delay = delay * (0.5 + random.random() * 0.5)
        spider.logger.debug(f"Retry {retries} for {request.url}, sleeping {delay:.2f}s: {reason}")
        time.sleep(delay)  # simple blocking; alternatively schedule via reactor callLater
        return super()._retry(request, reason, spider)
```
Add to settings (optional):
```python
BACKOFF_BASE = 0.5
BACKOFF_MAX = 15.0
```

### 7.3 Resume After Crash
Run spider with job directory:
```bash
scrapy crawl cascadeur_api -s JOBDIR=jobdata/cascadeur
```
If the process stops, rerun the same command: pending requests are restored.

---
## 8. Incremental Update Strategy
1. Before crawl: compute hash of existing `objects.inv` (store in `inventory_state.json`).
2. Fetch new `objects.inv`; if hash unchanged, skip crawl.
3. If changed, run spider; pipeline dedup prevents rewriting unchanged symbols.

Snippet to pre-check:
```python
import requests, hashlib, json, pathlib
INV = "https://cascadeur.com/python-api/objects.inv"
state_file = pathlib.Path("data/inventory_state.json")
inv_bytes = requests.get(INV, timeout=30).content
h = hashlib.sha256(inv_bytes).hexdigest()
prev = json.loads(state_file.read_text())['hash'] if state_file.exists() else None
if h == prev:
    print("Inventory unchanged; skip crawl")
else:
    state_file.parent.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps({"hash": h}))
    # invoke scrapy programmatically or shell out
```

---
## 9. Handling Missing Anchors
Reasons anchors fail:
- Theme minifies or transforms IDs.
- Inventory stale vs deployed HTML.
Mitigation:
- Fallback prefix match (already shown).
- If still not found, log & optionally queue a heuristic search (e.g. search by final component of qualified name in text).

---
## 10. Performance Tuning
| Setting | Effect | Suggested Start |
|---------|--------|-----------------|
| `CONCURRENT_REQUESTS` | Parallelism | 8 |
| `DOWNLOAD_DELAY` | Politeness gap | 0.25s |
| `AUTOTHROTTLE_*` | Dynamic tuning | Enabled |
| `RETRY_TIMES` | Resilience | 5 (raise if flaky network) |

Monitor with `scrapy stats collector` (log tail) for:
- `downloader/exception_type_count/*`
- `retry/count`
- `httpcache/hit` ratio

---
## 11. Export Formats
Quick alternative to custom pipeline—use feed export:
```bash
scrapy crawl cascadeur_api -o symbols.jsonl -s FEED_EXPORT_ENCODING=utf-8 -s FEED_FORMAT=jsonlines
```
But custom pipeline gives incremental dedupe & checksums.

---
## 12. Integrating Into Larger Pipeline
After crawl:
- Validate schema (e.g. Pydantic model) before downstream ingestion.
- Chunk docs for embeddings (split on double newline / 800 tokens).
- Store `(source_url, anchor)` as provenance in vector store.

---
## 13. Source References
- Sphinx Objects Inventory: https://www.sphinx-doc.org/en/master/usage/inventory.html
- sphobjinv Docs: https://sphobjinv.readthedocs.io/
- Scrapy Retry Middleware: https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#retrymiddleware
- AutoThrottle: https://docs.scrapy.org/en/latest/topics/autothrottle.html
- Jobdir (persistent crawl state): https://docs.scrapy.org/en/latest/topics/jobs.html
- HTTP Cache: https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware

---
## 14. Summary
Leverage `objects.inv` to *plan* the crawl (deterministic, minimal requests), then let Scrapy provide robust networking (retry, backoff, caching, resume). This hybrid approach reduces failure points and ensures complete, deduplicated symbol coverage with efficient network usage.
