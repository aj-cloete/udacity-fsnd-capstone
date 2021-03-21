from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property

from database import db
from database.models.movie import Movie


class Actor(db.Model):
    def __init__(self, name, surname=None, age=None, gender=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    movie_uuid = db.Column(
        UUID(as_uuid=True), db.ForeignKey("movies.uuid"), nullable=True
    )
    name = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer(), nullable=True)
    gender = db.Column(db.String(1), nullable=True)
    movies = db.relationship(Movie, backref="actors")

    @hybrid_property
    def full_name(self):
        return f"{self.name} {self.surname}"
