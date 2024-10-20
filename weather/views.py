# weather/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now, timedelta
from .models import WeatherData
from .serializers import WeatherDataSerializer
from django.db.models import Avg, Max, Min, Count


class WeatherDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

    def list(self, request, *args, **kwargs):
        # Get the latest weather data entry for each city
        latest_weather = WeatherData.objects.values('city').annotate(max_id=Max('id'))

        # Create a list to hold the latest weather entries
        latest_weather_entries = []

        for entry in latest_weather:
            # Fetch the latest weather data using the max id for each city
            latest_entry = WeatherData.objects.get(id=entry['max_id'])
            latest_weather_entries.append(latest_entry)

        # Serialize the latest data for each city
        serializer = self.get_serializer(latest_weather_entries, many=True)
        
        # Return the serialized data
        return Response(serializer.data)

    def retrieve(self, request, city_name=None, *args, **kwargs):
        # Get the latest weather data for the specific city by name
        latest_weather = WeatherData.objects.filter(city=city_name).order_by('-timestamp')  # Replace 'created_at' with your actual timestamp field name
        
        if not latest_weather.exists():
            return Response({"detail": "Not found."}, status=404)

        # Get the most recent entry
        latest_entry = latest_weather.first()

        # Serialize the latest entry
        serializer = self.get_serializer(latest_entry)

        # Return the serialized data
        return Response(serializer.data)

    @action(detail=False)
    def daily_summary(self, request):
        today = now().date()
        daily_data = WeatherData.objects.filter(timestamp__date=today)
        avg_temp = daily_data.aggregate(Avg('temp'))['temp__avg']
        max_temp = daily_data.aggregate(Max('temp'))['temp__max']
        min_temp = daily_data.aggregate(Min('temp'))['temp__min']
        dominant_condition = daily_data.values('main').annotate(count=Count('main')).order_by('-count').first()

        return Response({
            'date': today,
            'average_temperature': avg_temp,
            'max_temperature': max_temp,
            'min_temperature': min_temp,
            'dominant_weather_condition': dominant_condition.get('main') if dominant_condition else 'N/A'
        })
