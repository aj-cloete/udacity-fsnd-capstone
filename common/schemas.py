from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemyAutoSchemaOpts

from database.db import Session

marshmallow = Marshmallow()  # noqa


class BaseOpts(SQLAlchemyAutoSchemaOpts):
    def __init__(self, meta, ordered=False):
        if not hasattr(meta, "sqla_session"):
            meta.sqla_session = Session
        super(BaseOpts, self).__init__(meta, ordered=ordered)
        self.load_instance = True
        self.include_fk = True


class ModelSchema(SQLAlchemyAutoSchema):
    OPTIONS_CLASS = BaseOpts
