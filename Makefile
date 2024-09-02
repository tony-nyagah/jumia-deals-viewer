# Define the directory containing the scrapy project
SCRAPY_DIR = src/jumia_deals_viewer

# Define the command to run the scrapy spider
scrape_data:
	cd $(SCRAPY_DIR) && scrapy crawl jumia

# Define the command to run the Flask application using gunicorn
run:
	cd $(SCRAPY_DIR) && gunicorn -w 4 -b 0.0.0.0:5050 backend.app:app

# Define the command to delete the existing SQLite database
clean:
	rm -f $(SCRAPY_DIR)/jumia_deals.db
