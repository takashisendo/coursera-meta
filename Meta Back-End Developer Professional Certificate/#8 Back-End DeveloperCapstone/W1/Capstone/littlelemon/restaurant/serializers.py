from rest_framework import serializers
from .models import Menu  # Import the Menu model from your models.py
from .models import Booking  # Import the Booking model from models.py within the same app

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  # Specify the model from which to create the serializer
        fields = '__all__'  # Specify which fields to include. Use '__all__' to include all fields
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Specify the model associated with this serializer
        fields = '__all__'  # Include all fields from the model in the serializer
