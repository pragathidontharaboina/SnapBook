from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from photographers.models import Availability, PhotographerProfile


@login_required
def create_booking(request):
    if request.method == 'POST':
        availability_id = request.POST.get('availability_id')
        availability = get_object_or_404(Availability, pk=availability_id)
        profile = availability.photographer
        # Create booking request
        booking = Booking.objects.create(
            photographer=profile,
            client=request.user,
            availability=availability,
            date=availability.date,
            start_time=availability.start_time,
            end_time=availability.end_time,
            status='requested'
        )
        messages.success(request, 'Booking requested')
        return redirect('photographers:detail', pk=profile.pk)

    return redirect('/')


@login_required
def booking_action(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    # only photographer who owns the profile may act
    if request.user != booking.photographer.user:
        messages.error(request, 'Not authorized')
        return redirect('/')

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'accept':
            booking.status = 'accepted'
            booking.save()
            # mark availability inactive
            if booking.availability:
                booking.availability.is_active = False
                booking.availability.save()
            messages.success(request, 'Booking accepted')
        elif action == 'reject':
            booking.status = 'rejected'
            booking.save()
            messages.success(request, 'Booking rejected')

    return redirect('photographers:dashboard')


@login_required
def client_bookings(request):
    bookings = Booking.objects.filter(client=request.user).order_by('-created_at')
    return render(request, 'bookings/list.html', {'bookings': bookings})
