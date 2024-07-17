from flask import Blueprint, render_template

bp = Blueprint("get_deals", __name__, url_prefix="/get_deals")


@bp.route("/")
def index():
    return render_template("get_deals/index.html.j2")
