# Cascadeur Documentation Scripts

This directory contains scripts for scraping and processing Cascadeur documentation.

## Scripts

### `scrape_api_docs.py`

Main scraping script for the Cascadeur Python API documentation.

**Prerequisites:**
```bash
pip install -r requirements.txt
export FIRECRAWL_API_KEY="fc-YOUR-API-KEY"
```

**Usage:**
```bash
# Basic usage - scrapes to ../python
python scrape_api_docs.py

# Custom output directory
python scrape_api_docs.py -o custom-output-dir

# Adjust batch size for rate limiting
python scrape_api_docs.py -b 10

# Help
python scrape_api_docs.py --help
```

**Output:**
- Creates structured markdown files in `../python/` directory
- Follows original website structure: `module/ClassName.md`
- Includes metadata and source attribution
- Generates comprehensive README.md and JSON reference

### `requirements.txt`

Python dependencies for the scraping scripts.

## API Key Setup

1. Sign up at [firecrawl.dev](https://firecrawl.dev)
2. Get your API key from the dashboard  
3. Set environment variable:
   ```bash
   export FIRECRAWL_API_KEY="fc-YOUR-API-KEY"
   ```

## Expected Output Structure

```
cascadeur-docs/python/
├── README.md              # Main documentation index
├── api_reference.json     # Structured API reference
├── model/                 # csc.model module
│   ├── BehaviourViewer.md
│   ├── DataEditor.md
│   └── ...
├── layers/                # csc.layers module  
│   ├── CyclesViewer.md
│   └── ...
└── [other modules]/
```

## Performance Tips

- **Batch Size**: Start with 25, reduce to 10-15 if rate limited
- **Caching**: The scraper uses 1-hour caching for better performance
- **Retries**: Automatic fallback to individual scraping on batch failures
- **Rate Limiting**: Built-in delays between requests to respect server resources