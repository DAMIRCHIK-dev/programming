import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from websocket.routing import websocket_urlpatterns  # sizning routing.py

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Django’ning http so‘rovlari
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
