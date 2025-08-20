"""
Example: Working with animation layers and keyframes.
"""

import cascadeur_client as csc


def main():
    """Demonstrate animation features."""
    
    # Connect and create scene
    client = csc.CascadeurClient()
    client.connect()
    scene = client.create_scene()
    
    # Create a joint
    joint = scene.create_joint("animated_joint", (0, 0, 0))
    
    # Get animation layers
    layers = scene.get_animation_layers()
    
    # Create a new animation layer if none exist
    if not layers:
        from cascadeur_client.animation import AnimationLayer
        layer = AnimationLayer("transform_layer")
        layers = [layer]
    else:
        layer = layers[0]
    
    # Add keyframes for position animation
    print("Adding keyframes...")
    
    # Keyframe at frame 1: joint at origin
    layer.add_keyframe("position_x", 1, 0.0)
    layer.add_keyframe("position_y", 1, 0.0)
    layer.add_keyframe("position_z", 1, 0.0)
    
    # Keyframe at frame 30: joint moved
    layer.add_keyframe("position_x", 30, 10.0)
    layer.add_keyframe("position_y", 30, 5.0)
    layer.add_keyframe("position_z", 30, 0.0)
    
    # Keyframe at frame 60: joint moved again
    layer.add_keyframe("position_x", 60, 0.0)
    layer.add_keyframe("position_y", 60, 10.0)
    layer.add_keyframe("position_z", 60, 5.0)
    
    # Check interpolated values
    print("Checking interpolated values...")
    for frame in [1, 15, 30, 45, 60]:
        x = layer.get_value_at_frame("position_x", frame)
        y = layer.get_value_at_frame("position_y", frame)
        z = layer.get_value_at_frame("position_z", frame)
        print(f"Frame {frame}: position = ({x}, {y}, {z})")
    
    # Work with timeline
    from cascadeur_client.animation import Timeline
    timeline = Timeline()
    timeline.set_frame_range(1, 60)
    timeline.goto_frame(30)
    
    print(f"Current frame: {timeline.current_frame}")
    
    print("Animation example completed!")


if __name__ == "__main__":
    main()
