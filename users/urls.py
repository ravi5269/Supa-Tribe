from django.urls import path
from users.views import UserLoginSerializer, UserAPIView, UserGeneric, UserGeneric2

urlpatterns = [
    path("user-login/", UserLoginSerializer.as_view(), name="user-login"),
    path("user/", UserAPIView.as_view()),
    path("user/<int:pk>", UserAPIView.as_view()),
    path("generic/", UserGeneric.as_view()),
    path("generic-user/<id>", UserGeneric2.as_view()),
    
]
