from django.db import models
from base.models import BaseModel
from users.models import User
from groups.models import Group

# Create your models here.


class Post(BaseModel):
    title = models.CharField(("title"), max_length=100, db_index=True, blank=True)
    content = models.CharField(("content"), max_length=50, db_index=True, blank=True)
    image = models.ImageField(
        ("image"), upload_to=None, height_field=None, width_field=None, max_length=100
    )
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    posted_at = models.OneToOneField(Group, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes")

    def __str__(self) -> str:
        return (f"{self.title},{self.owner},{self.posted_at}")
