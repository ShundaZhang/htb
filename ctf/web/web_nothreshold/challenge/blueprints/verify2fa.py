from flask import Blueprint, render_template, request, jsonify, session, redirect
import uwsgi

verify2fa_bp = Blueprint("verify2fa", __name__, template_folder="templates")

def requires_2fa(func):
    def wrapper(*args, **kwargs):
        if uwsgi.cache_exists("2fa-code"):
            return func(*args, **kwargs)
        else:
            return redirect("/auth/login")

    return wrapper


@verify2fa_bp.route("/verify-2fa", methods=["GET", "POST"])
@requires_2fa
def verify():
    if request.method == "POST":

        code = request.form.get("2fa-code")
        
        if not code:
            return render_template("private/verify2fa.html", error_message="2FA code is empty!"), 400

        stored_code = uwsgi.cache_get("2fa-code").decode("utf-8")

        if code == stored_code:
            uwsgi.cache_del("2fa-code")
            session["authenticated"] = True
            return redirect("/dashboard")

        else:
            return render_template("private/verify2fa.html", error_message="Invalid 2FA Code!"), 400
    return render_template("private/verify2fa.html")
