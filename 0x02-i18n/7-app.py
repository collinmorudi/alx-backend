#!/usr/bin/env python3
"""7-app"""


from flask import Flask, render_template, request
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError

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
    """Determine the best match for supported languages
    or use URL parameter."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Determine the appropriate time zone or default to UTC."""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            # Validate timezone using pytz
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass  # Ignore invalid timezone and fall back to default

    # Simulate retrieving a user time zone setting
    # (for example, from a database)
    user_timezone = "UTC"
    return user_timezone


@app.route('/')
def index():
    """Renders the homepage with translated content."""
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run()
