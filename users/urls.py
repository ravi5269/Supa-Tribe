from django.urls import path
from users.views import (
    UserListAPIView,
    UserDetailAPIView,
    UserJoinAPIView,
    UserEmailVerifyAPIView,
)


urlpatterns = [
    path("users/", UserListAPIView.as_view()),
    path("users-detail/<int:pk>", UserDetailAPIView.as_view()),
    path("email-register/", UserJoinAPIView.as_view()),
    path("email-verify/", UserEmailVerifyAPIView.as_view()),
]
