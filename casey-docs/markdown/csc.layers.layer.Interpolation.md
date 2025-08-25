[CLEAN]

# csc.layers.layer.Interpolation

## Overview
An enumeration of keyframe interpolation modes used in Cascadeur's layer system. These values determine how animation values transition between keyframes (e.g., smooth curves, linear transitions, or stepped changes). Use these constants when setting or reading interpolation for keys on animation layers.

## Class Definition
```python
class csc.layers.layer.Interpolation
```

## Constructor

### `__init__(value)`
Initializes the enumeration member.

- Parameters:
  - value: undocumented – Underlying value used to construct the enum member.
- Returns: None

## Attributes
- BEZIER: int – 0
- LOW_AMPLITUDE_BEZIER: int – 1 (viscous)
- LINEAR: int – 2
- STEP: int – 3
- FIXED: int – 4
- NONE: int – 5
- CLAMPED_BEZIER: int – 6

## Usage Notes
- Choose an Interpolation value to control how a key transitions to the next key on a layer.
- Exact behavior of each mode is defined by Cascadeur; consult the original documentation for detailed semantics.

