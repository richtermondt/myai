from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from app.config import Config

from .log_config import configure_logging

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    print("SECRET_KEY:", app.config.get('SECRET_KEY'))
    print("SQLALCHEMY_DATABASE_URI:", app.config.get('SQLALCHEMY_DATABASE_URI'))
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    configure_logging()

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
