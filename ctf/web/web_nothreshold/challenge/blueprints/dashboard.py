from flask import Blueprint, render_template, request, jsonify, session, redirect
from app.config import Config

dashboard_bp = Blueprint("dashboard", __name__, template_folder="templates")

def requires_authentication(func):
    def wrapper(*args, **kwargs):
        if session.get("authenticated"):
            return func(*args, **kwargs)
        else:
            return redirect("/auth/login")

    return wrapper


@dashboard_bp.route("/dashboard", methods=["GET"])
@requires_authentication
def dash():
    return render_template("private/dashboard.html", flag=Config.FLAG)
