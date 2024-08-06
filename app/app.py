# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request
from handler import openai_handler

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/',  methods =["GET", "POST"])
# ‘/’ URL is bound with hello_world() function.
def index():
    if request.method == "POST":
        print("POST")
        query = request.form.get("query")
        reply = openai_handler.chat(query)
        print(query + " " + reply)
        return render_template("index.html", reply=reply)
    else:
        return render_template("index.html")

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()