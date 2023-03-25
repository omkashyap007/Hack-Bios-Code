from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as gp
gp.setmode(gp.BOARD)
gp.setup(5 , gp.OUT)
gp.setwarnings(False)
import time
def homePage(request , *args , **kwargs) :
    command = int(request.GET.get("command"))
    if command == 1 :
        gp.output(5 , gp.HIGH)
        time.sleep(1)
        gp.output(5 , gp.LOW)
    if command == 0 :
        print(f"This is the command for zero ")
    return HttpResponse(f"The command is : {command} ")
    
    
