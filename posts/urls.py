from django.urls import path
from posts.views import UserListView, PostListAPIView, PostDetailAPIView

urlpatterns = [
    path("post/", PostListAPIView.as_view()),
    path("post/<id>", PostDetailAPIView.as_view()),
    path("post-filter/", UserListView.as_view()),
]
