# tests/test_websocket.py
import pytest
from channels.testing import WebsocketCommunicator
from config.asgi import application

@pytest.mark.asyncio
async def test_inventory_ws_connect():
    """WebSocket /ws/inventory/ successful handshake."""
    communicator = WebsocketCommunicator(application, "/ws/inventory/")
    connected, _ = await communicator.connect()
    assert connected
    await communicator.disconnect()
