from django.db import models
from django.contrib.auth.models import User


class PhotographerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='photographer_profile')
    bio = models.TextField(blank=True)
    hourly_rate = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.user.username} - Photographer"


class Availability(models.Model):
    photographer = models.ForeignKey(PhotographerProfile, on_delete=models.CASCADE, related_name='availabilities')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['date', 'start_time']

    def __str__(self):
        return f"{self.photographer.user.username} available {self.date} {self.start_time}-{self.end_time}"
