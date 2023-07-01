from django.shortcuts import render
from groups.models import Group
from groups.serializers import GroupSerializer

from django.core.paginator import Paginator


# Create your views here.
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


class CustomNumberPagination(PageNumberPagination):
    page_size = 5


class GroupGeneric(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = CustomNumberPagination


class GroupGeneric2(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = "id"
