from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .gpio_functions import *

class BaseConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        print("Accepted the connection ")
        await self.accept()

    async def receive_json(self , content , *args , **kwargs):
        print(f"This is content : {content}")

        command = content.get("command")
        if command == "change_switch_status" : 
            button_number = content.get("button_number")
            print(f"This is button number: {button_number}")
            state_change_value = content.get("state_change_value")
            print(f"This is change state value : {state_change_value}")
            state_changed = await changePinStatus(button_number , state_change_value)
            if state_changed : 
                await self.sendMessage(
                    {
                        "state_changed" : True ,
                        "button_number" : button_number , 
                    }
                )
            else :
                await self.sendMessage(
                    {
                        "state_changed" : False,
                        "button_number" : button_number , 
                    }
                )


    async def sendMessage(self, message) :
        await self.send_json(          
            message 
        )
            

    async def disconnect(self ,  close_code):
        await self.close()

