from django.urls import path
from .views import *

urlpatterns = [

    path("", dashboard, name="dashboard"),
    path("challenge/", challenge, name="challenge"),
    path("users/", users, name="user")
]
