from flask import Flask
from flask_cors import CORS
from flask_environments import Environments
from flask_migrate import Migrate

from database import db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    migrate = Migrate(app, db)  # noqa
    env = Environments(app)
    env.from_object("instance.config")
    CORS(app)
    db.init_app(app)

    return app
