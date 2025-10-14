from django.db import models
from django.contrib.auth.models import *
# Create your models here.

CATEGORY = (
    ("web", "Web Exploitation"),
    ("binex", "Binary Exploitation"),
    ("re", "Reverse Engineering"),
    ("foren", "Forensic"),
    ("osint", "OSINT"),
    ("misc", "Misc")
)

STATUS = (
    ("visible", "Visible"),
    ("hidden", "Hidden")
)

class Challenge(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY, blank=False, null=False)
    message = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=100, choices=STATUS, blank=False, null=False)
    connection = models.CharField(max_length=1000, blank=False,null=False)
    value = models.IntegerField(null=False) 

class ChallFile(models.Model):
    chall = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    file = models.FileField(upload_to="chall/")

class ChallFlag(models.Model):
    chall = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    flag = models.CharField(max_length=1000, null=False, blank=False)

class ChallHint(models.Model):
    chall = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    hint = models.CharField(max_length=1000, null=False, blank=False)

class Team(models.Model):
    team_name = models.CharField(max_length=500, null=False, blank=False)
    affiliation = models.CharField(max_length=500, null=False, blank=False)
    email = models.EmailField()
    banned = models.BooleanField()
    status = models.CharField(max_length=100, choices=STATUS, null=False)  
    total_point = models.IntegerField()

class Player(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=500, choices=STATUS)
    verified = models.BooleanField(default=False) 

class Activity(models.Model):
    desc = models.TextField(null=False)

class ChallSolved(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    chall = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    point = models.IntegerField(null=False)
