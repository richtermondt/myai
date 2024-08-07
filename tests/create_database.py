# Add the project root directory to the Python path
import os
import sys

# Add the parent directory of the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()
    print("Tables created successfully.")