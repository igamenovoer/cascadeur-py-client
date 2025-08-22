[CLEAN]
<!-- Cleaned by batch script 2025-08-22 22:45 | Original: aa4fbd6e -->

# csc.update.GroupAttributeId

**Module:** `csc.update.GroupAttributeId`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.update.GroupAttributeId.html)

## Overview

Represents an attribute within a group by combining the group's identifier (GroupId) with the attribute's GUID-based identifier. Group attribute names and indices can change over time, so each attribute is identified by its own GUID.

## Class Definition

```python
class csc.update.GroupAttributeId
```

A value object that implements a GroupAttributeId, defined by a GroupId and a GUID of the attribute.

## Constructor

### `__init__(group_id, attribute_id) -> None`

Create a GroupAttributeId from a group identifier and an attribute GUID.

**Parameters:**
- `group_id` (GroupId): Get GroupId.
- `attribute_id` (csc.Guid): Get csc.Guid — id of the attribute.

**Returns:**
- None

## Methods

This class does not define additional public methods beyond the constructor.

## Usage Example

```python
import csc.update

# Obtain or reference the required identifiers
group_id = ...       # GroupId instance identifying the group
attr_guid = ...      # csc.Guid identifying the attribute

# Create a GroupAttributeId instance
gaid = csc.update.GroupAttributeId(group_id, attr_guid)
```

## Usage Notes

- Attributes:
  - group_id (GroupId): The identifier of the group.
  - attribute_id (csc.Guid): The GUID of the attribute within the group.
- Group attribute names and indices may change; rely on attribute_id (GUID) for stable identification.
- Construct instances only with valid GroupId and csc.Guid values to ensure consistent referencing.

## See Also

- csc.update.GroupId
- csc.Guid