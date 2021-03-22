from flask import request

from api.movie.schemas import movie_post_schema, movie_schema, movies_schema
from common.resources import ApiResource
from database.models import Movie


class MoviesApi(ApiResource):
    def get(self):
        movies = Movie.all()
        return movies_schema.dump(movies)

    def post(self):
        data = request.json
        movie = movie_post_schema.load(data)
        movie.insert()
        return movie_schema.dump(movie)


class MovieApi(ApiResource):
    def get(self, uuid):
        movie = Movie.query.get(uuid)
        return movie_schema.dump(movie)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
