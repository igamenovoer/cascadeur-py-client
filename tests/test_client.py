"""
Basic tests for the Cascadeur client.
"""

import pytest
from cascadeur_client import CascadeurClient, Scene
from cascadeur_client.exceptions import ConnectionError, SceneError


class TestCascadeurClient:
    """Test the main client class."""
    
    def test_client_creation(self):
        """Test creating a client instance."""
        client = CascadeurClient()
        assert client is not None
        assert not client.is_connected()
        
    def test_client_connection(self):
        """Test connecting to Cascadeur."""
        client = CascadeurClient()
        client.connect()
        assert client.is_connected()
        
    def test_client_disconnection(self):
        """Test disconnecting from Cascadeur."""
        client = CascadeurClient()
        client.connect()
        client.disconnect()
        assert not client.is_connected()
        
    def test_create_scene(self):
        """Test creating a new scene."""
        client = CascadeurClient()
        scene = client.create_scene()
        assert isinstance(scene, Scene)


class TestScene:
    """Test the Scene class."""
    
    def test_scene_creation(self):
        """Test creating a scene."""
        client = CascadeurClient()
        scene = Scene(client)
        assert scene.client == client
        
    def test_scene_info(self):
        """Test getting scene information."""
        client = CascadeurClient()
        scene = Scene(client)
        info = scene.get_scene_info()
        assert isinstance(info, dict)
        assert "frame_count" in info
        assert "current_frame" in info
        
    def test_frame_operations(self):
        """Test frame-related operations."""
        client = CascadeurClient()
        scene = Scene(client)
        
        # Test getting frame count
        frame_count = scene.get_frame_count()
        assert isinstance(frame_count, int)
        assert frame_count > 0
        
        # Test current frame
        current_frame = scene.get_current_frame()
        assert isinstance(current_frame, int)
        
        # Test setting frame
        scene.set_current_frame(10)
        # Note: In a real implementation, this would actually change the frame


if __name__ == "__main__":
    pytest.main([__file__])
