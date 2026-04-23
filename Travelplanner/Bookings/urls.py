from django.urls import path
from . import views

urlpatterns =[
    
    path('bookings/', views.bookings, name='Bookings-bookings'),
    path('book/', views.create_booking, name='create-booking'),
    path('receipts/', views.receipts_view, name='receipts'),
]   
