[CLEAN]

# csc.update.InterfaceId

## Overview
Represents an interface identifier within the update system. An InterfaceId is defined by a GroupId and a connection direction (input or output). It is used to uniquely identify a node's interface by combining its group membership with its direction. Further details are undocumented.

## Class Definition
```python
class csc.update.InterfaceId
```

## Constructor

### __init__(group_id, direction)
Create a new InterfaceId from a group identifier and a direction.

**Parameters:**
- group_id: GroupId – Group identifier; exact type details are undocumented.
- direction: csc.Direction – Direction type of the node (input or output).

**Returns:**
- None

## Attributes
- group_id: GroupId – Get GroupId.
- direction: csc.Direction – Get direction type.

## Usage Notes
- The direction corresponds to whether the node represents an input or output connection.
- Additional behavior and constraints are undocumented.

