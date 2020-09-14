from rest_framework import serializers
from .models import Flight, Booking

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        exclude = ['miles',]



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['flight', 'date', 'id']
