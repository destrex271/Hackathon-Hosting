from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import RegisterUser, GetAllUsers

urlpatterns = [
    path('register', RegisterUser.as_view(), name="register"),
    path('get_users', GetAllUsers.as_view(), name="get_users")
]
