# Batch Processing Documentation

## Overview

This directory contains robust batch processing tools for cleaning Cascadeur API documentation using LLM (Large Language Model) services.

## Tools Available

### 1. PowerShell Batch Processor (`batch_process_docs.ps1`)

The most robust option with advanced features:
- **Configurable retry logic** (default: 5 attempts per file)
- **Resume capability** - saves state and can continue from interruptions
- **Real-time progress tracking** with ETA
- **Detailed error reporting**
- **Graceful failure handling** - continues processing even when files fail

### 2. Python Batch Processor (`batch_clean_docs.py`)

Alternative Python-based implementation:
- Async processing with configurable concurrency
- State persistence for resumability
- Validation of cleaned content
- Exponential backoff for transient errors

### 3. Single File Cleaner (`single_file_cleaner.py`)

Used internally by PowerShell script:
- Processes one file at a time
- Clear error messages for debugging
- Standalone usage for testing individual files

## Quick Start

### IMPORTANT: Security Notice
**NEVER hardcode API keys in tracked files!** This repository is public. Use environment variables or untracked config files.

### Step 1: Configure Credentials Securely

```bash
# Option 1: Save API key to gitignored file (RECOMMENDED)
echo "your-api-key-here" > tools\cleanup\.api_key

# Option 2: Run the secure setup script
tools\cleanup\setup_credentials.bat

# Option 3: Set environment variable
$env:CUSTOM_LLM_API_KEY = "your-api-key-here"  # NEVER commit this!
```

### Step 2: Run Batch Processor

```powershell
# Simplest way - will auto-load from .api_key file
powershell -ExecutionPolicy Bypass -File tools\cleanup\batch_process_docs.ps1

# Or use the simple batch file
tools\cleanup\run_batch.bat

# Or with custom parameters
powershell -ExecutionPolicy Bypass -File tools\cleanup\batch_process_docs.ps1 `
    -BaseUrl "https://your-llm-endpoint.com/v1" `
    -Model "gpt-5-2025-08-07" `
    -MaxRetries 5 `
    -ContinueOnError

# Or use the advanced batch file for more control
tools\cleanup\run_ps_batch_advanced.bat 10  # 10 retries
```

### Using Python Batch Processor

```bash
# With command line arguments (use env variable for key)
pixi run -e dev python tools/cleanup/batch_clean_docs.py \
    --api-key "$CUSTOM_LLM_API_KEY" \
    --base-url "https://your-llm-endpoint.com/v1" \
    --model "gpt-5-2025-08-07" \
    --max-concurrency 3
```

## Configuration Parameters

