from ..dao.directors_dao import DirectorsDAO
from ..db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

class DirectorsService:
    @staticmethod
    def get_all():
        directors = DirectorsDAO.get_all_directors()
        return [director.to_dict() for director in directors]

    @staticmethod
    def get_by_id(director_id):
        director = DirectorsDAO.get_director_by_id(director_id)
        return director.to_dict() if director else None

    @staticmethod
    def create(data):
        director = DirectorsDAO.create_director(
            data.get("first_name"),
            data.get("last_name"),
            data.get("bio")
        )
        return director.to_dict()

    @staticmethod
    def update(director_id, data):
        director = DirectorsDAO.update_director(
            director_id,
            data.get("first_name"),
            data.get("last_name"),
            data.get("bio")
        )
        return director.to_dict() if director else None

    @staticmethod
    def delete(director_id):
        return DirectorsDAO.delete_director(director_id)

    @staticmethod
    def call_insert_dummy_directors():
        try:
            db.session.execute(text("CALL insert_dummy_directors()"))
            db.session.commit()
            return {"message": "10 dummy directors inserted successfully"}
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}
