from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['destination', 'accommodation', 'vehicle']

        widgets = {
            'destination': forms.Select(attrs={'class': 'form-select'}),
            'accommodation': forms.Select(attrs={'class': 'form-select'}),
            'vehicle': forms.Select(attrs={'class': 'form-select'}),
        }