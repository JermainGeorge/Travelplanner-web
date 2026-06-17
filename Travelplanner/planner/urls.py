from django.urls import path
from . import views

urlpatterns =[
    path('', views.planner, name='planner-home'),
    path('about/', views.about, name='planner-about'),
    path('popular-destinations/', views.popular_destinations, name='popular-destinations'),
    path('newsletter/', views.newsletter, name='newsletter'),
  
    
    
]