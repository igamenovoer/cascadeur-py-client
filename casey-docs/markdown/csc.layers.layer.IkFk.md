[CLEAN]

# csc.layers.layer.IkFk

## Overview
IkFk is an enumeration used in Cascadeur layers to denote the kinematic mode of a frame.  
It provides three members: IK, FK, and GR, mapped to 0, 1, and 2 respectively.  
Use this enum to label or check the mode of an animation layer frame; detailed behavior is undocumented.

## Class Definition
```python
class csc.layers.layer.IkFk:
    IK = 0
    FK = 1
    GR = 2
```

## Constructor
### __init__(self, value)
Initializes/represents an enum member by its underlying value; details are undocumented.

- value: undocumented – underlying numeric value for the member

## Attributes
- IK – enum member with value 0
- FK – enum member with value 1
- GR – enum member with value 2
- name – undocumented
- value – undocumented

## Usage Notes
- Values are fixed: IK = 0, FK = 1, GR = 2.
- Intended for selecting or checking the IK/FK/GR mode on layer frames; integration details are undocumented.

```python
from csc.layers.layer import IkFk

mode = IkFk.IK
if mode == IkFk.FK:
    # handle FK-specific logic
    pass

