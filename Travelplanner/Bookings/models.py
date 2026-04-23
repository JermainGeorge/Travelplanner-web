
from django.db import models
from django.contrib.auth.models import User


class Destination(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.country}"
    

class Accommodation(models.Model):
    ACCOMMODATION_TYPES = [
        ('hotel', 'Hotel'),
        ('airbnb', 'Airbnb'),
    ]

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=ACCOMMODATION_TYPES)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.type})"



class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('car', 'Car'),
        ('van', 'Van'),
        ('bus', 'Bus'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=VEHICLE_TYPES)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booking to {self.destination}"