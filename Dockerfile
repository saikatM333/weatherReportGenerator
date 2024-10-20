# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Copy the requirements file into the container
COPY requirement.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Django runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
