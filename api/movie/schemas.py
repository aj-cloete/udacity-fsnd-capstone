from common.schemas import ModelSchema
from database.models import Movie


# Data Transformation Objects #
###############################
class MovieSchema(ModelSchema):
    class Meta:
        model = Movie


movie_schema = MovieSchema()  # noqa
movies_schema = MovieSchema(many=True)  # noqa
movie_post_schema = MovieSchema(
    exclude=[
        "uuid",
    ]
)  # noqa
