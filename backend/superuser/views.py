import os
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from XenoCTF.settings import BASE_DIR
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
            flag = form2.cleaned_data["flag"]
            hint = form2.cleaned_data["hint"]

            if file != "" and file != None:
                ChallFile(chall_id=id, file=file).save()

            if flag != "" and flag != None:
                ChallFlag(chall_id=id, flag=flag).save()

            if hint != "" and hint != None:
                ChallHint(chall_id=id, hint=hint).save()

        if form.is_valid() or form2.is_valid():
            return redirect("c_edit", data.id) 

    else:
        form = ChallengeForm(instance=data)
        form2 = ChallMiscForm()
    return render(request, "views/details/challenge_edit.html", {"form":form, "data":data, "form2":form2, "file":ChallFile.objects.filter(chall_id=id)})

def challenge_delete(request, id):
    if request.method == "POST":
        Challenge(id=id).delete()
        return redirect("challenge")

def challfile_delete(request, file_id):
    if request.method == "POST":
        os.remove(os.path.join(BASE_DIR,"media/"+ ChallFile.objects.get(id=file_id).file.name))
        ChallFile(id=file_id).delete()
        return redirect("challenge")

def users(request):
    return render(request, "views/users.html")

def teams(request):
    return render(request, "views/teams.html")

