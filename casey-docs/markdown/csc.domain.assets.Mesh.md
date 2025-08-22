[CLEAN]

# csc.domain.assets.Mesh

**Module:** `csc.domain.assets.Mesh`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.domain.assets.Mesh.html)

## Overview

The `Mesh` class represents the properties and geometric data of a 3D mesh asset within the Cascadeur domain system. It provides the basic structure for defining object appearance through vertices, triangles, quads, normals, and texture coordinates, serving as the fundamental building block for 3D geometry in scenes.

## Class Definition

```python
class csc.domain.assets.Mesh
```

The Mesh class encapsulates all geometric data required to define a 3D mesh, including vertex positions, face connectivity, surface normals, and texture mapping coordinates.

## Constructor

### `__init__(self)`

Initializes a new Mesh instance with empty geometric data.

## Methods

### `figure_vertices_count(self) -> int`

Returns the total number of vertices in the mesh.

**Returns:**
- int: The count of vertices in the mesh

### `normals(self) -> Vector4f[]`

Retrieves the surface normal vectors for the mesh vertices.

**Returns:**
- Vector4f[]: Array of 4D vector normals for lighting and rendering calculations

### `quads(self) -> Quad[]`

Gets the quadrilateral faces that compose the mesh.

**Returns:**
- Quad[]: Array of quad face definitions

### `texture_coords(self) -> Vector2f[]`

Retrieves the texture coordinate mapping for the mesh vertices.

**Returns:**
- Vector2f[]: Array of 2D texture coordinates for UV mapping

### `triangles(self) -> Triangle[]`

Gets the triangular faces that compose the mesh.

**Returns:**
- Triangle[]: Array of triangle face definitions

### `vertices(self) -> Vector4f[]`

Retrieves the vertex positions that define the mesh geometry.

**Returns:**
- Vector4f[]: Array of 4D vertex position vectors

## Attributes

### `id -> int`

Unique identifier for the mesh asset.

**Type:** int

## Usage Example

```python
import csc.domain.assets

# Create a new mesh
mesh = csc.domain.assets.Mesh()

# Get mesh geometric data
vertex_count = mesh.figure_vertices_count()
print(f"Mesh has {vertex_count} vertices")

# Access geometric components
vertices = mesh.vertices()
triangles = mesh.triangles()
normals = mesh.normals()
texture_coords = mesh.texture_coords()

# Process vertex data
if vertices:
    print(f"First vertex position: {vertices[0]}")
    
# Process face data
if triangles:
    print(f"Triangle count: {len(triangles)}")
    
if mesh.quads():
    print(f"Quad count: {len(mesh.quads())}")

# Access texture mapping
if texture_coords:
    print(f"Texture coordinate count: {len(texture_coords)}")

# Mesh analysis workflow
def analyze_mesh(mesh):
    """Analyze mesh properties and structure."""
    analysis = {
        'vertex_count': mesh.figure_vertices_count(),
        'triangle_count': len(mesh.triangles()),
        'quad_count': len(mesh.quads()),
        'has_normals': len(mesh.normals()) > 0,
        'has_texture_coords': len(mesh.texture_coords()) > 0,
        'mesh_id': mesh.id
    }
    
    return analysis

# Use with AssetManager
assets_manager = csc.domain.assets.AssetsManager()

# Get primitive meshes
cube_mesh = assets_manager.get_cube_mesh()
plane_mesh = assets_manager.get_plane_mesh()

# Analyze the meshes
cube_analysis = analyze_mesh(cube_mesh)
plane_analysis = analyze_mesh(plane_mesh)

print("Cube mesh analysis:", cube_analysis)
print("Plane mesh analysis:", plane_analysis)
```

## Usage Notes

- The Mesh class provides read-only access to geometric data components
- Vertices are stored as 4D vectors (homogeneous coordinates) for transformation calculations
- Both triangular and quadrilateral faces are supported for flexible mesh representation
- Normal vectors are essential for proper lighting and surface rendering
- Texture coordinates enable UV mapping for material application
- The mesh ID provides unique identification within the asset management system
- Vertex count method offers quick access to mesh complexity information
- All geometric data arrays should be checked for existence before processing

## See Also

- `csc.domain.assets.AssetsManager` - Asset management and mesh creation
- `csc.domain.assets.Triangle` - Triangle face representation
- `csc.domain.assets.FigureVertex` - Vertex data structures
- `csc.domain.assets.MeshDependency` - Mesh dependency relationships
- `csc.domain.Asset` - Base asset functionality