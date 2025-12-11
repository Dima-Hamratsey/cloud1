from flask import Flask
from swagger import init_swagger
from t09_flask_mysql.app.my_project.route import register_routes


def create_app():
    app = Flask(__name__)

    # Підключаємо Swagger
    init_swagger(app)

    # Підключаємо твої маршрути
    register_routes(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
