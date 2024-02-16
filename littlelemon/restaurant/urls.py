from django.urls import path, include
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("menu", views.MenuItemsView.as_view(), name='menu-detail'),
    path("menu/<int:pk>", views.SingleMenuItemsView.as_view(), name='menu-detail'),

    path("booking", views.BookingsView.as_view(), name='booking-list'),
    path("booking/<int:pk>", views.SingleBookingsView.as_view(), name='booking-detail')
]
