import os
from pathlib import Path
import subprocess

import click
import sqlite3

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from jinja2 import StrictUndefined

app = Flask(__name__)
CORS(app)
app.jinja_env.undefined = StrictUndefined


def get_existing_db():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__name__)), "jumia_deals.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute("select * from deals")
    deals = cursor.fetchall()

    deals_list = []
    for deal in deals:
        deal_dict = {
            "product_name": deal[0],
            "product_price": deal[1],
            "product_image": deal[2],
            "old_price": deal[3],
            "product_link": deal[4],
        }
        deals_list.append(deal_dict)

    return jsonify(deals_list)


def render_deals_context(deals):
    deals_list = deals.get_json()
    page = request.args.get("page", 1, type=int)
    items_per_page = 12
    total_pages = (len(deals_list) + items_per_page - 1) // items_per_page

    if page < 1 or page > total_pages:
        return "Invalid page number."

    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    paginated_deals = deals_list[start_index:end_index]

    # Calculate the range of pages to display
    max_visible_pages = 7
    half_visible_pages = max_visible_pages // 2
    start_page = max(1, page - half_visible_pages)
    end_page = min(total_pages, start_page + max_visible_pages - 1)

    # Adjust start_page if end_page is at the maximum
    if end_page == total_pages:
        start_page = max(1, end_page - max_visible_pages + 1)

    page_range = range(start_page, end_page + 1)

    return {
        "context": paginated_deals,
        "page": page,
        "total_pages": total_pages,
        "page_range": page_range,
    }


@app.route("/fetch_deals")
def fetch_deals():
    scrapy_config_path = Path(__file__).parent.absolute()
    subprocess.run(["scrapy", "crawl", "jumia"], cwd=scrapy_config_path, check=True)

    deals = get_existing_db()
    context = render_deals_context(deals)
    return render_template("index.html.j2", **context)


@app.route("/")
def index():
    deals = get_existing_db()
    context = render_deals_context(deals)
    return render_template("index.html.j2", **context)


@click.command()
@click.option(
    "--debug", is_flag=True, default=False, help="enable auto reload and debugging"
)
def main(debug: bool):
    app.run(debug=debug, port=5050)


if __name__ == "__main__":
    main()
