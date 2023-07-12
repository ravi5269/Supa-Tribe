from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.


class User(AbstractBaseUser):
    username = models.CharField(
        ("username"),
        max_length=10,
        null=False,
        blank=True,
        unique=True,
        db_index=True,
        db_column="username",
    )
    name = models.CharField(("Name"), max_length=50, blank=True, db_index=True)
    email = models.EmailField(("Email"), max_length=50, blank=True, db_index=True)
    phone = models.CharField(("Phone"), max_length=12, blank=True, db_index=True)
    bio = models.CharField(("Bio"), max_length=12, blank=True, db_index=True)
    image = models.ImageField(("Image"), upload_to="images", blank=True, db_index=True)
    city = models.CharField(("City"), max_length=20, blank=True, db_index=True)
    state = models.CharField(("State"), max_length=20, blank=True, db_index=True)
    country = models.CharField(("Country"), max_length=20, blank=True, db_index=True)

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = ["name", "email", "phone"]
