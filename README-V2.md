## Jumia Deals Viewer
This project is a web application for viewing all products currently on discount on jumia.co.ke. The data is scraped using Scrapy and displayed to users using a combination of Fastapi, HTMX, AlpineJS, and TailwindCSS.

### About
This application was inspired by a hackathon organized by Data Science East. The goal is to provide users with a convenient way to access the latest deals on Jumia.

### Technologies
**Scrapy**: Used for web scraping.
**Fastapi**: Used for building the web application.
**HTMX**: Used for handling connections beween the web pages.
**AlpineJS**: Used for adding interactivity to the web pages.
**TailwindCSS**: Used for styling the web pages.

### Installation
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.

### Usage
1. Run the Scrapy spider to scrape the deals from `jumia.co.ke` with:
   - `python get_scraper_data.py`
2. Start the Fastapi application to display the scraped data to users with:
   - `uvicorn main:app --reload`
   
### Contributing
We welcome contributions from the community. If you'd like to contribute, please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgements
Data Science East Africa for organizing the hackathon that inspired this project.