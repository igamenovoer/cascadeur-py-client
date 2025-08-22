[CLEAN]

# csc.domain.IntervalActionOnChange

**Module:** `csc.domain.IntervalActionOnChange`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.IntervalActionOnChange.html)

## Overview

The `IntervalActionOnChange` enumeration defines different actions that can be taken when interval changes occur in Cascadeur. This enum controls the behavior of animation systems when interval modifications are detected.

## Enumeration Definition

```python
class csc.domain.IntervalActionOnChange(enum.Enum)
```

An enumeration that specifies the action to perform when interval changes are detected during animation operations.

## Enumeration Values

### `Fixing = 0`

Apply fixing behavior to maintain consistency when interval changes are detected.

### `DoNothing = 1`

Perform no special action when interval changes occur.

## Attributes

### `name`

The name of the enumeration member as a string.

### `value`

The numeric value associated with the enumeration member.

## Usage Example

```python
import csc.domain

# Use specific enumeration values
action = csc.domain.IntervalActionOnChange.Fixing
print(f"Action: {action.name}, Value: {action.value}")

# Compare enumeration values
if action == csc.domain.IntervalActionOnChange.Fixing:
    print("Fixing behavior is enabled")

# Set different actions
fixing_action = csc.domain.IntervalActionOnChange.Fixing
do_nothing_action = csc.domain.IntervalActionOnChange.DoNothing

# Use in configuration or function calls
def configure_interval_behavior(action: csc.domain.IntervalActionOnChange):
    if action == csc.domain.IntervalActionOnChange.Fixing:
        print("Configuring interval fixing behavior")
    elif action == csc.domain.IntervalActionOnChange.DoNothing:
        print("Configuring no action on interval changes")

# Apply configuration
configure_interval_behavior(csc.domain.IntervalActionOnChange.Fixing)
```

## Usage Notes

- This enumeration is typically used in animation interval and timeline configurations
- Fixing (0) applies constraints or fixing behavior to maintain animation integrity during interval changes
- DoNothing (1) disables special behavior, allowing manual control over interval modifications
- The enum values are integers that can be compared numerically
- Use the enumeration constants rather than raw integer values for better code clarity
- Related to `FrameActionOnChange` but specifically for interval-based operations

## See Also

- `csc.domain.FrameActionOnChange` - Related enumeration for frame-based actions
- Animation and timeline classes that use interval-based enumerations
- Interval and section manipulation functions