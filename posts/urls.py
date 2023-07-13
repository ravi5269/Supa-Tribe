from django.urls import path
from posts.views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path("post/", PostListAPIView.as_view()),
    path("post-detail/<id>", PostDetailAPIView.as_view()),
]
