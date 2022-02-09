import flask_wtf
import wtforms
from wtforms.widgets import NumberInput


class Form(flask_wtf.FlaskForm):
    username = wtforms.StringField("Name", [wtforms.validators.Length(min=4, max=11), wtforms.validators.DataRequired()])
    password = wtforms.PasswordField("Password", [wtforms.validators.DataRequired()])
    bio = wtforms.StringField("Bio")
    submit = wtforms.SubmitField("Submit")

class Inscription_Form(flask_wtf.FlaskForm):
    first_name = wtforms.StringField("Enter your First Name", [wtforms.validators.Length(min=4, max=11), wtforms.validators.DataRequired()])
    last_name = wtforms.StringField("Enter your Last Name", [wtforms.validators.Length(min=4, max=11), wtforms.validators.DataRequired()])
    age = wtforms.IntegerField('Select your age' )
    submit = wtforms.SubmitField("Send")

#wsgi : web server gateway interface
