[CLEAN]

# csc.update.Group

## Overview

Represents a group node in Cascadeur’s update graph. Provides ways to manage child nodes, inputs/outputs, and interface/virtual nodes (constants and settings). Supports accessing nodes by name or id and organizing them hierarchically. Specific parameter types and return values are largely undocumented in the source text.

## Class Definition

```python
class csc.update.Group
```

## Constructor

### `__init__(*args, **kwargs)`
Constructor for the Group node; parameters are undocumented.
- Parameters:
  - *args: undocumented – additional positional arguments
  - **kwargs: undocumented – additional keyword arguments
- Returns: None

## Methods

### `add_input(name)`
Add an input attribute to the group (details undocumented).
- Parameters:
  - name: undocumented – input name
- Returns: undocumented

### `add_output(name)`
Add an output attribute to the group (details undocumented).
- Parameters:
  - name: undocumented – output name
- Returns: undocumented

### `attributes(d)`
Return attributes related to inputs and outputs (details undocumented).
- Parameters:
  - d: undocumented – filter or direction (undocumented)
- Returns: undocumented

### `constant_datas()`
Get a virtual node to access constant datas.
- Parameters: none
- Returns: undocumented

### `constant_settings()`
Get a virtual node to access constant settings.
- Parameters: none
- Returns: undocumented

### `create_group(name)`
Create a subgroup (details undocumented).
- Parameters:
  - name: undocumented – subgroup name
- Returns: undocumented

### `delete_node(node)`
Delete a child node from the group (details undocumented).
- Parameters:
  - node: undocumented – target node identifier or reference
- Returns: undocumented

### `equal_to(arg0)`
Check equality with another object (details undocumented).
- Parameters:
  - arg0: undocumented – object to compare
- Returns: undocumented

### `full_name()`
Get the full name including all parent nodes.
- Parameters: none
- Returns: undocumented

### `group(nodes, name)`
Group given nodes under a new subgroup name (details undocumented).
- Parameters:
  - nodes: undocumented – nodes to group
  - name: undocumented – name of the new subgroup
- Returns: undocumented

### `group_id()`
Get the subgroup identifier (details undocumented).
- Parameters: none
- Returns: undocumented

### `has_input(name)`
Check if there is an input with the given name.
- Parameters:
  - name: undocumented – input name
- Returns: undocumented

### `has_node(name)`
Check whether there is a child node with the given name.
- Parameters:
  - name: undocumented – node name
- Returns: undocumented

### `has_output(name)`
Check if there is an output with the given name.
- Parameters:
  - name: undocumented – output name
- Returns: undocumented

### `id()`
Get the unique id of this group.
- Parameters: none
- Returns: undocumented

### `input(name)`
Get an input attribute by name; acts as a shortcut when there is a single input (details undocumented).
- Parameters:
  - name: undocumented – input name
- Returns: undocumented

### `input_interface_node()`
Access the input-side interface node (details undocumented).
- Parameters: none
- Returns: undocumented

### `inputs()`
Return all input attributes (details undocumented).
- Parameters: none
- Returns: undocumented

### `interface_input(name)`
Access an interface input attribute by name (details undocumented).
- Parameters:
  - name: undocumented – interface input name
- Returns: undocumented

### `interface_inputs()`
Get group attributes exposed as interface inputs.
- Parameters: none
- Returns: undocumented

### `interface_node(direction)`
Access the interface node for a given direction.
- Parameters:
  - direction: undocumented – interface direction
- Returns: undocumented

### `interface_output(name)`
Access an interface output attribute by name (details undocumented).
- Parameters:
  - name: undocumented – interface output name
- Returns: undocumented

### `interface_outputs()`
Return interface output attributes (details undocumented).
- Parameters: none
- Returns: undocumented

### `is_active()`
Check whether the group is active for the current actuality/state.
- Parameters: none
- Returns: undocumented

### `is_fictive()`
Whether this is a fictive node (e.g., constants, inputs/outputs of a group, or external properties).
- Parameters: none
- Returns: undocumented

### `is_root()`
Whether this group is the root (details undocumented).
- Parameters: none
- Returns: undocumented

### `leaf_children()`
Get all leaf child nodes (settings, datas, functions).
- Parameters: none
- Returns: undocumented

### `name()`
Get the group’s name.
- Parameters: none
- Returns: undocumented

### `node(name: str) -> csc.update.Node`
Access a child node by name.
- Parameters:
  - name: str – node name
- Returns: csc.update.Node

### `node(node: Union[csc.update.GroupId, csc.update.InterfaceId, csc.update.ExternalPropertiesId, csc.update.ConstantDatasId, csc.update.ConstantSettingsId, csc.model.ObjectId, csc.model.HyperedgeId, csc.model.DataId, csc.model.SettingFunctionId, csc.model.SettingId]) -> csc.update.Node`
Access a child node by id.
- Parameters:
  - node: Union[csc.update.GroupId, csc.update.InterfaceId, csc.update.ExternalPropertiesId, csc.update.ConstantDatasId, csc.update.ConstantSettingsId, csc.model.ObjectId, csc.model.HyperedgeId, csc.model.DataId, csc.model.SettingFunctionId, csc.model.SettingId] – node identifier
- Returns: csc.update.Node

### `node_deep(name)`
Access a node by name or id recursively.
- Parameters:
  - name: undocumented – node name or id
- Returns: undocumented

### `node_with_type(type_name, name)`
Find a node with the given type and name.
- Parameters:
  - type_name: undocumented – type name
  - name: undocumented – node name
- Returns: undocumented

### `node_with_type_deep(type_name, name)`
Recursively find a node with the given type and name.
- Parameters:
  - type_name: undocumented – type name
  - name: undocumented – node name
- Returns: undocumented

### `nodes()`
Get all direct child nodes (non-recursive).
- Parameters: none
- Returns: undocumented

### `output(name)`
Get an output attribute by name; acts as a shortcut when there is a single output (details undocumented).
- Parameters:
  - name: undocumented – output name
- Returns: undocumented

### `output_interface_node()`
Access the output-side interface node (details undocumented).
- Parameters: none
- Returns: undocumented

### `outputs()`
Return all output attributes (details undocumented).
- Parameters: none
- Returns: undocumented

### `parent_group()`
Return the parent group (where this group node is located).
- Parameters: none
- Returns: undocumented

### `parent_object()`
Return the underlying object of this node (details undocumented).
- Parameters: none
- Returns: undocumented

### `set_name(name)`
Rename this group node.
- Parameters:
  - name: undocumented – new name
- Returns: undocumented

## Usage Notes

- Many parameter and return types are undocumented here; consult the official Cascadeur API documentation for authoritative details.  
- Methods related to “interface”, “constants”, and “settings” refer to virtual/interface nodes in the update graph.  
- Node lookup utilities support both names and various id types; prefer the explicit overloads when available.

