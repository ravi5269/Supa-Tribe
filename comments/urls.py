from django.urls import path
from comments.views import CommentGeneric, CommentGeneric2

urlpatterns = [
    path("comment/", CommentGeneric.as_view()),
    path("comment/<id>", CommentGeneric2.as_view()),
]
