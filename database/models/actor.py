from sqlalchemy import Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property

from database import db

movies_actors = Table(
    "movies_actors",
    db.Model.metadata,
    db.Column("actor_uuid", UUID(as_uuid=True), db.ForeignKey("actors.uuid")),
    db.Column("movie_uuid", UUID(as_uuid=True), db.ForeignKey("movies.uuid")),
)


class Actor(db.Model):
    def __init__(self, name, surname=None, age=None, gender=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    name = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer(), nullable=True)
    gender = db.Column(db.String(1), nullable=True)
    movies = db.relationship("Movie", secondary=movies_actors, back_populates="actors")

    @hybrid_property
    def full_name(self):
        return f"{self.name} {self.surname}"
