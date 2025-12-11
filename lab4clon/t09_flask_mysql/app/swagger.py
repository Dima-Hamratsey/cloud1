from flask import Blueprint
from flasgger import Swagger

swagger_bp = Blueprint('swagger_bp', __name__)

def init_swagger(app):
    swagger = Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": "Movies API",
            "description": "API for movies, actors, directors",
            "version": "1.0.0"
        },
        "basePath": "/"
    })
    return swagger
