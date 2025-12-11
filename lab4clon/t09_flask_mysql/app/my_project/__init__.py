import os
import yaml
from flask import Flask
from flasgger import Swagger
from t09_flask_mysql.app.my_project.db import db
from t09_flask_mysql.app.my_project.route import register_routes


def load_config():
    flask_env = os.getenv('FLASK_ENV', 'development').lower()
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'app.yml')

    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)

    return config.get(flask_env, config['development'])


def create_app():
    app = Flask(__name__)

    # Load config from YAML
    config = load_config()
    app.config.update(config)

    # Init DB
    db.init_app(app)

    # ─────────────────────────────────────────────
    #                SWAGGER CONFIG
    # ─────────────────────────────────────────────
    app.config['SWAGGER'] = {
        'title': 'Movie Actors API',
        'uiversion': 3
    }

    Swagger(app)  # ← Підключення Swagger UI
    # http://localhost:5000/apidocs

    # Register routes (Blueprints)
    register_routes(app)

    return app


if __name__ == '__main__':
    app = create_app()

    # Create tables
    with app.app_context():
        db.create_all()

    app.run(debug=app.config.get('DEBUG', True))
