[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:35 | Original: ad0aa005 -->

# csc.model.SettingMode

**Module:** `csc.model.SettingMode`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.model.SettingMode.html)

## Overview

Setting::Mode enum. This enumerates the basic types of data: Static, Animation.

## Class Definition

```python
class csc.model.SettingMode
```

Enumeration representing basic data types.

## Constructor

### `__init__(self, value) -> None`

Initializes the enum with a given value.

**Parameters:**
- `value` (unknown): Enum value to initialize with.

**Returns:**
- None

## Methods

No additional methods documented.

## Attributes

- `Animation`: Enum member.
- `Static`: Enum member.
- `name`: Enum member name.
- `value`: Enum member value.

## Usage Example

```python
import csc.model as model

# Practical usage example
mode = model.SettingMode('Static')
current_name = mode.name
current_value = mode.value
```

## Usage Notes

- Use `Static` for non-animated data.
- Use `Animation` for animated data.
- Access `name` and `value` for enum metadata.

## See Also

- Other enums and settings within `csc.model`