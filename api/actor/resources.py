from api.actor.schemas import ActorSchema
from common.resources import ApiResource
from database.models import Actor


class ActorsApi(ApiResource):
    def get(self):
        actors = Actor.all()
        return ActorSchema(many=True).dump(actors)

    def post(self):
        pass

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
