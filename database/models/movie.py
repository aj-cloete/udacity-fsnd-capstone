from database import db
from database.models.actor import movies_actors


class Movie(db.Model):
    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    title = db.Column(db.String(64), nullable=False, unique=True)
    release_date = db.Column(db.Date(), nullable=False, unique=False)
    actors = db.relationship("Actor", secondary=movies_actors, back_populates="movies")
