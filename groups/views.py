from django.shortcuts import render
from groups.models import Group
from groups.serializers import GroupSerializer

# Create your views here.
from rest_framework import generics
from django.core.paginator import Paginator


from rest_framework.filters import SearchFilter
from rest_framework import filters


class GroupListAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id", "name"]


class GroupDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = "id"
