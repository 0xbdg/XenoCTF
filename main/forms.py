from django import forms
from django.forms.widgets import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class SignupForm(UserCreationForm):
    username=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField()
    password2=forms.CharField()

    class Meta:
        model = User