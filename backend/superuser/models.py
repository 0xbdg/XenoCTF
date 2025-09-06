from django.db import models
from django.contrib.auth.models import User
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
    chall_id = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    file = models.FileField(upload_to="chall/")

class ChallFlag(models.Model):
    chall_id = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    flag = models.CharField(max_length=1000, null=False, blank=False)

class ChallHint(models.Model):
    chall_id = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    hint = models.CharField(max_length=1000, null=False, blank=False)

class Team(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    affiliate = models.CharField(max_length=500, null=False, blank=False)
    total_point = models.IntegerField(null=False)
    player = models.ForeignKey(User, on_delete=models.CASCADE)

class Activity(models.Model):
    desc = models.TextField(null=False)
