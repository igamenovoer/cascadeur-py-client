[CLEAN]

# csc.domain.assets.AssetsManager

**Module:** `csc.domain.assets.AssetsManager`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.assets.AssetsManager.html)

## Overview

The `AssetsManager` class provides comprehensive functionality for managing various types of assets within the Cascadeur domain system. It implements basic methods for adding, retrieving, and removing assets, with support for different asset types including meshes, mesh dependencies, and blendshapes.

## Class Definition

```python
class csc.domain.assets.AssetsManager
```

The AssetsManager class serves as the central hub for asset management operations, providing overloaded methods for different asset types and built-in geometric primitives.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new AssetsManager instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Methods

### `add(self, asset) -> AssetId` (Overloaded)

Adds an asset to the manager and returns its unique identifier.

**Overloads:**

#### `add(self, asset: MeshBlendshape) -> AssetId`
Adds a mesh blendshape asset.

**Parameters:**
- `asset` (MeshBlendshape): The mesh blendshape to add

**Returns:**
- AssetId: Unique identifier for the added blendshape asset

#### `add(self, asset: Mesh) -> AssetId`
Adds a mesh asset.

**Parameters:**
- `asset` (Mesh): The mesh to add

**Returns:**
- AssetId: Unique identifier for the added mesh asset

#### `add(self, asset: MeshDependency) -> AssetId`
Adds a mesh dependency asset.

**Parameters:**
- `asset` (MeshDependency): The mesh dependency to add

**Returns:**
- AssetId: Unique identifier for the added dependency asset

### `at(self, asset_id) -> Asset`

Retrieves an asset by its identifier.

**Parameters:**
- `asset_id`: The asset identifier

**Returns:**
- Asset: The asset corresponding to the identifier

### `erase(self, ids) -> None`

Removes assets from the manager.

**Parameters:**
- `ids`: Asset identifiers to remove

### `get_cube_mesh() -> Mesh` (Static)

Generates a default cube mesh primitive.

**Returns:**
- Mesh: A cube mesh asset

### `get_plane_mesh() -> Mesh` (Static)

Generates a default plane mesh primitive.

**Returns:**
- Mesh: A plane mesh asset

## Usage Example

```python
import csc.domain.assets

# Create an assets manager
assets_manager = csc.domain.assets.AssetsManager()

# Create primitive meshes
cube_mesh = csc.domain.assets.AssetsManager.get_cube_mesh()
plane_mesh = csc.domain.assets.AssetsManager.get_plane_mesh()

# Add meshes to the manager
cube_id = assets_manager.add(cube_mesh)
plane_id = assets_manager.add(plane_mesh)

# Retrieve assets by ID
retrieved_cube = assets_manager.at(cube_id)
retrieved_plane = assets_manager.at(plane_id)

# Working with different asset types
if hasattr(csc.domain.assets, 'MeshBlendshape'):
    blendshape = csc.domain.assets.MeshBlendshape()
    blendshape_id = assets_manager.add(blendshape)

# Remove assets when no longer needed
assets_manager.erase([cube_id, plane_id])

# Asset management workflow
def manage_scene_assets():
    manager = csc.domain.assets.AssetsManager()
    
    # Add various asset types
    asset_ids = []
    
    # Add primitive meshes
    primitive_cube = manager.get_cube_mesh()
    primitive_plane = manager.get_plane_mesh()
    
    cube_id = manager.add(primitive_cube)
    plane_id = manager.add(primitive_plane)
    
    asset_ids.extend([cube_id, plane_id])
    
    # Process assets
    for asset_id in asset_ids:
        asset = manager.at(asset_id)
        # Process each asset as needed
    
    return asset_ids, manager
```

## Usage Notes

- The AssetsManager supports multiple asset types through overloaded `add()` methods
- Asset identifiers are unique and persistent for the lifetime of the manager
- Primitive mesh generation (cube, plane) provides standard geometric assets
- The `at()` method enables asset retrieval by identifier for further processing
- Asset removal with `erase()` helps manage memory and organizational efficiency
- The manager integrates with the broader Cascadeur asset pipeline
- Always store asset IDs when adding assets for later retrieval or removal

## See Also

- `csc.domain.Asset` - Base asset representation
- `csc.domain.AssetId` - Asset identification system
- `csc.domain.assets.Mesh` - Mesh asset implementation
- `csc.domain.assets.MeshDependency` - Mesh dependency relationships
- `csc.domain.assets.MeshBlendshape` - Blendshape asset functionality