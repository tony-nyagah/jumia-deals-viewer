# Jumia Deals Viewer
A simple program to view deals on Jumia.

## Installation
### Run Locally
First create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then run the application using commands in the `Makefile`, this should work under a Linux or WSL environment:
```bash
# scrape data from Jumia
make scrape_data 
# view the scraped data on `localhost:5050`
make run
```
The scraped data is put in the file `jumia_deals.db` under `src/jumia_deals_viewer`.

### Run in Docker
Build the image using the `Dockerfile`:
```bash
docker build -t jumia_deals_viewer .
```

Run the image using the `Dockerfile`:
```bash
docker run -p 5050:5050 jumia_deals_viewer
```
