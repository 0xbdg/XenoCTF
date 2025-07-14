from django.shortcuts import render
from .models import *
# Create your views here.

def dashboard(request):
    return render(request, "views/dashboard.html")

def challenge(request):
    chall = Challenge.objects.all()
    return render(request, "views/challenges.html")

def users(request):
    return render(request, "views/users.html")

def teams(request):
    return render(request, "views/teams.html")

def challenge_add(request):
    return render(request, "views/details/challenge_add.html")
