#!/usr/bin/python3

import os
import subprocess

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

CMD_PATH = os.getenv("CMD_PATH", "./main")

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return "File not in request", 400

    file = request.files["file"]
    is_mp3 = file.filename.endswith(".mp3")

    if not is_mp3:
        return "File is not mp3", 400

    filepath = os.path.join("/tmp", "test.mp3")
    file.save(filepath)

    return redirect("/")


@app.route("/play", methods=["GET"])
def play():
    sp = subprocess.run([CMD_PATH], capture_output=True, text=True)
    return sp.stdout, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1337, debug=True)