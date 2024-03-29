from rest_framework import serializers
from .models import BookingModel, MenuModel

class BookingSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='booking-detail')

    class Meta:
        model = BookingModel
        fields = ['id', 'name', 'number_of_guests', 'booking_date']


class MenuSerializers(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='menu-detail')

    class Meta:
        model = MenuModel
        fields = ['id', 'title', 'price', 'inventory']

