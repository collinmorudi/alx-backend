#!/usr/bin/env python3
"""2-app.y"""


from flask import Flask, render_template, request
from flask_babel import Babel


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
    """Determine the best match for supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders the homepage with a welcome message."""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
