[CLEAN]

# csc.model.ModelViewer

**Module:** `csc.model.ModelViewer`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.model.ModelViewer.html)

## Overview

The `ModelViewer` class represents basic methods to view the scene model in Cascadeur. It provides access to object information, names, types, and related viewers for comprehensive model inspection and analysis.

## Class Definition

```python
class csc.model.ModelViewer
```

Represents basic methods to view the scene model, offering functionality to inspect objects, their properties, and access related viewing systems.

## Constructor

### `__init__(self, *args, **kwargs) -> None`

Initializes a ModelViewer instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Variable length keyword arguments

**Returns:**
- None

## Viewer Access Methods

### `behaviour_viewer(self) -> BehaviourViewer`

Gets the behaviour viewer for examining object behaviours.

**Returns:**
- BehaviourViewer: The behaviour viewer instance for inspecting object behaviours

### `data_viewer(self) -> DataViewer`

Gets the data viewer for examining object data.

**Returns:**
- DataViewer: The data viewer instance for inspecting object data

## Object Query Methods

### `get_objects(*args, **kwargs) -> List[csc.model.ObjectId]`

Gets objects from the model. This method has multiple overloaded signatures:

**Overloaded signatures:**
1. `get_objects(self) -> List[csc.model.ObjectId]`
2. `get_objects(self, name: str) -> List[csc.model.ObjectId]`

**Parameters:**
- `name` (str, optional): Name filter to find objects with specific names

**Returns:**
- List[csc.model.ObjectId]: List of object identifiers, either all objects or those matching the name filter

### `get_object_name(self, id: csc.model.ObjectId) -> str`

Gets the name of the specified object.

**Parameters:**
- `id` (csc.model.ObjectId): The object identifier

**Returns:**
- str: The name of the object

### `get_object_type_name(self, id: csc.model.ObjectId) -> str`

Gets the type name of the specified object.

**Parameters:**
- `id` (csc.model.ObjectId): The object identifier

**Returns:**
- str: The type name of the object

## Usage Example

```python
import csc.model
import csc.app

# Get the application and scene
app = csc.app.get_application()
scene = app.get_scene_manager().current_scene()

# Get the model viewer
model_viewer = scene.model_viewer()

# Get all objects in the model
all_objects = model_viewer.get_objects()
print(f"Total objects in model: {len(all_objects)}")

# Get objects by name
character_objects = model_viewer.get_objects("Character")
print(f"Character objects found: {len(character_objects)}")

# Inspect object details
for obj_id in all_objects[:5]:  # First 5 objects
    name = model_viewer.get_object_name(obj_id)
    type_name = model_viewer.get_object_type_name(obj_id)
    print(f"Object: {name}, Type: {type_name}")

# Access related viewers
behaviour_viewer = model_viewer.behaviour_viewer()
data_viewer = model_viewer.data_viewer()

# Use related viewers for detailed inspection
for obj_id in character_objects:
    name = model_viewer.get_object_name(obj_id)
    
    # Get object data through data viewer
    # object_data = data_viewer.get_data(obj_id)  # Example usage
    
    # Get object behaviours through behaviour viewer  
    # behaviours = behaviour_viewer.get_behaviours(obj_id)  # Example usage
    
    print(f"Processing object: {name}")

# Search for specific objects
arm_objects = model_viewer.get_objects("Arm")
leg_objects = model_viewer.get_objects("Leg")

print(f"Found {len(arm_objects)} arm objects")
print(f"Found {len(leg_objects)} leg objects")
```

## Usage Notes

- ModelViewer provides read-only access to scene model information
- Use the overloaded `get_objects()` method to retrieve all objects or filter by name
- Object names and type names help identify and categorize scene elements
- Access related viewers (behaviour_viewer, data_viewer) for detailed object inspection
- Object IDs can be used with other model system components for further operations
- The viewer provides a foundation for model analysis and object management workflows

## See Also

- `csc.model.BehaviourViewer` - Viewer for object behaviours
- `csc.model.DataViewer` - Viewer for object data
- `csc.model.ObjectId` - Object identifier class
- `csc.model.ModelEditor` - Editor for model modifications
- `csc.domain.Scene` - Scene class that provides model viewer access
- Model system and object management in Cascadeur