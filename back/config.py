import os

# Clase base con configuraciones comunes
class Config:
    # Clave secreta (usada para sesiones, formularios, etc.)
    SECRET_KEY = os.environ.get("SECRET_KEY", "clave_por_defecto_segura")

    # Configuración de la base de datos (por defecto SQLite)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///smartnotes.db"
    )

    # Desactiva el rastreo de modificaciones (mejora el rendimiento)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Configuración para entorno de desarrollo
class DevelopmentConfig(Config):
    DEBUG = True


# Configuración para entorno de producción
class ProductionConfig(Config):
    DEBUG = False


# Configuración para entorno de pruebas
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
