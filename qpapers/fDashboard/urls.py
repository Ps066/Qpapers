from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "fdash"

urlpatterns = [
    path('user/', dash_view, name="index")
]
