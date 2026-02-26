from django.shortcuts import render, get_object_or_404, redirect
from .models import PhotographerProfile, Availability
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


def list_photographers(request):
    profiles = PhotographerProfile.objects.select_related('user').all()
    return render(request, 'photographers/list.html', {'profiles': profiles})


def profile_detail(request, pk):
    profile = get_object_or_404(PhotographerProfile, pk=pk)
    availabilities = profile.availabilities.filter(is_active=True)
    return render(request, 'photographers/detail.html', {'profile': profile, 'availabilities': availabilities})


@login_required
def photographer_dashboard(request):
    # assumes logged in user is a photographer
    try:
        profile = request.user.photographer_profile
    except PhotographerProfile.DoesNotExist:
        messages.error(request, "You are not a photographer")
        return redirect('/')
    from bookings.models import Booking

    bookings = Booking.objects.filter(photographer=profile).order_by('-created_at')
    return render(request, 'photographers/dashboard.html', {'profile': profile, 'bookings': bookings})
