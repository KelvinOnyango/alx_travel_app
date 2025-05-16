from django.contrib import admin
from .models import Destination, Booking

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price', 'available')
    list_filter = ('available', 'created')
    search_fields = ('name', 'location', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'destination', 'travel_date', 'status')
    list_filter = ('status', 'travel_date')
    search_fields = ('customer_name', 'customer_email', 'destination__name')
