from flask_sqlalchemy import Model
from sqlalchemy import Column, MetaData, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr

# Naming conventions so that Alembic doesn't get confused.
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)


class UUIDMixin:
    @declared_attr
    def uuid(self):
        return Column(
            UUID(as_uuid=True),
            primary_key=True,
            server_default=text("UUID(gen_random_uuid())"),
            unique=True,
            nullable=False,
        )


class BaseModel(Model, UUIDMixin):
    @classmethod
    def all(cls):
        """
        Get all model instances
        :return: list of all model instances
        """
        return cls.query.all()

    @declared_attr
    def __tablename__(self):
        return f"{self.__name__.lower()}s"
