# First flask app

from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template

# A minimal application
app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Index Page"

# @app.route("/hello")
# def hello_world():
#     return "Hello World!"
#
# # HTML escaping
# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

# Variable rules
# @app.route("/user/<username>")
# def show_user_profile(username):
#     # show the user profile for that user
#     return f"User {escape(username)}"

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

# URL building
@app.route("/")
def index():
    return "index"

# @app.route("/login")
# def login():
#     return "login"

@app.route("/user/<username>")
def profile(username):
    return f"{username}\'s profile"

with app.test_request_context():
    print(url_for("index"))
    # print(url_for("login"))
    # print(url_for("login", next="/"))
    print(url_for("profile", username="Bishal Poudel"))

# # HTTP method
# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()

# # static files
# url_for("static", filename="style.css")

# rendering templates
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)

# context locals
with app.test_request_context("/hello", method="POST"):
    assert request.path == "/hello"
    assert request.method == "POST"

# The request object
@app.route("/login", methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"],
                       request.form["password"]):
            return log_the_user_in(request.form["username"])
        else:
            error = "Invalid username/password"
    # execute if request method was GET or credentials were invalid
    return render_template("login.html", error=error)