[CLEAN]

# csc.layers.Layers

## Overview
The Layers class is the root object that describes the scene's layer hierarchy. Each scene object can be placed on a layer to define its interpolation properties. This documentation summarizes the available constructor, methods, and attributes as observed, with unspecified details marked as undocumented.

## Class Definition
```python
class csc.layers.Layers
```

## Constructor

### `__init__(*args, **kwargs)`
Initializes a Layers instance. Specific parameters and behavior are undocumented.

**Parameters:**
- `*args`: undocumented – variable positional arguments
- `**kwargs`: undocumented – variable keyword arguments

**Returns:**
- undocumented

## Methods

### `folders() -> <FolderId, Folder>{}`
Returns a collection of folders associated with the layer hierarchy; exact container type is undocumented.

**Returns:**
- `<FolderId, Folder>{}`: undocumented exact type

### `layers() -> LayersContainer`
Returns the layers container; precise API is undocumented.

**Returns:**
- `LayersContainer`: undocumented

### `userLabels() -> UserLabels`
Returns the user labels associated with layers; details are undocumented.

**Returns:**
- `UserLabels`: undocumented

## Attributes

- `root_id`: `csc.Guid` — Identifier of the root of the layer hierarchy; further details are undocumented.

## Usage Notes

- This class represents the hierarchy of layers used to control interpolation behavior in the scene.
- Type details and container semantics are taken from the source text and remain undocumented.
- Refer to the original API for authoritative definitions.

