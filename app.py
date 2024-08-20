from app import create_app
from dotenv import load_dotenv
import os

load_dotenv('.flaskenv')

app = create_app()

if __name__ == "__main__":
    host = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_RUN_PORT", 5000))
    app.run(host=host, port=port, debug=True)
