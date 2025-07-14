from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY = (
    ("web", "Web Exploitation"),
    ("binex", "Binary Exploitation"),
    ("re", "Reverse Engineering"),
    ("foren", "Forensic"),
    ("osint", "Osint"),
    ("misc", "Misc")
)

class Challenge(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY, blank=False, null=False)
    message = models.TextField(null=False, blank=False)
    status = models.BooleanField(default=True)
    value = models.IntegerField(null=False)

    def __str__(self):
        return f"{self.name} - {self.category}"

class Team(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    affiliate = models.CharField(max_length=500, null=False, blank=False)
    total_point = models.IntegerField(null=False)

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Chall(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    file = models.FileField(upload_to="chall/")

class Activity(models.Model):
    desc = models.TextField(null=False)
