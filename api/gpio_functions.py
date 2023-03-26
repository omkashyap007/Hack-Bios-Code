from channels.db import database_sync_to_async
import RPi.GPIO as gp
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time

def toggleDevice(switch , relay):
    
    print("Toggle functions started")
    try :
        relay_state=gp.input(relay)
        gp.output(relay, int(not relay_state))
        print("off" if relay_state==1 else "on")
        return True
    except Exception as e: 
        print(e)
        return False
