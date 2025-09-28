from .models import *
from django import forms
from django.forms.widgets import *

class ChallengeForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    category = forms.ChoiceField(label="Category", choices=CATEGORY, required=True,widget=Select(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    message =  forms.CharField(required=True, widget=Textarea(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    status = forms.ChoiceField(label="Status", choices=STATUS,required=True, widget=Select(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    connection = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    value = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))

    class Meta:
        model = Challenge
        fields = "__all__"

class ChallMiscForm(forms.Form):
    file = forms.FileField(required=False,widget=FileInput(attrs={"class":"border border-gray-300 rounded px-2 py-1 text-sm","aria-describedby":"file-upload"}))
    flag = forms.CharField(required=False,widget=TextInput(attrs={"class":"border border-gray-300 rounded px-2 py-1 text-sm"}))
    hint = forms.CharField(required=False,widget=TextInput(attrs={"class":"border border-gray-300 rounded px-2 py-1 text-sm"}))

class TeamForm(forms.ModelForm):
    team_name = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    affiliation = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    email = forms.EmailField(widget=EmailInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    status = forms.ChoiceField(label="Status",required=True,choices=STATUS, widget=Select(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    banned = forms.BooleanField(label="banned", initial=False,required=False,widget=CheckboxInput(attrs={"":""}))

    class Meta:
        model = Team
        fields = ["team_name", "affiliation", "email", "status", "banned"]

class TeamPlayerForm(forms.Form):
    player = forms.ModelChoiceField(queryset=Player.objects.all(), empty_label="Select player", widget=Select(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))

class PlayerForm(forms.ModelForm): 
    first_name = forms.CharField(widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    last_name = forms.CharField(widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    username = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    email = forms.EmailField(required=True, widget=EmailInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    password = forms.CharField(required=True, widget=PasswordInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"})) 

    class Meta:
        model = Player
        fields = ["first_name","last_name","username", "email", "password", "is_superuser", "verified"]

    def save(self, commit=True):
        user = super(PlayerForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.is_active = True
        user.is_superuser = self.cleaned_data["is_superuser"]
        user.verified = self.cleaned_data["verified"]

        if commit:
            user.save()
        return user
