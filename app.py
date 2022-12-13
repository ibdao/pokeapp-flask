from flask import Flask, request, redirect, render_template, g
from models import db, connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pokeapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

############################################################################
# User signup/login/logout

@app.before_request
def add_user_to_g():
    """If user is logged in, add curr user to Flask global."""

@app.before_request
def add_csrf_only_form():
    """Add a CSRF-only form so that ever route can use it"""

def do_logout():
    """Log out user"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login and redirect to homepage on success"""


@app.post('/logout')
def logout():
    """Handle logout of user and redirect to homepage."""

    do_logout()
#############################################################################
# Homepage routes

@app.get("/")
def homepage():
    """Homepage of site; redirect to register."""

    return redirect("/register")