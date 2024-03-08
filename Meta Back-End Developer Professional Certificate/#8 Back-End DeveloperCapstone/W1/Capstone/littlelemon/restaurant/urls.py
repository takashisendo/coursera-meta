# Define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.MenuItemView.as_view(), name='menu-items'),
    path('items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
]

