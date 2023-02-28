#!/usr/bin/env python3
"""start a flask app"""

from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to Holberton"
