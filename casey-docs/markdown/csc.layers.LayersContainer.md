[CLEAN]

# csc.layers.LayersContainer

## Overview
Container class for layers in the Cascadeur API. Provides access to layers and their identifiers, and exposes mappings between layers, layer IDs, and object IDs. Specific parameter and return details are largely undocumented in the source available here. Use this as a utility for querying and organizing layers.

## Class Definition
```python
class csc.layers.LayersContainer
```

## Constructor

### `__init__(*args, **kwargs)`
Constructor; parameters are undocumented.

**Parameters:**
- `*args`: undocumented – variable arguments
- `**kwargs`: undocumented – keyword arguments

**Returns:**
- undocumented

## Methods

### `at(arg0) -> Layer`
Returns a Layer; details are undocumented.

**Parameters:**
- `arg0`: undocumented – identifier or handle

**Returns:**
- `Layer`: undocumented

### `has_any_obj_ids()`
Undocumented.

**Returns:**
- undocumented

### `has_obj_id(id)`
Undocumented.

**Parameters:**
- `id`: undocumented

**Returns:**
- undocumented

### `layer_id_by_obj_id(id) -> LayerId`
Returns a LayerId; details are undocumented.

**Parameters:**
- `id`: undocumented

**Returns:**
- `LayerId`: undocumented

### `layer_id_by_obj_id_or_null(id) -> LayerId`
Returns a LayerId; details are undocumented.

**Parameters:**
- `id`: undocumented

**Returns:**
- `LayerId`: undocumented

### `map() -> <LayerId, Layer>{}`
Returns a mapping of layer identifiers to layers; details are undocumented.

**Returns:**
- `<LayerId, Layer>{}`: undocumented

### `obj_ids() -> <csc.model.ObjectId, LayerId>{}`
Returns a mapping of object identifiers to layer identifiers; details are undocumented.

**Returns:**
- `<csc.model.ObjectId, LayerId>{}`: undocumented

## Usage Notes
- Method and parameter semantics are not fully documented here; consult the official Cascadeur documentation for authoritative details.
- Identifiers referenced by the methods are internal object or layer IDs; their formats and lifecycles are undocumented in this context.

