from django.shortcuts import render
from groups.models import Group
from groups.serializers import GroupSerializer

# from django.core.paginator import Paginator
# from rest_framework.generics import ListAPIView

from rest_framework import filters

# Create your views here.
from rest_framework import generics
import django_filters.rest_framework
from django.core.paginator import Paginator



class GroupGeneric(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
 

class GroupGeneric2(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = "id"



   