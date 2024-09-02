# Jumia Deals Viewer
A simple program to view deals on Jumia.

## Commands
### Run Locally
First of all go into the `src/jumia_deals_viewer` directory:
* `cd src/jumia_deals_viewer`

1. Scrape data by running: 
    * `scrapy crawl jumia` - to run a scraper and store the data in a sqlite database file.

2. Locally run the up with: `python backend/app.py`.

To use the production server, run: `gunicorn -w 4 -b 0.0.0.0:5050 backend.app:app`.

To manually delete the existing SQLite database: `rm -f jumia_deals.db`.