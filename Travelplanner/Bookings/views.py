from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from .forms import DestinationForm, AccommodationForm, VehicleForm
from .models import Accommodation, Booking, Destination, Vehicle

@login_required
def bookings(request):
    active_step = request.GET.get('step', 'destination')
    if active_step not in ['destination', 'accommodation', 'vehicles', 'receipts']:
        active_step = 'destination'
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
                request.session['destination_people'] = d_form.cleaned_data['people']
                return redirect(f"{reverse('nav-bookings')}?step=accommodation")
            active_step = 'destination'

        # ACCOMMODATION
        elif 'accommodation_submit' in request.POST:
            a_form = AccommodationForm(request.POST)
            if a_form.is_valid():
                obj = a_form.cleaned_data['accommodation']

                request.session['accommodation_id'] = obj.id
                request.session['accommodation_people'] = a_form.cleaned_data['people']
                return redirect(f"{reverse('nav-bookings')}?step=vehicles")
            active_step = 'accommodation'

        # VEHICLE
        elif 'vehicle_submit' in request.POST:
            v_form = VehicleForm(request.POST)
            if v_form.is_valid():
                obj = v_form.cleaned_data['vehicle']

                request.session['vehicle_id'] = obj.id
                request.session['vehicle_seats'] = v_form.cleaned_data['seats']
                return redirect(f"{reverse('nav-bookings')}?step=receipts")
            active_step = 'vehicles'

        # FINAL BOOKING
        elif 'confirm_booking' in request.POST:
            dest_id = request.session.get('destination_id')
            acc_id = request.session.get('accommodation_id')
            veh_id = request.session.get('vehicle_id')

            if dest_id and acc_id and veh_id:
                destination = Destination.objects.get(id=dest_id)
                accommodation = Accommodation.objects.get(id=acc_id)
                vehicle = Vehicle.objects.get(id=veh_id)
                destination_people = request.session.get('destination_people', 1)
                accommodation_people = request.session.get('accommodation_people', 1)
                total_price = (
                    destination.estimated_price * destination_people
                    + accommodation.price_per_night * accommodation_people
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
                request.session.pop('destination_people', None)
                request.session.pop('accommodation_people', None)
                request.session.pop('vehicle_seats', None)

                return redirect('receipts')
            active_step = 'receipts'

    destination = None
    accommodation = None
    vehicle = None
    destination_total = 0
    accommodation_total = 0
    vehicle_total = 0

    dest_id = request.session.get('destination_id')
    acc_id = request.session.get('accommodation_id')
    veh_id = request.session.get('vehicle_id')
    destination_people = request.session.get('destination_people', 1)
    accommodation_people = request.session.get('accommodation_people', 1)
    vehicle_seats = request.session.get('vehicle_seats', 1)

    if dest_id:
        destination = Destination.objects.filter(id=dest_id).select_related('location').first()
        if destination:
            destination_total = destination.estimated_price * destination_people

    if acc_id:
        accommodation = Accommodation.objects.filter(id=acc_id).select_related('location').first()
        if accommodation:
            accommodation_total = accommodation.price_per_night * accommodation_people

    if veh_id:
        vehicle = Vehicle.objects.filter(id=veh_id).select_related('location').first()
        if vehicle:
            vehicle_total = vehicle.price_per_day

    receipt_total = destination_total + accommodation_total + vehicle_total
    booking_options = {
        'destinations': [
            {
                'id': destination.id,
                'name': destination.name,
                'location_id': destination.location_id,
                'price': str(destination.estimated_price),
            }
            for destination in Destination.objects.select_related('location').order_by('name')
        ],
        'accommodations': [
            {
                'id': accommodation.id,
                'name': accommodation.name,
                'location_id': accommodation.location_id,
                'type': accommodation.type,
                'price': str(accommodation.price_per_night),
            }
            for accommodation in Accommodation.objects.select_related('location').order_by('name')
        ],
        'vehicles': [
            {
                'id': vehicle.id,
                'name': vehicle.name,
                'location_id': vehicle.location_id,
                'type': vehicle.vehicle_type,
                'capacity': vehicle.capacity,
                'price': str(vehicle.price_per_day),
            }
            for vehicle in Vehicle.objects.select_related('location').order_by('name')
        ],
    }

    return render(request, 'Bookings/bookings.html', {
        'd_form': d_form,
        'a_form': a_form,
        'v_form': v_form,
        'active_step': active_step,
        'selected_destination': destination,
        'selected_accommodation': accommodation,
        'selected_vehicle': vehicle,
        'destination_people': destination_people,
        'accommodation_people': accommodation_people,
        'vehicle_seats': vehicle_seats,
        'destination_total': destination_total,
        'accommodation_total': accommodation_total,
        'vehicle_total': vehicle_total,
        'receipt_total': receipt_total,
        'booking_options': booking_options,
    })

@login_required
def receipts_view(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date')
    return render(request, 'Bookings/receipts.html', {'bookings': bookings})
