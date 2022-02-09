from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Family(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=100)

    def __repr__(self):
        return f'Family : {self.name}'


class Animals(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(null=False, max_length=100)
    legs = models.IntegerField(default=0)
    weight =models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True)
    image= models.ImageField(null=True, upload_to='photo_animals/')
    video= models.CharField(max_length=200, null=True)
    owner = models.ManyToManyField(User, null=True)

    def __repr__(self):
        return f'Animal: {self.name}'


    def get_absolute_url(self):
        return reverse('home')
