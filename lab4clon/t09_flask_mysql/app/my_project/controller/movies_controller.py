from flask import Blueprint, request, jsonify
from t09_flask_mysql.app.my_project.service.movies_service import MoviesService

movies_bp = Blueprint("movies", __name__)
movie_actor_bpp = Blueprint("movie_actor", __name__)
movies_avg_duration = Blueprint("movies_avg_duration", __name__)
movies_random = Blueprint("movies_random", __name__)

service = MoviesService()


# =======================
#       MOVIES CRUD
# =======================

@movies_bp.route('/', methods=['GET'])
def get_all_movies():
    """
    Get all movies
    ---
    tags:
      - Movies
    responses:
      200:
        description: List of movies
    """
    return jsonify(service.get_all())


@movies_bp.route('/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    """
    Get movie by ID
    ---
    tags:
      - Movies
    parameters:
      - name: movie_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Movie found
      404:
        description: Not found
    """
    movie = service.get_by_id(movie_id)
    if movie:
        return jsonify(movie)
    return jsonify({"error": "Movie not found"}), 404


@movies_bp.route('/', methods=['POST'])
def create_movie():
    """
    Create a new movie
    ---
    tags:
      - Movies
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            title:
              type: string
            duration:
              type: integer
            director_id:
              type: integer
    responses:
      201:
        description: Created
    """
    data = request.get_json()
    return jsonify(service.create(data)), 201


@movies_bp.route('/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    """
    Update movie
    ---
    tags:
      - Movies
    parameters:
      - name: movie_id
        in: path
        type: integer
      - in: body
        name: body
        schema:
          type: object
    responses:
      200:
        description: Updated
      404:
        description: Not found
    """
    data = request.get_json()
    updated = service.update(movie_id, data)
    if updated:
        return jsonify(updated)
    return jsonify({"error": "Movie not found"}), 404


@movies_bp.route('/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    """
    Delete movie
    ---
    tags:
      - Movies
    responses:
      200:
        description: Deleted
      404:
        description: Not found
    """
    deleted = service.delete(movie_id)
    if deleted:
        return jsonify({"message": "Movie deleted"})
    return jsonify({"error": "Movie not found"}), 404



# ========================================
#   INSERT ACTOR → MOVIE RELATION
# ========================================

@movie_actor_bpp.route('/', methods=['POST'])
def add_actor_to_movie():
    """
    Add actor to movie
    ---
    tags:
      - Movies
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            movie_id:
              type: integer
            actor_id:
              type: integer
    responses:
      201:
        description: Relation created
    """
    data = request.get_json()
    return jsonify(service.add_actor(data)), 201



# ========================================
#   AVERAGE MOVIE DURATION
# ========================================

@movies_avg_duration.route('/', methods=['GET'])
def avg_movie_duration():
    """
    Get average movie duration
    ---
    tags:
      - Movies
    responses:
      200:
        description: Average duration
    """
    return jsonify(service.get_avg_duration())



# ========================================
#   RANDOM ACTORS FROM MOVIES
# ========================================

@movies_random.route('/', methods=['GET'])
def random_actors():
    """
    Get random actors from movies
    ---
    tags:
      - Movies
    responses:
      200:
        description: Random actors
    """
    return jsonify(service.get_random_actors())
