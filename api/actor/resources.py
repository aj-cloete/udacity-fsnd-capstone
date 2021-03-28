from flask import Blueprint, request

from api.actor.schemas import actor_post_schema, actor_schema, actors_schema
from auth.auth import requires_auth
from common.resources import Api, ApiResource
from database.models import Actor, Movie

actor_bp = Blueprint("actor_bp", __name__)
api = Api(actor_bp)


class ActorsApi(ApiResource):
    @requires_auth("get:actors")
    def get(self):
        actors = Actor.all()
        return actors_schema.dump(actors)

    @requires_auth("post:actors")
    def post(self):
        data = request.form or request.json or request.data
        actor = actor_post_schema.load(data)
        movie_uuid = data.get("movie_uuid")
        if movie_uuid:
            if isinstance(movie_uuid, str):
                movie_uuid = [movie_uuid]
            for uuid in movie_uuid:
                movie = Movie.query.get(uuid)
                actor.movies.append(movie)
        actor.insert()
        return actor_schema.dump(actor)


class ActorApi(ApiResource):
    @requires_auth("get:actors")
    def get(self, uuid):
        actor = Actor.query.get(uuid)
        return actor_schema.dump(actor)

    @requires_auth("patch:actors")
    def patch(self, uuid):
        actor = Actor.query.get(uuid)
        data = request.form or request.json or request.data
        actor.update(data)
        return actor_schema.dump(actor)

    @requires_auth("delete:actors")
    def delete(self, uuid):
        actor = Actor.query.get(uuid)
        actor_uuid = str(actor.uuid)
        actor.delete()
        return actor_uuid


api.add_resource(ActorsApi, "/")
api.add_resource(ActorApi, "/<uuid>")
