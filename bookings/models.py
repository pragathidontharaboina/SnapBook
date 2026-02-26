from django.db import models
from django.contrib.auth.models import User
from photographers.models import PhotographerProfile, Availability


class Booking(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
    ]

    photographer = models.ForeignKey(PhotographerProfile, on_delete=models.CASCADE, related_name='bookings')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    availability = models.ForeignKey(Availability, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} {self.photographer.user.username} by {self.client.username} on {self.date}"
