from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from openai import OpenAI

from app.handler import openai_handler
from app.handler.openai_streamer import OpenAIStreamer

# Create a Blueprint named 'main'
main = Blueprint('main', __name__)

# Define the index route


@main.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("POST")
        query = request.form.get("query")
        reply = openai_handler.chat(query)
        print(query + " " + reply)
        return render_template("index.html", reply=reply)
    else:
        return render_template("index.html")


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/chat')
@login_required
def chat():
    return render_template('chat.html')


@main.route("/answer", methods=["GET", "POST"])
def answer():
    openai_streamer = OpenAIStreamer()
    data = request.get_json()
    message = data["message"]

    def generate():
        openai_streamer.chat(message)

    return generate(), {"Content-Type": "text/plain"}
