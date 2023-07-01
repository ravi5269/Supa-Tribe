from django.urls import path
from posts.views import PostGeneric, PostGeneric2

urlpatterns = [
    path("post/", PostGeneric.as_view()),
    path("post/<id>", PostGeneric2.as_view()),
]
