from django.shortcuts import render
from groups.models import Group
from groups.serializers import GroupSerializer

# Create your views here.
from rest_framework import generics
from django.core.paginator import Paginator


from rest_framework.filters import SearchFilter

# from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters


class GroupListAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetailAPIView(
    generics.UpdateAPIView,
    generics.DestroyAPIView,
    generics.ListAPIView,
    generics.RetrieveAPIView,
):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = "id"


class GroupFilterAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id", "name"]
