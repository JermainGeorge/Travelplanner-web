from django.urls import path
from . import views

urlpatterns =[
    
    path('bookings/', views.bookings, name='Bookings-bookings'),
    
    
]