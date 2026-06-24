from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Destination(models.Model):
    DESTINATION_CATEGORIES = [
        ('coastal', 'Coastal'),
        ('safari', 'Safari'),
        ('historical', 'Historical Tour'),
        ('backpacking', 'Backpacking'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=DESTINATION_CATEGORIES, default='coastal')
    description = models.TextField(blank=True)
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Accommodation(models.Model):
    ACCOMMODATION_TYPES = [
        ('hotel', 'Hotel'),
        ('airbnb', 'Airbnb'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    type = models.CharField(max_length=10, choices=ACCOMMODATION_TYPES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.location})"


class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('van', 'Van'),
        ('bus', 'Bus'),
        ('suv', 'SUV'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    capacity = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Booking(models.Model):
    PAYMENT_METHODS = [
        ('card', 'Card'),
        ('mobile_money', 'Mobile Money'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
    ]

    BOOKING_STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)

    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)

    date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default='mobile_money')
    status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user} - {self.destination}"
