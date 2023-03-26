from django.urls import path
from api import views as api_views

urlpatterns = [
    path("change-device-state/" , api_views.changeDeviceState , name = "change-device-state") , 
]
