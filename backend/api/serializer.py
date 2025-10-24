from rest_framework import serializers

from superuser.models import *

class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Challenge
        fields = "__all__"
