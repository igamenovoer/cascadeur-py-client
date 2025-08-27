# Cascadeur Python Client

A pythonic client API to interface with [Cascadeur](https://cascadeur.com/) animation software.

## Overview

Cascadeur is a physics-based animation software that allows animators to create realistic character animations. This Python client library provides a high-level, pythonic interface to interact with Cascadeur's Python API, making it easier to automate animation workflows, create custom tools, and integrate Cascadeur into larger pipelines.

## Features

- **High-level API**: Simplified, pythonic interface over Cascadeur's native Python API
- **Scene Management**: Easy scene creation, loading, and manipulation
- **Animation Tools**: Programmatic access to Cascadeur's animation tools
- **Rig Management**: Create and modify character rigs
- **Asset Management**: Handle mesh data and assets
- **Node Editor Integration**: Work with Cascadeur's node-based update system

## Installation

`ash
pip install cascadeur-py-client
`

## Quick Start

`python
import cascadeur_py_client as csc

# Connect to Cascadeur
client = csc.CascadeurClient()

# Load a scene
scene = client.load_scene("path/to/scene.casc")

# Get all joints in the scene
joints = scene.get_joints()

# Move a joint
joint = joints[0]
joint.move_to(x=10, y=20, z=30)

# Save the scene
scene.save("path/to/modified_scene.casc")
`

## Requirements

- Python 3.7+
- Cascadeur 2022.1+ (with Python API support)

## Documentation

Full documentation is available at [Read the Docs](https://cascadeur-py-client.readthedocs.io/) (coming soon).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Cascadeur](https://cascadeur.com/) by Nekki - The amazing physics-based animation software
- The Cascadeur development team for providing the Python API

## Related Links

- [Cascadeur Official Website](https://cascadeur.com/)
- [Cascadeur Python API Documentation](https://cascadeur.com/help/category/215)
- [Cascadeur Community](https://cascadeur.com/community)

## Disclaimer

This is an unofficial client library. It is not affiliated with or endorsed by Nekki or the Cascadeur development team.
