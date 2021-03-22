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
        data = request.form or request.json or request.data
        actor = actor_post_schema.load(data)
        actor.insert()
        return actor_schema.dump(actor)


class ActorApi(ApiResource):
    def get(self, uuid):
        actor = Actor.query.get(uuid)
        return ActorSchema().dump(actor)

    def patch(self, uuid):
        actor = Actor.query.get(uuid)
        data = request.form or request.json or request.data
        actor.update(data)
        return actor_schema.dump(actor)

    def delete(self, uuid):
        actor = Actor.query.get(uuid)
        actor_uuid = str(actor.uuid)
        actor.delete()
        return actor_uuid
