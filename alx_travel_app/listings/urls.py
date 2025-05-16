from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'listings'

router = DefaultRouter()
router.register(r'destinations', views.DestinationViewSet, basename='destination')
router.register(r'bookings', views.BookingViewSet, basename='booking')

urlpatterns = router.urls
