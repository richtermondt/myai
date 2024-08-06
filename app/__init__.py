from flask import Flask

def create_app():
    app = Flask(__name__)
    # Configure the app here if needed

    # Import the Blueprint
    from .routes import main as main_blueprint

    # Register the Blueprint
    app.register_blueprint(main_blueprint)

    return app