from django.db import models
from CardG.models import Card
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    picture = models.URLField(max_length=200, null=True,
                              default='https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
    cards = models.ManyToManyField(Card, default=None, blank=True)
    balance = models.FloatField(default=0)

    def __repr__(self):
        return f'{self.username}'

    def __str__(self):
        return f'{self.username}'
