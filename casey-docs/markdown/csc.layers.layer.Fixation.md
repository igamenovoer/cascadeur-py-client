[CLEAN]

# csc.layers.layer.Fixation

## Overview
Fixation is an enumeration representing the layer frame fixation state in Cascadeur. Known members are Free (0) and Fulcrum (2). Use this type wherever an API expects or returns a fixation state for animation layers. Specific behavior associated with each state is undocumented in the available source.

## Class Definition
```python
class csc.layers.layer.Fixation
```

## Constructor

### __init__(self, value)
Initializes an enumeration member.

- Parameters:
  - value: undocumented – underlying value for the member.
- Returns: None

## Attributes
- Free: enumeration member with value 0.
- Fulcrum: enumeration member with value 2.
- name: standard Enum attribute; the member name.
- value: standard Enum attribute; the member value.

## Usage Notes
- Refer to members as Fixation.Free or Fixation.Fulcrum when specifying a fixation state.
- Detailed behavior for each state is not documented here.

