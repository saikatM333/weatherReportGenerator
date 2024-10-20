# weatherReport/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from weather.tasks import fetch_weather_data
import logging

# Set up logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def start_scheduler():
    scheduler = BackgroundScheduler()
    
    # Schedule the job to fetch weather data every 5 minutes
    scheduler.add_job(fetch_weather_data, 'interval', minutes=1)
    
    # Start the scheduler
    scheduler.start()
    logger.info("Scheduler started!")
