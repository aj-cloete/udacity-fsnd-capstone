from flask import request

from api.actor.schemas import (
    ActorSchema,
    actor_post_schema,
    actor_schema,
    actors_schema,
)
from common.resources import ApiResource
from database.models import Actor


class ActorsApi(ApiResource):
    def get(self):
        actors = Actor.all()
        return actors_schema.dump(actors)

    def post(self):
        data = request.json
        actor = actor_post_schema.load(data)
        actor.insert()
        return actor_schema.dump(actor)

    def put(self):
        pass

    def delete(self):
        pass


class ActorApi(ApiResource):
    def get(self, uuid):
        actor = Actor.query.get(uuid)
        return ActorSchema().dump(actor)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
