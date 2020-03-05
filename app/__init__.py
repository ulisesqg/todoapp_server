from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():

    # App initialization
    app = Flask(__name__)
    app.config.from_object("config")

    # Init Apps
    db.init_app(app)
    migrate.init_app(app, db)

    # Routes
    @app.route("/")
    def index():
        return jsonify({"message": "Hello World!"})

    return app
