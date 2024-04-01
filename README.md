# Jumia Deal Viewer

This project is a web application that allows users to view deals on Jumia Kenya (jumia.co.ke). It utilizes Scrapy, a powerful web scraping framework, to extract data from the Jumia website. The frontend is built using modern web technologies such as HTMX, AlpineJS, and TailwindCSS, providing a smooth and responsive user experience.

## Features

- View current deals and discounts on Jumia Kenya
- Filter deals by category, price range, or other criteria
- Sort deals based on relevance, price, or popularity
- Lightweight and efficient frontend powered by HTMX and AlpineJS
- Responsive and visually appealing design with TailwindCSS

## Prerequisites

Before running the project, ensure that you have the following installed:

- Python (version 3.6 or higher)

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/jumia-deal-viewer.git
```

2. Navigate to the project directory:

```
cd jumia-deal-viewer
```

3. Install Python dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Start the Scrapy spider to fetch data from Jumia:

```
scrapy crawl jumia
```

This will populate the database with the latest deals from Jumia.

2. Start the web server:

```
python app.py
```

3. Open your web browser and navigate to `http://localhost:5000` to access the Jumia Deal Viewer.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Scrapy](https://scrapy.org/) - The web scraping framework used in this project
- [HTMX](https://htmx.org/) - For building modern HTML experiences
- [AlpineJS](https://alpinejs.dev/) - A rugged, minimal tool for composing behavior directly in your markup
- [TailwindCSS](https://tailwindcss.com/) - A utility-first CSS framework for rapidly building custom designs