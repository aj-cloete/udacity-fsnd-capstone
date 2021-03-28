from authlib.integrations.flask_client import OAuth
from flask import Flask
from flask_cors import CORS
from flask_environments import Environments
from flask_migrate import Migrate

from api.blueprints import register_blueprints as register_api_blueprints
from auth.auth import register_login_logout
from auth.blueprints import register_blueprints as register_auth_blueprints
from common.errors import init_error_handlers
from common.resources import Api
from common.schemas import marshmallow
from database import models  # noqa ## so alembic is aware of all the models
from database import db
from database.db import setup_pg_extensions

api = Api()
cors = CORS(resources={r"/*": {"origins": "*"}})
env = Environments()
migrate = Migrate(compare_type=True)
oauth = OAuth()


def init_plugins(app):
    """Initialise plugins that need to run BEFORE app context is activated
    Args:
        app: flask app with no activated context
    """
    from database import models  # noqa

    env.init_app(app)
    api.init_app(app)
    marshmallow.init_app(app)
    cors.init_app(app)
    oauth.init_app(app)
    register_login_logout(app, oauth)


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
    init_plugins(app)
    with app.app_context():
        register_api_blueprints(app)
        register_auth_blueprints(app)
        init_plugins_with_context(app, db)
        init_error_handlers(app)
    return app
