from urllib import response
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from user.models import Hobby

# Create your views here.

class UserApi(APIView):
    # permission_classes
    def get(self, request):
        hobby_list = Hobby.objects.filter(id__gt=5)
        for hobby in hobby_list:
            print(hobby)
        
        return Response({"message": "get success!!"})
    