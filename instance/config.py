import os


class Config(object):
    FLASK_ENV = "DEVELOPMENT"
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://udacity:BestPass2021!@localhost:5432/capstone"
    )
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = os.environ.get("FLASK_APP", "app.py")
    SECRET_KEY = os.environ.get("SECRET", "very-long-string-of-random-characters")


class Production(Config):
    FLASK_ENV = "PRODUCTION"


class Development(Config):
    FLASK_ENV = "DEVELOPMENT"
    FLASK_DEBUG = 1
    DEBUG = True
    SQLALCHEMY_ECHO = True


class Testing(Config):
    FLASK_ENV = "TESTING"
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://user:password@127.0.0.1:5105/test_db"
    )


class Docker(Config):
    FLASK_ENV = "DEVELOPMENT"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://udacity:BestPass2021!@postgres:5432/capstone"
    )


app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production,
    "docker": Docker,
}
