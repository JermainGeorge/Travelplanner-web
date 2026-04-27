from django import forms
from django.utils import timezone
from .models import Booking


class BookingForm(forms.ModelForm):
    date = forms.DateField(
        initial=timezone.now().date(),
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Booking
        fields = ['destination', 'accommodation', 'vehicle', 'date']