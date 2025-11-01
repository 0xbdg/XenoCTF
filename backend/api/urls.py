from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("challenge", ChallengeAPIView)
router.register("file", ChallFileAPIView)

urlpatterns = [path("test/", include(router.urls))]
