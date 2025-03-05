from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from app.routes.libro_routes import libro_bp
from app.routes.usuario_routes import usuario_bp
from app.routes.prestamo_routes import prestamo_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Registrar blueprints
    app.register_blueprint(libro_bp, url_prefix='/api')
    app.register_blueprint(usuario_bp, url_prefix='/api')
    app.register_blueprint(prestamo_bp, url_prefix='/api')

    # Configuración de Swagger UI
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Sistema de Biblioteca"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app