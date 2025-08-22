[CLEAN]
<!-- Cleaned by batch script 2025-08-22 23:41 | Original: 54f178bc -->

# csc.tools.attractor.attract

**Module:** `csc.tools.attractor.attract`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.tools.attractor.attract.html)

## Overview

Provides the attract function for the Attractor tool. It applies attraction behavior based on the provided arguments.

## Class Definition

```python
# This module exposes a function, not a class.
```

This module contains a single callable function: attract.

## Constructor

### `__init__(params) -> None`

Not applicable. This is a function-only module and does not define a class constructor.

**Parameters:**
- None

**Returns:**
- None

## Methods

### `attract(args: csc.tools.attractor.Args) -> None`

Executes the attraction operation using the specified arguments.

**Parameters:**
- `args` (csc.tools.attractor.Args): Configuration and parameters for the attraction operation.

**Returns:**
- None: This function does not return a value.

## Usage Example

```python
from csc.tools.attractor import attract, Args

# Configure attraction arguments
a = Args()
# set up fields on a as required...

# Run the attract operation
attract(a)
```

## Usage Notes

- Prepare an instance of csc.tools.attractor.Args with all required fields before calling attract.
- The function performs its operation procedurally and does not return a result; inspect the scene or tool state for outcomes.
- Ensure the Attractor tool context and scene objects are properly set up as expected by the provided Args.

## See Also

- csc.tools.attractor.Args
- csc.tools.AttractorTool
- csc.tools.attractor.AttractorGeneralSettings