from .models import *
from django import forms
from django.forms.widgets import *

class ChallengeAddForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    category = forms.ChoiceField(label="Category", choices=CATEGORY, required=True,widget=Select(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    message =  forms.CharField(required=True, widget=Textarea(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    status = forms.ChoiceField(label="Status", choices=STATUS,required=True, widget=Select(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    connection = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    value = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))

    class Meta:
        model = Challenge
        fields = "__all__"

class ChallengeEditForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    category = forms.ChoiceField(label="Category", choices=CATEGORY, required=True,widget=Select(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    message =  forms.CharField(required=True, widget=Textarea(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    status = forms.ChoiceField(label="Status", choices=STATUS,required=True, widget=Select(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    connection = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))
    value = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full border border-gray-300 rounded px-3 py-2 text-sm text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-600 focus:border-blue-600"}))

    class Meta:
        model = Challenge
        fields = "__all__"

