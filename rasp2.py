import requests
import RPi.GPIO as gp
gp.setmode(gp.BOARD)
SWITCH_1, SWITCH_2 = 3, 5
RELAY_1, RELAY_2 = 40, 38

gp.setup(SWITCH_1, gp.IN)	# switch 1
gp.setup(SWITCH_2, gp.IN)	# switch 2

gp.setup(RELAY_1, gp.OUT)	# relay 1
gp.setup(RELAY_1, gp.OUT)	#relay 2

OLD_SWITCH_1_VAL = gp.input(SWITCH_1)
OLD_SWITCH_2_VAL = gp.input(SWITCH_2)
try:
    while True :
        NEW_SWITCH_1_VAL = gp.input(SWITCH_1)
        NEW_SWITCH_2_VAL = gp.input(SWITCH_2)
        
        if NEW_SWITCH_1_VAL
    #     if command != PIN_THREE :
    #         print(f"The value of the pin 3 has changed")
    #         response = requests.get('http://localhost:8080/' , params = {"command" : abs(1-command)})
    #         print(response)
    #         PIN_THREE = command
    
finally:
    gp.cleanup()