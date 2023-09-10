from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

from config import Config
from .database.database import db, base
import app.models


def setup_database(app):
    with app.app_context():
        base.metadata.create_all(db)


def setup_swagger(app):
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yaml'
    swagger_bp = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Bored API Wrapper"})
    app.register_blueprint(swagger_bp, url_prefix=SWAGGER_URL)


def create_app():
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(Config)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    setup_database(app)
    setup_swagger(app)

    from .views import wrapper_bp
    app.register_blueprint(wrapper_bp)

    return app
