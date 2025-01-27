from flask import Blueprint, render_template, request, jsonify, redirect
from app.database import *
import random
import string
import uwsgi

login_bp = Blueprint("login", __name__, template_folder="templates")


def set_2fa_code(d):
    uwsgi.cache_del("2fa-code")
    uwsgi.cache_set(
        #"2fa-code", "".join(random.choices(string.digits, k=d)), 300 # valid for 5 min
        "2fa-code", "1234", 3000 # valid for 5 min
    ) 


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    print('Debug: Login!')
    if request.method == "POST":
        print('Debug: PSOT Login!')
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return render_template("public/login.html", error_message="Username or password is empty!"), 400
        try:
            user = query_db(
                f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'",
                one=True,
            )
            print('Debug: Queried DB!')
            if user is None:
                print('Debug: User None!')
                return render_template("public/login.html", error_message="Invalid username or password"), 400

            set_2fa_code(4)
            print('Debug: Redirect to Verify-2fa from Login!')

            return redirect("/auth/verify-2fa")
        finally:
            close_db()
    return render_template("public/login.html")
