from django.db import models
from django.urls import reverse


class Type(models.Model):
    name = models.CharField(max_length=2550)

    def __str__(self):
        return f'{self.name}'


class Race(models.Model):
    name = models.CharField(max_length=2550)

    def __str__(self):
        return f'{self.name}'


class Archetype(models.Model):
    name = models.CharField(max_length=2550)

    def __str__(self):
        return f'{self.name}'


class Cardset(models.Model):
    set_name = models.CharField(max_length=2550)
    set_code = models.CharField(max_length=2550)
    set_rarity = models.CharField(max_length=2550)
    set_rarity_code = models.CharField(max_length=2550)
    set_price = models.FloatField()

    def __str__(self):
        return f'{self.set_name}'


class Attribute(models.Model):
    name = models.CharField(max_length=2550)

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    api_id = models.IntegerField()
    image_url = models.URLField()
    image_url_small = models.URLField()

    def __str__(self):
        return f'{self.api_id}'


class Card(models.Model):
    api_id = models.IntegerField()
    name = models.CharField(max_length=2550)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True)
    desc = models.CharField(max_length=2550, null=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, null=True, blank=True)
    archetype = models.ForeignKey(Archetype, on_delete=models.CASCADE, null=True, blank=True)
    cardset = models.ManyToManyField(Cardset, blank=True)
    card_atk = models.IntegerField(null=True, blank=True)
    card_def = models.IntegerField(null=True, blank=True)
    card_level = models.IntegerField(null=True, blank=True)
    attribute = models.ForeignKey(Attribute, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.OneToOneField(Image, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.api_id}: {self.name}'

    def get_absolute_url(self):
        return reverse('card_detail', args=[str(self.id)])


class CardPrice(models.Model):
    cardmarket_price = models.FloatField()
    tcgplayer_price = models.FloatField()
    ebay_price = models.FloatField()
    amazon_price = models.FloatField()
    coolstuffinc_price = models.FloatField()
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.card.api_id}: {self.card.name}'
