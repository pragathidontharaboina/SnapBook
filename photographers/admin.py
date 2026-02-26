from django.contrib import admin
from .models import PhotographerProfile, Availability


@admin.register(PhotographerProfile)
class PhotographerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'hourly_rate')


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('photographer', 'date', 'start_time', 'end_time', 'is_active')
    list_filter = ('photographer', 'date')
