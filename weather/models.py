# weather/models.py
from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    temp = models.FloatField()
    feels_like = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Weather Data'
        verbose_name_plural = 'Weather Data'

    def __str__(self):
        return f"{self.city} - {self.main} - {self.temp}°C"
