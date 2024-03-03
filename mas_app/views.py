from django.shortcuts import render,redirect
from .models import Mytable

# to show the home.html


def create(requests):
    data = Mytable()
    data.name = requests.POST.get("name")
    data.age = requests.POST.get("age")
    data.email = requests.POST.get("email")
    data.password = requests.POST.get("password")
    data.gender = requests.POST.get("gender")
    data.save()

    return redirect('/mas/home')

def home(requests):
    myat_chan_data = Mytable.objects.raw("select * from mas_app_mytable")
    return render(requests, 'home.html',{"data":myat_chan_data})

def about(requests):
    return render(requests,'aboutus.html')

def contact(requests):
    return render(requests,'contact.html')
