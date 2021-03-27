from flask import Blueprint, request

from api.movie.schemas import movie_post_schema, movie_schema, movies_schema
from common.resources import Api, ApiResource
from database.models import Actor, Movie

movie_bp = Blueprint("movie_bp", __name__)
api = Api(movie_bp)


class MoviesApi(ApiResource):
    def get(self):
        movies = Movie.all()
        return movies_schema.dump(movies)

    def post(self):
        data = request.form or request.json or request.data
        movie = movie_post_schema.load(data)

        actor_uuid = data.get("actor_uuid")
        if actor_uuid:
            if isinstance(actor_uuid, str):
                actor_uuid = [actor_uuid]
            for uuid in actor_uuid:
                actor = Actor.query.get(uuid)
                movie.actors.append(actor)
        movie.insert()
        return movie_schema.dump(movie)


class MovieApi(ApiResource):
    def get(self, uuid):
        movie = Movie.query.get(uuid)
        return movie_schema.dump(movie)

    def patch(self, uuid):
        movie = Movie.query.get(uuid)
        data = request.form or request.json or request.data
        movie.update(data)
        return movie_schema.dump(movie)

    def delete(self, uuid):
        movie = Movie.query.get(uuid)
        movie_uuid = str(movie.uuid)
        movie.delete()
        return movie_uuid


api.add_resource(MoviesApi, "/")
api.add_resource(MovieApi, "/<uuid>")
