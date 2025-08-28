# CSC Module Documentation Extraction Guide

This guide explains how to extract documentation from Cascadeur's `csc` module, which only exists within Cascadeur's Python runtime environment.

## The Problem

The `csc` module is only available when running Python inside Cascadeur. You cannot import it from external Python scripts, which means standard documentation tools like `pdoc` or `sphinx` cannot be used directly.

## Solution: In-Runtime Documentation Extraction

We've created scripts that run **inside** Cascadeur's Python console to extract all docstrings and module information.

## Available Scripts

### 1. `extract_csc_simple.py` (Recommended for quick extraction)

A lightweight script that quickly extracts basic documentation.

**Features:**
- Simple and fast
- Creates both JSON and human-readable text files
- Handles errors gracefully
- Limited depth to avoid infinite recursion

### 2. `extract_csc_docs.py` (Comprehensive extraction)

A more comprehensive script that creates detailed markdown documentation.

**Features:**
- Creates markdown files with proper formatting
- Follows module hierarchy in file structure
- Extracts detailed information about classes, methods, properties
- More robust error handling
- Generates cross-linked documentation

## How to Use

### Step 1: Choose Your Script

- For quick overview: Use `extract_csc_simple.py`
- For detailed docs: Use `extract_csc_docs.py`

### Step 2: Run Inside Cascadeur

1. **Open Cascadeur**
2. **Open the Python Console** (usually found in the Windows menu)
3. **Navigate to the script location** (optional, or use full path)
4. **Execute the script:**

```python
# Method 1: Using exec with file path
exec(open(r'path\\to\\extract_csc_simple.py').read())

# Method 2: If you're in the same directory
exec(open('extract_csc_simple.py').read())

# Method 3: Copy-paste the script content directly into the console
```

### Step 3: Check Output Files

The scripts will create files in the current working directory:

**For `extract_csc_simple.py`:**
- `csc_docs_YYYYMMDD_HHMMSS.json` - Machine-readable data
- `csc_docs_YYYYMMDD_HHMMSS.txt` - Human-readable documentation

**For `extract_csc_docs.py`:**
- `csc_documentation/` directory containing:
  - `index.md` - Main module documentation
  - `submodule_name.md` - Individual submodule docs
  - `csc_raw_data.json` - Raw extracted data

## Example Output Structure

```
csc_documentation/
├── index.md                 # Main csc module
├── animation.md             # csc.animation submodule
├── scene.md                 # csc.scene submodule
├── physics.md               # csc.physics submodule
├── ui.md                    # csc.ui submodule
└── csc_raw_data.json       # Raw data for debugging
```

## Converting to Other Formats

Once you have the markdown files, you can convert them to other formats:

### HTML Documentation Site
```bash
# Using mkdocs
pip install mkdocs
mkdocs new csc-docs
# Copy markdown files to docs/
mkdocs serve

# Using pandoc
pandoc -f markdown -t html index.md -o index.html
```

### PDF Documentation
```bash
# Using pandoc
pandoc -f markdown -t pdf index.md -o csc_documentation.pdf
```

### Static Site with pdoc-style
```bash
# Use the extracted JSON data with a custom generator
python generate_static_site.py csc_raw_data.json
```

## Troubleshooting

### Common Issues:

1. **"Cannot import csc module"**
   - Solution: Make sure you're running the script inside Cascadeur's Python console

2. **"File not found"**
   - Solution: Use the full path to the script file or navigate to the correct directory first

3. **Script hangs or takes too long**
   - Solution: Use the simple extractor first, or reduce max_depth in the comprehensive script

4. **Permission errors when saving files**
   - Solution: Make sure Cascadeur has write permissions to the current directory

### Getting the Current Directory:
```python
import os
print("Current directory:", os.getcwd())
```

### Changing Directory (if needed):
```python
import os
os.chdir(r'C:\\path\\to\\desired\\directory')
```

## Advanced Usage

### Customizing Extraction Depth
Edit the script and modify the `max_depth` parameter:

```python
# In extract_csc_simple.py
csc_info = extract_basic_info(csc, "csc", max_depth=2)  # Reduce for faster extraction

# In extract_csc_docs.py
# Look for depth-related parameters in the functions
```

### Filtering Specific Modules
Modify the scripts to only extract specific submodules:

```python
# Only extract specific submodules
submodules_to_extract = ['animation', 'scene', 'ui']
# Add filtering logic in the extraction functions
```

## Creating a Complete Documentation Site

After extraction, you can create a professional documentation site:

1. **Extract using the comprehensive script**
2. **Set up MkDocs:**
   ```bash
   pip install mkdocs mkdocs-material
   mkdocs new cascadeur-csc-docs
   ```
3. **Copy generated markdown files to `docs/` folder**
4. **Configure `mkdocs.yml`:**
   ```yaml
   site_name: Cascadeur CSC Module Documentation
   theme:
     name: material
   nav:
     - Home: index.md
     - Animation: animation.md
     - Scene: scene.md
     # Add other modules
   ```
5. **Build and serve:**
   ```bash
   mkdocs serve  # For development
   mkdocs build  # For production
   ```

## Alternative: Manual Documentation

If the scripts don't work for your specific case, you can also manually extract documentation:

```python
# Run this in Cascadeur's Python console
import csc
import inspect

# Get basic info
print("CSC Module:", csc.__doc__)
print("Members:", dir(csc))

# Get detailed info for specific items
for name in dir(csc):
    if not name.startswith('_'):
        obj = getattr(csc, name)
        print(f"\n{name}: {type(obj)}")
        if hasattr(obj, '__doc__') and obj.__doc__:
            print(f"  Doc: {obj.__doc__}")
```

This approach gives you full control over what gets extracted and how it's formatted.
