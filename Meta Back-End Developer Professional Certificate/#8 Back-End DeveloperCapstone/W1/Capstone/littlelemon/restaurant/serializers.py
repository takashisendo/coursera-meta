from rest_framework import serializers
from .models import Menu  # Import the Menu model from your models.py

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  # Specify the model from which to create the serializer
        fields = '__all__'  # Specify which fields to include. Use '__all__' to include all fields
