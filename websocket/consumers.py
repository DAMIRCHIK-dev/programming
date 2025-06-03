from channels.generic.websocket import AsyncWebsocketConsumer
import json

class InventoryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("inventory", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard("inventory", self.channel_name)

    async def inventory_update(self, event):
        await self.send(text_data=json.dumps({
            "type": "update",
            "message": event["message"],
        }))

# ─── Yangi: MealLogConsumer ────────────────────────────────────────────
class MealLogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("meal_log", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard("meal_log", self.channel_name)

    async def meal_update(self, event):
        # serverdan {"type":"meal_update","message":{…}} keladi
        await self.send(text_data=json.dumps({
            "type": "meal",
            "message": event["message"],
        }))
