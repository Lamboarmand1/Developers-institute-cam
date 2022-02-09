from datetime import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class VehicleType(models.Model):
    name = models.CharField(max_length=50)

class VehicleSize(models.Model):
    name = models.CharField(max_length=50)

class Vehicle(models.Model):
    vehicletype = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    cost = models.FloatField()

class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    vehicle_rent = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING)

class RentalRate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)