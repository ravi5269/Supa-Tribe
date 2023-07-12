from django.urls import path
from groups.views import GroupListAPIView, GroupDetailAPIView, GroupFilterAPIView

urlpatterns = [
    path("group-list/", GroupListAPIView.as_view()),
    path("group/<id>", GroupDetailAPIView.as_view()),
    path("group-filter/", GroupFilterAPIView.as_view()),
    #  path("group-filter/<id>", GroupFilterAPIView.as_view())
]
