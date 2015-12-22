from flask_wtf import Form # pragma: no cover
from wtforms import TextField, TextAreaField # pragma: no cover
from wtforms.validators import DataRequired, Length # pragma: no cover


class MessageForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=140)])


