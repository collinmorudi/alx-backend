#!/usr/bin/env python3
"""
Module to create a Flask application with internationalization support.

This module sets up a Flask application that uses Flask-Babel for translation
and displays the current time based on the user's locale.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _, format_datetime
from datetime import datetime

app = Flask(__name__)


class Config:
    """Configuration for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages or use URL parameter."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders the homepage with translated content and current time."""
    current_time = format_datetime(datetime.now())
    return render_template('index.html', current_time=current_time)


if __name__ == "__main__":
    app.run()
