from tkinter import Place
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# Create your views here.


def message(request):
    abc = {'message':'success!!!'}
    return JsonResponse(abc)

class PlaceAPI(APIView):
    # permission_classes
    def get(self, request):
        return Response({"message":"Hello!"})

