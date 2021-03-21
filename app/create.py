from flask import Flask
from flask_cors import CORS
from flask_environments import Environments
from flask_migrate import Migrate
from flask_restful import Api

from api.routes import register_blueprints
from common.schemas import marshmallow
from database import models  # noqa ## so alembic is aware of all the models
from database import db
from database.db import setup_pg_extensions

migrate = Migrate(compare_type=True)
env = Environments()
cors = CORS(resources={r"/*": {"origins": "*"}})


def init_plugins(app):
    """Initialise plugins that need to run BEFORE app context is activated
    Args:
        app: flask app with no activated context
    """
    from database import models  # noqa

    env.init_app(app)
    cors.init_app(app)
    marshmallow.init_app(app)


def init_plugins_with_context(app, db):
    """Initialise plugins that need to run AFTER app context is activated
    Args:
        app: flask app within active context
    """
    env.from_object("instance.config")
    db.init_app(app)
    migrate.init_app(app, db)
    setup_pg_extensions(db.engine)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    api = Api(app)
    init_plugins(app)
    with app.app_context():
        register_blueprints(api)
        init_plugins_with_context(app, db)
    return app
