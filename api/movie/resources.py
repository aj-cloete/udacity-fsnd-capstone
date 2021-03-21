from api.movie.schemas import MovieSchema
from common.resources import ApiResource
from database.models import Movie


class MoviesApi(ApiResource):
    def get(self):
        movies = Movie.all()
        return MovieSchema(many=True).dump(movies)

    def post(self):
        # movie = Movie(title=title, release_date=release_date)
        # movie.insert()
        pass

    def put(self):
        pass

    def delete(self):
        pass


class MovieApi(ApiResource):
    def get(self, uuid):
        movie = Movie.query.get(uuid)
        return MovieSchema().dump(movie)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
