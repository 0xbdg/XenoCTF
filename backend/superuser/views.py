import os
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from XenoCTF.settings import BASE_DIR
from .models import *
from .forms import *
# Create your views here.

def dashboard(request):
    total_team = Team.objects.count()
    total_challenge = Challenge.objects.count()
    total_user = Player.objects.count()
    total_solved = ChallSolved.objects.count()

    return render(request, "views/dashboard.html", {"total_team":total_team, "total_chall":total_challenge, "total_user":total_user, "total_solved":total_solved})

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
    data = Player.objects.all()
    return render(request, "views/users.html", {"users":data})

def user_add(request):
    form = PlayerAddForm(data=request.POST)

    if form.is_valid():
        form.save()
        return redirect("user")
    
    else:
        form = PlayerAddForm()

    return render(request, "views/details/user_add.html", {"form":form})

def user_edit(request, id):
    data = Player.objects.get(id=id)
    form = PlayerAddForm(data=request.POST, instance=data)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("user_edit", data.id)

    else:
        pass
    return render(request,"views/details/team_edit.html", {"data":data})

def teams(request):
    data = Team.objects.all()
    return render(request, "views/teams.html", {"teams":data})

def team_add(request):
    form = TeamForm(data=request.POST)

    if request.method == "POST":
        if form.is_valid():
            team_name = form.cleaned_data["team_name"]
            affiliation = form.cleaned_data["affiliation"]
            team_email = form.cleaned_data["email"]
            status = form.cleaned_data["status"]
            is_banned = form.cleaned_data["banned"]
            
            Team(team_name=team_name, affiliation=affiliation, email=team_email, status=status, banned=is_banned, total_point=0).save()
            return redirect("team")

    else:
        form = TeamForm()
    return render(request, "views/details/team_add.html", {"form":form})

def team_edit(request, id):
    data = Team.objects.get(id=id)
    form = TeamForm(data=request.POST, instance=data)
    form2 = TeamPlayerForm(data=request.POST)

    if request.method == "POST":
        
        if form.is_valid():
            form.save()

        if form2.is_valid():
            player_input = form2.cleaned_data["player"]

            TeamMember(player_id=player_input)

        if form.is_valid() or form2.is_valid():
            return redirect("team_edit", data.id) 
    else:
        form = TeamForm(instance=data)
    return render(request, "views/details/team_edit.html", {"data":data,"form":form, "player":TeamMember.objects.all(), "users":Player.objects.all(), "form2":form2})
