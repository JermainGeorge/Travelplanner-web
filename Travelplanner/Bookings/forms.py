from django import forms
from .models import Accommodation, Destination, Location, Vehicle

class DestinationForm(forms.Form):
    location = forms.ModelChoiceField(
        queryset=Location.objects.none(),
        empty_label="Choose a location in Kenya",
        label="Location",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    destination = forms.ModelChoiceField(
        queryset=Destination.objects.none(),
        empty_label="Choose a tour destination",
        label="Tour destination",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    people = forms.IntegerField(
        min_value=1,
        label="People",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number of people visiting"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.order_by('name')
        destinations = Destination.objects.select_related('location').order_by('name')
        location_id = self.data.get('location') if self.is_bound else None

        if location_id:
            destinations = destinations.filter(location_id=location_id)

        self.fields['destination'].queryset = destinations

    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get('location')
        destination = cleaned_data.get('destination')

        if location and destination and destination.location_id != location.id:
            self.add_error('destination', 'Choose a destination that belongs to the selected location.')

        return cleaned_data

class AccommodationForm(forms.Form):
    location = forms.ModelChoiceField(
        queryset=Location.objects.none(),
        empty_label="Choose accommodation location",
        label="Location",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    accommodation_type = forms.ChoiceField(
        choices=[('', 'Choose stay type')] + Accommodation.ACCOMMODATION_TYPES,
        label="Hotel / Airbnb",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    accommodation = forms.ModelChoiceField(
        queryset=Accommodation.objects.none(),
        empty_label="Choose a stay name",
        label="Name",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    people = forms.IntegerField(
        min_value=1,
        label="People",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number of guests"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.order_by('name')
        accommodations = Accommodation.objects.select_related('location').order_by('name')
        location_id = self.data.get('location') if self.is_bound else None
        accommodation_type = self.data.get('accommodation_type') if self.is_bound else None

        if location_id:
            accommodations = accommodations.filter(location_id=location_id)

        if accommodation_type:
            accommodations = accommodations.filter(type=accommodation_type)

        self.fields['accommodation'].queryset = accommodations

    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get('location')
        accommodation_type = cleaned_data.get('accommodation_type')
        accommodation = cleaned_data.get('accommodation')

        if location and accommodation and accommodation.location_id != location.id:
            self.add_error('accommodation', 'Choose a stay that belongs to the selected location.')

        if accommodation_type and accommodation and accommodation.type != accommodation_type:
            self.add_error('accommodation', 'Choose a stay that matches the selected type.')

        return cleaned_data

class VehicleForm(forms.Form):
    location = forms.ModelChoiceField(
        queryset=Location.objects.none(),
        empty_label="Choose pickup location",
        label="Location",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    vehicle_type = forms.ChoiceField(
        choices=[('', 'Choose vehicle type')] + Vehicle.VEHICLE_TYPES,
        label="Type",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    vehicle = forms.ModelChoiceField(
        queryset=Vehicle.objects.none(),
        empty_label="Choose a rental vehicle",
        label="Vehicle",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    seats = forms.IntegerField(
        min_value=1,
        label="Seater",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Number of seats"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].queryset = Location.objects.order_by('name')
        vehicles = Vehicle.objects.select_related('location').order_by('name')
        location_id = self.data.get('location') if self.is_bound else None
        vehicle_type = self.data.get('vehicle_type') if self.is_bound else None

        if location_id:
            vehicles = vehicles.filter(location_id=location_id)

        if vehicle_type:
            vehicles = vehicles.filter(vehicle_type=vehicle_type)

        self.fields['vehicle'].queryset = vehicles

    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get('location')
        vehicle_type = cleaned_data.get('vehicle_type')
        vehicle = cleaned_data.get('vehicle')
        seats = cleaned_data.get('seats')

        if location and vehicle and vehicle.location_id != location.id:
            self.add_error('vehicle', 'Choose a vehicle that belongs to the selected pickup location.')

        if vehicle_type and vehicle and vehicle.vehicle_type != vehicle_type:
            self.add_error('vehicle', 'Choose a vehicle that matches the selected type.')

        if seats and vehicle and seats > vehicle.capacity:
            self.add_error('seats', 'The selected vehicle does not have enough seats.')

        return cleaned_data
