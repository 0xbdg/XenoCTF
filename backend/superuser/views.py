from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, "views/dashboard.html")

def challenge(request):
    return render(request, "views/challenges.html")

def users(request):
    return render(request, "views/users.html")
