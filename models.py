"""Models for pokeapp."""
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

class User(db.Model):
    """User in the system"""
    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    password = db.Column(
        db.Text,
        nullable=False
    )

    total_exp = db.Column(
        db.Integer,
        default=0,
    )

    pokemons = db.relationship('Pokemon', backref='user')

    @classmethod
    def signup(cls, username, password):
        """Sign up user, hash password and adds user to system"""
        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            password=hashed_pwd
        )

        db.session.add(user)
        return user
    
    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If this can't find matching user (or if password is wrong), returns
        False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False


class Pokemon(db.Model):
    """Pokemon in the system"""

    __tablename__ = 'pokemons'

    id = db.Column(
        db.Integer,
        primary_key=True 
    )

    name = db.Column(
        db.Text,
        nullable=False
    )

    exp = db.Column(
        db.Integer
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='CASCADE')
    )





def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)