from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.

def dashboard(request):
    return render(request, "views/dashboard.html")

def challenge(request):
    chall = Challenge.objects.all()
    return render(request, "views/challenges.html", {"challs":chall})

def challenge_add(request):
    form = ChallengeForm(data=request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("challenge")

    else:
        form = ChallengeForm()
    return render(request, "views/details/challenge_add.html", {"form":form})

def challenge_edit(request, id):
    data = Challenge.objects.get(id=id)
    form = ChallengeForm(data=request.POST, instance=data)
    form2 = ChallMiscForm(request.POST, request.FILES)

    if request.method == "POST":

        if form.is_valid():
            form.save()

        if form2.is_valid():
            file = form2.cleaned_data["file"]

            ChallFile(chall_id=id, file=file).save()

        if form.is_valid() or form2.is_valid():
            return redirect("c_edit", data.id) 

    else:
        form = ChallengeForm(instance=data)
        form2 = ChallMiscForm()
    return render(request, "views/details/challenge_edit.html", {"form":form, "data":data, "form2":form2})

def challenge_delete(request, id):
    if request.method == "POST":
        Challenge(id=id).delete()
        return redirect("challenge")

def users(request):
    return render(request, "views/users.html")

def teams(request):
    return render(request, "views/teams.html")

