#!/usr/bin/env python3
"""using locale"""

from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Language"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


@babel.localeselector
def get_locale():
    """get locale"""
    return request.accept_languages.best_match(app.config(['LANGUAGES']))


@app.route("/", strict_slashes=False)
def hello():
    """hello world"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
