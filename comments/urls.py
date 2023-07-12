from django.urls import path
from comments.views import (
    CommentListAPIView,
    CommentDetailAPIView,
    CommentFilterAPIView,
)


urlpatterns = [
    path("comment-list/", CommentListAPIView.as_view()),
    path("comment/<id>", CommentDetailAPIView.as_view()),
    path("comment-filter/", CommentFilterAPIView.as_view()),
]
