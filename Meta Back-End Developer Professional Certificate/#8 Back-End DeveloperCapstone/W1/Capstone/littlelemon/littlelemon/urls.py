"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import List, Any

from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views
from restaurant import views  # Make sure this import correctly points to your app's views
from django.urls import include, path


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)  # Register BookingViewSet with 'tables' as the route

urlpatterns: list[Any] = [
   path('admin/', admin.site.urls),
   path('restaurant/', include('restaurant.urls')),  # Corrected to include as a string
   path('restaurant/menu/', include(router.urls)),
   path('restaurant/booking/', include(router.urls)),
   # Include the router URLs
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.authtoken')),
   path('api/', include('restaurant.urls')),
   path('api-token-auth/', auth_views.obtain_auth_token),
]

