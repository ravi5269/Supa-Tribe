from django.urls import path
from comments.views import CommentListAPIView, CommentDetailAPIView


urlpatterns = [
    path("comment/", CommentListAPIView.as_view()),
    path("comment-detail/<id>", CommentDetailAPIView.as_view()),
]
