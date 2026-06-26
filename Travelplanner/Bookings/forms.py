from django import forms
from .models import Destination, Accommodation, Vehicle

class DestinationForm(forms.Form):
    destination = forms.ModelChoiceField(
        queryset=Destination.objects.none(),
        empty_label="Choose a destination",
        label="Destination",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['destination'].queryset = Destination.objects.select_related('location').order_by('name')

class AccommodationForm(forms.Form):
    accommodation = forms.ModelChoiceField(
        queryset=Accommodation.objects.none(),
        empty_label="Choose a stay",
        label="Stay",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['accommodation'].queryset = Accommodation.objects.select_related('location').order_by('name')

class VehicleForm(forms.Form):
    vehicle = forms.ModelChoiceField(
        queryset=Vehicle.objects.none(),
        empty_label="Choose a rental vehicle",
        label="Car rental",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicle'].queryset = Vehicle.objects.order_by('name')
