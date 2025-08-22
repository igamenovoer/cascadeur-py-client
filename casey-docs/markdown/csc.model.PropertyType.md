[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:30 | Original: 4ad50866 -->

# csc.model.PropertyType

**Module:** `csc.model.PropertyType`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.model.PropertyType.html)

## Overview

The `PropertyType` class is an enumerable that defines various types of properties used within the Cascadeur framework. These types categorize properties into different groups such as data, settings, objects, behaviors, and assets, each with their respective range types.

## Class Definition

```python
class csc.model.PropertyType
```

The `PropertyType` class provides a set of predefined property types that can be used to classify and manage different elements within the Cascadeur environment.

## Constructor

### `__init__(value) -> None`

Initializes a new instance of the `PropertyType` class with the specified value.

**Parameters:**
- `value` (type): The initial value for the property type.

**Returns:**
- None

## Methods

No additional methods are explicitly defined in the documentation.

## Usage Example

```python
import csc.model

# Example of using PropertyType
property_type = csc.model.PropertyType(csc.model.PropertyType.DataType)
print(property_type)
```

## Usage Notes

- The `PropertyType` class is used to define and manage different property categories within Cascadeur.
- It is important to select the correct property type for the intended use case to ensure proper functionality.

## See Also

- Related classes and modules within the `csc.model` namespace.