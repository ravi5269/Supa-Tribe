from django.db import models
from base.models import BaseModel
from users.models import User
from posts.models import Post

# Create your models here.


class Comment(BaseModel):
    content = models.CharField(max_length=50, db_index=True, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="Like")
    commented_At = models.OneToOneField(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content
