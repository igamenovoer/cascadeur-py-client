[CLEAN]

# csc.domain.FrameActionOnChange

**Module:** `csc.domain.FrameActionOnChange`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.FrameActionOnChange.html)

## Overview

The `FrameActionOnChange` enumeration defines different actions that can be taken when frame changes occur in Cascadeur. This enum controls the behavior of animation systems when frame modifications are detected.

## Enumeration Definition

```python
class csc.domain.FrameActionOnChange(enum.Enum)
```

An enumeration that specifies the action to perform when frame changes are detected during animation operations.

## Enumeration Values

### `AutoKey = 0`

Automatically create keyframes when frame changes are detected.

### `Fixing = 1` 

Apply fixing behavior to maintain consistency during frame changes.

### `DoNothing = 2`

Perform no special action when frame changes occur.

## Attributes

### `name`

The name of the enumeration member as a string.

### `value`

The numeric value associated with the enumeration member.

## Usage Example

```python
import csc.domain

# Use specific enumeration values
action = csc.domain.FrameActionOnChange.AutoKey
print(f"Action: {action.name}, Value: {action.value}")

# Compare enumeration values
if action == csc.domain.FrameActionOnChange.AutoKey:
    print("Auto-keying is enabled")

# Set different actions
fixing_action = csc.domain.FrameActionOnChange.Fixing
do_nothing_action = csc.domain.FrameActionOnChange.DoNothing

# Use in configuration or function calls
def configure_frame_behavior(action: csc.domain.FrameActionOnChange):
    if action == csc.domain.FrameActionOnChange.AutoKey:
        print("Configuring automatic keyframe creation")
    elif action == csc.domain.FrameActionOnChange.Fixing:
        print("Configuring frame fixing behavior")
    elif action == csc.domain.FrameActionOnChange.DoNothing:
        print("Configuring no action on frame changes")

# Apply configuration
configure_frame_behavior(csc.domain.FrameActionOnChange.AutoKey)
```

## Usage Notes

- This enumeration is typically used in animation and timeline configurations
- AutoKey (0) enables automatic keyframe generation when properties change
- Fixing (1) applies constraints or fixing behavior to maintain animation integrity  
- DoNothing (2) disables special behavior, allowing manual control
- The enum values are integers that can be compared numerically
- Use the enumeration constants rather than raw integer values for better code clarity

## See Also

- `csc.domain.IntervalActionOnChange` - Related enumeration for interval-based actions
- Animation and timeline classes that use this enumeration
- Frame and keyframe manipulation functions