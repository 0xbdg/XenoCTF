from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("challenge", ChallengeView)
router.register("challenge/file", ChallFileView)

urlpatterns = [path("test/", include(router.urls))]
