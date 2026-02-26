from django.urls import path
from . import views

app_name = 'photographers'

urlpatterns = [
    path('', views.list_photographers, name='list'),
    path('<int:pk>/', views.profile_detail, name='detail'),
    path('dashboard/', views.photographer_dashboard, name='dashboard'),
]
