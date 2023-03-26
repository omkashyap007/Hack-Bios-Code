from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .gpio_functions import *
from .async_functions import *

@api_view(["POST"])
def changeDeviceState(request , *args ,**kwargs):
    response = {
        "data" : None , 
        "errors" : None , 
        "success" : False , 
    }
    button_number = int(request.POST.get("button_number"))
    state_change_value = int(request.POST.get("state_change_value"))
    print(f"The value of button number is : {button_number}")
    print(f"The value of state change value is : {state_change_value}")
    state_changed = changePinStatus(button_number , state_change_value)
    if state_changed : 
        response["success"] = True
        response["data"] = f"Changed : {button_number} : {state_change_value}"
        return Response(
            response , 
        )
    else : 
        return Response(
            response , 
        )