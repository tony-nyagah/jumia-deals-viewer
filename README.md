# Jumia Deals Viewer
A simple program to view deals on Jumia.

## Commands
Scrape data with: `scrapy crawl jumia` while in the `src` folder.
Locally run the up with: `python src/backend/app.py`.
For production use Gunicorn with: `gunicorn -w 4 -b 0.0.0.0:5050 src.backend.app:app`.