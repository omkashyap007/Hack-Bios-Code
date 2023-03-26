
import time
import requests
import switches as sw
import RPi.GPIO as gp

gp.setmode(gp.BOARD)

gp.setup(sw.SWITCH_1, gp.IN)	# switch 1
gp.setup(sw.SWITCH_2, gp.IN)	# switch 2
# 
# gp.setup(sw.RELAY_1, gp.OUT)	# relay 1


def toggleRelay(switch, relay):
    """It will simply toggle the relay on or off """
    gp.setup(relay, gp.OUT)
    relay_state=gp.input(relay)
#     gp.output(relay, int(not relay_state))
    print("off" if relay_state==1 else "on")
    response = requests.get('http://localhost:8080/api/change-device-state/' ,
        params = {"button_number" : int(relay) , "state_change_value": int(not relay_state)})
    print(response)
    
# these last states will also be fetched from db
SWITCH_1_LAST =gp.input(sw.SWITCH_1) 
SWITCH_2_LAST =gp.input(sw.SWITCH_2) 


try:
    while True : 
        if gp.input(sw.SWITCH_1) != SWITCH_1_LAST:
            if gp.input(sw.SWITCH_1) == 1:
                toggleRelay(sw.SWITCH_1, sw.RELAY_1)
            SWITCH_1_LAST = abs(1-SWITCH_1_LAST)
        
        if gp.input(sw.SWITCH_2) == SWITCH_2_LAST:
            if gp.input(sw.SWITCH_2) == 1:
                toggleRelay(sw.SWITCH_2, sw.RELAY_2)
            SWITCH_2_LAST = abs(1-SWITCH_2_LAST)
    
    
finally:
    gp.cleanup()
    print("CleanUp Complete")