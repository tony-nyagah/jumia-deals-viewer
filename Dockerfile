# Use an official Python image as a base
FROM python:3.12-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Change directory to src/jumia_deals_viewer
WORKDIR /app/src/jumia_deals_viewer

# Run the scrapy command to scrape data and store it in the sqlite database file
RUN scrapy crawl jumia
# Run the application using gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5050", "backend.app:app"]