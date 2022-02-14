from django.urls import path
from . views import dashboard, profile_list

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list")
]
