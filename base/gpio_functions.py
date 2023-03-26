from channels.db import database_sync_to_async
import RPi.GPIO as gp
import switches as s
import time
@database_sync_to_async
def changePinStatus(button_number , state_change_value):
    print("The function was run and command was sent to change state !")
    try :
        print(state_change_value)
        if state_change_value:
            gp.output(button_number, gp.HIGH)
            print("HIGH Signal Sent")
        else:
            gp.output(button_number, gp.LOW)
            print("Low Signal Sent")   
        signal_sent = True
    except : 
        signal_sent = False
    return signal_sent