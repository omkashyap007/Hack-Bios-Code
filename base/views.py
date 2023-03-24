from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as gp
import time
gp.setwarnings(False)
gp.setmode(gp.BOARD)
gp.setup(5 , gp.OUT)
    
def homePage(request , *args , **kwargs) :
    command = int(request.GET.get("command"))
    if command == 1 :
        gp.output(5 , gp.HIGH)
        time.sleep(5)
        gp.output(5 , gp.LOW)
    return HttpResponse(f"The command is : {command} ")
    
    
