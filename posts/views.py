from django.shortcuts import render

# Create your views here.
from posts.models import Post
from posts.serializers import PostSerializer


# Create your views here.
from django.core.paginator import Paginator
from rest_framework import generics

from rest_framework import filters


class UserListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "id"]


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(
    generics.UpdateAPIView,
    generics.DestroyAPIView,
    generics.ListAPIView,
    generics.RetrieveAPIView,
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"
