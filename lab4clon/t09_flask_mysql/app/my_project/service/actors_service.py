# actors_service.py
from ..db import db  # <- це обов'язково
from ..dao.actors_dao import ActorsDAO

class ActorsService:
    @staticmethod
    def get_all_actors():
        return ActorsDAO.get_all_actors()

    @staticmethod
    def get_actor_by_id(actor_id):
        return ActorsDAO.get_actor_by_id(actor_id)

    @staticmethod
    def create_actor(first_name, last_name, birth_date, bio):
        return ActorsDAO.create_actor(first_name, last_name, birth_date, bio)

    @staticmethod
    def update_actor(actor_id, first_name, last_name, birth_date, bio):
        return ActorsDAO.update_actor(actor_id, first_name, last_name, birth_date, bio)

    @staticmethod
    def delete_actor(actor_id):
        return ActorsDAO.delete_actor(actor_id)


# Модель Actor прямо тут
class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date)
    bio = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date.isoformat() if self.birth_date else None,
            "bio": self.bio
        }
