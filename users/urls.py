from django.urls import path
from users.views import (
    UserLogin,
    UserListAPIView,
    UserDetailAPIView,
    UserAPIView,
    UserFilterAPIView,
)

urlpatterns = [
    path("user-login/", UserLogin.as_view(), name="user-login"),
    path("users/", UserAPIView.as_view()),
    path("users/<int:pk>", UserAPIView.as_view()),
    path("generic/", UserListAPIView.as_view()),
    path("generic/<int:pk>", UserDetailAPIView.as_view()),
    path("user-filter/", UserFilterAPIView.as_view()),
]
