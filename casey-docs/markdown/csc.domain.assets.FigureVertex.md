[CLEAN]

# csc.domain.assets.FigureVertex

**Module:** `csc.domain.assets.FigureVertex`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.assets.FigureVertex.html)

## Overview

The `FigureVertex` class represents a vertex within a figure asset, providing essential indexing properties for mesh topology and control systems. It implements the fundamental vertex properties required for 3D geometry representation, including both geometric indexing and control point management within the asset pipeline.

## Class Definition

```python
class csc.domain.assets.FigureVertex
```

The FigureVertex class encapsulates vertex identification and control data for figure-based mesh assets.

## Constructor

### `__init__(*args, **kwargs)`

Initializes a new FigureVertex instance.

**Parameters:**
- `*args`: Variable length argument list
- `**kwargs`: Arbitrary keyword arguments

## Attributes

### `index -> int`

The geometric index of the vertex within the figure mesh.

**Type:** int  
**Access:** Read-only

### `control_index -> int`

The control system index for the vertex, used in rigging and deformation operations.

**Type:** int  
**Access:** Read-only

## Usage Example

```python
import csc.domain.assets

# Access figure vertex properties
def analyze_figure_vertices(figure_vertices):
    """Analyze figure vertex properties and indexing."""
    vertex_data = []
    
    for vertex in figure_vertices:
        vertex_info = {
            'geometric_index': vertex.index,
            'control_index': vertex.control_index,
            'has_control': vertex.control_index >= 0
        }
        vertex_data.append(vertex_info)
    
    return vertex_data

# Working with figure mesh vertices
def process_mesh_vertices(mesh):
    """Process vertices in a figure mesh."""
    if hasattr(mesh, 'vertices'):
        vertices = mesh.vertices()
        
        # Analyze vertex indices
        for i, vertex in enumerate(vertices):
            if hasattr(vertex, 'index') and hasattr(vertex, 'control_index'):
                print(f"Vertex {i}: geometric={vertex.index}, control={vertex.control_index}")

# Vertex indexing and mapping
def create_vertex_mapping(figure_vertices):
    """Create mapping between geometric and control indices."""
    geometric_to_control = {}
    control_to_geometric = {}
    
    for vertex in figure_vertices:
        geo_idx = vertex.index
        ctrl_idx = vertex.control_index
        
        geometric_to_control[geo_idx] = ctrl_idx
        if ctrl_idx >= 0:  # Valid control index
            control_to_geometric[ctrl_idx] = geo_idx
    
    return geometric_to_control, control_to_geometric

# Integration with asset management
def analyze_figure_asset(asset_manager, asset_id):
    """Analyze figure asset vertex structure."""
    try:
        asset = asset_manager.at(asset_id)
        
        if hasattr(asset, 'vertices'):
            vertices = asset.vertices()
            vertex_analysis = analyze_figure_vertices(vertices)
            
            # Statistics
            total_vertices = len(vertex_analysis)
            controlled_vertices = sum(1 for v in vertex_analysis if v['has_control'])
            
            return {
                'total_vertices': total_vertices,
                'controlled_vertices': controlled_vertices,
                'control_ratio': controlled_vertices / total_vertices if total_vertices > 0 else 0,
                'vertex_details': vertex_analysis
            }
    except Exception as e:
        print(f"Error analyzing figure asset: {e}")
        return None
```

## Usage Notes

- FigureVertex provides dual indexing for geometric and control system operations
- The `index` attribute refers to the vertex position in the geometric mesh structure
- The `control_index` links vertices to rigging and deformation control systems
- Control indices may be -1 or invalid for vertices not participating in control systems
- Essential for mapping between mesh topology and animation/rigging systems
- Used in conjunction with mesh processing and asset management workflows
- Both indices are read-only properties determined during asset creation

## See Also

- `csc.domain.assets.Mesh` - Mesh asset containing figure vertices
- `csc.domain.assets.Triangle` - Triangle face definitions using vertex indices
- `csc.domain.assets.AssetsManager` - Asset management for figure-based meshes
- `csc.domain.assets.MeshDependency` - Mesh dependency relationships involving vertices
- Rigging and deformation systems that utilize control indices