from flask import Blueprint, render_template

index_bp = Blueprint(
    "index",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static",
)


@index_bp.route("/", methods=["GET"])
def index():
    return render_template("public/index.html")
