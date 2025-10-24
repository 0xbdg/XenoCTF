from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import *

router = routers.DefaultRouter()
router.register("challenge", ChallengeView)

urlpatterns = [
    path("test/", include(router.urls))
]
