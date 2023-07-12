from django.urls import path
from users.views import UserLogin, UserGeneric, UserGeneric2, UserAPIView

urlpatterns = [
    path("user-login/", UserLogin.as_view(), name="user-login"),
    path("users/", UserAPIView.as_view()),
    path("users/<int:pk>", UserAPIView.as_view()),
    path("generic/", UserGeneric.as_view()),
    path("generic/<int:pk>", UserGeneric2.as_view()),
]
