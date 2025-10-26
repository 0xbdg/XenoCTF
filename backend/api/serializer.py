from rest_framework import serializers

from superuser.models import *

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = "__all__"

class ChallFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallFile
        fields = "__all__"
