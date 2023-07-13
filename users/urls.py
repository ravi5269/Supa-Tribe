from django.urls import path
from users.views import UserLogin, UserListAPIView, UserDetailAPIView

urlpatterns = [
    path("user-registration/", UserLogin.as_view(), name="user-login"),
    path("users/", UserListAPIView.as_view()),
    path("users-detail/<int:pk>", UserDetailAPIView.as_view()),
]
