from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class CSRFProtection(FlaskForm):
    """CSRFProtection form, left blank."""

class UserAddForm(FlaskForm):
    """Form for adding users"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    """Form for logging in users"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])