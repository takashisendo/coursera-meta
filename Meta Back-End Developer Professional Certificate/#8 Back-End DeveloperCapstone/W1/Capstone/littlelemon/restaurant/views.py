from django.shortcuts import render
from .models import Menu
from .serializers import MenuSerializer
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # Fetches all Booking objects
    serializer_class = BookingSerializer  # Specifies to use BookingSerializer for serialization

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # Example: only allow access to admins
