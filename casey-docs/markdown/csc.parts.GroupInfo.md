[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:36 | Original: fa130b54 -->

# csc.parts.GroupInfo

**Module:** `csc.parts.GroupInfo`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.parts.GroupInfo.html)

## Overview

GroupInfo class. Provides access to group-related identifiers and settings.

## Class Definition

```python
class csc.parts.GroupInfo
```

Represents information about a group, including type, name, path, and associated object identifiers.

## Constructor

### `__init__(self) -> None`

Initialize a GroupInfo instance.

**Parameters:**
- None

**Returns:**
- None

## Methods

(No additional methods documented.)

## Attributes

- `type` (Data::Id{}): Get set Data::Id{}
- `name` (Setting::Id{}): Get set Setting::Id{}
- `path` (HyperedgeId{}): Get set HyperedgeId{}
- `object_id` (SettingFunctionId{}): Get set SettingFunctionId{}
- `datas`: Attribute
- `regular_funcs`: Attribute
- `settings`: Attribute
- `settings_funcs`: Attribute

## Usage Example

```python
import csc.parts

# Practical usage example
info = csc.parts.GroupInfo()
# Access attributes (get/set patterns depend on API property implementation)
# info.type, info.name, info.path, info.object_id
```

## Usage Notes

- The attributes type, name, path, and object_id are described as get/set properties; actual access patterns may depend on the API bindings.
- Additional attributes (datas, regular_funcs, settings, settings_funcs) are available but not further described in the source snippet.

## See Also

- Related classes and modules in csc.parts