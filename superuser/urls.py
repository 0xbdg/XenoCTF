from django.urls import path
from .views import *

urlpatterns = [
    path("admin/login/", LoginPage().as_view()),
    path("admin/dashboard/", Dashboard().as_view())
]
