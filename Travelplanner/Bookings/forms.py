from django import forms
from .models import Destination, Accommodation, Vehicle

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'location']

class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ['name', 'location', 'type', 'price_per_night']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'vehicle_type', 'capacity', 'price_per_day']