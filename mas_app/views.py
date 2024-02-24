from django.shortcuts import render

# to show the home.html
def home(requests):
    return render(requests,'home.html')

def about(requests):
    return render(requests,'aboutus.html')

def contact(requests):
    return render(requests,'contact.html')