### PowerShell Script Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `-ApiKey` | Required | Your LLM API key |
| `-BaseUrl` | None | LLM endpoint URL (e.g., https://yunwu.ai/v1) |
| `-Model` | gpt-5-2025-08-07 | Model name to use |
| `-MaxRetries` | **5** | Maximum retry attempts per file |
| `-SourceDir` | casey-docs\markdown | Directory containing markdown files |
| `-StateFile` | tmp\cleanup\ps_batch_state.json | State persistence file |
| `-ContinueOnError` | true | Continue processing when files fail |

### Python Script Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--api-key` | Required | Your LLM API key |
| `--base-url` | None | LLM endpoint URL |
| `--model` | gpt-4o | Model name to use |
| `--max-concurrency` | 3 | Concurrent requests limit |
| `--src-dir` | casey-docs/markdown | Source directory |
| `--state-path` | tmp/cleanup/clean_state.json | State file path |

## Retry Logic

The PowerShell batch processor includes intelligent retry logic:

1. **Default: 5 attempts** per file (configurable)
2. **Exponential backoff** between retries
3. **Specific error handling** for:
   - Connection timeouts
   - Rate limiting (with 30-second wait)
   - LLM processing errors
4. **Automatic skip** after max retries exceeded

To adjust retry count:
```powershell
# For 10 retries per file
-MaxRetries 10

# For 2 retries (faster but less reliable)
-MaxRetries 2
```

## State Management and Resume

Both processors save state for resumability:

### PowerShell State File
Location: `tmp\cleanup\ps_batch_state.json`

Contains:
- Processed files with status
- Failed files list
- Cleaned files list
- Timestamps and error details

### Resume After Interruption
Simply run the same command again - it will:
1. Load previous state
2. Skip already processed files
3. Continue from where it left off
4. Retry previously failed files if desired

### Reset Progress
To start fresh:
```powershell
# Delete state file
Remove-Item tmp\cleanup\ps_batch_state.json

# Or move it for backup
Move-Item tmp\cleanup\ps_batch_state.json tmp\cleanup\ps_batch_state.backup.json
```

## Progress Tracking

The PowerShell processor shows real-time progress:
```
[##################-------------------------------] 37.6% (79/210) ETA: 00:06:35 - Processing file.md
```

Components:
- **Progress bar** - Visual representation
- **Percentage** - Overall completion
- **File count** - (processed/total)
- **ETA** - Estimated time remaining
- **Current file** - File being processed

## Error Handling

### Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Processing failed with exit code 1" | LLM processing error | Check API key and endpoint |
| "Connection timeout" | Network or slow LLM | Increase timeout or retry |
| "Rate limit exceeded" | Too many requests | Reduce concurrency or wait |
| "File already clean" | Has [CLEAN] marker | Normal - file skipped |

### Debugging Failed Files

1. Check specific error in state file:
```powershell
$state = Get-Content tmp\cleanup\ps_batch_state.json | ConvertFrom-Json
$state.ProcessedFiles | Where-Object { $_.Status -eq "failed" }
```

2. Test single file manually:
```bash
pixi run -e dev python tools/cleanup/single_file_cleaner.py \
    --file "casey-docs/markdown/problem_file.md" \
    --api-key "$CUSTOM_LLM_API_KEY" \
    --base-url "https://your-endpoint/v1" \
    --model "gpt-5-2025-08-07"
```

## Performance Optimization

### Typical Processing Times
- Small files (<1KB): 5-15 seconds
- Medium files (1-5KB): 15-30 seconds
- Large files (>5KB): 30-90 seconds

### Optimization Tips

1. **Network**: Ensure stable connection to LLM endpoint
2. **Retry Count**: Balance between reliability and speed
   - High (7-10): More reliable but slower
   - Medium (5): Good balance (default)
   - Low (2-3): Faster but may skip difficult files
3. **Concurrency**: For Python script, adjust based on rate limits
4. **State Saves**: Automatic every 5 files to minimize data loss

## Batch File Options

### Basic Launcher
`run_ps_batch.bat` - Simple execution with secure credential loading

### Advanced Launcher
`run_ps_batch_advanced.bat` - Configurable parameters:
```batch
# First configure credentials securely
tools\cleanup\setup_credentials.bat

# Then run with custom retry count
run_ps_batch_advanced.bat 10

# Run with 10 retries and specific model
run_ps_batch_advanced.bat 10 gpt-5-2025-08-07

# API key is loaded from environment or .api_key file
# NEVER pass API keys as command line arguments!
```

## Best Practices

1. **First Run**: Test on a few files first
   ```powershell
   # Process only first 5 files to test
   # Then Ctrl+C to stop
   ```

2. **Monitor Initial Files**: Watch the first few files to ensure:
   - API connection works
   - [CLEAN] markers are added
   - No consistent failures

3. **Regular State Backups**: For large batches
   ```powershell
   Copy-Item tmp\cleanup\ps_batch_state.json "tmp\cleanup\backup_$(Get-Date -Format 'yyyyMMdd_HHmmss').json"
   ```

4. **Handle Failures**: After completion, review failed files:
   - Check if they need manual cleaning
   - Adjust retry count if needed
   - Consider rate limiting issues

5. **Verify Results**: Spot-check cleaned files for quality

## Troubleshooting

### Script Won't Start
- Check PowerShell execution policy
- Verify pixi/Python environment is activated
- Ensure LiteLLM is installed: `pixi add litellm`

### All Files Failing
- Verify API key is correct
- Check endpoint URL is accessible
- Test with single_file_cleaner.py first
- Confirm model name is valid

### Slow Processing
- Check network latency to LLM endpoint
- Consider reducing retry count temporarily
- Monitor for rate limiting messages

### State File Corruption
- Delete corrupted state file
- Script will start fresh
- Previous [CLEAN] markers prevent reprocessing

## Summary Statistics

After completion, you'll see:
```
============================================================
BATCH PROCESSING SUMMARY
============================================================
Total Files:          210
Already Clean:        64
Successfully Cleaned: 140
Failed:              6
Time Elapsed:        02:34:15
Avg Time/File:       31.2 seconds
============================================================
```

Failed files can be retried by running the script again or processing manually.