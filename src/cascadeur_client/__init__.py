"""
Cascadeur Python Client

A pythonic client API to interface with Cascadeur animation software.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
__license__ = "MIT"

from .client import CascadeurClient
from .scene import Scene
from .exceptions import CascadeurError, ConnectionError, SceneError

__all__ = [
    "CascadeurClient",
    "Scene", 
    "CascadeurError",
    "ConnectionError",
    "SceneError",
]
