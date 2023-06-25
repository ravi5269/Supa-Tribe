from django.urls import path
from users.views import UserRegistrationView, UserAPIView, UserGeneric, UserGeneric2

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-register"),
    path("user/", UserAPIView.as_view()),
    path("user/<int:pk>", UserAPIView.as_view()),
    
    path("generic/", UserGeneric.as_view()),
    path("generic-user/<id>", UserGeneric2.as_view()),
]
