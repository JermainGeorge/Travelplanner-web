from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import DestinationForm, AccommodationForm, VehicleForm
from .models import Accommodation, Booking, Destination, Vehicle

@login_required
def bookings(request):
    d_form = DestinationForm()
    a_form = AccommodationForm()
    v_form = VehicleForm()

    if request.method == 'POST':

        # DESTINATION
        if 'destination_submit' in request.POST:
            d_form = DestinationForm(request.POST)
            if d_form.is_valid():
                obj = d_form.cleaned_data['destination']

                request.session['destination_id'] = obj.id
                return redirect('bookings')

        # ACCOMMODATION
        elif 'accommodation_submit' in request.POST:
            a_form = AccommodationForm(request.POST)
            if a_form.is_valid():
                obj = a_form.cleaned_data['accommodation']

                request.session['accommodation_id'] = obj.id
                return redirect('bookings')

        # VEHICLE
        elif 'vehicle_submit' in request.POST:
            v_form = VehicleForm(request.POST)
            if v_form.is_valid():
                obj = v_form.cleaned_data['vehicle']

                request.session['vehicle_id'] = obj.id
                return redirect('bookings')

        # FINAL BOOKING
        elif 'confirm_booking' in request.POST:
            dest_id = request.session.get('destination_id')
            acc_id = request.session.get('accommodation_id')
            veh_id = request.session.get('vehicle_id')

            if dest_id and acc_id and veh_id:
                destination = Destination.objects.get(id=dest_id)
                accommodation = Accommodation.objects.get(id=acc_id)
                vehicle = Vehicle.objects.get(id=veh_id)
                total_price = (
                    destination.estimated_price
                    + accommodation.price_per_night
                    + vehicle.price_per_day
                )

                Booking.objects.create(
                    user=request.user,
                    destination=destination,
                    accommodation=accommodation,
                    vehicle=vehicle,
                    date=timezone.now().date(),
                    payment_method=request.POST.get('payment_method', 'mobile_money'),
                    status='confirmed',
                    total_price=total_price
                )

                request.session.pop('destination_id', None)
                request.session.pop('accommodation_id', None)
                request.session.pop('vehicle_id', None)

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
