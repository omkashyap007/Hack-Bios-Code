from django.shortcuts import render
from django.http import HttpResponse
import time

def homePage(request , *args , **kwargs) :
    context = {"command" : 1}
    return render(request , "base/switchBoard.html" , context = context)    
