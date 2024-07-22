from flask import Flask
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    swagger = Swagger(app)
    
    from .routes.static import static_bp
    app.register_blueprint(static_bp, url_prefix='/static')

    from .routes.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
