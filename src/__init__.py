from flask import Flask
import db_engine
from bp.integration import bp
from resource.integration import api_integration
from flask import current_app, g

# from flask_sqlalchemy import SQLAlchemy


# Globally accessible libraries
# db = SQLAlchemy()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.Config')

    # Initialize Plugins
    db_engine.init_app(app)
    # r.init_app(app)
    @app.before_request
    def before_request():
        g.db = db_engine.connect_engine()

    with app.app_context():
        # Include our Routes
        # from . import routes

        # Register Blueprints
        app.register_blueprint(bp)
        # Init api
        api_integration.init_app(app)

        return app




