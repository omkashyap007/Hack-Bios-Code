from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .gpio_functions import *

@api_view(["POST"])
def changeDeviceState(request , *args ,**kwargs):
    response = {
        "data" : None , 
        "errors" : None , 
        "success" : False , 
    }
    button_number = request.POST.get("button_number")
    state_change_value = request.POST.get("state_chanage_value")
    
    state_changed = toggleDevice(switch , relay)
    if state_changed : 
        response["success"] = True
        response["data"] = f"Changed : {switch} : {relay}"
        return Response(
            response , 
        )
    else : 
        return Response(
            response , 
        )
