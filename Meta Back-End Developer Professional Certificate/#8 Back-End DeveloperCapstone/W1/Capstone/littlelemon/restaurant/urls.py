# Define URL route for index() view
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet
from django.urls import path
from .views import UserListView

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.MenuItemView.as_view(), name='menu-items'),
    path('items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('', include(router.urls)),
    path('users/', UserListView.as_view(), name='user-list'),
]
