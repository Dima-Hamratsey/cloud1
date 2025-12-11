from ..controller.directors_controller import directors_bp
from ..controller.actors_controller import actors_bp
from ..controller.movies_controller import movies_bp, movie_actor_bpp, movies_avg_duration, movies_random


def register_routes(app):

    app.register_blueprint(directors_bp, url_prefix='/directors')
    app.register_blueprint(actors_bp, url_prefix='/actors')
    app.register_blueprint(movies_bp, url_prefix='/movies')
    app.register_blueprint(movie_actor_bpp, url_prefix='/movies/movie_actor_insert')
    app.register_blueprint(movies_avg_duration, url_prefix='/movies/avg_movie_duration')
    app.register_blueprint(movies_random, url_prefix='/movies/random_actors')
