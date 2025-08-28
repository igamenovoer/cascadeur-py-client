# Crawling Cascadeur Python API Documentation

This guide shows you **4 different approaches** to crawl the Cascadeur Python API documentation from https://cascadeur.com/python-api/ into markdown format.

## 🎯 Quick Summary of Methods

| Method | Best For | Setup Required | Output Quality |
|--------|----------|----------------|----------------|
| **MCP Tools** | VS Code/Cursor users | None (already available) | ⭐⭐⭐⭐⭐ |
| **Python SDK** | Python developers | `pip install firecrawl-py` | ⭐⭐⭐⭐⭐ |
| **Direct API** | Custom integrations | `requests` library | ⭐⭐⭐⭐⭐ |
| **Tavily** | Alternative crawler | Built-in MCP | ⭐⭐⭐⭐ |

---

## 🔥 Method 1: Firecrawl MCP Tools (Recommended)

**Best for:** VS Code/Cursor users who want immediate results

### ✅ Advantages:
- No setup required
- Works directly in your editor
- High-quality markdown output
- Built-in content filtering

### 📋 Usage:
The MCP tools are already available in your environment. Just use:

```javascript
// Scrape single page
firecrawl_scrape({
  url: "https://cascadeur.com/python-api/",
  formats: ["markdown"],
  onlyMainContent: true
})

// Crawl entire documentation
firecrawl_crawl({
  url: "https://cascadeur.com/python-api/",
  limit: 10,
  max_depth: 2,
  scrapeOptions: {
    formats: ["markdown"],
    onlyMainContent: true
  }
})
```

---

## 🐍 Method 2: Firecrawl Python SDK

**Best for:** Python developers who want programmatic control

### 🚀 Setup:
```bash
# Install the SDK
python setup_firecrawl.py

# Or manually:
pip install firecrawl-py
```

### 🔑 Get API Key:
1. Visit https://firecrawl.dev/
2. Sign up for an account
3. Get your API key
4. Set environment variable: `FIRECRAWL_API_KEY=your_key_here`

### 📋 Usage:
```bash
python crawl_cascadeur_docs.py
```

### 📁 Output:
- `cascadeur_docs_crawled/crawl_results.json` - Complete JSON results
- `cascadeur_docs_crawled/01_page_name.md` - Individual markdown files

---

## 🌐 Method 3: Direct API Calls

**Best for:** Custom integrations and detailed control

### 🚀 Setup:
```bash
pip install requests
export FIRECRAWL_API_KEY=your_key_here
```

### 📋 Usage:
```bash
python firecrawl_direct_api.py
```

### 🎛️ Options:
1. **Full crawl** - Crawls entire documentation site
2. **Single page** - Just scrapes the main page

### ⚙️ Customization:
Modify the crawl options in `firecrawl_direct_api.py`:
```python
crawl_options = {
    "limit": 15,  # Number of pages
    "scrapeOptions": {
        "formats": ["markdown"],
        "onlyMainContent": True,
        "waitFor": 1000
    },
    "crawlerOptions": {
        "includes": ["**/python-api/**"],  # Only API docs
        "excludes": ["**/search**", "**/genindex**"]  # Skip search pages
    }
}
```

---

## 🔍 Method 4: Tavily Crawler

**Best for:** Alternative approach with different crawling strategy

### 📋 Usage:
Tavily MCP tools are also available:

```javascript
tavily_crawl({
  url: "https://cascadeur.com/python-api/",
  format: "markdown",
  limit: 10,
  max_depth: 2,
  extract_depth: "basic"
})
```

---

## 📊 Comparison of Results

### Firecrawl (Methods 1-3):
- ✅ Excellent markdown formatting
- ✅ Proper content extraction
- ✅ Filters out navigation/ads
- ✅ Preserves code blocks and links
- ✅ Handles complex documentation structure

### Tavily (Method 4):
- ✅ Good general content extraction
- ✅ Fast crawling
- ⚠️ Less specialized for documentation
- ⚠️ May include more non-content elements

---

## 🎯 Recommended Workflow

1. **Start with MCP Tools** (Method 1) for immediate testing
2. **Use Python SDK** (Method 2) for production automation
3. **Use Direct API** (Method 3) for custom integrations
4. **Try Tavily** (Method 4) as backup/alternative

---

## 📁 Output Structure

All methods will create structured output:

```
cascadeur_docs/
├── crawl_results.json          # Complete JSON data
├── 01_main_documentation.md    # Main API overview
├── 02_csc_module.md           # CSC module docs
├── 03_math_functions.md       # Math utilities
├── 04_update_system.md        # Update system
└── 05_tools_module.md         # Tools and utilities
```

---

## 🔧 Troubleshooting

### Common Issues:

1. **Rate Limiting**: Add delays between requests
2. **Large Output**: Reduce `limit` parameter
3. **Missing Content**: Check `includes/excludes` patterns
4. **API Errors**: Verify your API key is correct

### Pro Tips:

- Use `onlyMainContent: true` for cleaner output
- Set appropriate `limit` to avoid overwhelming results  
- Include specific path patterns with `includes` for targeted crawling
- Save both JSON and markdown formats for flexibility

---

## 🎉 Next Steps

After crawling the documentation:

1. **Process the markdown** files for your specific needs
2. **Convert to other formats** (PDF, HTML, etc.)
3. **Index for search** using vector databases
4. **Integrate with your toolchain** for automated documentation updates

Choose the method that best fits your workflow and requirements!
