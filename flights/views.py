from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightSerializer, BookingSerializer
from django.utils import timezone

class FlightView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class BookingView(ListAPIView):
    queryset = Booking.objects.filter(date__gte=timezone.now())
    serializer_class = BookingSerializer
