from marshmallow import fields

from common.schemas import ModelSchema
from database.models import Actor


# Data Transformation Objects #
###############################
class ActorSchema(ModelSchema):
    class Meta:
        model = Actor

    movies = fields.Nested(
        "MovieSchema",
        many=True,
        exclude=[
            "actors",
        ],
    )


class ActorSchemaPost(ActorSchema):
    class Meta:
        model = Actor

    movie_uuid = fields.String()


actor_schema = ActorSchema()  # noqa
actors_schema = ActorSchema(many=True)  # noqa
actor_post_schema = ActorSchemaPost(
    exclude=[
        "uuid",
    ]
)  # noqa
