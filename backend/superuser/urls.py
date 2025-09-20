from django.urls import path
from .views import *

urlpatterns = [

    path("", dashboard, name="dashboard"),
    path("challenges/", challenge, name="challenge"),
    path("users/", users, name="user"),
    path("teams/", teams, name="team"),
    path("challenge/add/", challenge_add, name="c_add"),
    path("challenge/edit/<int:id>/", challenge_edit, name="c_edit"),
    path("challenge/delete/<int:id>", challenge_delete, name="c_delete"),
    path("chall/file/delete/<int:file_id>", challfile_delete, name="delete_file"),
    path("team/add/", team_add, name="team_add"),
    path("team/edit/<int:id>/", team_edit, name="team_edit")
]
