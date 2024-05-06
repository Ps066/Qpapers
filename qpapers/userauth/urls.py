from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "userauth"

urlpatterns = [
    path('sign-in/', login_view, name="login"),
    path('sign-up/', register_view, name="register"),
    
]
