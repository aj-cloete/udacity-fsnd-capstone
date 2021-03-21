from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchemaOpts

from database.db import Session

marshmallow = Marshmallow()  # noqa


class BaseOpts(SQLAlchemySchemaOpts):
    def __init__(self, meta, ordered=False):
        if not hasattr(meta, "sqla_session"):
            meta.sqla_session = Session
        super(BaseOpts, self).__init__(meta, ordered=ordered)

    include_fk = None
    include_relationships = None


class ModelSchema(SQLAlchemyAutoSchema):
    OPTIONS_CLASS = BaseOpts
