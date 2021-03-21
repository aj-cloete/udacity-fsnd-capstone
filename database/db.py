from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.orm import scoped_session

from common.models import BaseModel, metadata

Session = scoped_session(
    lambda: current_app.extensions["sqlalchemy"].db.session,
    scopefunc=lambda: current_app.extensions["sqlalchemy"].db.session,
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

    @staticmethod
    def update(self):
        """
        updates the instance details in the database
        EXAMPLE
            drink = Drink.query.filter(Drink.uuid == uuid).one_or_none()
            drink.title = 'Black Coffee'
            drink.update()
        """
        Session.commit()


def setup_pg_extensions(engine):
    pgcrypto = "CREATE EXTENSION IF NOT EXISTS pgcrypto"
    extensions = [
        pgcrypto,
    ]
    with engine.connect():
        engine.execute(text(";\n".join(extensions)).execution_options(autocommit=True))


db = SQLAlchemy(model_class=ApiModel, metadata=metadata)
