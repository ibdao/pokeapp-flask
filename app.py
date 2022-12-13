import os
from dotenv import load_dotenv
from flask import Flask, request, redirect, render_template, g, session, flash
from models import db, connect_db, User
from forms import UserAddForm, CSRFProtection, LoginForm
from sqlalchemy.exc import IntegrityError

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ['DATABASE_URL'].replace("postgres://", "postgresql://"))
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

CURR_USER = "curr_user"

############################################################################
# User signup/login/logout

@app.before_request
def add_user_to_g():
    """If user is logged in, add curr user to Flask global."""
    
    if CURR_USER in session:
        g.user = User.query.get(session[CURR_USER])
    else:
        g.user = None

@app.before_request
def add_csrf_only_form():
    """Add a CSRF-only form so that ever route can use it"""
    g.csrf_form = CSRFProtection()

def do_logout():
    """Log out user"""
    if CURR_USER in session:
        del session[CURR_USER]

def do_login(user):
    """Login user"""
    session[CURR_USER] = user.id


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login and redirect to homepage on success"""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(
            form.username.data,
            form.password.data,
        )

        if user:
            do_login(user)
            return redirect('/')
    return render_template('users/login.html', form=form)

@app.post('/logout')
def logout():
    """Handle logout of user and redirect to homepage."""

    do_logout()
    return redirect('/')
#############################################################################
# Homepage routes

@app.get("/")
def homepage():
    """Homepage of site; redirect to register."""
    if g.user:
        return render_template('home.html')
    else:
        return render_template('home-anon.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Add user to database"""
    if CURR_USER in session:
        del session[CURR_USER]

    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data
            )
            db.session.commit()
        
        except IntegrityError:
            flash('Username already taken', 'danger')
            return render_template('users/signup.html', form=form)
        
        do_login(user)
        return redirect('/')
    else:
        return render_template('users/signup.html', form=form)
