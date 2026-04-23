from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking




@login_required
def  bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            return redirect('receipts')  # go to receipts page
    else:
        form = BookingForm()

    return render(request, 'Bookings/bookings.html', {'form': form})


@login_required
def receipts_view(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'Bookings/receipts.html', {'bookings': bookings})