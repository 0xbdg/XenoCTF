from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
# Create your views here.

class ChallengeView(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
