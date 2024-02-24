from django.urls import path
from mas_app import views



urlpatterns = [
    path('home/',views.home,name="home"),
    path('about-us/',views.about,name="about"),
    path('contact/',views.contact,name="contact")
]