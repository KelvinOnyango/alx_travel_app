from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Destination, Booking
from .serializers import DestinationSerializer, BookingSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    @action(detail=True, methods=['post'])
    def book(self, request, pk=None):
        destination = self.get_object()
        if not destination.available:
            return Response(
                {'error': 'This destination is not available'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(destination=destination)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        booking = self.get_object()
        new_status = request.data.get('status')
        if new_status not in [s[0] for s in Booking.STATUS_CHOICES]:
            return Response(
                {'error': 'Invalid status'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        booking.status = new_status
        booking.save()
        return Response(self.get_serializer(booking).data)
