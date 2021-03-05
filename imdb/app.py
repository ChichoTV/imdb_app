from flask import Flask
import sqlalchemy

from imdb.blueprints.page.views import page
from imdb.extensions import debug_toolbar, db

def create_app():
    """
    Create a Flask application using the app factory pattern.
        asdsadd
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)

    extensions(app)
    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    debug_toolbar.init_app(app)
    db.init_app(app)
    return None
