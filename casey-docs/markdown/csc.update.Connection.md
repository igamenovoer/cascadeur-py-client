[CLEAN]

# csc.update.Connection

## Overview
Connection represents a link between two attributes in the Cascadeur update system, defining data flow from a source to a destination. It exposes the identifiers of the output attribute (source) and the input attribute (destination). Detailed parameter types and behaviors are undocumented in the provided source.

## Class Definition
```python
class Connection:
    ...
```

## Constructor

### `__init__(self, source, destination)`
Initializes a connection between a source attribute and a destination attribute.

**Parameters:**
- `source`: undocumented – output AttributeId of the source.
- `destination`: undocumented – input AttributeId of the destination.

**Returns:**
- None

## Attributes
- `source`: undocumented – output AttributeId of the source.
- `destination`: undocumented – input AttributeId of the destination.

## Usage Notes
- Attribute IDs may include types such as RegularDataAttributeId, ActualityAttributeId, SettingFunctionAttributeId, SettingDataAttributeId, GroupAttributeId, ExternalPropertyAttributeId, ConstantDataAttributeId, or ConstantSettingAttributeId. Specific type details are not documented here.

