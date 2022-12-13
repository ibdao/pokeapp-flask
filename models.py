"""Models for pokeapp."""
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt

db = SQLAlchemy()

class User(db.Model):
    """User in the system"""
    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key = True
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


class Pokemon(db.Model):
    """Pokemon in the system"""
    __tablename__ = 'pokemons'



def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)