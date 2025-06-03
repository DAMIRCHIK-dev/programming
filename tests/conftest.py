# tests/conftest.py
import pytest
from django.conf import settings

@pytest.fixture(autouse=True, scope="session")
def _patch_channel_layer_settings():
    """
    Testlarda Redis talab qilmaslik uchun InMemoryChannelLayer ishlatamiz.
    """
    settings.CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer",
        }
    }
