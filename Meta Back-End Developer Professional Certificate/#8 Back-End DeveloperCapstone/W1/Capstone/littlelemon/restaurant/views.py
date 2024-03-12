from django.shortcuts import render
from .models import Menu
from .models import Booking
from .serializers import MenuSerializer  # Ensure you have a serializer for the Menu model
from rest_framework import viewsets
from .serializers import BookingSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]


# Assuming you have MenuItem model and MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Fetches all Booking objects
    serializer_class = BookingSerializer  # Specifies to use BookingSerializer for serialization
    permission_classes = [AllowAny]


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # Example: only allow access to admins
