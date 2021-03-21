from api.actor.resources import ActorApi, ActorsApi
from api.movie.resources import MovieApi, MoviesApi


def register_blueprints(api):
    api.add_resource(MoviesApi, "/movies")
    api.add_resource(MovieApi, "/movies/<uuid>")
    api.add_resource(ActorsApi, "/actors")
    api.add_resource(ActorApi, "/actors/<uuid>")
