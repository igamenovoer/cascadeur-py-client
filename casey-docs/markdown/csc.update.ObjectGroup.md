[CLEAN]

# csc.update.ObjectGroup

## Overview

ObjectGroup represents a group node in Cascadeur's update graph. It organizes objects and nested sub-groups, and exposes inputs, outputs, and interface nodes for connecting data flow. It also provides access to virtual nodes for constant data and settings, and common utilities for querying, grouping, and renaming nodes within the group.

## Class Definition

```python
class csc.update.ObjectGroup
```

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new ObjectGroup instance.

- Parameters:
  - `*args`: undocumented
  - `**kwargs`: undocumented

## Methods

### `add_input(self, name)`

Add an input attribute to the group.

- Parameters:
  - `name`: undocumented
- Returns: undocumented

### `add_output(self, name)`

Add an output attribute to the group.

- Parameters:
  - `name`: undocumented
- Returns: undocumented

### `attributes(self, d)`

Return an array of all input and output attributes.

- Parameters:
  - `d`: undocumented
- Returns: undocumented

### `constant_datas(self)`

Get a virtual node to access constant datas.

- Parameters: none
- Returns: undocumented

### `constant_settings(self)`

Get a virtual node to access constant settings.

- Parameters: none
- Returns: undocumented

### `create_group(self, name)`

Create a new subgroup within this group.

- Parameters:
  - `name`: undocumented
- Returns: undocumented

### `create_object(self, name: str) -> csc.update.Object`

Create a new object with the given name.

- Parameters:
  - `name: str` – object name
- Returns: `csc.update.Object`

### `create_object(self, name: str, id: csc.model.ObjectId) -> csc.update.Object`

Create a new object with the given name and explicit id.

- Parameters:
  - `name: str` – object name
  - `id: csc.model.ObjectId` – undocumented
- Returns: `csc.update.Object`

### `create_sub_object_group(self, name) -> ObjectGroup`

Create a nested ObjectGroup.

- Parameters:
  - `name`: undocumented
- Returns: `ObjectGroup`

### `delete_node(self, node)`

Delete a child node from this group.

- Parameters:
  - `node`: undocumented
- Returns: undocumented

### `equal_to(self, arg0)`

Check equality with another value.

- Parameters:
  - `arg0`: undocumented
- Returns: undocumented

### `full_name(self)`

Get the full hierarchical name including all parent nodes.

- Parameters: none
- Returns: undocumented

### `group(self, nodes, name)`

Group nodes under a new subgroup with the given name.

- Parameters:
  - `nodes`: undocumented
  - `name`: undocumented
- Returns: undocumented

### `group_id(self)`

Get the identifier for a subgroup.

- Parameters: none
- Returns: undocumented

### `has_input(self, name)`

Check whether there is an input with the given name.

- Parameters:
  - `name`: undocumented
- Returns: undocumented

### `has_node(self, name)`

Check whether there is a child node with the given name.

- Parameters:
  - `name`: undocumented
- Returns: undocumented

### `has_output(self, name)`

Check whether there is an output with the given name.

- Parameters:
  - `name`: undocumented
- Returns: undocumented

### `id(self)`

Get unique id of this group.

- Parameters: none
- Returns: undocumented

### `input(self, name)`

Access an input attribute by name (shortcut if only one input exists).

- Parameters:
  - `name`: undocumented
- Returns: undocumented

### `input_interface_node(self)`

Access the input interface node.

- Parameters: none
- Returns: undocumented

### `inputs(self)`

Return all input attributes.

- Parameters: none
- Returns: undocumented

### `interface_input(self, name)`

Access an interface input attribute by name.

- Parameters:
  - `name`: undocumented
- Returns: undocumented

### `interface_inputs(self)`

Get group attributes as interface attributes (inputs).

- Parameters: none
- Returns: undocumented

### `interface_node(self, direction)`

Access the interface node for a given direction.

- Parameters:
  - `direction`: undocumented
- Returns: undocumented

### `interface_output(self, name)`

Access an interface output attribute by name.

- Parameters:
  - `name`: undocumented
- Returns: undocumented

### `interface_outputs(self)`

Get group attributes as interface attributes (outputs).

- Parameters: none
- Returns: undocumented

### `is_active(self)`

Check whether the group is active for current actuality states.

- Parameters: none
- Returns: undocumented
- Notes: See Additional functionality in csc.update.UpdateEditor.

### `is_fictive(self)`

Whether this node is fictive (constants, inputs/outputs of a group, or external properties).

- Parameters: none
- Returns: undocumented

### `is_root(self)`

Check whether this group is the root.

- Parameters: none
- Returns: undocumented

### `leaf_children(self)`

Get all leaf child nodes (settings, datas, functions).

- Parameters: none
- Returns: undocumented

### `name(self)`

Get the group's name.

- Parameters: none
- Returns: undocumented

### `node(self, *args, **kwargs)`

Access a child node (overloaded function).

- Parameters:
  - `*args`: undocumented
  - `**kwargs`: undocumented
- Returns: undocumented

### `node_deep(self, name)`

Access a node by name or id recursively.

- Parameters:
  - `name`: undocumented
- Returns: undocumented

### `node_with_type(self, type_name, name)`

Find a node with the given name and type.

- Parameters:
  - `type_name`: undocumented
  - `name`: undocumented
- Returns: undocumented

### `node_with_type_deep(self, type_name, name)`

Find a node with the given name and type recursively.

- Parameters:
  - `type_name`: undocumented
  - `name`: undocumented
- Returns: undocumented

### `nodes(self)`

Get all direct child nodes (non-recursive).

- Parameters: none
- Returns: undocumented

### `object_groups(self)`

Get contained object groups.

- Parameters: none
- Returns: undocumented

### `objects(self)`

Get contained objects.

- Parameters: none
- Returns: undocumented

### `output(self, name)`

Access an output attribute by name (shortcut if only one output exists).

- Parameters:
  - `name`: undocumented
- Returns: undocumented

### `output_interface_node(self)`

Access the output interface node.

- Parameters: none
- Returns: undocumented

### `outputs(self)`

Return all output attributes.

- Parameters: none
- Returns: undocumented

### `parent_group(self)`

Return the parent group containing this node.

- Parameters: none
- Returns: undocumented

### `parent_object(self)`

Return the object of this node.

- Parameters: none
- Returns: undocumented

### `set_name(self, name)`

Rename this node.

- Parameters:
  - `name`: undocumented
- Returns: undocumented

## Usage Notes

- Many return types and parameter details are undocumented here; consult the original API reference for exact types and behaviors.
- Methods mirror Cascadeur's node-graph concepts (groups, nodes, interfaces, constants); use with care in the context of the update editor.

