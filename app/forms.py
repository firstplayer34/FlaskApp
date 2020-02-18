from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    taskNumber = StringField("Номер задания", validators=[DataRequired()])
    submit = SubmitField("Подтвердить")
