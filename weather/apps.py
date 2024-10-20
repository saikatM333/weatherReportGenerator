# weather/apps.py

from django.apps import AppConfig

class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'

    def ready(self):
        from .scheduler import start_scheduler  # Import your scheduler here
        start_scheduler()  # Start the scheduler when the app is ready
