from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    id= models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image=models.ImageField(null=True, upload_to='image_profile/')
    bio = models.TextField(null=True)
