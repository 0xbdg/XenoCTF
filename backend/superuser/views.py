from django.shortcuts import redirect, render
from .models import *
from .forms import *
# Create your views here.

def dashboard(request):
    return render(request, "views/dashboard.html")

def challenge(request):
    chall = Challenge.objects.all()
    return render(request, "views/challenges.html", {"challs":chall})

def users(request):
    return render(request, "views/users.html")

def teams(request):
    return render(request, "views/teams.html")

def challenge_add(request):
    form = ChallengeAddForm(data=request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("challenge")

    else:
        form = ChallengeAddForm()
    return render(request, "views/details/challenge_add.html", {"form":form})

def challenge_edit(request, id):
    data = Challenge.objects.get(id=id)
    form = ChallengeEditForm(data=request.POST, instance=data)

    if request.method == "POST":
        form.save()
        return redirect("c_edit", data.id)

    else:
        form = ChallengeEditForm(instance=data)
    return render(request, "views/details/challenge_edit.html", {"form":form, "data":data})

def challenge_delete(request, id):
    if request.method == "POST":
        Challenge(id=id).delete()
        return redirect("challenge")

