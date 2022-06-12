
from django.contrib import admin
from django.urls import path

from user.views import UserApi

urlpatterns = [
    path('', UserApi.as_view()),
]
