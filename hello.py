# First flask app

from flask import Flask
from markupsafe import escape

# A minimal application
app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/hello")
def hello_world():
    return "Hello World!"

# HTML escaping
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

# Variable rules
@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return f"User {escape(username)}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id
    return f"Post {post_id}"

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"

# Unique URLs/ redirection behaviour
@app.route("/projects/")
def projects():
    return "This is project page"

@app.route("/about")
def about():
    return "This is about page"