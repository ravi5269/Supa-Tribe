from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from users.manager import UserManager 

# Create your models here.

class User(AbstractBaseUser):
    name = models.CharField(("Name"), max_length=50, blank=True, db_index=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(("Phone"), max_length=12, blank=True, db_index=True)
    bio = models.CharField(("Bio"), max_length=12, blank=True, db_index=True)
    image = models.ImageField(("Image"), upload_to=None, height_field=None, width_field=None, max_length=100)
    city = models.CharField(("City"), max_length=20, blank=True, db_index=True)
    state = models.CharField(("State"), max_length=20, blank=True, db_index=True)
    country = models.CharField(("Country"), max_length=20, blank=True, db_index=True)
    otp = models.IntegerField(null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
    
    def has_module_perms(self,app_label):
        return True
    
    def has_perm(self,perm,obj = None):
        return True
    