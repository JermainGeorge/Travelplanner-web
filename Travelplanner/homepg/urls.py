from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name='homepg-home'),
    path("about/", views.about, name='homepg-about'),
   
]