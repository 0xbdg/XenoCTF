from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/main/index.html")

def teams(request):
    return render(request, "pages/main/teams.html")

def scoreboard(request):
    score = [
      { "y": 100, "label": "Texas" },
      { "y": 200, "label": "Pennsylvania" },
      { "y": 200, "label": "Florida" },
      { "y": 100, "label": "New York" },
      { "y": 250, "label": "Massachusetts" },
      { "y": 100, "label": "Texas" },
      { "y": 200, "label": "Pennsylvania" },
      { "y": 200, "label": "Florida" },
      { "y": 100, "label": "New York" },
      { "y": 250, "label": "Massachusetts" },
    ]
    return render(request, "pages/main/scoreboard.html", context={"scoreboard":score})

def challenge(request):
    return render(request, "pages/main/challenge.html")

def login(request):
    return render(request, "pages/main/login.html",)

def signup(request):
    return render(request, "pages/main/signup.html",)