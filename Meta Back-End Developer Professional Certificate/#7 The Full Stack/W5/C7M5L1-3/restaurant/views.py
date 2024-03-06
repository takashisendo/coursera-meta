# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
from datetime import datetime
from .models import Booking


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
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

@csrf_exempt
@require_http_methods(["GET", "POST"])  # Ensures only GET and POST requests are handled
def bookings(request):
    if request.method == 'POST':
        # Try-except block to handle potential errors in JSON processing or field extraction
        try:
            data = json.loads(request.body.decode('utf-8'))  # Correct way to parse JSON data from the request body

            # Check if a booking with the given reservation date and slot already exists
            exist = Booking.objects.filter(
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot']
            ).exists()

            if not exist:
                # If no existing booking is found, create a new Booking object and save it
                booking = Booking(
                    first_name=data['first_name'],
                    reservation_date=data['reservation_date'],
                    reservation_slot=data['reservation_slot'],
                )
                booking.save()
                return JsonResponse({"success": True}, status=201)  # Return success response
            else:
                # If a booking already exists, return an error message
                return JsonResponse({"error": 1}, content_type='application/json', status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)  # Handle JSON parsing error
        except KeyError as e:
            # Handle missing required data fields by returning an appropriate error message
            return JsonResponse({"error": f"Missing field: {str(e)}"}, status=400)

    # Handle GET request to retrieve bookings for a specified date or today's date by default
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    # Return the serialized bookings for the requested date
    return HttpResponse(booking_json, content_type='application/json')

