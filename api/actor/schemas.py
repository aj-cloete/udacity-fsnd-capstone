from common.schemas import ModelSchema
from database.models import Actor


# Data Transformation Objects #
###############################
class ActorSchema(ModelSchema):
    class Meta:
        model = Actor
        include_relationships = True
        load_instance = True
