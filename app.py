import click
import sqlite3

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Hello, world!"


@app.route("/api/deals")
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


@click.command()
@click.option(
    "--debug", is_flag=True, default=False, help="enable auto reload and debugging"
)
def main(debug: bool):
    app.run(debug=debug)


if __name__ == "__main__":
    main()
