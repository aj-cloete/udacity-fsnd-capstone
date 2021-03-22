from marshmallow import fields

from common.schemas import ModelSchema
from database.models import Movie


# Data Transformation Objects #
###############################
class MovieSchema(ModelSchema):
    class Meta:
        model = Movie

    actors = fields.Nested(
        "ActorSchema",
        many=True,
        exclude=[
            "movies",
        ],
    )


class MovieSchemaPost(MovieSchema):
    class Meta:
        model = Movie

    actor_uuid = fields.String()


movie_schema = MovieSchema()  # noqa
movies_schema = MovieSchema(many=True)  # noqa
movie_post_schema = MovieSchema(
    exclude=[
        "uuid",
    ]
)  # noqa
