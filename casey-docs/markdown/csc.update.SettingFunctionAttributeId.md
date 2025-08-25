[CLEAN]

# csc.update.SettingFunctionAttributeId

## Overview
Represents an identifier for a specific attribute of a setting function. It is defined by a SettingFunctionId and an attribute index. For attributes that are arrays, an optional attribute_sub_index may refer to an element within the array. This class implements the SettingFunctionAttributeId concept used by the API.

## Class Definition
```python
class csc.update.SettingFunctionAttributeId
```

## Constructor

### `__init__(self, function_id, attribute_index)`
Create a new attribute identifier for a given setting function.

**Parameters:**
- function_id: undocumented – Identifier of the setting function.
- attribute_index: undocumented – Index of the attribute.

**Returns:**
- None

## Attributes
- function_id: undocumented – Get SettingFunctionId.
- attribute_index: undocumented – Get index of the attribute.
- attribute_sub_index: undocumented – Get index of the attribute in array.

## Usage Notes
- Parameter and attribute types are undocumented in the source; consult the original documentation if available.
- attribute_sub_index applies when the target attribute is an array; details are undocumented.

