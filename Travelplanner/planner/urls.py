from django.urls import path
from . import views

urlpatterns =[
    path('', views.planner, name='planner-home'),
    path('about/', views.about, name='planner-about'),
    path('bookings/', views.bookings, name='planner-bookings'),
    path('profile/', views.profile, name='planner-profile')
    
]