# from django.http import HttpResponse
from django.shortcuts import render

from .models import Menu
from django.core.serializers import serialize
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from .forms import BookingForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add code for the bookings() view
# Corrected bookings view function
def bookings(request):
    # Create a variable called date
    date = request.GET.get('date', datetime.today().date())

    # Filter bookings based on the provided date
    bookings = Booking.objects.filter(date=date) # Assuming Booking model has a 'date' field to filter on

    # Serialize the filtered bookings
    booking_json = serialize('json', bookings)

    # Return the render() function with serialized bookings data
    return render(request, "bookings.html", {"bookings": booking_json})


def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 