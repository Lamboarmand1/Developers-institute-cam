from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    publication_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
