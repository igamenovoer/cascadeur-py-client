[CLEAN]

# csc.domain.assets.MeshDependency

## Overview
MeshDependency represents mesh skinning dependency data, exposing inverse bind matrices for joints and per-vertex weight information used in deformation/skinning. It provides read-only access to the core data needed to understand how a mesh is influenced by a rig. This is useful for inspection, validation, and export workflows within the Cascadeur environment.

## Class Definition
```python
class MeshDependency:
    ...
```

## Constructor

### `__init__(arg0)`
Initializes a MeshDependency instance.

Parameters:
- arg0: undocumented – Input as documented is unspecified.

## Methods

### `joints_inverse_bind_matrices() -> Matrix4f[]`
Returns the inverse bind matrices associated with joints.

Parameters:
- none

Returns:
- Matrix4f[] – Collection of 4x4 inverse bind matrices.

Notes:
- Matrix4f is defined by the Cascadeur API.

### `vertices_weights() -> List[List[VertexWeight]]`
Returns per-vertex skinning weights.

Parameters:
- none

Returns:
- List[List[VertexWeight]] – For each vertex, the list of its weights.

Notes:
- VertexWeight is defined by the Cascadeur API.

## Usage Notes
- Read-only access intended for processing, validation, or export scenarios.
- Exact container and element types are provided by the Cascadeur Python API bindings.

