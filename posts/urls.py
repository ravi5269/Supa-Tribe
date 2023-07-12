from django.urls import path
from posts.views import PostGeneric, PostGeneric2, UserListView

urlpatterns = [
    path("post/", PostGeneric.as_view()),
    path("post/<id>", PostGeneric2.as_view()),
    # path("post-filter/", UserListView.as_view()),
]
