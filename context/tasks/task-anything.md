# General Tasks Description

## Task 1: Crawl the cascadeur API documentation

we want to crawl the cascadeur API documentation, which is hosted at https://cascadeur.com/python-api/, download the docs as html into `<workspace>/casey-docs/`, crawling code should be put in `tools/doc-crawl/`.

you may encounter lost connections during the crawl, so you should implement retries and handle errors, make your implementation robust, and make it recoverable from where it left off (keep index of what to be crawled and what has been crawled)

- guide: `context\hints\howto-crawl-sphinx-with-scrapy-retries.md`
- scraping tools (already installed):
  - `scrapy`
  - `beautifulsoup4`
  - `sphobjinv`
  - `playwright`
- temp dir for anything: `<workspace>/tmp`
- more tools you can use:
```powershell
PS D:\code\cascadeur-py-client> uv tool list
aider-chat v0.85.2
- aider.exe
blender-remote v1.2.5
- blender-remote-cli.exe
- blender-remote.exe
claude-monitor v3.1.0
- ccm.exe
- ccmonitor.exe
- claude-code-monitor.exe
- claude-monitor.exe
- cmonitor.exe
httpie v3.2.4
- http.exe
- httpie.exe
- https.exe
mitmproxy v12.1.1
- mitmdump.exe
- mitmproxy.exe
- mitmweb.exe
shot-scraper v1.8
- shot-scraper.exe
```