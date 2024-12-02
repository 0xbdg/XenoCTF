from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path("teams/", teams,name="team"),
    path("scoreboard/", scoreboard,name="scoreboard"),
    path("challenge/", challenge,name="challenge"),
]
