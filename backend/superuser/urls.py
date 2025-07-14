from django.urls import path
from .views import *

urlpatterns = [

    path("", dashboard, name="dashboard"),
    path("challenge/", challenge, name="challenge"),
    path("users/", users, name="user"),
    path("teams/", teams, name="team"),
    path("challenge/add/", challenge_add, name="c_add")
]
