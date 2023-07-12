from django.shortcuts import render
from comments.models import Comment
from comments.serializers import CommentSerializer


# Create your views here.
from rest_framework import filters
from rest_framework import generics


class CommentListAPIView(generics.ListCreateAPIView):
    # import pdb; pdb.set_trace()
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailAPIView(
    generics.UpdateAPIView, generics.DestroyAPIView, generics.RetrieveAPIView
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"


class CommentFilterAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id"]
