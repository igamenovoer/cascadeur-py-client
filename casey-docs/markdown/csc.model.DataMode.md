[CLEAN]

# csc.model.DataMode

## Overview
DataMode is an enumeration that distinguishes between static and time-varying data in Cascadeur. Use it to tell APIs whether an operation should act on a single state or over an animation timeline. Choosing the correct mode helps avoid unintended processing across frames or missed time variation.

## Class Definition
```python
class csc.model.DataMode  # enum
    Static
    Animation
```

## Attributes
- Static: enumeration member – Non-animated (time-invariant) data.
- Animation: enumeration member – Animated (time-varying) data.
- name: str – Name of the enum member.
- value: undocumented – Underlying value associated with the enum member.

## Usage Notes
- Use Static for operations on a single pose or snapshot.
- Use Animation when traversing, evaluating, or modifying data across frames.
- Prefer the enum members over raw literals for clarity and safety.

