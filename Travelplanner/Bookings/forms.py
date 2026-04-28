from django import forms
from django.utils import timezone
from .models import Booking , Destination, Accommodation, Vehicle

#create forms for each model to be used in the views and templates
class DestinationFrom(forms.ModelForm):
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

class BookingForm(forms.ModelForm):
    date = forms.DateField(
        initial=timezone.now().date(),
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Booking
        fields = ['destination', 'accommodation', 'vehicle', 'date']