from flask import Flask
from .config import DevelopmentConfig
from .extensions import db, cors
from .routes.note_routes import note_bp


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)

    # Cargar configuración
    app.config.from_object(config_class)

    # Inicializar extensiones
    db.init_app(app)
    cors.init_app(app)

    # Registrar Blueprints (rutas)
    app.register_blueprint(note_bp)

    return app
