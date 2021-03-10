from flask import Flask
from . import db_engine
from .blueprint.integration import bp
from flask import current_app, g
from flask_restful import Api
from .api.routes import initialize_routes


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('application.config.DevelopmentConfig')
    # Initialize Plugins
    db_engine.init_app(app)
    # r.init_app(app)
    @app.before_request
    def before_request():
        g.db = db_engine.connect_engine(app.config['DATABASE_URI'])

    with app.app_context():
        # Register Blueprints
        app.register_blueprint(bp)
        # Init api
        api = Api(app)
        initialize_routes(api)

        return app




