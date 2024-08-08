from app import create_app
from dotenv import load_dotenv
import os

load_dotenv('.flaskenv')

print("DATABASE_URL from .flaskenv:", os.getenv('DATABASE_URL'))

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)