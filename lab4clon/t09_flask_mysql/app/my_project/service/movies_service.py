# t09_flask_mysql/app/my_project/service/movies_service.py
from t09_flask_mysql.app.my_project.dao.movies_dao import MoviesDAO
from t09_flask_mysql.app.my_project.db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

class MoviesService:

    @staticmethod
    def get_all():
        movies = MoviesDAO.get_all_movies()
        return [movie.to_dict() for movie in movies]

    @staticmethod
    def get_by_id(movie_id):
        movie = MoviesDAO.get_movie_by_id(movie_id)
        return movie.to_dict() if movie else None

    @staticmethod
    def create(data):
        movie = MoviesDAO.create_movie(
            data.get("title"),
            data.get("description"),
            data.get("release_date"),
            data.get("duration"),
            data.get("genre_id"),
            data.get("director_id")
        )
        return movie.to_dict()

    @staticmethod
    def update(movie_id, data):
        movie = MoviesDAO.update_movie(
            movie_id,
            data.get("title"),
            data.get("description"),
            data.get("release_date"),
            data.get("duration"),
            data.get("genre_id"),
            data.get("director_id")
        )
        return movie.to_dict() if movie else None

    @staticmethod
    def delete(movie_id):
        return MoviesDAO.delete_movie(movie_id)

    # =======================
    #        RELATIONS
    # =======================
    @staticmethod
    def add_actor(data):
        movie_title = data.get("movie_title")
        actor_first_name = data.get("actor_first_name")
        actor_last_name = data.get("actor_last_name")
        role = data.get("role")
        try:
            db.session.execute(
                text("CALL insert_movie_actor(:movie_title, :actor_first_name, :actor_last_name, :role)"),
                {
                    "movie_title": movie_title,
                    "actor_first_name": actor_first_name,
                    "actor_last_name": actor_last_name,
                    "role": role
                }
            )
            db.session.commit()
            return {"message": "Actor added to movie successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}

    # =======================
    #        AGGREGATES
    # =======================
    @staticmethod
    def get_avg_duration():
        avg_duration = MoviesDAO.get_avg_movie_duration()
        if avg_duration is None:
            return {"message": "No movies found"}, 404
        return {"avg_movie_duration": avg_duration}

    @staticmethod
    def get_random_actors():
        actors = MoviesDAO.get_random_actors()
        return [actor.to_dict() for actor in actors]
