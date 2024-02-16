from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuModel, BookingModel
from .serializers import BookingSerializer, MenuSerializers
from rest_framework import status, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializers
    permission_classes = [IsAuthenticated]


class SingleMenuItemsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializers
    permission_classes = [IsAuthenticated]


class BookingViewSet(ModelViewSet):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class BookingsView(generics.ListCreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class SingleBookingsView(generics.RetrieveUpdateDestroyAPIView):
    queryset =BookingModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
