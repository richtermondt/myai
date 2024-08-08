from contextlib import contextmanager
from http import client
import logging
from flask import Blueprint, Response, current_app, render_template, request, stream_with_context
from flask_login import login_required, current_user
from openai import OpenAI

import app
from app.handler import openai_handler
from app.handler.openai_streamer import OpenAIStreamer

# Create a Blueprint named 'main'
main = Blueprint('main', __name__)

logger = logging.getLogger(__name__)

# Define the index route


@main.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        app.logger.info("POST request received")
        query = request.form.get("query")
        reply = openai_handler.chat(query)
        logger.info(f"Query: {query} Reply: {reply}")
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
    print("Current User:", current_user.get_id())
    logger.info(f"Current User: {current_user.get_id()}")
    return render_template('chat.html')


@main.route("/answer", methods=["GET", "POST"])
@login_required
def answer():
    data = request.get_json()
    message = data["message"]
    logger.info(f"Current User: {current_user.get_id()}")
    user_id = current_user.get_id()

    streamer = OpenAIStreamer()

    @stream_with_context
    def generate():
        response = streamer.chat(message, user_id)
        for res in response:
            yield res

    return Response(generate(), content_type="text/plain")
