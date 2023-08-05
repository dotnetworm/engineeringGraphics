from flask import Flask
from .Routes.routes_api import api
from .Routes.routes_site import site

def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.register_blueprint(api)
    app.register_blueprint(site)
    return app