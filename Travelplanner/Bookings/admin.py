# Register your models here.

from django.contrib import admin
from .models import Location, Destination, Accommodation, Vehicle, Booking

admin.site.register(Location)
admin.site.register(Destination)
admin.site.register(Accommodation)
admin.site.register(Vehicle)
admin.site.register(Booking)