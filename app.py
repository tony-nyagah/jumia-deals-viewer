import click
import sqlite3

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from jinja2 import StrictUndefined

from blueprints import get_deals

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined

app.register_blueprint(get_deals.bp)


# @app.route("/api/deals")
def get_deals():
    connection = sqlite3.connect("deals.db")
    cursor = connection.cursor()
    cursor.execute("select * from deals")
    deals = cursor.fetchall()
    connection.close()

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


@app.route("/")
def index():
    deals = get_deals()
    deals_list = deals.get_json()

    page = request.args.get("page", 1, type=int)
    items_per_page = 12
    total_pages = (len(deals_list) + items_per_page - 1) // items_per_page

    if page < 1 or page > total_pages:
        return "Invalid page number."

    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    paginated_deals = deals_list[start_index:end_index]

    return render_template(
        "index.html.j2", context=paginated_deals, page=page, total_pages=total_pages
    )


@click.command()
@click.option(
    "--debug", is_flag=True, default=False, help="enable auto reload and debugging"
)
def main(debug: bool):
    app.run(debug=debug, port=5050)


if __name__ == "__main__":
    main()
