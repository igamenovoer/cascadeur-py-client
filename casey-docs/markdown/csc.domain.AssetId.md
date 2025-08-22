[CLEAN]

# csc.domain.AssetId

**Module:** `csc.domain.AssetId`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.AssetId.html)

## Overview

The `AssetId` class represents a unique identifier for assets within the Cascadeur domain system. It provides functionality for creating, managing, and working with asset identifiers.

## Class Definition

```python
class csc.domain.AssetId
```

The AssetId class encapsulates asset identification functionality and provides methods for asset ID operations.

## Constructor

The constructor is overloaded to support different initialization methods:

### `__init__(self, arg0: str) -> None`

Creates a new AssetId from a string representation.

**Parameters:**
- `arg0` (str): String representation of the asset ID

**Returns:**
- None

### `__init__(self) -> None`

Creates a new empty/null AssetId instance.

**Returns:**
- None

## Methods

### `is_null(self) -> bool`

Checks if the asset ID is null or empty.

**Returns:**
- bool: True if the asset ID is null, False otherwise

### `null() -> csc.domain.AssetId` (static)

Creates and returns a null asset ID instance.

**Returns:**
- csc.domain.AssetId: A null asset ID instance

### `to_string(self) -> str`

Converts the asset ID to its string representation.

**Returns:**
- str: String representation of the asset ID

## Usage Example

```python
import csc.domain

# Create a null asset ID
null_asset_id = csc.domain.AssetId()

# Create an asset ID from string
asset_id_str = "asset_12345"
asset_id = csc.domain.AssetId(asset_id_str)

# Check if asset ID is null
if asset_id.is_null():
    print("Asset ID is null")

# Get string representation
asset_id_string = asset_id.to_string()
print(f"Asset ID: {asset_id_string}")

# Create a null asset ID using static method
null_asset_id_static = csc.domain.AssetId.null()

# Compare asset IDs
if null_asset_id.is_null() and null_asset_id_static.is_null():
    print("Both asset IDs are null")

# Working with assets manager
app = csc.app.get_application()
scene = app.get_scene_manager().get_current_scene()
assets_manager = scene.assets_manager()

# Use asset ID to retrieve assets (example)
# asset = assets_manager.get_asset_by_id(asset_id)
```

## Usage Notes

- The constructor supports both string initialization and default (null) initialization
- Use `is_null()` to check if an asset ID is empty or uninitialized
- The `null()` static method provides a convenient way to create null asset IDs
- String format follows standard asset identifier conventions
- Asset IDs are commonly used with the AssetsManager for asset retrieval and management

## See Also

- `csc.domain.Asset` - Asset class that uses these identifiers
- `csc.domain.assets.AssetsManager` - Asset management using asset IDs
- `csc.Guid` - Similar identifier class for general purposes
- Asset management and identification in Cascadeur