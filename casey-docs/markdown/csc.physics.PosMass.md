[CLEAN]

# csc.physics.PosMass

**Module:** `csc.physics.PosMass`  
**Source:** [Cascadeur Python API Documentation](https://cascadeur.com/python-api/_generate/csc.physics.PosMass.html)

## Overview

The `PosMass` class represents a fundamental physics entity that combines mass and spatial position information. This structure is essential for physics calculations, dynamics simulations, and center-of-mass computations within the Cascadeur physics system, providing the basic building block for mass distribution analysis and physical behavior modeling.

## Class Definition

```python
class csc.physics.PosMass
```

The PosMass class encapsulates mass and position data for physics calculations and center-of-mass operations.

## Constructor

### `__init__(self, mass: float, position: Vector3f)`

Initializes a PosMass instance with specified mass and position values.

**Parameters:**
- `mass` (float): The mass value of the physics point
- `position` (Vector3f): The 3D position vector of the mass point

## Attributes

### `mass -> float`

The mass value of the physics point.

**Type:** float  
**Access:** Read/Write

### `position -> Vector3f`

The 3D position vector of the mass point.

**Type:** Vector3f  
**Access:** Read/Write

## Usage Example

```python
import csc.physics

# Create a mass point at a specific location
mass_value = 2.5
position_vector = [1.0, 2.0, 3.0]  # or appropriate Vector3f object

mass_point = csc.physics.PosMass(mass_value, position_vector)

# Access and modify mass
print(f"Mass: {mass_point.mass}")
mass_point.mass = 3.0

# Access and modify position
print(f"Position: {mass_point.position}")
mass_point.position = [2.0, 3.0, 4.0]

# Physics calculations with multiple mass points
def calculate_center_of_mass(mass_points):
    """Calculate the center of mass from multiple PosMass objects."""
    total_mass = 0.0
    weighted_position = [0.0, 0.0, 0.0]
    
    for point in mass_points:
        total_mass += point.mass
        # Assuming position supports component access
        weighted_position[0] += point.mass * point.position[0]
        weighted_position[1] += point.mass * point.position[1]
        weighted_position[2] += point.mass * point.position[2]
    
    if total_mass > 0:
        center_of_mass = [
            weighted_position[0] / total_mass,
            weighted_position[1] / total_mass,
            weighted_position[2] / total_mass
        ]
        return center_of_mass
    else:
        return [0.0, 0.0, 0.0]

# Working with mass distribution
mass_points = [
    csc.physics.PosMass(1.0, [0.0, 0.0, 0.0]),
    csc.physics.PosMass(2.0, [1.0, 0.0, 0.0]),
    csc.physics.PosMass(1.5, [0.5, 1.0, 0.0])
]

# Calculate center of mass
center = calculate_center_of_mass(mass_points)
print(f"Center of mass: {center}")

# Physics simulation setup
def setup_physics_body(masses, positions):
    """Create a physics body from mass and position data."""
    mass_points = []
    
    for mass, pos in zip(masses, positions):
        point = csc.physics.PosMass(mass, pos)
        mass_points.append(point)
    
    return mass_points

# Example: Character physics setup
bone_masses = [0.5, 1.0, 0.8, 0.3, 0.3]  # Head, torso, arms, etc.
bone_positions = [
    [0.0, 1.8, 0.0],  # Head
    [0.0, 1.2, 0.0],  # Torso
    [-0.6, 1.2, 0.0], # Left arm
    [0.6, 1.2, 0.0],  # Right arm
    [0.0, 0.6, 0.0]   # Lower body
]

character_physics = setup_physics_body(bone_masses, bone_positions)
character_center = calculate_center_of_mass(character_physics)
```

## Usage Notes

- PosMass serves as a fundamental data structure for physics calculations
- The mass attribute affects the influence of this point in center-of-mass calculations
- Position coordinates are typically in world space or local object coordinates
- Essential for physics simulations, balance calculations, and dynamics analysis
- Both mass and position can be modified after creation for dynamic simulations
- Commonly used in arrays or collections for multi-point physics calculations
- Important for center-of-mass computations in animation and character balance

## See Also

- `csc.physics.inertia_tensor` - Inertia tensor calculations for rotational dynamics
- Physics simulation and dynamics systems
- Mass distribution analysis tools
- Center-of-mass calculation utilities
- Character balance and physics workflows