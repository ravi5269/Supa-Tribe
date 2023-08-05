from django.urls import path
from groups.views import GroupListAPIView, GroupDetailAPIView

urlpatterns = [
    path("group/", GroupListAPIView.as_view()),
    path("group-detail/<id>", GroupDetailAPIView.as_view()),
]
