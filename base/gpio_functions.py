from channels.db import database_sync_to_async
import RPi.GPIO as gp
import time
@database_sync_to_async
def changePinStatus(button_number , state_change_value):
    print("The function was run and command was sent to change state !")
    print(f"The button number is : {button_number} ")
    print(f"The state change value : {state_change_value}")
    try :
        print(f"The state change value is : {state_change_value}")
        if state_change_value:
            gp.output(button_number, gp.HIGH)
            print("HIGH Signal Sent")
        else:
            gp.output(button_number, gp.LOW)
            print("Low Signal Sent")   
        signal_sent = True
    except Exception as e:
        print(e)
        signal_sent = False
    return signal_sent