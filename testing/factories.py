import random

import factory

from common.testing import BaseFactory
from database.models import Actor, Movie


class MovieFactory(BaseFactory):
    class Meta:
        model = Movie

    title = factory.Faker("sentence")
    release_date = factory.Faker("date")


class MovieActorFactory(BaseFactory):
    class Meta:
        model = Movie

    title = factory.Faker("sentence")
    release_date = factory.Faker("date")
    actors = factory.SubFactory("database.models.actor.ActorFactory")


class ActorFactory(BaseFactory):
    class Meta:
        model = Actor

    name = factory.Faker("name")
    surname = factory.Faker("name")
    age = factory.Faker("pyint")
    gender = factory.LazyAttribute(lambda x: random.choice(["M", "F"]))


class ActorMovieFactory(BaseFactory):
    class Meta:
        model = Actor

    name = factory.Faker("name")
    surname = factory.Faker("surname")
    age = factory.Faker("age")
    gender = factory.Faker("gender")
    movies = factory.SubFactory("database.models.movie.MovieFactory")
