from django.contrib import admin
from .models import Menu
from .models import Booking
# Import the Menu model from models.py

# Register the Menu model
admin.site.register(Menu)
admin.site.register(Booking)