from rest_framework import viewsets, permissions
from rest_framework.renderers import JSONRenderer
from .serializer import *
# Create your views here.

class ChallengeAPIView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    renderer_classes= [JSONRenderer]
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

class ChallFileAPIView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]
    queryset = ChallFile.objects.all()
    serializer_class = ChallFileSerializer
