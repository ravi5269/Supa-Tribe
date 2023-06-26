from django.db import models
from base.models import BaseModel 
from users.models import User
from groups.models import Group
# Create your models here.

class Post(BaseModel):
    title = models.CharField(("Title"),max_length=100,db_index=True,blank=True)
    content = models.CharField(("Content"),max_length=50,db_index=True,blank=True)
    image = models.ImageField(("Image"),upload_to=None, height_field=None, width_field=None, max_length=100)
    owner = models.OneToOneField(User,on_delete=models.CASCADE)
    posted_At = models.OneToOneField(Group,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name='Likes')
