[CLEAN]

# csc.update.InterfaceAttributeSide

## Overview
InterfaceAttributeSide is an enumeration indicating the context of an interface attribute within the Cascadeur update module. It distinguishes attributes that apply to the interface of a group from those that apply to the group node itself. Use this enum where APIs require specifying which side of a group an operation targets.

## Class Definition
```python
class InterfaceAttributeSide
```

## Constructor

### __init__(self, value)
Initialize an enum member with a value (undocumented).

- Parameters:
  - value: undocumented – underlying value for the enum member.
- Returns: InterfaceAttributeSide

## Attributes
- InterfaceSide: inside the group (undocumented).
- GroupSide: when the group is a node (undocumented).
- name: undocumented.
- value: undocumented.

## Usage Notes
- Select InterfaceSide to refer to attributes on the group's interface.
- Select GroupSide to refer to attributes on the group node itself.

