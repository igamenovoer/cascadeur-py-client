# Documentation Batch Cleanup Tools

This directory contains tools for batch cleaning API documentation using LiteLLM with OpenAI-compatible LLM endpoints.

## Overview

The batch cleanup system processes markdown documentation files in `casey-docs/markdown/` and transforms them into a standardized, professional format. Files that have already been cleaned are marked with `[CLEAN]` and skipped in subsequent runs.

## Setup

### 1. Install Dependencies

```bash
pixi add litellm
```

Or using pip:

```bash
pip install litellm
```

### 2. Configure Credentials Securely

**IMPORTANT: Never hardcode API keys in tracked files!**

Run the setup script to configure your credentials:

```bash
tools\cleanup\setup_credentials.bat
```

Or manually set environment variables:

```powershell
# Required: Your API key (NEVER commit this!)
$env:CUSTOM_LLM_API_KEY = "your-api-key-here"

# Optional: Custom OpenAI-compatible endpoint
$env:CUSTOM_LLM_BASE_URL = "https://your-llm-endpoint.com/v1"

# Optional: Model name (default: gpt-4o)
$env:CUSTOM_LLM_MODEL = "gpt-4o"
```

Alternative: Create an untracked config file:
```powershell
# This file is gitignored
echo "your-api-key-here" > tools\cleanup\.api_key
```

## Usage

### Test Connection First

Always test your configuration before running the full batch:

```bash
pixi run -e dev python tools/cleanup/test_llm_connection.py
```

This will:
1. Verify LiteLLM is installed
2. Test the connection to your LLM endpoint
3. Try cleaning a sample document
4. Report if everything is working

### Run Batch Cleanup

Once the test passes, run the main cleanup:

```bash
pixi run -e dev python tools/cleanup/batch_clean_docs.py
```

Or use the convenience batch file:

```bash
tools\cleanup\run_cleanup.bat
```

## Files

- **`batch_clean_docs.py`** - Main cleaning script with async processing
- **`test_llm_connection.py`** - Test script to verify setup
- **`run_cleanup.bat`** - Windows batch file for easy execution
- **`README.md`** - This documentation

## How It Works

1. **Discovery**: Scans `casey-docs/markdown/` for `.md` files
2. **Filtering**: Skips files containing `[CLEAN]` marker
3. **Processing**: Sends each file to LLM for cleaning with rate limiting
4. **Validation**: Checks cleaned output for:
   - Presence of `[CLEAN]` marker
   - Preservation of API methods
   - No hallucinated content
5. **Persistence**: Saves state to `tmp/cleanup/clean_state.json` for resumability
6. **Output**: Overwrites original files with cleaned versions

## Features

- **Idempotent**: Files with `[CLEAN]` marker are skipped
- **Resumable**: State saved to disk, can continue after interruption
- **Concurrent**: Processes multiple files in parallel (configurable)
- **Validated**: Checks that API information is preserved
- **Rate Limited**: Exponential backoff for transient errors
- **Traceable**: Adds provenance comments with timestamps and checksums

## Output Format

Cleaned files follow this structure:

```markdown
[CLEAN]
<!-- Cleaned by batch script YYYY-MM-DD HH:MM | Original: hash -->

# module.name.ClassName

**Module:** `module.name.ClassName`  
**Source:** [Cascadeur Python API Documentation](url)

## Overview
Brief description...

## Class Definition
```python
class module.name.ClassName
```

## Constructor
### `__init__(params)`
...

## Methods
### `method_name(params) -> return_type`
...

## Usage Example
```python
# Example code
```

## Usage Notes
- Important points...

## See Also
- Related classes...
```

## Monitoring Progress

The script provides real-time feedback:
- `[OK] Cleaned: filename.md` - Successfully processed
- `[FAIL] Failed: filename.md` - Processing failed
- Progress updates every 10 files
- Final summary with statistics

## Troubleshooting

### LiteLLM not installed
```
Error: LiteLLM not installed
Solution: Run `pixi add litellm`
```

### API key not set
```
Error: CUSTOM_LLM_API_KEY not set
Solution: Set the environment variable with your API key
```

### Connection timeout
```
Error: Connection timeout
Solution: Check your CUSTOM_LLM_BASE_URL and network connection
```

### Rate limiting
```
Error: 429 Too Many Requests
Solution: Reduce CLEANER_MAX_CONCURRENCY (e.g., set to 1 or 2)
```

### Validation failures
```
Warning: Validation failed - missing methods
Action: Script will retry with additional guidance
```

## State Management

Progress is saved to `tmp/cleanup/clean_state.json`:

```json
{
  "processed": {
    "path/to/file.md": {
      "status": "cleaned",
      "timestamp": "2024-01-01T12:00:00",
      "original_hash": "abc123"
    }
  },
  "cleaned": ["file1.md", "file2.md"],
  "failed": ["file3.md"],
  "skipped": ["file4.md"]
}
```

To reset and start fresh:
```bash
rm tmp/cleanup/clean_state.json
```

## Performance

Typical processing times:
- Small file (<1KB): 2-5 seconds
- Medium file (1-5KB): 3-8 seconds  
- Large file (>5KB): 5-15 seconds

With 3 concurrent requests, expect ~20-40 files per minute depending on size and LLM response time.

## Cost Estimation

Rough token usage per file:
- Input: ~(file_chars / 4) tokens
- Output: ~(file_chars / 4) tokens
- Total: ~(file_chars / 2) tokens

For 150 files averaging 3KB each:
- Total characters: 450,000
- Estimated tokens: 225,000
- Cost varies by provider (check your LLM pricing)

## Next Steps

After cleaning:
1. Review a sample of cleaned files for quality
2. Commit changes to version control
3. Consider running type checking: `pixi run -e dev mypy tools/cleanup/`
4. Update any dependent documentation or build processes