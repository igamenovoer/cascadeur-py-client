"""
Example: Basic scene manipulation with Cascadeur Python Client.
"""

import cascadeur_client as csc


def main():
    """Demonstrate basic usage of the Cascadeur Python Client."""
    
    # Create a client and connect to Cascadeur
    print("Connecting to Cascadeur...")
    client = csc.CascadeurClient()
    client.connect()
    
    # Create a new scene
    print("Creating new scene...")
    scene = client.create_scene()
    
    # Get scene information
    info = scene.get_scene_info()
    print(f"Scene info: {info}")
    
    # Create some joints
    print("Creating joints...")
    root_joint = scene.create_joint("root", (0, 0, 0))
    spine_joint = scene.create_joint("spine", (0, 10, 0))
    head_joint = scene.create_joint("head", (0, 20, 0))
    
    # Set up joint hierarchy
    root_joint.add_child(spine_joint)
    spine_joint.add_child(head_joint)
    
    # Move joints
    print("Moving joints...")
    root_joint.move_to(0, 0, 0)
    spine_joint.move_to(0, 10, 0)
    head_joint.move_to(0, 20, 0)
    
    # Work with timeline
    print("Setting up timeline...")
    scene.set_current_frame(1)
    
    # Get all joints
    joints = scene.get_joints()
    print(f"Total joints in scene: {len(joints)}")
    
    # Save the scene
    print("Saving scene...")
    scene.save("example_scene.casc")
    
    print("Example completed!")


if __name__ == "__main__":
    main()
