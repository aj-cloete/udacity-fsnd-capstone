import random

import pytest

from app import create_app
from database import db
from testing.factories import ActorFactory, MovieFactory


@pytest.fixture(scope="module")
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
        yield app
        db.session.close()
        db.drop_all()
        db.session.remove()


@pytest.fixture(scope="module")
def _db():
    """
    see https://pypi.org/project/pytest-flask-sqlalchemy/
    """
    return db


@pytest.fixture(scope="function")
def actors():
    actors = ActorFactory.create_batch(5)
    return actors


@pytest.fixture(scope="function")
def actor(actors):
    actor = random.choice(actors)
    return actor


@pytest.fixture(scope="function")
def movies():
    movies = MovieFactory.create_batch(5)
    return movies


@pytest.fixture(scope="function")
def movie(movies):
    movie = random.choice(movies)
    return movie
