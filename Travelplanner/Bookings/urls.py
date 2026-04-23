from django.urls import path
from . import views

urlpatterns =[
    
    path('bookings/', views.bookings, name='nav-bookings'),
    path('receipts/', views.receipts_view, name='receipts'),
]   
