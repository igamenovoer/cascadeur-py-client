"""
Rig elements: joints, controllers, and other rig components.
"""

import logging
from typing import Tuple, Optional, Dict, Any


logger = logging.getLogger(__name__)


class RigElement:
    """Base class for rig elements."""
    
    def __init__(self, name: str, element_id: Optional[str] = None):
        """
        Initialize a rig element.
        
        Args:
            name: Name of the element
            element_id: Unique identifier for the element
        """
        self.name = name
        self.id = element_id or name
        self._position = (0.0, 0.0, 0.0)
        self._rotation = (0.0, 0.0, 0.0)
        
    def get_position(self) -> Tuple[float, float, float]:
        """Get the position of the element."""
        return self._position
    
    def set_position(self, x: float, y: float, z: float) -> None:
        """Set the position of the element."""
        self._position = (x, y, z)
        logger.info(f"Set position of {self.name} to ({x}, {y}, {z})")
    
    def move_to(self, x: float, y: float, z: float) -> None:
        """Move the element to a specific position."""
        self.set_position(x, y, z)
    
    def get_rotation(self) -> Tuple[float, float, float]:
        """Get the rotation of the element."""
        return self._rotation
    
    def set_rotation(self, x: float, y: float, z: float) -> None:
        """Set the rotation of the element."""
        self._rotation = (x, y, z)
        logger.info(f"Set rotation of {self.name} to ({x}, {y}, {z})")


class Joint(RigElement):
    """Represents a joint in the character rig."""
    
    def __init__(self, name: str, position: Tuple[float, float, float] = (0, 0, 0)):
        """
        Initialize a joint.
        
        Args:
            name: Name of the joint
            position: Initial position as (x, y, z) tuple
        """
        super().__init__(name)
        self._position = position
        self.parent = None
        self.children = []
        
    def add_child(self, child: 'Joint') -> None:
        """Add a child joint."""
        if child not in self.children:
            self.children.append(child)
            child.parent = self
            
    def remove_child(self, child: 'Joint') -> None:
        """Remove a child joint."""
        if child in self.children:
            self.children.remove(child)
            child.parent = None
            
    def get_world_position(self) -> Tuple[float, float, float]:
        """Get the world position of the joint."""
        # Placeholder implementation - would calculate from parent chain
        return self._position


class PointController(RigElement):
    """Represents a point controller in the rig."""
    
    def __init__(self, name: str, controlled_joint: Optional[Joint] = None):
        """
        Initialize a point controller.
        
        Args:
            name: Name of the controller
            controlled_joint: Joint this controller affects
        """
        super().__init__(name)
        self.controlled_joint = controlled_joint
        
    def set_controlled_joint(self, joint: Joint) -> None:
        """Set the joint this controller affects."""
        self.controlled_joint = joint


class BoxController(RigElement):
    """Represents a box controller in the rig."""
    
    def __init__(self, name: str, size: Tuple[float, float, float] = (1, 1, 1)):
        """
        Initialize a box controller.
        
        Args:
            name: Name of the controller
            size: Size of the box as (width, height, depth) tuple
        """
        super().__init__(name)
        self._size = size
        
    def get_size(self) -> Tuple[float, float, float]:
        """Get the size of the box controller."""
        return self._size
    
    def set_size(self, width: float, height: float, depth: float) -> None:
        """Set the size of the box controller."""
        self._size = (width, height, depth)
        logger.info(f"Set size of {self.name} to ({width}, {height}, {depth})")


class Behavior:
    """Represents a behavior in the rig."""
    
    def __init__(self, name: str, behavior_type: str):
        """
        Initialize a behavior.
        
        Args:
            name: Name of the behavior
            behavior_type: Type of behavior
        """
        self.name = name
        self.type = behavior_type
        self.enabled = True
        self.parameters = {}
        
    def set_parameter(self, param_name: str, value: Any) -> None:
        """Set a behavior parameter."""
        self.parameters[param_name] = value
        logger.info(f"Set parameter '{param_name}' of behavior '{self.name}' to {value}")
        
    def get_parameter(self, param_name: str) -> Any:
        """Get a behavior parameter."""
        return self.parameters.get(param_name)
