from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('reservations/', views.reservations, name='reservations'),
    path('contact/', contact, name='contact'),
]