from django.shortcuts import render

# Create your views here.
from posts.models import Post
from posts.serializers import PostSerializer


# Create your views here.
from django.core.paginator import Paginator
from rest_framework import generics

from rest_framework import filters


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "id"]


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"
