[CLEAN]

# csc.update.UpdateGroup

## Overview
Represents an update group node within Cascadeur’s update system. An UpdateGroup organizes nodes, inputs/outputs, constants, and settings, and supports hierarchical grouping. It provides methods to create and manage data/functions, query structure, and navigate parent/child relationships. Many details are undocumented in the source material and may require consulting the original API reference.

## Class Definition
```python
class csc.update.UpdateGroup
```

## Constructor

### `__init__(*args, **kwargs)`
Initialize a new UpdateGroup (details undocumented).

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

**Returns:**
- None

## Methods

### `add_input(name)`
Add an input attribute with the given name.

**Parameters:**
- `name`: undocumented — input name

**Returns:**
- undocumented

### `add_output(name)`
Add an output attribute with the given name.

**Parameters:**
- `name`: undocumented — output name

**Returns:**
- undocumented

### `attributes(d)`
Return the collection of all input and output attributes.

**Parameters:**
- `d`: undocumented

**Returns:**
- undocumented

### `constant_datas()`
Get the virtual node to access constant data.

**Returns:**
- undocumented

### `constant_settings()`
Get the virtual node to access constant settings.

**Returns:**
- undocumented

### `create_group(name)`
Create a child group with the given name.

**Parameters:**
- `name`: undocumented — group name

**Returns:**
- undocumented

### `create_regular_data(name, value, ...)`
Create a regular data node.

**Parameters:**
- `name`: undocumented
- `value`: undocumented
- `...`: undocumented

**Returns:**
- undocumented

### `create_regular_function(name, function)`
Create a regular function node.

**Parameters:**
- `name`: undocumented
- `function`: undocumented

**Returns:**
- undocumented

### `create_setting_data(name, value, ...)`
Create a setting data node.

**Parameters:**
- `name`: undocumented
- `value`: undocumented
- `...`: undocumented

**Returns:**
- undocumented

### `create_setting_function(name, ...)`
Create a setting function node.

**Parameters:**
- `name`: undocumented
- `...`: undocumented

**Returns:**
- undocumented

### `create_sub_update_group(arg0)`
Create a sub update group.

**Parameters:**
- `arg0`: undocumented

**Returns:**
- undocumented

### `create_sub_update_group2(name, group_id)`
Create a sub update group by name and identifier.

**Parameters:**
- `name`: undocumented
- `group_id`: undocumented

**Returns:**
- `UpdateGroup`

### `delete_node(node)`
Delete the specified child node.

**Parameters:**
- `node`: undocumented

**Returns:**
- undocumented

### `equal_to(arg0)`
Check equality against the given object.

**Parameters:**
- `arg0`: undocumented

**Returns:**
- undocumented

### `external_properties()`
Access the external properties virtual node.

**Returns:**
- `ExternalProperties`

### `full_name()`
Get the full hierarchical name including parent groups.

**Returns:**
- undocumented

### `group(nodes, name)`
Group the given nodes under a new group with the provided name.

**Parameters:**
- `nodes`: undocumented
- `name`: undocumented

**Returns:**
- undocumented

### `group_id()`
Get this group's identifier.

**Returns:**
- undocumented

### `groups()`
Return the collection of sub-groups.

**Returns:**
- `UpdateGroup{}` — undocumented collection of UpdateGroup

### `has_input(name)`
Check whether there is an input with the given name.

**Parameters:**
- `name`: undocumented

**Returns:**
- undocumented

### `has_node(name)`
Check whether there is a child node with the given name.

**Parameters:**
- `name`: undocumented

**Returns:**
- undocumented

### `has_output(name)`
Check whether there is an output with the given name.

**Parameters:**
- `name`: undocumented

**Returns:**
- undocumented

### `id()`
Get the unique identifier.

**Returns:**
- undocumented

### `input(name)`
Shortcut accessor when the node has a single input attribute.

**Parameters:**
- `name`: undocumented

**Returns:**
- undocumented

### `input_interface_node()`
Get the interface node for inputs.

**Returns:**
- undocumented

### `inputs()`
Return the collection of all input attributes.

**Returns:**
- undocumented

### `interface_input(name)`
Access a specific interface input attribute by name.

**Parameters:**
- `name`: undocumented

**Returns:**
- undocumented

### `interface_inputs()`
Get group attributes exposed as interface inputs.

**Returns:**
- undocumented

### `interface_node(direction)`
Access the interface node.

**Parameters:**
- `direction`: undocumented

**Returns:**
- undocumented

### `interface_output(name)`
Access a specific interface output attribute by name.

**Parameters:**
- `name`: undocumented

**Returns:**
- undocumented

### `interface_outputs()`
Get group attributes exposed as interface outputs.

**Returns:**
- undocumented

### `is_active()`
Check whether the group is active for the current actuality/state.

**Returns:**
- undocumented

**Notes:**
- See additional functionality in `csc.update.UpdateEditor`.

### `is_fictive()`
Whether this node is fictive (e.g., constants, inputs/outputs of a group, or external properties).

**Returns:**
- undocumented

### `is_root()`
Whether this group is the root.

**Returns:**
- undocumented

### `leaf_children()`
Get all leaf nodes (settings, data, functions).

**Returns:**
- undocumented

### `name()`
Get the name of the node.

**Returns:**
- undocumented

### `node(*args, **kwargs)`
Overloaded accessor to a child node.

**Parameters:**
- `*args`: undocumented
- `**kwargs`: undocumented

**Returns:**
- undocumented

### `node_deep(name)`
Access a node by name or id recursively.

**Parameters:**
- `name`: undocumented

**Returns:**
- undocumented

### `node_with_type(type_name, name)`
Find a node with the given name and type.

**Parameters:**
- `type_name`: undocumented
- `name`: undocumented

**Returns:**
- undocumented

### `node_with_type_deep(type_name, name)`
Recursively find a node with the given name and type.

**Parameters:**
- `type_name`: undocumented
- `name`: undocumented

**Returns:**
- undocumented

### `nodes()`
Get all direct child nodes (non-recursive).

**Returns:**
- undocumented

### `output(name)`
Shortcut accessor when the node has a single output attribute.

**Parameters:**
- `name`: undocumented

**Returns:**
- undocumented

### `output_interface_node()`
Get the interface node for outputs.

**Returns:**
- undocumented

### `outputs()`
Return the collection of all output attributes.

**Returns:**
- undocumented

### `parent_group()`
Return the parent group where this group node is located.

**Returns:**
- undocumented

### `parent_object()`
Return the underlying object of this node.

**Returns:**
- undocumented

### `regular_datas()`
Return the collection of regular data nodes.

**Returns:**
- `RegularData{}` — undocumented collection of regular data

### `regular_functions()`
Return the collection of regular function nodes.

**Returns:**
- `RegularFunction{}` — undocumented collection of regular functions

### `set_name(name)`
Rename this node.

**Parameters:**
- `name`: undocumented

**Returns:**
- undocumented

### `setting_functions()`
Return the collection of setting function nodes.

**Returns:**
- `SettingFunction{}` — undocumented collection of setting functions

### `settings_datas()`
Return the collection of settings data nodes.

**Returns:**
- `SettingsData{}` — undocumented collection of settings data

## Usage Notes
- This summary reflects limited information; consult the original documentation for precise types, return values, and semantics.
- Many methods return collections or node handles whose exact shapes are undocumented here.
- Hierarchical operations (grouping, node access) may depend on existing graph structure and naming conventions.

