from django.shortcuts import render
from user_accounts.models import *
from rest_framework import generics , mixins
from .serializers import *
# Create your views here.


class List_View(generics.ListAPIView):
    
    queryset = staff.objects.all()
    serializer_class = staff_serializers
    
