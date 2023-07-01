from django.db import models
from base.models import BaseModel
from users.models import User


class Group(BaseModel):
    name = models.CharField(("Name"), max_length=50, blank=True, db_index=True)
    description = models.CharField(
        ("Description"), max_length=50, blank=True, db_index=True
    )
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="groups")
    members = models.ManyToManyField(User, related_name="members")
    mods = models.ManyToManyField(User, related_name="mods")

    def __str__(self) -> str:
        return self.name
