import os
from flask import Flask, redirect, render_template, render_template_string, request, Blueprint, session

from application.util.general import generate, invalid_chars
from application.util.database import Database
from application.util.scanner import scan_directory

web = Blueprint("web", __name__)

def auth_middleware(func):
  def check_user(*args, **kwargs):
    db_session = Database()

    if not session.get("loggedin"):
      if request.args.get("token") and db_session.check_token(request.args.get("token")):
        return func(*args, **kwargs)
      else:
        return redirect("/login")

    return func(*args, **kwargs)

  check_user.__name__ = func.__name__
  return check_user


@web.route("/", methods=["GET"])
def index():
  return redirect("/home")


@web.route("/login", methods=["GET"])
def login():
  username = request.args.get("username")
  password = request.args.get("password")

  if not username or not password:
    return render_template("login.html", title="log-in")

  db_session = Database()
  user_valid = db_session.check_user(username, password)

  if not user_valid:
    return render_template("error.html", title="error", error="invalid username/password"), 401

  session["loggedin"] = True
  return redirect("/home")


@web.route("/register", methods=["GET"])
def register():
  username = request.args.get("username")
  password = request.args.get("password")

  if not username or not password:
    return render_template("register.html", title="register")

  db_session = Database()
  token = generate(16)
  user_valid = db_session.create_user(username, password, token)
  
  if not user_valid:
    return render_template("error.html", title="error", error="user exists"), 401

  return render_template("error.html", title="success", error=f"User created with token: {token}"), 200


@web.route("/logout", methods=["GET"])
def logout():
    session.pop("loggedin", default=None)
    return redirect("/login")


@web.route("/home", methods=["GET", "POST"])
@auth_middleware
def feed():
  directory = request.args.get("directory")
  
  if not directory:
    dirs = os.listdir(os.getcwd())
    return render_template("index.html", title="home", dirs=dirs)

  if any(char in directory for char in invalid_chars):
    return render_template("error.html", title="error", error="invalid directory"), 400

  try:
    with open("./application/templates/scan.html", "r") as file:
        template_content = file.read()
        results = scan_directory(directory)
        template_content = template_content.replace("{{ results.date }}", results["date"])
        template_content = template_content.replace("{{ results.scanned_directory }}", results["scanned_directory"])
        return render_template_string(template_content, results=results)
        
  except Exception as e:
    return render_template("error.html", title="error", error=e), 500