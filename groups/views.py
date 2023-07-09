from django.shortcuts import render
from groups.models import Group
from groups.serializers import GroupSerializer
# Create your views here.
from rest_framework import generics
from django.core.paginator import Paginator


from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters

class UserListView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']

class GroupGeneric(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    


class GroupGeneric2(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = "id"

