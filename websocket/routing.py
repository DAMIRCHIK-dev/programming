from django.urls import re_path
from .consumers import InventoryConsumer, MealLogConsumer

websocket_urlpatterns = [
    re_path(r"ws/inventory/$", InventoryConsumer.as_asgi()),
    re_path(r"ws/meal-log/$", MealLogConsumer.as_asgi()),   # ← yangi yo‘l
]
