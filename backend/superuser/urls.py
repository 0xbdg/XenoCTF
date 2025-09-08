from django.urls import path
from .views import *

urlpatterns = [

    path("", dashboard, name="dashboard"),
    path("challenge/", challenge, name="challenge"),
    path("users/", users, name="user"),
    path("teams/", teams, name="team"),
    path("challenge/add/", challenge_add, name="c_add"),
    path("challenge/edit/<int:id>/", challenge_edit, name="c_edit"),
    path("challenge/delete/<int:id>", challenge_delete, name="c_delete")
]
