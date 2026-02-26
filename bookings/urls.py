from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('create/', views.create_booking, name='create'),
    path('<int:pk>/action/', views.booking_action, name='action'),
    path('my/', views.client_bookings, name='my_bookings'),
]
