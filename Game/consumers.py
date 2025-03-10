from channels.generic.websocket import AsyncWebsocketConsumer
import json 

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'Connected to WebSocket!'
        }))
