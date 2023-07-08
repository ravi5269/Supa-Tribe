from django.urls import path
from groups.views import GroupGeneric, GroupGeneric2

urlpatterns = [
    path("group/", GroupGeneric.as_view()),
    path("group/<id>", GroupGeneric2.as_view())
]
