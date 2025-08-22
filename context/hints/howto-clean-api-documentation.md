# How to Clean and Standardize API Documentation

This guide provides a step-by-step approach to cleaning cluttered API documentation files and standardizing them into a consistent, readable format.

## Problem Overview

Original API documentation files often contain:
- Extensive navigation menus and breadcrumbs
- Social media links and footer content
- Duplicated HTML artifacts
- Poor formatting and structure
- Mixed content that obscures the actual API information

## Solution: Standardized Documentation Format

### 1. Document Structure Template

Every cleaned documentation file should follow this structure:

```markdown
# module.name.ClassName

**Module:** `module.name.ClassName`  
**Source:** [Original Documentation Link](https://example.com/docs)

## Overview

Brief description of the class/module purpose and functionality.

## Class Definition

```python
class module.name.ClassName
```

Additional context about the class.

## Constructor

### `__init__(*args, **kwargs)`

Description of the constructor.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `method_name(param1: type, param2: type = default) -> return_type`

Method description.

**Parameters:**
- `param1` (type): Description of parameter
- `param2` (type, optional): Description with default value

**Returns:**
- return_type: Description of return value

**Example:**
```python
import module.name

# Usage example
instance = module.name.ClassName()
result = instance.method_name("value")
```

## Usage Notes

- Key points about usage
- Important considerations
- Best practices
```

### 2. Header Format Standards

**Before (cluttered):**
```markdown
---
source_url: https://example.com/api/module.html
html_file: abc123.html
module: module.name
---
```

**After (clean):**
```markdown
# module.name.ClassName

**Module:** `module.name.ClassName`  
**Source:** [Original Documentation Link](https://example.com/api/module.html)
```

### 3. Method Documentation Standards

**Format each method consistently:**

```markdown
### `method_name(param: type, optional_param: type = default) -> return_type`

Brief description of what the method does.

**Parameters:**
- `param` (type): Description of the parameter
- `optional_param` (type, optional): Description with default value

**Returns:**
- return_type: Description of what is returned

**Example:**
```python
# Practical usage example
result = instance.method_name("example_value")
```
```

## Step-by-Step Cleaning Process

### Step 1: Remove Navigation Clutter

Delete everything that's not API documentation:
- Main navigation menus
- Social media links (Discord, Twitter, Facebook, etc.)
- Footer content (copyright, privacy policy, etc.)
- Language switchers
- "Previous/Next" navigation
- Breadcrumb trails

### Step 2: Extract Core API Information

Identify and preserve only:
- Class name and module path
- Method signatures with parameters and return types
- Brief descriptions of functionality
- Source URL for reference

### Step 3: Apply Standard Structure

Transform the extracted information into the standard template:

```markdown
# Class/Module Name
**Module:** `full.module.path`
**Source:** [Link to original]

## Overview
## Class Definition  
## Constructor
## Methods
## Usage Notes
```

### Step 4: Enhance with Examples

Add practical code examples showing:
- How to import the module
- How to instantiate classes
- How to call methods with realistic parameters

## Automated Cleaning Approach

For files with extensive clutter, use this systematic approach:

### Method 1: Complete Replacement

```bash
# Delete the original file
Remove-Item "path/to/cluttered-file.md"

# Create clean version with new content
# Use create_file tool with standardized content
```

### Method 2: Targeted Replacement

```markdown
# Use replace_string_in_file for specific sections
# Replace header section
# Replace method documentation sections
# Remove footer sections
```

## Quality Standards

### Content Requirements

- **Accuracy**: All parameter types and return types must be correct
- **Completeness**: Include all public methods and properties
- **Clarity**: Use clear, concise descriptions
- **Examples**: Provide practical usage examples

### Formatting Requirements

- **Consistent headers**: Use ## for major sections, ### for methods
- **Code blocks**: Use ```python for code examples
- **Parameter lists**: Use bullet points with (type) annotations
- **Links**: Only include essential reference links

### File Organization

- **Naming**: Keep original filenames for consistency
- **Location**: Maintain directory structure
- **Dependencies**: Update cross-references between files

## Example Transformation

### Before (cluttered):
```markdown
---
source_url: https://example.com/api
---

* [ABOUT](/about)
* Learn
  [Tutorials](/learn)
* Community
  [Forum](http://forum.example.com/)
  [Discord](https://discord.example.com/)

# module.Class

*class* module.Class
:   Class description
    __init__(*args, **kwargs)
    Methods
    | method1 | description |
    | method2 | description |

* [Previous](other.html)
* [Next](another.html)

Social
Learn
[Privacy policy](https://example.com/privacy)
© 2024 Company
```

### After (clean):
```markdown
# module.Class

**Module:** `module.Class`  
**Source:** [Example API Documentation](https://example.com/api)

## Overview

Brief description of the class purpose and functionality.

## Class Definition

```python
class module.Class
```

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `method1(self) -> str`

Description of method1.

**Returns:**
- str: Return value description

## Usage Notes

- Key usage information
- Important considerations
```

## Tools and Techniques

### VS Code Tools Used

- `replace_string_in_file`: For targeted content replacement
- `create_file`: For complete file recreation
- `run_in_terminal`: For file deletion when needed
- `read_file`: For content analysis

### Quality Checks

1. **Verify all methods documented**: Ensure no API methods are missed
2. **Check parameter types**: Validate type annotations are correct
3. **Test examples**: Ensure code examples are syntactically correct
4. **Cross-reference links**: Update internal documentation links

## Best Practices

1. **Preserve essential information**: Never lose actual API details
2. **Maintain consistency**: Use the same format across all files
3. **Focus on developers**: Optimize for practical usage
4. **Include examples**: Always provide working code snippets
5. **Regular updates**: Keep documentation synchronized with API changes

## Source References

- [Python Documentation Style Guide](https://devguide.python.org/documenting/)
- [Sphinx Documentation](https://www.sphinx-doc.org/en/master/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
