# website/__init__.py
from flask import Flask
from .home import home

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home, url_prefix='/')
    return app
