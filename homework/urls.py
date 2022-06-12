
from django.contrib import admin
from django.urls import path
from .views import PlaceAPI, message

urlpatterns = [
    path('', message),
    path('test/', PlaceAPI.as_view()),
]

