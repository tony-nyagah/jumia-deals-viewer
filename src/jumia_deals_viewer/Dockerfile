# Use an official Python image as a base
FROM python:3.12-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Change directory to src/jumia_deals_viewer
WORKDIR /app/src/jumia_deals_viewer

# Run the application using gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5050", "backend.app:app"]