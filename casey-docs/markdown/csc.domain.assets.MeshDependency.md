# [CLEAN] csc.domain.assets.MeshDependency

## Overview
MeshDependency represents mesh skinning dependency data, exposing inverse bind matrices for joints and per-vertex weight information used in deformation/skinning. It provides read access to the core data needed to understand how a mesh is influenced by a rig. This is useful for inspection, validation, or export workflows. Details below reflect only what is present in the source documentation.

## Class Definition
```python
class MeshDependency:
    ...
```

## Constructor

### `__init__(arg0)`
Initializes a MeshDependency instance.

- arg0: (unspecified) – Undocumented input from the source documentation.

## Methods

### `joints_inverse_bind_matrices() -> Matrix4f[]`
Returns the inverse bind matrices associated with joints.

- Parameters: None
- Returns: Matrix4f[] – Collection of 4x4 inverse bind matrices.
- Notes: Matrix4f type is defined by the Cascadeur API.

### `vertices_weights() -> List[List[VertexWeight]]`
Returns per-vertex skinning weights.

- Parameters: None
- Returns: List[List[VertexWeight]] – A list where each item contains the weights for a given vertex.
- Notes: VertexWeight type is defined by the Cascadeur API.

## Usage Notes
- Intended for read access to bind transforms and skinning weights for processing and export scenarios.
- Exact container and element types (Matrix4f, VertexWeight) are provided by the Cascadeur Python API bindings.
- No additional behavior or mutators are documented here.
