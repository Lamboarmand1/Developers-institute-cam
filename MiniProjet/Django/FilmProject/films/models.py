from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Country : {self.name}'

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Category : {self.name}'

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'Director : {self.first_name}'


class Film(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField(auto_now_add=True) #default=timezone.now | from django.utils import timezone
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    available_in_countries = models.ManyToManyField(Country, related_name='film_in_country', blank=True)
    category = models.ManyToManyField(Category, related_name='film_in_category')
    director = models.ManyToManyField(Director, related_name='film_director')

    def __str__(self):
        return f'Film : {self.title}'

