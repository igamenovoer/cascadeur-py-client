# Cascadeur Python Client Documentation

Welcome to the Cascadeur Python Client documentation!

## Quick Start

`python
import cascadeur_client as csc

# Connect to Cascadeur
client = csc.CascadeurClient()

# Create a new scene
scene = client.create_scene()

# Create and manipulate joints
joint = scene.create_joint("my_joint", (0, 0, 0))
joint.move_to(10, 20, 30)

# Save the scene
scene.save("my_scene.casc")
`

## API Reference

### CascadeurClient

Main client class for connecting to Cascadeur.

### Scene

Represents a Cascadeur scene with animation data.

### Rig Elements

- **Joint**: Character rig joints
- **PointController**: Point controllers for animation
- **BoxController**: Box controllers for physics simulation

### Animation

- **AnimationLayer**: Animation tracks/layers
- **Keyframe**: Individual keyframes
- **Timeline**: Timeline management

## Examples

See the xamples/ directory for complete usage examples:

- asic_usage.py: Basic scene manipulation
- nimation_example.py: Working with animation layers

## Installation

`ash
pip install cascadeur-py-client
`

## Requirements

- Python 3.7+
- Cascadeur 2022.1+ with Python API support
