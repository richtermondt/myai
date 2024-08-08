import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from app.config import Config

from .log_config import configure_logging

db = SQLAlchemy()
login_manager = LoginManager()

logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    logger.info("Database initialized")

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    logger.info("Login manager initialized")

    configure_logging()
    logger.info("Logging configured")

    logger.info("App configuration:")
    logger.info("SQLALCHEMY_DATABASE_URI: %s",
                app.config.get('SQLALCHEMY_DATABASE_URI'))

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
