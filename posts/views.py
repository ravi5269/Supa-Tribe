from django.shortcuts import render

# Create your views here.
from posts.models import Post
from posts.serializers import PostSerializer


# Create your views here.

from rest_framework import generics


class PostGeneric(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostGeneric2(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"
