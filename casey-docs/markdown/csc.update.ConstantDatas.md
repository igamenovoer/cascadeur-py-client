[CLEAN]

# csc.update.ConstantDatas

## Overview
ConstantDatas represents a node that provides constant data within the update system. It appears broadly in the graph and can be referenced anywhere a constant value is needed. The API exposes utilities to query inputs/outputs, naming, hierarchy, and activity state, plus helpers for managing constant data entries. Specific types and return values are largely undocumented in the source material.

## Class Definition
```python
class csc.update.ConstantDatas
```

## Constructor

### `__init__(*args, **kwargs)`
Initialize a ConstantDatas instance (details undocumented).

**Parameters:**
- `*args`: undocumented – additional positional arguments
- `**kwargs`: undocumented – additional keyword arguments

**Returns:**
- None

## Methods

### `add_data(name, value: Data.Value)`
Add a constant data entry to this node.

**Parameters:**
- `name`: undocumented – name/key of the data
- `value: Data.Value` – value to add

**Returns:**
- undocumented

---

### `attributes(d)`
Return an array of all input and output attributes (usage details undocumented).

**Parameters:**
- `d`: undocumented

**Returns:**
- undocumented

---

### `equal_to(arg0)`
Check whether this node is equal to another object.

**Parameters:**
- `arg0`: undocumented – object to compare against

**Returns:**
- undocumented

---

### `full_name()`
Get the name including all parent nodes.

**Parameters:**
- None

**Returns:**
- undocumented

---

### `has_input(name)`
Check if there is an input with the given name.

**Parameters:**
- `name`: undocumented – input name to check

**Returns:**
- undocumented

---

### `has_output(name)`
Check if there is an output with the given name.

**Parameters:**
- `name`: undocumented – output name to check

**Returns:**
- undocumented

---

### `id()`
Get the unique identifier for this node.

**Parameters:**
- None

**Returns:**
- undocumented

---

### `input(name)`
Retrieve an input attribute by name; if the node has only one input, this may act as a shortcut.

**Parameters:**
- `name`: undocumented – input name

**Returns:**
- undocumented

---

### `inputs()`
Get an array of all input attributes.

**Parameters:**
- None

**Returns:**
- undocumented

---

### `is_active()`
Check whether the node is active for the current actuality states.

**Parameters:**
- None

**Returns:**
- undocumented

---

### `is_fictive()`
Determine whether this is a fictive node (e.g., constants, group I/O, or external properties).

**Parameters:**
- None

**Returns:**
- undocumented

---

### `name()`
Get the node name.

**Parameters:**
- None

**Returns:**
- undocumented

---

### `output(name)`
Retrieve an output attribute by name; if the node has only one output, this may act as a shortcut.

**Parameters:**
- `name`: undocumented – output name

**Returns:**
- undocumented

---

### `outputs()`
Get an array of all output attributes.

**Parameters:**
- None

**Returns:**
- undocumented

---

### `parent_group()`
Return the parent group where this node is located.

**Parameters:**
- None

**Returns:**
- undocumented

---

### `parent_object()`
Return the object (owner) of this node.

**Parameters:**
- None

**Returns:**
- undocumented

---

### `set_name(name)`
Rename the node.

**Parameters:**
- `name`: undocumented – new name for the node

**Returns:**
- undocumented

## Usage Notes
- Some methods act as shortcuts when there is only a single input or output; exact return types are undocumented.
- Behavior may depend on the surrounding update graph and editor state.

