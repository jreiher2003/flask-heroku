from flask_wtf import Form # pragma: no cover
from wtforms import TextField, PasswordField # pragma: no cover
from wtforms.validators import DataRequired, Length, Email, EqualTo # pragma: no cover


class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(Form):
    username = TextField('username', validators=[DataRequired(), Length(min=3, max=25)])
    email = TextField('email', validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6, max=25)])
    confirm = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])