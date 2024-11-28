from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/main/index.html")

def playerlist(request):
    return render(request, "pages/main/playerlists.html")

def scoreboard(request):
    return render(request, "pages/main/scoreboard.html")

def challenge(request):
    return render(request, "pages/main/challenge.html")

def login(request):
    return render(request, "pages/main/login.html",)

def signup(request):
    return render(request, "pages/main/signup.html",)