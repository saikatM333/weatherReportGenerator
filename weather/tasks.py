# weather/tasks.py

import requests
from django.conf import settings
from .models import WeatherData
from datetime import datetime
import logging
import os
from dotenv import load_dotenv
load_dotenv()
logger = logging.getLogger(__name__)

def fetch_weather_data():
    logger.info(f"Fetching weather data at {datetime.now()}...")
    cities = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
    api_key = os.getenv('API_KEY')
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    for city in cities:
        
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # Temperature in Celsius
        }
        
        response = requests.get(base_url, params=params);
        
        if response.status_code == 200:
            print(response.status_code)
            data = response.json()
            main = data.get('weather', [{}])[0].get('main', '')
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            print(city)
            WeatherData.objects.create(
                city=city,
                main=main,
                temp=temp,
                feels_like=feels_like,
            )
            print("featching done")
        else:
            print(response.status_code)
            print("there is some issue")



def check_alerts():
    alerts = []
    threshold_temp = 35  # Example threshold
    latest_data = WeatherData.objects.filter(temp__gt=threshold_temp).order_by('-timestamp')[:2]

    if len(latest_data) >= 2:
        alerts.append(f"Temperature exceeded {threshold_temp}°C in {latest_data[0].city}.")
    
    # Display or log alerts as needed.
    if alerts:
        print("Alerts:", alerts)
