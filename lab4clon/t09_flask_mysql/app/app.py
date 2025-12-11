from flask import Flask
import os
import yaml
from t09_flask_mysql.app.swagger import init_swagger
from t09_flask_mysql.app.my_project.db import db
from t09_flask_mysql.app.my_project.route import register_routes  # Переконайся, що route.py є в папці my_project


def load_config():
    flask_env = os.getenv('FLASK_ENV', 'development').lower()
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'app.yml')

    with open(config_path, 'r') as config_file:
        config = yaml.safe_load(config_file)

    # Повертаємо конфіг для потрібного середовища
    return config.get(flask_env, config['development'])


def create_app():
    app = Flask(__name__)

    # Load config
    config = load_config()
    app.config.update(config)

    # Init DB
    db.init_app(app)

    # Swagger config
    app.config['SWAGGER'] = {
        'title': 'Movies API',
        'uiversion': 3
    }

    # Підключаємо Swagger через локальну функцію
    init_swagger(app)

    # Register routes (Blueprints)
    register_routes(app)

    # Автоматичне створення таблиць
    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config.get('DEBUG', True))
