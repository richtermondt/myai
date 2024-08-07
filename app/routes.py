from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from app.handler import openai_handler

# Create a Blueprint named 'main'
main = Blueprint('main', __name__)

# Define the index route
@main.route('/', methods =["GET", "POST"])
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
def profile():
    return render_template('profile.html', name=current_user.name)

