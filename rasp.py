import requests
import RPi.GPIO as gp
gp.setmode(gp.BOARD)

gp.setup(5 , gp.OUT)
gp.setup(3 , gp.IN)
PIN_THREE = gp.input(3)

while True :
    command = gp.input(3)
    if command != PIN_THREE :
        print(f"The value of the pin 3 has changed")
        response = requests.get('http://localhost:8080/' , params = {"command" : abs(1-command)})
        print(response)
        PIN_THREE = command