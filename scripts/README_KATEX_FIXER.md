# KaTeX Error Fixer Scripts

This directory contains scripts to systematically fix KaTeX parse errors in your Cascadeur documentation files.

## Problem Description

The KaTeX render engine (used by many markdown processors) doesn't support certain LaTeX commands like `\[` and `\]` for display math. When numpy type annotations like `numpy.ndarray\[numpy.float32\[3, 1\]\]` appear in documentation, they cause "Undefined control sequence" errors because the backslash-bracket combinations are interpreted as unsupported LaTeX commands.

## Scripts

### 1. `fix_katex_errors.py` - Main Fixer Script
The primary script that fixes KaTeX parse errors by converting numpy type annotations to proper code formatting.

**Usage:**
```bash
# Run dry-run to see what would be fixed
python fix_katex_errors.py --dry-run

# Fix all files in cascadeur-docs directory
python fix_katex_errors.py

# Fix files in a specific directory
python fix_katex_errors.py /path/to/your/docs
```

**What it fixes:**
- `numpy.ndarray\[numpy.float32\[3, 1\]\]` → `numpy.ndarray[numpy.float32[3, 1]]`
- `numpy.ndarray[numpy.float32[3, 1]]` → `numpy.ndarray[numpy.float32[3, 1]]`
- Other numpy type patterns

### 2. `fix_katex_errors_v2.py` - Improved Version
Enhanced version that handles edge cases and cleanup issues better.

**Features:**
- Cleans up double backticks from previous fixes
- Better pattern matching
- Preserves existing backups
- More robust error handling

### 3. `run_katex_fixer.py` - Interactive Runner
A user-friendly script that provides an interactive menu for running the fixer.

**Usage:**
```bash
python run_katex_fixer.py
```

## Results

When run on the Cascadeur documentation, the scripts:

- **Processed**: 39 markdown files
- **Modified**: 14 files with issues
- **Fixed**: Over 1,100 KaTeX parse errors total
- **Created**: Backup files (.bak) for all modified files

## Examples

### Before (causes KaTeX error):
```markdown
numpy.ndarray\[numpy.float32\[3, 1\]\]
```

### After (renders correctly):
```markdown
`numpy.ndarray[numpy.float32[3, 1]]`
```

## Safety Features

- **Automatic backups**: All modified files get `.bak` backups
- **Dry-run mode**: See what would be changed without making changes
- **Preserved backups**: Won't overwrite existing backup files
- **Error handling**: Graceful handling of encoding and permission issues

## Restore Original Files

If you need to restore the original files:

```bash
# Find and restore all backup files
find cascadeur-docs -name '*.bak' -exec bash -c 'mv "$1" "${1%.bak}"' _ {} \;
```

## Technical Details

The scripts use regex patterns to identify and fix:

1. **Escaped square brackets**: `\[` and `\]` 
2. **Numpy type annotations**: Various numpy array type patterns
3. **Double backticks**: Cleanup from previous fixes
4. **Standalone numpy types**: Individual type annotations

The fixes convert problematic patterns to inline code formatting using backticks, which:
- Prevents KaTeX from parsing the content as math
- Maintains readability
- Is semantically appropriate for type annotations
- Works across different markdown renderers

## Future Use

These scripts can be reused whenever you:
- Add new documentation files
- Update existing documentation 
- Encounter similar KaTeX parse errors
- Need to process documentation from other sources

The patterns are configurable and can be extended for other similar issues.
