from flask import Blueprint, request, jsonify
from t09_flask_mysql.app.my_project.service.actors_service import ActorsService

actors_bp = Blueprint("actors", __name__)
service = ActorsService()

@actors_bp.route('/', methods=['GET'])
def get_all_actors():
    actors = service.get_all_actors()
    return jsonify([actor.to_dict() for actor in actors])

@actors_bp.route('/<int:actor_id>', methods=['GET'])
def get_actor(actor_id):
    actor = service.get_actor_by_id(actor_id)
    if actor:
        return jsonify(actor.to_dict())
    return jsonify({"error": "Actor not found"}), 404

@actors_bp.route('/', methods=['POST'])
def create_actor():
    data = request.get_json()
    actor = service.create_actor(
        data.get("first_name"),
        data.get("last_name"),
        data.get("birth_date"),
        data.get("bio")
    )
    return jsonify(actor.to_dict()), 201

@actors_bp.route('/<int:actor_id>', methods=['PUT'])
def update_actor(actor_id):
    data = request.get_json()
    updated = service.update_actor(
        actor_id,
        data.get("first_name"),
        data.get("last_name"),
        data.get("birth_date"),
        data.get("bio")
    )
    if updated:
        return jsonify(updated.to_dict())
    return jsonify({"error": "Actor not found"}), 404

@actors_bp.route('/<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
    deleted = service.delete_actor(actor_id)
    if deleted:
        return jsonify({"message": "Actor deleted"})
    return jsonify({"error": "Actor not found"}), 404
