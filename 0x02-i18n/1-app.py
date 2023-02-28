#!/usr/bin/env python3
"""start babel"""

from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)


class Config(object):
    """Language"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app.config.from_object(Config)

babel = Babel(app)


@app.route("/", strict_slashes=False)
def hello():
    """Hello world!"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
