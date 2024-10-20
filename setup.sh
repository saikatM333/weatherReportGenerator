#!/bin/bash

# Step 1: Introduction
echo "----------------------------"
echo " Django Project Setup Script "
echo "----------------------------"
echo "This script will set up your Django project environment."

# Step 2: Create Virtual Environment
echo "Creating a virtual environment..."
python -m venv env

# Step 3: Activate Virtual Environment
echo "Activating the virtual environment..."
source env/bin/activate

# Step 4: Install Dependencies
echo "Installing required packages..."
pip install -r requirement.txt

# Step 5: Set Up Environment Variables
echo "Creating .env file with required environment variables..."

# Prompt user for inputs
read -p "Enter your SECRET_KEY (or press enter to generate one): " SECRET_KEY
read -p "Enter your API_KEY: " API_KEY


# Generate a random secret key if not provided
if [ -z "$SECRET_KEY" ]; then
  SECRET_KEY=$(openssl rand -hex 32)
  echo "Generated SECRET_KEY: $SECRET_KEY"
fi

# Write to .env file
echo "SECRET_KEY=\"$SECRET_KEY\"" > .env
echo "API_KEY=\"$API_KEY\"" >> .env

echo ".env file created successfully."

# Step 6: Apply Migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate



# Step 8: Start the Django Development Server
echo "Starting the Django development server..."
echo "first url for api testing - GET http://127.0.0.1:8000/api/weather/"
echo "secound url for api testing  -GET  http://127.0.0.1:8000/api/weather/daily_summary/"
echo "third url for api testing - GET http://127.0.0.1:8000/api/weather/name/Delhi"
echo "data collected for only this cities "Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad" "
python manage.py runserver

echo "----------------------------"
echo "Setup is complete! Your server is running at http://127.0.0.1:8000/"

echo "To stop the server, press CTRL+C."
echo "----------------------------"
