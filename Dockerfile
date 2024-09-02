# Use an official Python image as a base
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY src/ .

# Expose the port for the production site
EXPOSE 5050

# Run the command to delete the existing SQLite database
RUN rm -f src/jumia.db

# Run the Scrapy spider
RUN cd src && scrapy crawl jumia

# Run the command to start the production site using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5050", "src.backend.app:app"]