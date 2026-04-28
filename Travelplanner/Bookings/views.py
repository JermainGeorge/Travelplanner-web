from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm, DestinationFrom, AccommodationForm, VehicleForm
from .models import Booking, Destination, Accommodation, Vehicle

# Creating views for each form to handle the booking process and display receipts
@login_required
def bookings(request):
    d_form = DestinationFrom()
    a_form = AccommodationForm()
    v_form = VehicleForm()

    if request.method == 'POST':
        if 'destination_submit' in request.POST:
            d_form = DestinationFrom(request.POST)
            if d_form.is_valid():
                obj = d_form.save(commit=False)
                obj.user = request.user
                obj.save()
                return redirect('receipts')

        elif 'accommodation_submit' in request.POST:
            a_form = AccommodationForm(request.POST)
            if a_form.is_valid():
                obj = a_form.save(commit=False)
                obj.user = request.user
                obj.save()
                return redirect('receipts')

        elif 'vehicle_submit' in request.POST:
            v_form = VehicleForm(request.POST)
            if v_form.is_valid():
                obj = v_form.save(commit=False)
                obj.user = request.user
                obj.save()
                return redirect('receipts')

    return render(request, 'Bookings/bookings.html', {
        'd_form': d_form,
        'a_form': a_form,
        'v_form': v_form,
    })


@login_required
def receipts_view(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'Bookings/receipts.html', {'bookings': bookings})