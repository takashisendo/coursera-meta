from rest_framework import serializers
from .models import Menu  # Import the Menu model from your models.py
from .models import Booking  # Import the Booking model from models.py within the same app
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  # Specify the model from which to create the serializer
        fields = '__all__'  # Specify which fields to include. Use '__all__' to include all fields
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Specify the model associated with this serializer
        fields = '__all__'  # Include all fields from the model in the serializer

# restaurant/serializers.py
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # ['id', 'username', 'email', 'first_name', 'last_name']  # Specify the fields to include
        # Alternatively, you can use fields = '__all__' to include all fields.

