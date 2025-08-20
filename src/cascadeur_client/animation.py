"""
Animation and timeline management.
"""

import logging
from typing import List, Dict, Any, Optional, Union


logger = logging.getLogger(__name__)


class Keyframe:
    """Represents a single keyframe."""
    
    def __init__(self, frame: int, value: Any, interpolation: str = "linear"):
        """
        Initialize a keyframe.
        
        Args:
            frame: Frame number
            value: Keyframe value
            interpolation: Interpolation type
        """
        self.frame = frame
        self.value = value
        self.interpolation = interpolation
        
    def __str__(self):
        return f"Keyframe(frame={self.frame}, value={self.value})"


class AnimationLayer:
    """
    Represents an animation layer (track) in Cascadeur.
    
    In Cascadeur's API, these are called Layers but represent
    what users see as Animation Tracks in the Timeline.
    """
    
    def __init__(self, name: str, layer_type: str = "transform"):
        """
        Initialize an animation layer.
        
        Args:
            name: Name of the layer
            layer_type: Type of layer (transform, behavior, etc.)
        """
        self.name = name
        self.type = layer_type
        self.keyframes = {}  # Dict of property_name -> List[Keyframe]
        self.enabled = True
        self.locked = False
        
    def add_keyframe(self, property_name: str, frame: int, value: Any) -> None:
        """
        Add a keyframe for a property.
        
        Args:
            property_name: Name of the animated property
            frame: Frame number
            value: Keyframe value
        """
        if property_name not in self.keyframes:
            self.keyframes[property_name] = []
            
        # Remove existing keyframe at same frame if it exists
        self.keyframes[property_name] = [kf for kf in self.keyframes[property_name] if kf.frame != frame]
        
        # Add new keyframe
        keyframe = Keyframe(frame, value)
        self.keyframes[property_name].append(keyframe)
        self.keyframes[property_name].sort(key=lambda kf: kf.frame)
        
        logger.info(f"Added keyframe to layer '{self.name}': {property_name} = {value} at frame {frame}")
        
    def remove_keyframe(self, property_name: str, frame: int) -> None:
        """
        Remove a keyframe.
        
        Args:
            property_name: Name of the animated property
            frame: Frame number
        """
        if property_name in self.keyframes:
            self.keyframes[property_name] = [kf for kf in self.keyframes[property_name] if kf.frame != frame]
            logger.info(f"Removed keyframe from layer '{self.name}': {property_name} at frame {frame}")
            
    def get_keyframes(self, property_name: str) -> List[Keyframe]:
        """
        Get all keyframes for a property.
        
        Args:
            property_name: Name of the animated property
            
        Returns:
            List of keyframes
        """
        return self.keyframes.get(property_name, [])
        
    def get_value_at_frame(self, property_name: str, frame: int) -> Any:
        """
        Get interpolated value at a specific frame.
        
        Args:
            property_name: Name of the animated property
            frame: Frame number
            
        Returns:
            Interpolated value
        """
        keyframes = self.get_keyframes(property_name)
        if not keyframes:
            return None
            
        # Find surrounding keyframes
        before = None
        after = None
        
        for kf in keyframes:
            if kf.frame <= frame:
                before = kf
            if kf.frame >= frame and after is None:
                after = kf
                break
                
        if before is None:
            return after.value if after else None
        if after is None:
            return before.value
        if before.frame == after.frame:
            return before.value
            
        # Simple linear interpolation (placeholder)
        t = (frame - before.frame) / (after.frame - before.frame)
        if isinstance(before.value, (int, float)) and isinstance(after.value, (int, float)):
            return before.value + t * (after.value - before.value)
        else:
            return before.value  # For non-numeric values, just return the before value


class Timeline:
    """Manages the timeline and animation playback."""
    
    def __init__(self):
        """Initialize the timeline."""
        self.current_frame = 1
        self.start_frame = 1
        self.end_frame = 120
        self.fps = 24
        self.playing = False
        
    def set_frame_range(self, start: int, end: int) -> None:
        """
        Set the frame range.
        
        Args:
            start: Start frame
            end: End frame
        """
        self.start_frame = start
        self.end_frame = end
        logger.info(f"Set frame range: {start} - {end}")
        
    def goto_frame(self, frame: int) -> None:
        """
        Go to a specific frame.
        
        Args:
            frame: Frame number
        """
        self.current_frame = max(self.start_frame, min(frame, self.end_frame))
        logger.info(f"Current frame: {self.current_frame}")
        
    def play(self) -> None:
        """Start playback."""
        self.playing = True
        logger.info("Started playback")
        
    def stop(self) -> None:
        """Stop playback."""
        self.playing = False
        logger.info("Stopped playback")
        
    def next_frame(self) -> None:
        """Go to next frame."""
        if self.current_frame < self.end_frame:
            self.current_frame += 1
            
    def previous_frame(self) -> None:
        """Go to previous frame."""
        if self.current_frame > self.start_frame:
            self.current_frame -= 1
