from flask import current_app as _app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session

from common.models import BaseModel, metadata
from instance import config

Session = scoped_session(
    lambda: _app.extensions["sqlalchemy"].db.session,
    scopefunc=lambda: _app.extensions["sqlalchemy"].db.session,
)


class ApiModel(BaseModel):
    def insert(self):
        """
        inserts the instance into the database
        """
        Session.add(self)
        Session.commit()

    def delete(self):
        """
        deletes the instance from the database
        """
        Session.delete(self)
        Session.commit()

    def update(self, data={}, **kwargs):
        """
        updates the instance details in the database
        optionally takes a dict in data with which to update the instance.
        kwargs can also be used to update information on instance.
        EXAMPLE
            drink = Drink.query.filter(Drink.uuid == uuid).one_or_none()
            drink.title = 'Black Coffee'
            drink.update()
        """
        update_data = data.update(**kwargs) if kwargs else data
        if update_data:
            for key, value in update_data:
                if hasattr(self, key):
                    setattr(self, key, update_data[key])
        Session.commit()


def setup_pg_extensions(engine):
    """
    Run raw SQL in the database to set up extensions
    """
    pgcrypto = "CREATE EXTENSION IF NOT EXISTS pgcrypto"
    extensions = [
        pgcrypto,
    ]
    with engine.connect():
        engine.execute(text(";\n".join(extensions)).execution_options(autocommit=True))


db = SQLAlchemy(model_class=ApiModel, metadata=metadata)
test_engine = create_engine(config.Testing.SQLALCHEMY_DATABASE_URI)
