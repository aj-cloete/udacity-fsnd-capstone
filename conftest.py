import flask_migrate
import pytest

from app import create_app
from database import db

# from flask_jwt_extended import create_access_token


@pytest.fixture(scope="module")
def app():
    app = create_app()
    with app.app_context():
        flask_migrate.upgrade()
        yield app
        db.session.close()
        db.drop_all()
        db.session.close()


@pytest.fixture(scope="module")
def _db():
    """
    see https://pypi.org/project/pytest-flask-sqlalchemy/
    """
    return db
