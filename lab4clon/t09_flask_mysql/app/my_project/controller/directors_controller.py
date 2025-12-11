from flask import Blueprint, request, jsonify
from ..service.directors_service import DirectorsService

directors_bp = Blueprint("directors", __name__)
service = DirectorsService()

@directors_bp.route('/', methods=['GET'])
def get_all_directors():
    return jsonify(service.get_all())

@directors_bp.route('/<int:director_id>', methods=['GET'])
def get_director(director_id):
    director = service.get_by_id(director_id)
    if director:
        return jsonify(director)
    return jsonify({"error": "Director not found"}), 404

@directors_bp.route('/', methods=['POST'])
def create_director():
    data = request.get_json()
    return jsonify(service.create(data)), 201

@directors_bp.route('/<int:director_id>', methods=['PUT'])
def update_director(director_id):
    data = request.get_json()
    updated = service.update(director_id, data)
    if updated:
        return jsonify(updated)
    return jsonify({"error": "Director not found"}), 404

@directors_bp.route('/<int:director_id>', methods=['DELETE'])
def delete_director(director_id):
    deleted = service.delete(director_id)
    if deleted:
        return jsonify({"message": "Director deleted"})
    return jsonify({"error": "Director not found"}), 404
