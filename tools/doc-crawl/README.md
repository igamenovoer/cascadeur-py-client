# Cascadeur Documentation Crawler

A robust crawler for downloading the Cascadeur Python API documentation from https://cascadeur.com/python-api/

## Features

- **Sphinx-aware crawling**: Uses `objects.inv` to efficiently discover all API symbols
- **Robust retry logic**: Exponential backoff with configurable retries for network failures
- **Resume capability**: Can resume from where it left off if interrupted
- **Progress tracking**: Saves state after each page for recovery
- **Duplicate prevention**: Tracks already crawled pages to avoid redundant downloads
- **Multiple output formats**: JSON and JSONL for different use cases

## Installation

The required dependencies are already installed via pixi:
- `scrapy`
- `beautifulsoup4`
- `sphobjinv`
- `requests`

## Usage

### Run the crawler
```bash
# From project root
pixi run -e dev python tools/doc-crawl/run_crawler.py

# Or directly
pixi run -e dev python tools/doc-crawl/cascadeur_doc_crawler.py
```

### Check crawler status
```bash
pixi run -e dev python tools/doc-crawl/run_crawler.py status
```

### Reset crawler (delete state and optionally output)
```bash
pixi run -e dev python tools/doc-crawl/run_crawler.py reset
```

## Output Structure

Downloaded documentation is saved to `casey-docs/`:
```
casey-docs/
├── objects.inv          # Sphinx inventory file
├── pages/              # Raw HTML pages (hashed filenames)
├── symbols/            # Extracted symbols by page (JSON)
├── cascadeur_api_docs.json   # Consolidated all symbols
└── cascadeur_api_docs.jsonl  # JSONL format for streaming
```

## State Management

Crawler state is saved in `tmp/crawler_state/`:
- `crawler_state.json`: Main state file with progress tracking
- Can resume from interruption by running the crawler again

## Crawling Process

1. **Fetch inventory**: Downloads `objects.inv` and checks if changed
2. **Parse symbols**: Extracts all API symbols and groups by page
3. **Crawl pages**: Downloads each page and extracts symbol documentation
4. **Extract docs**: Parses HTML to find anchors and documentation blocks
5. **Save progress**: Updates state after each page
6. **Retry failures**: Automatically retries failed pages once
7. **Consolidate**: Creates final JSON/JSONL with all symbols

## Error Handling

- Network errors: Exponential backoff retry (up to 5 attempts)
- Missing anchors: Multiple fallback strategies (partial match, text search)
- Interruption: Saves state for resume
- Failed pages: Tracked and retried once at the end

## Logs

Detailed logs are written to:
- Console output
- `tmp/crawler.log` file

## Architecture

The crawler follows the guide in `context/hints/howto-crawl-sphinx-with-scrapy-retries.md` but uses a simpler requests-based approach instead of full Scrapy for easier debugging and control.