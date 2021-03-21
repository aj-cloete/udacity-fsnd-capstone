from common.schemas import ModelSchema
from database.models import Movie


# Data Transformation Objects #
###############################
class MovieSchema(ModelSchema):
    class Meta:
        model = Movie
        include_relationships = True
        load_instance = True
