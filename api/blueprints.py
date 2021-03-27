from api.actor.resources import actor_bp
from api.docs.resources import docs_bp
from api.movie.resources import movie_bp


def register_blueprints(app):
    app.register_blueprint(actor_bp, url_prefix="/actors")
    app.register_blueprint(docs_bp)
    app.register_blueprint(movie_bp, url_prefix="/movies")
