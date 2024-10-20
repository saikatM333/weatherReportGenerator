# weather/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WeatherDataViewSet

router = DefaultRouter()
router.register(r'weather', WeatherDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('weather/name/<str:city_name>/', WeatherDataViewSet.as_view({'get': 'retrieve'}), name='weather-by-name'),
]
