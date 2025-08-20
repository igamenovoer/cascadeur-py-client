"""
Custom exceptions for the Cascadeur client.
"""


class CascadeurError(Exception):
    """Base exception for Cascadeur-related errors."""
    pass


class ConnectionError(CascadeurError):
    """Raised when unable to connect to Cascadeur."""
    pass


class SceneError(CascadeurError):
    """Raised for scene-related errors."""
    pass


class RigError(CascadeurError):
    """Raised for rig-related errors."""
    pass


class AnimationError(CascadeurError):
    """Raised for animation-related errors."""
    pass


class APIError(CascadeurError):
    """Raised for general API errors."""
    pass
